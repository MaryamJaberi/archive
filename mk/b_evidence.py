from common import *
from a_game import K
import re

def mk(cite, year, tier=2, prefix=None):
    return src(prefix or cite[:60], cite, year, tier)

# real sources used by the claims dataset and library
SRC = {
 'abrah93': mk('Abrahamian, E. (1993). Khomeinism: Essays on the Islamic Republic. University of California Press.', 1993),
 'keddie81': mk('Keddie, N. R. (1981). Roots of Revolution: An Interpretive History of Modern Iran. Yale University Press.', 1981),
 'keddie03': src('Keddie, N. R. (2003). Modern Iran'),
 'abisaab': mk('Abisaab, R. J. (2004). Converting Persia: Religion and Power in the Safavid Empire. I.B. Tauris.', 2004),
 'newman': mk('Newman, A. J. (2006). Safavid Iran: Rebirth of a Persian Empire. I.B. Tauris.', 2006),
 'newman93': mk('Newman, A. J. (1993). The Myth of the Clerical Migration to Safawid Iran. Die Welt des Islams, 33.', 1993),
 'matthee': mk('Matthee, R. (2012). Persia in Crisis: Safavid Decline and the Fall of Isfahan. I.B. Tauris.', 2012),
 'tucker': mk('Tucker, E. (2006). Nadir Shah\'s Quest for Legitimacy in Post-Safavid Iran. University Press of Florida.', 2006),
 'litvak': mk('Litvak, M. (1998). Shi\'i Scholars of Nineteenth-Century Iraq: The Ulama of Najaf and Karbala. Cambridge University Press.', 1998),
 'akhavi': mk('Akhavi, S. (1980). Religion and Politics in Contemporary Iran: Clergy-State Relations in the Pahlavi Period. SUNY Press.', 1980),
 'arjomand': mk('Arjomand, S. A. (1984). The Shadow of God and the Hidden Imam: Religion, Political Order, and Societal Change in Shi\'ite Iran from the Beginning to 1890. University of Chicago Press.', 1984),
 'amanat': mk('Amanat, A. (1989). Resurrection and Renewal: The Making of the Babi Movement in Iran, 1844-1850. Cornell University Press.', 1989),
 'sarshar': mk('Sarshar, H. (Ed.). (2002). Esther\'s Children: A Portrait of Iranian Jews. Center for Iranian Jewish Oral History.', 2002),
 'kad18': mk('Kadivar, M. A. (2018). Mass Mobilization and the Durability of New Democracies. American Sociological Review, 83(2).', 2018),
 'elster': mk('Elster, J. (2004). Closing the Books: Transitional Justice in Historical Perspective. Cambridge University Press.', 2004),
 'hayner': mk('Hayner, P. B. (2001). Unspeakable Truths: Confronting State Terror and Atrocity. Routledge.', 2001),
 'teitel': mk('Teitel, R. G. (2000). Transitional Justice. Oxford University Press.', 2000),
 'sharp': mk('Sharp, G. (1973). The Politics of Nonviolent Action, Part Two: The Methods of Nonviolent Action. Porter Sargent.', 1973),
 'moin': mk('Moin, B. (1999). Khomeini: Life of the Ayatollah. I.B. Tauris.', 1999),
 'iranica': mk('Encyclopaedia Iranica. ISRAEL i. Relations with Iran. https://iranicaonline.org', None),
 'ushmm': mk('United States Holocaust Memorial Museum. Encyclopedia entry: Abdol Hossein Sardari.', None),
 'wb_lit': mk('World Bank. Literacy rate, adult total (SE.ADT.LITR.ZS). UNESCO Institute for Statistics.', None),
 'michels': mk('Michels, R. (1911). Zur Soziologie des Parteiwesens in der modernen Demokratie (Political Parties).', 1911),
 'abrah08': src('Abrahamian, E. (2008). A History of Modern Iran'),
 'abrah99': src('Abrahamian, E. (1999). Tortured Confessions'),
 'dod': mk('Bueno de Mesquita, B., & Smith, A. (2011). The Dictator\'s Handbook: Why Bad Behavior is Almost Always Good Politics. PublicAffairs.', 2011),
 'svolik': mk('Svolik, M. W. (2012). The Politics of Authoritarian Rule. Cambridge University Press.', 2012),
 'gwf': mk('Geddes, B., Wright, J., & Frantz, E. (2018). How Dictatorships Work: Power, Personalization, and Collapse. Cambridge University Press.', 2018),
 'ar06': mk('Acemoglu, D., & Robinson, J. A. (2006). Economic Origins of Dictatorship and Democracy. Cambridge University Press.', 2006),
 'linz': src('Linz, J. J., & Stepan, A. (1996). Problems of Democratic Transition'),
 'prz': mk('Przeworski, A. (1991). Democracy and the Market: Political and Economic Reforms in Eastern Europe and Latin America. Cambridge University Press.', 1991),
 'hunt': mk('Huntington, S. P. (1991). The Third Wave: Democratization in the Late Twentieth Century. University of Oklahoma Press.', 1991),
 'parsa': mk('Parsa, M. (2016). Democracy in Iran: Why It Failed and How It Might Succeed. Harvard University Press.', 2016),
 'harris': mk('Harris, K. (2017). A Social Revolution: Politics and the Welfare State in Iran. University of California Press.', 2017),
 'ostovar': mk('Ostovar, A. (2016). Vanguard of the Imam: Religion, Politics, and the Iran\'s Revolutionary Guards. Oxford University Press.', 2016),
 'afary': mk('Afary, J. (1996). The Iranian Constitutional Revolution, 1906-1911. Columbia University Press.', 1996),
 'walter': mk('Walter, B. F. (2022). How Civil Wars Start: And How to Stop Them. Crown.', 2022),
 'dodge': mk('Dodge, T. (2012). Iraq: From War to a New Authoritarianism. Routledge/IISS.', 2012),
 'tufekci': mk('Tufekci, Z. (2017). Twitter and Tear Gas: The Power and Fragility of Networked Protest. Yale University Press.', 2017),
 'attar': mk('Attar of Nishapur. Mantiq al-Tayr (The Conference of the Birds).', None),
 'ferdowsi': mk('Ferdowsi. Shahnameh (critical edition: Khaleghi-Motlagh).', None),
}
S_ = SRC; S_.update({k: v for k, v in K.items() if v})

