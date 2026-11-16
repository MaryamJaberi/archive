from common import *
import re
strip = lambda s: re.sub(r'<[^>]+>', '', s or '').replace('‌‌', '‌')

K = dict(
 kuran=src('Kuran, Timur (1995)'),
 kuran91=src('Kuran, T. (1991). Now out of never', None),
 kurzman=src('Kurzman, C. (2004). The Unthinkable Revolution in Iran'),
 olson=src('Olson, M. (1965). The Logic of Collective Action: Public Goods'),
 schelling=src('Schelling, T. C. (1960). The Strategy of Conflict'),
 cs=src('Chenoweth, E., & Stephan, M. J. (2011). Why Civil Resistance Works: Th'),
 ch21=src('Chenoweth, E. (2021). Civil Resistance: What Everyone Needs to Know'),
 odon=src('O’Donnell', 'O’Donnell, G., & Schmitter, P. C. (1986). Transitions from Authoritarian Rule: Tentative Conclusions about Uncertain Democracies. Johns Hopkins University Press.', 1986, 2) if False else None,
)
K['odon'] = src('O\'Donnell, G., & Schmitter', 'O\'Donnell, G., & Schmitter, P. C. (1986). Transitions from Authoritarian Rule: Tentative Conclusions about Uncertain Democracies. Johns Hopkins University Press.', 1986, 2)
K['lw'] = src('Levitsky, S., & Way, L. A. (2022)', 'Levitsky, S., & Way, L. A. (2022). Revolution and Dictatorship: The Violent Origins of Durable Authoritarianism. Princeton University Press.', 2022, 2)
K['kadivar22'] = src('Kadivar, M. A. (2022)', 'Kadivar, M. A. (2022). Popular Politics and the Path to Durable Democracy. Princeton University Press.', 2022, 2)
K['gamaan'] = src('GAMAAN (2026)', 'GAMAAN (2026). Iranians’ Attitudes Toward the 2026 Protests and War. https://gamaan.org', 2026, 2)
K['abrah82'] = src('Abrahamian, E. (1982). Iran Between Two Revolutions')
K['nokar'] = src('Katouzian, H. (2004)', 'Katouzian, H. (2004). The Short-term Society: A Study in the Problems of Long-term Political and Economic Development in Iran. Middle Eastern Studies, 40(1).', 2004, 2)

# ---------------- root & fields ----------------
new('simorgh', T('سیمرغ', 'Simorgh', 'Simorgh'),
    T('همهٔ آنچه دربارهٔ «پَرِ سیمرغ» ــ بازیِ میزِ مافیای ایران ــ ساخته شده، در یک جا و با یک نقشهٔ روشن: بازی و استعاره، شواهد و ادعاها، تاریخ، راهبرد، قدمِ هر آدم، و خودِ پروژه با ابزارهایش. این ویکی صفحه‌های قاطی‌پاتی را جایگزین نمی‌کند، مرتب می‌کند: هر صفحه و هر ابزار اینجا یک جای مشخص دارد و در مدخلِ «نقشهٔ صفحه‌ها» می‌بینی هر صفحهٔ قدیمی کجا رفته. خصوصی است و در گاوصندوق می‌ماند.',
      'Everything built around Par-e Simorgh, the Iran-as-a-Mafia-table game, in one place with one clear map: game and metaphor, evidence and claims, history, strategy, a step for every person, and the project itself with its tools. It does not replace the scattered pages, it orders them: the page map entry shows where each old page went. Private; kept in the vault.'),
    kind='root', aliases=['سیمرغ', 'پر سیمرغ', 'پَرِ سیمرغ', 'مافیای ایران'])

