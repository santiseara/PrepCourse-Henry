# -*- coding: utf-8 -*-
"""Inserts de producto de Carteras Maison / el Metodo Riviera (Argentina, 2026-11-10).

Clonados de Maison Luxe Bags (maisonluxebags.impultienda.ar), que en cada ad mete la tapa del
libro apoyada sobre carteras reales, la pagina de moldes con grilla de modelos, la lista de
materiales y las tapas de los bonos. Se dibujan por codigo (HTML + Chrome headless), asi que
no hace falta que el producto exista (regla del 2026-11-05).

Las fotos salen de cuadros de los propios clips de TikTok del pool (fotos/p1.jpg..), igual que
el ganador. Cada insert sale sobre un lienzo 1.10x con el sobrante desenfocado, porque el editor
le mete a las fotos fijas un zoom de 1.0 a 1.14 mas un golpe de 1.16 por corte.

Uso: python3 gfx_carteras.py
"""
import os, subprocess
from PIL import Image, ImageFilter

OUT = os.path.expanduser('~/Desktop/carteras-maison/anuncios/work/gfx')
FOT = os.path.expanduser('~/Desktop/carteras-maison/anuncios/work/fotos')
os.makedirs(OUT, exist_ok=True)
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
W, H = 1080, 1920
MW, MH = 1188, 2112            # 1.10x

PAPEL, TINTA, ROSA, GRIS, VERDE = '#F7F3EC', '#1C1A19', '#D4356F', '#6E6862', '#2E7D53'
FONDO = '#15120F'

FONTS = ('<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,600'
         '&family=Inter:wght@400;600;700;800;900&display=swap" rel="stylesheet">')

BASE = f"""<style>
*{{margin:0;padding:0;box-sizing:border-box;font-family:'Cormorant Garamond',Georgia,serif}}
body{{width:{W}px;height:{H}px;background:{FONDO};display:flex;align-items:center;justify-content:center;overflow:hidden}}
body:before{{content:"";position:absolute;inset:0;background:radial-gradient(circle at 50% 35%,rgba(212,53,111,.20),transparent 65%)}}
.hoja{{position:relative;width:980px;background:{PAPEL};padding:64px 58px 56px;border-radius:6px;
 box-shadow:0 44px 90px rgba(0,0,0,.55)}}
.kick{{font-family:Inter,sans-serif;font-size:24px;letter-spacing:6px;font-weight:800;color:{ROSA};text-align:center}}
h1{{font-size:86px;line-height:1.0;color:{TINTA};margin-top:14px;text-align:center;letter-spacing:-1px;font-weight:600}}
h1 em{{font-style:italic;color:{ROSA}}}
.sub{{font-family:Inter,sans-serif;font-size:28px;color:{GRIS};margin-top:16px;line-height:1.4;text-align:center;font-weight:500}}
.hr{{height:3px;background:{TINTA};opacity:.12;margin:28px 0}}
.pill{{display:inline-block;background:{ROSA};color:#fff;font-family:Inter,sans-serif;font-weight:800;
 font-size:24px;letter-spacing:3px;padding:12px 26px;border-radius:30px}}
.ctr{{text-align:center}}
</style>"""


def foto(n, alto=300, extra=''):
    p = f'{FOT}/p{n}.jpg'
    if os.path.exists(p):
        return f'<div style="height:{alto}px;border-radius:8px;overflow:hidden;{extra}"><img src="file://{p}" style="width:100%;height:100%;object-fit:cover"></div>'
    return f'<div style="height:{alto}px;border-radius:8px;background:#E7DFD3;{extra}"></div>'


def hoja(cuerpo, extra=''):
    return f"""<!doctype html><html><head><meta charset="utf-8">{FONTS}{BASE}{extra}</head><body>
<div class="hoja">{cuerpo}</div></body></html>"""


# --- 1) la tapa del libro ------------------------------------------------------------------
TAPA = hoja(f"""
<div class="kick">250+ MOLDES PASO A PASO</div>
<h1>Carteras<br><em>Maison</em></h1>
<div class="sub">EL MÉTODO RIVIERA</div>
<div class="hr"></div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:18px">
  {foto(1, 330)}{foto(2, 330)}
</div>
<div style="margin-top:18px">{foto(3, 300)}</div>
<div class="ctr" style="margin-top:30px"><span class="pill">SIN MÁQUINA DE COSER</span></div>
""")

# --- 2) la pagina de moldes, con la grilla de capitulos -------------------------------------
CAPS = [('1', 'Clásicas de todos los días'), ('2', 'La Colección Riviera'), ('3', 'Vida y viaje'),
        ('4', 'Fiestas y ocasiones'), ('5', 'Maison Signature')]
