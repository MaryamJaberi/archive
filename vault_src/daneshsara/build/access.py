# -*- coding: utf-8 -*-
"""هر فایل صندوق را به یک سطح محرمانگی و یک حوزه نسبت می‌دهد.
اجرا:  python3 build/access.py [مسیر صندوق] [مسیر سایت عمومی]
خروجی: data/access/classify.json  (پنل همین را می‌خواند)
قاعده: اول override صریح، بعد قاعدهٔ مسیر، بعد هشدارهای محتوایی که سطح را بالا می‌برند.
هر فایلی که قاعده نداشته باشد سطح ۴ می‌گیرد — پیش‌فرض، بسته‌ترین حالت است، نه بازترین."""
import json, os, re, sys, collections, datetime

VAULT = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUBLIC = sys.argv[2] if len(sys.argv) > 2 else ''
MODEL = json.load(open(f'{VAULT}/data/access/model.json', encoding='utf-8'))

# قاعدهٔ مسیر: (الگو, سطح, حوزه, دلیل) — اولین تطبیق برنده است
RULES = [
    (r'^data/access/',            4, 'access',  'خودِ تنظیمات دسترسی'),
    (r'^core/panel\.html$',       4, 'access',  'پنل دسترسی'),
    (r'^data/simorgh/cheat-ledger\.json$', 4, 'raw', 'دفتر تقلب نظرسنجی: نقشهٔ حرکت‌های ممکن'),
    (r'^data/ideas/',             4, 'raw',     'ایده‌های خام مردم'),
    (r'^data/sakht/ideas_bodies\.json$', 4, 'raw', 'متن خام ایده‌ها'),
    (r'^simorgh/poll\.html$',     3, 'poll',    'نظرسنجی: روش و دفتر یکجا'),
    (r'^simorgh/plan\.html$',     3, 'plan',    'نقشهٔ کلان و تصمیم‌های نگرفته'),
    (r'^simorgh/circle\.html$',   3, 'plan',    'میز حلقه'),
    (r'^simorgh/archive\.html$',  3, 'plan',    'فهرست همهٔ صفحه‌های خصوصی'),
    (r'^simorgh/entries\.html$',  3, 'plan',    'فهرست مدخل‌های خصوصی'),
    (r'^sakht/(work|day)\.html$', 3, 'sakht',   'میز کار و روز بعد: برنامهٔ اجرا'),
    (r'^data/sakht/(work|day)\.json$', 3, 'sakht', 'دادهٔ برنامهٔ اجرا'),
    (r'^data/plan/',              3, 'plan',    'دادهٔ نقشه و عقب‌مانده‌ها'),
    (r'^data/status\.json$',       3, 'plan',    'وضعیت همهٔ کارها'),
    (r'^data/tests\.json$',        3, 'work',    'فهرست تست‌ها'),
    (r'^core/tests\.html$',        3, 'work',    'صفحهٔ تست‌ها'),
    (r'^wellbeing/',              3, 'work',    'کار با همکاران'),
    (r'^sakht/',                  2, 'sakht',   'ساخت ایران: محتوای نیمه‌تمام'),
    (r'^data/sakht/',             2, 'sakht',   'دادهٔ ساخت ایران'),
    (r'^iran/',                   2, 'iran',    'ویکی ایران'),
    (r'^simorgh/(birds|why|sim|transitions|index)\.html$', 2, 'simorgh', 'ویکی سیمرغ'),
    (r'^data/simorgh/',           2, 'simorgh', 'مدخل‌های سیمرغ'),
    (r'^simorgh/par/(docs|old|files)/', 2, 'par', 'پیش‌نویس‌ها و نسخه‌های قدیمی پَرِ سیمرغ'),
    (r'^simorgh/par/',            1, 'par',     'پَرِ سیمرغ: همان نسخهٔ اشتراکی'),
    (r'^build/',                  3, 'work',    'ابزار ساخت'),
    (r'^core/',                   2, 'work',    'مشترک'),
    (r'^data/(soc|psy|phil|tabar|tarikh)/', 0, 'par', 'لایهٔ علمی، عمومی است'),
    (r'^atlas/',                  0, 'par',     'روی سایت عمومی هم هست'),
    (r'^data/coverage\.json$',    0, 'par',     'پوشش لایهٔ علمی، عمومی است'),
    (r'^data/library/',           2, 'work',    'صف و سرنخ منابع'),
]

