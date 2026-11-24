const {chromium}=require('playwright');
const URL='https://maryamjaberi.github.io/daneshsara/vault.html';
(async()=>{
 const b=await chromium.launch();
 const p=await b.newPage({viewport:{width:430,height:900}});
 let cur='(ورود)';const errs=[];
 p.on('pageerror',e=>errs.push(cur+' → '+e.message.slice(0,60)));
 await p.goto(URL,{waitUntil:'load'});await p.waitForTimeout(2200);
 await p.fill('input[type=password]',process.env.VP);await p.keyboard.press('Enter');
 await p.waitForTimeout(9000);
 const n=(await p.$$('#list a')).length;
 const bad=[],anchorBad=[];
 for(let i=0;i<n;i++){
   const a=(await p.$$('#list a'))[i];cur=(await a.textContent()).trim();
   await a.click();await p.waitForTimeout(400);
   // صبر کن تا صفحه آرام بگیرد (بعضی صفحه‌ها خودشان را می‌سازند)
   for(let w=0;w<10;w++){const l1=await p.evaluate(()=>{const d=document.getElementById('view').contentDocument;
      return d&&d.body?d.body.innerText.length:0});await p.waitForTimeout(220);
     const l2=await p.evaluate(()=>{const d=document.getElementById('view').contentDocument;
      return d&&d.body?d.body.innerText.length:0});if(l1===l2&&l2>0)break}
   const r=await p.evaluate(()=>{const f=document.getElementById('view'),d=f.contentDocument;
     if(!d)return{e:'no doc'};
     const t=(d.body&&d.body.innerText||'').trim();
     return{len:t.length,is404:/this page has moved|was never here/i.test(t),
            ow:d.documentElement.scrollWidth-f.clientWidth,
            anchors:[...d.querySelectorAll('a[href^="#"]')].length}});
   if(r.e||r.len<60||r.is404||r.ow>4) bad.push(cur+' '+JSON.stringify(r));
   // هر لنگر داخل صفحه را بزن و ببین صفحه عوض نمی‌شود
   if(r.anchors){
     const k=Math.min(r.anchors,6);
     for(let j=0;j<k;j++){
       const ok=await p.evaluate(j=>{const d=document.getElementById('view').contentDocument;
         const as=[...d.querySelectorAll('a[href^="#"]')];if(!as[j])return true;
         as[j].click();return true},j);
       await p.waitForTimeout(260);
       const after=await p.evaluate(()=>{const d=document.getElementById('view').contentDocument;
         const t=(d.body&&d.body.innerText||'').trim();
         return{is404:/this page has moved|was never here/i.test(t),len:t.length}});
       if(after.is404||after.len<60){anchorBad.push(cur+' لنگر#'+j);break}
     }
   }
 }
 console.log('صفحه‌ها:',n,'| خراب:',bad.length,'| لنگرِ خراب:',anchorBad.length);
 bad.slice(0,6).forEach(x=>console.log('  صفحه:',x));
 anchorBad.slice(0,6).forEach(x=>console.log('  لنگر:',x));
 console.log(errs.length?'خطاها: '+errs.slice(0,4).join(' | '):'بدون خطای جاوااسکریپت');
 await b.close();
 process.exit(bad.length+anchorBad.length?1:0);
})();
