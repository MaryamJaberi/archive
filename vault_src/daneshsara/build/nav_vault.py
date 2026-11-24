# -*- coding: utf-8 -*-
"""معماری اطلاعات صندوق: core/nav.json
ترتیب و عنوان‌ها این‌جا دستی چیده شده‌اند، نه از روی نام پوشه.
قاعده‌ها: پرکاربردترین بالا؛ هر بخش حداکثر ۹ قلم؛ عنوان کوتاه و بدون تکرار نام بخش؛
صفحه‌های واسط و نسخه‌های قدیمی در «بایگانی» ته فهرست؛ صفحه‌های عمومی اصلاً نمی‌آیند."""
import json, os, re

V = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

NAV = [
 ("هر روز", "چیزهایی که مدام باز می‌کنی", [
   ("sakht/work.html",       "میز کار",            "کارهای در جریان ساخت ایران"),
   ("sakht/day.html",        "روز بعد",            "برنامهٔ روزِ پس از تغییر"),
   ("simorgh/plan.html",     "نقشهٔ کلان",          "تصمیم‌های گرفته و نگرفتهٔ سیمرغ"),
   ("core/tests.html",       "تست‌ها",              "وضعیت تست همهٔ پروژه‌ها"),
   ("core/log.html",         "دفتر پروژه",          "رویدادهای ثبت‌شده"),
 ]),
 ("دسترسی و آدم‌ها", "چه کسی چه چیزی را می‌بیند", [
   ("core/panel.html",       "پنل دسترسی",          "سطح‌ها، رول‌ها، آدم‌ها"),
   ("simorgh/circle.html",   "میز حلقه",            "حلقهٔ معتمد و سهم هر کس"),
   ("wellbeing/monday.html", "برگهٔ جلسهٔ همکاری",   "برای جلسه با همکارها"),
 ]),
 ("پَرِ سیمرغ · متن اصلی", "خودِ بازی و روایت", [
   ("simorgh/par/game.html",      "متنِ کامل بازی",  "قاعده‌ها، هفت شب، بازیکن‌ها، همه یک‌جا"),
   ("simorgh/par/gam.html",       "کارتِ تو",        "هجده نقش و کار هر کدام"),
   ("simorgh/par/roles.html",     "میز مافیای ایران","نقش‌ها روی میز واقعی"),
   ("simorgh/par/map.html",       "کجای میز ایستاده‌ای؟", "جای خودت را پیدا کن"),
   ("simorgh/par/story.html",     "خانه‌ای در افسریه","داستان، با تصویر"),
   ("simorgh/par/two-irans.html", "دو ایران",        "چرا دو ایران شد"),
   ("simorgh/par/shared.html",    "ایرانیان و اسرائیلی‌ها", "میز مشترک"),
   ("simorgh/par/timeline.html",  "خطِ زمان",        "رویدادها از مشروطه تا امروز"),
 ]),
 ("پَرِ سیمرغ · سند راهبردی", "همان تحلیل، برای نشان‌دادن به دیگران", [
   ("simorgh/par/sanad-rahbordi.html", "تشخیص، گزینه‌ها، مسیر", "سند کامل"),
   ("simorgh/par/eraee-rahbordi.html", "همان سند، به شکل ارائه", "برای جلسه"),
   ("simorgh/par/europe.html",         "ارائهٔ اروپا",           "نسخهٔ کوتاه برای مخاطب اروپایی"),
   ("simorgh/par/docs/qa-europe.html", "پرسش و پاسخِ اروپا",     "جواب‌های آماده"),
   ("simorgh/par/docs/qa-site.html",   "پرسش و پاسخِ سایت",      "جواب‌های آماده"),
 ]),
 ("شواهد و بازرسی", "هر ادعا از کجا آمده و چقدر محکم است", [
   ("simorgh/par/data.html",     "میزِ داده",        "۸۴ ادعا با منبع و شرط ابطال"),
   ("simorgh/par/argmap.html",   "نقشهٔ استدلال",     "از استعاره تا کار"),
   ("simorgh/par/inspect.html",  "بازرسیِ ادعا",      "یک ادعا را خودت وارسی کن"),
   ("simorgh/par/audit.html",    "دفترِ ممیزی",       "ضعف‌هایی که خودمان پیدا کردیم"),
   ("simorgh/par/health.html",   "سلامتِ دیتاست",     "عددها با هم می‌خوانند؟"),
   ("simorgh/par/status.html",   "وضعیتِ سند",        "چه چیزی کهنه شده"),
   ("simorgh/par/problems.html", "نقشهٔ مشکل‌ها",      "مسئله‌ها و ربطشان"),
   ("simorgh/par/library.html",  "کتابخانه",          "کتاب‌ها و مقاله‌ها"),
   ("simorgh/par/docs/manabe.html","منابعِ پیشنهادی", "صفِ خواندن"),
 ]),
 ("سیمرغ · بازی و سنجش", "ابزارهای دور میز", [
   ("simorgh/birds.html",      "کارت‌های سی مرغ",   "سی گروه، سی کارت"),
   ("simorgh/why.html",        "چرا؟ علم پشت هر نقش","پشتوانهٔ علمی هر نقش"),
   ("simorgh/sim.html",        "شهر: بازی ده‌نوبته", "شبیه‌سازی"),
   ("simorgh/transitions.html","گذار در کشورهای دیگر","چه شد و چه درس دارد"),
   ("simorgh/poll.html",       "نبض میز",            "نظرسنجی ماهانه و دفتر تقلب"),
 ]),
 ("ساخت ایران", "از تشخیص تا کار", [
   ("sakht/index.html", "ساخت ایران", "ایده‌ها و کارها"),
   ("sakht/map.html",   "نقشهٔ خرابی‌ها","چه چیزی خراب است و کجا"),
 ]),
 ("ویکی ایران", "ایران در عدد و سند", [
   ("iran/index.html",          "ویکی ایران",        "مدخل‌ها"),
   ("iran/entries.html",        "برای ایران",        "یادداشت‌ها و ریشه‌یابی"),
   ("iran/tools/index.html",    "ابزارها",           "فهرست ابزارهای ایران"),
   ("iran/tools/check.html",    "راستی‌آزمای ادعا",   ""),
   ("iran/tools/guess.html",    "اول حدس بزن",       "ایران در عدد"),
   ("iran/tools/lens.html",     "ایران از دید هر رشته",""),
   ("iran/tools/matrix.html",   "ماتریس مسئله × رشته",""),
   ("iran/tools/timeline.html", "خط زمانی ایران",    ""),
 ]),
 ("English", "the shareable English pages", [
   ("simorgh/par/en/index.html",   "Par-e Simorgh",       "index"),
   ("simorgh/par/en/gam.html",     "Your Card",           "the eighteen roles"),
   ("simorgh/par/en/library.html", "Library",             "books and papers"),
   ("simorgh/par/en/shared.html",  "Iranians & Israelis", ""),
 ]),
 ("بایگانی", "نگه داشته‌ایم ولی روزمره نیست", [
   ("simorgh/par/old/full-game-shahrivar.html", "نسخهٔ شهریور ۱۴۰۵", "متن کامل قدیمی، با پروپوزال"),
   ("simorgh/par/docs/story-text.html",         "افسریه: فقط متن",   "همان داستان، بدون تصویر"),
   ("simorgh/par/docs/didgah.html",             "دیدگاه‌های رسانه‌ای","دفترچهٔ منابع"),
   ("simorgh/par/docs/masterplan.html",         "نقشهٔ کلان: خلاصهٔ زنده",""),
   ("simorgh/par/downloads.html",               "دانلود و منابع",    ""),
   ("simorgh/par/index.html",                   "نمایهٔ پَرِ سیمرغ",  "فهرست قدیمی"),
   ("simorgh/archive.html",                     "همهٔ پَرِ سیمرغ",    "فهرست قدیمی"),
   ("simorgh/index.html",                       "ویکی سیمرغ",        "صفحهٔ اول قدیمی"),
   ("core/repos.html",                          "مخزن‌های تازه",      ""),
   ("core/need.html",                           "چیزهایی که باید بگیریم",""),
 ]),
]

