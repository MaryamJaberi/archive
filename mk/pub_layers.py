"""Move science and history out of the Simorgh wiki into the public soc / tarikh wikis.
Runs the simorgh generators in memory (to reuse their text and sources), then writes public concepts.
Only general science and history goes public; nothing of the Simorgh plan."""
import sys, json, copy, glob
sys.path.insert(0, '.')
import common
import a_game, b_evidence, c_rest, d_review, e_gamaan, f_csr
from common import T, P, L, R
C = common.CREATED; SALL = common.S
PUB = json.load(open(f'{R}/core/sources.json'))   # committed registry, edited in place
OUTS = {}

def pts(slug, drop=()):
    return [copy.deepcopy(p) for i, p in enumerate(C[f'simorgh:{slug}']['points']) if i not in drop]

def reg(keys, wiki):
    for k in keys:
        e = copy.deepcopy(SALL[k]); e['wikis'] = sorted({w for w in e['wikis'] if w != 'simorgh'} | {wiki})
        if k in PUB:
            PUB[k]['wikis'] = sorted(set(PUB[k]['wikis']) | {wiki})
        else:
            PUB[k] = e

def concept(cid, kind, title, summary, points, links, parent, field):
    d = {'id': cid, 'kind': kind, 'title': title, 'aliases': [], 'parent': parent, 'field': field, 'summary': summary,
         'points': points, 'links': links, 'people': [], 'sources': [], 'booklets': [], 'origin': None, 'iran': None,
         'wikidata': None, 'status': 'draft'}
    for p in points:
        for k in p['sources']:
            if k not in d['sources']: d['sources'].append(k)
    OUTS[cid] = d; return d

def extend(cid, points, links=()):
    w, s = cid.split(':')
    d = OUTS.get(cid) or json.load(open(f'{R}/data/{w}/concepts/{s}.json'))
    for p in points:
        if p['text']['fa'] not in [q['text']['fa'] for q in d['points']]:
            d['points'].append(p)
            for k in p['sources']:
                if k not in d['sources']: d['sources'].append(k)
    for l in links:
        if not any(x['to'] == l['to'] for x in d['links']): d['links'].append(l)
    OUTS[cid] = d

# ---------------- tarikh ----------------
concept('tarikh:safavid-qajar', 'field', T('از صفویه تا قاجار: دین، دولت و روحانیت', 'From the Safavids to the Qajars: religion, state and clergy'),
        T('سه سده‌ای که ایران شیعه شد و روحانیتِ شیعه از کارگزارِ دولت به قدرتی مستقل با پول، پیرو و سلسله‌مراتبِ خودش بدل شد؛ زمینهٔ مشروطه و ۱۳۵۷.',
          'Three centuries in which Iran became Shia and the Shia clergy turned from state servants into an independent power with its own money, followers and hierarchy; the background to 1906 and 1979.'),
        [], [], 'tarikh:tarikh', None)
tp = pts('two-irans', drop=(3,))
concept('tarikh:shiism-becomes-iranian', 'concept', T('ایران چطور شیعه شد', 'How Iran became Shia'),
        C['simorgh:two-irans']['summary'], tp,
        [L('tarikh:clerical-rise-eight-steps', 'هشت پله تا قدرت', 'Eight steps to power'), L('tarikh:two-irans-dispute-ledger', 'دفترِ مناقشه‌ها', 'Dispute ledger'), L('tarikh:iran-and-jews', 'ایران و یهودیان', 'Iran and the Jews')],
        'tarikh:safavid-qajar', 'tarikh:safavid-qajar')
cp = pts('clerical-rise')
cp[-1] = P('۱۳۵۷: مردم مذهبی‌تر از دهه‌های پیش نشده بودند؛ پرسشِ درست این است که چرا وقتی رژیم افتاد فقط یک نیرو آمادهٔ گرفتنِ قدرت بود (حزب توده پس از ۱۳۳۲ متلاشی شد، جبههٔ ملی فلج شد). سازمان‌یافتگی، نه محبوبیت، برنده بود.',
           'Nineteen seventy-nine: people had not become more religious; the right question is why only one force was ready to take power when the regime fell. Organisation, not popularity, won.', cp[-1]['sources'], True)
