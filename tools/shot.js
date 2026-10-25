const {chromium}=require('/workspace/krow-site/tools/node_modules/playwright-core');
(async()=>{
 const b=await chromium.launch({executablePath:'/usr/bin/google-chrome',args:['--no-sandbox']});
 const base=process.argv[2]||'http://127.0.0.1:8091/';
 for(const [path,w,h,out,full] of [['',1440,900,'/workspace/dedehan-1440.png',true],['',390,844,'/workspace/dedehan-390.png',true],['en/',1440,900,'/workspace/dedehan-en-1440.png',false],['en/',390,844,'/workspace/dedehan-en-390.png',false]]){
  const pg=await b.newPage({viewport:{width:w,height:h},deviceScaleFactor:1});
  const errs=[];pg.on('console',m=>{if(m.type()==='error')errs.push(m.text())});pg.on('pageerror',e=>errs.push('PAGEERR '+e.message));
  pg.on('requestfailed',r=>errs.push('FAILED '+r.url()));
  pg.on('response',r=>{if(r.status()>=400)errs.push(r.status()+' '+r.url())});
  await pg.goto(base+path,{waitUntil:'networkidle'});await pg.evaluate(()=>document.querySelectorAll('img[loading=lazy]').forEach(i=>i.loading='eager'));await pg.waitForLoadState('networkidle');
  await pg.evaluate(async()=>{for(let y=0;y<document.body.scrollHeight;y+=400){window.scrollTo(0,y);await new Promise(r=>setTimeout(r,60))}window.scrollTo(0,0)});
  await pg.evaluate(()=>document.querySelectorAll('.rv').forEach(e=>e.classList.add('in')));
  await pg.waitForTimeout(1500);
  const broken=await pg.evaluate(()=>[...document.images].filter(i=>i.getAttribute('src')&&(!i.complete||i.naturalWidth===0)).map(i=>i.src));
  const ow=await pg.evaluate(()=>document.documentElement.scrollWidth>window.innerWidth);
  await pg.screenshot({path:out,fullPage:full});
  console.log(path||'/',w,'errors:',JSON.stringify(errs),'broken:',JSON.stringify(broken),'hOverflow:',ow);
  await pg.close();
 }
 // test lightbox + form on mobile
 const pg=await b.newPage({viewport:{width:390,height:844}});
 await pg.goto(base,{waitUntil:'networkidle'});
 await pg.click('.burger');await pg.waitForTimeout(600);await pg.screenshot({path:'/workspace/dedehan-390-menu.png'});await pg.click('.nav a[href="#galeri"]');
 await pg.waitForTimeout(800);await pg.click('.gal button >> nth=0');await pg.waitForTimeout(600);
 await pg.screenshot({path:'/workspace/dedehan-390-lightbox.png'});
 console.log('lightbox on:',await pg.evaluate(()=>document.querySelector('.lb').classList.contains('on')));
 await pg.keyboard.press('Escape');
 let popupUrl=null;pg.context().on('page',p=>{popupUrl=p.url()});
 await pg.evaluate(()=>{window.open=(u)=>{window.__u=u}});
 await pg.fill('[name=name]','Test Kişi');
 const d1=new Date(Date.now()+86400e3*3).toISOString().slice(0,10),d2=new Date(Date.now()+86400e3*5).toISOString().slice(0,10);
 await pg.fill('[name=in]',d1);await pg.fill('[name=out]',d2);
 await pg.click('form.inq button[type=submit]');
 console.log('wa url:',decodeURIComponent(await pg.evaluate(()=>window.__u)));
 await b.close();
})();
