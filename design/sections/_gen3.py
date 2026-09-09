exec(open('_gen.py').read().split('# ══ HÉRO')[0])

STEPS=[("Jour 0","Trente minutes au téléphone","Gratuit. Vous repartez avec quelque chose à appliquer seul."),
("Semaine 1","Une demi-journée sur place","Avec les gens qui font le travail. Vous recevez la liste chiffrée."),
("Semaines 2 à 4","Le premier système, en production","Construit, testé, il tourne dans vos comptes."),
("Ensuite","Vous décidez","Un autre, ou rien du tout. Rien ne se reconduit tout seul.")]

# A · quatre colonnes (actuel)
cols="".join(f'''<div style="padding-right:26px;{'border-left:1px solid #EBECEF;padding-left:26px;' if i else ''}">
 <div style="font-size:11.5px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:#2563EB;margin-bottom:14px">{a}</div>
 <div style="font-size:16.5px;font-weight:600;margin-bottom:7px;line-height:1.35">{b}</div>
 <div style="font-size:14.5px;color:#5B6270;line-height:1.55">{c}</div></div>''' for i,(a,b,c) in enumerate(STEPS))
w("StepA",f'''<div style="padding:44px 48px">
 <div class="eb">Comment ça démarre</div>
 <p class="h2" style="max-width:26ch"><span class="bl">Trois semaines</span> entre le premier appel et un système qui tourne.</p>
 <div style="height:1px;background:#2563EB;margin:34px 0 0"></div>
 <div style="display:grid;grid-template-columns:repeat(4,minmax(0,1fr));margin-top:26px">{cols}</div></div>''')

# B · frise verticale
rows="".join(f'''<div style="display:grid;grid-template-columns:120px 28px 1fr;gap:0;align-items:start">
 <div style="text-align:right;padding:0 22px 34px 0;font-size:11.5px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:#8A909B">{a}</div>
 <div style="position:relative;height:100%">
  <div style="position:absolute;left:50%;top:6px;bottom:0;width:1px;background:{'#EBECEF' if i==len(STEPS)-1 else '#2563EB'};transform:translateX(-50%)"></div>
  <div style="position:absolute;left:50%;top:6px;width:9px;height:9px;border-radius:99px;background:#2563EB;transform:translate(-50%,-50%);box-shadow:0 0 0 4px rgba(37,99,235,.14)"></div></div>
 <div style="padding:0 0 34px 22px"><div style="font-size:18px;font-weight:600;margin-bottom:5px">{b}</div>
 <div style="font-size:14.5px;color:#5B6270;line-height:1.55;max-width:52ch">{c}</div></div></div>''' for i,(a,b,c) in enumerate(STEPS))
w("StepB",f'''<div style="padding:44px 48px">
 <div class="eb">Comment ça démarre</div>
 <p class="h2" style="max-width:26ch"><span class="bl">Trois semaines</span> entre le premier appel et un système qui tourne.</p>
 <div style="margin-top:36px">{rows}</div></div>''')

# ══ COMPARATIF ════════════════════════════════════════════════════════════
VS=[("Tous les ans","Une fois"),("Congés, arrêts, turnover","Les nuits, les samedis, le mois d'août"),("Le savoir part avec la personne","Le savoir reste dans l'outil")]
r="".join(f'''<div style="display:grid;grid-template-columns:1fr 1fr;gap:32px;padding:26px 0;border-bottom:1px solid #F2F3F5">
 <b style="font-family:'Inter Tight';font-size:24px;font-weight:500;letter-spacing:-.03em;color:#8A909B;text-decoration:line-through;text-decoration-thickness:1px;text-decoration-color:#D6D9DE">{a}</b>
 <b style="font-family:'Inter Tight';font-size:24px;font-weight:500;letter-spacing:-.03em">{b}</b></div>''' for a,b in VS)
