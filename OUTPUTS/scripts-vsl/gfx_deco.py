# -*- coding: utf-8 -*-
"""Inserts de producto de la tanda LATAM de Deco Magic (2026-11-09).

El ganador (Magic Deco / decomagic.shop) muestra el producto en pantalla casi la mitad del ad:
la app con su buscador y la grilla de temáticas, y el diseño abierto en Canva mientras le
cambian el nombre. Acá esas dos pantallas se dibujan por código (HTML + Chrome headless),
sin marca ni logo, porque la oferta propia todavía no tiene landing (regla del 2026-11-05:
no hace falta que el producto exista para lanzar la tanda).

Cada insert sale sobre un lienzo 1.20x con el sobrante desenfocado, porque el editor le mete
a las fotos fijas un zoom de 1.0 a 1.14 más un golpe de 1.16 por corte.

Uso: python3 gfx_deco.py
"""
import os, subprocess
from PIL import Image, ImageFilter

OUT = os.path.expanduser('~/Desktop/deco-magic/anuncios/work/gfx')
os.makedirs(OUT, exist_ok=True)
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
W, H = 1080, 1920
MW, MH = 1296, 2304            # 1.20x

ROSA, VIOLETA, FONDO, TINTA, GRIS = '#E74FA4', '#7E3D96', '#FDF2F8', '#2A1B2E', '#8A7B90'

FUENTE = ("font-family:-apple-system,'Helvetica Neue',Helvetica,Arial,sans-serif")

# --- 1) la app: buscador + grilla de temáticas -------------------------------
TEMAS = [('Cajita de dulces', '12 × 8 cm'), ('Bolsita de papas', '11 × 8,5 cm'),
         ('Topper de torta', '15 × 15 cm'), ('Etiqueta de botella', '9 × 6 cm'),
         ('Banderín con nombre', '18 × 12 cm'), ('Invitación', 'A5'),
         ('Caja de regalo', '15 × 10 cm'), ('Portarretrato', '13 × 18 cm')]

tarjetas = ''.join(f"""
 <div class=card>
   <div class=thumb><div class=ico>{i}</div><span class=pill>CANVA</span></div>
   <div class=cn>{n}</div><div class=cs>{s} · Abrir en Canva →</div>
 </div>""" for i, (n, s) in zip('🎁🍿🎂🏷️🎏💌📦🖼️', TEMAS))

APP = f"""<style>
*{{margin:0;padding:0;box-sizing:border-box;{FUENTE}}}
body{{width:{W}px;height:{H}px;background:{FONDO};overflow:hidden}}
.top{{padding:52px 44px 18px;display:flex;align-items:center;gap:18px}}
.logo{{width:62px;height:62px;border-radius:18px;background:linear-gradient(140deg,{VIOLETA},{ROSA})}}
.tt{{font-size:38px;font-weight:800;color:{TINTA};letter-spacing:-.5px}}
.idio{{margin-left:auto;display:flex;gap:10px}}
.idio span{{font-size:22px;font-weight:700;color:{GRIS};padding:7px 13px;border-radius:9px}}
.idio span.on{{background:{ROSA};color:#fff}}
h1{{padding:14px 44px 0;font-size:72px;font-weight:900;color:{TINTA};letter-spacing:-2px}}
.sub{{padding:6px 44px 0;font-size:28px;color:{GRIS}}}
.buscador{{margin:26px 44px 10px;height:108px;background:#fff;border:3px solid #F3D4E6;border-radius:26px;
 display:flex;align-items:center;gap:20px;padding:0 30px;box-shadow:0 10px 28px rgba(126,61,150,.10)}}
.lupa{{font-size:40px;opacity:.5}}
.q{{font-size:40px;font-weight:700;color:{TINTA}}}
.caret{{width:4px;height:46px;background:{ROSA};margin-left:2px}}
.cont{{padding:10px 44px 0;font-size:24px;font-weight:700;color:{ROSA}}}
.grid{{padding:16px 44px;display:grid;grid-template-columns:1fr 1fr;gap:24px}}
.card{{background:#fff;border-radius:26px;overflow:hidden;box-shadow:0 10px 26px rgba(126,61,150,.10)}}
.thumb{{position:relative;height:250px;background:linear-gradient(145deg,#FBE6F3,#EADCF6);
 display:flex;align-items:center;justify-content:center}}
.ico{{font-size:110px}}
.pill{{position:absolute;top:14px;right:14px;background:{ROSA};color:#fff;font-size:18px;font-weight:800;
 padding:7px 14px;border-radius:999px;letter-spacing:.5px}}
.cn{{padding:16px 20px 2px;font-size:28px;font-weight:800;color:{TINTA}}}
.cs{{padding:0 20px 18px;font-size:21px;color:{GRIS}}}
</style>
<div class=top><div class=logo></div><div class=tt>Tu app de fiestas</div>
 <div class=idio><span class=on>ES</span><span>EN</span><span>PT</span></div></div>
<h1>Temáticas</h1>
<div class=sub>Todo el set, ya diseñado y combinando</div>
<div class=buscador><span class=lupa>🔍</span><span class=q>dinosaurios</span><span class=caret></span></div>
<div class=cont>48 diseños en esta temática</div>
<div class=grid>{tarjetas}</div>
"""

