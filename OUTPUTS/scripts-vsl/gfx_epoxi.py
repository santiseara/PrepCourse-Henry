# -*- coding: utf-8 -*-
"""Inserts de producto de El Manual del Piso Epoxi (LATAM, 2026-11-10).

Clonados de Hands & Home / The Epoxy Floor Playbook (handshome.impultienda.ar), que mete en
cada ad: la pagina "Metallic Marble - Step by Step" con la grilla de fotos numeradas, la
"Fix-It Chart", la tabla de cuanto cobrar por metro, las 3 tapas de bonos y el celular con las
paginas adentro. Se dibujan por codigo (HTML + Chrome headless), asi que no hace falta que el
producto exista todavia (regla del 2026-11-05).

Las fotos de los pasos salen de cuadros de los propios clips de TikTok del pool (fotos/p1.jpg..),
igual que el ganador, que usa fotos reales del proceso.

Cada insert sale sobre un lienzo 1.20x con el sobrante desenfocado, porque el editor le mete a
las fotos fijas un zoom de 1.0 a 1.14 mas un golpe de 1.16 por corte (regla del 2026-11-05).

Uso: python3 gfx_epoxi.py
"""
import os, subprocess
from PIL import Image, ImageFilter

OUT = os.path.expanduser('~/Desktop/pisos-epoxi/anuncios/work/gfx')
FOT = os.path.expanduser('~/Desktop/pisos-epoxi/anuncios/work/fotos')
os.makedirs(OUT, exist_ok=True)
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
W, H = 1080, 1920
MW, MH = 1188, 2112            # 1.10x

PAPEL, TINTA, COBRE, GRIS, ROJO = '#F7F2E9', '#241C16', '#C06A2C', '#6F675E', '#C0392B'
FONDO = '#1C1713'

FONTS = ('<link href="https://fonts.googleapis.com/css2?family=Source+Serif+4:ital,wght@0,400;0,600;0,700;1,600'
         '&family=Inter:wght@400;600;700;800;900&display=swap" rel="stylesheet">')

BASE = f"""<style>
*{{margin:0;padding:0;box-sizing:border-box;font-family:'Source Serif 4',Georgia,serif}}
body{{width:{W}px;height:{H}px;background:{FONDO};display:flex;align-items:center;justify-content:center;overflow:hidden}}
body:before{{content:"";position:absolute;inset:0;background:radial-gradient(circle at 50% 35%,rgba(192,106,44,.22),transparent 65%)}}
.hoja{{position:relative;width:980px;background:{PAPEL};padding:70px 62px 62px;border-radius:6px;
 box-shadow:0 44px 90px rgba(0,0,0,.55)}}
.kick{{font-family:Inter,sans-serif;font-size:25px;letter-spacing:5px;font-weight:800;color:{COBRE};text-align:center}}
h1{{font-size:72px;line-height:1.02;color:{TINTA};margin-top:12px;text-align:center;letter-spacing:-1px}}
h1 em{{font-style:italic;color:{COBRE}}}
.sub{{font-family:Inter,sans-serif;font-size:29px;color:{GRIS};margin-top:16px;line-height:1.4;text-align:center;font-weight:500}}
.hr{{height:3px;background:{TINTA};opacity:.13;margin:30px 0}}
.pill{{display:inline-block;background:{COBRE};color:#fff;font-family:Inter,sans-serif;font-weight:800;
 font-size:24px;letter-spacing:3px;padding:12px 26px;border-radius:30px}}
.ctr{{text-align:center}}
</style>"""


def hoja(cuerpo, extra=''):
    return f"""<!doctype html><html><head><meta charset="utf-8">{FONTS}{BASE}{extra}</head><body>
<div class="hoja">{cuerpo}</div></body></html>"""


# --- 1) la pagina del sistema, con la grilla de pasos y fotos ------------------------------
PASOS = [
    ('Prueba de humedad', 'Cinta y plástico, 24 h'),
    ('Desbaste del concreto', 'Abres el poro, no lo pintas'),
    ('Fisuras y juntas', 'Masilla epoxi y arena'),
    ('Imprimación', 'La capa que agarra'),
    ('Mezcla sin burbujas', 'Tiempo y revoluciones exactas'),
    ('Vertido y rasqueta', 'Espesor parejo'),
    ('Pigmento metálico', 'Veta y movimiento'),
    ('Capa final de brillo', 'El espejo'),
]

