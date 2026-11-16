# -*- coding: utf-8 -*-
"""Build core/need.html — «چیزهایی که باید بگیریم»: what the project still lacks and only the editor can
bring (books, own files, people, settings), plus the reading queue of what we already hold. Data below."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__)); R = os.path.abspath(HERE + '/..')
B = json.load(open(f'{R}/data/library/books.json', encoding='utf-8')); C = json.load(open(f'{R}/data/library/collection.json', encoding='utf-8'))
I = json.load(open(f'{R}/data/sakht/sakht.json', encoding='utf-8'))['ideas']
rd = {b.get('drive'): b.get('read') for b in B}
have = {'کتاب و فایل در کتابخانه': len(C), 'خوانده و سنجیده (کامل یا بخشی)': sum(1 for c in C if rd.get(c['id']) in ('full', 'partial')),
        'ایده در مخزن ایده‌ها': len(I), 'ایدهٔ خلاصه‌شده': sum(1 for i in I if i.get('s'))}
# group, [title, by, why, where it is used]
NEED = [
 ['book', 'منبع برای علم‌هایی که هنوز تقریباً منبعی ندارند', 'یک کتاب هنوز ناقص است (اولی). بقیه این‌ها علم‌هایی‌اند که نقشهٔ کلان لازم دارد و در کتابخانه کم یا هیچ منبعی برایشان نیست. هر کدام یک پیشنهادِ مشخص دارد؛ هر منبعِ معتبرِ دیگری هم به کار می‌آید. هیچ‌کدام فوری نیست.', [
  ['Private Truths, Public Lies: بقیهٔ کتاب', 'کوران، ۱۹۹۵: فصل‌های ۵ تا ۱۹', 'فصل ۱ تا ۴ خوانده شد. هستهٔ فصلِ ۱۵ را از مقالهٔ «جرقه و آتشِ دشت» (۱۹۸۹، کامل خوانده شد) گرفتیم. هنوز مانده: فصلِ ۱۶ (فروپاشی کمونیسم) یا مقالهٔ «Now Out of Never» (۱۹۹۱). گوگل‌بوکس این صفحه‌ها را نشان نمی‌دهد؛ کتابخانه یا خرید', '../soc/#preference-falsification'],
  ['علوم سیاسی: قانون اساسی', 'Elkins, Ginsburg & Melton (2009). The Endurance of National Constitutions', 'چرا بعضی قانون‌های اساسی می‌مانند و بعضی نه؛ برای نگارشِ پیش‌نویس در «۶۰۰ روز»', '../simorgh/entries.html#covenantal-transition'],
  ['علوم سیاسی: طراحیِ انتخابات', 'International IDEA (2005). Electoral System Design: The New International IDEA Handbook (رایگان روی سایتِ IDEA)', 'کدام نظامِ انتخاباتی برای کشوری چندقومی و قطبی‌شده', '../simorgh/entries.html#covenantal-transition'],
  ['علوم سیاسی: تمرکززدایی و فدرالیسم', 'Stepan, A. (1999). Federalism and Democracy: Beyond the U.S. Model. Journal of Democracy 10(4)', '۲۰٪ در پیمایشِ گمان نوعی نظامِ فدرال خواسته‌اند؛ بحثش منبع می‌خواهد', '../iran/#political-attitudes-2026'],
  ['حقوق بین‌الملل و تحریم', 'Mulder, N. (2022). The Economic Weapon: The Rise of Sanctions as a Tool of Modern War', 'تحریم چطور کار می‌کند و چطور برداشته می‌شود؛ دفترِ ویرانی‌ها این‌جا خالی است', '../simorgh/plan.html#ledger'],
  ['ارتباطات و رسانه: شایعه و راستی‌آزمایی', 'Wardle, C. & Derakhshan, H. (2017). Information Disorder. Council of Europe (رایگان)', 'پایهٔ «نهادِ شفافیت» و نبرد بر سرِ روایت', '../simorgh/entries.html#ten-unbuilt-roles'],
  ['ارتباطات و رسانه: شایعه', 'Sunstein, C. R. (2009). On Rumors', 'چرا شایعه در جامعهٔ بی‌اعتماد سریع پخش می‌شود', '../simorgh/entries.html#ten-unbuilt-roles'],
  ['اقتصادِ پس از گذار', 'Åslund, A. (2007). How Capitalism Was Built', 'درس‌های اروپای شرقی برای «قوانینِ روزِ اول»: پول، قیمت، خصوصی‌سازی', '../simorgh/entries.html#strategy-paper'],
  ['آب و کشاورزی', 'Madani, K. (2014). Water management in Iran: what is causing the looming crisis? Journal of Environmental Studies and Sciences 4', 'ورشکستگیِ آبی؛ تنها پروندهٔ برگشت‌ناپذیرِ دفترچهٔ سیاست', '../iran/#groundwater-depletion'],
  ['مدیریت بحران', 'UNDRR (2015). Sendai Framework for Disaster Risk Reduction 2015–2030 (رایگان)', 'زلزله، جنگ، قطعِ خدمات؛ برای «روزِ آزادی» و مرغ‌های نگهبانِ جان', '../simorgh/entries.html#liberation-day'],
  ['شهرسازی و مسکن: فقط PDFِ سه گزارشِ مرکز پژوهش‌های مجلس', 'خانه‌های خالی به‌مثابه ذخیرهٔ مسکن (۱۱۹۴۸)، مالیات بر خانه‌های خالی (۹۳۶۵)، ارزیابی اجرای قانون (۱۱۳۲۴)', 'فهرستت رسید و سه مقالهٔ اصلی را خودم پیدا و چک کردم؛ سایت مرکز پژوهش‌ها به‌روی من بسته است، پس فقط این سه را بفرست', '../simorgh/plan.html#ledger'],
  ['کتابِ عارفی: Learning from Informal Settlements in Iran (۲۰۱۸)', 'اگر از کتابخانه یا خرید قانونی به دستت رسید', 'تنها کتابِ جامعِ انگلیسی دربارهٔ حاشیه‌نشینی ایران؛ اختیاری', ''],
 ]],
 ['own', 'فایل‌هایی که فقط پیش خودت است', '', [
  ['فایل‌های خام دورهٔ روان', 'رونویس جلسه‌ها و اسلایدها', 'برای مقایسه با صفحه‌های موضوعی و پیدا کردن نکته‌های جاافتاده؛ و جلسه‌ای که دربارهٔ کمبود توجه بود', '../psy/'],
  ['نام ده فایل بی‌نام در کتابخانه', 'ده فایل در پوشهٔ کتاب‌ها عنوان ندارند', 'تا نامشان معلوم نشود در قفسه‌ای نمی‌نشینند', '../atlas/collection.html'],
  ['ادامهٔ کتاب هایک از فصل ۵', 'فایل کتاب یا فصل‌های بعدی', 'خلاصهٔ فصل‌های ۱ تا ۴ در ویکی هست و ادامه‌اش مانده', '../core/review.html'],
 ]],
 ['people', 'آدم‌هایی که کار بدون آن‌ها کامل نمی‌شود', 'فقط نقش؛ هیچ نامی این‌جا نمی‌آید.', [
  ['یک متخصص امنیت', '', 'پیش از هر ابزاری که از مردم داده بگیرد', '../simorgh/plan.html'],
  ['یک روان‌شناس یا روان‌پزشک برای مرور «کمک عملی»', '', 'آن ۳۵ بخش توصیهٔ سلامت است و باید چشم متخصص ببیندش', '../psy/topics/crisis.html#help'],
  ['یک حقوق‌دان آشنا با عدالت انتقالی', '', 'برای مدخل‌های دادخواهی، عفو و پالایش', '../soc/#transitional-justice-options'],
  ['یک تاریخ‌دان ایران معاصر', '', 'برای مرور شش مدخل تازهٔ تاریخ، به‌ویژه جاهای محل اختلاف', '../tarikh/#oil-nationalisation-1953-coup'],
  ['نخستین مشتری آزمایشی سنجش سازمان', '', 'محصول شمارهٔ یک برای درآمد', '../wellbeing/orgsvc.html'],
  ['سه تا پنج نفر معتمد برای یک شب بازی', '', 'آزمودن بازی «شهر» و میز مافیای ایران با آدم واقعی', '../simorgh/sim.html'],
 ]],
 ['data', 'داده‌هایی که هنوز پیدا نکرده‌ام', 'اگر منبع معتبری می‌شناسی بفرست؛ بدون منبع عددی نمی‌نویسم.', [
  ['اقلیت‌های قومی و دینی', '', 'هیچ آمار رسمی قابل‌اتکایی نیست؛ دفتر ویرانی‌ها این‌جا خالی است', '../simorgh/plan.html#ledger'],
  ['روابط خارجی و تحریم‌ها', '', 'عدد قابل‌اتکا برای هزینهٔ تحریم و دارایی‌های مسدود', '../simorgh/plan.html#ledger'],
  ['آسیب جنگ ۱۴۰۴–۱۴۰۵', '', 'برآورد مستقل از خسارت زیرساخت، میراث و تلفات', '../simorgh/plan.html#ledger'],
  ['شمار مهاجران و بازگشت‌پذیری', '', 'فقط گفته‌های پراکنده داریم (ردهٔ D)', '../iran/#emigration'],
 ]],
 ['set', 'تنظیم‌هایی که خودت باید بزنی', '', [
  ['پنهان کردن ایمیل در GitHub', 'Settings ← Emails ← Keep my email addresses private', 'تا ایمیل شخصی دوباره وارد تاریخچهٔ عمومی نشود', '../simorgh/plan.html'],
  ['ورود دومرحله‌ای برای GitHub و ایمیل', '', 'حساب گرداننده تنها نقطهٔ شکست سایت است', '../simorgh/plan.html'],
 ]],
]
QUEUE = ['کوران: فصل ۱ تا ۴ و مقالهٔ ۱۹۸۹ خوانده شد ← تحریف ترجیحات، انقلاب ۱۳۵۷، نبض میز', 'کورزمن، انقلابِ تصورناپذیر در ایران ← ۱۳۵۷، هفت شب', 'چنووث ۲۰۲۱، مقاومت مدنی (فارسی) ← قدمِ تو، سرکوبِ دیجیتال', 'چنووت و استفان ۲۰۱۱، بقیهٔ کتاب (فصل ایران خوانده شد) ← قدمِ تو', 'عجم‌اوغلو و رابینسون، راهِ باریکِ آزادی ← دولتِ توانا و جامعهٔ توانا', 'آبراهامیان، ایران بین دو انقلاب (متن‌خوانی از روی تصویر در جریان) ← ویکی تاریخ', 'اودانل و اشمیتر ← گذارِ میثاقی', 'هاینر، حقیقت‌های ناگفتنی ← عدالتِ انتقالی', 'لینز و استپان ← گذار از سلطانیسم', 'شلینگ، راهبردِ کشمکش ← نقطهٔ کانونی', 'اولسون، استروم، اکسلرود (بخشی) ← کنشِ جمعی و همکاری', 'مور، پیش‌گفتارِ تاریخِ جهان در آینهٔ هفت چیزِ ارزان ← ویکی تاریخ', 'تاریخ جهان (فارسی، ۵۷۴ صفحه) ← ویکی تاریخ', 'تاریخ روابط سیاسی ایران و انگلیس (جلدهای ۶ و ۷؛ بقیه فقط یک فصل خوانده شده) ← روابط خارجی',
         'چرا ایران عقب ماند و غرب پیش رفت؟ ← اقتصاد و نهادها', 'توتالیتاریسم (هانا آرنت)', 'مقاومت شکننده', 'آداب دیکتاتوری (فرانک دیکوتر)', 'استبداد', 'سیر تاریخی ابداع حقوق بشر', 'لویاتان', 'ملت‌ها مهم‌اند', 'اسطورهٔ دولت']
DATA = json.dumps({'have': have, 'need': NEED, 'queue': QUEUE}, ensure_ascii=False)
TPL = r'''<!doctype html>
<html lang="fa" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>چیزهایی که باید بگیریم | دانش‌سرا</title>
<meta name="description" content="آنچه داریم، آنچه در صف خواندن است، و آنچه هنوز باید به دست بیاید: کتاب، فایل، آدم، داده و تنظیم.">
<link rel="stylesheet" href="design/tokens.css">
<style>
main{padding-block:var(--s5) var(--s10)}
h1{font-size:var(--h1);margin:var(--s4) 0 var(--s2);line-height:var(--lh-tight)}
h2{font-size:var(--h3);margin:var(--s8) 0 4px}
.lead{color:var(--ink-2);max-width:62ch;line-height:1.9;margin:0 0 var(--s4)}
.sub{color:var(--ink-2);font-size:.9rem;margin:0 0 10px;max-width:62ch;line-height:1.8}
.tiles{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:10px}
.tile{padding:14px;border-radius:16px;border:1px solid var(--line);background:var(--surface)}
.tile b{display:block;font-size:1.8rem;color:var(--primary);font-variant-numeric:tabular-nums}.tile span{font-size:.84rem;color:var(--ink-2)}
.nav{display:flex;flex-wrap:wrap;gap:6px;margin:var(--s4) 0}
.nav a{padding:6px 14px;border-radius:99px;border:1px solid var(--line-strong);text-decoration:none;color:var(--ink);font-size:.88rem;background:var(--surface)}
.nav a b{color:var(--primary)}
.it{display:grid;grid-template-columns:auto minmax(0,1fr);gap:12px;align-items:start;padding:12px 14px;border-radius:14px;border:1px solid var(--line);background:var(--surface);margin-bottom:8px;line-height:1.8}
.it input{width:22px;height:22px;margin-top:5px;accent-color:var(--primary)}
.it b{display:block}.it small{color:var(--ink-3)}.it span{color:var(--ink-2);font-size:.9rem;display:block}
.it a{font-size:.84rem}
.it.ok{opacity:.55}.it.ok b{text-decoration:line-through}
.q{display:flex;flex-wrap:wrap;gap:6px}
.q span{padding:5px 12px;border-radius:99px;border:1px solid var(--line);background:var(--surface);font-size:.86rem}
.q span i{font-style:normal;color:var(--primary);font-weight:700;margin-inline-end:6px}
</style>
</head>
<body>
<main class="wrap" id="main">
<h1>چیزهایی که باید بگیریم</h1>
<p class="lead">سه بخش: آنچه داریم، آنچه از همین داشته‌ها در صف خواندن است، و آنچه هنوز باید از بیرون بیاید. هر چه را گرفتی تیک بزن.</p>
<div class="tiles" id="tiles"></div>
<h2>از کتابخانهٔ خودمان، در صف خواندن</h2>
<p class="sub">برای این‌ها کاری از تو لازم نیست. اول کتاب‌هایی که جای خالی دفتر ویرانی‌ها را پر می‌کنند (جلوی هرکدام نوشته شده کدام حوزه)، بعد بقیه. برای آب، خاک، آموزش و اقتصاد در کتابخانه کتابی نداریم؛ آن‌ها باید از داده و گزارش بیاید.</p>
<div class="q" id="q"></div>
<div class="nav" id="nav"></div>
<div id="need"></div>
<p class="sub" style="margin-top:var(--s6)">این فهرست زنده است و با هر کار تازه عوض می‌شود. وضع کل کارها: <a href="log.html">دفتر پروژه</a> · فهرست و سنجش کتاب‌ها: <a href="../atlas/library-plan.html">نقشهٔ کتابخانه</a></p>
</main>
<script>
const D = __DATA__, $ = id => document.getElementById(id);
const esc = s => String(s).replace(/[&<>"]/g, c => ({"&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;"}[c]));
const fa = n => String(n).replace(/\d/g, c => "۰۱۲۳۴۵۶۷۸۹"[c]);
let done = {}; try { done = JSON.parse(localStorage.getItem("ds-need") || "{}") || {}; } catch (_) {}
$("tiles").innerHTML = Object.entries(D.have).map(([k, v]) => `<div class="tile"><b>${fa(v)}</b><span>${esc(k)}</span></div>`).join("");
$("q").innerHTML = D.queue.map((t, i) => `<span><i>${fa(i + 1)}</i>${esc(t)}</span>`).join("");
function draw(){
  $("nav").innerHTML = D.need.map(g => `<a href="#g-${g[0]}">${esc(g[1].split(" ").slice(0, 3).join(" "))}… <b>${fa(g[3].filter((_, i) => !done[g[0] + i]).length)}</b></a>`).join("");
  $("need").innerHTML = D.need.map(g => `<section id="g-${g[0]}"><h2>${esc(g[1])}</h2>${g[2] ? `<p class="sub">${esc(g[2])}</p>` : ""}${g[3].map((x, i) => `<label class="it ${done[g[0] + i] ? "ok" : ""}"><input type="checkbox" data-k="${g[0] + i}" ${done[g[0] + i] ? "checked" : ""}><div><b dir="auto">${esc(x[0])}</b>${x[1] ? `<small dir="auto">${esc(x[1])}</small>` : ""}<span>${esc(x[2])}</span><a href="${x[3]}">کجا به کار می‌آید ←</a></div></label>`).join("")}</section>`).join("");
}
$("need").addEventListener("change", e => { const k = e.target.dataset.k; if (!k) return; if (e.target.checked) done[k] = 1; else delete done[k]; try { localStorage.setItem("ds-need", JSON.stringify(done)); } catch (_) {} draw(); });
draw();
</script>
</body>
</html>
'''
open(f'{R}/core/need.html', 'w', encoding='utf-8').write(TPL.replace('__DATA__', DATA))
print('core/need.html:', sum(len(g[3]) for g in NEED), 'items;', have)
