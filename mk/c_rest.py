from common import *
from a_game import K, strip
from b_evidence import SRC, S_
import re

# ===================== HISTORY =====================
new('two-irans', T('دو ایران: تشیع چطور ایرانی شد', 'Two Irans: how Shi\'ism became Iranian'),
    T('روایتِ تاریخیِ اینکه چرا ایران شیعه شد و نه چیزِ دیگر، بر پایهٔ پژوهش‌های دانشگاهی. نه تاریخ‌نگاری از بالا و نه توطئه؛ تفسیری است با دفتر مناقشهٔ علنی، و کارکردگرایی (هر باور به چه کار دولت آمد) را به‌عنوان یک برش می‌خواند نه کلِ واقعیت.',
      'A historical account of why Iran became Shia, based on academic research; an interpretation with an open dispute ledger that treats functionalism as one slice, not the whole of reality.'),
    [P('صفویه هم در آغاز شیعه نبود: پیش از آن شهرهایی مثل قم، کاشان، سبزوار و ری قرن‌ها شیعه بودند، ایلخان الجایتو در ۱۳۱۰ به تشیعِ دوازده‌امامی گروید، و «وفاداریِ علوی» میانِ سنیانِ ایران گسترده بود. صفویه تشیع را بر بستری آماده تحمیل و تسریع کرد؛ «واردات محض» غلط است.', 'The Safavids did not begin Shia either: Qom, Kashan, Sabzevar and Rayy had been Shia for centuries, Ilkhan Oljeitu converted in 1310, and Alid loyalism was widespread among Iranian Sunnis. The Safavids imposed and sped up Shi\'ism on a prepared ground; "pure import" is wrong.', [SRC['abisaab'], SRC['newman']]),
     P('پرسشِ معکوس، چرا یهودی نشد: یهودیتِ متأخر دینِ تبلیغی نیست و هرگز قدرتِ دولتی پشتش نبود، ولی «ناممکن» هم نبود؛ رشتهٔ یهودی کهن‌ترین پیوندِ ایران است (نک. ایران و اسرائیل).', 'The reverse question, why not Jewish: late Judaism is not a missionary religion and never had state power behind it, yet it was not "impossible"; the Jewish strand is Iran\'s oldest tie.', [SRC['sarshar']]),
     P('دو قطبِ تمدنِ ایران: قطبِ ایرانشهری و قطبِ اسلامی–شیعی؛ تمدنِ ایران حاصلِ هر دو است نه فقط یکی، و هیچ‌کدام «ایرانِ واقعی» نیست.', 'Two poles of Iranian civilisation: the Iranshahri pole and the Islamic–Shia pole; Iranian civilisation is the product of both, neither alone is the "real Iran".'),
     P('پاسخ به دو ادعای پرتکرار: غیرایرانی‌ها بر ایران حکومت نمی‌کنند؛ و «چپ از ایدئولوژی سوءاستفاده می‌کند» تعمیمی است که صفحه نمی‌پذیرد و استدلالش را می‌آورد.', 'Answering two frequent claims, with arguments given rather than assumed.', [], True)],
    [L('simorgh:clerical-rise', 'هشت پله تا قدرت', 'Eight steps to power'), L('simorgh:disputes-ledger', 'دفترِ مناقشه‌ها', 'Dispute ledger'),
     L('simorgh:iran-israel', 'ایران و اسرائیل', 'Iran and Israel'), L('tarikh:tarikh', 'ویکی تاریخ', 'History wiki')], 'simorgh:history')

new('clerical-rise', T('پانصد سال بالا رفتن: هشت پله', 'Five centuries of rising: eight steps'),
    T('روحانیتِ شیعه یک‌شبه قدرت نگرفت: تا ۱۵۰۱ میلادی اکثریتِ ایران سنی بود و بعد، هشت پلهٔ انباشتِ نهادی که هیچ‌کدام بعداً پس گرفته نشد. درسِ امروز: سازمان‌یافتگی، نه محبوبیت، تعیین‌کنندهٔ برنده است.',
      'The Shia clergy did not take power overnight: until 1501 most Iranians were Sunni; then eight steps of institutional accumulation, none later reversed. The lesson for today: organisation, not popularity, picks the winner.'),
    [P('پلهٔ یکم، صفوی: علما وارد شدند، حوزه ساخته شد، اوقاف (زمین، بازار، مدرسه، کاروانسرا) به آن‌ها سپرده شد؛ گروهِ عالم مالک شد.', 'Step 1, Safavid: clergy arrived, the seminary was built and endowments were entrusted to them; scholars became owners.', [SRC['abisaab'], SRC['newman']]),
     P('پلهٔ دوم، نادرشاه: پس از سقوطِ اصفهان در ۱۷۲۲ نادر خواست تشیع را از هویتِ رسمی پایین بکشد (مذهبِ پنجمِ «جعفری»)؛ علما به عتباتِ زیرِ حاکمیتِ عثمانی رفتند و نهاد را بیرون از دسترسِ حاکمِ ایرانی از نو ساختند. این نقش بزرگ‌نمایی شده است: مهاجرت پیش از او هم بود.', 'Step 2, Nader Shah: after Isfahan fell in 1722 Nader tried to lower Shi\'ism from the official identity; clergy went to the Ottoman-ruled shrine cities and rebuilt the institution beyond the Iranian ruler\'s reach. The role is exaggerated: migration predates him.', [SRC['tucker'], SRC['matthee']]),
     P('پلهٔ سوم، نبردِ اصولی و اخباری: پیروزیِ اصولی‌ها (وحید بهبهانی) یعنی تقلید از مجتهدِ زنده واجب است، که سه چیز می‌سازد: سلسله‌مراتب، پیرو (مقلد) و خزانه (خمس).', 'Step 3, Usuli versus Akhbari: the Usuli victory (Behbahani) made following a living jurist obligatory, creating hierarchy, followers and a treasury.', [SRC['arjomand']]),
     P('پلهٔ چهارم، قاجار: ایلِ بدونِ ادعای دینی مشروعیت را از علما خرید؛ در این معامله طرفی که نیاز بیشتری داشت (دولت) ضعیف‌تر بود.', 'Step 4, Qajar: a tribe with no religious claim bought legitimacy from the clergy; the party with more need, the state, was weaker.', [SRC['akhavi']]),
     P('پلهٔ پنجم، جهاد: در جنگ‌های ایران و روس فقها اختیارِ اعلامِ جهادِ ابتدایی را که از امامِ معصوم بود به خود گرفتند؛ جنگ باخته شد اما هزینهٔ سیاسی را دولت پرداخت نه روحانیت.', 'Step 5, jihad: in the Russo-Persian wars jurists took the authority to declare offensive jihad, which belonged to the infallible imam; the war was lost but the state paid the political cost.', [SRC['arjomand']]),
     P('پلهٔ ششم، انصاری و پول: پس از ۱۸۵۰ یک نفر مرجعِ بلامنازعِ جهانِ شیعه شد و نظامِ وجوهات را قاعده‌مند کرد. «موقوفهٔ اوده» (پولِ هند که بریتانیا توزیع می‌کرد) تصویرِ استقلالِ کاملِ مالی را پیچیده‌تر می‌کند، اما پژوهش نشان می‌دهد پول‌دادن لزوماً کنترل نخرید.', 'Step 6, Ansari and money: after 1850 one man became the undisputed authority of the Shia world and regularised dues. The Oudh Bequest (Indian money distributed by Britain) complicates the picture of full financial independence, but research shows paying did not buy control.', [SRC['litvak']]),
     P('پلهٔ هفتم، باب: جنبشِ بابی روحانیتِ رسمی را کنارِ دولت به‌عنوانِ نگهبانِ نظم تعریف کرد و یک دشمنِ درونیِ دائمی داد.', 'Step 7, the Bab: the Babi movement defined the official clergy as a guardian of order beside the state and gave it a permanent internal enemy.', [SRC['amanat']]),
     P('پلهٔ هشتم، امتیازات و کشفِ اهرم: امتیازِ رویتر (۱۸۷۲) و تنباکو (۱۸۹۰). تحریمِ سراسری کار کرد و قرارداد در ۱۸۹۲ لغو شد؛ ائتلافِ بازار و روحانیت (یکی پول دارد و دیگری مشروعیت) موتورِ ۱۸۹۱، مشروطه و ۱۳۵۷ شد.', 'Step 8, concessions and discovering leverage: the Reuter (1872) and tobacco (1890) concessions. The nationwide boycott worked and the contract was cancelled in 1892; the bazaar-clergy coalition (one has money, the other legitimacy) was the engine of 1891, the Constitution and 1979.', [SRC['keddie81']]),
     P('۱۳۵۷ و درسِ امروز: مردم مذهبی‌تر از دهه‌های پیش نشده بودند؛ پرسشِ درست این است که چرا وقتی رژیم افتاد فقط یک نیرو آمادهٔ گرفتنِ قدرت بود (حزب توده پس از ۱۳۳۲ متلاشی شد، جبههٔ ملی فلج شد). سازمان‌یافتگی، نه محبوبیت، برنده بود؛ هر نیرویی که امروز محبوب است ولی شبکهٔ عملیاتی ندارد همان‌جا می‌ایستد که جبههٔ ملی ایستاد.', 'Nineteen seventy-nine and today\'s lesson: people had not become more religious; the right question is why only one force was ready to take power when the regime fell. Organisation, not popularity, won.', [SRC['abrah82'], K['kurzman']], True)],
    [L('simorgh:two-irans', 'دو ایران', 'Two Irans'), L('simorgh:disputes-ledger', 'دفترِ مناقشه‌ها', 'Dispute ledger')], 'simorgh:history')

