exec(open('_gen.py').read().split('# ══ HÉRO')[0])

CAPS=[("Demandes entrantes","Mail, formulaire, appel manqué. Qualifié, orienté, répondu dans la minute."),
("Suivi des devis","Relancés au bon moment. Et il vous dit lesquels méritent un appel."),
("Comptes rendus","Écrits et classés avant l'appel suivant."),
("Double saisie","Saisi une fois. Le devis, le tableur et la compta suivent."),
("Reporting","À jour en permanence. Plus personne ne colle d'exports."),
("Ce qui n'appartient qu'à vous","Les deux ou trois tâches absurdes que seule votre entreprise a.")]

# A · cartes avec icônes (l'actuel)
cards="".join(f'''<div style="border:1px solid #EBECEF;border-radius:14px;padding:24px">
 <div style="width:34px;height:34px;border-radius:10px;background:#EFF5FF;margin-bottom:14px"></div>
 <div style="font-size:16.5px;font-weight:600;margin-bottom:7px">{t}</div>
 <div style="font-size:14.5px;color:#5B6270;line-height:1.55">{d}</div></div>''' for t,d in CAPS)
w("CapA",f'''<div style="padding:44px 48px">
 <div class="eb">Ce qu'il prend en charge</div>
 <p class="h2" style="max-width:24ch">Le travail que <span class="bl">personne n'a le temps</span> de faire correctement.</p>
 <div style="display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px;margin-top:36px">{cards}</div></div>''')

# B · liste éditoriale
lines="".join(f'''<div style="display:grid;grid-template-columns:38px 1fr auto;gap:20px;align-items:baseline;padding:22px 0;border-bottom:1px solid #F2F3F5">
 <span style="font-size:12px;font-weight:600;color:#C3C7CE;font-variant-numeric:tabular-nums">0{i+1}</span>
 <div><div style="font-family:'Inter Tight';font-size:22px;font-weight:500;letter-spacing:-.03em">{t}</div>
 <div style="font-size:14.5px;color:#5B6270;margin-top:4px">{d}</div></div>
 <span style="width:7px;height:7px;border-radius:99px;background:#2563EB;opacity:{.25+i*.15:.2f}"></span></div>''' for i,(t,d) in enumerate(CAPS))
w("CapB",f'''<div style="padding:44px 48px">
 <div class="eb">Ce qu'il prend en charge</div>
 <p class="h2" style="max-width:24ch">Le travail que <span class="bl">personne n'a le temps</span> de faire correctement.</p>
 <div style="margin-top:30px">{lines}</div></div>''')

# C · bento
w("CapC",f'''<div style="padding:44px 48px">
 <div class="eb">Ce qu'il prend en charge</div>
 <p class="h2" style="max-width:24ch">Le travail que <span class="bl">personne n'a le temps</span> de faire correctement.</p>
 <div style="display:grid;grid-template-columns:repeat(4,minmax(0,1fr));grid-auto-rows:132px;gap:14px;margin-top:34px">
  <div style="grid-column:span 2;grid-row:span 2;border-radius:16px;background:#0F1115;color:#fff;padding:26px;display:flex;flex-direction:column;justify-content:flex-end">
   <div style="font-family:'Inter Tight';font-size:26px;font-weight:500;letter-spacing:-.03em">Demandes entrantes</div>
   <div style="font-size:14.5px;color:#A8AFBA;margin-top:8px;max-width:26ch">Mail, formulaire, appel manqué. Qualifié, orienté, répondu dans la minute au lieu du lendemain.</div></div>
  <div style="grid-column:span 2;border-radius:16px;background:#EFF5FF;padding:22px">
   <div style="font-size:17px;font-weight:600;color:#1D4ED8">Suivi des devis</div>
   <div style="font-size:14px;color:#3B6BC4;margin-top:6px">Relancés au bon moment, et il vous dit lesquels méritent un appel.</div></div>
  <div style="border-radius:16px;border:1px solid #EBECEF;padding:20px"><div style="font-size:15.5px;font-weight:600">Comptes rendus</div><div style="font-size:13.5px;color:#5B6270;margin-top:5px">avant l'appel suivant</div></div>
  <div style="border-radius:16px;border:1px solid #EBECEF;padding:20px"><div style="font-size:15.5px;font-weight:600">Double saisie</div><div style="font-size:13.5px;color:#5B6270;margin-top:5px">saisi une seule fois</div></div>
  <div style="grid-column:span 2;border-radius:16px;border:1px solid #EBECEF;padding:20px"><div style="font-size:15.5px;font-weight:600">Reporting</div><div style="font-size:13.5px;color:#5B6270;margin-top:5px">à jour sans que personne y touche</div></div>
  <div style="grid-column:span 2;border-radius:16px;background:#F7F8FA;padding:20px"><div style="font-size:15.5px;font-weight:600">Ce qui n'appartient qu'à vous</div><div style="font-size:13.5px;color:#5B6270;margin-top:5px">les deux ou trois tâches absurdes que seule votre entreprise a</div></div>
 </div></div>''')