SISTEMA = hoja(f"""
  <div class="kick">POR ESO CREAMOS</div>
  <h1>El Manual del <em>Piso Epoxi</em></h1>
  <div class="ctr" style="margin-top:18px"><span class="pill">60+ PROYECTOS DE PISOS Y SUPERFICIES</span></div>
  <div class="hr"></div>
  <div style="font-family:Inter,sans-serif;font-size:23px;letter-spacing:4px;font-weight:800;color:{COBRE}">PARTE 2</div>
  <div style="font-size:50px;color:{TINTA};margin:6px 0 24px">Mármol metálico &middot; <i>paso a paso</i></div>
  <div class="gr">""" + ''.join(
    f"""<div class="p"><div class="im" style="background-image:url('file://{FOT}/p{i+1}.jpg')"></div>
        <div class="n">{i+1}</div><b>{t}</b><span>{s}</span></div>""" for i, (t, s) in enumerate(PASOS)) + """
  </div>
  <div class="tip"><b>TIP PRO</b> Si el concreto se oscurece con una gota de agua, absorbe: ya está listo para la imprimación.</div>
""", extra=f"""<style>
.gr{{display:grid;grid-template-columns:repeat(4,1fr);gap:18px}}
.p{{position:relative;background:#fff;border:2px solid #E8E0D3;border-radius:9px;padding:10px 10px 14px}}
.im{{height:150px;border-radius:6px;background-size:cover;background-position:center;background-color:#CFC6B8}}
.n{{position:absolute;left:18px;top:18px;width:46px;height:46px;border-radius:50%;background:{COBRE};color:#fff;
 font-family:Inter,sans-serif;font-weight:900;font-size:26px;display:flex;align-items:center;justify-content:center;
 box-shadow:0 4px 10px rgba(0,0,0,.35)}}
.p b{{display:block;font-family:Inter,sans-serif;font-size:23px;font-weight:800;color:{TINTA};margin-top:10px;line-height:1.15}}
.p span{{display:block;font-size:21px;color:{GRIS};margin-top:4px;line-height:1.25}}
.tip{{margin-top:26px;background:#F0E6D6;border-left:9px solid {COBRE};border-radius:8px;padding:20px 24px;
 font-family:Inter,sans-serif;font-size:25px;color:{TINTA};line-height:1.4}}
.tip b{{color:{COBRE};letter-spacing:2px;font-weight:900;margin-right:10px}}
</style>""")

# --- 2) la tabla de soluciones --------------------------------------------------------------
FIX = [
    ('Burbujas', 'El concreto larga aire', 'Imprimación y pasada de pincho'),
    ('Manchas pegajosas', 'Mezcla mal batida', 'Tiempo y revoluciones exactos'),
    ('Se levanta en placas', 'No hubo desbaste', 'Abrir el poro y volver a imprimar'),
    ('Marcas de rodillo', 'Capa fuera de tiempo', 'Ventana de repaso, minuto a minuto'),
    ('Amarillea con el sol', 'Capa final equivocada', 'Poliuretano arriba del epoxi'),
]

TABLA = hoja(f"""
  <div class="kick">PARTE 5</div>
  <h1>La Tabla de <em>Soluciones</em></h1>
  <div class="sub">Los doce problemas típicos, su causa y cómo se arregla cada uno.</div>
  <div class="hr"></div>
  <div class="t">
    <div class="hd"><span>Problema</span><span>Por qué pasa</span><span>Cómo se arregla</span></div>
""" + ''.join(
    f"""<div class="row"><span class="pr"><i>{i+1}</i>{a}</span><span>{b}</span><span class="fx">{c}</span></div>"""
    for i, (a, b, c) in enumerate(FIX)) + """
  </div>
  <div class="ctr" style="margin-top:34px"><span class="pill">SE ARREGLA EN MINUTOS</span></div>
""", extra=f"""<style>
.t{{border:2px solid #E4DBCC;border-radius:10px;overflow:hidden}}
.hd,.row{{display:grid;grid-template-columns:1.05fr 1fr 1.15fr;align-items:center}}
.hd{{background:{TINTA};color:#F3E8D8;font-family:Inter,sans-serif;font-size:24px;font-weight:800;letter-spacing:2px}}
.hd span{{padding:18px 20px}}
.row{{border-top:2px solid #EDE5D7;font-family:Inter,sans-serif;font-size:25px;color:{TINTA};background:#fff}}
.row:nth-child(even){{background:#FBF7F0}}
.row span{{padding:22px 20px;line-height:1.3}}
.pr{{font-weight:800;display:flex;align-items:center;gap:14px}}
.pr i{{flex:none;width:40px;height:40px;border-radius:50%;background:{ROJO};color:#fff;font-style:normal;
 font-size:22px;font-weight:900;display:flex;align-items:center;justify-content:center}}
.fx{{color:{COBRE};font-weight:700}}
</style>""")