new('disputes-ledger', T('دفترِ مناقشه‌ها: هفت ادعای مرکزیِ «دو ایران» و شاهدِ نقضشان', 'Dispute ledger: the seven central claims of "Two Irans" and their counter-evidence'),
    T('هر چه در «دو ایران» خوانده می‌شود تفسیر است نه واقعیتِ خام. دفتر هفت ادعای مرکزی را می‌گیرد و برای هرکدام شاهدِ نقض، تعبیرِ رقیب و وزنِ نهایی می‌دهد.',
      'Everything in "Two Irans" is interpretation, not raw fact. The ledger takes the seven central claims and gives each its counter-evidence, rival reading and final weight.'),
    [P('۱. «تشیع را صفویه از بیرون آورد»: باید بازنویسی شود؛ تحمیل و تسریع بر بستری آماده، نه واردات.', '1. "The Safavids brought Shi\'ism from outside": must be rewritten; imposition and acceleration on a ready ground.', [SRC['newman']]),
     P('۲. «کرکی در ۱۵۳۰ نخستین ادعای ولایتِ سیاسیِ فقیه را ثبت کرد»: ریشه‌ها واقعی‌اند اما خطِ سیر ناپیوسته است؛ نراقی (د. ۱۸۲۹) حلقهٔ گمشده است و نوآوریِ خمینی در دامنه بود نه اصل.', '2. "Karaki in 1530 recorded the first claim of the jurist\'s political guardianship": roots are real but the line is discontinuous; Naraqi is the missing link and Khomeini\'s innovation was in scope.', [SRC['arjomand'], SRC['abrah93']]),
     P('۳. «نادرشاه با مصادرهٔ اوقاف ناخواسته روحانیت را مستقل کرد»: سازوکار درست، نقش بزرگ‌نمایی‌شده؛ یکی از چند عامل نه علتِ یگانه.', '3. "Nader\'s confiscations unintentionally made the clergy independent": mechanism right, role exaggerated; one of several factors.', [SRC['tucker']]),
     P('۴. «استقلالِ مالی از مردمِ ایران آمد»: نتیجه درست، مسیر ناقص؛ پولِ اوده را فراموش نکن، و درسِ جانبی: پول‌دادن کنترل نمی‌خرد.', '4. "Financial independence came from Iranians": conclusion right, path incomplete; remember the Oudh money, and the side lesson that paying does not buy control.', [SRC['litvak']]),
     P('۵. «فتوای تنباکو تنهایی شاه را شکست داد»: رویداد واقعی، روایتش بعداً بزرگ شد؛ انتسابِ فتوا به یک نفر سندِ قطعی ندارد و فشارِ روسیه و اعتراضِ بازار عاملِ مستقل بودند؛ بزرگ‌شدنِ روایت خودش داده است (اثباتِ مفهوم).', '5. "The tobacco fatwa broke the Shah alone": real event, later inflated; attribution to one man lacks decisive documents and Russian pressure and bazaar protest were independent factors.', [SRC['keddie81']]),
     P('۶. «مسجد تنها شبکهٔ بازمانده بود»: باید محدود شود؛ ضربهٔ نهایی اعتصابِ نفت بود که شبکه‌های کارگری و چپ سازمانش دادند. مسجد توضیح می‌دهد چرا روحانیت توانست هماهنگ کند نه چرا در نبردِ ۵۸ تا ۶۰ برد؛ کرزمن کلِ توضیحِ ساختارگرا را رد می‌کند.', '6. "The mosque was the only surviving network": must be limited; the final blow was the oil strike organised by labour and left networks; Kurzman rejects the whole structuralist explanation.', [K['kurzman'], SRC['abrah82']]),
     P('۷. «یک نهاد تا وقتی متحدِ مردم است که دولت نباشد»: گرایشِ قوی نه قانون (کلیسای لهستان، کنگرهٔ ملیِ آفریقا نقض‌اند)؛ متغیرِ واقعی شاید وجودِ سازوکارِ برکناری است.', '7. "An institution is the people\'s ally only while it is not the state": a strong tendency, not a law; the real variable may be a removal mechanism.', [SRC['michels']]),
     P('چالش بر کلِ صفحه: روایتِ غالب کارکردگرایانه است و ایمان را سیستماتیک نمی‌بیند؛ تقلیلِ هر باور به سودمندی‌اش همان‌قدر تک‌بعدی است که تقلیلِ هر رویداد به توطئه. صفحه یک برش است نه کلِ واقعیت.', 'A challenge to the whole page: the dominant account is functionalist and systematically misses faith; reducing each belief to its usefulness is as one-dimensional as reducing each event to conspiracy.', [], True)],
    [L('simorgh:two-irans', 'دو ایران', 'Two Irans'), L('simorgh:clerical-rise', 'هشت پله', 'Eight steps'), L('simorgh:audit', 'ممیزی', 'Audit')], 'simorgh:history')

new('iran-israel', T('ایران و اسرائیل: ۴۷ سال در برابر ۲۶۰۰ سال', 'Iran and Israel: 47 years against 2,600'),
    T('دشمنیِ رسمیِ دو دولت ۴۷ سال عمر دارد و رابطهٔ دو سرزمین حدودِ ۲۶۰۰ سال؛ یعنی دشمنی کمتر از دو درصدِ عمرِ رابطه. این صفحه دربارهٔ یک دولت است، نه یک دین و نه یک جامعه، و جنگ را ندیده نمی‌گیرد و دربارهٔ حق‌وناحقش حکم نمی‌دهد.',
      'The official enmity of the two states is 47 years old, the relation between the lands about 2,600; the enmity is under two percent of the relation. It concerns a state, not a religion or a community, does not ignore the war and does not rule on its rights and wrongs.'),
    [P('حسابِ ساده: حضورِ یهودیان در ایران به حدودِ ۲۶۰۰ سال می‌رسد و دشمنیِ رسمی از ۱۳۵۷ است؛ ۴۷ از ۲۶۰۰ حدود ۱٫۸٪ است. (فرقِ ۲۶۰۰ و ۲۷۰۰ از نقطهٔ آغازِ متفاوت است.)', 'Simple arithmetic: Jewish presence in Iran spans about 2,600 years, official enmity dates from 1979; 47 of 2,600 is about 1.8 percent. (The 2,600 versus 2,700 difference comes from different starting points.)', [SRC['iranica']]),
     P('آنچه مشترک است: کوروش (حدود ۵۳۷ پ.م) به تبعیدیانِ بابل اجازهٔ بازگشت داد؛ یهودیانِ ایران از قدیمی‌ترین اجتماع‌های پیوستهٔ یهودی‌اند؛ تلمودِ بابلی در خاکِ ساسانی نوشته شد؛ عبدالحسین سرداری در پاریسِ اشغالی برای یهودیانِ ایرانی‌تبار پیگیری کرد (رقمِ ۱۵۰۰ نفر را منبعِ اصلی تأیید نمی‌کند و ردش شده است)؛ ایران در ۱۹۵۰ اسرائیل را عملاً به‌رسمیت شناخت و از ۱۹۵۷ نفت فروخت.', 'What is shared: Cyrus (c. 537 BC) allowed the Babylonian exiles to return; Iran\'s Jews are among the oldest continuous Jewish communities; the Babylonian Talmud was written on Sasanian soil; Sardari acted in occupied Paris (the 1,500 figure is not confirmed by the primary source and was rejected); Iran de facto recognised Israel in 1950 and sold oil from 1957.', [SRC['ushmm'], SRC['sarshar'], SRC['iranica']]),
     P('تصحیحِ ادعا: «تا ۱۹۷۹ تقریباً بی‌وقفه مثبت» اغراق است؛ در صفوی و اوایلِ قاجار موجِ تغییرِ دینِ اجباری، محله‌های جدا و احکامِ نجاست بود. قابِ درست «بهتر از اروپای هم‌دوره» است. و «استوانهٔ کوروش نخستین منشورِ حقوقِ بشر است» ردشده است: کتیبه‌ای شاهیِ استاندارد است و خوانشِ حقوق‌بشری عمدتاً ساختهٔ دههٔ ۱۹۵۰–۷۰ است.', 'Correction: "almost uninterruptedly positive until 1979" is an exaggeration; the right frame is "better than contemporary Europe". And "the Cyrus Cylinder is the first human-rights charter" is refuted.', [SRC['iranica']], True),
     P('آنچه صفحه نمی‌گوید: جنگ درست بود؛ تغییر از بیرون می‌آید (برعکس: هیچ‌کس با حملهٔ خارجی به دموکراسی نرسیده)؛ مسئلهٔ فلسطین را حل می‌کند؛ یهودیانِ ایران آزادند (زیرِ همان حکومتِ دیگران زندگی می‌کنند و در جنگ روی لبهٔ باریکی راه می‌روند)؛ ایران همیشه با یهودیان خوب بود؛ و از کسی نمی‌خواهد ببخشد، فقط می‌گوید خشم را به آدرسِ درست بفرستید.', 'What the page does not say: that the war was right; that change comes from outside; that it solves the Palestinian question; that Iran\'s Jews are free; that Iran was always good to Jews; or that anyone should forgive.'),
     P('جملهٔ اجباریِ ارائهٔ اروپا که در هر نسخه می‌ماند: «این دربارهٔ یک دولت است، نه یک دین و نه یک جامعه.»', 'The mandatory sentence of the Europe deck, kept in every version: "This concerns a state, not a religion and not a community."')],
    [L('simorgh:claims-iran-israel', 'ادعاهای ایران و اسرائیل', 'Iran-Israel claims'), L('simorgh:europe-deck', 'ارائهٔ اروپا', 'Europe deck'),
     L('simorgh:two-irans', 'دو ایران', 'Two Irans')], 'simorgh:history')