w("VsA",f'''<div style="padding:44px 48px">
 <div class="eb">Ce que ça remplace</div>
 <p class="h2" style="max-width:26ch">Comparez-le à <span class="bl">une embauche</span>. <span class="gy">Pas à un abonnement de plus.</span></p>
 <div style="margin-top:38px;border-top:1px solid #EBECEF">
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:32px;padding:16px 0;border-bottom:1px solid #EBECEF">
   <span style="font-size:11.5px;font-weight:600;letter-spacing:.16em;text-transform:uppercase;color:#8A909B">Embaucher</span>
   <span style="font-size:11.5px;font-weight:600;letter-spacing:.16em;text-transform:uppercase;color:#2563EB">Construire une fois</span></div>
  {r}</div></div>''')

w("VsB",'''<div style="padding:44px 48px">
 <div class="eb">Ce que ça remplace</div>
 <p class="h2" style="max-width:26ch">Comparez-le à <span class="bl">une embauche</span>. <span class="gy">Pas à un abonnement de plus.</span></p>
 <div style="display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-top:38px">
  <div style="border:1px solid #EBECEF;border-radius:16px;padding:28px;background:#FAFAFB">
   <div style="font-size:11.5px;font-weight:600;letter-spacing:.16em;text-transform:uppercase;color:#8A909B;margin-bottom:20px">Embaucher</div>
   <div style="font-size:17px;color:#8A909B;padding:12px 0;border-bottom:1px solid #EFF0F2">Un salaire, tous les ans</div>
   <div style="font-size:17px;color:#8A909B;padding:12px 0;border-bottom:1px solid #EFF0F2">Recruter, former, remplacer</div>
   <div style="font-size:17px;color:#8A909B;padding:12px 0;border-bottom:1px solid #EFF0F2">Congés, arrêts, turnover</div>
   <div style="font-size:17px;color:#8A909B;padding:12px 0">Le savoir part avec la personne</div></div>
  <div style="border:1px solid #0F1115;border-radius:16px;padding:28px">
   <div style="font-size:11.5px;font-weight:600;letter-spacing:.16em;text-transform:uppercase;color:#2563EB;margin-bottom:20px">Construire une fois</div>
   <div style="font-size:17px;font-weight:500;padding:12px 0;border-bottom:1px solid #F2F3F5">Une construction, puis c'est à vous</div>
   <div style="font-size:17px;font-weight:500;padding:12px 0;border-bottom:1px solid #F2F3F5">Rien à recruter</div>
   <div style="font-size:17px;font-weight:500;padding:12px 0;border-bottom:1px solid #F2F3F5">Les nuits, les samedis, le mois d'août</div>
   <div style="font-size:17px;font-weight:500;padding:12px 0">Le savoir reste dans l'outil</div></div>
 </div></div>''')

# ══ SCÈNE NOIRE ═══════════════════════════════════════════════════════════
IDEAS=["Répondre à la demande de 19h20.","Relancer chaque devis jusqu'à un oui ou un non.","Écrire le compte rendu avant l'appel suivant.","Supprimer la double saisie.","Remplacer le tableur que tout le monde attend.","Refaire le reporting, une bonne fois.","Trier la liste de demain pendant la nuit.","Ce que votre équipe fait deux fois par semaine en le détestant."]
w("DarkA",'''<div style="background:#0B0C0E;height:100%;box-sizing:border-box;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:48px">
 <div class="eb" style="color:#7FB0FB;margin-bottom:28px">Ce qu'on peut construire</div>
 <p style="font-family:'Inter Tight';font-weight:500;letter-spacing:-.04em;font-size:32px;color:#fff;margin:0 0 40px">Dites-nous ce qui mange <span style="color:#5B9DFF">votre semaine</span>.</p>
 <div style="font-size:11.5px;letter-spacing:.16em;color:#5C636E;margin-bottom:18px"><span style="color:#5B9DFF">03</span> / 08</div>
 <p style="font-family:'Inter Tight';font-weight:500;letter-spacing:-.035em;font-size:40px;color:#fff;margin:0;max-width:20ch;line-height:1.14">Écrire le compte rendu avant l'appel suivant.</p>
 <div style="width:300px;height:1px;background:rgba(255,255,255,.16);margin-top:52px;position:relative"><div style="position:absolute;left:0;top:0;height:100%;width:38%;background:#fff"></div></div>
</div>''')