# ------------ claims by topic ------------
TOPIC = {
 'demography': ('claims-demography', 'ادعاهای جمعیت و ساختار', 'Claims: demography and structure'),
 'economy': ('claims-economy', 'ادعاهای اقتصاد و معیشت', 'Claims: economy and livelihood'),
 'history': ('claims-history', 'ادعاهای تاریخ', 'Claims: history'),
 'iran-israel': ('claims-iran-israel', 'ادعاهای ایران و اسرائیل', 'Claims: Iran and Israel'),
 'model': ('claims-model', 'ادعاهای مدلِ هزینه و سناریو', 'Claims: cost model and scenarios'),
 'politics': ('claims-politics', 'ادعاهای سیاست و افکار عمومی', 'Claims: politics and public opinion'),
 'resistance': ('claims-resistance', 'ادعاهای مقاومت مدنی و گذار', 'Claims: civil resistance and transition'),
 'security': ('claims-security', 'ادعاهای امنیت و جنگ', 'Claims: security and war'),
}
SRCMAP = [  # (substring in claim source, key)
 ('چنووث و استفان', 'cs'), ('اریکا چنووث', 'ch21'), ('کارهای متأخرِ چنووث', 'ch21'), ('کوران', 'kuran'), ('کرزمن', 'kurzman'),
 ('Iran Between Two Revolutions', 'abrah82'), ('Khomeinism', 'abrah93'), ('Roots of Revolution', 'keddie81'),
 ('Modern Iran', 'keddie03'), ('Converting Persia', 'abisaab'), ('Safavid Iran', 'newman'), ('Myth of the Clerical Migration', 'newman93'),
 ('Persia in Crisis', 'matthee'), ("Nadir Shah's Quest", 'tucker'), ('Shi\'i Scholars', 'litvak'), ('لیتواک', 'litvak'),
 ('Religion and Politics in Contemporary Iran', 'akhavi'), ('Shadow of God', 'arjomand'), ('Resurrection and Renewal', 'amanat'),
 ("Esther's Children", 'sarshar'), ('Mass Mobilization', 'kad18'), ('کدیور', 'kadivar22'), ('Closing the Books', 'elster'),
 ('Unspeakable Truths', 'hayner'), ('Transitional Justice', 'teitel'), ('Nonviolent Action', 'sharp'), ('اودانل', 'odon'),
 ('Khomeini: Life of the Ayatollah', 'moin'), ('ISRAEL i', 'iranica'), ('USHMM', 'ushmm'), ('SE.ADT.LITR.ZS', 'wb_lit'),
 ('لویتسکی', 'lw'), ('میخلز', 'michels'), ('شلینگ', 'schelling'),
]
base_note = 'ارجاعِ این ادعا به «گزارشِ مبنای پروژه» (تحلیلِ مدوّنِ داخلی) است، نه به یک منبعِ مستقلِ منتشرشده؛ ردهٔ آن به همین دلیل پایین‌تر از دادهٔ اولیه است.'
by_topic = {}
for c in CLAIMS:
    t = c['topic']; t = 'security' if t == 'war' else t
    by_topic.setdefault(t, []).append(c)
