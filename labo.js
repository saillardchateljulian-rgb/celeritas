/* Celeritas · trois mécaniques en démonstration */

/* ══ A · le canevas qui se construit ══════════════════════════════════════ */
(function(){
 const cv=document.getElementById('cv'); if(!cv)return;
 const svg=document.getElementById('edges'), tok=document.getElementById('tok');
 const capL=document.getElementById('capL'), capR=document.getElementById('capR');
 const FLOWS=[
  {name:"Appel manqué à 19:20",nodes:[
   {x:12,y:50,ico:"T",b:"Appel manqué",i:"19:20"},
   {x:36,y:26,ico:"?",b:"Qualifier",i:"budget, délai"},
   {x:36,y:74,ico:"↺",b:"Rappeler par SMS",i:"dans la minute"},
   {x:64,y:50,ico:"✓",b:"Rendez-vous proposé",i:"jeudi 14h"},
   {x:88,y:50,ico:"→",b:"CRM",i:"fiche créée"}],
   edges:[[0,1],[0,2],[1,3],[2,3],[3,4]]},
  {name:"Devis sans réponse depuis 9 jours",nodes:[
   {x:12,y:50,ico:"€",b:"Devis 8 400 €",i:"envoyé le 28/08"},
   {x:38,y:30,ico:"◷",b:"Aucune réponse",i:"9 jours"},
   {x:38,y:72,ico:"✎",b:"Relance rédigée",i:"ton habituel"},
   {x:66,y:50,ico:"!",b:"Validation",i:"un clic"},
   {x:89,y:50,ico:"→",b:"Envoyé",i:"réponse reçue"}],
   edges:[[0,1],[1,2],[2,3],[3,4]]},
  {name:"Fin d'appel commercial",nodes:[
   {x:12,y:50,ico:"☏",b:"Appel terminé",i:"14 min"},
   {x:36,y:28,ico:"⌁",b:"Résumé écrit",i:"décisions, suite"},
   {x:36,y:72,ico:"⊞",b:"Fiche mise à jour",i:"sans saisie"},
   {x:63,y:50,ico:"◔",b:"Rappel programmé",i:"lundi 9h"},
   {x:88,y:50,ico:"→",b:"Reporting",i:"à jour"}],
   edges:[[0,1],[0,2],[1,3],[2,3],[3,4]]}];

 const wait=ms=>new Promise(r=>setTimeout(r,ms));
 let stop=false;
 new IntersectionObserver(e=>{stop=!e[0].isIntersecting},{threshold:.15}).observe(cv);

 function pos(n){const r=cv.getBoundingClientRect();return{x:n.x/100*r.width,y:n.y/100*r.height}}

 async function play(fi){
  const F=FLOWS[fi];
  capR.textContent=fi+1; capL.textContent="Construction du flux";
  cv.querySelectorAll('.nd').forEach(e=>e.remove()); svg.innerHTML=''; tok.style.opacity=0;
  const els=F.nodes.map(n=>{
   const d=document.createElement('div'); d.className='nd';
   d.style.left=n.x+'%'; d.style.top=n.y+'%';
   d.innerHTML=`<span class="ico">${n.ico}</span><span><b>${n.b}</b><br><i>${n.i}</i></span>`;
   cv.appendChild(d); return d;});
  for(const d of els){ if(stop)return; d.classList.add('on'); await wait(210); }
  const paths=[];
  for(const [a,b] of F.edges){
   const A=pos(F.nodes[a]), B=pos(F.nodes[b]);
   const p=document.createElementNS('http://www.w3.org/2000/svg','path');
   const mx=(A.x+B.x)/2;
   p.setAttribute('d',`M${A.x} ${A.y} C ${mx} ${A.y}, ${mx} ${B.y}, ${B.x} ${B.y}`);
   p.setAttribute('class','edge'); svg.appendChild(p);
   p.style.setProperty('--L',Math.ceil(p.getTotalLength()));
   paths.push({p,a,b}); await wait(90); p.classList.add('on');
  }
  await wait(700); if(stop)return;
  capL.textContent="Exécution";
  els[0].classList.add('run');
  for(const {p,b} of paths){
   if(stop)return;
   p.classList.add('live'); tok.style.opacity=1;
   const L=p.getTotalLength(), t0=performance.now(), D=620;
   await new Promise(res=>{(function s(now){
     const k=Math.min(1,(now-t0)/D), pt=p.getPointAtLength(k*L);
     tok.style.left=pt.x+'px'; tok.style.top=pt.y+'px';
     k<1?requestAnimationFrame(s):res();})(t0)});
   els[b].classList.add('run');
   await wait(120);
   els[b].classList.add('ok'); els[b].querySelector('.ico').textContent='✓';
  }
  tok.style.opacity=0; els.forEach(e=>e.classList.add('ok'));
  capL.textContent=F.name+" · terminé";
  await wait(2200); if(stop)return;
  els.forEach((e,i)=>setTimeout(()=>e.classList.remove('on'),i*60));
  svg.querySelectorAll('.edge').forEach(p=>p.classList.remove('on'));
  await wait(700);
 }
 (async function loop(){let i=0;while(true){if(!stop)await play(i++%FLOWS.length);else await wait(400);}})();
})();