# --- 3) cuanto cobrar: material contra precio de venta, en multiplos ------------------------
SIST = [
    ('Color sólido', 'El más fácil', 'x3'),
    ('Flake para garage', 'El más pedido', 'x4'),
    ('Mármol metálico', 'El mejor pagado', 'x5'),
    ('Océano y 3D', 'El que se viraliza', 'x5'),
    ('Sobre cerámica vieja', 'Sin romper nada', 'x4'),
    ('Mesadas y barras', 'El de mayor margen', 'x10'),
]

PRECIOS = hoja(f"""
  <div class="kick">PARTE 6</div>
  <h1>Calcula y <em>cobra</em></h1>
  <div class="sub">Cuánto comprar para no desperdiciar nada, y cuánto se paga el metro terminado<br>frente a lo que te cuesta el material.</div>
  <div class="hr"></div>
""" + ''.join(
    f"""<div class="r"><span class="s">{a}<i>{b}</i></span><span class="m">{c}<em>sobre el material</em></span></div>"""
    for a, b, c in SIST) + f"""
  <div class="pie">El material es la parte barata. La tabla del manual te da la cantidad exacta por metro cuadrado.</div>
""", extra=f"""<style>
.r{{display:flex;align-items:center;justify-content:space-between;background:#fff;border:2px solid #EDE5D7;
 border-left:10px solid {COBRE};border-radius:10px;padding:22px 26px;margin-bottom:16px}}
.s{{font-family:Inter,sans-serif;font-size:31px;font-weight:800;color:{TINTA}}}
.s i{{display:block;font-style:normal;font-size:23px;font-weight:500;color:{GRIS};margin-top:5px}}
.m{{font-family:Inter,sans-serif;font-size:56px;font-weight:900;color:{COBRE};text-align:right;line-height:1}}
.m em{{display:block;font-style:normal;font-size:20px;font-weight:700;letter-spacing:2px;color:{GRIS};margin-top:6px}}
.pie{{margin-top:22px;font-family:Inter,sans-serif;font-size:24px;color:{GRIS};text-align:center;line-height:1.4}}
</style>""")

# --- 4) los tres bonos ----------------------------------------------------------------------
BONOS_D = [
    ('BONO 1', 'Tu Primer<br>Trabajo Pago', 'Dónde conseguir los primeros tres clientes y qué decirles'),
    ('BONO 2', 'Dónde Comprar<br>y Qué Alquilar', 'Materiales baratos y la máquina por día, país por país'),
    ('BONO 3', 'Antes y Después<br>que Vende', 'Cómo fotografiar el reflejo y publicarlo para que te llamen'),
]

BONOS = hoja(f"""
  <div class="kick">CON TU PEDIDO DE HOY</div>
  <h1>Tres bonos <em>gratis</em></h1>
  <div class="sub">La parte que convierte un piso terminado en el siguiente trabajo pago.</div>
  <div class="hr"></div>
  <div class="gb">""" + ''.join(
    f"""<div class="b"><div class="tp"><span>{k}</span><b>{t}</b></div><p>{d}</p>
        <div class="free">GRATIS HOY</div></div>""" for k, t, d in BONOS_D) + """
  </div>
""", extra=f"""<style>
.gb{{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}}
.b{{background:#fff;border:2px solid #EDE5D7;border-radius:12px;overflow:hidden;text-align:center;
 box-shadow:0 16px 30px rgba(0,0,0,.14)}}
.tp{{background:linear-gradient(160deg,#2B211A,#4A3524);padding:30px 18px 34px;color:#fff}}
.tp span{{font-family:Inter,sans-serif;font-size:19px;letter-spacing:4px;font-weight:800;color:#E8A765}}
.tp b{{display:block;font-size:34px;line-height:1.12;margin-top:12px;font-weight:600}}
.b p{{font-family:Inter,sans-serif;font-size:22px;color:{GRIS};padding:20px 18px 12px;line-height:1.35}}
.free{{font-family:Inter,sans-serif;font-size:21px;font-weight:900;letter-spacing:3px;color:{COBRE};padding-bottom:22px}}
</style>""")