for t, (slug, fa, en) in TOPIC.items():
    cl = by_topic[t]
    pts = []
    for c in cl:
        keys = []
        for sub, k in SRCMAP:
            if sub in c['source'] and S_.get(k) and S_[k] not in keys: keys.append(S_[k])
        tail = f" شرطِ ابطال: {c['falsifier']}"
        if c['contested']: tail += ' (محلِ نزاع)'
        if c['note']: tail += f" یادداشت: {c['note']}"
        if not keys:
            tail += ' ' + ('منبع: مدلِ خودِ پروژه، نه یافتهٔ بیرونی.' if 'مدلِ خود' in c['source'] or 'حسابیِ' in c['source'] else base_note)
        pts.append(P(f"{c['fa']} ({c['value']}؛ {c['period']}؛ ردهٔ {c['tier']}؛ {c['basis']}).{tail}",
                     f"Claim {c['id']}: value, period, tier {c['tier']} and falsifier as in the Persian text.",
                     keys, flag=(c['tier'] == 3 or c['contested'])))
    new(slug, T(fa, en),
        T(f"{len(cl)} ادعای منبع‌دار از مجموعهٔ ۸۴ادعایی، هر کدام با مقدار، دوره، ردهٔ اعتبار (۱ داده/سند، ۲ پژوهش، ۳ برآورد یا مدل) و شرطی که آن را باطل می‌کند. ادعایی که نتواند بگوید چه چیز ردش می‌کند ادعا نیست.",
          f"{len(cl)} sourced claims of the 84-claim set, each with value, period, tier (1 data/document, 2 research, 3 estimate or model) and the condition that would refute it."),
        pts,
        [L('simorgh:dataset-84', 'جدولِ ۸۴ ادعا (ابزار)', '84-claim table (tool)'), L('simorgh:audit', 'ممیزیِ ضعف‌ها', 'Audit of weaknesses'),
         L('simorgh:inspect-claim', 'وارسیِ یک ادعا', 'Inspect a claim')], 'simorgh:evidence')

new('dataset-84', T('دیتاستِ ۸۴ ادعا و جدولِ داده', 'The 84-claim dataset and data table'),
    T('پشتِ همهٔ صفحه‌ها یک دیتاستِ باز است: ۸۴ ادعا، هر کدام با مقدار، دوره، مبنا، ردهٔ اعتبار، منبع، شرطِ ابطال، جای استفاده و نشانِ محل نزاع. جدولِ داده همین را قابل‌جست‌وجو می‌کند.',
      'Behind every page is an open dataset: 84 claims with value, period, basis, tier, source, falsifier, where used and a contested flag. The data table makes it searchable.'),
    [P('ردهٔ ۱: ۲۱ ادعا (دادهٔ اولیه یا سند)؛ ردهٔ ۲: ۳۲ (پژوهش یا ادبیاتِ تخصصی)؛ ردهٔ ۳: ۳۱ (برآورد، مدل یا ارزیابیِ کیفی). موضوع‌ها: جمعیت، اقتصاد، تاریخ، ایران و اسرائیل، مدل، سیاست، مقاومت، امنیت و جنگ.', 'Tier 1: 21 claims (primary data or documents); tier 2: 32 (research); tier 3: 31 (estimates, models, qualitative judgement). Topics as listed.'),
     P('قاعدهٔ دیتاست: ادعایی که نتواند بگوید چه شواهدی ردش می‌کند، ادعا نیست؛ و هر عدد که منبعِ قابل‌ارجاع نداشت ننوشته شد.', 'Dataset rule: a claim that cannot say what evidence would refute it is no claim; any number without a citable source was not written.'),
     P('فایل‌ها: claims-dataset.json، problems-dataset.json، و جدول در صفحهٔ data.', 'Files: claims-dataset.json, problems-dataset.json and the table in the data page.')],
    [L(f'simorgh:{v[0]}', v[1], v[2]) for v in TOPIC.values()] + [L('simorgh:audit', 'ممیزی', 'Audit'), L('simorgh:dataset-health', 'سلامتِ دیتاست', 'Dataset health')], 'simorgh:evidence')

