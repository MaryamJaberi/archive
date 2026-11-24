# -*- coding: utf-8 -*-
"""پنل دسترسی را می‌سازد: core/panel.html
داده را همان‌جا داخل صفحه می‌گذارد (مثل بقیهٔ صفحه‌های صندوق؛ صندوق fetch ندارد).
اجرا بعد از build/access.py:  python3 build/panel.py"""
import json, os, datetime
V = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
M = json.load(open(f'{V}/data/access/model.json', encoding='utf-8'))
C = json.load(open(f'{V}/data/access/classify.json', encoding='utf-8'))
rows = [r for r in C['rows'] if not r.get('public')]
FA = '۰۱۲۳۴۵۶۷۸۹'
def fa(n): return str(n).translate(str.maketrans('0123456789', FA))

HTML = """<!doctype html><html lang="fa" dir="rtl"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>پنل دسترسی | صندوق | دانش‌سرا</title>
<style>
:root{--bg:#F7F4EF;--card:#fff;--ink:#1C1915;--ink2:#5c574f;--line:#e3ddd2;--pri:#8a4f0c}
@media(prefers-color-scheme:dark){:root{--bg:#141210;--card:#1e1b18;--ink:#ece7df;--ink2:#b5aea3;--line:#35302a;--pri:#d99a4e}}
*{box-sizing:border-box}
body{margin:0;padding:0 0 3rem;background:var(--bg);color:var(--ink);font-family:Vazirmatn,Tahoma,system-ui,sans-serif;line-height:1.75}
.wrap{max-width:60rem;margin:0 auto;padding-inline:max(14px,env(safe-area-inset-right,0px)) max(14px,env(safe-area-inset-left,0px))}
h1{font-size:1.25rem;margin:1rem 0 .2rem}
.sub{color:var(--ink2);font-size:.85rem;margin:0 0 1rem}
nav{display:flex;gap:.3rem;flex-wrap:wrap;position:sticky;top:0;background:var(--bg);padding:.5rem 0;z-index:5;border-bottom:1px solid var(--line)}
nav button{font:inherit;font-size:.85rem;border:1px solid var(--line);background:var(--card);color:var(--ink);border-radius:99px;padding:.25rem .8rem;cursor:pointer}
nav button[aria-current=true]{background:var(--pri);color:#fff;border-color:var(--pri)}
.card{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:.7rem .9rem;margin:.6rem 0}
.lv{display:inline-block;color:#fff;border-radius:99px;padding:0 .6rem;font-size:.8rem;white-space:nowrap}
.row{display:flex;gap:.5rem;align-items:center;flex-wrap:wrap}
.grow{flex:1 1 12rem;min-width:0}
table{width:100%;border-collapse:collapse;font-size:.85rem}
th,td{text-align:right;padding:.35rem .3rem;border-bottom:1px solid var(--line);vertical-align:top}
th{font-weight:600;color:var(--ink2);font-size:.8rem}
input,select,textarea{font:inherit;background:var(--bg);color:var(--ink);border:1px solid var(--line);border-radius:8px;padding:.25rem .5rem;max-width:100%}
textarea{width:100%;min-height:14rem;font-family:ui-monospace,monospace;font-size:.75rem;direction:ltr;text-align:left}
.b{font:inherit;font-size:.82rem;border:1px solid var(--line);background:var(--bg);color:var(--ink);border-radius:8px;padding:.2rem .7rem;cursor:pointer}
.b.p{background:var(--pri);color:#fff;border-color:var(--pri)}
.mut{color:var(--ink2);font-size:.8rem}
.chk{display:inline-flex;gap:.25rem;align-items:center;font-size:.8rem;margin-inline-end:.6rem}
section[hidden]{display:none}
.bar{height:.5rem;border-radius:99px;background:var(--line);overflow:hidden;display:flex}
.warn{border-inline-start:4px solid #b3261e;padding-inline-start:.7rem}
.ok{color:#2f6b3a}
</style></head><body><div class="wrap">
<h1>پنل دسترسی</h1>
<p class="sub">سطح‌های محرمانگی، رول‌ها، آدم‌ها و اینکه هر صفحه در کدام سطح است. ساخته‌شده از <code>data/access/model.json</code> در __DATE__. تغییرهایت را این‌جا بده و آخرش از برگهٔ «خروجی» بردار و به کلاد بده.</p>
<nav>
<button data-t="levels" aria-current="true">سطح‌ها</button>
<button data-t="roles">رول‌ها</button>
<button data-t="people">آدم‌ها</button>
<button data-t="content">محتوا</button>
<button data-t="out">خروجی</button>
</nav>

<section id="levels"></section>
<section id="roles" hidden></section>
<section id="people" hidden></section>
<section id="content" hidden></section>
<section id="out" hidden>
  <div class="card"><p class="mut">این دو متن را کپی کن و در گفت‌وگو به کلاد بده؛ خودش در صندوق می‌گذارد و بسته‌ها را از نو می‌سازد. تا وقتی این کار نشود، تغییرهایت فقط در همین مرورگر می‌ماند.</p>
  <p class="row"><button class="b p" id="cp1">کپی تنظیمات</button><button class="b" id="cp2">کپی تغییرهای سطح فایل‌ها</button><button class="b" id="rst">برگرد به حالت ذخیره‌شده</button></p>
  <p class="mut">۱. تنظیمات (model.json)</p><textarea id="t1" readonly></textarea>
  <p class="mut">۲. تغییرهای دستی سطح فایل‌ها (overrides.json)</p><textarea id="t2" readonly></textarea></div>
</section>
</div>
<script>
const MODEL=__MODEL__, ROWS=__ROWS__;
const KEY='ds-access-v1';
let S=JSON.parse(localStorage.getItem(KEY)||'null')||{model:structuredClone(MODEL),over:{}};
const save=()=>{try{localStorage.setItem(KEY,JSON.stringify(S))}catch(e){}};
const L=id=>S.model.levels.find(l=>l.id===id)||{fa:'؟',color:'#888'};
const fa=n=>String(n).replace(/[0-9]/g,d=>'۰۱۲۳۴۵۶۷۸۹'[d]);
const esc=s=>String(s??'').replace(/[<>&"]/g,c=>({'<':'&lt;','>':'&gt;','&':'&amp;','"':'&quot;'}[c]));
const lvlOf=p=>{const o=S.over[p];return o?o.level:(ROWS.find(r=>r.path===p)||{}).level};

function levels(){
  const n={};ROWS.forEach(r=>{const l=lvlOf(r.path);n[l]=(n[l]||0)+1});
  const tot=ROWS.length;
  document.getElementById('levels').innerHTML=
  `<div class="card"><div class="bar">`+S.model.levels.map(l=>`<i style="width:${(n[l.id]||0)/tot*100}%;background:${l.color}"></i>`).join('')+`</div></div>`+
  S.model.levels.map(l=>`<div class="card"><div class="row"><span class="lv" style="background:${l.color}">سطح ${fa(l.id)} · ${esc(l.fa)}</span>
  <b>${fa(n[l.id]||0)}</b> <span class="mut">فایل</span></div>
  <p class="mut" style="margin:.3rem 0 0"><b>چه کسی:</b> ${esc(l.who)}</p>
  <p class="mut" style="margin:.1rem 0 0"><b>قاعده:</b> ${esc(l.rule)}</p></div>`).join('')+
  `<div class="card warn"><b>قاعده‌های ایمنی</b><ul class="mut">`+S.model.safety_rules.map(r=>`<li>${esc(r)}</li>`).join('')+`</ul></div>`;
}

function roles(){
  const acts=S.model.actions;
  document.getElementById('roles').innerHTML=S.model.roles.map((r,i)=>`<div class="card">
   <div class="row"><b class="grow">${esc(r.fa)}</b><span class="mut">${esc(r.key)}</span>
   ${r.key==='owner'?'':`<button class="b" data-del="${i}">حذف رول</button>`}</div>
   <p class="mut" style="margin:.2rem 0">${esc(r.note||'')}</p>
   <p style="margin:.3rem 0"><span class="mut">تا کدام سطح می‌بیند:</span><br>`+
   S.model.levels.map(l=>`<label class="chk"><input type="checkbox" data-r="${i}" data-lv="${l.id}" ${r.levels.includes(l.id)?'checked':''}>
     <span class="lv" style="background:${l.color}">${fa(l.id)}</span> ${esc(l.fa)}</label>`).join('')+`</p>
   <p style="margin:.3rem 0"><span class="mut">چه کاری می‌تواند بکند:</span><br>`+
   acts.map(a=>`<label class="chk"><input type="checkbox" data-r="${i}" data-ac="${a.key}" ${r.actions.includes(a.key)?'checked':''}> ${esc(a.fa)}</label>`).join('')+`</p>
   <p class="mut">حوزه‌ها: ${r.areas==='*'?'همه':r.areas.map(a=>esc((S.model.areas.find(x=>x.key===a)||{}).fa||a)).join('، ')}</p>
  </div>`).join('')+
  `<div class="card"><div class="row"><input id="nr" class="grow" placeholder="نام رول تازه، مثل: مترجم"><button class="b p" id="addr">افزودن رول</button></div></div>`;
  document.querySelectorAll('[data-lv]').forEach(c=>c.onchange=e=>{
    const r=S.model.roles[+e.target.dataset.r], v=+e.target.dataset.lv;
    r.levels=e.target.checked?[...new Set([...r.levels,v])].sort():r.levels.filter(x=>x!==v);save();roles()});
  document.querySelectorAll('[data-ac]').forEach(c=>c.onchange=e=>{
    const r=S.model.roles[+e.target.dataset.r], v=e.target.dataset.ac;
    r.actions=e.target.checked?[...new Set([...r.actions,v])]:r.actions.filter(x=>x!==v);save();roles()});
  document.querySelectorAll('[data-del]').forEach(b=>b.onclick=e=>{
    S.model.roles.splice(+e.target.dataset.del,1);save();roles();people()});
  document.getElementById('addr').onclick=()=>{
    const v=document.getElementById('nr').value.trim();if(!v)return;
    S.model.roles.push({key:'r'+Date.now().toString(36),fa:v,levels:[0],actions:['read'],areas:'*',note:''});save();roles();people()};
}

function people(){
  const opts=S.model.roles.map(r=>`<option value="${r.key}">${esc(r.fa)}</option>`).join('');
  document.getElementById('people').innerHTML=`<div class="card"><p class="mut">نام واقعی و ایمیل این‌جا نوشته نمی‌شود. فقط برچسبی که معنایش را خودت می‌دانی.</p>
  <table><thead><tr><th>برچسب</th><th>رول</th><th>وضعیت</th><th></th></tr></thead><tbody>`+
  S.model.people.map((p,i)=>`<tr><td><input value="${esc(p.label)}" data-p="${i}" data-f="label" style="width:7rem"></td>
   <td><select data-p="${i}" data-f="role">${opts}</select></td>
   <td><select data-p="${i}" data-f="status"><option value="active">فعال</option><option value="paused">موقتاً بسته</option><option value="revoked">لغو شده</option></select></td>
   <td>${p.role==='owner'?'':`<button class="b" data-pd="${i}">حذف</button>`}</td></tr>`).join('')+
  `</tbody></table><div class="row" style="margin-top:.5rem"><input id="np" class="grow" placeholder="برچسب آدم تازه، مثل: همکار سرور">
   <button class="b p" id="addp">افزودن</button></div></div>`;
  S.model.people.forEach((p,i)=>{
    const q=f=>document.querySelector(`[data-p="${i}"][data-f="${f}"]`);
    q('role').value=p.role;q('status').value=p.status||'active';});
  document.querySelectorAll('[data-p]').forEach(el=>el.onchange=e=>{
    S.model.people[+e.target.dataset.p][e.target.dataset.f]=e.target.value;save();});
  document.querySelectorAll('[data-pd]').forEach(b=>b.onclick=e=>{
    S.model.people.splice(+e.target.dataset.pd,1);save();people()});
  document.getElementById('addp').onclick=()=>{
    const v=document.getElementById('np').value.trim();if(!v)return;
    S.model.people.push({id:'p'+Date.now().toString(36),label:v,role:'guest',note:'',status:'active'});save();people()};
}

function content(){
  const q=(document.getElementById('q')||{}).value||'', f=(document.getElementById('flv')||{}).value||'';
  const list=ROWS.filter(r=>(!q||r.path.includes(q)||(r.title||'').includes(q))&&(f===''||String(lvlOf(r.path))===f));
  document.getElementById('content').innerHTML=`<div class="card"><div class="row">
   <input id="q" class="grow" placeholder="جستجو در مسیر یا عنوان" value="${esc(q)}">
   <select id="flv"><option value="">همهٔ سطح‌ها</option>`+S.model.levels.map(l=>`<option value="${l.id}">سطح ${fa(l.id)} · ${esc(l.fa)}</option>`).join('')+
   `</select></div><p class="mut">${fa(list.length)} از ${fa(ROWS.length)} فایل. سطح هر فایل را می‌توانی عوض کنی؛ تغییرها در برگهٔ «خروجی» جمع می‌شوند.</p>
   <table><thead><tr><th>سطح</th><th>فایل</th><th>چرا</th></tr></thead><tbody>`+
   list.slice(0,400).map(r=>{const lv=lvlOf(r.path),l=L(lv),ch=!!S.over[r.path];
    return `<tr><td><select data-c="${esc(r.path)}" style="background:${l.color};color:#fff;border:0">`+
    S.model.levels.map(x=>`<option value="${x.id}" ${x.id===lv?'selected':''}>${fa(x.id)} ${esc(x.fa)}</option>`).join('')+
    `</select></td><td>${esc(r.title||'')}<br><span class="mut" style="direction:ltr;display:inline-block">${esc(r.path)}</span></td>
    <td class="mut">${ch?'<b>عوض کردی</b>':esc(r.why)}</td></tr>`}).join('')+
   `</tbody></table>${list.length>400?'<p class="mut">فقط ۴۰۰ ردیف اول نشان داده شد؛ جستجو کن.</p>':''}</div>`;
  document.getElementById('q').oninput=content;document.getElementById('flv').onchange=content;
  document.getElementById('flv').value=f;
  document.querySelectorAll('[data-c]').forEach(s=>s.onchange=e=>{
    const p=e.target.dataset.c,v=+e.target.value,base=(ROWS.find(r=>r.path===p)||{}).level;
    if(v===base)delete S.over[p];else S.over[p]={level:v,area:(ROWS.find(r=>r.path===p)||{}).area,why:'دستیِ خودم در پنل'};
    save();content();levels()});
}

function out(){
  document.getElementById('t1').value=JSON.stringify(S.model,null,1);
  document.getElementById('t2').value=JSON.stringify(S.over,null,1);
  const cp=(id)=>{const t=document.getElementById(id);t.removeAttribute('readonly');t.select();
    try{navigator.clipboard.writeText(t.value)}catch(e){document.execCommand&&document.execCommand('copy')}
    t.setAttribute('readonly','')};
  document.getElementById('cp1').onclick=()=>cp('t1');
  document.getElementById('cp2').onclick=()=>cp('t2');
  document.getElementById('rst').onclick=()=>{localStorage.removeItem(KEY);S={model:structuredClone(MODEL),over:{}};levels();roles();people();content();out()};
}

document.querySelectorAll('nav button').forEach(b=>b.onclick=()=>{
  document.querySelectorAll('nav button').forEach(x=>x.setAttribute('aria-current',x===b));
  ['levels','roles','people','content','out'].forEach(id=>document.getElementById(id).hidden=(id!==b.dataset.t));
  if(b.dataset.t==='out')out();if(b.dataset.t==='content')content();});
levels();roles();people();content();
</script></body></html>"""

slim = [{'path': r['path'], 'level': r['level'], 'area': r['area'], 'why': r['why'], 'title': r['title']} for r in rows]
html = (HTML.replace('__MODEL__', json.dumps(M, ensure_ascii=False))
            .replace('__ROWS__', json.dumps(slim, ensure_ascii=False))
            .replace('__DATE__', datetime.date.today().isoformat()))
open(f'{V}/core/panel.html', 'w', encoding='utf-8').write(html)
print('core/panel.html ساخته شد |', len(rows), 'فایل |', len(M['roles']), 'رول')
