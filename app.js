/* Celeritas · comportement de la page */

/* ── bloc 1 ─────────────────────────────────────────────── */
(function(){
const V=(window.I18N&&window.I18N.V)||[
{t:"Tuesday, 8 September · work handled",lh:"Done this morning",ls:"with nobody on it",rh:"What it needs from you",
 rows:[["Incoming enquiry qualified and routed","08:12","Renovation job, budget stated, sent to the right rep","ok","Handled"],
 ["Call note written and filed","09:41","Client record updated, next step scheduled","ok","Handled"],
 ["Four quotes chased","10:00","One reply, meeting booked for Thursday","ok","Handled"],
 ["21,600&nbsp;€ quote, silent for 21 days","10:02","Too big for an email, so it hands it to you","you","Your call"],
 ["Weekly reporting refreshed","10:15","Signed revenue, open quotes, win rate","ok","Handled"]],
 right:{to:"Follow up drafted · quote from 28 August · 8,400&nbsp;€",p:["Hello,","I am getting back to you about the quote for the second floor renovation, sent nine days ago."],ty:"Does the budget line up with what you had in mind, or should we talk it through"}},
{t:"Incoming enquiries · last 24 hours",lh:"Enquiries received",ls:"replied to in under a minute",rh:"Reply sent",
 rows:[["Website form · office refurbishment","07:54","Budget and deadline captured, routed to sales","ok","Qualified"],
 ["Missed call at 19:20 last night","19:20","Called back by text within the minute, meeting offered","ok","Recovered"],
 ["Email · supplier invoice","08:03","Not a lead, filed to accounts, nobody disturbed","ok","Filed"],
 ["Email · complaint about a delivery","08:40","Flagged as sensitive, no automatic reply sent","you","Your call"]],
 right:{to:"Auto reply sent · office refurbishment",p:["Thank you for your message,","I have passed your request to the person who handles refurbishment work."],ty:"They will call you back today. In the meantime, could you confirm the floor area"}},
{t:"Quote follow up · this week",lh:"Quotes still open",ls:"7 of 12 with no reply",rh:"Chase drafted",
 rows:[["Office refurbishment, second floor","8,400&nbsp;€","Sent 9 days ago, never chased","you","Chase today"],
 ["Boiler replacement","3,150&nbsp;€","Sent 4 days ago, opened twice","ok","Chase in 2 days"],
 ["Annual maintenance contract","1,920&nbsp;€","Chased yesterday, reply received","ok","Meeting booked"],
 ["Workshop extension","21,600&nbsp;€","Sent 21 days ago, two chases","you","Call, don't email"]],
 right:{to:"Follow up drafted · quote from 28 August · 8,400&nbsp;€",p:["Hello,","I am getting back to you about the quote for the second floor renovation, sent nine days ago."],ty:"Does the budget line up with what you had in mind, or should we talk it through"}},
{t:"Call notes · today",lh:"Calls written up",ls:"nobody typed a word",rh:"Note filed",
 rows:[["Call with a returning client, 14 min","09:38","Summary, decisions, next step scheduled for Monday","ok","Filed"],
 ["Site visit debrief, voice memo","11:20","Turned into a note and attached to the job","ok","Filed"],
 ["Prospect call, 6 min","15:02","Budget mentioned, quote to prepare, reminder set","ok","Filed"],
 ["Call with unclear next step","16:45","It could not tell what was agreed, so it asks you","you","Your call"]],
 right:{to:"Note filed · returning client · 14 min",p:["Wants the same work on the third floor, before the end of the year.","Mentioned a competitor quote around 9,000&nbsp;€."],ty:"Next step: send a quote before Friday, call back Monday morning"}},
{t:"Reporting · week 37",lh:"Kept up to date",ls:"no exports, no copy paste",rh:"Sent to you",
 rows:[["Signed revenue this week","48,200&nbsp;€","Up from 31,900&nbsp;€ last week","ok","Current"],
 ["Open quotes","94,700&nbsp;€","Across 12 quotes, 7 with no reply","ok","Current"],
 ["Win rate, rolling 90 days","38 %","Rises to 61 % on quotes chased twice","ok","Current"],
 ["Average reply time to an enquiry","4 min","Was 14 hours before the first workflow","ok","Current"]],
 right:{to:"Monday summary · sent to your phone at 07:30",p:["Three quotes need a call this week, one of them over 20,000 €.","Reply time held under five minutes all week."],ty:"Nothing else needs you today"}}];
const rows=document.getElementById('rows'),right=document.getElementById('right');
const esc=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
function draw(i,skel){const v=V[i];
 document.getElementById('wt').textContent=v.t;document.getElementById('lh').textContent=v.lh;
 document.getElementById('ls').textContent=v.ls;document.getElementById('rh').textContent=v.rh;
 if(skel!==false&&!matchMedia('(prefers-reduced-motion:reduce)').matches){
  rows.innerHTML='<div class="sk"></div><div class="sk"></div><div class="sk"></div>';
  right.innerHTML='<div class="sk" style="height:150px"></div>';
  clearTimeout(window.__sk);window.__sk=setTimeout(()=>paint(v),330);return}
 paint(v);}
function paint(v){
 rows.innerHTML=v.rows.map((r,ix)=>`<div class="row" style="--i:${ix*55}ms"><span class="n">${esc(r[0])}</span><span class="m">${esc(r[1])}</span><span class="s">${esc(r[2])}</span><span class="tg ${r[3]}">${esc(r[4])}</span></div>`).join('');
 right.innerHTML=`<div class="draft"><div class="to">${v.right.to}</div>${v.right.p.map(p=>`<p>${p}</p>`).join('')}<p class="type">${v.right.ty}</p><div class="act"><span class="a1">Send</span><span class="a2">Edit</span><span class="a2">Later</span></div></div><p class="note">${window.I18N&&window.I18N.lang==='fr'?"Rien ne part à un client sans votre validation, tant que vous n'en décidez pas autrement.":"Nothing reaches a client without your approval, until you decide otherwise."}</p>`;
}
const TB=[...document.querySelectorAll('.tab')];
function sel(b){ai=TB.indexOf(b);TB.forEach(x=>{x.classList.remove('on');x.setAttribute('aria-selected','false')});b.classList.add('on');b.setAttribute('aria-selected','true');draw(+b.dataset.i);}
TB.forEach((b,i)=>{b.addEventListener('click',()=>sel(b));
 b.addEventListener('keydown',e=>{if(e.key!=='ArrowRight'&&e.key!=='ArrowLeft')return;e.preventDefault();
  const n=TB[(i+(e.key==='ArrowRight'?1:TB.length-1))%TB.length];n.focus();sel(n);});});
addEventListener('scroll',()=>document.querySelector('header').classList.toggle('stuck',scrollY>8),{passive:true});
function countUp(){
 if(matchMedia('(prefers-reduced-motion:reduce)').matches)return;
 rows.querySelectorAll('.m').forEach(el=>{
  const raw=el.textContent, m=raw.match(/^([\d.,]+)/); if(!m)return;
  const target=parseFloat(m[1].replace(/,/g,'')); if(!isFinite(target)||target<10)return;
  const suffix=raw.slice(m[1].length), dec=(m[1].split('.')[1]||'').length, t0=performance.now(), D=680;
  (function step(now){const k=Math.min(1,(now-t0)/D), e=1-Math.pow(1-k,3), v=target*e;
   el.textContent=(dec?v.toFixed(dec):Math.round(v)).toString().replace(/\B(?=(\d{3})+(?!\d))/g,',')+suffix;
   if(k<1)requestAnimationFrame(step)})(t0);
 });
}
draw(0);
let auto=null,ai=0;
const reduce=matchMedia('(prefers-reduced-motion:reduce)').matches;
function stopAuto(){if(auto){clearInterval(auto);auto=null}document.querySelectorAll('.tab').forEach(b=>b.classList.remove('timing'))}
function restartTiming(){const on=document.querySelector('.tab.on');if(!on)return;on.classList.remove('timing');void on.offsetWidth;if(auto)on.classList.add('timing')}
function startAuto(){if(reduce)return;stopAuto();auto=setInterval(()=>{ai=(ai+1)%TB.length;sel(TB[ai])},4200);restartTiming()}
new IntersectionObserver(es=>es.forEach(e=>e.isIntersecting?startAuto():stopAuto()),{threshold:.35})
 .observe(document.querySelector('.win'));
['click','keydown','touchstart'].forEach(ev=>document.querySelector('.stage').addEventListener(ev,stopAuto,{once:true}));
document.addEventListener('visibilitychange',()=>document.hidden&&stopAuto());
const bg=document.querySelector('.burger'),mn=document.querySelector('.nav ul');
bg.addEventListener('click',()=>{const o=mn.classList.toggle('open');bg.setAttribute('aria-expanded',o)});
mn.addEventListener('click',e=>{if(e.target.tagName==='A'){mn.classList.remove('open');bg.setAttribute('aria-expanded','false')}});

/* ===== mouvement piloté par le défilement ===== */
(function(){
 const RM=matchMedia('(prefers-reduced-motion:reduce)').matches;

 /* le titre mot par mot */
 const h1=document.querySelector('h1');
 if(h1&&!RM){
  const walk=n=>{[...n.childNodes].forEach(c=>{
    if(c.nodeType===3){const f=document.createDocumentFragment();
      c.textContent.split(/(\s+)/).forEach(w=>{if(!w.trim()){f.appendChild(document.createTextNode(w));return}
        const s=document.createElement('span');s.className='wd';s.textContent=w;f.appendChild(s)});
      n.replaceChild(f,c);} else if(c.nodeType===1) walk(c);});};
  walk(h1);
  h1.querySelectorAll('.wd').forEach((w,i)=>w.style.animationDelay=(0.06+i*0.045)+'s');
  h1.style.animation='none';h1.style.opacity='1';h1.style.transform='none';
 }

 const clamp=(v,a,b)=>Math.max(a,Math.min(b,v));
 const prog=(el,ahead=0)=>{const r=el.getBoundingClientRect();
  return clamp((innerHeight*0.92-r.top-ahead)/(innerHeight*0.75+r.height*0.5),0,1)};


 /* la scène épinglée : trois moments de la journée */
 const pin=document.getElementById('never');
 const MOMENTS=(window.I18N&&window.I18N.MOMENTS)||[
  'Answer the 19:20 enquiry.',
  'Chase every quote to a yes or a no.',
  'Write the call note before the next call.',
  'End the double entry.',
  'Replace the spreadsheet everyone waits for.',
  'Rebuild the reporting, once.',
  'Sort tomorrow\u2019s list overnight.',
  'Whatever your team does twice a week and hates.'
 ];
 let last=-1;
 function pinFrame(){
  if(!pin)return;
  const r=pin.getBoundingClientRect();
  const p=clamp(-r.top/(r.height-innerHeight),0,1);
  const bar=document.getElementById('pbar'); if(bar)bar.style.transform='scaleX('+p.toFixed(3)+')';
  const i=clamp(Math.floor(p*MOMENTS.length),0,MOMENTS.length-1);
  if(i!==last){last=i;
   const line=document.getElementById('dline'), num=document.getElementById('dnum');
   line.style.opacity='0';line.style.transform='translateY(10px)';
   setTimeout(()=>{line.textContent=MOMENTS[i];num.textContent=String(i+1).padStart(2,'0');
    line.style.opacity='1';line.style.transform='none'},150);
  }
 }

 /* la barre de navigation s'efface vers le bas, revient vers le haut */
 const hd=document.querySelector('header'); let prev=scrollY;
 function navFrame(){
  const y=scrollY;
  hd.classList.toggle('shy', y>prev && y>320 && !hd.contains(document.activeElement));
  prev=y;
 }

 let tick=false;
 function frame(){pinFrame();navFrame();tick=false}
 addEventListener('scroll',()=>{if(!tick){tick=true;requestAnimationFrame(frame)}},{passive:true});
 addEventListener('resize',frame,{passive:true});
 frame();
})();

/* ===== couche d'effets ===== */
(function(){
 const RM=matchMedia('(prefers-reduced-motion:reduce)').matches;
 const clamp=(v,a,b)=>Math.max(a,Math.min(b,v));

 /* progression de lecture */
 const sp=document.getElementById('sp');
 /* la barre de navigation s'inverse au-dessus de la scène noire */
 const hd=document.querySelector('header'), pin=document.getElementById('never');
 function bar(){
  const h=document.documentElement;
  const max=h.scrollHeight-innerHeight;
  if(sp)sp.style.transform='scaleX('+(max>0?clamp(scrollY/max,0,1):0).toFixed(4)+')';
  if(pin){const r=pin.getBoundingClientRect();
   hd.classList.toggle('dark', r.top<=68 && r.bottom>68);}
 }
 addEventListener('scroll',bar,{passive:true});addEventListener('resize',bar,{passive:true});bar();

 /* le contour de la fenêtre se dessine à son entrée */
 const win=document.querySelector('.win');
 if(win&&!RM){new IntersectionObserver((es,o)=>es.forEach(e=>{
   if(e.isIntersecting){win.classList.add('armed');o.disconnect()}}),{threshold:.4}).observe(win);}

 /* la fenêtre suit la souris, très légèrement */
 const stage=document.querySelector('.stage');
 if(stage&&win&&!RM&&matchMedia('(pointer:fine)').matches){
  stage.addEventListener('pointermove',e=>{
   const r=stage.getBoundingClientRect();
   const x=(e.clientX-r.left)/r.width-.5, y=(e.clientY-r.top)/r.height-.5;
   win.style.transform=`rotateY(${(x*3.2).toFixed(2)}deg) rotateX(${(-y*2.2).toFixed(2)}deg) translateZ(0)`;
  });
  stage.addEventListener('pointerleave',()=>{win.style.transform=''});
 }

 /* compteur de la barre de fenêtre */
 const cnt=document.getElementById('cnt');
 if(cnt){let v=0;const target=47;
  const io=new IntersectionObserver((es,o)=>es.forEach(e=>{if(!e.isIntersecting)return;o.disconnect();
   if(RM){cnt.textContent=target;return}
   const t0=performance.now();
   (function s(n){const k=clamp((n-t0)/900,0,1);cnt.textContent=Math.round(target*(1-Math.pow(1-k,3)));
    if(k<1)requestAnimationFrame(s);else setInterval(()=>{if(document.hidden)return;v++;cnt.textContent=target+v},14000)})(t0);
  }),{threshold:.5});io.observe(cnt);}

 /* les titres de section se révèlent mot par mot */
 if(!RM){
  document.querySelectorAll('.sentence').forEach(h=>{
   const walk=n=>{[...n.childNodes].forEach(c=>{
     if(c.nodeType===3){const f=document.createDocumentFragment();
       c.textContent.split(/(\s+)/).forEach(w=>{if(!w.trim()){f.appendChild(document.createTextNode(w));return}
         const s=document.createElement('span');s.className='sw';s.style.cssText='display:inline-block;opacity:0;transform:translateY(12px);transition:opacity .42s cubic-bezier(.22,1,.36,1),transform .42s cubic-bezier(.22,1,.36,1)';
         s.textContent=w;f.appendChild(s)});
       n.replaceChild(f,c);} else if(c.nodeType===1) walk(c);});};
   walk(h);
   const ws=[...h.querySelectorAll('.sw')];
   ws.forEach((w,i)=>w.style.transitionDelay=(i*34)+'ms');
   new IntersectionObserver((es,o)=>es.forEach(e=>{if(e.isIntersecting){
     ws.forEach(w=>{w.style.opacity='1';w.style.transform='none'});o.disconnect()}}),{threshold:.25}).observe(h);
   setTimeout(()=>ws.forEach(w=>{w.style.opacity='1';w.style.transform='none'}),4000);
  });
 }
})();

/* la comparaison avant / après se dresse au défilement */
(function(){
 const ba=document.getElementById('ba'); if(!ba)return;
 [...ba.querySelectorAll('.seg')].forEach((s,i)=>s.style.setProperty('--d',(i%3*110)+'ms'));
 if(matchMedia('(prefers-reduced-motion:reduce)').matches){ba.classList.add('on');return}
 new IntersectionObserver((es,o)=>es.forEach(e=>{if(e.isIntersecting){ba.classList.add('on');o.disconnect()}}),{threshold:.3}).observe(ba);
 setTimeout(()=>ba.classList.add('on'),4200);
 document.querySelectorAll('.card').forEach(c=>{
  c.querySelectorAll('.k svg *').forEach(s=>{try{const L=s.getTotalLength?s.getTotalLength():120;s.style.setProperty('--L',Math.ceil(L))}catch(e){}});
 });
})();

/* la frise verticale s'anime à l'entrée */
(function(){
 const rail=document.querySelector('.rail'); if(!rail)return;
 [...rail.querySelectorAll('.rdot')].forEach((d,i)=>d.style.setProperty('--d',(i*130)+'ms'));
 if(matchMedia('(prefers-reduced-motion:reduce)').matches){rail.classList.add('on');return}
 new IntersectionObserver((es,o)=>es.forEach(e=>{if(e.isIntersecting){rail.classList.add('on');o.disconnect()}}),{threshold:.2}).observe(rail);
 setTimeout(()=>rail.classList.add('on'),4000);
})();

/* ===== quarante points, mouvement libre, qui s'écartent du curseur ===== */
(function(){
 const field=document.getElementById('field'); if(!field)return;
 const RM=matchMedia('(prefers-reduced-motion:reduce)').matches;
 const N=40, dots=[];
 const R=()=>Math.random();
 for(let i=0;i<N;i++){
  const el=document.createElement('b');
  const size=1.5+Math.pow(R(),2)*5.5;
  const glow=size>4.4;
  el.style.width=el.style.height=size.toFixed(1)+'px';
  el.style.opacity=(0.28+R()*0.72).toFixed(2);
  if(glow)el.style.boxShadow='0 0 '+(size*3.4).toFixed(0)+'px '+(size/2).toFixed(0)+'px rgba(59,130,246,.45)';
  field.appendChild(el);
  dots.push({el,
   r:8+Math.pow(R(),0.72)*46,        /* rayon en % de la plus petite dimension */
   a:R()*Math.PI*2,                   /* angle de départ */
   w:(R()<0.5?-1:1)*(0.05+R()*0.22),  /* vitesse angulaire, les deux sens */
   e:0.72+R()*0.55,                   /* aplatissement, aucune orbite parfaitement ronde */
   ti:R()*Math.PI*2, ts:0.25+R()*0.7, ta:2+R()*9,  /* dérive propre */
   ox:0, oy:0, vx:0, vy:0});
 }
 let mx=-9999, my=-9999, w=0, h=0, unit=0;
 function measure(){const r=field.getBoundingClientRect();w=r.width;h=r.height;unit=Math.min(w,h)/100}
 measure(); addEventListener('resize',measure,{passive:true});
 const pin=document.getElementById('never');
 if(pin){
  pin.addEventListener('pointermove',e=>{const r=field.getBoundingClientRect();mx=e.clientX-r.left-w/2;my=e.clientY-r.top-h/2},{passive:true});
  pin.addEventListener('pointerleave',()=>{mx=my=-9999},{passive:true});
 }
 let t0=performance.now(), run=true;
 if(pin)new IntersectionObserver(es=>es.forEach(e=>{run=e.isIntersecting;if(run)t0=performance.now()}),{threshold:0}).observe(pin);
 function frame(now){
  requestAnimationFrame(frame);
  if(!run||RM)return;
  const dt=Math.min(0.05,(now-t0)/1000); t0=now;
  for(const d of dots){
   d.a+=d.w*dt; d.ti+=d.ts*dt;
   const bx=Math.cos(d.a)*d.r*unit + Math.cos(d.ti)*d.ta;
   const by=Math.sin(d.a)*d.r*d.e*unit + Math.sin(d.ti*1.3)*d.ta;
   /* répulsion du curseur */
   const dx=bx+d.ox-mx, dy=by+d.oy-my, dist=Math.hypot(dx,dy)||1;
   const reach=140;
   if(dist<reach){const f=(1-dist/reach)*260/dist; d.vx+=dx*f*dt; d.vy+=dy*f*dt}
   /* rappel élastique vers l'orbite */
   d.vx+=-d.ox*7.5*dt; d.vy+=-d.oy*7.5*dt;
   d.vx*=0.90; d.vy*=0.90;
   d.ox+=d.vx*dt*60*0.05; d.oy+=d.vy*dt*60*0.05;
   d.el.style.transform=`translate(${(bx+d.ox).toFixed(1)}px,${(by+d.oy).toFixed(1)}px) translate(-50%,-50%)`;
  }
 }
 requestAnimationFrame(frame);
})();
})();