FIELDS = [
 ('game', 'بازی و استعاره', 'Game and metaphor', 'میزِ مافیا، سه جناح، شخصیت‌ها و نقش‌ها، هفت شبِ گذشته، پَر، و بازی‌هایی که می‌شود امتحان کرد.', 'The Mafia table, factions, characters and roles, the seven past nights, the feather, and the games to try.'),
 ('evidence', 'شواهد و ادعاها', 'Evidence and claims', 'هشتادوچهار ادعای منبع‌دار با ردهٔ اعتبار و شرطِ ابطال، ممیزیِ ضعف‌ها، و کتابخانهٔ منبع‌ها.', 'Eighty-four sourced claims with tiers and falsifiers, the audit of weaknesses, and the source library.'),
 ('history', 'تاریخ و ریشه‌ها', 'History and roots', 'دو ایران، پانصد سالِ بالا رفتنِ روحانیت، ۱۳۵۷ و ایران و اسرائیل در بلندمدت.', 'Two Irans, five centuries of clerical rise, 1979, and Iran and Israel in the long run.'),
 ('strategy', 'راهبرد و گزینه‌ها', 'Strategy and options', 'سه راه و قیمتشان، برنامهٔ ۹۰/۹/۶۰۰، نقدِ نُه جناح، و سند راهبردی.', 'Three paths and their price, the 90/9/600 plan, the nine-faction critique, and the strategy paper.'),
 ('action', 'عمل و آمادگی', 'Action and readiness', 'قدمِ هر آدم، سی مرغ، بیست گروه، پانزده خطر و روز آزادی.', 'A step for every person, thirty birds, twenty groups, fifteen risks and liberation day.'),
 ('project', 'خودِ پروژه', 'The project itself', 'نقشهٔ کلان، علم‌ها، دفتر ویرانی‌ها، محصولات، میز دایره‌ای، ابزارها و نقشهٔ صفحه‌ها.', 'The master plan, sciences, ruins ledger, products, circle table, tools and the page map.'),
]
for slug, fa, en, sfa, sen in FIELDS:
    new(slug, T(fa, en), T(sfa, sen), parent='simorgh:simorgh', kind='field')
# fields point to the root via parent; order list written in build step

# ---------------- GAME ----------------
new('metaphor', T('استعارهٔ میز: ایران یک میزِ مافیاست', 'The table metaphor: Iran as a Mafia table'),
    T('شهری با ۸۷ میلیون نفر؛ شب عده‌ای کم بیدارند و یکدیگر را می‌شناسند، و هشتاد نفر از هر صد نفر خوابند و شمارهٔ هم را ندارند. بازی از ۱۳۵۷ شروع شده. این بازیِ کشتن نیست، بازیِ هماهنگی است.',
      'A city of 87 million: at night a small group is awake and knows each other, while eighty in a hundred sleep without each other\'s numbers. The game began in 1979. It is a coordination game, not a game of killing.'),
    [P('ایران یک میزِ مافیاست: ۸۷ میلیون بازیکن؛ پایگاه حاکمان ۱۰ تا ۱۵ درصد و شهروندان ۸۰ تا ۸۵ درصد. این نسبت‌ها برآوردِ کیفی‌اند، نه یافتهٔ پیمایشی؛ آنچه با داده قابل‌دفاع است «اکثریتی بزرگ، میان دوسوم تا سه‌چهارم» است.', 'Iran as a Mafia table: 87 million players; the rulers\' base 10 to 15 percent, citizens 80 to 85 percent. These ratios are qualitative estimates, not survey findings; what data supports is "a large majority, between two thirds and three quarters".', [K['gamaan']], True),
     P('سه جناح: مافیا شب حرکت می‌کند و روز حرف می‌زند؛ شهر روز حرف می‌زند و شب می‌خوابد؛ مستقل‌ها نه می‌برند نه می‌بازند و فقط تعیین می‌کنند بازی چقدر طول بکشد.', 'Three factions: the Mafia moves by night and talks by day; the City talks by day and sleeps by night; the independents neither win nor lose, they decide how long the game lasts.'),
     P('شرط برد مافیا: ادامهٔ بازی. لازم نیست ببرد، کافی است بازی تمام نشود؛ هر شبِ اضافه یک نفر از شهر کم می‌کند (مهاجرت، فقر، فرسودگی).', 'Mafia win condition: the game continues. It need not win; it is enough that the game does not end; each extra night subtracts someone from the city (emigration, poverty, exhaustion).'),
     P('شرط برد شهر: یک رأیِ واحد در یک روز؛ نه برنامهٔ کامل، یک میثاقِ حداقلی که همه بتوانند پایش را امضا کنند و یک لحظهٔ مشخص که همه هم‌زمان بگویند.', 'City win condition: one vote on one day; not a full programme, a minimal covenant everyone can sign and one defined moment when all speak together.'),
     P('قانونِ طلاییِ میز: موفقیتِ گذار با میزانِ خشونتِ اعمال‌شده در دورهٔ گذار نسبتِ عکس دارد؛ تنها گزاره‌ای که همهٔ صداهای پرونده بر سرش توافق دارند.', 'The table\'s golden rule: transition success is inversely related to the violence used during the transition; the only proposition on which all voices in the file agree.', [K['cs']]),
     P('شهر نیمی از راه را آمده: می‌داند مافیا کیست، اما نمی‌داند فردا صبح چه بگوید. بازی هماهنگی یک راه‌حلِ کلاسیک دارد: یک نشانهٔ پرهزینه و آشکار که همه ببینند و بدانند بقیه هم دیده‌اند؛ اسمش در اسطوره «پَرِ سیمرغ» است.', 'The city is half way: it knows who the Mafia is but not what to say tomorrow morning. A coordination game has a classic solution: a costly, public signal everyone sees and knows the others saw; in myth it is called the Simorgh\'s feather.', [K['schelling'], K['kuran']])],
    [L('soc:coordination-focal-points', 'بازی هماهنگی و نقطهٔ کانونی', 'Coordination game and focal point'),
     L('soc:preference-falsification', 'تحریف ترجیحات', 'Preference falsification'),
     L('simorgh:three-feathers', 'سه پَر', 'The three feathers'),
     L('simorgh:seven-nights', 'هفت شب', 'Seven nights'),
     L('simorgh:roles-47', '۴۷ نقشِ اجتماعی', '47 social roles')], 'simorgh:game')

