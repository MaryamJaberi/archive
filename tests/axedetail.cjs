const {chromium}=require('playwright');const fs=require('fs');const http=require('http'),path=require('path');
const AXE=fs.readFileSync(require.resolve('axe-core/axe.min.js'),'utf8');const ROOT='/home/claude/maryamjaberi.github.io';
const T={'.html':'text/html; charset=utf-8','.js':'text/javascript','.css':'text/css','.json':'application/json','.svg':'image/svg+xml','.woff2':'font/woff2'};
const srv=http.createServer((q,s)=>{let f=path.join(ROOT,decodeURIComponent(q.url.split('?')[0]));if(fs.existsSync(f)&&fs.statSync(f).isDirectory())f=path.join(f,'index.html');if(!fs.existsSync(f)){s.writeHead(404);return s.end()}s.writeHead(200,{'Content-Type':T[path.extname(f)]||'application/octet-stream'});fs.createReadStream(f).pipe(s)}).listen(8793);
(async()=>{const b=await chromium.launch();const agg={};
for(const u of process.argv.slice(2)){for(const scheme of ['light','dark']){const p=await b.newPage({viewport:{width:1300,height:850},colorScheme:scheme});await p.route(/^https?:\/\/(?!localhost)/,r=>r.abort());
await p.goto('http://localhost:8793/'+u,{waitUntil:'load'});await p.waitForTimeout(500);await p.addScriptTag({content:AXE});
const r=await p.evaluate(async()=>{const res=await axe.run(document,{runOnly:['color-contrast']});return res.violations.flatMap(v=>v.nodes.map(n=>{const d=n.any[0]&&n.any[0].data||{};return (d.fgColor+' on '+d.bgColor+' ratio '+d.contrastRatio+' need '+d.expectedContrastRatio+' | '+n.target.join(' ').slice(-50))}))});
for(const x of r){const k=scheme+' '+x.split(' | ')[0];agg[k]=agg[k]||{n:0,ex:x.split(' | ')[1],pages:new Set()};agg[k].n++;agg[k].pages.add(u)}await p.close()}}
const L=Object.entries(agg).sort((a,b)=>b[1].n-a[1].n).slice(0,25);for(const [k,v] of L)console.log(v.n,k,'e.g.',v.ex,[...v.pages].slice(0,3).join(','));await b.close();srv.close()})();
