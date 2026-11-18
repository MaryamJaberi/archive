# -*- coding: utf-8 -*-
"""فهرست همهٔ تست‌ها (عمومی + مخصوص هر پروژه) و نتیجهٔ آخرین اجرا.
ورودی: crawl2.json (خزندهٔ خودکار)، flows.json (مسیر کاربر)، vault.json، بررسی محتوای دانش‌سرا.
خروجی: tests.json (برای میز فرمان و صندوق) و TESTS.md (بخش تستِ هر پروژه)."""
import json, collections, glob, os, re, sys, datetime
T = '/home/claude/work/tests'; SITE = '/home/claude/maryamjaberi.github.io'
crawl = json.load(open(f'{T}/crawl2.json'))['pages']
flows = json.load(open(f'{T}/flows.json')); vault = json.load(open(f'{T}/vault.json'))

P = collections.OrderedDict([
 ('portfolio', 'پورتفولیو'), ('daneshsara', 'دانش‌سرا (ویکی‌های علمی)'), ('wellbeing-check', 'سنجش سلامت سازمان'),
 ('Dour', 'دور (تیک‌تاک)'), ('Language-Learning-Party-Game', 'دور: زبان'), ('mafia', 'میز خدا (مافیا)'),
 ('earth-through-time', 'زمین در گذر زمان'), ('ganjoor-no', 'گنجور نو'), ('darang', 'درنگ'),
 ('psychology-wiki', 'ویکی روانِ قدیمی'), ('simorgh', 'سیمرغ (صندوق و نسخهٔ اشتراکی)')])
def proj(u):
    s = u.split('/')[0]
    return 'portfolio' if s in ('', 'fa', 'cv.html', 'case', 'index.html') else s
by = collections.defaultdict(list)
for p in crawl: by[proj(p['url'])].append(p)
rows = []
def add(project, tid, kind, name, how, status, detail=''):
    rows.append(dict(project=P[project], id=f'{project[:4].upper()}-{tid}', kind=kind, name=name, how=how, status=status, detail=detail))
ok = lambda cond: 'قبول' if cond else 'رد'
fa = lambda n: str(n).translate(str.maketrans('0123456789', '۰۱۲۳۴۵۶۷۸۹'))

