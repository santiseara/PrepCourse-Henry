# -*- coding: utf-8 -*-
"""Inserts de producto de The Party Box Vault (mercado ingles, 2026-11-10).

Clonados de Moldes Prontos / caixinha cenario (page 1288335281030909), que mete en cada ad
la carpeta de PDFs con los moldes, la vista de Canva y los disenos por tema, con un chip
grande encima ("+100 MOLDES"). Se dibujan por codigo (HTML + Chrome headless), asi que no
hace falta que el producto exista todavia (regla del 2026-11-05).

Los moldes se dibujan como dielines en SVG, que es lo que se ve en el insert del ganador.

Cada insert sale sobre un lienzo 1.10x con el sobrante desenfocado, porque el editor le mete
a las fotos fijas un zoom de 1.0 a 1.14 mas un golpe de 1.16 por corte.

Uso: python3 gfx_boxes.py
"""
import os, subprocess
from PIL import Image, ImageFilter

OUT = os.path.expanduser('~/Desktop/party-box-vault/anuncios/work/gfx')
os.makedirs(OUT, exist_ok=True)
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
W, H = 1080, 1920
MW, MH = 1188, 2112            # 1.10x

PAPEL, TINTA, ROSA, GRIS, ORO = '#FBF4EE', '#2A1D24', '#D94F70', '#786068', '#C9983A'
FONDO = '#241820'

FONTS = ('<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,500;0,9..144,700;1,9..144,600'
         '&family=Inter:wght@400;600;700;800;900&display=swap" rel="stylesheet">')

BASE = f"""<style>
*{{margin:0;padding:0;box-sizing:border-box;font-family:Fraunces,Georgia,serif}}
body{{width:{W}px;height:{H}px;background:{FONDO};display:flex;align-items:center;justify-content:center;overflow:hidden}}
body:before{{content:"";position:absolute;inset:0;background:radial-gradient(circle at 50% 32%,rgba(217,79,112,.26),transparent 66%)}}
.hoja{{position:relative;width:980px;background:{PAPEL};padding:64px 56px 56px;border-radius:8px;
 box-shadow:0 44px 90px rgba(0,0,0,.55)}}
.kick{{font-family:Inter,sans-serif;font-size:24px;letter-spacing:5px;font-weight:800;color:{ROSA};text-align:center}}
h1{{font-size:70px;line-height:1.02;color:{TINTA};margin-top:12px;text-align:center;letter-spacing:-1px}}
h1 em{{font-style:italic;color:{ROSA}}}
.hr{{height:3px;background:{TINTA};opacity:.12;margin:28px 0}}
.pill{{display:inline-block;background:{ROSA};color:#fff;font-family:Inter,sans-serif;font-weight:800;
 font-size:24px;letter-spacing:3px;padding:12px 26px;border-radius:30px}}
.ctr{{text-align:center}}
</style>"""


def hoja(cuerpo, extra=''):
    return f"""<!doctype html><html><head><meta charset="utf-8">{FONTS}{BASE}{extra}</head><body>
<div class="hoja">{cuerpo}</div></body></html>"""