new('audit', T('ممیزیِ ضعف‌ها: آنچه اگر ننویسیم منتقد پیدا می‌کند', 'Audit of weaknesses'),
    T('پروژه ضعف‌های خودش را علنی فهرست کرده، چون اگر خودش نگوید اولین منتقدِ جدی پیدایش می‌کند. یافته‌های اصلی در یک نگاه.',
      'The project lists its own weaknesses openly, since otherwise the first serious critic will find them. Main findings at a glance.'),
    [P('۱۴ ادعا (۱۸٪) به یک ارجاعِ جمعی بند است: کلِ بلوکِ اقتصادی و جمعیتی به یک گزارشِ مدوّن وصل است که خودش به مرکز آمار، مرکز پژوهش‌های مجلس، بانک جهانی و پیمایش‌ها تکیه می‌کند؛ پس این ادعاها مستقل از هم تأیید نشده‌اند.', '14 claims (18 percent) rest on one collective reference: the whole economic and demographic block hangs on one compiled report; they are not independently confirmed.'),
     P('متنِ اصلی پیش از جنگِ ۱۴۰۴–۱۴۰۵ نوشته شده و بخشی از اعداد پیش از جنگ‌اند؛ باید با دادهٔ تازه دوباره سنجیده شوند.', 'The core text predates the 2025-26 war and some numbers are pre-war; they must be re-checked against new data.'),
     P('«۲۶۰۰ در برابر ۲۷۰۰ سال» در دو جا فرق می‌کند چون نقطهٔ آغازشان فرق دارد (اسارتِ بابل در برابر نخستین پیوندها)؛ باید هر جا یکی بماند و نقطهٔ آغاز گفته شود.', '"2600 versus 2700 years" differs because the origin points differ; one should remain and its start be stated.'),
     P('«۸۰ تا ۹۰ درصدِ مسئله» (اثرِ موضع‌گیریِ صریح نسبت به رفتارِ هواداران) عددی بدونِ روش است و فقط به‌عنوانِ داوریِ کیفیِ نقل‌شده در منبع آمده.', '"80 to 90 percent of the problem" is a number without method, quoted only as a qualitative judgement from the source.', [], True),
     P('رقمِ ≈۵۰ میلیارد دلارِ سالانهِ فرار مغزها منبعِ اولیه ندارد و فقط به‌صورت «برآوردِ منسوب به بانکِ جهانی» نقل شده؛ مقایسه‌اش با صادراتِ نفتِ ۲۰۱۹ هم‌جنس نیست و در میزِ نقد هم همین گفته شد.', 'The ≈50 billion dollars a year brain-drain figure has no primary source and is quoted as "attributed to the World Bank"; comparing it with 2019 oil exports is not like for like.', [], True),
     P('۱۰ از ۱۸ کارتِ قدمِ تو (در نسخهٔ آن زمان) پشتوانهٔ دیتاست نداشتند؛ حالا کارت‌ها ۲۳ تا هستند و باید دوباره سنجیده شوند.', '10 of 18 "your step" cards lacked dataset backing at the time; there are now 23 cards and they must be re-checked.'),
     P('ناهمخوانیِ شمارش: صفحه‌ها گاهی ۷۶ و گاهی ۸۴ ادعا می‌گویند؛ شمارهٔ درست ۸۴ است.', 'Count mismatch: some pages say 76 claims, others 84; 84 is correct.')],
    [L('simorgh:dataset-84', 'دیتاست', 'Dataset'), L('simorgh:dataset-health', 'سلامتِ دیتاست', 'Dataset health'), L('simorgh:nine-faction-critique', 'میزِ نقد', 'Critique table')], 'simorgh:evidence')

