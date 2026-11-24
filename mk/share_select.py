# -*- coding: utf-8 -*-
"""فایل‌های بستهٔ اشتراکی را بر اساس سطح محرمانگی انتخاب می‌کند و یک صفحهٔ ورودی ساده می‌سازد."""
import json, os, shutil, sys, re
SRC, DST = sys.argv[1], sys.argv[2]
M = json.load(open(f'{SRC}/data/access/model.json', encoding='utf-8'))
C = json.load(open(f'{SRC}/data/access/classify.json', encoding='utf-8'))
guest = next(r for r in M['roles'] if r['key'] == 'guest')
MAX = max(guest['levels'])
over = {}
op = f'{SRC}/data/access/overrides.json'
if os.path.exists(op): over = json.load(open(op, encoding='utf-8'))
lvl = {r['path']: over.get(r['path'], r)['level'] for r in C['rows'] if not r.get('public')}
n = 0
for rel, l in sorted(lvl.items()):
    if l > MAX or rel.startswith(('build/', 'data/access/')): continue
    d = os.path.join(DST, rel); os.makedirs(os.path.dirname(d), exist_ok=True)
    shutil.copy2(os.path.join(SRC, rel), d); n += 1
# صفحهٔ ورودی: بیننده با simorgh/index.html شروع می‌کند
pages = []
for rel, l in sorted(lvl.items()):
    if l <= MAX and rel.startswith('simorgh/par/') and rel.endswith('.html') and '/en/' not in rel and '/old/' not in rel:
        t = re.search(r'<title>(.*?)</title>', open(os.path.join(SRC, rel), encoding='utf-8').read(), re.S)
        pages.append((rel[len('simorgh/'):], (t.group(1).split('—')[0].split('|')[0].strip() if t else rel)))
os.makedirs(f'{DST}/simorgh', exist_ok=True)
open(f'{DST}/simorgh/index.html', 'w', encoding='utf-8').write(
 '<!doctype html><html lang="fa" dir="rtl"><head><meta charset="utf-8">'
 '<meta name="viewport" content="width=device-width,initial-scale=1"><title>پَرِ سیمرغ</title><style>'
 'body{margin:0;padding:18px;background:#F7F4EF;color:#1C1915;font-family:Vazirmatn,Tahoma,sans-serif;line-height:1.8}'
 'h1{font-size:1.2rem}a{display:block;background:#fff;border:1px solid #e3ddd2;border-radius:10px;'
 'padding:.5rem .8rem;margin:.4rem 0;color:#1C1915;text-decoration:none}'
 '@media(prefers-color-scheme:dark){body{background:#141210;color:#ece7df}a{background:#1e1b18;border-color:#35302a;color:#ece7df}}'
 '</style></head><body><h1>پَرِ سیمرغ</h1><p>تحلیل و بازی. نسخهٔ اشتراکی.</p>'
 + ''.join(f'<a href="{h}">{t}</a>' for h, t in pages) + '</body></html>')
print(f'{n} فایل تا سطح {MAX} انتخاب شد؛ {len(pages)} صفحه در فهرست')
