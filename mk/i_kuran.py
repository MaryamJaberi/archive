"""Pass 7: Kuran (1995) chapter 4 applied to the game. The theory itself lives in soc:preference-falsification."""
from common import *
from d_review import addp, addl, N

KU = src('Kuran, Timur (1995)')

addp('three-feathers', P(
 'از کوران (فصل ۴): پَرِ یکم با «عددِ واقعی» نمی‌سوزد، با «انتظار» می‌سوزد. هر دو طرف می‌کوشند خود را اکثریت نشان دهند، پس عددی که از یک طرف می‌آید باور نمی‌شود. برای همین نهادِ داده باید بی‌طرفیِ دیدنی داشته باشد و هرگز عدد را بزرگ نکند؛ یک بار گزافه‌گویی کافی است تا پَر خیس شود. و چون آدم‌ها به روایتِ ملموس بیش از آمار وزن می‌دهند، هر عدد با یک تصویرِ ساده همراه شود (بی‌آنکه کسی را به خطر بیندازد).',
 'From Kuran ch. 4: feather one burns through expectations, not the true number. Both sides claim to be the majority, so a number from one side is not believed; the data body must be visibly neutral and never inflate. People weigh vivid stories over statistics, so pair each number with a simple image.', [KU], True))

addp('game-rules-v2', P(
 'افزوده از کوران (بازیِ انتظار): در اعلامِ روز، مافیا می‌تواند کارتِ «عددسازی» بازی کند: جمعِ اعلام‌شده دو واحد کمتر از واقعی گفته می‌شود. کارتِ آمار این را خنثی می‌کند. اگر شهر خودش عدد را بزرگ اعلام کند و بعد لو برود، کارتِ آمارش تا پایانِ بازی بی‌اثر می‌شود. درس: در جنگِ انتظار، اعتبار تنها سرمایه است.',
 'Added from Kuran (expectations game): the Mafia may play a "fake count" card lowering the announced total by two; the statistics card cancels it. If the city inflates its own count and is exposed, its statistics card is void for the rest of the game.', [KU]), at=4)

addp('pre-mortem', P(
 'حالتِ ۱۱، موجِ وارونه (از کوران): پس از سرکوبی بزرگ، اگر به نظر برسد حکومت می‌ماند، مشارکت در چند هفته فرو می‌ریزد، چنان‌که در هندِ ۱۹۷۵ پس از وضعِ اضطراری. نشانه: کم‌شدنِ ناگهانیِ نشانه‌های کم‌هزینه (نه فقط خیابان). حفاظ: نشانه‌های کم‌خطری که همیشه در دسترس‌اند و انتظار را زنده نگه می‌دارند، و عددِ مستقلِ منظم که نشان دهد ترجیحِ درونی عوض نشده است.',
 'Mode 11, the reverse bandwagon (Kuran): after a major crackdown, if the regime seems set to survive, participation collapses within weeks, as in India 1975. Safeguard: always-available low-risk signals and regular independent numbers showing private preferences have not changed.', [KU], True))

addp('why-not-january', P(
 'از کوران: سرکوبِ دی ۱۴۰۴ فقط کسانی را که گرفت ساکت نکرد؛ انتظارِ بقیه را عوض کرد. این همان «موجِ وارونه» است که کوران در هندِ ۱۹۷۵ نشان می‌دهد، و قطعِ ۸۸روزهٔ اینترنت راهِ دیدنِ اینکه «دیگران هنوز هستند» را هم بست. ترجیحِ درونی اما در پیمایشِ شش ماه بعد عوض نشده بود؛ یعنی تعادل جابه‌جا نشد، فقط پنهان شد.',
 'From Kuran: the January 2026 crackdown changed everyone else\'s expectations, the reverse bandwagon Kuran shows for India 1975, and the 88-day shutdown removed the means of seeing that others were still there. Private preferences had not changed six months later; the equilibrium hid rather than moved.', [KU, N['gam']], True))

addp('threshold-indicators', P(
 'از کوران: نشانگری که بیشتر از همه معنا دارد «انتظار» است، نه فقط «ترجیح»: پرسشِ «فکر می‌کنید چند درصدِ مردم با شما هم‌نظرند؟» در کنارِ «شما چه فکر می‌کنید؟». فاصلهٔ این دو اندازهٔ نادانیِ جمعی است؛ هر چه کوچک‌تر شود، آستانه نزدیک‌تر است.',
 'From Kuran: the most meaningful indicator is expectation, not only preference: ask "what share agree with you?" beside "what do you think?". The gap measures pluralistic ignorance; as it shrinks, the threshold nears.', [KU], True))

for s in ['three-feathers', 'game-rules-v2', 'threshold-indicators']:
    addl(s, L('soc:preference-falsification', 'نظریه: تحریفِ ترجیحات (کوران)', 'Theory: preference falsification'))