grid="".join(f'''<div style="border:1px solid {'#2563EB' if i==2 else 'rgba(255,255,255,.10)'};border-radius:12px;padding:20px;background:{'rgba(37,99,235,.10)' if i==2 else 'transparent'}">
 <div style="font-size:11px;letter-spacing:.14em;color:{'#5B9DFF' if i==2 else '#5C636E'};margin-bottom:10px">0{i+1}</div>
 <div style="font-family:'Inter Tight';font-size:19px;font-weight:500;letter-spacing:-.03em;color:{'#fff' if i==2 else '#C8CDD5'};line-height:1.25">{x}</div></div>''' for i,x in enumerate(IDEAS))
w("DarkB",f'''<div style="background:#0B0C0E;height:100%;box-sizing:border-box;padding:44px 48px">
 <div class="eb" style="color:#7FB0FB">Ce qu'on peut construire</div>
 <p style="font-family:'Inter Tight';font-weight:500;letter-spacing:-.04em;font-size:32px;color:#fff;margin:14px 0 34px;max-width:24ch">Dites-nous ce qui mange <span style="color:#5B9DFF">votre semaine</span>.</p>
 <div style="display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:14px">{grid}</div></div>''')

# ══ TARIFS ET FIN ═════════════════════════════════════════════════════════
w("PriceA",'''<div style="padding:44px 48px">
 <div class="eb">Nos tarifs</div>
 <p class="h2" style="max-width:26ch">Un <span class="bl">prix fixe</span> à chaque étape. <span class="gy">Jamais de tarif journalier.</span></p>
 <div style="display:grid;grid-template-columns:repeat(3,minmax(0,1fr));margin-top:36px;border-top:1px solid #EBECEF">
  <div style="padding:30px 30px 0 0"><div style="font-size:11.5px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:#8A909B">Étape 01</div>
   <div style="font-family:'Inter Tight';font-size:34px;font-weight:500;letter-spacing:-.045em;margin:12px 0 4px">Une demi-journée</div>
   <div style="font-size:13.5px;color:#8A909B;padding-bottom:18px;border-bottom:1px solid #F2F3F5;margin-bottom:18px">Une semaine, déduite de la construction</div>
   <div style="font-size:16.5px;font-weight:600;margin-bottom:7px">On vient voir</div>
   <div style="font-size:14.5px;color:#5B6270;line-height:1.55">Avec les gens qui font le travail. Vous recevez la liste chiffrée des heures perdues.</div></div>
  <div style="padding:30px 30px 0;border-left:1px solid #EBECEF"><div style="font-size:11.5px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:#8A909B">Étape 02</div>
   <div style="font-family:'Inter Tight';font-size:34px;font-weight:500;letter-spacing:-.045em;margin:12px 0 4px">Trois semaines</div>
   <div style="font-size:13.5px;color:#8A909B;padding-bottom:18px;border-bottom:1px solid #F2F3F5;margin-bottom:18px">Prix fixe, convenu avant la première ligne</div>
   <div style="font-size:16.5px;font-weight:600;margin-bottom:7px">La construction</div>
   <div style="font-size:14.5px;color:#5B6270;line-height:1.55">Un système à la fois, chacun avec son prix ferme et sa date.</div></div>
  <div style="padding:30px 0 0 30px;border-left:1px solid #EBECEF"><div style="font-size:11.5px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:#8A909B">Étape 03</div>
   <div style="font-family:'Inter Tight';font-size:34px;font-weight:500;letter-spacing:-.045em;margin:12px 0 4px">Au mois</div>
   <div style="font-size:13.5px;color:#8A909B;padding-bottom:18px;border-bottom:1px solid #F2F3F5;margin-bottom:18px">Optionnel, résiliable à tout moment</div>
   <div style="font-size:16.5px;font-weight:600;margin-bottom:7px">On garde un œil</div>
   <div style="font-size:14.5px;color:#5B6270;line-height:1.55">Surveillance, corrections, règles ajustées quand l'activité change.</div></div>
 </div></div>''')