# ══ BRANCHEMENT ═══════════════════════════════════════════════════════════
w("PlugA",'''<div style="padding:44px 48px">
 <div class="eb">Comment ça se branche</div>
 <p class="h2" style="max-width:26ch">Le flux se <span class="bl">construit tout seul</span>, puis il s'exécute.</p>
 <div style="margin-top:34px;border:1px solid #EBECEF;border-radius:14px;height:280px;position:relative;background-image:radial-gradient(#EBECEF 1px,transparent 1px);background-size:22px 22px">
  <svg viewBox="0 0 780 280" style="position:absolute;inset:0;width:100%;height:100%" fill="none" stroke="#2563EB" stroke-width="1.8">
   <path d="M150 140 C 210 140, 210 72, 285 72"/><path d="M150 140 C 210 140, 210 208, 285 208"/>
   <path d="M455 72 C 520 72, 520 140, 570 140"/><path d="M455 208 C 520 208, 520 140, 570 140"/>
  </svg>
  <div style="position:absolute;left:60px;top:140px;transform:translate(-50%,-50%);background:#fff;border:1px solid #2563EB;border-radius:11px;padding:11px 14px;box-shadow:0 8px 22px -12px rgba(16,24,40,.3);white-space:nowrap">
   <div style="font-size:13.5px;font-weight:600">Appel manqué</div><div style="font-size:12px;color:#8A909B">19:20</div></div>
  <div style="position:absolute;left:370px;top:72px;transform:translate(-50%,-50%);background:#fff;border:1px solid #EBECEF;border-radius:11px;padding:11px 14px;white-space:nowrap">
   <div style="font-size:13.5px;font-weight:600">Qualifier</div><div style="font-size:12px;color:#8A909B">budget, délai</div></div>
  <div style="position:absolute;left:370px;top:208px;transform:translate(-50%,-50%);background:#fff;border:1px solid #EBECEF;border-radius:11px;padding:11px 14px;white-space:nowrap">
   <div style="font-size:13.5px;font-weight:600">Rappeler par SMS</div><div style="font-size:12px;color:#8A909B">dans la minute</div></div>
  <div style="position:absolute;left:660px;top:140px;transform:translate(-50%,-50%);background:#F6FCF9;border:1px solid #CBEBDC;border-radius:11px;padding:11px 14px;white-space:nowrap">
   <div style="font-size:13.5px;font-weight:600;color:#0F9960">Rendez-vous proposé ✓</div><div style="font-size:12px;color:#5B9C7E">jeudi 14h</div></div>
 </div>
 <p class="cap" style="margin-top:16px">Trois automatisations s'enchaînent en boucle, comme dans un outil de workflow.</p></div>''')