/* ── bloc 2 ─────────────────────────────────────────────── */
(function(){
/* révélations au défilement */
(function(){
 const RM=matchMedia('(prefers-reduced-motion:reduce)').matches;
 const groups=[['.shead',0],['.bt',55],['.rstep',70],['.c2',90],['.bs',80],['.risk div',70],['#custom .li',45],['#who p',80],['details',35],['.final .sentence',0],['.final p',70],['.final .hcta',120]];
 const targets=[];
 groups.forEach(([sel,step])=>{document.querySelectorAll(sel).forEach((el,i)=>{el.classList.add('rv');el.style.setProperty('--d',(i*step)+'ms');targets.push(el)})});
 if(RM){targets.forEach(e=>e.classList.add('in'));document.querySelector('.steps').classList.add('in');return}
 const show=el=>{el.classList.add('in')};
 const inView=el=>{const r=el.getBoundingClientRect();return r.top<innerHeight*0.94&&r.bottom>0};
 const sweep=()=>{let left=0;targets.forEach(el=>{if(el.classList.contains('in'))return;if(inView(el))show(el);else left++});
  if(!left)removeEventListener('scroll',sweep);};
 if('IntersectionObserver' in window){
  const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){show(e.target);io.unobserve(e.target)}}),{threshold:.12,rootMargin:'0px 0px -6% 0px'});
  targets.forEach(e=>io.observe(e));
  const st=document.querySelector('.steps');
  if(st)new IntersectionObserver(es=>es.forEach(e=>e.isIntersecting&&e.target.classList.add('in')),{threshold:.25}).observe(st);
 }
 /* filet de sécurité : rien ne doit rester invisible */
 addEventListener('scroll',sweep,{passive:true});
 addEventListener('resize',sweep,{passive:true});
 requestAnimationFrame(sweep);
 setTimeout(sweep,300);
 setTimeout(()=>{targets.forEach(show);const st=document.querySelector('.steps');if(st)st.classList.add('in')},3500);
})();
})();




