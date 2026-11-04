(()=>{'use strict';
if(!document.body||!location.pathname.includes('/class09/'))return;
const buddies=[
 {id:'milo',name:'Milo the Cat',icon:'🐱',lines:['Psst… look for the little detail that makes this idea click.','Curiosity is a superpower. What would happen if we tried it another way?','Nice thinking! Let’s test that idea.']},
 {id:'byte',name:'Byte the Robot',icon:'🤖',lines:['System ready! Let’s break this concept into small steps.','Think of this as input, processing and output. Can you spot each part?','Excellent logic. One step at a time!']},
 {id:'foxy',name:'Foxy the Fox',icon:'🦊',lines:['I have a question: what clue helped you reach that answer?','Let’s investigate. Can you find a pattern?','Aha! Asking why is how discoveries begin.']},
 {id:'momo',name:'Momo the Monkey',icon:'🐵',lines:['Oops! Even experts make mistakes. Let’s have another go.','Challenge accepted! Can you beat this little puzzle?','That deserves a happy dance. Keep going!']}
];
const dock=document.createElement('nav');dock.className='class09-buddy-dock';dock.setAttribute('aria-label','Choose your learning buddy');
dock.innerHTML='<span class="buddy-label">LEARNING BUDDY</span>'+buddies.map((b,i)=>`<button type="button" data-buddy="${b.id}" aria-label="Choose ${b.name}" aria-pressed="${i===1}">${b.icon}</button>`).join('');
const toast=document.createElement('aside');toast.className='class09-buddy-toast';toast.setAttribute('aria-live','polite');toast.innerHTML='<strong>Byte the Robot</strong><p>System ready! Let’s break this concept into small steps.</p>';
document.body.append(toast,dock);
let active='byte',count=0;
try{const saved=localStorage.getItem('cs9-learning-buddy');if(buddies.some(b=>b.id===saved))active=saved}catch(e){}
function render(id,show=true){const b=buddies.find(x=>x.id===id)||buddies[1];active=b.id;dock.querySelectorAll('button').forEach(btn=>btn.setAttribute('aria-pressed',String(btn.dataset.buddy===active)));let line=b.lines[count++%b.lines.length];toast.innerHTML=`<strong>${b.name}</strong><p>${line}</p>`;if(show){toast.classList.add('is-visible');clearTimeout(render.timer);render.timer=setTimeout(()=>toast.classList.remove('is-visible'),5200)}try{localStorage.setItem('cs9-learning-buddy',active)}catch(e){}}
dock.addEventListener('click',e=>{const btn=e.target.closest('[data-buddy]');if(btn)render(btn.dataset.buddy)});
render(active,false);
// Offer contextual encouragement on successful practice without interrupting lesson flow.
document.addEventListener('click',e=>{const btn=e.target.closest('[data-check],[data-run-flowchart],[data-run-sim],[data-sim-run],[data-submit]');if(!btn)return;render(active,true)},true);
})();