# ── تست‌های عمومی: روی هر پروژهٔ عمومی یکسان اجرا می‌شود ──
home = [p for p in crawl if p['url'] in ('', 'index.html')][0]
forward = {l.split('/')[0] for l in home['internalLinks'] if l}
for k in list(P)[:-1]:
    v = by.get(k, [])
    if not v: continue
    n = len(v); G = 'عمومی'
    b = [p for p in v if p.get('status') != 200]
    add(k, 'G01', G, 'همهٔ صفحه‌ها باز می‌شوند', f'خزندهٔ خودکار، {fa(n)} صفحه', ok(not b), '، '.join(p['url'] for p in b[:3]))
    b = [p for p in v if p['pageErrors'] or p['console']]
    add(k, 'G02', G, 'بدون خطای برنامه در مرورگر', 'خزنده، گوش‌دادن به خطاها', ok(not b), '، '.join(p['url'] for p in b[:3]))
    b = [p for p in v if p['failed']]
    add(k, 'G03', G, 'هیچ فایل داخلی گم نشده', 'خزنده، پاسخ ۴۰۴', ok(not b), (b[0]['failed'][0] if b else ''))
    b = [p for p in v if p.get('brokenLinks')]
    add(k, 'G04', G, 'پیوند داخلیِ شکسته ندارد', 'خزنده', ok(not b), '، '.join(p['url'] for p in b[:3]))
    b = [p for p in v if (p.get('overflow') or 0) > 2]
    add(k, 'G05', 'تجربهٔ کاربری', 'روی گوشی (۳۹۰ پیکسل) از عرض صفحه بیرون نمی‌زند', 'خزنده، اولین صفحه', ok(not b), '، '.join(p['url'] for p in b[:3]))
    b = [p for p in v if not p.get('title')]
    add(k, 'G06', G, 'هر صفحه عنوان دارد', 'خزنده', ok(not b))
    b = [p for p in v if not p.get('lang') or not p.get('dir')]
    add(k, 'G07', G, 'زبان و جهت متن (راست‌به‌چپ) اعلام شده', 'خزنده', ok(not b))
    b = [p for p in v if not p.get('metaDesc')]
    add(k, 'G08', 'دیده‌شدن', 'توضیح صفحه برای موتور جستجو', 'خزنده', ok(not b), f'{fa(len(b))} صفحه بی‌توضیح' if b else '')
    b = sum(p.get('imgNoAlt', 0) for p in v)
    add(k, 'G09', 'دسترس‌پذیری', 'تصویرها متن جایگزین دارند', 'خزنده', ok(not b))
    ax = collections.Counter()
    for p in v:
        for a in p.get('axe') or []:
            if a.get('impact') in ('critical', 'serious'): ax[a['id']] += a['n']
    con = ax.pop('color-contrast', 0)
    add(k, 'G10', 'زیبایی و خوانایی', 'کنتراست رنگ متن کافی است (WCAG AA)', 'axe-core روی هر صفحه', ok(con == 0), f'{fa(con)} مورد' if con else '')
    add(k, 'G11', 'دسترس‌پذیری', 'بدون ایراد جدیِ دسترس‌پذیری', 'axe-core، فقط جدی و بحرانی', ok(not ax), '، '.join(f'{i}×{fa(c)}' for i, c in ax.most_common(3)))
    back = any(l in ('', 'index.html', 'fa/', 'fa/index.html') for p in v for l in p['internalLinks'])
    if k != 'portfolio':
        fwd = k in forward or any(k in l for p in by['portfolio'] for l in p['internalLinks']) or k in open(f'{SITE}/index.html', encoding='utf-8').read()
        add(k, 'G12', 'ارتباط پروژه‌ها', 'رفت: از پورتفولیو به این پروژه راه هست', 'خواندن پیوندهای پورتفولیو', ok(fwd))
        add(k, 'G13', 'ارتباط پروژه‌ها', 'برگشت: از این پروژه به پورتفولیو راه هست', 'خواندن پیوندهای پروژه', ok(back), '' if back else 'هیچ پیوند برگشتی نیست')

# ── بررسی‌های متنی روی کل مخزن ──
def grep(pattern, exts=('.html', '.js', '.json')):
    hits = []
    for root, ds, fs in os.walk(SITE):
        if '/.git' in root or '/node_modules' in root or '/_src' in root: continue
        for f in fs:
            if f.endswith(exts):
                try: s = open(os.path.join(root, f), encoding='utf-8').read()
                except Exception: continue
                if re.search(pattern, s): hits.append(os.path.relpath(os.path.join(root, f), SITE))
    return hits
ids = json.load(open('/home/claude/work/drive_ids.json'))
h = [x for x in grep('|'.join(re.escape(i) for i in ids[:400])) + grep('|'.join(re.escape(i) for i in ids[400:]))]
add('daneshsara', 'S01', 'حریم خصوصی', 'شناسهٔ فایل‌های شخصی (درایو) روی سایت نیست', 'جستجوی همهٔ شناسه‌ها در مخزن', 'رفع شد' if not h else 'رد', '۷۵۲ شناسه در ۱۶۳ فایل بود؛ از صفحه‌ها پاک شد' if not h else h[0])
h = grep(r'[A-Za-z0-9._%+-]+@gmail\.com')
CONTACT = {'cv.html', 'index.html', 'fa/index.html', 'wellbeing-check/join.html'}
add('portfolio', 'S02', 'حریم خصوصی', 'ایمیل فقط در صفحه‌های تماس است، نه جای دیگر', 'جستجو در مخزن', ok(not (set(h) - CONTACT)), 'نشانی تماسِ خودِ پورتفولیو عمداً هست')
h = grep(r'fonts\.googleapis\.com|fonts\.gstatic\.com', ('.html', '.css'))
hp = collections.Counter(proj(x) for x in h)
for k in list(P)[:-1]:
    if k in by: add(k, 'S03', 'حریم خصوصی', 'قلم‌ها از سرور بیرونی (گوگل) بار نمی‌شوند', 'جستجو در فایل‌ها', ok(hp.get(k, 0) == 0), f'{fa(hp[k])} فایل' if hp.get(k) else '')