new('dataset-health', T('سلامتِ دیتاست و وضعیتِ اسناد', 'Dataset health and document status'),
    T('دو ابزارِ زنده: «سلامت» شمارندهٔ زندهٔ دیتاست (چند ادعا، چند رده، چند محلِ نزاع) و «وضعیت» که برای هر سند می‌گوید در چه مرحله‌ای است. هر دو برای این‌اند که همیشه بدانیم کجای کار ایستاده‌ایم.',
      'Two live tools: "health" is a live counter of the dataset and "status" says what stage each document is at.'),
    [P('سلامت: شمارندهٔ ادعاها بر حسب رده و موضوع، و ادعاهای محلِ نزاع.', 'Health: counters by tier and topic, plus contested claims.'),
     P('وضعیتِ سند: پیش‌نویس، نیازمندِ بازبینی، یا تثبیت‌شده؛ برای هر صفحه.', 'Document status: draft, needs review, or settled, per page.')],
    [L('simorgh:dataset-84', 'دیتاست', 'Dataset'), L('simorgh:audit', 'ممیزی', 'Audit')], 'simorgh:evidence')

new('argmap', T('نقشهٔ استدلال', 'Argument map'),
    T('پانزده گره و هجده پیوند در پنج گام: استعاره، ادعا، شاهد، ممیزی، عمل؛ نشان می‌دهد هر نتیجه از کدام ادعا و کدام شاهد می‌آید و کجا ضعیف است.',
      'Fifteen nodes and eighteen links in five steps: metaphor, claim, evidence, audit, action; shows which claim and evidence each conclusion comes from and where it is weak.'),
    [P('پنج گام: استعاره، ادعا، شاهد، ممیزی، عمل.', 'Five steps: metaphor, claim, evidence, audit, action.'),
     P('هر گره به ادعاهای دیتاست وصل است؛ گرهی که پشتوانه ندارد همان‌جا نشان داده می‌شود.', 'Each node links to dataset claims; a node without support is shown as such.')],
    [L('simorgh:dataset-84', 'دیتاست', 'Dataset'), L('simorgh:inspect-claim', 'وارسیِ ادعا', 'Inspect a claim'), L('simorgh:audit', 'ممیزی', 'Audit')], 'simorgh:evidence')

new('inspect-claim', T('وارسیِ یک ادعا در چهار گام', 'Inspecting a claim in four steps'),
    T('ابزاری که هر ادعا را در چهار گام می‌گذراند: چه می‌گوید، از کجاست، چه چیز ردش می‌کند، و چقدر می‌شود بر آن تکیه کرد.',
      'A tool that walks any claim through four steps: what it says, where it comes from, what would refute it, and how far it can be relied on.'),
    [P('چهار گام: متنِ ادعا، منبع و ردهٔ اعتبار، شرطِ ابطال، و حکمِ تکیه‌پذیری.', 'Four steps: statement, source and tier, falsifier, reliability verdict.')],
    [L('simorgh:dataset-84', 'دیتاست', 'Dataset'), L('simorgh:argmap', 'نقشهٔ استدلال', 'Argument map')], 'simorgh:evidence')