concept('tarikh:clerical-rise-eight-steps', 'concept', T('پانصد سال بالا رفتن: هشت پلهٔ قدرتِ روحانیت', 'Five centuries of rising: eight steps of clerical power'),
        C['simorgh:clerical-rise']['summary'], cp,
        [L('tarikh:shiism-becomes-iranian', 'ایران چطور شیعه شد', 'How Iran became Shia'), L('tarikh:revolution-1979', 'انقلاب ۱۳۵۷', '1979 revolution'), L('tarikh:constitutional-revolution-1906', 'مشروطه', 'Constitutional Revolution')],
        'tarikh:safavid-qajar', 'tarikh:safavid-qajar')
concept('tarikh:two-irans-dispute-ledger', 'concept', T('دفترِ مناقشه‌ها: هفت ادعای رایج دربارهٔ روحانیت و شاهدِ نقضشان', 'Dispute ledger: seven common claims about the clergy and their counter-evidence'),
        C['simorgh:disputes-ledger']['summary'], pts('disputes-ledger'),
        [L('tarikh:clerical-rise-eight-steps', 'هشت پله', 'Eight steps'), L('tarikh:shiism-becomes-iranian', 'ایران چطور شیعه شد', 'How Iran became Shia')],
        'tarikh:safavid-qajar', 'tarikh:safavid-qajar')
concept('tarikh:iran-and-jews', 'concept', T('ایران و یهودیان: ۲۶۰۰ سال پیوند، ۴۷ سال دشمنیِ دو دولت', 'Iran and the Jews: 2,600 years of ties, 47 years of enmity between two states'),
        C['simorgh:iran-israel']['summary'], pts('iran-israel', drop=(4,)),
        [L('tarikh:shiism-becomes-iranian', 'ایران چطور شیعه شد', 'How Iran became Shia')], 'tarikh:neighbours', 'tarikh:neighbours')
extend('tarikh:revolution-1979', pts('lesson-1357', drop=(7,)),
       [L('tarikh:clerical-rise-eight-steps', 'هشت پله', 'Eight steps'), L('soc:civil-resistance-success-rates', 'موفقیتِ مقاومتِ مدنی', 'Civil resistance success'), L('soc:consent-theory-of-power', 'نظریهٔ رضایت', 'Consent theory')])

# ---------------- soc ----------------
N = d_review.N
ev = pts('exit-voice')
concept('soc:exit-voice-loyalty', 'concept', T('خروج، صدا، وفاداری: هیرشمن', 'Exit, voice and loyalty: Hirschman'),
        T('وقتی سازمانی رو به افول است اعضا سه راه دارند: می‌روند (خروج)، اعتراض می‌کنند (صدا) یا می‌مانند و تحمل می‌کنند (وفاداری). خروجِ آسان صدا را ضعیف می‌کند، چون پرمهارت‌ترین‌ها اول می‌روند؛ و وقتی خروج بسته شود فشار به سمتِ صدا می‌رود.',
          'Members of a declining organisation can leave (exit), protest (voice) or stay and endure (loyalty). Easy exit weakens voice because the most skilled leave first; when exit closes, pressure shifts to voice.'),
        [P('سازوکار: خروجِ آسان صدا را ضعیف می‌کند، چون پرمهارت‌ترین و پرانرژی‌ترین‌ها اول می‌روند؛ سازمانِ رو به افول با هر خروج کمتر زیرِ فشار است.', 'Mechanism: easy exit weakens voice because the most skilled and energetic leave first; a declining organisation faces less pressure with each exit.', [N['hirsch']]), ev[1], P('شاهد از ایران (گمان، تیر ۱۴۰۵): ۴۳٪ به نوعی می‌خواهند بروند و ۳۲٪ می‌خواهند قانونی بروند ولی امکانش را ندارند؛ یعنی «خروجِ بسته» برای بخشِ بزرگی از جامعه واقعیت است. نمونهٔ این پیمایش آنلاین و از راه فیلترشکن است.', 'Evidence from Iran (GAMAAN, June 2026): 43 percent want to leave in some form and 32 percent want to leave legally but cannot; a blocked exit for a large share. The sample is online and VPN-based.', [N['gam']], True), ev[2]],
        [L('soc:clear-horizon-exit-voice', 'افق روشن و مهاجرت', 'Clear horizon and migration'), L('soc:preference-falsification', 'تحریف ترجیحات', 'Preference falsification')],
        'soc:collective', 'soc:collective')