new('timeline-tool', T('خطِ زمان: ۸۴ ادعا روی زمان', 'Timeline: the 84 claims on time'),
    T('همان ۸۴ ادعا این بار روی محور زمان در سه بازه که عرضِ برابر ندارند (۲۲۵۰ سال، ۴۰۰ سال، ۱۳۰ سال)؛ چگالیِ رویداد در بازه‌ها قابل‌مقایسه نیست.',
      'The same 84 claims on a time axis in three spans of unequal width (2,250, 400 and 130 years); event density is not comparable across spans.'),
    [P('بازه‌ها: «باستان تا صفویه» (۵ ادعا)، «چهار قرنِ ساخته‌شدن» (۱۱ ادعا) و دورهٔ معاصر؛ هر ردیف ردهٔ اعتبار و پیوند به سطرِ کاملِ ادعا دارد.', 'Spans: ancient to Safavid (5 claims), four centuries of making (11 claims), and the contemporary period; each row has a tier and a link to the full claim row.'),
     P('هشدار مقیاس: روی یک محورِ خطی کلِ دورهٔ معاصر یک خطِ نازک می‌شد.', 'Scale warning: on one linear axis the whole contemporary period would be a thin line.')],
    [L('simorgh:dataset-84', 'دیتاست', 'Dataset'), L('simorgh:seven-nights', 'هفت شب', 'Seven nights')], 'simorgh:history')

# ===================== STRATEGY =====================
new('three-paths', T('سه راه و راهِ صفر', 'Three paths and path zero'),
    T('سه شاخهٔ ممکن، هرکدام در جای دیگری از جهان اجرا شده و نتیجه‌اش را می‌دانیم؛ پیش‌بینی نیستند. تفاوتشان در «حق بودن» نیست، در هزینه است. ماندن هم راهی است («راه صفر») و قیمتش کمتر نیست، فقط آهسته‌تر پرداخت می‌شود.',
      'Three possible branches, each run elsewhere in the world with known outcomes; not predictions. They differ in cost, not in being right. Staying is also a path ("path zero") and costs no less, only more slowly.'),
    [P('راهِ یکم (توصیه‌شده)، گذارِ میثاقی: الگوها آفریقای جنوبی ۱۹۹۰–۹۴، لهستان ۱۹۸۹، شیلی ۱۹۸۸–۹۰؛ سازوکار میثاقِ حداقلیِ پیشینی، عفوِ مشروط در برابرِ اعترافِ کامل، تاریخِ مشخصِ رأی‌گیری و حفظِ زیرساخت و بوروکراسی. خطرِ اصلی: اجماعِ نخبگانی حاصل نشود، همان ✗ امروز.', 'Path 1 (recommended), covenantal transition: models South Africa 1990-94, Poland 1989, Chile 1988-90; mechanism: a prior minimal covenant, conditional amnesty for full confession, a fixed vote date, infrastructure and bureaucracy kept. Main risk: no elite consensus, today\'s "no".', [K['odon'], K['lw']]),
     P('راهِ دوم، گسستِ سریع: الگوها صربستان ۲۰۰۰، تونس ۲۰۱۱ و، با احتیاطِ فراوان، سوریهٔ اخیر؛ سریع‌تر اما فردای بی‌نقشه. هشدارِ متن: قیاس با سوریه خوش‌بینانه است و تجربهٔ آن هنوز شکل می‌گیرد.', 'Path 2, rapid rupture: models Serbia 2000, Tunisia 2011 and, with great caution, recent Syria; faster but a tomorrow without a plan.', [SRC['hunt']], True),
     P('راهِ سوم (پرهیز)، چرخهٔ خشونت: لیبی ۲۰۱۱، سوریه ۲۰۱۱–۲۴، عراق ۲۰۰۳؛ سقوط با انتقام، تجزیهٔ اقتدار، بازیگرِ مسلحِ محلی و بعد خارجی. خطری که همهٔ طرف‌ها می‌بینند: درغلتیدن به اقتدارگراییِ تازه.', 'Path 3 (avoid), cycle of violence: Libya 2011, Syria 2011-24, Iraq 2003; fall with revenge, fragmenting authority, local then foreign armed actors.', [SRC['walter'], SRC['dodge']]),
     P('راهِ صفر، ادامهٔ وضع موجود: باروریِ زیر ۱٫۵، جمعیتِ دانشجویی از ۴٫۸ به ۳٫۱۸ میلیون، سالمندی با پنج برابرِ نرخِ رشدِ کل و خروجِ سالانهٔ مغزها؛ گران‌ترین سناریو نیست اما تنها سناریویی است که در آن هیچ‌کس نمی‌برد.', 'Path zero, status quo: fertility under 1.5, student population from 4.8 to 3.18 million, ageing at five times the overall growth and yearly brain drain; not the costliest but the only one where nobody wins.')],
    [L('simorgh:covenantal-transition', 'گذارِ میثاقی و برنامهٔ ۹۰/۹/۶۰۰', 'Covenantal transition and the 90/9/600 plan'), L('simorgh:cost-model', 'برآوردِ هزینه', 'Cost model'), L('simorgh:claims-model', 'ادعاهای مدل', 'Model claims')], 'simorgh:strategy')

new('covenantal-transition', T('گذارِ میثاقی و برنامهٔ ۹۰ روز / ۹ ماه / ۶۰۰ روز', 'Covenantal transition and the 90 day / 9 month / 600 day plan'),
    T('راهِ یکم اگر بخواهد از حرف به فرایند بدل شود سه بازهٔ زمانی دارد و هیچ‌کدام به مجوزِ کسی نیاز ندارد. هر بازه یک یا چند قفلِ میز را می‌شکند.',
      'If path 1 is to turn from talk into process it has three time spans, none needing anyone\'s permission. Each breaks one or more locks of the table.'),
    [P('۹۰ روز، سوزاندنِ پَرِ یکم: ساختنِ «آمارگرِ مستقل» و «نهادِ شفافیت» که هر ماه اندازهٔ واقعیِ اکثریت را منتشر کند و ادعای هر دو طرف را راستی‌آزمایی کند، و انتشارِ نسخهٔ صفرِ میثاقِ حداقلی در چهار بند با امضای فراجناحی. قفل‌ها: آبشارِ اطلاعاتی، نبودِ نقطهٔ کانونی.', '90 days, burning feather one: build an independent statistician and a transparency body that publishes the majority\'s true size monthly and fact-checks both sides, and issue version zero of the minimal covenant in four clauses with cross-camp signatures. Locks: information cascade, no focal point.'),
     P('۹ ماه، ساختنِ صندوق و سپر: «صندوقِ پشتیبانیِ اعتصاب» (حقوقِ یک تا سه ماه) و «حامی و پوشش‌دهنده» (شبکهٔ حقوقی-درمانیِ داوطلب)، و انتشارِ متنِ عدالتِ انتقالی با عفوِ مشروط که حقوق‌دانانِ داخل و خارج امضا کنند. قفل‌ها: نامتقارنیِ هزینه، ترسِ جزء دوم و سوم.', '9 months, building fund and shield: a strike-support fund (one to three months\' pay) and a patron-and-cover network (volunteer legal and medical), plus a transitional-justice text with conditional amnesty signed by lawyers inside and outside. Locks: cost asymmetry, fear of the second and third tier.', [SRC['elster'], SRC['hayner']]),
     P('۶۰۰ روز، رأیِ مؤسسان: پیش‌نویسِ قانونِ اساسی با بیشترین مشارکت (نه پشتِ درهای بسته)؛ تاریخِ همه‌پرسی از روزِ نخست اعلام می‌شود و تغییر نمی‌کند. پس از میزِ نقد، نگارشِ پیش‌نویس از فازِ سوم به فازِ اول منتقل شد. قفل‌ها: فقدانِ فرایندِ تأسیس، خطرِ فردمحوری.', '600 days, the founders\' vote: a draft constitution with maximum participation; the referendum date is announced on day one and never changes. After the critique table, drafting moved from phase three to phase one. Locks: no founding process, personality dependence.'),
     P('میثاقِ حداقلی شش بند دارد (نه شصت): تمامیتِ ارضی و برابریِ شهروندی؛ حاکمیتِ قانون؛ عدالت بدون انتقام؛ آزادیِ دین و بی‌دینی؛ تاریخِ مشخصِ رأی‌گیری؛ عدمِ بهره‌برداریِ انتخاباتی از دورهٔ گذار. اجماع بر فرمِ حکومت لازم نیست و همین‌الان ممکن هم نیست.', 'The minimal covenant has six clauses (not sixty): territorial integrity and equal citizenship; rule of law; justice without revenge; freedom of religion and non-religion; a fixed vote date; no electoral exploitation of the transition. Consensus on the form of government is not needed and not possible now.')],
    [L('simorgh:ten-unbuilt-roles', 'ده نقشِ نساخته', 'Ten unbuilt roles'), L('simorgh:three-paths', 'سه راه', 'Three paths'), L('simorgh:nine-faction-critique', 'میزِ نقد', 'Critique table')], 'simorgh:strategy')

