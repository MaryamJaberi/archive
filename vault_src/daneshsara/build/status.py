# -*- coding: utf-8 -*-
"""یک فهرستِ واحد از همه‌چیزِ پروژه: هرچه ساخته شده، در کار است، مانده، یا منتظرِ مریم است.
منبعِ داشبوردِ «میز فرمان». شمارش‌ها از خودِ داده خوانده می‌شود؛ فهرستِ دستی فقط برای چیزهایی است که جای دیگری ثبت نشده.
اجرا: python3 build/status.py <public_daneshsara_dir> <vault_daneshsara_dir> <out.json>"""
import json, glob, os, sys, datetime

PUB, VAULT, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
SITE = 'https://maryamjaberi.github.io/'
DS = SITE + 'daneshsara/'
VL = DS + 'vault.html#'
load = lambda p: json.load(open(p, encoding='utf-8'))
reg = load(f'{PUB}/core/registry.json')
plan = load(f'{VAULT}/data/plan/plan.json')
ledger = load(f'{VAULT}/data/simorgh/cheat-ledger.json')
rows = []

def add(area, name, kind, status, where, link='', count=None, note='', stage=''):
    rows.append(dict(area=area, name=name, kind=kind, status=status, where=where,
                     count=count, note=note, stage=stage, link=link))

# ── ۱. دانش‌سرا: ویکی‌های عمومی ────────────────────────────────
A = 'دانش‌سرا'
ent = reg['entries']
def n(w, kind='concept'): return sum(1 for v in ent.values() if v['wiki'] == w and v['type'] == kind)
def rev(w): return sum(1 for v in ent.values() if v['wiki'] == w and v['type'] == 'concept' and v.get('status') == 'reviewed')
for w, t in [('psy', 'ویکی روان'), ('soc', 'ویکی جامعه'), ('phil', 'ویکی فلسفه'), ('tabar', 'ویکی تبار و ژنتیک'), ('tarikh', 'ویکی تاریخ و ایران‌شناسی')]:
    c, r = n(w), rev(w)
    add(A, t, 'ویکی', 'ساخته' if c > 60 else 'در کار', 'عمومی', DS + w + '/', c,
        f'{r} مدخل بازبینی‌شده، بقیه پیش‌نویس' if r else 'همه پیش‌نویس (منتظر بازبینی)')
st = reg['stats']
add(A, 'اطلس رشته‌ها و پل‌ها', 'ویکی', 'ساخته', 'عمومی', DS + 'atlas/', st['fields'], f"{st['bridges']} پل میان رشته‌ها")
add(A, 'آدم‌ها', 'داده', 'ساخته', 'عمومی', DS + 'core/people.html', st['people'])
add(A, 'منابع', 'داده', 'ساخته', 'عمومی', DS + 'core/sources.html', st['sources'], 'تکراری‌های کوران، کرزمن، چنووث و گمان هنوز یکی نشده‌اند')
add(A, 'پیوندهای میان ویکی‌ها', 'داده', 'ساخته', 'عمومی', DS, st['cross_wiki_links'])
for name, link, note in [
    ('بپرس از دانش‌سرا (جستجو)', 'core/ask.html', ''),
    ('آزمایشگاه‌ها', 'soc/tools/lab.html', 'برای جامعه، فلسفه و تاریخ'),
    ('از کجا شروع کنم؟ (مسیرهای راهنما)', 'soc/tools/path.html', ''),
    ('ریشه‌یابی آسیب', 'miyan/roots.html', ''),
    ('صف بازبینی مدخل‌ها', 'core/review.html', ''),
    ('فراخوان همکاری', 'call.html', ''),
]:
    add(A, name, 'ابزار', 'ساخته', 'عمومی', DS + link, note=note)

# ── ۲. صندوق: لایهٔ ایران، سیمرغ، ساخت ایران ───────────────────
I = 'لایهٔ ایران'
notes = [p for p in glob.glob(f'{VAULT}/iran/*.json')]
add(I, 'یادداشت‌های آماری ایران (دفتر ویرانی‌ها)', 'داده', 'در کار', 'صندوق', VL + 'iran/index.html', len(notes),
    'هر عدد با منبع و ردهٔ اعتبار؛ اقلیت‌ها و روابط خارجی هنوز داده ندارند')
add(I, 'اول حدس بزن: ایران در عدد', 'ابزار', 'ساخته', 'صندوق', VL + 'iran/tools/guess.html')

