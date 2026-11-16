"""Pass 6: layer separation. History -> tarikh, science -> soc (both public, written by pub_layers.py),
dated numbers -> iran layer (private, iran/*.json in the vault). Simorgh keeps the game and strategy and links out."""
import json, copy
from common import *
from d_review import get, addp, addl, N

C = CREATED
MOVED = {'simorgh:two-irans': 'tarikh:shiism-becomes-iranian', 'simorgh:clerical-rise': 'tarikh:clerical-rise-eight-steps',
         'simorgh:disputes-ledger': 'tarikh:two-irans-dispute-ledger', 'simorgh:iran-israel': 'tarikh:iran-and-jews',
         'simorgh:lesson-1357': 'tarikh:revolution-1979'}
keep1357 = copy.deepcopy(C['simorgh:lesson-1357']['points'][7])
for k in MOVED: del C[k]
for d in C.values():
    seen = set(); out = []
    for l in d['links']:
        l['to'] = MOVED.get(l['to'], l['to'])
        if l['to'] not in seen: seen.add(l['to']); out.append(l)
    d['links'] = out

# history field: seven-nights moves here, plus a hub to the tarikh entries
C['simorgh:seven-nights']['field'] = C['simorgh:seven-nights']['parent'] = 'simorgh:history'
new('history-roots', T('ریشه‌های تاریخیِ میز (در ویکی تاریخ)', 'Historical roots of the table (in the history wiki)'),
    T('روایت‌های تاریخیِ پروژه (ایران چطور شیعه شد، هشت پلهٔ قدرتِ روحانیت، دفترِ مناقشه‌ها، ایران و یهودیان، و درس‌های ۱۳۵۷) تاریخ‌اند، نه بازی؛ برای همین به ویکی تاریخ رفته‌اند. اینجا فقط می‌گوید هرکدام برای میز چه معنایی دارد.',
      'The project\'s historical accounts are history, not game, so they moved to the history wiki. This entry only says what each means for the table.'),
    [P('ایران چطور شیعه شد و هشت پلهٔ قدرتِ روحانیت ← برای میز: «مافیا» ساختاری پانصدساله است با پول، پیرو و سلسله‌مراتبِ خودش؛ با یک موج نمی‌رود و جانشینش هم باید نهاد باشد، نه یک نفر.', 'Shi\'ism and the eight steps: the "Mafia" is a five-century structure with its own money, followers and hierarchy; it does not go with one wave and its successor must be an institution, not a person.'),
     P('دفترِ مناقشه‌ها ← برای میز: روایتِ تاریخیِ پروژه تفسیر است و نقطه‌های ضعفش علنی است؛ هر کارتِ بازی که به تاریخ تکیه دارد باید به این دفتر ارجاع دهد.', 'Dispute ledger: the project\'s historical account is interpretation with public weak points.'),
     P('ایران و یهودیان ← برای میز و ارائهٔ اروپا: دشمنیِ دو دولت ۴۷ سال است و پیوندِ دو سرزمین ۲۶۰۰ سال؛ جملهٔ اجباری «این دربارهٔ یک دولت است، نه یک دین و نه یک جامعه» در ارائهٔ اروپا می‌ماند.', 'Iran and the Jews: the mandatory sentence stays in the Europe deck.'),
     keep1357],
    [L('tarikh:shiism-becomes-iranian', 'ایران چطور شیعه شد', 'How Iran became Shia'), L('tarikh:clerical-rise-eight-steps', 'هشت پله', 'Eight steps'),
     L('tarikh:two-irans-dispute-ledger', 'دفترِ مناقشه‌ها', 'Dispute ledger'), L('tarikh:iran-and-jews', 'ایران و یهودیان', 'Iran and the Jews'),
     L('tarikh:revolution-1979', 'انقلاب ۱۳۵۷', '1979 revolution'), L('simorgh:seven-nights', 'هفت شب', 'Seven nights')], 'simorgh:history')

# exit-voice: the general mechanism now lives in soc:exit-voice-loyalty
ev = C['simorgh:exit-voice']
ev['points'] = [p for p in ev['points'] if not p['text']['fa'].startswith('سازوکار: خروجِ آسان')]
ev['summary'] = T('در بازیِ نسخهٔ یک کسی از میز بلند نمی‌شد؛ در ایران «خروج» بزرگ‌ترین حرکتِ پنهان است. نظریه (هیرشمن) در ویکی جامعه‌شناسی است؛ اینجا معنایش برای بازی و برنامه.',
                  'In version one nobody left the table; in Iran exit is the largest hidden move. The theory (Hirschman) is in the sociology wiki; here, its meaning for the game and the plan.')