# صفحه‌هایی که اصلاً در فهرست نمی‌آیند: واسط، تغییرمسیر، یا عمومی
HIDE = [
 "simorgh/par/nights.html", "simorgh/par/players.html", "simorgh/par/rules.html",
 "simorgh/par/en/nights.html", "simorgh/par/en/players.html", "simorgh/par/en/rules.html",
 "simorgh/entries.html",
 "atlas/coverage.html", "atlas/sitemap.html", "atlas/story.html",
]

def main():
    have = set()
    for _, _, items in NAV:
        for p, _, _ in items: have.add(p)
    missing = [p for p in have if not os.path.exists(os.path.join(V, p))]
    on_disk = set()
    for root, ds, fs in os.walk(V):
        ds[:] = [d for d in ds if d not in ('.git', '__pycache__')]
        for f in fs:
            if f.endswith('.html'):
                on_disk.add(os.path.relpath(os.path.join(root, f), V))
    extra = sorted(on_disk - have - set(HIDE))
    out = {'built': __import__('datetime').date.today().isoformat(),
           'sections': [{'title': t, 'note': n,
                         'items': [{'path': p, 'label': l, 'note': nt} for p, l, nt in items if p in on_disk]}
                        for t, n, items in NAV],
           'hide': HIDE}
    if extra:
        out['sections'].append({'title': 'بقیه', 'note': 'هنوز جایی برایشان تعیین نشده',
                                'items': [{'path': p, 'label': '', 'note': ''} for p in extra]})
    json.dump(out, open(f'{V}/core/nav.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    n = sum(len(s['items']) for s in out['sections'])
    print(f"core/nav.json: {len(out['sections'])} بخش، {n} صفحه، {len(HIDE)} پنهان")
    if missing: print('در فهرست هست ولی فایلش نیست:', '، '.join(sorted(missing)))
    if extra:   print('فایل هست ولی جایش تعیین نشده:', '، '.join(extra))

main()
