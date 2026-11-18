const {chromium}=require('playwright');const http=require('http'),fs=require('fs'),path=require('path');
const ROOT='/home/claude/maryamjaberi.github.io';
const T={'.html':'text/html; charset=utf-8','.js':'text/javascript','.css':'text/css','.json':'application/json','.svg':'image/svg+xml','.png':'image/png','.jpg':'image/jpeg','.webp':'image/webp','.woff2':'font/woff2','.mp3':'audio/mpeg','.webmanifest':'application/manifest+json'};
const srv=http.createServer((q,s)=>{let f=path.join(ROOT,decodeURIComponent(q.url.split('?')[0]));if(fs.existsSync(f)&&fs.statSync(f).isDirectory())f=path.join(f,'index.html');if(!fs.existsSync(f)){s.writeHead(404);return s.end()}s.writeHead(200,{'Content-Type':T[path.extname(f)]||'application/octet-stream'});fs.createReadStream(f).pipe(s)}).listen(8791);
(async()=>{const b=await chromium.launch();
for(const a of process.argv.slice(2)){const p=await b.newPage({viewport:{width:1300,height:850}});const errs=[];p.on('pageerror',e=>errs.push(e.message.slice(0,120)));
await p.goto('http://localhost:8791/'+a,{waitUntil:'load'}).catch(e=>errs.push(String(e).slice(0,100)));await p.waitForTimeout(2500);
const btn=await p.$$eval('button,[role=button],a.btn,input[type=submit]',x=>x.filter(e=>e.offsetParent).map(e=>(e.innerText||e.value||e.getAttribute('aria-label')||'').trim().slice(0,30)).filter(Boolean).slice(0,25));
const n=a.replace(/\W+/g,'_');await p.screenshot({path:`peek_${n}.png`});console.log(a,'| title:',await p.title(),'| errs:',errs.join(' / '),'\n  buttons:',JSON.stringify(btn));await p.close()}
await b.close();srv.close()})();