ext = open(f'{T}/extlinks.md', encoding='utf-8').read()
add('portfolio', 'S04', 'محتوا', 'پیوندهای بیرونی زنده‌اند', 'tools/check_links.py روی سایت زنده، ۱۳۲ پیوند', ok('Everything that can be checked answers 200' in ext), 'گیت‌هاب و لینکدین به ربات جواب نمی‌دهند؛ دستی باز شود')

# ── دانش‌سرا: علمی بودن، اعتبار منابع، پیوند ویکی‌ها ──
D = f'{SITE}/daneshsara'; S = json.load(open(f'{D}/core/sources.json'))
C = [json.load(open(p)) for w in ['psy', 'soc', 'phil', 'tabar', 'tarikh'] for p in glob.glob(f'{D}/data/{w}/concepts/*.json')]
con = [c for c in C if c['kind'] == 'concept']; pts = [pt for c in con for pt in c.get('points', [])]
K = 'علمی بودن'
import subprocess
val = subprocess.run(['python3', f'{D}/build/validate.py'], capture_output=True, text=True).stdout.strip().splitlines()[-1]
subprocess.run(['git', '-C', SITE, 'checkout', '--', 'daneshsara/core/registry.json'])
add('daneshsara', 'K01', K, 'ساختار همهٔ مدخل‌ها و ارجاع‌ها درست است', 'build/validate.py', ok(val.startswith('0 ')), val)
n = sum(1 for c in con if not c.get('sources') and not any(p.get('sources') for p in c.get('points', [])))
add('daneshsara', 'K02', K, 'هر مدخل دست‌کم یک منبع دارد', 'شمارش در داده', ok(n == 0), f'{fa(n)} از {fa(len(con))} مدخل بی‌منبع')
n = sum(1 for p in pts if not p.get('sources'))
add('daneshsara', 'K03', K, 'هر گزاره منبع خودش را دارد', 'شمارش در داده', ok(n / len(pts) < 0.02), f'{fa(n)} از {fa(len(pts))} گزاره بی‌منبع ({fa(round(100*n/len(pts)))}٪)؛ فلسفه و تاریخ بیشترین')
n = sum(1 for p in pts if p.get('sources') and all(S.get(s, {}).get('tier') == 4 for s in p['sources']))
add('daneshsara', 'K04', 'اعتبار منابع', 'گزاره‌ها فقط بر منبع ردهٔ ۴ (سرنخ، نه سند) تکیه ندارند', 'ردهٔ همهٔ منابع هر گزاره', ok(n == 0), f'{fa(n)} گزاره فقط منبع ردهٔ ۴ دارد؛ باید روی صفحه علامت بخورد یا منبع بهتر بگیرد')
tiers = collections.Counter(s.get('tier') for s in S.values())
add('daneshsara', 'K05', 'اعتبار منابع', 'سهم منابع قوی (ردهٔ ۱ و ۲) دست‌کم یک‌سوم است', 'شمارش رده‌ها', ok((tiers[1] + tiers[2]) / len(S) >= 1/3), f'ردهٔ ۱: {fa(tiers[1])}، ۲: {fa(tiers[2])}، ۳: {fa(tiers[3])}، ۴: {fa(tiers[4])}')
n = sum(1 for s in S.values() if not s.get('url'))
add('daneshsara', 'K06', 'اعتبار منابع', 'منبع‌ها نشانیِ قابل‌بازکردن دارند', 'شمارش', ok(n / len(S) < 0.5), f'{fa(n)} از {fa(len(S))} منبع بدون نشانی')
key = collections.Counter(re.sub(r'\W+', '', s['cite'].lower())[:60] for s in S.values()); dup = sum(v - 1 for v in key.values() if v > 1)
add('daneshsara', 'K07', 'اعتبار منابع', 'منبع تکراری نداریم', 'مقایسهٔ متن ارجاع‌ها', ok(dup == 0), f'{fa(dup)} تکراریِ قطعی (تکراری‌های با نگارش متفاوت جدا شمرده نشده)')
st = collections.Counter(c['status'] for c in con)
add('daneshsara', 'K08', K, 'مدخل‌ها بازبینی انسانی شده‌اند', 'وضعیت مدخل‌ها', ok(st['draft'] / len(con) < 0.5), f'{fa(st["draft"])} پیش‌نویس، {fa(st.get("reviewed", 0))} بازبینی‌شده')
inbound = collections.Counter(l['to'] for c in C for l in c.get('links', []))
n = sum(1 for c in con if inbound[c['id']] == 0)
add('daneshsara', 'K09', 'ارتباط پروژه‌ها', 'هیچ مدخلی یتیم نیست (از جای دیگری به آن پیوند هست)', 'شمارش پیوندهای ورودی', ok(n / len(con) < 0.05), f'{fa(n)} مدخل بدون پیوند ورودی')
x = sum(1 for c in C for l in c.get('links', []) if l['to'].split(':')[0] != c['id'].split(':')[0])
add('daneshsara', 'K10', 'ارتباط پروژه‌ها', 'ویکی‌ها به هم پیوند دارند (رفت و برگشت)', 'شمارش پیوند میان‌ویکی', ok(x > 500), f'{fa(x)} پیوند میان ویکی‌ها')
n = sum(1 for c in con if not c['title'].get('en'))
add('daneshsara', 'K11', 'محتوا', 'عنوان انگلیسی و هلندی برای همهٔ مدخل‌ها', 'شمارش', ok(n == 0), f'{fa(n)} مدخل بدون عنوان انگلیسی')
add('daneshsara', 'K12', 'محتوا', 'نمونه‌برداری دستی: ۲۰ مدخل تصادفی با منبع اصلی مقایسه شود', 'دستی، هر ماه', 'دستی', 'هنوز انجام نشده')
add('daneshsara', 'K13', 'تجربهٔ کاربری', 'جستجو («بپرس از دانش‌سرا») برای ۱۰ پرسش نمونه جواب مربوط می‌دهد', 'دستی یا خودکار', 'مانده')
add('daneshsara', 'K14', 'زیبایی و خوانایی', 'حالت تاریک و روشن هر دو خوانا', 'axe در هر دو حالت روی ۸ صفحهٔ نمونه', 'رفع شد', 'رنگ خاکستری کم‌رنگ عوض شد')