new('cost-model', T('برآوردِ هزینه: جانی و مالی', 'Cost model: lives and money'),
    T('این‌ها پیش‌بینی نیستند؛ بازه‌های مدل‌شده‌اند از قیاسِ گذارهای مستندِ جهانی، مقیاس‌شده به ۸۷ میلیون با سه تعدیل (شهرنشینیِ ۷۷٪، ارزیابی‌های متن دربارهٔ خطرِ تجزیه و فردمحوری، و رفتارِ مشاهده‌شدهٔ جامعه در دی ۱۴۰۴). هر عدد مرتبهٔ بزرگی است نه رقم؛ ارزش در مقایسهٔ نسبیِ سه ستون است.',
      'These are not predictions; they are modelled ranges from comparable documented transitions, scaled to 87 million with three adjustments. Each number is an order of magnitude, not a figure; the value lies in comparing the columns.'),
    [P('هزینهٔ جانی: گذارِ میثاقی ۱٬۰۰۰ تا ۱۵٬۰۰۰ کشته و کمتر از ۵۰۰ هزار آواره، ۱ تا ۳ سال ناامنی؛ گسستِ سریع ۵٬۰۰۰ تا ۵۰٬۰۰۰ کشته، ۰٫۵ تا ۲ میلیون آواره، ۲ تا ۵ سال؛ چرخهٔ خشونت ۱۰۰٬۰۰۰ تا ۵۰۰٬۰۰۰+ کشته، ۳ تا ۱۰ میلیون آواره، ۱۰ تا ۲۰ سال؛ وضعِ موجود: مرگ‌های «آرام» و مهاجرتِ فزاینده، نامحدود.', 'Human cost: covenantal 1,000 to 15,000 deaths and under 500,000 displaced, 1 to 3 years; rapid rupture 5,000 to 50,000 deaths, 0.5 to 2 million displaced, 2 to 5 years; cycle of violence 100,000 to 500,000+ deaths, 3 to 10 million displaced, 10 to 20 years; status quo: slow deaths and rising emigration, open-ended.', [], True),
     P('هزینهٔ مالی: افتِ GDP در اوج: ۵ تا ۱۲٪ (میثاقی)، ۱۵ تا ۲۵٪ (گسست)، ۴۰ تا ۷۰٪ (چرخهٔ خشونت)؛ بازسازی ۳۰–۶۰، ۸۰–۱۵۰ و ۲۵۰–۵۰۰ میلیارد دلار؛ بازگشت به سطحِ امروز ۲ تا ۴، ۵ تا ۸ و ۱۵ تا ۲۵ سال؛ بازدهِ خالصِ ده‌ساله +۴۰۰ تا ۸۰۰، +۵۰ تا ۳۰۰ و −۶۰۰ تا ۱٬۲۰۰ میلیارد دلار؛ وضعِ موجود −۴۰۰ تا ۶۰۰ هزینهٔ فرصت.', 'Financial cost: peak GDP drop 5 to 12, 15 to 25 and 40 to 70 percent; reconstruction 30-60, 80-150 and 250-500 billion dollars; return to today\'s level 2-4, 5-8 and 15-25 years; ten-year net return +400 to 800, +50 to 300 and -600 to -1,200 billion; status quo -400 to -600 opportunity cost.', [], True),
     P('لنگرِ عددی: فرارِ مغزها ≈۵۰ میلیارد دلار در سال (برآوردِ منسوب به بانکِ جهانی، بی‌منبعِ اولیه) در برابرِ ≈۲۰ میلیارد صادراتِ نفتِ ۲۰۱۹؛ درآمدِ سرانه ۵٬۶۱۷ (۲۰۲۵) در برابرِ ۷٬۴۴۲ (۱۹۷۶). منتقدِ روش‌شناس می‌گوید این دو هم‌جنس نیستند و ترکیبِ جمعیت را نادیده می‌گیرد؛ نسبتِ اهرمِ ۱ به ۱۰٬۰۰۰ بازمحاسبه شد.', 'Anchors: brain drain ≈50 billion dollars a year (estimate attributed to the World Bank, no primary source) against ≈20 billion 2019 oil exports; income per head 5,617 (2025) against 7,442 (1976). The methodologist critic says these are not like for like; the 1-to-10,000 leverage ratio was recomputed.', [], True),
     P('معادلهٔ پنجاه‌هزار: در حوزهٔ تمدنِ ایرانی (۳۰ تا ۵۰ کشور) پنجاه‌هزار نفرِ نخبه می‌خواهید که بدانند به یک تمدن تعلق دارند؛ و منبعِ تولیدِ آن‌ها، جمعیتِ دانشجویی، از ۴٫۸ به ۳٫۱۸ میلیون باریک می‌شود. هر سال تأخیر ظرفیتِ ساختنِ فردا را کم می‌کند و این جبران‌پذیر نیست.', 'The fifty-thousand equation: across the Iranian civilisational area (30 to 50 countries) you need fifty thousand elite people who feel they belong to one civilisation; the student population that produces them shrinks from 4.8 to 3.18 million. Each year of delay reduces the capacity to build tomorrow, irreversibly.')],
    [L('simorgh:three-paths', 'سه راه', 'Three paths'), L('simorgh:claims-model', 'ادعاهای مدل', 'Model claims'), L('simorgh:audit', 'ممیزی', 'Audit')], 'simorgh:strategy')

CR = GAME['CRIT']
new('nine-faction-critique', T('میزِ نقد: نُه جناح به سند چه می‌گویند', 'Critique table: what nine factions say to the paper'),
    T('سند را از نُه موضعِ سیاسیِ متفاوت، بعضی دشمنِ هم، نقد می‌کنند و هر نقد در قوی‌ترین شکلش نوشته شده. نقدِ پذیرفته‌شده در متنِ اصلی تغییر ایجاد کرده؛ نقدِ ردشده دلیلِ ردش دارد. هفده تغییر از این میز بیرون آمد. آزمونِ جانشینی: هر بندی که با عوض‌کردنِ نامِ یک جریان به نامِ جریانِ دیگر بی‌معنا شود جانبدارانه است و بازنویسی می‌شود.',
      'The paper is criticised from nine different political positions, some enemies of each other, each critique at full strength. Accepted critiques changed the main text; rejected ones carry reasons. Seventeen changes came out of this table. The substitution test: any clause that becomes meaningless when one current\'s name is swapped for another\'s is partisan and gets rewritten.'),
    [P(f"{c['w']} — {c['t']}: {c['tl']} نقدها: " + '؛ '.join(o['h'] for o in c['o']) + '. چه تغییر کرد: ' + ' '.join(strip(y) for y in c['y'])[:600] + ((' چه نشد: ' + ' '.join(strip(x) for x in c['n'])[:400]) if c['n'] else ''),
       f"Critique from {c['w']}: objections, changes made and changes not made, as in the Persian text.") for c in CR]
    + [P('آزمونِ جانشینی روی هر پنج ابتکار اجرا شد؛ ابتکارِ سوم تنها موردی بود که ردش نکرد و صورت‌بندی‌اش از «پیشنهاد به یک نفر» به «معیارِ عمومی برای هر مدعیِ رهبری» عوض شد.', 'The substitution test was run on all five initiatives; the third alone failed it and was reformulated from "a proposal to one person" to "a public standard for any claimant to leadership".')],
    [L('simorgh:covenantal-transition', 'برنامهٔ ۹۰/۹/۶۰۰', '90/9/600 plan'), L('simorgh:cost-model', 'برآوردِ هزینه', 'Cost model'), L('simorgh:audit', 'ممیزی', 'Audit')], 'simorgh:strategy')