# --- 2) Canva: el diseño abierto y el nombre cambiándose ----------------------
CANVA = f"""<style>
*{{margin:0;padding:0;box-sizing:border-box;{FUENTE}}}
body{{width:{W}px;height:{H}px;background:#F1F1F3;overflow:hidden}}
.bar{{height:120px;background:linear-gradient(90deg,#00C4CC,#7D2AE8);display:flex;align-items:center;
 justify-content:space-between;padding:0 40px}}
.bar .l{{color:#fff;font-size:40px;font-weight:800;letter-spacing:-.5px}}
.bar .r{{color:#fff;font-size:32px;font-weight:700;opacity:.92}}
.lienzo{{margin:60px 60px 0;height:1020px;background:#fff;border-radius:18px;
 box-shadow:0 26px 60px rgba(0,0,0,.18);position:relative;overflow:hidden}}
.deco{{position:absolute;inset:0;background:
 radial-gradient(circle at 18% 20%,#FFE2F1 0 180px,transparent 181px),
 radial-gradient(circle at 86% 78%,#E4DBFB 0 220px,transparent 221px),
 linear-gradient(160deg,#FFF7FB,#F6F0FF)}}
.pieza{{position:absolute;left:90px;right:90px;top:150px;text-align:center}}
.tema{{font-size:40px;letter-spacing:10px;color:{VIOLETA};font-weight:800}}
.nombre{{font-size:150px;font-weight:900;color:{TINTA};letter-spacing:-4px;margin-top:10px;
 border:5px solid {ROSA};border-radius:14px;display:inline-block;padding:6px 34px}}
.edad{{font-size:58px;font-weight:800;color:{ROSA};margin-top:28px}}
.ico{{font-size:120px;margin-top:26px}}
.tool{{margin:34px 60px 0;height:104px;background:#fff;border-radius:16px;display:flex;align-items:center;
 gap:26px;padding:0 30px;box-shadow:0 10px 26px rgba(0,0,0,.10)}}
.tool div{{font-size:30px;font-weight:700;color:#4A4A55}}
.tool .act{{background:{ROSA};color:#fff;padding:10px 20px;border-radius:12px}}
.tec{{position:absolute;left:0;right:0;bottom:0;height:420px;background:#D4D6DC;padding:26px 18px;
 display:grid;grid-template-columns:repeat(10,1fr);gap:12px}}
.tec span{{background:#fff;border-radius:12px;display:flex;align-items:center;justify-content:center;
 font-size:30px;font-weight:600;color:#2A2A33;height:76px}}
</style>
<div class=bar><div class=l>Canva</div><div class=r>Gratis · Editando</div></div>
<div class=lienzo><div class=deco></div>
 <div class=pieza><div class=tema>DINOSAURIOS</div>
  <div class=nombre>Martina</div><div class=edad>5 años</div><div class=ico>🦕</div></div>
</div>
<div class=tool><div>Fuente</div><div>88,9 pt</div><div class=act>Texto</div><div>Color</div><div>Posición</div></div>
<div class=tec>{''.join('<span>%s</span>' % c for c in 'QWERTYUIOPASDFGHJKLÑZXCVBNM')}</div>
"""


def shot(html, name):
    p = f'{OUT}/_{name}.html'
    open(p, 'w').write(html)
    subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--hide-scrollbars',
                    f'--window-size={W},{H}', f'--screenshot={OUT}/_{name}.png',
                    '--virtual-time-budget=6000', 'file://' + p], check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    im = Image.open(f'{OUT}/_{name}.png').convert('RGB').resize((W, H), Image.LANCZOS)
    bg = im.resize((MW, MH), Image.LANCZOS).filter(ImageFilter.GaussianBlur(28))
    bg = Image.blend(bg, Image.new('RGB', (MW, MH), (126, 61, 150)), 0.30)
    bg.paste(im, ((MW - W) // 2, (MH - H) // 2))
    bg.save(f'{OUT}/{name}.png')
    os.remove(f'{OUT}/_{name}.html'); os.remove(f'{OUT}/_{name}.png')
    print(f'{OUT}/{name}.png')


for html, name in [(APP, 'app'), (CANVA, 'canva')]:
    shot(html, name)