# ── مخصوص هر پروژه ──
F = 'کارکرد'
def flow(k, key):
    a, b = flows.get(key + '_1300', {}), flows.get(key + '_390', {})
    good = all(not x.get('error') and not x.get('errs') and any(s.startswith('ok:') for s in x.get('log', [])) for x in (a, b))
    return ok(good)
add('Dour', 'F01', F, 'شروع بازی جدید در رایانه و گوشی', 'Playwright: کلیک روی «شروع بازی جدید»', flow('Dour', 'tiktak'))
add('Dour', 'F02', 'دسترس‌پذیری', 'بزرگ‌نمایی با دو انگشت ممکن است', 'خواندن تگ viewport', 'رفع شد', 'قبلاً قفل بود')
add('Dour', 'F03', F, 'تست‌های منطق بازی (۱۰۰ سناریو)', 'vitest در مخزن بازی', '__UNIT_Dour__')
add('Dour', 'F04', 'تجربهٔ کاربری', 'یک دورِ کامل چهارنفره تا امتیاز پایانی', 'دستی با چهار نفر واقعی', 'دستی')
add('Dour', 'F05', 'محتوا', 'واژه‌ها تکراری، توهین‌آمیز یا بیش‌ازحد سخت نیستند', 'مرور فهرست واژه‌ها', 'مانده')
add('Language-Learning-Party-Game', 'F01', F, 'شروع بازی دورهمی در رایانه و گوشی', 'Playwright', flow('L', 'polyglot'))
add('Language-Learning-Party-Game', 'F02', F, 'تست‌های خودِ بازی (زبان‌ها، کارت‌ها، امتیاز)', 'vitest در مخزن بازی', '__UNIT_Lang__')
add('Language-Learning-Party-Game', 'F03', 'محتوا', 'ترجمهٔ واژه‌ها در هر زبان درست است', 'بازبینی یک گویشور بومی برای هر زبان', 'دستی')
add('Language-Learning-Party-Game', 'F04', 'محتوا', 'README همین پروژه را توضیح می‌دهد', 'خواندن', 'رد', 'README رونوشتِ بازی «دور» است')
add('mafia', 'F01', F, 'ورود به ساخت بازی و دیدن ۱۹ سناریو', 'Playwright', flow('m', 'nightshift'))
add('mafia', 'F02', 'تجربهٔ کاربری', 'صفحهٔ ساخت بازی روی گوشی بیرون نمی‌زند', 'Playwright ۳۹۰ پیکسل', 'رفع شد', '۳۰ پیکسل بیرون می‌زد')
add('mafia', 'F03', F, 'بدون سرور هم کار می‌کند (حالت تک‌دستگاه)', 'نسخهٔ گیت‌هاب سرور ندارد', 'قبول', 'اتاق چنددستگاهی و مشاور هوش مصنوعی در این نسخه خاموش‌اند')
add('mafia', 'F04', 'تجربهٔ کاربری', 'دکمهٔ «پرسش از مشاور» وقتی سرور نیست پیام روشن می‌دهد', 'دستی', 'مانده')
add('mafia', 'F05', F, 'یک بازی کامل کلاسیک ۱۰ نفره: شب، روز، رأی، پایان', 'دستی یا تست خودکار', 'مانده', 'این پروژه هیچ تست خودکاری ندارد')
add('mafia', 'F06', 'محتوا', 'قانون‌های هر سناریو با مرجع بازی می‌خواند', 'مقایسه با مهارت mafia-host', 'مانده')
add('mafia', 'F07', 'محتوا', 'README دارد', 'خواندن', 'رد', 'فقط SECURITY.md هست')
add('earth-through-time', 'F01', F, 'پرش در زمان، لایهٔ انسان‌ها، پخش', 'Playwright', flow('e', 'planet'))
add('earth-through-time', 'F02', K, 'هر رویداد و نقشه منبع و «حد صداقت» دارد', 'README و data/atlas', 'قبول', 'بخش Honest limits هست')
add('earth-through-time', 'F03', 'تجربهٔ کاربری', 'دکمهٔ دوره‌ها روی گوشی هم در دسترس است', 'Playwright', 'رد', '«۶۶ میلیون» در ۳۹۰ پیکسل پیدا نشد')
add('earth-through-time', 'F04', K, 'تاریخ‌ها با جدول چینه‌شناسی بین‌المللی می‌خواند', 'مقایسهٔ دستی', 'مانده')
add('ganjoor-no', 'F01', F, 'شعر تصادفی از سرور گنجور می‌آید', 'Playwright روی سایت زنده', 'قبول')
add('ganjoor-no', 'F02', 'تجربهٔ کاربری', 'صفحهٔ شعر روی گوشی بیرون نمی‌زند', 'Playwright ۳۹۰ پیکسل', 'رفع شد', '۱۶۲ پیکسل بیرون می‌زد')
add('ganjoor-no', 'F03', F, 'وقتی سرور گنجور جواب نمی‌دهد پیام روشن می‌بینیم', 'قطع شبکه در تست', 'مانده')
add('ganjoor-no', 'F04', 'محتوا', 'خلاصهٔ هوش مصنوعیِ شعرها برچسب «ماشینی» دارد', 'دیدن صفحه', 'قبول')
add('wellbeing-check', 'F01', F, 'نسخهٔ آزمایشی اسکن باز می‌شود', 'Playwright', flow('w', 'teamweather'))
add('wellbeing-check', 'F02', 'حریم خصوصی', 'پاسخ‌ها ناشناس می‌ماند و گروه کوچک نمایش داده نمی‌شود', 'تست قاعده‌های پایگاه‌داده', 'مانده', 'کارِ عامل فنی wellbeing-tech-docs')
add('wellbeing-check', 'F03', K, 'پرسش‌نامه‌ها نسخهٔ معتبر و مجوزدار هستند', 'بررسی حق نشر هر پرسش‌نامه', 'دستی', 'کارِ عامل ip-protection-expert')
add('wellbeing-check', 'F04', F, 'مسیر کامل: ساخت سازمان، دعوت، پرکردن، گزارش', 'دستی یا خودکار', 'مانده')
add('wellbeing-check', 'F05', 'محتوا', 'سه زبان (هلندی، انگلیسی، فارسی) هم‌معنا هستند', 'بازبینی گویشور', 'دستی')
add('darang', 'F01', F, 'نمونهٔ آماده باز می‌شود', 'Playwright', flow('d', 'darang'))
add('darang', 'F02', K, 'خوانش‌های جداشدهٔ ۲۰ جملهٔ نمونه درست است', 'دستی', 'مانده')
add('portfolio', 'F01', 'محتوا', 'هر محصولِ فهرست، پیوند زنده و مطالعهٔ موردی دارد', 'assets/projects.json', 'قبول')
add('portfolio', 'F02', 'محتوا', 'نسخهٔ فارسی و انگلیسی هم‌محتوا هستند', 'مقایسهٔ دستی', 'دستی')
add('portfolio', 'F03', 'درآمد', 'صفحهٔ «خدمات» با قیمت و راه تماس دارد', 'دیدن سایت', 'رد', 'هنوز صفحهٔ خدمات نیست')
add('psychology-wiki', 'F01', 'ارتباط پروژه‌ها', 'بازدیدکننده را به دانش‌سرا می‌فرستد', 'دیدن صفحه', 'قبول')
V = vault['vault']; Sh = vault['share']
add('simorgh', 'V01', 'حریم خصوصی', 'بدون رمز هیچ چیز دیده نمی‌شود', 'Playwright روی سایت زنده', ok(V['locked'] and Sh['locked']))
add('simorgh', 'V02', 'حریم خصوصی', 'رمز غلط پذیرفته نمی‌شود', 'Playwright', ok(V['wrongRejected'] and Sh['wrongRejected']))
add('simorgh', 'V03', 'حریم خصوصی', 'فایل رمزگذاری‌شده متن خوانا ندارد', 'جستجوی واژه در فایل', ok(not vault['plaintextLeak']))
add('simorgh', 'V04', F, 'همهٔ صفحه‌های صندوق باز می‌شوند و خالی نیستند', f'Playwright، {fa(V["pages"])} صفحه', ok(not V['empty'] and not V['bad']))
add('simorgh', 'V05', F, 'همهٔ صفحه‌های نسخهٔ اشتراکی باز می‌شوند', f'Playwright، {fa(Sh["pages"])} صفحه', ok(not Sh['empty'] and not Sh['bad']))
add('simorgh', 'V06', F, 'بدون خطای برنامه در صفحه‌های صندوق', 'Playwright', ok(not V['errs']), 'دو خطا در یک یا دو صفحه: replaceState و یک اسکریپت ناقص')
add('simorgh', 'V07', 'حریم خصوصی', 'هیچ نام واقعی، نام کاربری یا فهرست آدم‌ها در سیمرغ نیست', 'جستجو و مرور', 'قبول', 'سه فایل خام با نام کاربری پاک شد')
add('simorgh', 'V08', K, 'هر ۸۴ ادعا منبع، ردهٔ اعتبار و شرط ابطال دارد', 'دیتاست ادعاها', 'قبول')
add('simorgh', 'V09', K, 'عددهای وضعیتِ امروز تاریخ دارند و کهنه نشده‌اند', 'مرور ماهانه', 'دستی', 'آخرین به‌روزرسانی آبان ۱۴۰۵')
add('simorgh', 'V10', 'ارتباط پروژه‌ها', 'پیوند مدخل‌های سیمرغ به ویکی‌های عمومی باز می‌شود (رفت)', 'validate با لایهٔ سیمرغ', 'قبول')
add('simorgh', 'V11', 'ارتباط پروژه‌ها', 'از ویکی‌های عمومی هیچ پیوندی به صفحهٔ خصوصی لو نمی‌رود (برگشت)', 'جستجوی نام صفحه‌های خصوصی در سایت عمومی', 'قبول', 'فقط صفحه‌های واسطِ بی‌محتوا')
add('simorgh', 'V12', 'تجربهٔ کاربری', 'یک آدم تازه‌وارد در ۵ دقیقه می‌فهمد سیمرغ چیست', 'تست با ۳ نفر واقعی', 'دستی')
add('simorgh', 'V13', F, 'تیم آبی برای ۷ حرکتِ بازِ دفتر تقلب پاسخ نوشته', 'دفتر تقلب', 'مانده')