new('strategy-paper', T('سندِ راهبردی: تشخیص، گزینه‌ها و مسیر (۱۲ بخش)', 'Strategy paper: diagnosis, options and path (12 sections)'),
    T('سندی ۴۵ دقیقه‌ای (مهر ۱۴۰۵) که می‌پرسد مسئلهٔ امروز چیست، چه گزینه‌هایی روی میز است، هرکدام چه قیمتی دارد و چه چیزی را می‌شود اندازه گرفت. تحلیلِ ساختاری است نه بیانیه و نه پیش‌بینی، و بر ۸۴ ادعای منبع‌دار تکیه دارد. نسخهٔ کوتاهِ آن «ارائهٔ راهبردی» است.',
      'A 45-minute paper (October 2026) asking what today\'s problem is, what options are on the table, what each costs and what can be measured. Structural analysis, not a manifesto nor a forecast, resting on 84 sourced claims. Its short version is the strategy brief.'),
    [P('شش گزارهٔ خلاصهٔ اجرایی: مسئله متقاعدکردنِ مردم نیست (۳۰٫۷٪ تا ۷۲٫۹٪ موافقِ جدایی دین از حکومت، از پیمایشِ خودِ حاکمیت)؛ ائتلافِ حاکم کوچک ولی منسجم است؛ فشارِ اقتصادی شکلِ خاصی دارد؛ ساعتِ جمعیتی می‌دود؛ گزینه‌ها قیمت دارند؛ و راهِ شدنی کوچک‌ترین قدمِ هماهنگ است.', 'The six executive propositions: the problem is not persuading people; the ruling coalition is small but cohesive; economic pressure has a specific shape; the demographic clock is running; options have prices; and the feasible way is the smallest coordinated step.', [K['gamaan']]),
     P('تشخیص با چهار سنجه: تقاضا اشباع است؛ ائتلاف حاکم ۱۰ تا ۱۵٪ (برآوردِ کیفی) در برابر ۸۰ تا ۸۵٪؛ فقر ۳۰٪ و طبقهٔ متوسط ۸۴٪ ← ۵۶٪؛ ساعتِ جمعیتی (باروری ۱٫۳۵ تا ۱٫۷، دانشجو ۴٫۸ ← ۳٫۱۸ میلیون، تورم ۸۷٫۹٪).', 'Diagnosis by four gauges: demand is saturated; the ruling coalition 10 to 15 percent (qualitative) against 80 to 85; poverty 30 percent, middle class 84 to 56; demographic clock.', [], True),
     P('ریشهٔ ساختاری: پانصد سال بالا رفتن (هشت پله) و ۱۳۵۷ با درسِ سازمان‌یافتگی؛ و کارتِ هجده قشر: کاسب و بازاری، کارگرِ صنعتی (نفت، گاز، پتروشیمی، بندر)، راننده، معلم، کادرِ درمان، سرباز و پلیس و نیروی امنیتی، کارمندِ دولت، اهلِ منبر و مسجد، دانشجو، متخصص، مهاجر، زنِ خانه، دست‌تنگ، سرمایه‌دار، وکیل، هنرمند، کم‌سواد، و کسی که نمی‌خواهد یا می‌ترسد؛ برای هرکدام نقش، وضع، خطر، خواست و چگونگیِ همراه‌شدن.', 'Structural roots: five centuries of rising and 1979; and the eighteen-strata card: for each what it does, its situation, risk, wish and how it joins.'),
     P('پایهٔ شواهد: ۸۴ ادعا؛ ردهٔ ۱ دادهٔ اولیه یا سند، ردهٔ ۲ پژوهش، ردهٔ ۳ برآورد یا مدل. آنچه ادبیات می‌گوید: خشونت‌پرهیزی مؤثرتر (۵۳٪ در برابر ۲۶٪)، قاعدهٔ ۳٫۵٪ مشاهده است نه قانون، و ریزشِ نیروهای نگه‌دارنده تعیین‌کننده است. آنچه ما را رد می‌کند: دوامِ رژیم‌های انقلابی، خطرِ میانهٔ راه و نرخِ کاهنده.', 'Evidence base: 84 claims across three tiers. What the literature says: nonviolence is more effective, the 3.5 percent rule is an observation not a law, and defection of supporting forces decides. What refutes us: durability of revolutionary regimes, the middle-of-the-road danger and the falling success rate.', [K['cs'], K['lw'], SRC['walter']]),
     P('گزینه‌ها و قیمت (چهار مسیر) و توصیه در سه افق (۹۰ روز، ۹ ماه، ۶۰۰ روز) با شش ابتکار؛ و یک اقدامِ پربازده: موضع‌گیریِ صریح و مکرر نسبت به رفتارِ هواداران که منبع «۸۰ تا ۹۰ درصدِ مسئله» می‌داند (داوریِ کیفی، بی‌روش).', 'Options and prices (four paths) and the three-horizon recommendation with six initiatives; plus one high-yield action: explicit, repeated position on supporters\' behaviour, which the source calls "80 to 90 percent of the problem" (qualitative, no method).', [], True),
     P('دفترچهٔ سیاست: ده پرونده با چهار خانه (مسئلهٔ امروز، چه می‌شود کرد، تجربهٔ جهانی، آنچه نمی‌دانیم؛ خانهٔ چهارم اجباری): مسکن و خانه‌های خالی؛ امنیتِ عمومی در صد روزِ اول؛ بودجه و پول‌های بلوکه؛ مسجد، حوزه و نهادِ دینی؛ پزشکِ سهمیه‌ای و عدالتِ آموزشی؛ سواد و آموزشِ بزرگسال؛ آب، محیط‌زیست و حیاتِ وحش (تنها پروندهٔ برگشت‌ناپذیر)؛ بازسازیِ پس از جنگ؛ قوانینِ روزِ اول (هفت متنِ کوتاه که باید امروز نوشته و در کشو گذاشته شود)؛ مردم چطور از خودشان مراقبت کنند.', 'Policy notebook: ten files with four boxes each (today\'s problem, what can be done, world experience, what we do not know; the fourth is mandatory).'),
     P('سنجه‌های ۹۰ روز: هر راهبردی که شرطِ شکستِ خودش را تعریف نکند راهبرد نیست؛ مثلاً «تنوعِ امضا» با هدفِ بیش از ۵۰٪ امضاکنندهٔ غیرپادشاهی‌خواه و آستانهٔ شکستِ زیر ۳۰٪. و ممیزی: ۱۴ ادعا به یک ارجاعِ جمعی بند است.', '90-day metrics: any strategy that does not define its own failure condition is not a strategy; e.g. "signature diversity" with a target above 50 percent non-monarchist signers and a failure threshold below 30. And the audit.', [], True),
     P('پروندهٔ جدا: ایران و اسرائیل در یک سندِ راهبردی، با چهار چیزی که نمی‌گوید.', 'A separate file: Iran and Israel, with the four things it does not say.')],
    [L('simorgh:covenantal-transition', 'برنامهٔ ۹۰/۹/۶۰۰', '90/9/600'), L('simorgh:nine-faction-critique', 'میزِ نقد', 'Critique table'), L('simorgh:audit', 'ممیزی', 'Audit'),
     L('simorgh:europe-deck', 'ارائهٔ اروپا', 'Europe deck'), L('simorgh:iran-israel', 'ایران و اسرائیل', 'Iran and Israel')], 'simorgh:strategy')

new('europe-deck', T('ارائهٔ اروپا، فایل‌های پرسش‌وپاسخ و دانلودها', 'Europe deck, Q&A files and downloads'),
    T('ارائه‌ای دوزبانه برای مخاطبِ اروپایی (حالتِ اسلاید، ۲۲ اسلایدِ PPTX)، دو فایلِ پرسش‌وپاسخ (دربارهٔ سایت و دربارهٔ ارائه) و صفحهٔ دانلودها که فایل‌های باز را یک‌جا می‌دهد.',
      'A bilingual deck for a European audience (slide mode, 22-slide PPTX), two Q&A files (about the site and about the deck) and a downloads page that gives the open files in one place.'),
    [P('ارائه: همان استدلال با زبانِ سیاستِ اروپایی و منبع‌های ICCT و دیگران؛ جملهٔ اجباریِ دربارهٔ ایران و اسرائیل در هر نسخه می‌ماند.', 'The deck: the same argument in European policy language with ICCT and other sources; the mandatory Iran-Israel sentence stays in every version.'),
     P('فایل‌ها: par-simorgh-deck.pptx (۲۲ اسلاید)، QA-site و QA-simorgh-europe، claims-dataset.json، problems-dataset.json، و ابزارِ voice2text که در مرورگر کار می‌کند و صدا را به جایی نمی‌فرستد.', 'Files: the PPTX deck, the two Q&A documents, the two datasets, and the voice2text tool that runs in the browser and sends audio nowhere.')],
    [L('simorgh:tools-directory', 'فهرست ابزارها', 'Tools directory'), L('simorgh:iran-israel', 'ایران و اسرائیل', 'Iran and Israel')], 'simorgh:strategy')

# ===================== ACTION =====================
gam = open(f'{SC}/sim/txt/site_gam.html.txt', encoding='utf-8').read().split('\n')
a = next(i for i, l in enumerate(gam) if l.startswith('## قدمِ تو')); b = next(i for i, l in enumerate(gam) if l.startswith('## خطر'))
cards = []; cur = None
for l in gam[a + 1:b]:
    if l.startswith('### '):
        cur = [l[4:].strip(), '', '']; cards.append(cur)
    elif cur:
        s = l.strip()
        if s.startswith('- ') and not cur[2]: cur[2] = s[2:].strip()
        elif s and not s.startswith('-') and not cur[1]: cur[1] = s