new('seven-nights', T('هفت شبِ گذشته و دورِ جاری', 'The seven past nights and the current round'),
    T('هر دور یک شب داشت و یک روز؛ آنچه عوض شد ترکیبِ نقش‌ها بود، نه گرداننده. کنارِ هر شب اسطوره‌ای از شاهنامه آمده که همان الگو را هزار سال پیش گفته است.',
      'Each round had a night and a day; what changed was the mix of roles, not the host. Beside each night stands a Shahnameh myth that told the same pattern a thousand years ago.'),
    [P('شبِ یکم، ۱۳۵۷ — ضحّاک: مافیا با رأیِ خودِ شهر انتخاب شد. اجماع اجتماعی بود، اجماع نخبگانی نه؛ در آن خلأ، سازمان‌یافته‌ترین گروه برنده شد، نه پرطرفدارترین.', 'Night 1, 1979, Zahhak: the Mafia was chosen by the city itself. Social consensus existed, elite consensus did not; in that vacuum the best organised group won, not the most popular.', [K['kurzman'], K['abrah82']]),
     P('شبِ دوم، ۱۳۶۰ تا ۱۳۶۸ — اکوان دیو: تثبیت با جنگ و ساختِ نقش‌های تازهٔ «وابستهٔ نهادی» (بازوی مسلح، شبکهٔ محله، حلقهٔ منفعت). بزرگ‌ترین کوهورتِ تاریخِ ایران متولد شد؛ زادگان ۱۳۶۵ نزدیک به ۱٫۹۵۷ میلیون در برابر ۹۷۹٬۹۲۳ در ۱۴۰۳.', 'Night 2, 1981 to 1989, Akvan Div: consolidation through war and new institution-dependent roles. The largest birth cohort in Iran\'s history was born; about 1,957,000 births in 1986 against 979,923 in 2024.'),
     P('شبِ سوم، ۱۳۷۶ — بیژن در چاه: شهر خواست از درونِ بازی رأی بدهد. چرخهٔ خاتمی، احمدی‌نژاد، روحانی سه بار همین را تکرار کرد تا جامعه گفت ماجرا تمام است.', 'Night 3, 1997, Bizhan in the well: the city tried to vote from inside the game. The Khatami, Ahmadinejad, Rouhani cycle repeated it three times until society said it was over.'),
     P('شبِ چهارم، ۱۳۸۸ — سیاوش: ارتِ «اصلاح» سوخت. بزرگ‌ترین کوهورت وارد بازاری شد که ظرفیتش را نداشت؛ نتیجه امروز در یک عدد دیده می‌شود: چهل درصدِ بیکاران فارغ‌التحصیل دانشگاه‌اند و بیکاری ۱۵ تا ۲۴ سال ۲۳٫۴٪ است.', 'Night 4, 2009, Siavash: the "reform" trial by fire burned. The biggest cohort entered a market without room; today one number shows it: forty percent of the unemployed are university graduates and 15 to 24 youth unemployment is 23.4 percent.'),
     P('شبِ پنجم، ۱۳۹۷ — نقطهٔ شکستِ نان و خشکسالیِ ساخته‌شده: نرخِ فقر در دو سال حدود هشت واحد بالا رفت و روی ۳۰٪ ماند؛ طبقهٔ متوسط از ۸۴٪ (سناریوی بدون تحریم) به ۵۶٪ رسید، یعنی حدود ۲۸ واحد، بیست و چند میلیون نفر. درآمد سرانه ۵٬۶۱۷ دلار در ۲۰۲۵ در برابر ۷٬۴۴۲ دلار در ۱۹۷۶.', 'Night 5, 2018, the bread breaking point and made-up drought: poverty rose about eight points in two years and settled near 30 percent; the middle class fell from 84 percent (no-sanctions scenario) to 56 percent, about 28 points. Income per head 5,617 dollars in 2025 against 7,442 in 1976.', [], True),
     P('شبِ ششم، ۱۴۰۱ — گُردآفرید: نقش‌ها بازتعریف شدند. زن از «موضوعِ بحث» به سوژهٔ محوری بدل شد و پرونده‌ی گروه‌هایی که به تمامیتِ ارضی نظر دیگری دارند تا حد زیادی بسته شد؛ ۲۹٪ خود را چندقومیتی می‌دانند و ۲۳٪ به پرسشِ قومیت پاسخ ندادند. پژوهشِ کدیور جابه‌جاییِ قدرتِ چانه‌زنی داخلِ خانه را از ماندگارترین تغییرات می‌داند.', 'Night 6, 2022, Gordafarid: roles were redefined. Women moved from topic of debate to central subject; 29 percent call themselves multi-ethnic and 23 percent did not answer the ethnicity question. Kadivar sees the shift of bargaining power inside the home as one of the most lasting changes.', [K['kadivar22']]),
     P('شبِ هفتم، ۱۸ و ۱۹ دی ۱۴۰۴ — سوگِ سیاوشان: «تقریباً همهٔ ما داغداریم» و پدیدهٔ بی‌نظیرِ دست‌افشانی بر مزار. شاخصِ تعیین‌کننده: هیچ ویدیویی برای شروعِ چرخهٔ انتقام بیرون نیامد؛ طبقِ قانونِ طلاییِ میز این مهم‌ترین شاخصِ برد است.', 'Night 7, 8 and 9 January 2026, Mourning of Siavash: "almost all of us are bereaved" and the unique dance at the graves. The deciding indicator: no video came out to start a cycle of revenge, which by the golden rule is the most important win indicator.', [], True),
     P('دورِ جاری، «دریچه باز است، فرایند نیست»: سه شرطِ گذار، یعنی ارادهٔ ملت ✓، دریچهٔ فرصت ✓ و نظام فکری و فرایندِ تأسیس ✗. اسطوره: زال با دستی روی پَر که هنوز نسوزانده.', 'Current round, "the window is open, the process is not": three transition conditions, national will yes, window of opportunity yes, an intellectual system and founding process no. Myth: Zal with his hand on the feather, not yet burned.')],
    [L('simorgh:metaphor', 'استعارهٔ میز', 'The table metaphor'),
     L('simorgh:timeline-tool', 'خطِ زمان (ابزار)', 'Timeline tool'),
     L('simorgh:three-feathers', 'سه پَر', 'The three feathers'),
     L('tarikh:tarikh', 'ویکی تاریخ', 'History wiki')], 'simorgh:game')

