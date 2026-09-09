import pathlib

HEAD = '''<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@400;500;600&family=Inter:wght@400;500;600&display=swap">
  <style>
    body{margin:0;background:#fff;font-family:Inter,system-ui,sans-serif;color:#0F1115;-webkit-font-smoothing:antialiased}
    a{color:#2563EB}a:hover{color:#1D4ED8}
    .eb{font-size:11.5px;font-weight:600;letter-spacing:.16em;text-transform:uppercase;color:#8A909B}
    .h1{font-family:'Inter Tight',Inter,sans-serif;font-weight:500;letter-spacing:-.045em;line-height:1.04;font-size:54px;margin:18px 0 0}
    .h2{font-family:'Inter Tight',Inter,sans-serif;font-weight:500;letter-spacing:-.04em;line-height:1.14;font-size:34px;margin:14px 0 0}
    .bl{color:#2563EB}.gy{color:#5B6270}
    .p{color:#5B6270;font-size:16px;line-height:1.6;margin:16px 0 0}
    .cap{color:#8A909B;font-size:13px;margin:0}
    .btn{display:inline-flex;align-items:center;gap:8px;background:#0F1115;color:#fff;border-radius:999px;padding:13px 24px;font-size:15px;font-weight:500}
    .btn2{display:inline-flex;align-items:center;gap:8px;background:#fff;color:#0F1115;border-radius:999px;padding:13px 24px;font-size:15px;font-weight:500;box-shadow:inset 0 0 0 1px #EBECEF}
    .win{border:1px solid #EBECEF;border-radius:14px;overflow:hidden;background:#fff}
    .wbar{padding:12px 16px;border-bottom:1px solid #F2F3F5;font-size:12.5px;color:#8A909B;display:flex;justify-content:space-between}
    .row{display:grid;grid-template-columns:1fr auto;gap:3px 12px;padding:13px 16px;border-bottom:1px solid #F2F3F5}
    .row b{font-size:14.5px;font-weight:500}
    .row i{font-style:normal;font-size:12.5px;color:#8A909B}
    .row s{grid-column:2;justify-self:end;text-decoration:none;font-size:11.5px;font-weight:600;color:#0F9960}
    .row s.you{color:#2563EB}
    .tabs{display:flex;gap:22px;font-size:14px;color:#8A909B;margin-bottom:20px}
    .tabs b{color:#0F1115;font-weight:500;border-bottom:1px solid #0F1115;padding-bottom:6px}
  </style>
</helmet>
'''
FOOT = "\n</x-dc>\n</body>\n</html>\n"

def w(name, body):
    pathlib.Path(name+".dc.html").write_text(HEAD+body+FOOT)

demo_rows = '''
      <div class="row"><b>Demande entrante qualifiée</b><i>08:12</i><i>chantier de rénovation, budget annoncé</i><s>Traité</s></div>
      <div class="row"><b>Compte rendu d'appel classé</b><i>09:41</i><i>fiche client à jour, rappel programmé</i><s>Traité</s></div>
      <div class="row"><b>Quatre devis relancés</b><i>10:00</i><i>une réponse, un rendez-vous jeudi</i><s>Traité</s></div>
      <div class="row"><b>Devis 21 600 €, 21 jours sans réponse</b><i>10:02</i><i>trop gros pour un mail</i><s class="you">À vous</s></div>'''

# ══ HÉRO ═══════════════════════════════════════════════════════════════════
w("Main", f'''<div style="padding:56px 56px 48px;text-align:center">
  <div class="eb">Un poste entier, pas un logiciel de plus</div>
  <p class="h1">Le poste que vous n'avez pas<br><span class="bl">les moyens d'embaucher</span>.</p>
  <p class="p" style="max-width:52ch;margin:24px auto 0">Il prend en charge le travail répétitif que votre équipe fait tous les jours, et ne vous rend que les décisions.</p>
  <div style="display:flex;gap:12px;justify-content:center;margin:32px 0 14px"><span class="btn">Prendre rendez-vous →</span><span class="btn2">Le voir tourner</span></div>
  <p class="cap" style="margin-bottom:34px">De dix à soixante personnes, sans informaticien.</p>
  <div class="win" style="text-align:left">
    <div class="wbar"><span>Mardi 8 septembre · travail traité</span><span>47 traités aujourd'hui</span></div>{demo_rows}
  </div>
</div>''')

w("HeroB", f'''<div style="padding:52px 56px;display:grid;grid-template-columns:minmax(0,42%) minmax(0,58%);gap:44px;align-items:center">
  <div>
    <div class="eb">Un poste entier</div>
    <p class="h1" style="font-size:44px">Le poste que vous n'avez pas <span class="bl">les moyens d'embaucher</span>.</p>
    <p class="p">Il prend en charge le travail répétitif que votre équipe fait tous les jours, et ne vous rend que les décisions.</p>
    <div style="display:flex;gap:10px;margin-top:28px"><span class="btn">Prendre rendez-vous →</span><span class="btn2">Le voir tourner</span></div>
    <p class="cap" style="margin-top:18px">De dix à soixante personnes, sans informaticien.</p>
  </div>
  <div class="win"><div class="wbar"><span>Mardi 8 · travail traité</span><span>47 aujourd'hui</span></div>{demo_rows}</div>
</div>''')

w("HeroC", f'''<div style="background:#0B0C0E;padding:56px 56px 0;color:#fff;height:100%;box-sizing:border-box">
  <div class="eb" style="color:#7FB0FB">Un poste entier, pas un logiciel de plus</div>
  <p class="h1" style="color:#fff;max-width:18ch">Le poste que vous n'avez pas <span style="color:#5B9DFF">les moyens d'embaucher</span>.</p>
  <p class="p" style="color:#A8AFBA;max-width:46ch">Il prend en charge le travail répétitif que votre équipe fait tous les jours, et ne vous rend que les décisions.</p>
  <div style="display:flex;gap:12px;margin:30px 0 40px"><span class="btn" style="background:#fff;color:#0B0C0E">Prendre rendez-vous →</span><span style="color:#A8AFBA;padding:13px 4px;font-size:15px">Le voir tourner</span></div>
  <div class="win" style="border-color:#26282C;background:#131519;margin:0 -12px">
    <div class="wbar" style="border-color:#212327;color:#6E757F"><span>Mardi 8 septembre · travail traité</span><span>47 traités</span></div>
    <div class="row" style="border-color:#1C1E22"><b style="color:#E8EAEE">Demande entrante qualifiée</b><i style="color:#6E757F">08:12</i><i style="color:#6E757F">envoyée au bon commercial</i><s style="color:#5BB98B">Traité</s></div>
    <div class="row" style="border-color:#1C1E22"><b style="color:#E8EAEE">Quatre devis relancés</b><i style="color:#6E757F">10:00</i><i style="color:#6E757F">un rendez-vous jeudi</i><s style="color:#5BB98B">Traité</s></div>
    <div class="row" style="border-color:#1C1E22"><b style="color:#E8EAEE">Devis 21 600 €, sans réponse</b><i style="color:#6E757F">10:02</i><i style="color:#6E757F">trop gros pour un mail</i><s class="you" style="color:#5B9DFF">À vous</s></div>
  </div>
</div>''')