/* ══ le journal d'exécution ═══════════════════════════════════════════════ */
(function(){
 const log=document.getElementById('flog'); if(!log)return;
 const cnt=document.getElementById('fcnt');
 const FR=window.I18N&&window.I18N.lang==='fr';
 const L=FR?[
  ["Demande entrante qualifiée","chantier de rénovation, budget annoncé","Traité"],
  ["Devis 3 150 € relancé","deuxième relance, ouvert deux fois","Traité"],
  ["Compte rendu d'appel classé","fiche client à jour, rappel lundi","Traité"],
  ["Appel manqué rattrapé","SMS envoyé dans la minute","Traité"],
  ["Facture fournisseur classée","personne dérangé","Traité"],
  ["Devis 21 600 € sans réponse","trop gros pour un mail","À vous",1],
  ["Reporting hebdomadaire mis à jour","chiffre signé, devis en cours","Traité"],
  ["Ligne de tableur synchronisée","plus de double saisie","Traité"],
  ["Réclamation détectée","marquée sensible, aucune réponse automatique","À vous",1],
  ["Rendez-vous confirmé","jeudi 14h, ajouté à l'agenda","Traité"]]:[
  ["Incoming enquiry qualified","renovation job, budget stated","Handled"],
  ["3,150 € quote chased","second chase, opened twice","Handled"],
  ["Call note filed","client record updated, reminder Monday","Handled"],
  ["Missed call recovered","text sent within the minute","Handled"],
  ["Supplier invoice filed","nobody disturbed","Handled"],
  ["21,600 € quote, no reply","too big for an email","Your call",1],
  ["Weekly reporting refreshed","signed revenue, open quotes","Handled"],
  ["Spreadsheet row synced","no more double entry","Handled"],
  ["Complaint detected","flagged sensitive, no automatic reply","Your call",1],
  ["Meeting confirmed","Thursday 2pm, added to the diary","Handled"]];
 const word=FR?" traités aujourd'hui":" handled today";
 let i=0,n=0,visible=false;
 new IntersectionObserver(e=>{visible=e[0].isIntersecting},{threshold:.2}).observe(log);
 const hhmm=()=>{const d=new Date();return String(d.getHours()).padStart(2,'0')+':'+String(d.getMinutes()).padStart(2,'0')};
 const esc=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
 function push(first){
  if(!first&&(!visible||document.hidden))return;
  const [m,e,s,you]=L[i++%L.length];
  const el=document.createElement('div');
  el.className='fln'+(you?' you':'');
  el.innerHTML='<span class="ft">'+hhmm()+'</span><span class="fm">'+esc(m)+' <em>· '+esc(e)+'</em></span><span class="fs">'+esc(s)+'</span>';
  log.prepend(el);
  while(log.children.length>8)log.lastChild.remove();
  if(!you){n++;cnt.textContent=n+word}
 }
 for(let k=0;k<4;k++)push(true);
 setInterval(push,1600);
})();