# ------------ library ------------
LIB = [
 ('library-collapse', 'کتابخانه: چرا حکومت‌ها ناگهان می‌افتند', 'Library: why regimes fall suddenly',
  'پنج منبعِ هستهٔ نظریِ ادعای اصلی: همه می‌دانند، هیچ‌کس نمی‌گوید، تا لحظه‌ای که همه هم‌زمان می‌گویند.',
  [('Kuran (1995) Private Truths, Public Lies', 'هسته: نظریهٔ «پنهان‌سازیِ ترجیح»؛ اگر یک کتاب اضافه شود این است.', 'kuran'),
   ('Kuran (1991) «Now Out of Never»', 'هسته: چرا فروپاشیِ ۱۹۸۹ را هیچ‌کس ندید؛ کوتاه و بهترین پاسخ به ژانرِ «تاریخِ سقوط را می‌گویم».', 'kuran91'),
   ('Kurzman (2004) The Unthinkable Revolution in Iran', 'هسته: تا هفته‌های آخر ۵۷ حتی آنان که در خیابان بودند شدنی نمی‌دانستند.', 'kurzman'),
   ('Lohmann (1994) The Dynamics of Informational Cascades', 'تظاهراتِ دوشنبه‌های لایپزیگ به‌مثابهٔ آبشار اطلاعاتی؛ مدلِ کمیِ همان استعارهٔ میز.', None),
   ('Olson (1965) The Logic of Collective Action', 'مسئلهٔ سواریِ مجانی: چرا اکثریتِ ناراضی لزوماً حرکت نمی‌کند.', 'olson')]),
 ('library-power', 'کتابخانه: نظریهٔ بازی و ساختارِ قدرت', 'Library: game theory and power structure',
  'ادبیاتِ استانداردِ ادعای «پروپوزالی در قالبِ نظریهٔ بازی»؛ شامل یک منبعِ مخالف.',
  [('Bueno de Mesquita & Smith (2011) The Dictator\'s Handbook', 'هسته: نظریهٔ «هستهٔ برنده»؛ چرا «کجای میز نشسته‌ای» پرسشِ درستی است.', 'dod'),
   ('Svolik (2012) The Politics of Authoritarian Rule', 'هسته: دو مسئلهٔ هر دیکتاتور، کنترلِ مردم و کنترلِ خودی‌ها.', 'svolik'),
   ('Geddes, Wright & Frantz (2018) How Dictatorships Work', 'داده‌محور: رژیم‌های اقتدارگرا از ۱۹۴۶ چطور تمام شده‌اند.', 'gwf'),
   ('Acemoglu & Robinson (2006) Economic Origins of Dictatorship and Democracy', 'مسئلهٔ «تعهدِ معتبر»؛ هستهٔ هر طرحِ گذارِ مذاکره‌شده.', 'ar06'),
   ('Schelling (1960) The Strategy of Conflict', 'چانه‌زنی، تهدیدِ معتبر، نقطهٔ کانونی؛ بدونِ آن «نظریهٔ بازی» ناقص است.', 'schelling'),
   ('Levitsky & Way (2022) Revolution and Dictatorship', 'نقدِ ما: رژیم‌های زادهٔ انقلابِ اجتماعی به‌طرزِ غیرعادی بادوام‌اند؛ قیاس با اروپای شرقیِ ۱۹۸۹ ممکن است اساساً غلط باشد.', 'lw')]),
 ('library-transition', 'کتابخانه: گذار از اینجا به آنجا', 'Library: transition from here to there',
  'منابعِ تجربی و نظریِ گذار؛ شامل دادهٔ NAVCO، قاعدهٔ ۳٫۵ درصد و نقدِ پژوهشگرِ ایرانی.',
  [('O\'Donnell & Schmitter (1986) Transitions from Authoritarian Rule', 'هسته: چارچوبِ تندرو/میانه‌رو در هر دو اردوگاه و منطقِ «پیمان»؛ ستون‌فقراتِ هر تحلیلِ گذار.', 'odon'),
   ('Chenoweth & Stephan (2011) Why Civil Resistance Works', 'هسته: دادهٔ NAVCO، ۳۲۳ خیزشِ ۱۹۰۰ تا ۲۰۰۶، ۵۳٪ در برابر ۲۶٪؛ مهم‌ترین منبعِ تجربیِ «قدمِ تو».', 'cs'),
   ('Chenoweth (2021) Civil Resistance: What Everyone Needs to Know', 'هسته: نسخهٔ کوتاه‌تر و بدونِ پنهان‌کردنِ افتِ نرخِ موفقیت؛ هر که فقط «۳٫۵٪» را نقل می‌کند این را نخوانده.', 'ch21'),
   ('Kadivar (2022) Popular Politics and the Path to Durable Democracy', 'هسته: جنبش‌های طولانی و سازمان‌یافته دموکراسیِ بادوام‌تری می‌سازند؛ نویسنده ایرانی است.', 'kadivar22'),
   ('Linz & Stepan (1996) Problems of Democratic Transition and Consolidation', 'گذار از سلطانیسم؛ بدترین حالت برای گذارِ نرم.', 'linz'),
   ('Przeworski (1991) Democracy and the Market', 'دموکراسی به‌مثابهٔ «عدم‌قطعیتِ نهادینه‌شده».', 'prz'),
   ('Huntington (1991) The Third Wave', 'تیپولوژی: دگرگونی از بالا، جایگزینی از پایین، گذارِ توافقی؛ «سه راه» را می‌شود روی آن نگاشت.', 'hunt'),
   ('Sharp, From Dictatorship to Democracy', 'عملیاتی‌ترین متنِ فهرست؛ واژگانِ مشترکِ بخشی از مخاطب.', None)]),
 ('library-iran', 'کتابخانه: ایران، تاریخ، ساختار، سپاه', 'Library: Iran, history, structure, the Guards',
  'منابعِ فهمِ ایران؛ شامل نقدِ «جامعهٔ کوتاه‌مدت» به خوش‌بینیِ مجموعه.',
  [('Abrahamian (1982) Iran Between Two Revolutions', 'هسته: مرجعِ پایه؛ بدونِ آن بخشِ تاریخیِ هر تحلیل روی هوا می‌ماند.', 'abrah82'),
   ('Parsa (2016) Democracy in Iran', 'هسته: همان پرسشِ مجموعه با روشِ جامعه‌شناسیِ تطبیقی؛ اصلاحِ درون‌سیستمی بن‌بست است.', 'parsa'),
   ('Harris (2017) A Social Revolution', 'هسته: دولتِ رفاه و طبقهٔ متوسطِ تازه؛ وفاداری‌ها هیچ‌وقت ساده نبوده‌اند.', 'harris'),
   ('Ostovar (2016) Vanguard of the Imam', 'تاریخِ نهادیِ سپاه؛ مرجعِ استانداردِ انگلیسی.', 'ostovar'),
   ('Abrahamian (1999) Tortured Confessions', 'تاریخِ «اعترافِ اجباری» در ایران.', 'abrah99'),
   ('Afary (1996) The Iranian Constitutional Revolution, 1906–1911', 'ریشهٔ مشروطه با تناقض‌هایش، نه نسخهٔ آرمانی‌شده.', 'afary'),
   ('Katouzian، «جامعهٔ کوتاه‌مدت»', 'نقدِ ما: اگر در ایران هر دوره میراثِ دورهٔ قبل را پاک می‌کند، عوض‌شدنِ حکومت چیزی را تضمین نمی‌کند.', 'nokar')]),
 ('library-after-fall', 'کتابخانه: بعد از سقوط', 'Library: after the fall',
  'فوری‌ترین بخش: بیشترِ منابع می‌گویند خطرِ اصلی بعد از سقوط است، نه پیش از آن.',
  [('Walter (2022) How Civil Wars Start', 'نقدِ ما: خطرناک‌ترین وضعیت میانه است، همان‌جا که هر گذار از آن می‌گذرد؛ هر برآوردِ هزینه‌ای که این را حساب نکند کم‌برآورد است.', 'walter'),
   ('Dodge (2012) Iraq: From War to a New Authoritarianism', 'نقدِ ما: انحلالِ یک‌بارهٔ ارتش و دستگاهِ حزبی در ۲۰۰۳ دولت را از بین برد؛ هشدار به هر طرحِ «انحلالِ سپاه».', 'dodge'),
   ('Elster (2004) Closing the Books', 'هسته: عدالتِ انتقالی در بسترِ تاریخی؛ چه کسی محاکمه شود، چه کسی عفو.', 'elster'),
   ('Hayner (2001) Unspeakable Truths', 'کمیسیون‌های حقیقت: چه برمی‌آید و چه برنمی‌آید.', 'hayner'),
   ('همه‌پرسیِ شیلی ۱۹۸۸ (کارزارِ «نه»)', 'الگوی عملیاتیِ رفراندوم زیرِ حکومتِ اقتدارگرا؛ نزدیک‌ترین نمونه به آنچه مجموعه پیشنهاد می‌دهد.', None)]),
 ('library-data-myth', 'کتابخانه: حقوقِ بشر، رسانه، داده، اسطوره', 'Library: rights, media, data, myth',
  'مرجع‌های داده برای هر ادعای عددی دربارهٔ سرکوب، و منابعِ لایهٔ روایی.',
  [('مأموریتِ مستقلِ حقیقت‌یابِ سازمان ملل دربارهٔ ایران (OHCHR)', 'داده: مرجعِ رسمی و قابل‌استناد؛ مأموریت در ژانویهٔ ۲۰۲۶ تمدید شد.', None),
   ('Freedom House، گزارشِ سرکوبِ فراملی', 'داده: «این مسئلهٔ خودِ توست، نه خیریه» برای مخاطبِ اروپایی.', None),
   ('ICCT، Crisis Group، ECFR', 'داده: تحلیلِ سیاستیِ کوتاه برای مخاطبِ بروکسل؛ ICCT منبعِ ارائهٔ اروپاست.', None),
   ('Amnesty، HRW، IHR، مرکز برومند، HRANA', 'داده: مستنداتِ موردی و آمارِ اعدام؛ منبعِ هر ادعای عددی دربارهٔ سرکوب باید یکی از این‌ها باشد.', None),
   ('NetBlocks، IODA، Access Now', 'داده: قطعیِ اینترنت بلادرنگ؛ Access Now خطِ کمکِ امنیتِ دیجیتال هم دارد.', None),
   ('V-Dem، NAVCO، ACLED، UCDP', 'داده: شاخص‌های دموکراسی، کارزارها و اعتراض و درگیری؛ ورودیِ هر برآوردِ جدی.', None),
   ('Tufekci (2017) Twitter and Tear Gas', 'چرا جنبش‌های شبکه‌ای سریع بزرگ و سریع شکسته می‌شوند.', 'tufekci'),
   ('عطار، منطق‌الطیر', 'هسته: سیمرغ از اینجاست؛ سی مرغ که می‌فهمند دنبالِ خودشان بوده‌اند.', 'attar'),
   ('فردوسی، شاهنامه (تصحیح خالقی مطلق)', 'هسته: منبعِ همهٔ نمادها: ضحّاک، کاوه، فریدون، سیمرغ.', 'ferdowsi'),
   ('Encyclopaedia Iranica', 'مرجعِ اسطوره‌شناسی برای درست‌کاربردنِ نمادها.', None)]),
]
for slug, fa, en, sfa, items in [(a, b, c, d, e) for a, b, c, d, e in LIB]:
    new(slug, T(fa, en), T(sfa, en),
        [P(f'{t}: {d}', f'{t}: why it is on the shelf (Persian text).', [S_[k]] if k and S_.get(k) else [], flag=('نقدِ ما' in d)) for t, d, k in items],
        [L('simorgh:library-honesty', 'این فهرست چه نیست', 'What this list is not')], 'simorgh:evidence')
