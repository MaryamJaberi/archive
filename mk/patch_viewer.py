"""Teach a vault viewer to run multi-file pages: inline vault CSS/JS, serve fetch() from the bundle, no duplicate sidebar groups."""
import sys
p = sys.argv[1]; s = open(p, encoding='utf-8').read()
if 'VAULT_FETCH' in s: print('already'); sys.exit()
def rep(a, b):
    global s
    assert a in s, a[:70]; s = s.replace(a, b, 1)
rep('    `window.__VAULT_PAGE=${JSON.stringify(path)};<\\/script>`;',
    '    `window.__VAULT_PAGE=${JSON.stringify(path)};<\\/script>` + VAULT_FETCH;')
rep('  let doc = html;',
    '  let doc = inlineAssets(html, dir);\n  window.__vaultFiles = FILES;')
rep('function render(path) {', r'''/* VAULT_FETCH: صفحه‌های چندفایلی (CSS، JS، داده) از درونِ همین بسته خوانده می‌شوند */
const VAULT_FETCH = `<script>(function(){var R=window.__VAULT_ROOT,F=function(){try{return parent.__vaultFiles}catch(e){return null}},of=window.fetch;
window.fetch=function(u,o){try{var x=new URL(typeof u==="string"?u:u.url,document.baseURI).href;if(x.indexOf(R)===0){var rel=decodeURI(x.slice(R.length)).split("#")[0].split("?")[0],f=F();
if(f&&f[rel]!=null)return Promise.resolve(new Response(f[rel],{status:200,headers:{"Content-Type":/\.json$/.test(rel)?"application/json":"text/plain;charset=utf-8"}}))}}catch(e){}return of.apply(this,arguments)}}())<\/script>`;
function resolveRel(dir, href) {
  if (/^([a-z]+:|\/\/|\/|#|data:)/i.test(href)) return null;
  const parts = (dir + href).split("#")[0].split("?")[0].split("/"), out = [];
  for (const x of parts) { if (x === "..") out.pop(); else if (x !== "." && x !== "") out.push(x); }
  return out.join("/");
}
function inlineAssets(html, dir) {
  html = html.replace(/<link\b[^>]*\bhref="([^"]+\.css)"[^>]*>/gi, (m, h) => {
    const r = resolveRel(dir, h);
    return r && FILES[r] != null && /stylesheet/i.test(m) ? `<style>${FILES[r]}</style>` : m;
  });
  return html.replace(/<script\b([^>]*)\bsrc="([^"]+\.js)"([^>]*)><\/script>/gi, (m, a, h, b) => {
    const r = resolveRel(dir, h);
    return r && FILES[r] != null ? `<script${(a + b).replace(/\b(defer|async)\b/g, "")}>${FILES[r].replace(/<\/script/gi, "<\\/script")}<\/script>` : m;
  });
}

function render(path) {''')
rep('    const items = paths.filter(p => p.startsWith(prefix));',
    '    const items = paths.filter(p => p.startsWith(prefix) && !used.has(p));')
open(p, 'w', encoding='utf-8').write(s); print('patched', p)