S = 'سیمرغ'
sim = glob.glob(f'{VAULT}/data/simorgh/concepts/*.json')
add(S, 'ویکی سیمرغ (مدخل‌ها)', 'ویکی', 'ساخته', 'صندوق + اشتراکی', VL + 'simorgh/entries.html', len(sim), 'شش بخش: بازی، شواهد، تاریخ، راهبرد، عمل، خودِ پروژه')
par = [p for p in glob.glob(f'{VAULT}/simorgh/par/**/*.html', recursive=True)]
add(S, 'همهٔ پَرِ سیمرغ (صفحه‌های اصلی)', 'صفحه', 'ساخته', 'صندوق + اشتراکی', VL + 'simorgh/archive.html', len(par), 'میز مافیا، ۴۷ نقش، متن کامل بازی، میز داده، سند راهبردی، ارائهٔ اروپا')
for f, t, note in [('plan.html', 'نقشهٔ کلان سیمرغ', 'پنج لایه، سهم من، سی مرغ، محصولات، نقشهٔ راه'),
                   ('birds.html', 'کارت‌های سی مرغ', ''), ('sim.html', 'شهر: بازی ده‌نوبته', 'نسخهٔ نخست'),
                   ('transitions.html', 'گذار در کشورهای دیگر', 'پانزده گذار'), ('why.html', 'چرا؟ علم پشت ۴۷ نقش', ''),
                   ('circle.html', 'میز حلقه (برگهٔ جلسه)', '')]:
    add(S, t, 'ابزار', 'ساخته', 'صندوق + اشتراکی', VL + 'simorgh/' + f, note=note)
add(S, 'نبضِ میز (نظرسنجی ماهانه)', 'ابزار', 'آمادهٔ انتشار', 'صندوق + اشتراکی', VL + 'simorgh/poll.html', None,
    'با انتشار سیمرغ باز می‌شود؛ نشانیِ کانال‌ها لازم است')
open_rows = [r for r in ledger.get('rows', []) if r.get('status') == 'باز']
add(S, 'دفتر تقلب (تیم قرمز و آبی)', 'داده', 'در کار', 'صندوق', VL + 'simorgh/poll.html', len(ledger.get('rows', [])),
    f'{len(open_rows)} حرکتِ باز، منتظر دورِ تیم آبی')
add(S, 'نسخهٔ اشتراکی برای آدم‌های مطمئن', 'صفحه', 'ساخته', 'اشتراکی', SITE + 'simorgh/', None, 'رمز جدا؛ هر روز خودکار به‌روز می‌شود')

K = 'ساخت ایران'
for f, t, stt, note in [('work.html', 'صندلی‌های خالی (میز کار متخصص‌ها)', 'ساخته', ''),
                        ('day.html', 'روز بعد و جشن', 'در کار', ''),
                        ('map.html', 'نقشهٔ خرابی‌ها', 'آمادهٔ انتشار', 'نشانی My Maps لازم است؛ عمومی نمی‌شود تا ایمنی‌اش حل شود')]:
    add(K, t, 'ابزار', stt, 'صندوق', VL + 'sakht/' + f, note=note)

P = 'دفتر پروژه'
for f, t in [('core/log.html', 'دفتر پروژه (هر روز چه تغییر کرد)'), ('core/need.html', 'چه چیزی از تو لازم دارم'),
             ('core/repos.html', 'مخزن‌ها'), ('atlas/sitemap.html', 'نقشهٔ سایت'), ('atlas/coverage.html', 'نقشهٔ پوشش')]:
    add(P, t, 'صفحه', 'ساخته', 'صندوق', VL + f)

def rel(l):
    if not l: return ''
    if l.startswith('../'): return DS + l[3:]
    if l.startswith('#'): return VL + 'simorgh/plan.html'
    return VL + 'simorgh/' + l

# ── ۳. علم‌ها ───────────────────────────────────────────────────
M = {'have': 'ساخته', 'part': 'در کار', 'none': 'مانده'}
for s in plan['sciences']:
    add('علم‌ها', s[0], 'علم', M.get(s[2], s[2]), 'عمومی' if s[2] != 'none' else '—', rel(s[3]) if len(s) > 3 else '',
        note=s[1][:90])

# ── ۴. محصول‌ها و درآمد ─────────────────────────────────────────
for p in plan['products']:
    link = rel(p[6])
    add('محصول‌ها', p[0], 'محصول', 'در کار' if p[5] == 'have' else 'مانده', '—', link, None, p[7] if len(p) > 7 else '', stage=p[4])

# ── ۵. کارها (فهرست کارهای پروژه) ───────────────────────────────
MB = {'done': 'ساخته', 'doing': 'در کار', 'todo': 'مانده'}
for b in plan['backlog']:
    add('کارها', b[1], 'کار', MB.get(b[2], b[2]), '—')