new('three-feathers', T('سه پَر، سه چیزی که پَر نیستند، و آستانه', 'Three feathers, three things that are not feathers, and the threshold'),
    T('پَر یک نشانهٔ پرهزینهٔ از پیش‌توافق‌شده است که وقتی روشن شد همه بدانند و بدانند بقیه هم می‌دانند. آنچه می‌سوزد سه چیزِ نامرئی است که شهر دارایی می‌پنداشت و بدهی بود. آستانه یک عدد نیست، یک هم‌زمانی است.',
      'The feather is a pre-agreed costly signal: once lit, everyone knows and knows that others know. What burns are three invisible things the city took for assets that were liabilities. The threshold is not a number but a simultaneity.'),
    [P('پَرِ یکم، ترسِ خصوصی: چیزی که می‌سوزد توهمِ «فقط من این‌طور فکر می‌کنم» است. ابزارش عددِ ۷۲٫۹٪ موافقِ جدایی نهادِ دین از حکومت از پیمایشِ خودِ حاکمیت است که در هشت سال از ۳۰٫۷٪ به آنجا رسیده؛ یک عدد از منبعِ مخالف از هزار شعار مؤثرتر است. هزینه کم، اثر زیاد.', 'Feather 1, private fear: what burns is the illusion "only I think this". The tool is the 72.9 percent in favour of separating religion from state, from the regime\'s own survey, up from 30.7 percent in eight years; one number from the opposing source beats a thousand slogans. Low cost, high effect.', [K['gamaan']], True),
     P('پَرِ دوم، همکاریِ روزمره: اعتصابِ هماهنگ و اعلام‌شده، در یک تاریخ و چند صنف هم‌زمان. چون ۶۰٪ اشتغال غیررسمی است، نه دولت اهرمِ اقتصادیِ کافی بر اکثریت دارد و نه جامعه شبکهٔ حمایتِ رسمی؛ اعتصاب فقط با صندوق ممکن است. هزینهٔ مالیِ سنگین برای فرد.', 'Feather 2, everyday cooperation: a coordinated, announced strike on a set date across several trades. With 60 percent informal employment, neither the state has enough economic leverage over the majority nor society a formal safety net; a strike is possible only with a fund. Heavy financial cost to the individual.'),
     P('پَرِ سوم، حقِ انتقام: گران‌ترینِ سه‌تا. اعلامِ علنی و مکتوب که فردا دادگاه هست و انتقام نیست؛ به همهٔ خطاها رسیدگی می‌شود، اما زمان دارد، مکان دارد، چارچوب دارد. تا جزء دوم و سومِ آن ۱۰–۱۵٪ فردایی برای خود نبینند، هیچ‌جا نمی‌روند. هزینهٔ اخلاقی و روانی برای داغدارترین‌ها.', 'Feather 3, the right of revenge: the costliest. A public written declaration that tomorrow there are courts but no revenge; every wrong will be addressed, with time, place and framework. Until the second and third tier of that 10 to 15 percent see a tomorrow for themselves they go nowhere. Moral and psychological cost for the most bereaved.', [K['kuran']]),
     P('سه چیز که پَر نیستند: جان (هر خشونت پَر را خیس می‌کند نه روشن)؛ زیرساخت (موزه‌ها، بانک مرکزی، خزانه؛ هرچه بیشتر بسوزد امکان تأسیسِ جدید کمتر می‌شود)؛ ایران (تنها میثاقِ پیشینیِ مشترک؛ کسی که مرزها را وسطِ بازی جابه‌جا کند پَر را در چاه می‌اندازد).', 'Three things that are not feathers: life (violence wets the feather rather than lighting it); infrastructure (museums, central bank, treasury; the more burns, the less room for a new founding); Iran (the only shared prior covenant; whoever moves borders mid-game drops the feather in the well).'),
     P('آستانه: سیمرغ وقتی می‌آید که هر سه پَر هم‌زمان بسوزند و دیده شوند، یعنی (الف) اندازهٔ واقعیِ اکثریت برای خودِ اکثریت آشکار شده باشد، (ب) دست‌کم سه صنفِ سراسری بتوانند یک روز هم‌زمان بایستند و گرسنه نمانند، (ج) جزء دوم و سومِ آن ۱۰–۱۵٪ متنی مکتوب برای فردایشان در دست داشته باشند.', 'Threshold: the Simorgh comes only when all three feathers burn at once and are seen: (a) the true size of the majority is visible to itself, (b) at least three national trades can stand together for one day without starving, (c) the second and third tier of the 10 to 15 percent hold a written text of their tomorrow.', [K['olson']], True),
     P('ماتریسِ هماهنگی: خانهٔ پایین-راستِ «من صبر می‌کنم و بقیه هم صبر می‌کنند» تعادلِ امروز است. راهِ خروج تغییرِ ترجیحِ مردم نیست (سال‌هاست تغییر کرده) بلکه تغییرِ باورِ هر نفر دربارهٔ رفتارِ بقیه است؛ و این دقیقاً کارِ پَر است.', 'Coordination matrix: the bottom-right cell, "I wait and the others wait", is today\'s equilibrium. The way out is not changing people\'s preference (it changed years ago) but each person\'s belief about the others\' behaviour; exactly what the feather does.')],
    [L('soc:threshold-models-of-collective-behaviour', 'مدل آستانه', 'Threshold model'),
     L('soc:preference-falsification', 'تحریف ترجیحات', 'Preference falsification'),
     L('simorgh:ten-unbuilt-roles', 'ده نقشِ نساخته', 'Ten unbuilt roles'),
     L('simorgh:threshold-simulator', 'شبیه‌ساز آستانه', 'Threshold simulator')], 'simorgh:game')