# --- dielines: lo que se ve en la carpeta de moldes del ganador ----------------------------
def dieline(c1, c2, kind):
    """Molde de caja dibujado en SVG. kind: 0 favor box, 1 explosion, 2 gable, 3 drawer."""
    if kind == 0:      # caja con tapa y solapas
        body = (f'<path d="M30 60 h60 v-30 h60 v30 h60 v120 h-60 v30 h-60 v-30 h-60 Z" fill="{c1}" opacity=".30"/>'
                f'<path d="M30 60 h180 v120 h-180 Z" fill="{c1}" opacity=".55"/>'
                f'<path d="M90 30 h60 v30 h-60 Z M90 180 h60 v30 h-60 Z" fill="{c2}" opacity=".7"/>'
                f'<path d="M30 60 h180 v120 h-180 Z M90 30 v180 M150 30 v180" fill="none" stroke="{c2}" stroke-width="3"/>'
                f'<path d="M30 60 h-18 v120 h18 M210 60 h18 v120 h-18" fill="none" stroke="{c2}" stroke-width="3" stroke-dasharray="7 6"/>')
    elif kind == 1:    # caja explosion: cruz de 5 caras
        body = (f'<path d="M90 30 h60 v60 h60 v60 h-60 v60 h-60 v-60 h-60 v-60 h60 Z" fill="{c1}" opacity=".45"/>'
                f'<path d="M90 90 h60 v60 h-60 Z" fill="{c2}" opacity=".65"/>'
                f'<path d="M90 30 h60 v60 h60 v60 h-60 v60 h-60 v-60 h-60 v-60 h60 Z" fill="none" stroke="{c2}" stroke-width="3"/>'
                f'<path d="M90 90 h60 M90 150 h60 M90 90 v60 M150 90 v60" fill="none" stroke="{c2}" stroke-width="3" stroke-dasharray="7 6"/>')
    elif kind == 2:    # gable box / maletita con manija
        body = (f'<path d="M24 70 h192 v110 h-192 Z" fill="{c1}" opacity=".5"/>'
                f'<path d="M24 70 l48 -40 h96 l48 40 Z" fill="{c2}" opacity=".55"/>'
                f'<path d="M24 70 h192 v110 h-192 Z M24 70 l48 -40 h96 l48 40" fill="none" stroke="{c2}" stroke-width="3"/>'
                f'<path d="M104 44 a16 10 0 0 1 32 0" fill="none" stroke="{c2}" stroke-width="4"/>'
                f'<path d="M72 30 v150 M168 30 v150" fill="none" stroke="{c2}" stroke-width="3" stroke-dasharray="7 6"/>')
    else:              # caja con gaveta
        body = (f'<path d="M36 40 h168 v160 h-168 Z" fill="{c1}" opacity=".35"/>'
                f'<path d="M56 70 h128 v100 h-128 Z" fill="{c2}" opacity=".55"/>'
                f'<circle cx="120" cy="120" r="12" fill="{PAPEL}"/>'
                f'<path d="M36 40 h168 v160 h-168 Z M56 70 h128 v100 h-128 Z" fill="none" stroke="{c2}" stroke-width="3"/>'
                f'<path d="M36 70 h20 M184 70 h20 M36 170 h20 M184 170 h20" stroke="{c2}" stroke-width="3"/>')
    return f'<svg viewBox="0 0 240 240" width="100%" height="100%">{body}</svg>'


TEMAS = [
    ('Birthday', '#D94F70', '#8E2E49', 0), ('Baby shower', '#7FA9C4', '#355C77', 1),
    ('Christening', '#C9983A', '#7A5A16', 2), ('Dinosaurs', '#6FA06B', '#2F5B2C', 0),
    ('Unicorns', '#B88BC9', '#5F3A6E', 1), ('Football', '#4A6EA8', '#223A61', 3),
    ('Christmas', '#C0463C', '#751F18', 0), ('Valentine', '#E0768F', '#92324A', 1),
    ('Graduation', '#3F4B63', '#1E2634', 2), ('Mermaids', '#58A8A0', '#1F5E58', 0),
    ('Cars', '#D08A3A', '#8A5212', 3), ('Easter', '#CBB76B', '#7E6D24', 1),
]

LIBRERIA = hoja(f"""
  <div class="kick">INSIDE THE VAULT</div>
  <h1>300+ party box <em>templates</em></h1>
  <div class="ctr" style="margin-top:16px"><span class="pill">SORTED BY THEME &middot; ALREADY MEASURED</span></div>
  <div class="hr"></div>
  <div class="gr">""" + ''.join(
    f"""<div class="p"><div class="im">{dieline(c1, c2, k)}</div><b>{t}</b><span>PDF &middot; A4 + Letter</span></div>"""
    for t, c1, c2, k in TEMAS) + f"""
  </div>
  <div class="tip"><b>EVERY FILE</b> prints on a normal printer, cuts with scissors, folds in about ten minutes.</div>
""", extra=f"""<style>
.gr{{display:grid;grid-template-columns:repeat(4,1fr);gap:18px}}
.p{{background:#fff;border:2px solid #EFE2DA;border-radius:10px;padding:12px 10px 14px;text-align:center}}
.p .im{{height:150px;background:#FDF8F4;border-radius:7px;display:flex;align-items:center;justify-content:center;padding:8px}}
.p b{{display:block;font-family:Inter,sans-serif;font-size:21px;font-weight:800;color:{TINTA};margin-top:9px}}
.p span{{display:block;font-family:Inter,sans-serif;font-size:16px;color:{GRIS};margin-top:2px}}
.tip{{margin-top:26px;background:#FBEDE6;border-left:8px solid {ROSA};padding:20px 22px;font-family:Inter,sans-serif;
 font-size:24px;color:{TINTA};line-height:1.35;border-radius:0 8px 8px 0}}
.tip b{{color:{ROSA};font-weight:900;letter-spacing:1px;margin-right:6px}}
</style>""")


