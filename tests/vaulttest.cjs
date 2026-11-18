const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const out={};
for(const [k,u,pw] of [['vault','https://maryamjaberi.github.io/daneshsara/vault.html',process.env.VP],['share','https://maryamjaberi.github.io/simorgh/',process.env.SP]]){
 const c=await b.newContext({viewport:{width:390,height:844}});const p=await c.newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message.slice(0,100)));
 await p.goto(u);const locked=await p.evaluate(()=>!document.querySelector('#app.on'));
 await p.fill('#pw','wrong password here');await p.click('#go');await p.waitForTimeout(2500);const wrongRejected=await p.evaluate(()=>!document.querySelector('#app.on'));
 await p.fill('#pw',pw);await p.click('#go');await p.waitForSelector('#app.on',{timeout:60000});await p.waitForTimeout(1500);
 const paths=await p.$$eval('#list a[data-p]',a=>a.map(x=>x.dataset.p));const html=paths.filter(x=>x.endsWith('.html'));
 let bad=[],empty=[];
 for(const h of html){await p.evaluate(x=>document.querySelector(`#list a[data-p="${x}"]`).click(),h);await p.waitForTimeout(350);
  const f=p.frames()[1];try{const n=await f.evaluate(()=>document.body.innerText.trim().length);if(n<40)empty.push(h)}catch(e){bad.push(h)}}
 out[k]={locked,wrongRejected,pages:html.length,empty,bad,errs:errs.slice(0,5),overflow:await p.evaluate(()=>document.documentElement.scrollWidth-innerWidth)};await c.close()}
const raw=await (await fetch('https://maryamjaberi.github.io/daneshsara/vault/bundle.enc')).arrayBuffer();const t=Buffer.from(raw).toString('latin1');
out.plaintextLeak=/simorgh|سیمرغ|<html/i.test(t.slice(40));
console.log(JSON.stringify(out,null,1));require('fs').writeFileSync('vault.json',JSON.stringify(out));await b.close()})();