# ---------------- characters ----------------
CH = GAME['CH']; EXIST = CH[:27]; UNB = CH[27:]
TL = {'mafia': 'جناح مافیا', 'city': 'جناح شهر', 'indie': 'مستقل‌ها'}
ZNf = GAME['ZN']


def chp(c):
    return P(f"{c['n']} ({ZNf.get(c['z'], c['z'])}) — {c['role']}. مثالِ واقعی: {c['who']}. ریشهٔ اسطوره‌ای: {strip(c['myth'])}",
             f"{c['n']} ({c['z']}): archetype of the table. Real-world examples and myth root as in the Persian text.")


def chgroup(slug, fa, en, sfa, sen, items, parent='simorgh:game', links=()):
    new(slug, T(fa, en), T(sfa, sen), [chp(c) for c in items], list(links), parent)


chgroup('characters-mafia', 'شخصیت‌های جناح مافیا', 'Mafia-faction characters',
        'نُه شخصیت که بازی را نگه می‌دارند: از روایت‌ساز و دربان تا رانت‌خوار. شخصیت‌ها تیپ‌اند، نه آدمِ مشخص؛ هیچ نشانِ حزبی، دولتی یا مذهبیِ واقعی ندارند.',
        'Nine characters that keep the game going, from narrator and gatekeeper to rent-seeker. They are archetypes, not named people; none carries a real party, state or religious emblem.',
        [c for c in EXIST if c['t'] == 'mafia'], links=[L('simorgh:roles-ruling', 'نقش‌های اجتماعیِ حاکمیت', 'Ruling social roles')])