# --- 5) el celular con el manual adentro ----------------------------------------------------
IND = [('01', 'Empieza aquí', 'Seguridad y herramientas'), ('02', 'La preparación es el 80%', 'Prueba, desbaste, reparación'),
       ('03', 'Los 6 sistemas de piso', 'Sólido, flake, metálico, 3D'), ('04', '48 diseños metálicos', 'Colores y orden de volcado'),
       ('05', 'La Tabla de Soluciones', '12 problemas resueltos'), ('06', 'Calcula y cobra', 'Cuánto comprar, cuánto cobrar')]

CELULAR = f"""<!doctype html><html><head><meta charset="utf-8">{FONTS}{BASE}
<style>
body{{background:{FONDO}}}
.tel{{position:relative;width:700px;height:1440px;background:#0D0B09;border-radius:66px;padding:16px;
 box-shadow:0 50px 90px rgba(0,0,0,.6);border:3px solid #3A322A}}
.scr{{width:100%;height:100%;background:{PAPEL};border-radius:52px;overflow:hidden;padding:60px 38px}}
.notch{{position:absolute;left:50%;transform:translateX(-50%);top:26px;width:170px;height:30px;background:#0D0B09;border-radius:18px;z-index:3}}
.k{{font-family:Inter,sans-serif;font-size:19px;letter-spacing:4px;font-weight:800;color:{COBRE};text-align:center}}
.t{{font-size:52px;color:{TINTA};text-align:center;margin:10px 0 8px;line-height:1.05}}
.t em{{font-style:italic;color:{COBRE}}}
.ln{{height:3px;background:{TINTA};opacity:.12;margin:18px 0}}
.it{{display:flex;gap:16px;align-items:flex-start;padding:21px 0;border-bottom:2px solid #EDE5D7}}
.it i{{flex:none;width:46px;height:46px;border-radius:10px;background:{COBRE};color:#fff;font-style:normal;
 font-family:Inter,sans-serif;font-weight:900;font-size:20px;display:flex;align-items:center;justify-content:center}}
.it b{{display:block;font-family:Inter,sans-serif;font-size:29px;font-weight:800;color:{TINTA};line-height:1.15}}
.it span{{display:block;font-family:Inter,sans-serif;font-size:23px;color:{GRIS};margin-top:4px}}
.bt{{margin-top:26px;background:{COBRE};color:#fff;font-family:Inter,sans-serif;font-weight:900;font-size:26px;
 letter-spacing:1px;text-align:center;padding:22px;border-radius:40px}}
</style></head><body>
<div class="tel"><div class="notch"></div><div class="scr">
  <div class="k">EL MANUAL DEL PISO EPOXI</div>
  <div class="t">Todo lo que <em>hay adentro</em></div>
  <div class="ln"></div>
  {''.join(f'<div class="it"><i>{n}</i><div><b>{t}</b><span>{s}</span></div></div>' for n, t, s in IND)}
  <div class="bt">ACCESO INMEDIATO</div>
</div></div></body></html>"""


def shot(html, name):
    p = f'{OUT}/_{name}.html'
    open(p, 'w').write(html)
    subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--hide-scrollbars',
                    f'--window-size={W},{H}', f'--screenshot={OUT}/_{name}.png',
                    '--virtual-time-budget=8000', 'file://' + p], check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    im = Image.open(f'{OUT}/_{name}.png').convert('RGB').resize((W, H), Image.LANCZOS)
    bg = im.resize((MW, MH), Image.LANCZOS).filter(ImageFilter.GaussianBlur(28))
    bg = Image.blend(bg, Image.new('RGB', (MW, MH), (26, 20, 15)), 0.38)
    bg.paste(im, ((MW - W) // 2, (MH - H) // 2))
    bg.save(f'{OUT}/{name}.png')
    os.remove(f'{OUT}/_{name}.html'); os.remove(f'{OUT}/_{name}.png')
    print(f'{OUT}/{name}.png')


def shot_alpha(html, name):
    """El telefono recortado sobre fondo transparente, para la placa de cierre."""
    p = f'{OUT}/_{name}.html'
    open(p, 'w').write(html.replace(f'background:{FONDO}', 'background:transparent')
                           .replace('body:before{content:"";position:absolute;inset:0;background:radial-gradient(circle at 50% 35%,rgba(192,106,44,.22),transparent 65%)}', ''))
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
    for html, name in [(SISTEMA, 'sistema'), (TABLA, 'tabla'), (PRECIOS, 'precios'),
                       (BONOS, 'bonos'), (CELULAR, 'celular')]:
        shot(html, name)
    shot_alpha(CELULAR, 'celular_solo')