# ── ۶. سایت شخصی و پروژه‌های دیگر ───────────────────────────────
O = 'سایت و پروژه‌های دیگر'
for path, t in [('', 'سایت شخصی (رزومه و نمونه‌کار)'), ('fa/', 'نسخهٔ فارسی سایت شخصی'), ('cv.html', 'رزومه'),
                ('Dour/', 'دور (بازی گروهی کلمه)'), ('Language-Learning-Party-Game/', 'دور: زبان'),
                ('earth-through-time/', 'زمین در گذر زمان (اطلس زمان)'), ('ganjoor-no/', 'گنجور نو'),
                ('mafia/', 'میز خدا (گردانندهٔ مافیا)'), ('wellbeing-check/', 'سنجش سلامت سازمان'),
                ('psychology-wiki/', 'ویکی روانِ قدیمی (به دانش‌سرا رفته)')]:
    add(O, t, 'سایت', 'ساخته', 'عمومی', SITE + path)

# ── ۷. منتظرِ تو ────────────────────────────────────────────────
W = 'منتظر تو'
for t, note, link in [
    ('سه گزارش مرکز پژوهش‌های مجلس (PDF)', 'خانه‌های خالی: شماره‌های ۱۱۹۴۸، ۹۳۶۵، ۱۱۳۲۴', VL + 'core/need.html'),
    ('فصل «فروپاشی کمونیسم» کوران یا مقالهٔ Now Out of Never', 'گوگل‌بوکس این صفحه‌ها را نشان نمی‌دهد', VL + 'core/need.html'),
    ('نشانی Google My Maps برای نقشهٔ خرابی‌ها', '', VL + 'sakht/map.html'),
    ('نشانی کانال‌های تلگرام و ایکس برای نبضِ میز', 'فقط وقتی سیمرغ منتشر شود', VL + 'simorgh/poll.html'),
    ('تصمیم: نقشه و نبضِ میز با انتشار سیمرغ عمومی شوند؟', '', ''),
    ('تصمیم: صفحهٔ «پروندهٔ امنیت» برگردد؟', '۲۳ آبان برداشته شد', ''),
    ('فایل‌های خام دوره‌های روان (۵۶ فایل)', 'برای کامل کردن صفحه‌های موضوعی روان', DS + 'psy/'),
    ('تصمیم: سطر «ریشهٔ اسطوره‌ای» روی کارت شخصیت‌ها بماند؟', '', ''),
    ('تأیید: بازنویسی تاریخچهٔ گیت برای پاک کردن شناسهٔ فایل‌های درایو از نسخه‌های قدیمی', 'صفحه‌های امروز پاک‌اند؛ نسخه‌های قدیمی هنوز دارند. نسخهٔ پشتیبان آماده است', ''),
    ('تست دستی: یک دور بازی «دور» و «دور: زبان» با چهار نفر واقعی', '', SITE + 'Dour/'),
    ('تست دستی: سه نفر تازه‌وارد سیمرغ را ببینند؛ در ۵ دقیقه می‌فهمند چیست؟', '', ''),
    ('تأیید خواندن مخزن ایده‌های IranAzadAbad', '', ''),
]:
    add(W, t, 'تصمیم یا فایل', 'منتظر تو', '—', link, note=note)

# ── ۷ب. تست‌ها ─────────────────────────────────────────────────
import collections
TR = load(f'{VAULT}/data/tests.json')['rows']
per = collections.OrderedDict()
for t in TR: per.setdefault(t['project'], collections.Counter())[t['status']] += 1
for pj, c in per.items():
    bad = c['رد'] + c['مانده']
    add('تست‌ها', pj, 'جمع تست', 'ساخته' if not bad else 'در کار', '—', count=c['قبول'] + c['رفع شد'],
        note='، '.join(f'{v} {k}' for k, v in c.items()))
for t in TR:
    if t['status'] in ('رد', 'مانده', 'دستی'):
        add('تست‌ها', f"{t['project']}: {t['name']}", t['kind'], 'منتظر تو' if t['status'] == 'دستی' else 'مانده', '—',
            note=(t['status'] + ('. ' + t['detail'] if t['detail'] else ''))[:140])