concept('soc:foreign-imposed-regime-change', 'concept', T('تغییرِ نظامِ تحمیل‌شده از بیرون', 'Foreign-imposed regime change'),
        T('وقتی یک قدرتِ خارجی حکومتی را با زور برمی‌دارد، چه می‌شود؟ پژوهشِ داونز و مونتن روی همهٔ موارد از ۱۸۱۶ نشان می‌دهد چنین تغییری به‌ندرت دموکراسی می‌سازد، مگر جایی که پیش‌شرط‌های داخلی از قبل بوده است.',
          'What happens when a foreign power removes a government by force? Downes and Monten find such change rarely produces democracy except where domestic preconditions already existed.'),
        [P('یافته: تغییرِ نظامِ تحمیل‌شده به‌طورِ کلی احتمالِ دموکراسی را بالا نمی‌برد؛ استثناها کشورهایی‌اند که ثروت، همگونی و تجربهٔ پیشینِ دموکراسی داشتند و جایی که مداخله‌گر خودش نهادسازیِ دموکراتیک را هدف گرفت.', 'Finding: foreign-imposed regime change does not generally raise the odds of democracy; exceptions are wealthy, homogeneous countries with prior democratic experience and cases where the intervener pursued institution-building.', [N['downes']]),
         P('سازوکار: حکومتِ تازه مشروعیتِ داخلی ندارد و به حامیِ بیرونی وابسته است؛ و فروپاشیِ دستگاهِ دولت (مثلِ انحلالِ ارتش و حزب در عراقِ ۲۰۰۳) خلأیی می‌سازد که گروه‌های مسلح پر می‌کنند.', 'Mechanism: the new government lacks domestic legitimacy and depends on its backer; collapse of the state apparatus (as in Iraq 2003) creates a vacuum armed groups fill.', [N['downes'], N['dodge']]),
         P('شاهد از ایران (گمان، تیر ۱۴۰۵): ۳۰٪ «مداخلهٔ نظامیِ خارجی» را راهِ مؤثرِ تغییر دانستند و جامعه دربارهٔ ماهیتِ جنگِ ۳۹روزه دو نیمه است (۴۲٪ تجاوز می‌دانند و تقریباً همین اندازه نه).', 'Evidence from Iran (GAMAAN, June 2026): 30 percent see foreign military intervention as effective, and society is split on the 39-day war.', [N['gam']], True)],
        [L('soc:civil-resistance-success-rates', 'موفقیتِ مقاومتِ مدنی', 'Civil resistance success'), L('soc:radical-minorities-violence-and-political-transitions', 'خشونت و گذار', 'Violence and transitions')],
        'soc:collective', 'soc:collective')
concept('soc:digital-repression', 'concept', T('سرکوبِ دیجیتال و قطعِ اینترنت', 'Digital repression and internet shutdowns'),
        T('حکومت‌ها یاد گرفته‌اند با نظارت، قطعِ اینترنت و دست‌کاریِ اطلاعات، هماهنگی را پیش از آنکه به خیابان برسد بشکنند. این یکی از دلیل‌هایی است که نرخِ موفقیتِ خیزش‌های مدنی در دهه‌های اخیر افت کرده است.',
          'Governments have learned to break coordination before it reaches the street through surveillance, shutdowns and information manipulation; one reason civil uprisings succeed less often than before.'),
        [P('فلدستاین سرکوبِ دیجیتال را در پنج شکل دسته‌بندی می‌کند: نظارت، سانسور، اطلاعاتِ نادرست، قطعِ اینترنت و آزارِ هدفمند؛ و نشان می‌دهد این ابزارها برای حکومت‌ها ارزان‌تر از سرکوبِ فیزیکی‌اند.', 'Feldstein groups digital repression into surveillance, censorship, disinformation, shutdowns and targeted harassment, cheaper for governments than physical repression.', [N['feld']]),
         P('چنووث (۲۰۲۱) افتِ نرخِ موفقیتِ مقاومتِ مدنی را بخشی به یادگیریِ حکومت‌ها نسبت می‌دهد، از جمله همین ابزارها؛ و هشدار می‌دهد جنبش‌هایی که فقط به شبکه‌های آنلاین تکیه دارند سریع بزرگ و سریع شکسته می‌شوند.', 'Chenoweth (2021) partly attributes the falling success rate to regime learning, including these tools; movements relying only on online networks grow fast and break fast.', [N['ch21']]),
         P('شاهد از ایران: به گزارشِ گمان (تیر ۱۴۰۵)، قطعیِ سراسریِ اینترنت در ۱۴۰۴–۱۴۰۵ ۸۸ روز طول کشید که نت‌بلاکس آن را طولانی‌ترین قطعیِ سراسریِ ثبت‌شده خواند؛ ۲۵٪ پاسخ‌دهندگان گفتند در اثرِ آن شغل یا منبعِ اصلیِ درآمدشان را از دست دادند.', 'Evidence from Iran: per GAMAAN the 2025-26 nationwide shutdown lasted 88 days, which NetBlocks called the longest recorded; 25 percent said they lost a job or main income because of it.', [N['gam']], True)],
        [L('soc:civil-resistance-success-rates', 'موفقیتِ مقاومتِ مدنی', 'Civil resistance success'), L('soc:coordination-focal-points', 'نقطهٔ کانونی', 'Focal points')],
        'soc:collective', 'soc:collective')
