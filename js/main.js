(function(){
  var d=document,hdr=d.querySelector('.hdr');
  function onScroll(){hdr.classList.toggle('solid',window.scrollY>40)}
  onScroll();window.addEventListener('scroll',onScroll,{passive:true});
  var burger=d.querySelector('.burger');
  burger.addEventListener('click',function(){var o=d.body.classList.toggle('menu-open');burger.setAttribute('aria-expanded',o)});
  d.querySelectorAll('.nav a').forEach(function(a){a.addEventListener('click',function(){d.body.classList.remove('menu-open');burger.setAttribute('aria-expanded','false')})});
  // reveal
  if('IntersectionObserver' in window){
    var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{rootMargin:'0px 0px -8% 0px'});
    d.querySelectorAll('.rv').forEach(function(el){io.observe(el)});
  }else d.querySelectorAll('.rv').forEach(function(el){el.classList.add('in')});
  // lightbox
  var items=[].slice.call(d.querySelectorAll('.gal button')),lb=d.querySelector('.lb'),lbImg=lb.querySelector('img'),cap=lb.querySelector('.cap'),i=0;
  function show(n){i=(n+items.length)%items.length;var b=items[i];lbImg.src=b.dataset.full;lbImg.alt=b.dataset.cap;cap.textContent=b.dataset.cap+'  ·  '+(i+1)+' / '+items.length}
  function open(n){show(n);lb.classList.add('on');d.body.style.overflow='hidden';lb.querySelector('.x').focus()}
  function close(){lb.classList.remove('on');d.body.style.overflow='';items[i].focus()}
  items.forEach(function(b,n){b.addEventListener('click',function(){open(n)})});
  lb.querySelector('.x').onclick=close;lb.querySelector('.p').onclick=function(){show(i-1)};lb.querySelector('.n').onclick=function(){show(i+1)};
  lb.addEventListener('click',function(e){if(e.target===lb)close()});
  d.addEventListener('keydown',function(e){if(!lb.classList.contains('on'))return;if(e.key==='Escape')close();if(e.key==='ArrowLeft')show(i-1);if(e.key==='ArrowRight')show(i+1)});
  var sx=0;lb.addEventListener('touchstart',function(e){sx=e.touches[0].clientX},{passive:true});
  lb.addEventListener('touchend',function(e){var dx=e.changedTouches[0].clientX-sx;if(Math.abs(dx)>50)show(i+(dx<0?1:-1))});
  // inquiry form
  var f=d.querySelector('form.inq');
  if(f){
    var t=JSON.parse(f.dataset.t),inEl=f.querySelector('[name=in]'),outEl=f.querySelector('[name=out]');
    var today=new Date().toISOString().slice(0,10);inEl.min=today;outEl.min=today;
    inEl.addEventListener('change',function(){outEl.min=inEl.value||today;if(outEl.value&&outEl.value<=inEl.value)outEl.value=''});
    f.addEventListener('submit',function(e){
      e.preventDefault();var err=f.querySelector('.form-err');
      var v=function(n){return (f.querySelector('[name='+n+']').value||'').trim()};
      if(!v('name')||!v('in')||!v('out')){err.textContent=t.req;err.style.display='block';return}
      if(v('out')<=v('in')){err.textContent=t.dates;err.style.display='block';return}
      err.style.display='none';
      var fmt=function(s){var p=s.split('-');return p[2]+'.'+p[1]+'.'+p[0]};
      var msg=t.hi+'\n\n'+t.name+': '+v('name')+'\n'+t.cin+': '+fmt(v('in'))+'\n'+t.cout+': '+fmt(v('out'))+'\n'+t.guests+': '+v('guests')+'\n'+t.room+': '+v('room')+(v('phone')?'\n'+t.phone+': '+v('phone'):'')+(v('note')?'\n'+t.note+': '+v('note'):'');
      window.open('https://wa.me/'+f.dataset.wa+'?text='+encodeURIComponent(msg),'_blank','noopener');
    });
  }
  d.querySelectorAll('[data-room]').forEach(function(a){a.addEventListener('click',function(){var s=d.querySelector('[name=room]');if(s)s.value=a.dataset.room})});
  var y=d.getElementById('yr');if(y)y.textContent=new Date().getFullYear();
})();