cards = [c for c in cards if c[0]]
new('step-cards', T(f'قدمِ تو: {len(cards)} کارت، کوچک‌ترین قدمِ هر آدم', f'Your step: {len(cards)} cards, the smallest step for each person'),
    T('صفحه‌ای که نمی‌گوید چه کار کنید؛ می‌گوید در ۳۲۳ خیزشِ ثبت‌شده چه کار کرد و چه نکرد، و برای هر جورِ آدمی یک کارت دارد با کارهای مرتب‌شده از کم‌خطر به پرخطر. همین‌جا فقط کم‌خطرترینِ هر کارت آمده؛ هیچ‌کس مجبور نیست، و کسی که داخلِ ایران است فقط قدم‌های کم‌خطر را ببیند.',
      'A page that does not tell you what to do; it says what worked and failed in 323 recorded uprisings, with a card for each kind of person, steps ordered from low to high risk. Only the lowest-risk step of each card is quoted here; nobody is obliged, and anyone inside Iran should see only low-risk steps.'),
    [P('شما تنها نیستید (ریاضی است نه دلداری): جایی که حرفِ راست خرج دارد همه حرفشان را می‌خورند، هرکس سکوت می‌بیند و فکر می‌کند تنهاست؛ تعداد از شدت مهم‌تر است (۵۳٪ در برابر ۲۶٪)؛ لحظهٔ تعیین‌کننده لحظهٔ ریزش است (سرباز، کارمند، قاضی، مدیر)؛ و هیچ تضمینی نیست: نرخِ موفقیت در دههٔ اخیر افت کرده چون حکومت‌ها یاد گرفته‌اند.', 'You are not alone (arithmetic, not consolation); numbers matter more than intensity; the decisive moment is defection; and there is no guarantee, since success rates have fallen.', [K['cs'], K['ch21'], K['kuran']]),
     P('کوچک‌ترین قدمِ ممکن: یک حرفِ راست به یک نفر که به شما اعتماد دارد؛ استعاره نیست، عیناً همان سازوکارِ شکستنِ تحریفِ ترجیحات است.', 'The smallest possible step: one true word to one person who trusts you; exactly the mechanism that breaks preference falsification.', [K['kuran']]),
     P('بخشِ «خطر»: همین حالا در ایران مردم اعدام می‌شوند؛ هر عددِ صفحه میانگینِ ۳۲۳ مورد است و شما یک نفرید. همین‌جا هم نقدها آمده‌اند: رژیم‌های زادهٔ انقلاب دیر می‌میرند، خطرناک‌ترین نقطه وسطِ راه است، عراقِ ۲۰۰۳، «جامعهٔ کوتاه‌مدت»، و نرخِ موفقیتِ کاهنده.', 'The "risk" section: people are being executed in Iran right now; every number is an average of 323 cases and you are one person. The critiques too: revolutionary regimes die late, the middle of the road is most dangerous, Iraq 2003, the short-term society, and falling success rates.', [K['lw'], SRC['walter'], SRC['dodge'], K['nokar']], True)]
    + [P(f"{c[0]}: {c[1][:230]} نخستین و کم‌خطرترین قدم: {c[2][:200]}", f"Card: {c[0]}. Research hook and lowest-risk first step as in the Persian text.") for c in cards],
    [L('simorgh:birds-30', 'سی مرغ', 'Thirty birds'), L('simorgh:population-groups', 'بیست گروه', 'Twenty groups'), L('simorgh:claims-resistance', 'ادعاهای مقاومت', 'Resistance claims')], 'simorgh:action')

BIRDS = PLAN['birds']; BC = PLAN['bird_cards']
new('birds-30', T('سی مرغ: شش گروه، پنج نقش', 'Thirty birds: six groups of five roles'),
    T('هر مرغ یک نقشِ مسئول برای روز آزادی و پس از آن است: نگهبانانِ جان، نگهبانانِ سرزمین، سازندگانِ نهاد، سازندگانِ دانایی، سازندگانِ پیوند و گروهِ ششم. هر مرغ یک «مأموریت»، یک «قدمِ امروز»، یک نقشِ روزِ آزادی و یک افقِ بلندمدت دارد. نقش‌ها جایگاه‌اند، نه فهرستِ آدم‌ها.',
      'Each bird is a responsible role for liberation day and after: guardians of life, guardians of land, builders of institutions, builders of knowledge, builders of ties, and a sixth group. Each has a mission, a step for today, a liberation-day role and a long-term horizon. Roles are places, not lists of people.'),
    [P(f'{g}: ' + '، '.join(bs), f'Group: {g}.') for g, bs in BIRDS],
    [L(f'simorgh:birds-{i+1}', g, g) for i, (g, _) in enumerate(BIRDS)] + [L('simorgh:liberation-day', 'روز آزادی', 'Liberation day')], 'simorgh:action')
for i, (g, bs) in enumerate(BIRDS):
    pts = []
    for b_ in bs:
        c = BC.get(b_)
        if c:
            pts.append(P(f'{b_}: مأموریت: {c[0]}. قدمِ امروز: {c[2]}. روزِ آزادی: {c[3]}. پس از آن: {c[4]}.', f'Bird {b_}: mission, step today, liberation-day role, long-term, as in the Persian text.'))
        else:
            pts.append(P(b_, b_))
    lks = []
    for b_ in bs:
        c = BC.get(b_)
        if c:
            for t_, u_ in c[6]:
                cid = planlink(u_)
                if cid and not any(l['to'] == cid for l in lks): lks.append(L(cid, t_, t_))
    new(f'birds-{i+1}', T(f'مرغ‌ها: {g}', f'Birds: {g}'), T(f'پنج مرغِ گروهِ «{g}» با مأموریت و قدمِ هرکدام.', f'The five birds of the group "{g}" with the mission and step of each.'),
        pts, lks[:8] + [L('simorgh:birds-30', 'سی مرغ', 'Thirty birds')], 'simorgh:action')

GR = PLAN['groups']
new('population-groups', T('بیست گروهِ جمعیتی و آنچه هرکدام لازم دارد', 'Twenty population groups and what each needs'),
    T('جامعه در سطحِ جمعیت به بیست گروه تقسیم شده تا برای هر گروه نیاز و نخستین سیاستِ لازم معلوم باشد. این تقسیم فقط جمعیتی است و هیچ فهرستِ آدم یا برچسب‌زدنِ فردی در آن نیست.',
      'Society at the population level is divided into twenty groups so each need and first policy is clear. The split is demographic only, with no lists of persons and no individual labelling.'),
    [P(f'{g[0]}: نیاز: {g[1]}. نخستین سیاست: {g[2]}.', f'{g[0]}: need and first policy, as in the Persian text.') for g in GR],
    [L('simorgh:step-cards', 'قدمِ تو', 'Your step'), L('simorgh:ruins-ledger', 'دفترِ ویرانی‌ها', 'Ruins ledger')], 'simorgh:action')

RK = PLAN['risks']
new('transition-risks', T('پانزده خطرِ گذار و پاسخِ هرکدام', 'Fifteen transition risks and the response to each'),
    T('خطرهای روزهای نخست، هرکدام با نشانه، پاسخِ از پیش‌آماده و مرغِ مسئول: انتقام و خشونتِ خیابانی، غارت، خلأ قدرت یا کودتا، گروه‌های مسلح و دیگران.',
      'The risks of the first days, each with signs, a pre-prepared response and the responsible bird.'),
    [P(f'{r[0]}: نشانه: {r[1]}. پاسخ: {r[2]}. مرغِ مسئول: {r[3]}.', f'{r[0]}: signs, response and responsible bird, as in the Persian text.') for r in RK],
    [L('simorgh:birds-30', 'سی مرغ', 'Thirty birds'), L('simorgh:liberation-day', 'روز آزادی', 'Liberation day'), L('simorgh:three-paths', 'سه راه', 'Three paths')], 'simorgh:action')

TK = PLAN['tasks']; CE = PLAN['celebrations']; CR_ = PLAN['celebration_roles']
phases = []
for t in TK:
    if t[0] not in phases: phases.append(t[0])
new('liberation-day', T('روز آزادی: کارهای هر بازه، جشن‌ها و نقش‌های جشن', 'Liberation day: tasks per phase, celebrations and celebration roles'),
    T(f'{len(TK)} کار در بازه‌های «{"، ".join(phases)}»، هرکدام برای «همه» یا «مهارت‌دار» و با مرغِ مسئول؛ هفت جشن؛ و هشت نقشِ جشن. هدف این است که شادی و آمادگی هم‌زمان باشند و تصویری به جهان برود که می‌گوید آمادهٔ ساختنیم.',
      f'{len(TK)} tasks across phases, each for everyone or for those with skills and with a responsible bird; seven celebrations; eight celebration roles. The aim is joy and readiness together, sending the world a picture of readiness to build.'),
    [P(f'{ph}: ' + '؛ '.join(f'{t[1]} ({t[2]}، {t[3]})' for t in TK if t[0] == ph), f'Phase {ph}: tasks as in the Persian text.') for ph in phases]
    + [P('جشن‌ها: ' + '؛ '.join(f'{c[0]} ({c[1]})' for c in CE), 'Celebrations as in the Persian text.'), P('نقش‌های جشن: ' + '، '.join(CR_), 'Celebration roles as in the Persian text.')],
    [L('simorgh:transition-risks', 'پانزده خطر', 'Fifteen risks'), L('simorgh:birds-30', 'سی مرغ', 'Thirty birds')], 'simorgh:action')