chgroup('characters-city', 'شخصیت‌های جناح شهر', 'City-faction characters',
        'شخصیت‌های شهر: از شهروند عادی و آمارگر مستقل تا ضامن و مترجم؛ و «مردد درونِ نظام» که قابل چرخش است.',
        'City characters, from ordinary citizen and independent statistician to guarantor and translator; plus the "doubter inside the system", who can turn.',
        [c for c in EXIST if c['t'] == 'city'], links=[L('simorgh:roles-citizen', 'نقش‌های اجتماعیِ شهروندان', 'Citizen social roles')])
chgroup('characters-indie', 'شخصیت‌های مستقل', 'Independent characters',
        'پنج شخصیتِ بیرون از دو جناح: ناظر، حسابِ پرسروصدا، صاحبِ زیرساخت، میانجی و قدرتِ خارجی؛ آن‌ها طولِ بازی را تعیین می‌کنند.',
        'Five characters outside both factions: observer, noisy account, infrastructure owner, mediator and outside power; they set how long the game lasts.',
        [c for c in EXIST if c['t'] == 'indie'], links=[L('simorgh:roles-independent', 'نقش‌های اجتماعیِ مستقل‌ها', 'Independent social roles')])

new('ten-unbuilt-roles', T('ده نقشی که شهر هنوز نساخته', 'Ten roles the city has not yet built'),
    T('شهر چون ناقص است می‌بازد، نه چون ضعیف. ده کارتِ خالی هر کدام یک سازوکار است که چند نفر می‌سازندش و بعد از سازندگانش مستقل می‌شود؛ هر کدام یکی از شش قفلِ میز را می‌شکند.',
      'The city loses because it is incomplete, not weak. Ten blank cards, each a mechanism that several people build and that then becomes independent of its builders; each breaks one of the six locks on the table.'),
    [P('شش قفلی که ده نقش می‌شکنند: نبودِ نقطهٔ کانونی، نامتقارنیِ هزینه، ترجیحِ پنهان، ترسِ جزء دوم و سوم از فردا، فقدانِ فرایندِ تأسیس، و خطرِ فردمحوری. درسِ چهار دههٔ گذشته: نه انگیزه کم بوده نه استعداد، نهاد کم بوده.',
       'Six locks broken by the ten roles: no focal point, cost asymmetry, hidden preference, fear of the second and third tier of tomorrow, no founding process, and personality dependence. The lesson of four decades: neither motivation nor talent was short, institutions were.')]
    + [P(f"{n} — {strip(b)} (خروجی: {strip(o)})", f"{n}: mechanism and expected output as in the Persian text.") for n, b, o in GAME['MECH']],
    [L('simorgh:three-feathers', 'سه پَر', 'The three feathers'), L('simorgh:covenantal-transition', 'گذارِ میثاقی', 'Covenantal transition'),
     L('simorgh:birds-30', 'سی مرغ', 'Thirty birds')], 'simorgh:game')

