# -*- coding: utf-8 -*-
"""هر صفحهٔ صندوق را از دو نظر می‌سنجد: مفهوم بودن و کاربردی بودن.
مفهوم: آیا بالای صفحه در یک جمله می‌گوید این چیست؟ سرفصل دارد؟ خیلی بلند نیست؟
کاربردی: آیا راهی به جای دیگر دارد؟ آیا کسی به آن لینک داده؟ آیا تاریخ دارد؟"""
import json, os, re, collections, sys
V = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NAV = json.load(open(f'{V}/core/nav.json', encoding='utf-8'))
pages = [(s['title'], it['path'], it['label']) for s in NAV['sections'] for it in s['items']]
P = {p for _, p, _ in pages}

def strip(h):
    h = re.sub(r'(?is)<(script|style|svg)[^>]*>.*?</\1>', ' ', h)
    return re.sub(r'\s+', ' ', re.sub(r'(?s)<[^>]+>', ' ', h)).strip()

inbound = collections.Counter()
rows = []
for sec, p, label in pages:
    h = open(os.path.join(V, p), encoding='utf-8').read()
    # برای پیداکردن جملهٔ معرفی، بلوک‌های افزودهٔ خودمان را نادیده بگیر
    hraw = re.sub(r'(?s)<(?:nav|aside|div|p)[^>]*data-ds="[^"]*"[^>]*>.*?</(?:nav|aside|div|p)>', '', h)
    d = os.path.dirname(p)
    links = re.findall(r'href="([^"#?][^"]*\.html)[^"]*"', h)
    out = set()
    for l in links:
        q = os.path.normpath(os.path.join(d, l)) if not l.startswith('/') else l.lstrip('/')
        if q in P and q != p: out.add(q)
    for q in out: inbound[q] += 1
    body = strip(h)
    # جملهٔ معرفی: اولین پاراگراف بعد از h1
    m = re.search(r'(?is)</h1>(.{0,1500}?)<p[^>]*>(.*?)</p>', hraw)
    lead = strip(m.group(2)) if m else ''
    rows.append({'sec': sec, 'path': p, 'label': label,
                 'words': len(body.split()),
                 'h1': len(re.findall(r'<h1', h)), 'h2': len(re.findall(r'<h2', h)),
                 'lead': lead, 'leadlen': len(lead), 'out': len(out),
                 'toc': 'data-ds="toc"' in h,
                 'filter': bool(re.search(r'type="search"|placeholder="[^"]*جستجو|oninput|addEventListener\("input"', h)),
                 'i18n': bool(re.search(r'<p[^>]*data-i="lead"', hraw)),
                 'date': bool(re.search(r'۱۴۰[۰-۹]|۲۰۲[۰-۹]|202[0-9]', body))})
for r in rows: r['in'] = inbound[r['path']]

DECK = {'simorgh/par/europe.html', 'simorgh/par/eraee-rahbordi.html'}

def flags(r):
    if r['path'] in DECK or r['i18n']: return []
    f = []
    if r['leadlen'] < 40:   f.append('بی‌جملهٔ معرفی')
    elif r['leadlen'] > 400: f.append('معرفیِ خیلی بلند')
    if r['h1'] != 1:        f.append(f"h1={r['h1']}")
    if r['words'] > 400 and r['h2'] < 2: f.append('بدون سرفصل')
    if r['out'] == 0:       f.append('بن‌بست (لینک به بیرون ندارد)')
    if r['in'] == 0:        f.append('یتیم (کسی لینکش نداده)')
    # صفحه‌ای که جستجو یا فیلتر دارد، راه بهترِ پیمایش دارد و به فهرست نیاز ندارد
    if r['words'] > 4000 and not r['toc'] and not r['filter']: f.append('خیلی بلند، بدون فهرست')
    if not r['date']:       f.append('بدون تاریخ')
    return f

for r in rows: r['flags'] = flags(r)
json.dump(rows, open(f'{V}/data/access/pagecheck.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
c = collections.Counter(f for r in rows for f in r['flags'])
print(len(rows), 'صفحه بررسی شد. پرتکرارترین ایرادها:')
for k, v in c.most_common(): print(f'  {v:>3}  {k}')
bad = sorted(rows, key=lambda r: -len(r['flags']))
print('\nبدترین‌ها:')
for r in bad[:14]: print(f"  {len(r['flags'])}  {r['label'] or r['path']:<26} {r['sec'][:18]:<20} {'، '.join(r['flags'])}")