# --- 2) lo que hay adentro, en el celular -------------------------------------------------
IND = [('01', '300+ box templates', 'Every theme, already measured'),
       ('02', 'Step by step assembly video', 'Watch once, fold it right'),
       ('03', 'The First Sale Kit', 'What to make first and who to show'),
       ('04', '100 ready messages', 'Copy, paste, answer the price question'),
       ('05', '30 day posting planner', 'What to post, every day'),
       ('06', 'Editable on your phone', 'Change a name in two taps')]

CELULAR = f"""<!doctype html><html><head><meta charset="utf-8">{FONTS}{BASE}
<style>
body{{background:{FONDO}}}
.tel{{position:relative;width:700px;height:1440px;background:#120C10;border-radius:66px;padding:16px;
 box-shadow:0 50px 90px rgba(0,0,0,.6);border:3px solid #3E2F38}}
.scr{{width:100%;height:100%;background:{PAPEL};border-radius:52px;overflow:hidden;padding:60px 38px}}
.notch{{position:absolute;left:50%;transform:translateX(-50%);top:26px;width:170px;height:30px;background:#120C10;border-radius:18px;z-index:3}}
.k{{font-family:Inter,sans-serif;font-size:19px;letter-spacing:4px;font-weight:800;color:{ROSA};text-align:center}}
.t{{font-size:52px;color:{TINTA};text-align:center;margin:10px 0 8px;line-height:1.05}}
.t em{{font-style:italic;color:{ROSA}}}
.ln{{height:3px;background:{TINTA};opacity:.12;margin:18px 0}}
.it{{display:flex;gap:16px;align-items:flex-start;padding:20px 0;border-bottom:2px solid #F0E3DB}}
.it i{{flex:none;width:46px;height:46px;border-radius:10px;background:{ROSA};color:#fff;font-style:normal;
 font-family:Inter,sans-serif;font-weight:900;font-size:20px;display:flex;align-items:center;justify-content:center}}
.it b{{display:block;font-family:Inter,sans-serif;font-size:28px;font-weight:800;color:{TINTA};line-height:1.15}}
.it span{{display:block;font-family:Inter,sans-serif;font-size:22px;color:{GRIS};margin-top:4px}}
.bt{{margin-top:24px;background:{ROSA};color:#fff;font-family:Inter,sans-serif;font-weight:900;font-size:26px;
 letter-spacing:1px;text-align:center;padding:22px;border-radius:40px}}
</style></head><body>
<div class="tel"><div class="notch"></div><div class="scr">
  <div class="k">THE PARTY BOX VAULT</div>
  <div class="t">Everything <em>inside</em></div>
  <div class="ln"></div>
  {''.join(f'<div class="it"><i>{n}</i><div><b>{t}</b><span>{s}</span></div></div>' for n, t, s in IND)}
  <div class="bt">INSTANT DOWNLOAD</div>
</div></div></body></html>"""


# --- 3) la pagina de armado paso a paso ---------------------------------------------------
PASOS = [('Pick the theme', 'Twelve families, one file each'),
         ('Print on card stock', 'Any home printer, A4 or Letter'),
         ('Cut the outline', 'Scissors work, no cutting machine'),
         ('Score the dashed lines', 'This is why it closes clean'),
         ('Fold and glue two tabs', 'Four minutes once you have done one'),
         ('Fill it and tie the bow', 'Ready to hand over')]

ARMADO = hoja(f"""
  <div class="kick">ITEM 02</div>
  <h1>The assembly <em>video</em></h1>
  <div class="ctr" style="margin-top:14px"><span class="pill">NO CUTTING MACHINE NEEDED</span></div>
  <div class="hr"></div>
  <div class="st">""" + ''.join(
    f"""<div class="s"><div class="im">{dieline(TEMAS[i][1], TEMAS[i][2], i % 4)}</div>
        <div class="tx"><i>{i+1}</i><b>{t}</b><span>{s}</span></div></div>""" for i, (t, s) in enumerate(PASOS)) + """
  </div>
""", extra=f"""<style>
.st{{display:flex;flex-direction:column;gap:14px}}
.s{{display:flex;gap:18px;align-items:center;background:#fff;border:2px solid #EFE2DA;border-radius:10px;padding:12px 16px}}
.s .im{{flex:none;width:118px;height:118px;background:#FDF8F4;border-radius:8px;padding:6px}}
.s .tx{{position:relative;padding-left:62px}}
.s i{{position:absolute;left:0;top:2px;width:46px;height:46px;border-radius:50%;background:{ROSA};color:#fff;font-style:normal;
 font-family:Inter,sans-serif;font-weight:900;font-size:24px;display:flex;align-items:center;justify-content:center}}
.s b{{display:block;font-family:Inter,sans-serif;font-size:32px;font-weight:800;color:{TINTA}}}
.s span{{display:block;font-family:Inter,sans-serif;font-size:23px;color:{GRIS};margin-top:3px}}
</style>""")


