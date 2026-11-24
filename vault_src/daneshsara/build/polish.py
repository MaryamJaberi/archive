# -*- coding: utf-8 -*-
"""صفحه‌های صندوق را مفهوم‌تر و کاربردی‌تر می‌کند، بدون دست‌زدن به متن خودِ صفحه:
۱. «در این صفحه»: فهرست سرفصل‌ها برای صفحه‌های بلند
۲. «بعد از این»: دو سه راه به صفحه‌های مربوط، تا هیچ صفحه‌ای بن‌بست نباشد
۳. تاریخ آخرین بررسی، تا معلوم باشد چقدر کهنه است
همهٔ بلوک‌ها نشان‌دار (data-ds) هستند و هر بار از نو ساخته می‌شوند."""
import json, os, re, hashlib, datetime
V = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NAV = json.load(open(f'{V}/core/nav.json', encoding='utf-8'))
TODAY = datetime.date.today().isoformat()
DP = f'{V}/data/access/dates.json'
DATES = json.load(open(DP, encoding='utf-8')) if os.path.exists(DP) else {}

# رنگ‌ها از خودِ صفحه گرفته می‌شوند تا روی صفحه‌های تیره و روشن یکسان بنشینند
CSS = ('font:inherit;margin:2.2rem 0 0;padding:1rem 1.1rem;border-radius:12px;line-height:1.9;'
       'border:1px solid color-mix(in srgb, currentColor 26%, transparent);'
       'background:color-mix(in srgb, currentColor 6%, transparent)')
LINK = ('color:inherit;text-decoration:none;'
        'border-bottom:1px solid color-mix(in srgb, currentColor 45%, transparent)')

def rel(frm, to):
    r = os.path.relpath(to, os.path.dirname(frm))
    return r.replace(os.sep, '/')

def unwrap_tables(h):
    """بسته‌بندی قبلی جدول‌ها را باز می‌کند تا هر بار از نو ساخته شود."""
    return re.sub(r'(?s)<div data-ds="scroll"[^>]*>(\s*<table\b.*?</table>\s*)</div>', r'\1', h)

def wrap_tables(h):
    """جدول پهن روی گوشی صفحه را کج نکند: خودش بلغزد."""
    return re.sub(r'(?s)(<table\b.*?</table>)',
                  r'<div data-ds="scroll" style="overflow-x:auto;max-width:100%">\1</div>', h)

def clean(h):
    return re.sub(r'(?s)<(?:nav|aside|div|p|style)[^>]*data-ds="[^"]*"[^>]*>.*?</(?:nav|aside|div|p|style)>', '', h)

FIX = ('<style data-ds="fix">:where(p,li,td,th,dd,dt,figcaption,blockquote,code,a,h1,h2,h3)'
       '{overflow-wrap:break-word}:where(img,svg,video,iframe){max-width:100%}</style>')

def add_fix(h):
    """نشانی‌های بلند و تصویرهای پهن صفحه را روی گوشی کج نکنند."""
    if re.search(r'(?i)</head>', h):
        return re.sub(r'(?i)</head>', FIX + '</head>', h, count=1)
    return FIX + h

def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

def has_own_nav(h):
    """صفحه‌ای که خودش فهرست لنگری دارد، فهرست دوم نمی‌خواهد."""
    body = re.sub(r'(?is)<(script|style)[^>]*>.*?</\1>', ' ', h)
    for m in re.finditer(r'(?is)<(nav|div|ul|ol|p|section)[^>]*>(.{0,3000}?)</\1>', body):
        if len(re.findall(r'href="#[^"]+"', m.group(2))) >= 3: return True
    return False

def toc(h, path):
    if has_own_nav(h): return h, False
    hs = re.findall(r'(?is)<h2\b([^>]*)>(.*?)</h2>', h)
    if len(hs) < 3: return h, False
    items, n = [], 0
    def txt(x): return re.sub(r'\s+', ' ', re.sub(r'(?s)<[^>]+>', '', x)).strip()
    new = h
    for attrs, inner in hs:
        t = txt(inner)
        if not t: continue
        m = re.search(r'id="([^"]+)"', attrs)
        if m: hid = m.group(1)
        else:
            n += 1; hid = f'ds-s{n}'
            new = new.replace(f'<h2{attrs}>{inner}</h2>', f'<h2{attrs} id="{hid}">{inner}</h2>', 1)
        items.append((hid, t))
    if len(items) < 3: return h, False
    lis = ' · '.join(f'<a href="#{i}" style="{LINK}">{esc(t)}</a>' for i, t in items[:14])
    block = (f'<nav data-ds="toc" style="{CSS};margin:1.2rem 0 1.6rem">'
             f'<b>در این صفحه</b><br>{lis}</nav>')
    # پیش از نخستین h2 بنشیند، نه وسط سرصفحهٔ طراحی‌شده
    m = re.search(r'(?is)<h2\b', new)
    if not m:
        m = re.search(r'(?is)</h1>', new)
        if not m: return new, False
        return new[:m.end()] + block + new[m.end():], True
    return new[:m.start()] + block + new[m.start():], True

def main():
    secs = NAV['sections']
    pos = {}
    for s in secs:
        for i, it in enumerate(s['items']): pos[it['path']] = (s, i)
    changed = tocs = 0
    for s in secs:
        items = s['items']
        for i, it in enumerate(items):
            p = it['path']
            f = os.path.join(V, p)
            if not os.path.exists(f): continue
            h = clean(unwrap_tables(open(f, encoding='utf-8').read()))
            core = re.sub(r'\s+', ' ', h)
            dg = hashlib.sha256(core.encode()).hexdigest()[:16]
            d = DATES.get(p)
            if not d or d.get('hash') != dg:
                DATES[p] = {'hash': dg, 'checked': TODAY}
            when = DATES[p]['checked']

            h = add_fix(wrap_tables(h))
            h, did = toc(h, p)
            tocs += did

            nxt = []
            if i + 1 < len(items): nxt.append((items[i + 1], 'بعدی در همین بخش'))
            if i > 0:              nxt.append((items[i - 1], 'قبلی'))
            if items[0]['path'] != p and (i + 1 >= len(items) or i == 0):
                nxt.append((items[0], 'اول این بخش'))
            links = ' '.join(
                f'<a href="{rel(p, t["path"])}" style="{LINK}">{esc(t["label"] or t["path"])}</a> '
                f'<span style="opacity:.6">({lab})</span>' for t, lab in nxt[:3])
            blk = (f'<nav data-ds="after" style="{CSS}">'
                   f'<b>بعد از این</b><br>{links or "<span style=\'opacity:.6\'>تنها صفحهٔ این بخش است</span>"}'
                   f'<br><span style="opacity:.6;font-size:.85em">بخش: {esc(s["title"])} · آخرین بررسی: {when}</span>'
                   f'</nav>')
            h = re.sub(r'(?is)</body>', blk + '</body>', h, count=1) if '</body>' in h.lower() else h + blk
            open(f, 'w', encoding='utf-8').write(h)
            changed += 1
    json.dump(DATES, open(DP, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    print(f'{changed} صفحه پالوده شد؛ {tocs} فهرستِ «در این صفحه» ساخته شد')

main()