# ---------------- 47 roles ----------------
WH = PLAN['why']


def roles(slug, fa, en, sfa, sen, key, links2=()):
    items = [r for r in WH if r[0] == key]
    pts = []; lk = []
    for _, name, sub, txt, ls in items:
        pts.append(P(f'{name} ({sub}): {txt}', f'{name} ({sub}): the science behind the role, as in the Persian text.'))
        for t, u in ls:
            cid = planlink(u)
            if cid and not any(l['to'] == cid for l in lk): lk.append(L(cid, t, t))
    new(slug, T(fa, en), T(sfa, sen), pts, lk[:14] + list(links2), 'simorgh:game')


roles('roles-ruling', 'نقش‌های اجتماعیِ حاکمیت (۱۲ نقش)', 'Ruling-side social roles (12)',
      'دوازده نقش در سمتِ حاکمیت، هرکدام با علمی که می‌گوید چرا این نقش پایدار است یا کجا می‌شکند: از «پدرخوانده» و «بازوی مسلح» تا نقش‌های خنثی‌شونده.',
      'Twelve roles on the ruling side, each with the science that says why it is stable or where it breaks.', 'mafia')
roles('roles-citizen', 'نقش‌های اجتماعیِ شهروندان (۱۸ نقش)', 'Citizen social roles (18)',
      'هجده نقشِ شهر، از کاسب و کارگر تا معلم، پرستار و دانشجو، هرکدام با پشتوانهٔ علمیِ اهرمی که در دست دارد.',
      'Eighteen city roles, from shopkeeper and worker to teacher, nurse and student, each with the science behind the leverage it holds.', 'citizen')
roles('roles-independent', 'نقش‌های اجتماعیِ مستقل‌ها و میانی (۱۷ نقش)', 'Independent and intermediate social roles (17)',
      'هفده نقشِ میانی و مستقل، از ناظر و میانجی تا صاحبانِ زیرساخت و قدرت‌های بیرونی.',
      'Seventeen intermediate and independent roles, from observers and mediators to infrastructure owners and outside powers.', 'third')