w("PlugB",'''<div style="padding:44px 48px">
 <div class="eb">Comment ça se branche</div>
 <p class="h2" style="max-width:26ch">Le travail défile <span class="bl">en direct</span>.</p>
 <div class="win" style="margin-top:34px">
  <div class="wbar" style="background:#F7F8FA"><span style="display:flex;align-items:center;gap:8px"><span style="width:6px;height:6px;border-radius:99px;background:#0F9960;display:block"></span>En cours d'exécution</span><span>47 traités aujourd'hui</span></div>
  <div class="row"><b>Demande entrante qualifiée</b><i>11:04</i><i>chantier de rénovation, budget annoncé</i><s>Traité</s></div>
  <div class="row"><b>Devis 3 150 € relancé</b><i>11:02</i><i>deuxième relance, ouvert deux fois</i><s>Traité</s></div>
  <div class="row"><b>Compte rendu d'appel classé</b><i>10:58</i><i>fiche à jour, rappel lundi</i><s>Traité</s></div>
  <div class="row"><b>Devis 21 600 € sans réponse</b><i>10:55</i><i>trop gros pour un mail</i><s class="you">À vous</s></div>
  <div class="row" style="opacity:.55"><b>Facture fournisseur classée</b><i>10:51</i><i>personne dérangé</i><s>Traité</s></div>
  <div class="row" style="opacity:.25;border-bottom:0"><b>Appel manqué rattrapé</b><i>10:47</i><i>SMS dans la minute</i><s>Traité</s></div>
 </div>
 <p class="cap" style="margin-top:16px">Aucun dessin. Les lignes tombent une par une, la plus ancienne s'efface.</p></div>''')

w("PlugC",'''<div style="padding:44px 48px">
 <div class="eb">Comment ça se branche</div>
 <p class="h2" style="max-width:26ch">La file <span class="bl">se vide</span> pendant que vous travaillez.</p>
 <div style="display:grid;grid-template-columns:1fr 1fr;border:1px solid #EBECEF;border-radius:14px;overflow:hidden;margin-top:34px;height:280px">
  <div style="padding:20px;border-right:1px solid #EBECEF">
   <div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:16px"><b style="font-size:13.5px">En attente</b><span style="font-family:'Inter Tight';font-size:26px;font-weight:500;letter-spacing:-.04em">5</span></div>
   <div style="border:1px solid #EBECEF;border-radius:10px;padding:11px 13px;margin-bottom:9px;font-size:13.5px">Demande de devis<small style="display:block;color:#8A909B;font-size:12px">formulaire du site</small></div>
   <div style="border:1px solid #EBECEF;border-radius:10px;padding:11px 13px;margin-bottom:9px;font-size:13.5px">Appel manqué<small style="display:block;color:#8A909B;font-size:12px">19:20</small></div>
   <div style="border:1px solid #EBECEF;border-radius:10px;padding:11px 13px;margin-bottom:9px;font-size:13.5px;opacity:.6">Devis à relancer<small style="display:block;color:#8A909B;font-size:12px">8 400 €</small></div>
   <div style="border:1px solid #EBECEF;border-radius:10px;padding:11px 13px;font-size:13.5px;opacity:.3">Compte rendu à écrire<small style="display:block;color:#8A909B;font-size:12px">appel de 14 min</small></div>
  </div>
  <div style="padding:20px;background:#FCFDFC">
   <div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:16px"><b style="font-size:13.5px">Traité</b><span style="font-family:'Inter Tight';font-size:26px;font-weight:500;letter-spacing:-.04em;color:#0F9960">31</span></div>
   <div style="border:1px solid #BBD5FF;background:#F3F8FF;border-radius:10px;padding:11px 13px;margin-bottom:9px;font-size:13.5px">Réclamation<small style="display:block;color:#3B6BC4;font-size:12px">livraison en retard · à vous</small></div>
   <div style="border:1px solid #CBEBDC;background:#F6FCF9;border-radius:10px;padding:11px 13px;margin-bottom:9px;font-size:13.5px">Facture fournisseur<small style="display:block;color:#5B9C7E;font-size:12px">classée</small></div>
   <div style="border:1px solid #CBEBDC;background:#F6FCF9;border-radius:10px;padding:11px 13px;font-size:13.5px;opacity:.6">Ligne à recopier<small style="display:block;color:#5B9C7E;font-size:12px">synchronisée</small></div>
  </div>
 </div>
 <p class="cap" style="margin-top:16px">Les cartes traversent l'écran une par une, les compteurs bougent.</p></div>''')