# هشدارهای محتوایی: اگر در فایل باشند سطح را دست‌کم به این عدد می‌برند
FLAGS = [
    (r'\b(?:[\w.+-]+@[\w-]+\.[\w.]+)\b', 4, 'نشانی ایمیل'),
    (r'github_pat_|ghp_|sk-[A-Za-z0-9]{20}|BEGIN (?:RSA |OPENSSH )?PRIVATE KEY', 4, 'کلید یا توکن'),
    (r'\+۹۸|\+98\d{8}', 4, 'شمارهٔ تماس'),
]
SKIP_FLAG = re.compile(r'^(?:build/|core/panel)')  # ابزارها خودشان الگو دارند، نه داده

over_path = f'{VAULT}/data/access/overrides.json'
OVER = json.load(open(over_path, encoding='utf-8')) if os.path.exists(over_path) else {}

def classify(rel, text):
    if rel in OVER:
        o = OVER[rel]; return o['level'], o.get('area', '—'), o.get('why', 'دستیِ خودم'), True
    for pat, lvl, area, why in RULES:
        if re.search(pat, rel):
            if not SKIP_FLAG.match(rel):
                for fpat, flvl, fwhy in FLAGS:
                    if re.search(fpat, text) and flvl > lvl:
                        return flvl, area, f'{why} — ولی {fwhy} دارد، پس بالا رفت', False
            return lvl, area, why, False
    return 4, '—', 'قاعده‌ای ندارد؛ پیش‌فرض بسته‌ترین سطح', False

rows, unruled = [], []
for root, ds, fs in os.walk(VAULT):
    ds[:] = [d for d in ds if d not in ('.git', '__pycache__', 'node_modules')]
    for f in sorted(fs):
        if f.startswith('.'): continue
        p = os.path.join(root, f); rel = os.path.relpath(p, VAULT)
        try: text = open(p, encoding='utf-8', errors='ignore').read()
        except Exception: text = ''
        # نشانی‌های اینترنتی و url(...) را کنار بگذار تا wght@300 با ایمیل اشتباه نشود
        text = re.sub(r'https?://\S+|url\([^)]*\)', ' ', text)
        lvl, area, why, manual = classify(rel, text)
        t = re.search(r'<title>(.*?)</title>', text, re.S)
        rows.append({'path': rel, 'level': lvl, 'area': area, 'why': why, 'manual': manual,
                     'title': (t.group(1).split('|')[0].split('—')[0].strip() if t else ''),
                     'bytes': os.path.getsize(p)})
        if why.startswith('قاعده‌ای ندارد'): unruled.append(rel)

if PUBLIC and os.path.isdir(PUBLIC):
    for root, ds, fs in os.walk(PUBLIC):
        ds[:] = [d for d in ds if d not in ('.git', '__pycache__', 'node_modules', 'vault', 'share')]
        for f in sorted(fs):
            if f.endswith(('.html', '.json')) and not f.startswith('.'):
                rel = os.path.relpath(os.path.join(root, f), PUBLIC)
                rows.append({'path': rel, 'level': 0, 'area': 'par', 'why': 'روی سایت عمومی است',
                             'manual': False, 'title': '', 'bytes': 0, 'public': True})

by = collections.Counter(r['level'] for r in rows)
out = {'built': datetime.date.today().isoformat(), 'model_version': MODEL['version'],
       'counts': {str(k): v for k, v in sorted(by.items())}, 'rows': rows}
os.makedirs(f'{VAULT}/data/access', exist_ok=True)
json.dump(out, open(f'{VAULT}/data/access/classify.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
print(len(rows), 'فایل |', ' '.join(f'س{k}:{v}' for k, v in sorted(by.items())))
if unruled:
    print('بدون قاعده (سطح ۴ گرفتند):', len(unruled)); [print('  ', u) for u in unruled[:25]]