# --- 4) el calendario de la demanda -------------------------------------------------------
MESES = [('JAN', 'Birthdays'), ('FEB', "Valentine's"), ('MAR', 'Baby showers'), ('APR', 'Easter'),
         ('MAY', 'Communions'), ('JUN', 'Weddings'), ('JUL', 'Summer parties'), ('AUG', 'Back to school'),
         ('SEP', 'Christenings'), ('OCT', 'Halloween'), ('NOV', 'Thanksgiving'), ('DEC', 'Christmas')]

CALENDARIO = hoja(f"""
  <div class="kick">WHY IT NEVER STOPS</div>
  <h1>A product with <em>no season</em></h1>
  <div class="hr"></div>
  <div class="cal">""" + ''.join(
    f"""<div class="m"><i>{m}</i><b>{t}</b></div>""" for m, t in MESES) + f"""
  </div>
  <div class="tip"><b>EVERY ONE OF THEM</b> ends with somebody handing a little box to every guest at the door.</div>
""", extra=f"""<style>
.cal{{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}}
.m{{background:#fff;border:2px solid #EFE2DA;border-radius:10px;padding:22px 14px;text-align:center}}
.m i{{display:block;font-style:normal;font-family:Inter,sans-serif;font-size:22px;letter-spacing:3px;font-weight:900;color:{ROSA}}}
.m b{{display:block;font-family:Inter,sans-serif;font-size:27px;font-weight:800;color:{TINTA};margin-top:8px}}
.tip{{margin-top:28px;background:#FBEDE6;border-left:8px solid {ROSA};padding:22px;font-family:Inter,sans-serif;
 font-size:26px;color:{TINTA};line-height:1.35;border-radius:0 8px 8px 0}}
.tip b{{color:{ROSA};font-weight:900;letter-spacing:1px;margin-right:6px}}
</style>""")


def shot(html, name):
    p = f'{OUT}/_{name}.html'
    open(p, 'w').write(html)
    subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--hide-scrollbars',
                    f'--window-size={W},{H}', f'--screenshot={OUT}/_{name}.png',
                    '--virtual-time-budget=8000', 'file://' + p], check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    im = Image.open(f'{OUT}/_{name}.png').convert('RGB').resize((W, H), Image.LANCZOS)
    bg = im.resize((MW, MH), Image.LANCZOS).filter(ImageFilter.GaussianBlur(28))
    bg = Image.blend(bg, Image.new('RGB', (MW, MH), (36, 24, 32)), 0.38)
    bg.paste(im, ((MW - W) // 2, (MH - H) // 2))
    bg.save(f'{OUT}/{name}.png')
    os.remove(f'{OUT}/_{name}.html'); os.remove(f'{OUT}/_{name}.png')
    print(f'{OUT}/{name}.png')


def shot_alpha(html, name):
    p = f'{OUT}/_{name}.html'
    open(p, 'w').write(html.replace(f'background:{FONDO}', 'background:transparent')
                           .replace('body:before{content:"";position:absolute;inset:0;background:radial-gradient(circle at 50% 32%,rgba(217,79,112,.26),transparent 66%)}', ''))
    subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--hide-scrollbars',
                    '--default-background-color=00000000',
                    f'--window-size={W},{H}', f'--screenshot={OUT}/{name}.png',
                    '--virtual-time-budget=8000', 'file://' + p], check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    im = Image.open(f'{OUT}/{name}.png').convert('RGBA')
    bb = im.getbbox()
    if bb: im.crop(bb).save(f'{OUT}/{name}.png')
    os.remove(f'{OUT}/_{name}.html')
    print(f'{OUT}/{name}.png')


if __name__ == '__main__':
    for html, name in [(LIBRERIA, 'libreria'), (CELULAR, 'celular'),
                       (ARMADO, 'armado'), (CALENDARIO, 'calendario')]:
        shot(html, name)
    shot_alpha(CELULAR, 'celular_solo')