ME = PLAN['me']
new('my-share', T('«سهم من»: دو پرسش، سه قدم', 'My share: two questions, three steps'),
    T('ابزاری که از هر نفر می‌پرسد «کارت چیست؟» و «چه سهمی می‌تواند داشته باشد؟»، و برای هر حرفه‌ای مرغ‌های مناسب و سه قدمِ کم‌خطر می‌دهد. برای کسی که داخلِ ایران است هیچ قدمِ پرخطری پیشنهاد نمی‌شود.',
      'A tool asking each person what they do and what share they could have, giving for each profession suitable birds and three low-risk steps. No high-risk step is suggested to anyone inside Iran.'),
    [P(f'{k}: مرغ‌های مناسب: ' + '، '.join(v[0]) + '. قدم‌ها: ' + '؛ '.join(v[1:]), f'{k}: suitable birds and steps, as in the Persian text.') for k, v in ME.items()],
    [L('simorgh:birds-30', 'سی مرغ', 'Thirty birds'), L('simorgh:step-cards', 'قدمِ تو', 'Your step')], 'simorgh:action')

# ===================== PROJECT =====================
LY = PLAN['layers']; RM = PLAN['roadmap']; SCI = PLAN['sciences']
new('master-plan', T('نقشهٔ کلان: پنج لایه و راهنقشهٔ دروازه‌ای', 'Master plan: five layers and a gated roadmap'),
    T('پروژه پنج لایه دارد که هرکدام دیگری را تغذیه می‌کند، و راهنقشه‌اش با دروازه می‌رود نه با تاریخ: هر مرحله وقتی شروع می‌شود که دروازهٔ قبلی بسته شده باشد.',
      'The project has five layers feeding each other and a roadmap that goes by gates, not dates: each stage starts once the previous gate has closed.'),
    [P('لایه‌ها: ' + '؛ '.join(f'{l[0]}: {l[1]}' for l in LY), 'Layers as in the Persian text.')]
    + [P(f'مرحلهٔ {r[0]}: {r[1]}' + (f'. دروازه: {r[2]}' if r[2] else ''), f'Stage {r[0]}: content and gate as in the Persian text.') for r in RM],
    [L('simorgh:sciences-26', 'بیست‌وشش علم', 'Twenty-six sciences'), L('simorgh:ruins-ledger', 'دفترِ ویرانی‌ها', 'Ruins ledger'), L('simorgh:products-19', 'نوزده محصول', 'Nineteen products'),
     L('simorgh:circle-table', 'میزِ دایره‌ای', 'Circle table'), L('simorgh:tools-directory', 'ابزارها', 'Tools')], 'simorgh:project')

new('sciences-26', T('بیست‌وشش علم: چه داریم، چه نیمه داریم، چه نداریم', 'Twenty-six sciences: what we have, partly have, lack'),
    T('بازی روی علم بنا شده؛ این مدخل می‌گوید برای هر علم چه چیزی لازم است و چقدر از آن در دانش‌سرا پوشش داده شده است (دارد، نیمه، ندارد).',
      'The game rests on science; this entry says what each science is needed for and how much Daneshsara covers it (have, partly, none).'),
    [P(f"{s[0]} [{ {'have': 'دارد', 'part': 'نیمه', 'none': 'ندارد'}.get(s[2], s[2]) }]: {s[1]}", f'{s[0]}: coverage status and use, as in the Persian text.', [], s[2] != 'have') for s in SCI],
    [L('simorgh:master-plan', 'نقشهٔ کلان', 'Master plan')], 'simorgh:project')

LG = PLAN['ledger']
new('ruins-ledger', T('دفترِ ویرانی‌ها: نوزده حوزه', 'Ruins ledger: nineteen domains'),
    T('دفتری که ویرانیِ هر حوزه را (آب، خاک و طبیعت، و دیگران) فهرست می‌کند و می‌گوید در دانش‌سرا چقدر پشتوانه دارد. قاعده: بی‌منبع نوشته نمی‌شود.',
      'A ledger listing the ruin in each domain (water, soil and nature, and others) and how much backing Daneshsara has. Rule: nothing is written without a source.'),
    [P(f"{d[0]} [{ {'have': 'دارد', 'part': 'نیمه', 'none': 'ندارد'}.get(d[2], d[2]) }]: " + '؛ '.join(d[1]), f'{d[0]}: items and coverage, as in the Persian text.', [], d[2] != 'have') for d in LG],
    [L('simorgh:population-groups', 'بیست گروه', 'Twenty groups'), L('simorgh:master-plan', 'نقشهٔ کلان', 'Master plan')], 'simorgh:project')

PR = PLAN['products']
new('products-19', T('نوزده محصول: اول آنچه پول می‌سازد', 'Nineteen products: money-makers first'),
    T('کسب‌وکارِ پروژه دو سبد دارد: سبدِ یک (سیمرغ: دانش‌سرا، بازی، «سهم من»، نقشهٔ روز بعد) رایگان و بازمتن است؛ سبدِ دو محصول‌هایی در اروپاست که پول در می‌آورند، شبکه می‌سازند و خرجِ سبدِ یک را می‌دهند. هر محصول با مشتری، مدلِ درآمد، سرعت و قدمِ بعد.',
      'Two baskets: basket one (Simorgh: Daneshsara, the game, My share, the next-day map) is free and open; basket two is products in Europe that earn, build a network and pay for basket one. Each product with customer, revenue model, speed and next step.'),
    [P(f"{p[0]}: مشتری: {p[1]}؛ مدل: {p[2]}؛ جامعه: {p[3]}؛ سرعت: {p[4]}؛ وضع: {p[5]}. قدمِ بعد: {p[7]}", f'{p[0]}: customer, model, speed and next step, as in the Persian text.') for p in PR],
    [L('simorgh:circle-table', 'میزِ دایره‌ای', 'Circle table'), L('simorgh:master-plan', 'نقشهٔ کلان', 'Master plan')], 'simorgh:project')

new('circle-table', T('میزِ دایره‌ای: برگهٔ جلسهٔ یک‌ساعته', 'Circle table: one-hour meeting sheet'),
    T('برگه‌ای نُه‌بخشی برای یک جلسهٔ یک‌ساعته؛ هر خط پیشنهاد است نه تصمیم و هر کس روی خطی که با آن موافق نیست می‌زند تا خط بخورد. بخش‌ها: ما چه هستیم و نیستیم، دنبال چه هستیم، از این حلقه چه می‌خواهم، محصول در دو سبد، بازاریابی، سرمایه، جاهای خالی، ده پرسش، جمع‌بست.',
      'A nine-part sheet for a one-hour meeting; every line is a proposal, not a decision, and anyone who disagrees strikes it. Sections: what we are and are not, what we seek, what I want from this circle, product in two baskets, marketing, capital, empty seats, ten questions, wrap-up.'),
    [P('هستیم: دانش‌سرایی منبع‌دار به زبانِ ساده، بازیِ تمرینِ اعتماد، نقشهٔ «روزِ بعد» (آب، برق، نان، عدالت)، شبکه‌ای که هر نفر یک قدمِ کوچک برمی‌دارد، شفاف در روش و پول.', 'We are: a sourced knowledge commons, a trust game, a day-after map, a network where each person takes one small step, transparent in method and money.'),
     P('نیستیم: حزب یا گروهِ سیاسی با رهبر؛ سازمانِ مخفی؛ رسانهٔ خبری؛ دادگاه (به هیچ آدمِ واقعی برچسب نمی‌زنیم و پرونده نمی‌سازیم)؛ دولتِ در تبعید.', 'We are not: a party with a leader; a secret organisation; a news outlet; a court (no real person is labelled and no file kept); a government in exile.'),
     P('دنبالش نیستیم: خشونت و انتقام؛ قدرت یا مقام؛ رشدِ سریع به بهای امنیتِ آدم‌ها؛ پولی با شرطِ سیاسی؛ هیچ کارِ پرخطر از کسی که داخلِ ایران است.', 'Not seeking: violence or revenge; power or office; fast growth at the cost of people\'s safety; money with political conditions; any high-risk act from someone inside Iran.'),
     P('خواسته‌ها از حلقه: نقدِ صریح، هر نفر مسئولِ یک چیز، هر کار روی سایت ثبت شود، آهسته اما پیوسته، «نه» گفتنِ راحت؛ و نخواستن: تأییدِ تعارفی، نامِ یا عکسِ کسی بی‌اجازه، و حرف‌زدن دربارهٔ حلقه بیرون از آن تا راهنمای امنیت آماده شود.', 'What is asked of the circle: frank critique, one responsibility each, all work recorded on the site, slow but steady, easy to say no; and what is not wanted: polite approval, anyone\'s name or photo without consent, talk about the circle outside it until the security guide is ready.'),
     P('سه محصولی که زودتر پول می‌شوند: سنجشِ سلامتِ سازمان (پرسش‌نامهٔ بی‌نام، گزارش، کارگاه؛ نمونه آماده)، کارگاهِ بازیِ جدی برای تیم‌ها، و خدماتِ طراحیِ محصول و پژوهشِ کاربر برای شرکت‌های اروپایی.', 'Three products nearest to money: organisational wellbeing assessment, serious-game workshops for teams, and product design and user-research services for European firms.')],
    [L('simorgh:products-19', 'نوزده محصول', 'Nineteen products'), L('simorgh:master-plan', 'نقشهٔ کلان', 'Master plan'), L('simorgh:roles-47', 'نقش‌ها', 'Roles')], 'simorgh:project')

