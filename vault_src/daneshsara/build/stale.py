# -*- coding: utf-8 -*-
"""عددهایی که در متن نوشته شده‌اند ولی با دادهٔ واقعی نمی‌خوانند را پیدا می‌کند.
تا وقتی عددِ متن و عددِ داده یکی نباشد، خواننده نمی‌تواند به بقیهٔ سند اعتماد کند."""
import json, os, re, glob, sys
V = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FA = str.maketrans('0123456789', '۰۱۲۳۴۵۶۷۸۹')
def fa(n): return str(n).translate(FA)

counts = {}
cj = f'{V}/simorgh/par/files/claims-dataset.json'
if os.path.exists(cj): counts['ادعا'] = len(json.load(open(cj, encoding='utf-8')))
pj = f'{V}/simorgh/par/files/problems-dataset.json'
if os.path.exists(pj): counts['مشکل'] = len(json.load(open(pj, encoding='utf-8')))

bad = []
for f in glob.glob(f'{V}/**/*.html', recursive=True):
    rel = os.path.relpath(f, V)
    if rel.startswith(('build/', 'core/panel')): continue
    h = open(f, encoding='utf-8').read()
    # فقط جایی که عدد یعنی «کلِ» ادعاها، نه یک زیرمجموعه
    for word, n in counts.items():
        TOTAL = [r'همهٔ\s*([۰-۹]{1,4})\s*' + word,
                 r'هر\s*([۰-۹]{1,4})\s*' + word,
                 r'([۰-۹]{1,4})\s*' + word + r'(?:ی|يِ|ِ)?\s*میزِ? داده',
                 r'مجموعاً\s*([۰-۹]{1,4})\s*' + word,
                 r'([۰-۹]{1,4})\s*' + word + r'\s*(?:داریم|ثبت شده|در جدول)']
        for pat in TOTAL:
            for m in re.finditer(pat, h):
                if m.group(1) != fa(n):
                    bad.append((rel, m.group(0).strip()[:40], f'{fa(n)} {word}'))
print(f"دادهٔ واقعی: " + '، '.join(f'{fa(v)} {k}' for k, v in counts.items()))
if bad:
    print(f'{len(bad)} عددِ ناهمخوان:')
    for r, got, want in bad[:20]: print(f'  {r}: «{got}» ولی داده می‌گوید {want}')
else:
    print('همهٔ عددهای متن با داده می‌خوانند')
sys.exit(0)