new('roles-47', T('۴۷ نقشِ اجتماعی: نقشه و ماتریسِ تصمیم', '47 social roles: map and decision matrix'),
    T('جامعه روی میز به ۴۷ نقش شکسته شده: ۱۲ در سمتِ حاکمیت، ۱۸ شهروند، ۱۷ مستقل و میانی. هر نقش یک اهرم و یک هزینهٔ مخصوص دارد؛ ماتریس نشان می‌دهد هر نقش کجای میز می‌نشیند.',
      'Society on the table is split into 47 roles: 12 on the ruling side, 18 citizens, 17 independent and intermediate. Each has its own leverage and cost; the matrix shows where each sits.'),
    [P('سه گروه: ۱۲ نقشِ حاکمیت، ۱۸ نقشِ شهر، ۱۷ نقشِ مستقل و میانی؛ هر کدام در یک مدخلِ جدا آمده.', 'Three groups, each in its own entry.'),
     P('این تقسیم فقط در سطحِ نقش و جمعیت است؛ هیچ فرد یا فهرستی از آدم‌های واقعی ساخته نمی‌شود و ساخته نخواهد شد.', 'The split is at the level of roles and populations only; no list of real people is or will be built.', [], True),
     P('ابزار: صفحهٔ نقش‌ها (ماتریس تصمیم)، «چرا؟» (علمِ هر نقش) و میزِ دایره‌ای.', 'Tools: roles page (decision matrix), the "why" page (science of each role) and the circle table.')],
    [L('simorgh:roles-ruling', '۱۲ نقش حاکمیت', '12 ruling roles'), L('simorgh:roles-citizen', '۱۸ نقش شهروند', '18 citizen roles'),
     L('simorgh:roles-independent', '۱۷ نقش مستقل', '17 independent roles'), L('simorgh:tools-directory', 'فهرست ابزارها', 'Tools directory')], 'simorgh:game')

new('ten-turn-game', T('بازیِ ده‌نوبتی و حدسِ گذارها', 'The ten-turn game and the transitions guess'),
    T('دو بازیِ کوچک که می‌شود امتحان کرد: یک بازیِ ده‌نوبتیِ آستانه، و ابزاری که از تو می‌خواهد پانزده گذارِ جهانی را حدس بزنی تا ببینی شهودت با تاریخ کجا جور نیست.',
      'Two small games to try: a ten-turn threshold game, and a tool that makes you guess fifteen world transitions to see where your intuition and history part.'),
    [P('بازیِ ده‌نوبتی (sim): هر نوبت یک تصمیم دربارهٔ هماهنگی و هزینه؛ هدفش حس‌کردنِ منطقِ آستانه است، نه پیش‌بینی.', 'The ten-turn game: each turn a decision about coordination and cost; it is to feel the threshold logic, not to predict.'),
     P('پانزده گذار (transitions): حدس بزن و ببین؛ مناسبِ یک شبِ دورهمی و میزِ دایره‌ای.', 'Fifteen transitions: guess and see; suited to an evening gathering and the circle table.')],
    [L('simorgh:threshold-simulator', 'شبیه‌ساز آستانه', 'Threshold simulator'), L('simorgh:circle-table', 'میزِ دایره‌ای', 'Circle table')], 'simorgh:game')

new('threshold-simulator', T('شبیه‌سازِ آستانه', 'Threshold simulator'),
    T('ابزاری که نشان می‌دهد وقتی هر کس آستانهٔ پیوستنِ خودش را دارد و فقط اندازهٔ دیده‌شده را می‌بیند، یک جامعه چرا ساکت می‌ماند و چرا ناگهان می‌ریزد.',
      'A tool showing why a society where everyone has a personal joining threshold and sees only the visible size stays silent, then suddenly falls.'),
    [P('مدلِ آستانه (گرانوتر، کوران): پیوستن به شرطِ دیدنِ کافیِ دیگران؛ یک نفرِ اضافه می‌تواند همه‌چیز را بچرخاند.', 'Threshold model: joining conditional on seeing enough others; one more person can tip everything.', [K['kuran91'], K['kuran']]),
     P('این ابزار آموزشی است و پیش‌بینی نمی‌کند؛ همان‌طور که کرزمن می‌گوید پیش از ۱۳۵۷ حتی کسانی که در خیابان بودند آن را شدنی نمی‌دانستند.', 'Educational, not predictive; as Kurzman notes, even people in the street before 1979 did not think it possible.', [K['kurzman']])],
    [L('soc:threshold-models-of-collective-behaviour', 'مدل آستانه', 'Threshold model'), L('simorgh:three-feathers', 'سه پَر', 'The three feathers')], 'simorgh:game')
