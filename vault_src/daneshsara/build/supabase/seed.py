# -*- coding: utf-8 -*-
"""از model.json و classify.json دستورهای INSERT می‌سازد تا پایگاه‌داده پر شود.
سطح ۴ را عمداً بیرون می‌گذارد: نه محتوایش، نه نام فایل‌هایش.
اجرا: python3 build/supabase/seed.py > /tmp/seed.sql"""
import json, os, sys
V = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
M = json.load(open(f'{V}/data/access/model.json', encoding='utf-8'))
C = json.load(open(f'{V}/data/access/classify.json', encoding='utf-8'))
op = f'{V}/data/access/overrides.json'
over = json.load(open(op, encoding='utf-8')) if os.path.exists(op) else {}
q = lambda s: "'" + str(s).replace("'", "''") + "'"
arr = lambda xs, t: "'{" + ','.join(f'"{x}"' if t == 'text' else str(x) for x in xs) + "}'::" + t + '[]'
out = ['begin;']
for l in M['levels']:
    out.append(f"insert into access.levels(id,key,fa,who,rule,color) values({l['id']},{q(l['key'])},{q(l['fa'])},{q(l['who'])},{q(l['rule'])},{q(l['color'])}) on conflict(id) do update set fa=excluded.fa,who=excluded.who,rule=excluded.rule,color=excluded.color;")
for a in M['areas']:
    out.append(f"insert into access.areas(key,fa) values({q(a['key'])},{q(a['fa'])}) on conflict(key) do update set fa=excluded.fa;")
for a in M['actions']:
    out.append(f"insert into access.actions(key,fa,note) values({q(a['key'])},{q(a['fa'])},{q(a.get('note',''))}) on conflict(key) do update set fa=excluded.fa,note=excluded.note;")
for r in M['roles']:
    areas = 'null' if r['areas'] == '*' else arr(r['areas'], 'text')
    out.append(f"insert into access.roles(key,fa,note,levels,actions,areas) values({q(r['key'])},{q(r['fa'])},{q(r.get('note',''))},{arr(r['levels'],'int')},{arr(r['actions'],'text')},{areas}) on conflict(key) do update set fa=excluded.fa,note=excluded.note,levels=excluded.levels,actions=excluded.actions,areas=excluded.areas;")
for p in M['people']:
    out.append(f"insert into access.people(label,role_key,status,note) select {q(p['label'])},{q(p['role'])},{q(p.get('status','active'))},{q(p.get('note',''))} where not exists(select 1 from access.people where label={q(p['label'])});")
n = 0
for r in C['rows']:
    if r.get('public'): continue
    lv = over.get(r['path'], r)['level']
    if lv > 3: continue          # سطح ۴ روی سرور نمی‌رود
    out.append(f"insert into access.content(path,level,area,title,why,manual) values({q(r['path'])},{lv},{q(r['area']) if r['area']!='—' else 'null'},{q(r['title'])},{q(r['why'])},{str(r['path'] in over).lower()}) on conflict(path) do update set level=excluded.level,area=excluded.area,title=excluded.title,why=excluded.why,manual=excluded.manual,updated_at=now();")
    n += 1
out.append('commit;')
sys.stderr.write(f'{n} مسیر تا سطح ۳ آمادهٔ فرستادن؛ سطح ۴ کنار گذاشته شد\n')
print('\n'.join(out))