MOLDES = hoja(f"""
<div class="kick">LO QUE HAY ADENTRO</div>
<h1>250+ moldes<br>en <em>5 capítulos</em></h1>
<div class="hr"></div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px">
  {''.join(foto(i, 250) for i in range(4, 8))}
</div>
<div style="margin-top:26px">
  {''.join(f'<div style="display:flex;gap:16px;align-items:center;padding:15px 0;border-bottom:2px solid #EAE2D5">'
           f'<i style="flex:none;width:44px;height:44px;border-radius:50%;background:{ROSA};color:#fff;font-style:normal;'
           f'font-family:Inter,sans-serif;font-weight:900;font-size:21px;display:flex;align-items:center;justify-content:center">{n}</i>'
           f'<b style="font-family:Inter,sans-serif;font-size:30px;font-weight:700;color:{TINTA}">{t}</b>'
           f'<span style="margin-left:auto;font-family:Inter,sans-serif;font-size:24px;color:{GRIS};font-weight:600">50 moldes</span></div>'
           for n, t in CAPS)}
</div>
""")

# --- 3) la lista de materiales --------------------------------------------------------------
MAT = [('Cañamazo plástico', 'Una plancha, firme, mantiene la forma'),
       ('Cordón náutico', 'Un rollo, en los colores que elijas'),
       ('Aguja de plástico', 'Sin punta: no se pincha nadie'),
       ('Tijera', 'La que ya tenés en casa'),
       ('Cierre y cadena', 'El terminado que la hace parecer de local')]
MATERIALES = hoja(f"""
<div class="kick">TU PRIMERA CARTERA</div>
<h1>Todo lo que<br><em>necesitás</em></h1>
<div class="hr"></div>
{''.join(f'<div style="display:flex;gap:18px;align-items:flex-start;padding:22px 0;border-bottom:2px solid #EAE2D5">'
         f'<i style="flex:none;width:46px;height:46px;border-radius:10px;background:{VERDE};color:#fff;font-style:normal;'
         f'font-family:Inter,sans-serif;font-weight:900;font-size:24px;display:flex;align-items:center;justify-content:center">✓</i>'
         f'<div><b style="display:block;font-family:Inter,sans-serif;font-size:32px;font-weight:800;color:{TINTA};line-height:1.15">{t}</b>'
         f'<span style="display:block;font-family:Inter,sans-serif;font-size:24px;color:{GRIS};margin-top:4px">{s}</span></div></div>'
         for t, s in MAT)}
<div class="ctr" style="margin-top:34px"><span class="pill">SIN CUERO · SIN MÁQUINA</span></div>
""")

# --- 4) las tapas de los bonos ---------------------------------------------------------------
BON = [('1', 'Mensajes listos para copiar y pegar'), ('2', 'Tu primera cartera en 3 días'),
       ('3', 'Dónde comprar los materiales'), ('4', 'La fórmula para ponerle precio'),
       ('5', 'El planificador del mes')]
BONOS = hoja(f"""
<div class="kick">SOLO HOY</div>
<h1>5 bonos<br><em>de regalo</em></h1>
<div class="hr"></div>
{''.join(f'<div style="display:flex;gap:18px;align-items:center;padding:24px 0;border-bottom:2px solid #EAE2D5">'
         f'<i style="flex:none;width:70px;height:92px;border-radius:6px;background:linear-gradient(160deg,{ROSA},#8E1F49);'
         f'color:#fff;font-style:normal;font-family:Inter,sans-serif;font-weight:900;font-size:34px;'
         f'display:flex;align-items:center;justify-content:center;box-shadow:0 10px 22px rgba(0,0,0,.25)">{n}</i>'
         f'<b style="font-family:Inter,sans-serif;font-size:31px;font-weight:700;color:{TINTA};line-height:1.2">{t}</b>'
         f'<span style="margin-left:auto;font-family:Inter,sans-serif;font-size:22px;font-weight:900;color:{VERDE}">GRATIS</span></div>'
         for n, t in BON)}
""")

# --- 5) el celular con el indice --------------------------------------------------------------
IND = [('1', 'Elegís el molde', '250+ modelos, en orden'),
       ('2', 'Mirás la clase', '25 videos, punto por punto'),
       ('3', 'Contás y cortás', 'El molde no te deja perderte'),
       ('4', 'Forro y herrajes', 'Lo que la hace parecer de local'),
       ('5', 'Le ponés precio', 'La fórmula, sin regalar tu trabajo')]