w("PriceB",'''<div style="padding:44px 48px">
 <div class="eb">Nos tarifs</div>
 <p class="h2" style="max-width:26ch">Un <span class="bl">prix fixe</span> à chaque étape. <span class="gy">Jamais de tarif journalier.</span></p>
 <div style="display:flex;align-items:stretch;border:1px solid #EBECEF;border-radius:16px;overflow:hidden;margin-top:36px">
  <div style="flex:1;padding:28px"><div style="display:flex;align-items:center;gap:10px;margin-bottom:14px"><span style="width:22px;height:22px;border-radius:99px;background:#0F1115;color:#fff;font-size:11px;display:grid;place-items:center;font-weight:600">1</span><span style="font-size:15.5px;font-weight:600">On vient voir</span></div>
   <div style="font-size:14px;color:#5B6270;line-height:1.55">Une demi-journée sur place, la liste chiffrée sous une semaine, déduite ensuite.</div></div>
  <div style="width:1px;background:#EBECEF"></div>
  <div style="flex:1;padding:28px;background:#FAFBFF"><div style="display:flex;align-items:center;gap:10px;margin-bottom:14px"><span style="width:22px;height:22px;border-radius:99px;background:#2563EB;color:#fff;font-size:11px;display:grid;place-items:center;font-weight:600">2</span><span style="font-size:15.5px;font-weight:600">La construction</span></div>
   <div style="font-size:14px;color:#5B6270;line-height:1.55">Trois semaines par système, prix ferme convenu avant la première ligne de code.</div></div>
  <div style="width:1px;background:#EBECEF"></div>
  <div style="flex:1;padding:28px"><div style="display:flex;align-items:center;gap:10px;margin-bottom:14px"><span style="width:22px;height:22px;border-radius:99px;background:#0F1115;color:#fff;font-size:11px;display:grid;place-items:center;font-weight:600">3</span><span style="font-size:15.5px;font-weight:600">On garde un œil</span></div>
   <div style="font-size:14px;color:#5B6270;line-height:1.55">Au mois, optionnel, résiliable à tout moment.</div></div>
 </div>
 <div style="display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:28px;margin-top:28px;padding-top:26px;border-top:1px solid #EBECEF">
  <div><b style="font-size:15px">Le premier appel ne coûte rien</b><div style="font-size:14px;color:#5B6270;margin-top:3px">Trente minutes, et vous gardez ce qui en sort.</div></div>
  <div><b style="font-size:15px">La visite est déduite</b><div style="font-size:14px;color:#5B6270;margin-top:3px">Si vous continuez, elle vient en déduction.</div></div>
  <div><b style="font-size:15px">Vous arrêtez quand vous voulez</b><div style="font-size:14px;color:#5B6270;margin-top:3px">Aucune durée minimum.</div></div>
 </div></div>''')

w("EndA",'''<div style="padding:64px 48px;text-align:center">
 <p class="h2" style="font-size:40px;max-width:22ch;margin:0 auto">Quel poste <span class="bl">n'arrivez-vous pas</span> <span class="gy">à ouvrir cette année ?</span></p>
 <p class="p" style="max-width:46ch;margin:22px auto 0">Dites-nous ce que vous faites et combien vous êtes. On répond dans la journée.</p>
 <div style="display:flex;gap:12px;justify-content:center;margin-top:32px"><span class="btn">contact@celeritas.agency →</span><span class="btn2">Appeler</span></div></div>''')

w("EndB",'''<div style="background:#0B0C0E;height:100%;box-sizing:border-box;padding:64px 48px;display:flex;flex-direction:column;justify-content:center">
 <p style="font-family:'Inter Tight';font-weight:500;letter-spacing:-.04em;font-size:40px;color:#fff;margin:0;max-width:20ch;line-height:1.12">Quel poste <span style="color:#5B9DFF">n'arrivez-vous pas</span> <span style="color:#7C838E">à ouvrir cette année ?</span></p>
 <div style="display:flex;gap:12px;align-items:center;margin-top:34px;max-width:560px">
  <div style="flex:1;border:1px solid rgba(255,255,255,.16);border-radius:999px;padding:15px 22px;color:#6E757F;font-size:15px">Ce que vous faites, et combien vous êtes</div>
  <span class="btn" style="background:#fff;color:#0B0C0E">Envoyer →</span></div>
 <p style="color:#7C838E;font-size:13.5px;margin-top:18px">On répond dans la journée. Le premier échange dure trente minutes et ne coûte rien.</p></div>''')