addl('exit-voice', L('soc:exit-voice-loyalty', 'نظریه: خروج، صدا، وفاداری', 'Theory: exit, voice, loyalty'))
for s, extra in [('game-reality-map', ['soc:consent-theory-of-power', 'soc:digital-repression', 'soc:foreign-imposed-regime-change', 'soc:exit-voice-loyalty']),
                 ('pillars-of-support', ['soc:consent-theory-of-power', 'soc:security-defection-credible-commitment']),
                 ('three-paths', ['soc:foreign-imposed-regime-change', 'soc:pacted-transitions']),
                 ('pre-mortem', ['soc:digital-repression']), ('why-not-january', ['soc:digital-repression', 'soc:civil-resistance-success-rates']),
                 ('covenantal-transition', ['soc:transitional-justice-options', 'soc:pacted-transitions'])]:
    addl(s, *[L(x, 'نظریه در ویکی جامعه‌شناسی', 'Theory in the sociology wiki') for x in extra])
addp('covenantal-transition', keep1357)

# dated numbers -> iran layer; Simorgh keeps only what they mean for the game
g = C['simorgh:gamaan-2026']
keep = [p for p in g['points'] if p['text']['fa'].startswith(('برای منطقِ بازی', 'برای میثاق', 'محدودیت‌هایی'))]
g['points'] = [P('عددهای این پیمایش (گرایش، نظامِ دلخواه، شعارها، پرچم، نگرانی‌ها، مهاجرت، قطعِ اینترنت) در لایهٔ ایران ثبت‌اند؛ اینجا فقط معنایشان برای بازی آمده.', 'The survey\'s numbers live in the Iran layer; here only their meaning for the game.', [N['gam']])] + keep
g['title'] = T('پیمایشِ گمان ۱۴۰۵: معنایش برای میز', 'The 2026 GAMAAN survey: what it means for the table')
g['iran'] = 'iran:political-attitudes-2026'
cs = C['simorgh:current-situation']
cs['points'] = [p for p in cs['points'] if p['text']['fa'].startswith(('آنچه این عددها', 'محدودیت‌ها'))]
cs['points'].insert(0, P('عددهای تاریخ‌دارِ جنگ، معیشت و کار (رویترز، آبان ۱۴۰۵) و پیمایشِ گمان در لایهٔ ایران ثبت‌اند و همان‌جا به‌روز می‌شوند؛ این مدخل فقط معنایشان را برای راهبرد نگه می‌دارد.', 'The dated numbers on war, livelihood and work and the GAMAAN survey live and are updated in the Iran layer; this entry keeps only their meaning for strategy.', [N['reuters']]))
cs['title'] = T('وضعیتِ امروز: معنایش برای راهبرد (آبان ۱۴۰۵)', 'The situation now: what it means for strategy (November 2026)')
cs['iran'] = 'iran:cost-of-living-2026'
for d in C.values():
    d['sources'] = sorted({k for p in d['points'] for k in p['sources']})

# page map
pm = C['simorgh:page-map']
pm['points'].append(P('جداسازیِ لایه‌ها (۲۴ آبان ۱۴۰۵): روایت‌های تاریخی به ویکی تاریخ رفتند (بخشِ تازهٔ «از صفویه تا قاجار»، ایران و یهودیان، و درس‌های ۱۳۵۷ در مدخلِ انقلاب)؛ نظریه‌های عمومی به ویکی جامعه‌شناسی (خروج و صدا، تغییرِ تحمیل‌شده از بیرون، سرکوبِ دیجیتال، و افزوده به نظریهٔ رضایت و عدالتِ انتقالی)؛ عددهای تاریخ‌دار به لایهٔ ایران. سیمرغ فقط بازی، راهبرد، عمل و خودِ پروژه را نگه می‌دارد و به آن‌ها پیوند می‌دهد.',
                       'Layer separation (15 November 2026): history to the history wiki, general theory to the sociology wiki, dated numbers to the Iran layer; Simorgh keeps game, strategy, action and project and links out.'))