/* ══ B · le journal d'exécution ═══════════════════════════════════════════ */
(function(){
 const log=document.getElementById('log'); if(!log)return;
 const cnt=document.getElementById('cnt');
 const L=[
  ["Demande entrante qualifiée","chantier de rénovation, budget annoncé","Traité"],
  ["Devis 3 150 € relancé","deuxième relance, ouvert deux fois","Traité"],
  ["Compte rendu d'appel classé","fiche client à jour, rappel lundi","Traité"],
  ["Appel manqué rattrapé","SMS envoyé dans la minute","Traité"],
  ["Facture fournisseur classée","personne dérangé","Traité"],
  ["Devis 21 600 € sans réponse","trop gros pour un mail","À vous",1],
  ["Reporting hebdomadaire mis à jour","chiffre signé, devis en cours","Traité"],
  ["Ligne de tableur synchronisée","plus de double saisie","Traité"],
  ["Réclamation détectée","marquée sensible, aucune réponse auto","À vous",1],
  ["Rendez-vous confirmé","jeudi 14h, ajouté à l'agenda","Traité"]];
 let i=0,n=0,stop=false;
 new IntersectionObserver(e=>{stop=!e[0].isIntersecting},{threshold:.15}).observe(log);
 function hhmm(){const d=new Date();return String(d.getHours()).padStart(2,'0')+':'+String(d.getMinutes()).padStart(2,'0')}
 function push(){
  if(stop||document.hidden)return;
  const [m,e,s,you]=L[i++%L.length];
  const el=document.createElement('div');
  el.className='ln'+(you?' you':'');
  el.innerHTML=`<span class="t">${hhmm()}</span><span class="m">${m} <em>· ${e}</em></span><span class="s">${s}</span>`;
  log.prepend(el);
  while(log.children.length>9)log.lastChild.remove();
  if(!you){n++;cnt.textContent=n+" traités aujourd'hui"}
 }
 push();setInterval(push,1500);
})();

/* ══ C · la file qui se vide ══════════════════════════════════════════════ */
(function(){
 const qin=document.getElementById('qin'); if(!qin)return;
 const qout=document.getElementById('qout'), qn=document.getElementById('qn'), dn=document.getElementById('dn');
 const ITEMS=[
  ["Demande de devis","formulaire du site"],["Appel manqué","19:20"],["Devis à relancer","8 400 €"],
  ["Compte rendu à écrire","appel de 14 min"],["Facture fournisseur","à classer"],["Ligne à recopier","tableur de suivi"],
  ["Devis à relancer","3 150 €"],["Réclamation","livraison en retard",1],["Rappel à programmer","jeudi"],
  ["Reporting","semaine 37"],["Devis 21 600 €","21 jours sans réponse",1],["Demande de devis","par téléphone"]];
 let k=0,done=0,stop=false;
 new IntersectionObserver(e=>{stop=!e[0].isIntersecting},{threshold:.15}).observe(qin);
 function card(t,s,you){const d=document.createElement('div');d.className='card'+(you?' you':'');
  d.innerHTML=`${t}<small>${s}</small>`;return d}
 function fill(){while(qin.children.length<5){const [t,s,y]=ITEMS[k++%ITEMS.length];qin.appendChild(card(t,s,y))}
  qn.textContent=qin.children.length}
 fill();
 setInterval(()=>{
  if(stop||document.hidden||!qin.firstChild)return;
  const c=qin.firstChild;
  c.classList.add('fly');
  setTimeout(()=>{
   const you=c.classList.contains('you');
   c.remove(); fill();
   const d=card(c.textContent.replace(/(.+?)([a-z])([A-ZÀ-Ý])/, '$1$2 $3'),'',you);
   d.innerHTML=c.innerHTML;
   qout.prepend(d); while(qout.children.length>5)qout.lastChild.remove();
   done++; dn.textContent=done;
  },480);
 },1700);
})();
