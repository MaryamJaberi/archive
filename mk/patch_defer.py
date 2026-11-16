import sys
p=sys.argv[1]; s=open(p,encoding='utf-8').read()
if 'DEFERRED' in s: print('already'); sys.exit()
old='''  return html.replace(/<script\\b([^>]*)\\bsrc="([^"]+\\.js)"([^>]*)><\\/script>/gi, (m, a, h, b) => {
    const r = resolveRel(dir, h);
    return r && FILES[r] != null ? `<script${(a + b).replace(/\\b(defer|async)\\b/g, "")}>${FILES[r].replace(/<\\/script/gi, "<\\\\/script")}<\\/script>` : m;
  });'''
new='''  const DEFERRED = [];
  html = html.replace(/<script\\b([^>]*)\\bsrc="([^"]+\\.js)"([^>]*)><\\/script>/gi, (m, a, h, b) => {
    const r = resolveRel(dir, h);
    if (!(r && FILES[r] != null)) return m;
    const tag = `<script${(a + b).replace(/\\b(defer|async)\\b/g, "")}>${FILES[r].replace(/<\\/script/gi, "<\\\\/script")}<\\/script>`;
    if (/\\bdefer\\b/.test(a + b)) { DEFERRED.push(tag); return ""; }
    return tag;
  });
  if (!DEFERRED.length) return html;
  return /<\\/body>/i.test(html) ? html.replace(/<\\/body>(?![\\s\\S]*<\\/body>)/i, DEFERRED.join("") + "</body>") : html + DEFERRED.join("");'''
assert old in s, 'pattern'
s=s.replace(old,new,1); open(p,'w',encoding='utf-8').write(s); print('ok',p)