# ── ۷ج. بازارها ────────────────────────────────────────────────
for kind, name, note, link in [
    ('شیرده', 'اسکن فشار روانی کار برای شرکت‌های کوچک هلند (سنجش سلامت سازمان)',
     'غیبتِ ناشی از فشار روانی کار سالی ۴٫۹ میلیارد یورو برای کارفرماها؛ حدود ۱۴٬۵۰۰ یورو هر مورد (TNO ۲۰۲۵). ۶۸٪ شرکت‌ها RI&E دارند و ۳۰٪ آن‌ها کیفیت کافی ندارد',
     'https://publications.tno.nl/publication/34645173/TN4nayzz/TNO-2025-werkstress.pdf'),
    ('شیرده', 'خدمات محصول و تجربهٔ کاربری (وقت خودت، صفحهٔ خدمات)', 'سریع‌ترین پول؛ فقط صفحهٔ خدمات و قیمت کم است', ''),
    ('شیرده', 'بازی برای تیم‌سازی و آموزش در شرکت‌ها (دور، میز خدا)',
     'بازار بازی جدی اروپا ۷٫۷ میلیارد دلار در ۲۰۲۶، رشد سالانه حدود ۱۸٪ (برآورد تجاری Mordor؛ تأییدنشده)',
     'https://www.mordorintelligence.com/industry-reports/europe-serious-gaming-market'),
    ('شیرده', 'تمرین هلندی سر کار برای کارفرما و مدرسهٔ زبان (دور: زبان)',
     'فلاندر سطح گفتاری تازه‌واردها را به B1 می‌برد و روی تمرین سر کار تکیه دارد؛ خریدار سازمان است نه فرد',
     'https://www.vlaanderen.be/onderwijsprofessionals/organisatie-en-administratie/specifiek-aanbod-en-organisatievormen/nederlands-als-tweede-taal-nt2/de-nt2-test'),
    ('بکر', 'اسکن سلامت سازمان به فارسی، با مؤسسه‌های روان‌شناسی ایرانی', 'رقیب تقریباً ندارد؛ پرداخت و اعتماد هنوز آزموده نشده', ''),
    ('بکر', 'بازی دورهمی فارسی برای خانواده‌های مهاجر و بچه‌هایشان (دور: زبان، حالت فارسی)', 'ابزار بازی‌محور کم است؛ اندازهٔ بازار نامعلوم', ''),
    ('بکر', 'ابزار گردانندهٔ مافیا برای کافه‌ها و دورهمی‌های ایرانی (میز خدا)', 'علاقه زیاد، عادت به پرداخت کم؛ فروش به کافه و رویداد محتمل‌تر از فرد', ''),
    ('بکر', 'کارگاه و دوره از روی دانش‌سرا (روان و جامعه، با منبع)', 'خودِ ویکی پول نمی‌سازد؛ کارگاه و دوره می‌سازد', ''),
    ('بکر', 'درنگ برای ویراستار و مترجم فارسی', 'بازار کوچک و تخصصی؛ آخر صف', ''),
]:
    add('بازارها', name, 'بازار ' + kind, 'مانده', '—', link, note=note)

# ── ۸. صف کتاب‌ها ──────────────────────────────────────────────
for i, (t, s) in enumerate([
    ('کوران: حقیقت‌های خصوصی (فصل ۱ تا ۴ و مقالهٔ ۱۹۸۹)', 'در کار'), ('کرزمن: انقلاب تصورناپذیر', 'مانده'),
    ('چنووث ۲۰۲۱ (ترجمهٔ فارسی)', 'مانده'), ('چنووث و استفان: بقیهٔ کتاب', 'مانده'),
    ('عجم‌اوغلو و رابینسون: راهروی باریک', 'مانده'), ('آبراهامیان (متن کامل آماده است)', 'مانده'),
    ('اُدانل و اشمیتر', 'مانده'), ('هاینر', 'مانده'), ('لینتس و استپان', 'مانده'), ('شلینگ', 'مانده'),
    ('اولسون، اوستروم، اکسلراد', 'مانده'), ('پیش‌گفتار مور', 'مانده'), ('تاریخ جهان (فارسی)', 'مانده')], 1):
    add('کتاب‌ها', t, 'کتاب', s, '—', note=f'نوبت {i}')

FA = str.maketrans('0123456789', '۰۱۲۳۴۵۶۷۸۹')
for i, r in enumerate(rows):
    r['id'] = f'r{i+1:03d}'
    r['note'] = r['note'].translate(FA)
out = {'rows': rows, 'meta': [{'label': 'built', 'value': datetime.date.today().isoformat()}, {'label': 'ساخته‌شده با', 'value': 'build/status.py در گاوصندوق: شمارش‌ها از registry.json، plan.json، دفتر تقلب و پوشه‌های صندوق'}]}
json.dump(out, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
from collections import Counter
print(len(rows), 'rows;', dict(Counter(r['status'] for r in rows)))
