/* Class 9 Study & Copy controls. Loaded only by Class 9 lesson pages that need the shared notebook UI. */
(()=>{'use strict';
const section=document.querySelector('#write-notes');
if(!section)return;
const buttons=[...section.querySelectorAll('[data-notes-mode]')];
const hint=section.querySelector('[data-notes-mode-hint]');
const note=section.querySelector('.handwritten-notes');
const focus=section.querySelector('[data-writing-focus]');
const status=section.querySelector('[data-notes-status]');
function setMode(mode){
 section.dataset.notesMode=mode;
 if(note){note.classList.toggle('notes-mode-notebook',mode==='notebook');note.classList.toggle('notes-mode-hybrid',mode==='hybrid')}
 buttons.forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.notesMode===mode)));
 if(hint)hint.textContent=mode==='notebook'?'Notebook view: lined paper, colourful headings and highlighted definitions.':'Clean view: uncluttered notes for reading and printing.';
}
buttons.forEach(b=>b.addEventListener('click',()=>setMode(b.dataset.notesMode)));
setMode('notebook');
focus?.addEventListener('click',()=>{
 const active=document.body.classList.toggle('writing-focus');
 focus.setAttribute('aria-pressed',String(active));
 focus.textContent=active?'✕ Exit writing view':'⛶ Writing view';
 if(active)note?.scrollIntoView({block:'start'});
});
section.querySelector('[data-print-notes]')?.addEventListener('click',()=>window.print());
section.querySelector('[data-copy-notes]')?.addEventListener('click',async()=>{
 if(!note||!status)return;
 try{await navigator.clipboard.writeText(note.innerText);status.textContent='Notes copied.'}
 catch(e){status.textContent='Copy is unavailable here; select the note text and copy it manually.'}
});
})();