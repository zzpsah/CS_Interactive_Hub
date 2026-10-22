/* Accessible image zoom viewer for the Chapter 1 hardware gallery.
   Kept separate from the general app so a failure in an unrelated interaction
   cannot disable image zoom. */
(()=>{'use strict';
 const dialog=document.querySelector('[data-image-zoom-dialog]');
 if(!dialog)return;
 const image=dialog.querySelector('[data-image-zoom-full]');
 const title=dialog.querySelector('[data-image-zoom-title]');
 const viewport=dialog.querySelector('[data-image-zoom-viewport]');
 const hint=dialog.querySelector('.image-zoom-hint');
 if(!image||!title||!viewport)return;
 let zoom=1;
 const render=()=>{
   image.style.width=(zoom*100)+'%';
   image.style.maxWidth='none';
   image.style.transform='none';
   image.style.margin='0';
   if(hint)hint.textContent='Zoom: '+Math.round(zoom*100)+'% · Use + / − to inspect details. / ज़ूम नियंत्रण से चित्र के भाग देखें।';
 };
 const open=(button)=>{
   zoom=1;
   image.style.width='100%';
   image.style.maxWidth='100%';
   image.style.transform='none';
   image.src=button.dataset.imageZoom;
   image.alt=button.querySelector('img')?.alt||button.dataset.imageTitle||'Hardware illustration';
   title.textContent=button.dataset.imageTitle||'Hardware detail';
   render();
   if(typeof dialog.showModal==='function'){
     if(!dialog.open)dialog.showModal();
   }else{
     dialog.setAttribute('open','');
   }
 };
 document.addEventListener('click',(event)=>{
   const button=event.target.closest('[data-image-zoom]');
   if(button){event.preventDefault();open(button);}
 });
 dialog.querySelector('[data-zoom-in]')?.addEventListener('click',()=>{zoom=Math.min(zoom+0.25,4);render();});
 dialog.querySelector('[data-zoom-out]')?.addEventListener('click',()=>{zoom=Math.max(zoom-0.25,0.5);render();});
 dialog.querySelector('[data-zoom-reset]')?.addEventListener('click',()=>{
   zoom=1;render();viewport.scrollTo({left:0,top:0,behavior:'auto'});
 });
 dialog.querySelector('[data-zoom-close]')?.addEventListener('click',()=>{
   if(typeof dialog.close==='function'&&dialog.open)dialog.close();else dialog.removeAttribute('open');
 });
 dialog.addEventListener('click',(event)=>{
   if(event.target===dialog){
     if(typeof dialog.close==='function'&&dialog.open)dialog.close();else dialog.removeAttribute('open');
   }
 });
 image.addEventListener('error',()=>{
   if(hint)hint.textContent='This illustration could not be loaded. Please reload the page and try again.';
 });
})();
