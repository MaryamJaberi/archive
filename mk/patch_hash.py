import sys
p=sys.argv[1]; s=open(p,encoding='utf-8').read()
if 'WANT_HASH' in s: print('already'); sys.exit()
a='  $("view").srcdoc = doc;'
b='''  const v = $("view"); v.onload = () => { try { const h = WANT_HASH; WANT_HASH = ""; if (h) { const el = v.contentDocument.getElementById(decodeURIComponent(h)); if (el) el.scrollIntoView(); } } catch (e) {} };
  v.srcdoc = doc;'''
assert a in s; s=s.replace(a,b,1)
a='  if (typeof p === "string") render(p.split("#")[0]);'
b='  if (typeof p === "string") { WANT_HASH = p.split("#")[1] || ""; render(p.split("#")[0]); }'
assert a in s; s=s.replace(a,b,1)
a='function render(path) {'
s=s.replace(a,'let WANT_HASH = "";\n'+a,1)
# initial location.hash like "simorgh/par/game.html#tarikh"
open(p,'w',encoding='utf-8').write(s); print('ok',p)