PB = PROBS
new('problems-map', T('نقشهٔ مشکل‌ها: ۲۴ مشکل روی دو محور', 'Problem map: 24 problems on two axes'),
    T('هر مشکل جایی روی دو محور می‌افتد: فراوانی (چه نسبتی درگیرند) و شدتِ زیسته (چقدر زندگیِ روزمره را مختل می‌کند)؛ جایی که می‌افتد تعیین می‌کند چه پاسخی به دردش می‌خورد. این نقشه برای آموزشِ چارچوب است و ادعای عددی نمی‌کند؛ «مهم‌ترین مشکل» پرسشِ بدی است.',
      'Each problem falls on two axes: frequency and lived severity; where it falls determines what response suits it. The map teaches a framework and makes no numerical claim; "the most important problem" is a bad question.'),
    [P('چهار ربع و چهار جورِ پاسخ: شایع و سنگین ← اولویتِ اضطراریِ سیاستِ کلان؛ نادر اما ویرانگر ← چترِ حمایت و آمادگیِ بحران، هدفمند؛ شایع و آزارنده ← اصلاحِ روزمره و خدماتِ عمومی؛ کم‌شیوع و خفیف ← پایش، منابع را این‌جا انبار نکنید.', 'Four quadrants, four kinds of response.')]
    + [P(f"{p['t']} ({p['lvl']}؛ فراوانی {p['x']}، شدت {p['y']}){'، کم‌ثبت در دادهٔ رسمی' if p.get('hidden') else ''}: {p['note']}", f"Problem {p['id']}: position on the two axes and note, as in the Persian text.") for p in PB],
    [L('simorgh:population-groups', 'بیست گروه', 'Twenty groups'), L('simorgh:ruins-ledger', 'دفترِ ویرانی‌ها', 'Ruins ledger'), L('simorgh:dataset-84', 'دیتاست', 'Dataset')], 'simorgh:project')

TL = PLAN['tools']; BK = PLAN['backlog']
new('tools-directory', T('فهرستِ همهٔ ابزارها و جایی که هرکدام زندگی می‌کند', 'Directory of all tools and where each lives'),
    T('هیچ ابزاری حذف نشده؛ اینجا همه با یک جمله و جای زندگی‌شان آمده‌اند. ابزارها در دو جا هستند: صفحه‌های عمومیِ «پَرِ سیمرغ» و لایهٔ خصوصیِ گاوصندوق.',
      'No tool was removed; all appear here with one line and where they live. They are in two places: the public Par-e Simorgh pages and the private vault layer.'),
    [P('ابزارهای صفحهٔ عمومی: نقشهٔ استدلال (argmap)؛ وارسیِ یک ادعا (inspect، چهار گام)؛ سلامتِ دیتاست (health، شمارندهٔ زنده)؛ وضعیتِ اسناد (status)؛ ممیزی (audit)؛ جدولِ داده (data، ۸۴ ادعا)؛ نقشهٔ مشکل‌ها (problems، ۲۴ مشکل)؛ خطِ زمان (timeline)؛ کتابخانه (library)؛ دو ایران (two-irans)؛ ایران و اسرائیل (shared)؛ قدمِ تو (gam، ۲۳ کارت)؛ سندِ راهبردی (sanad-rahbordi) و نسخهٔ کوتاهش (eraee-rahbordi)؛ بازیِ کامل (game، ۱۲ جلد)؛ نقش‌ها (roles، ۴۷ نقش)؛ ارائهٔ اروپا (europe)؛ دانلودها (downloads)؛ voice2text (در مرورگر، صدا را نمی‌فرستد).', 'Public-page tools as listed.'),
     P('ابزارهای لایهٔ خصوصی (گاوصندوق): نقشهٔ کلان (plan)، سی مرغ (birds)، میزِ دایره‌ای (circle)، بازیِ ده‌نوبتی (sim)، حدسِ پانزده گذار (transitions)، چرا؟ (why، علمِ ۴۷ نقش)، و دفترِ پروژه که هر روز تغییرها را ثبت می‌کند.', 'Private-layer tools as listed.')]
    + [P(f"{t[0]}: {t[1]} [{ {'have': 'آماده', 'part': 'نیمه', 'none': 'نیست'}.get(t[2], t[2]) }]", f'{t[0]}: status as in the Persian text.', [], t[2] != 'have') for t in TL],
    [L('simorgh:page-map', 'نقشهٔ صفحه‌ها', 'Page map'), L('simorgh:threshold-simulator', 'شبیه‌ساز آستانه', 'Threshold simulator'), L('simorgh:ten-turn-game', 'بازیِ ده‌نوبتی', 'Ten-turn game')], 'simorgh:project')

new('page-map', T('نقشهٔ صفحه‌ها: هر صفحهٔ قدیمی کجا رفت', 'Page map: where each old page went'),
    T('پاسخ به «صفحه‌ها قاطی‌پاتی است»: هر صفحه و زیرصفحه یک مدخلِ مشخص در این ویکی دارد و ابزارها سر جایشان مانده‌اند. صفحهٔ قدیمی مرجعِ ابزار است و این ویکی مرجعِ محتوا.',
      'The answer to "the pages are a mess": every page and sub-page has a specific entry in this wiki and the tools stayed where they are. The old page is the tool; this wiki is the content.'),
    [P('صفحهٔ اصلی (index) و صفحهٔ بازی (game، ۱۲ جلد: قواعد، هفت شب، نقشهٔ میز، کتابِ شخصیت‌ها، ده نقشِ نساخته، پَر، سه راه، هزینه، کمیک، میزِ نقد، سی مرغ) ← بازی و استعاره: استعاره، هفت شب، سه پَر، شخصیت‌ها (سه مدخل)، ده نقشِ نساخته؛ و راهبرد: سه راه، گذارِ میثاقی، هزینه، میزِ نقد.', 'Index and game pages map to the game and strategy entries.'),
     P('نقش‌ها (roles) و چرا؟ (why) ← سه مدخلِ ۴۷ نقش؛ صفحه‌های nights، players و rules (نسخه‌های خالیِ جا‌ماندهٔ قدیمی) ← در «هفت شب» و «شخصیت‌ها» ادغام شدند و می‌توان حذفشان کرد.', 'Roles and why map to the three 47-role entries; the empty nights, players and rules stubs merged into Seven nights and Characters and can be removed.'),
     P('data، health، status، audit، argmap، inspect، timeline، library ← بخشِ شواهد: دیتاست، ادعاها به تفکیکِ موضوع، ممیزی، سلامت، نقشهٔ استدلال، وارسی، خطِ زمان، شش مدخلِ کتابخانه.', 'Evidence pages map to the evidence entries.'),
     P('two-irans، shared، timeline ← تاریخ: دو ایران، هشت پله، دفترِ مناقشه‌ها، ایران و اسرائیل.', 'History pages map to the history entries.'),
     P('sanad-rahbordi، eraee-rahbordi، europe، downloads، QA فایل‌ها ← راهبرد: سندِ راهبردی، ارائهٔ اروپا و فایل‌ها.', 'Strategy pages map to the strategy entries.'),
     P('gam (قدمِ تو)، birds، plan.me، transitions-risks ← عمل: قدمِ تو، سی مرغ (شش مدخل)، بیست گروه، پانزده خطر، روز آزادی، سهمِ من.', 'Action pages map to the action entries.'),
     P('plan، circle، sim، transitions، problems، map ← پروژه: نقشهٔ کلان، علم‌ها، دفترِ ویرانی‌ها، محصولات، میزِ دایره‌ای، نقشهٔ مشکل‌ها، ابزارها، فهرستِ کارهای مانده.', 'Project pages map to the project entries.'),
     P('صفحهٔ story (کارگاهِ نوشتنِ یک متنِ شخصی) بخشی از ادعاها یا بازی نیست و محتوایش در این ویکی نیامده؛ فقط وجودش ثبت شده است.', 'The story page (a personal writing workshop) is not part of the claims or the game and its content is deliberately not reproduced here; only its existence is noted.', [], True),
     P('پیشنهادِ مرتب‌سازی (انجام نشده، فقط پیشنهاد): صفحهٔ عمومی به چهار ورودی کاهش یابد (بازی، شواهد، قدمِ تو، دانلود) و بقیه از زیرِ همین‌ها به ابزارها پیوند بخورند؛ نسخه‌های خالیِ nights، players و rules حذف شوند.', 'Tidy-up proposal (not done, only suggested): reduce the public entrance to four doors and link the rest as tools beneath them; remove the empty stubs.', [], True)],
    [L('simorgh:tools-directory', 'فهرستِ ابزارها', 'Tools directory'), L('simorgh:backlog', 'کارهای مانده', 'Backlog')], 'simorgh:project')

new('backlog', T('کارهای انجام‌شده و مانده', 'Done and remaining work'),
    T('فهرستِ کارهای پروژه با وضعِ هرکدام (انجام‌شده یا مانده)، که دفترِ پروژه هر روز به‌روز می‌کند.',
      'The project\'s work list with the status of each (done or remaining), updated daily by the project log.'),
    [P(f"{x[1]} [{ {'done': 'انجام شد', 'todo': 'مانده', 'doing': 'در حال انجام'}.get(x[2], x[2]) }]", f'{x[1]}: status.', [], x[2] != 'done') for x in BK],
    [L('simorgh:master-plan', 'نقشهٔ کلان', 'Master plan')], 'simorgh:project')