new('library-honesty', T('کتابخانه: این فهرست چه نیست', 'Library: what this list is not'),
    T('صداقتِ پایانیِ کتابخانه: کامل نیست، بی‌طرف نیست، جایگزینِ خواندنِ منبع نیست؛ و چند چیز عمداً در آن نیست.',
      'The library\'s closing honesty: it is not complete, not neutral, not a substitute for reading; and some things are deliberately missing.'),
    [P('کامل نیست؛ بی‌طرف نیست (بر اساسِ ادعاهای این مجموعه چیده شده)؛ توضیح‌ها راهنمای انتخاب‌اند، نه خلاصهٔ کتاب؛ و بیشترِ منابع به فارسی ترجمه نشده‌اند که خودش یکی از مشکل‌هاست.', 'Not complete; not neutral; blurbs guide choice rather than summarise; most sources are untranslated into Persian.'),
     P('عمداً نیست: کانال‌های «پیش‌بینیِ سقوط»، هر عددی که منبعِ قابل‌ارجاع نداشت، و هر نقل‌قولی که بدونِ سند به شخصی واقعی نسبت داده شود.', 'Deliberately absent: collapse-prediction channels, any number without a citable source, any quote attributed to a real person without a document.')],
    [L(f'simorgh:{s}', fa, en) for s, fa, en, _, _ in LIB], 'simorgh:evidence')