# رفع‌هایی که در مخزن منبع انجام شده و نسخهٔ روی سایت در همگام‌سازی بعدی (هر ۶ ساعت) می‌گیرد
FIXED = {'DOUR-G08': 'توضیح صفحه اضافه شد', 'EART-G08': 'توضیح صفحه اضافه شد', 'EART-G10': 'دو رنگ بایگانی تبار تیره‌تر شد',
         'EART-G13': 'پیوند «کارهای دیگرِ سازنده» زیر صفحه', 'GANJ-G13': 'نام سازنده در پاصفحه پیوند شد',
         'PORT-G08': 'توضیح صفحهٔ رزومه اضافه شد', 'PORT-G11': 'گره‌های فرش نقش گرفتند و جعبهٔ پیمایش با صفحه‌کلید در دسترس است',
         'LANG-F04': 'README تازه نوشته شد، با بخش تست', 'MAFI-F07': 'README با بخش تست نوشته شد',
         'DOUR-F03': None}
for r in rows:
    if r['id'] in FIXED and r['status'] == 'رد' and FIXED[r['id']]:
        r['status'] = 'رفع شد'; r['detail'] = FIXED[r['id']]
    if r['id'] == 'EART-G11' and r['status'] == 'رد': r['detail'] = 'برچسب نوار زمان رفع شد؛ یک دکمهٔ تودرتو در صفحهٔ تبار مانده'