pl = pts('pillars-of-support')
extend('soc:consent-theory-of-power', [pl[0], P('شاهد از ایران (۱۳۵۷): به روایتِ چنووت و استفان، برادری با سرباز (گل در لولهٔ تفنگ، «ارتش جزوِ ملت است») روحیهٔ ارتش را فرو ریخت و اعتصابِ چرخشی دولت را از کار انداخت، چون سرباز نمی‌تواند پالایشگاه و نیروگاه را بچرخاند؛ به نقلِ کورزمن، فرماندهان بازداشتِ صد هزار نفر را بررسی کردند ولی زندان‌ها فقط جای پنج هزار نفر داشت.', 'Evidence from Iran (1979): fraternisation broke army morale and rolling strikes disabled the state; per Kurzman, commanders considered 100,000 arrests but jails had room for 5,000.', [N['cs'], f_csr.KZ])],
       [L('soc:security-defection-credible-commitment', 'ریزشِ نیروهای امنیتی', 'Security defection'), L('tarikh:revolution-1979', 'انقلاب ۱۳۵۷', '1979 revolution')])
extend('soc:transitional-justice-options', [P('مرزِ عفو در حقوقِ بین‌الملل: سیاستِ سازمان ملل عفوِ نسل‌کشی، جنایتِ جنگی، جنایت علیه بشریت و نقضِ فاحشِ حقوقِ بشر را نمی‌پذیرد. پس «عفوِ مشروط» در هر گذار فقط می‌تواند برای بدنهٔ بزرگی باشد که دستش به این جرم‌ها آلوده نیست.', 'The limit of amnesty in international law: UN policy does not accept amnesty for genocide, war crimes, crimes against humanity or gross human-rights violations; conditional amnesty can only cover those not implicated.', [N['ohchr']])])
extend('soc:civil-resistance-success-rates', [P('هشدارِ خودِ پژوهشگر: قاعدهٔ ۳٫۵ درصد یک مشاهدهٔ تاریخی است، نه قانون؛ و چنووث (۲۰۲۱) می‌گوید نرخِ موفقیت در دههٔ ۲۰۱۰ افت کرد. ایرانِ ۱۳۵۷ هم نشان می‌دهد کارزارِ خشونت‌پرهیزِ پیروز همیشه به دموکراسی نمی‌رسد، هرچند به گفتهٔ چنووت و استفان این استثناست.', 'The researchers\' own caveat: the 3.5 percent rule is an observation, not a law; success rates fell in the 2010s; and Iran 1979 shows a winning nonviolent campaign does not always yield democracy, though it is the exception.', [N['ch21'], N['cs']])],
       [L('soc:digital-repression', 'سرکوبِ دیجیتال', 'Digital repression'), L('soc:foreign-imposed-regime-change', 'تغییرِ تحمیل‌شده از بیرون', 'Foreign-imposed regime change'), L('tarikh:revolution-1979', 'انقلاب ۱۳۵۷', '1979 revolution')])

# ---------------- write ----------------
for cid, d in OUTS.items():
    w = cid.split(':')[0]
    for p in d['points']:
        reg(p['sources'], w)
    json.dump(d, open(f"{R}/data/{w}/concepts/{cid.split(':')[1]}.json", 'w'), ensure_ascii=False, indent=1)
o = json.load(open(f'{R}/data/tarikh/order.json'))
if 'tarikh:safavid-qajar' not in o:
    o.insert(o.index('tarikh:modern'), 'tarikh:safavid-qajar'); json.dump(o, open(f'{R}/data/tarikh/order.json', 'w'), ensure_ascii=False)
json.dump(PUB, open(f'{R}/core/sources.json', 'w'), ensure_ascii=False, indent=1)
print('written', sorted(OUTS))