CELULAR = f"""<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>
*{{margin:0;padding:0;box-sizing:border-box;font-family:'Cormorant Garamond',Georgia,serif}}
body{{width:{W}px;height:{H}px;background:{FONDO};display:flex;align-items:center;justify-content:center;overflow:hidden}}
body:before{{content:"";position:absolute;inset:0;background:radial-gradient(circle at 50% 35%,rgba(212,53,111,.20),transparent 65%)}}
.tel{{position:relative;width:760px;height:1540px;background:#0C0A09;border-radius:68px;padding:22px;
 box-shadow:0 48px 90px rgba(0,0,0,.6)}}
.notch{{position:absolute;left:50%;transform:translateX(-50%);top:30px;width:190px;height:30px;background:#000;border-radius:18px;z-index:2}}
.scr{{width:100%;height:100%;background:{PAPEL};border-radius:50px;padding:92px 44px 44px}}
.k{{font-family:Inter,sans-serif;font-size:23px;letter-spacing:5px;font-weight:800;color:{ROSA};text-align:center}}
.t{{font-size:60px;color:{TINTA};text-align:center;margin-top:8px;line-height:1.05;font-weight:600}}
.t em{{font-style:italic;color:{ROSA}}}
.ln{{height:3px;background:{TINTA};opacity:.12;margin:18px 0}}
.it{{display:flex;gap:16px;align-items:flex-start;padding:21px 0;border-bottom:2px solid #EAE2D5}}
.it i{{flex:none;width:46px;height:46px;border-radius:10px;background:{ROSA};color:#fff;font-style:normal;
 font-family:Inter,sans-serif;font-weight:900;font-size:20px;display:flex;align-items:center;justify-content:center}}
.it b{{display:block;font-family:Inter,sans-serif;font-size:29px;font-weight:800;color:{TINTA};line-height:1.15}}
.it span{{display:block;font-family:Inter,sans-serif;font-size:23px;color:{GRIS};margin-top:4px}}
.bt{{margin-top:26px;background:{ROSA};color:#fff;font-family:Inter,sans-serif;font-weight:900;font-size:26px;
 letter-spacing:1px;text-align:center;padding:22px;border-radius:40px}}
</style></head><body>
<div class="tel"><div class="notch"></div><div class="scr">
  <div class="k">CARTERAS MAISON</div>
  <div class="t">El <em>Método Riviera</em></div>
  <div class="ln"></div>
  {''.join(f'<div class="it"><i>{n}</i><div><b>{t}</b><span>{s}</span></div></div>' for n, t, s in IND)}
  <div class="bt">ACCESO INMEDIATO</div>
</div></div></body></html>"""


def shot(html, name):
    p = f'{OUT}/_{name}.html'
    open(p, 'w').write(html)
    subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--hide-scrollbars',
                    '--allow-file-access-from-files',
                    f'--window-size={W},{H}', f'--screenshot={OUT}/_{name}.png',
                    '--virtual-time-budget=8000', 'file://' + p], check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    im = Image.open(f'{OUT}/_{name}.png').convert('RGB').resize((W, H), Image.LANCZOS)
    bg = im.resize((MW, MH), Image.LANCZOS).filter(ImageFilter.GaussianBlur(28))
    bg = Image.blend(bg, Image.new('RGB', (MW, MH), (21, 18, 15)), 0.38)
    bg.paste(im, ((MW - W) // 2, (MH - H) // 2))
    bg.save(f'{OUT}/{name}.png')
    os.remove(f'{OUT}/_{name}.html'); os.remove(f'{OUT}/_{name}.png')
    print(f'{OUT}/{name}.png')


def shot_alpha(html, name):
    p = f'{OUT}/_{name}.html'
    open(p, 'w').write(html.replace(f'background:{FONDO}', 'background:transparent')
                           .replace('body:before{content:"";position:absolute;inset:0;background:radial-gradient(circle at 50% 35%,rgba(212,53,111,.20),transparent 65%)}', ''))
    subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--hide-scrollbars',
                    '--default-background-color=00000000', '--allow-file-access-from-files',
                    f'--window-size={W},{H}', f'--screenshot={OUT}/{name}.png',
                    '--virtual-time-budget=8000', 'file://' + p], check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    im = Image.open(f'{OUT}/{name}.png').convert('RGBA')
    bb = im.getbbox()
    if bb: im.crop(bb).save(f'{OUT}/{name}.png')
    os.remove(f'{OUT}/_{name}.html')
    print(f'{OUT}/{name}.png')


if __name__ == '__main__':
    for html, name in [(TAPA, 'tapa'), (MOLDES, 'moldes'), (MATERIALES, 'materiales'), (BONOS, 'bonos'), (CELULAR, 'celular')]:
        shot(html, name)
    shot_alpha(CELULAR, 'celular_solo')