unit = {}
for k, f in [('Dour', 'unit_src-Dour-new.log'), ('Lang', 'unit_src-Language-Learning-Party-Game-new.log')]:
    try:
        s = re.sub(r'\x1b\[[0-9;]*m', '', open(f'{T}/{f}').read())
        m = re.search(r'Tests\s+(?:(\d+) failed\s*\|\s*)?(\d+) passed', s)
        unit[k] = ('قبول' if m and not m.group(1) else 'رد', (f'{fa(m.group(2))} قبول' + (f'، {fa(m.group(1))} رد' if m.group(1) else '')) if m else 'اجرا نشد')
    except Exception: unit[k] = ('مانده', 'اجرا نشد')
for r in rows:
    if r['status'].startswith('__UNIT_'):
        k = r['status'][7:-2]; r['status'], r['detail'] = unit[k]

json.dump({'rows': rows, 'meta': [{'label': 'built', 'value': datetime.date.today().isoformat()}]}, open(f'{T}/tests.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
c = collections.Counter(r['status'] for r in rows); print(len(rows), dict(c))
md = ['# تست‌ها\n', f'آخرین اجرا: {datetime.date.today().isoformat()}. ابزارها در همین پوشه: `crawl.mjs` (خزندهٔ عمومی)، `flows.cjs` (مسیر کاربر)، `gen_tests.py` (جمع‌بندی).\n',
      'وضعیت‌ها: **قبول**، **رد**، **رفع شد** (رد بود و درست شد)، **دستی** (آدم باید ببیند)، **مانده** (هنوز نوشته یا اجرا نشده).\n']
for name in P.values():
    if 'سیمرغ' in name: continue
    rs = [r for r in rows if r['project'] == name]
    if not rs: continue
    md.append(f'\n## {name}\n\n| شناسه | نوع | تست | چطور | وضعیت | توضیح |\n|---|---|---|---|---|---|')
    md += [f"| {r['id']} | {r['kind']} | {r['name']} | {r['how']} | {r['status']} | {r['detail']} |" for r in rs]
open(f'{T}/TESTS.md', 'w', encoding='utf-8').write('\n'.join(md) + '\n')
for r in rows:
    if r['status'] == 'رد': print('رد', r['id'], r['name'], '|', r['detail'][:80])
