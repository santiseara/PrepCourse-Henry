# -*- coding: utf-8 -*-
"""Inserts de producto de la oferta de displays de papel (LATAM, 2026-11-11).

Competimos contra Decorarina / Fabrica de Displays EN EL MISMO MERCADO, asi que esto
NO copia su estetica: ellos corren UGC real con su pastel de fiesta infantil (rosa, amarillo,
lila) y la pantalla del celular como unico inserto. Aca va papel crema + tinta azul noche +
un solo acento naranja quemado, y los insertos se dibujan por codigo.

Sin cifras en moneda: la oferta sale a varios paises de LATAM a la vez, asi que la cuenta se
cuenta en MULTIPLOS (regla del 2026-11-08).

Uso: python3 gfx_displays.py
"""
import os, subprocess
from PIL import Image, ImageFilter

OUT = os.path.expanduser('~/Desktop/displays-de-papel/anuncios/work/gfx')
os.makedirs(OUT, exist_ok=True)
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
W, H = 1080, 1920
MW, MH = 1188, 2112            # 1.10x

PAPEL, TINTA, NARANJA, GRIS = '#F7F1E6', '#1B2A3A', '#C8622A', '#6B6256'
FONDO = '#121C26'

FONTS = ('<link href="https://fonts.googleapis.com/css2?family=Bitter:ital,wght@0,500;0,700;1,600'
         '&family=Inter:wght@400;600;700;800;900&display=swap" rel="stylesheet">')

BASE = f"""<style>
*{{margin:0;padding:0;box-sizing:border-box;font-family:Bitter,Georgia,serif}}
body{{width:{W}px;height:{H}px;background:{FONDO};display:flex;align-items:center;justify-content:center;overflow:hidden}}
body:before{{content:"";position:absolute;inset:0;background:radial-gradient(circle at 50% 34%,rgba(200,98,42,.26),transparent 66%)}}
.hoja{{position:relative;width:980px;background:{PAPEL};padding:62px 56px 56px;border-radius:6px;
 box-shadow:0 44px 90px rgba(0,0,0,.55)}}
.kick{{font-family:Inter,sans-serif;font-size:24px;letter-spacing:5px;font-weight:800;color:{NARANJA};text-align:center}}
h1{{font-size:68px;line-height:1.03;color:{TINTA};margin-top:12px;text-align:center;letter-spacing:-1px}}
h1 em{{font-style:italic;color:{NARANJA}}}
.hr{{height:3px;background:{TINTA};opacity:.12;margin:28px 0}}
.pill{{display:inline-block;background:{NARANJA};color:#fff;font-family:Inter,sans-serif;font-weight:800;
 font-size:24px;letter-spacing:3px;padding:12px 26px;border-radius:30px}}
.ctr{{text-align:center}}
</style>"""


def hoja(cuerpo, extra=''):
    return f"""<!doctype html><html><head><meta charset="utf-8">{FONTS}{BASE}{extra}</head><body>
<div class="hoja">{cuerpo}</div></body></html>"""


def figura(c1, c2, kind):
    """Silueta de display recortado, dibujada en SVG."""
    if kind == 0:      # oso
        body = (f'<circle cx="120" cy="92" r="52" fill="{c1}"/><circle cx="78" cy="48" r="22" fill="{c1}"/>'
                f'<circle cx="162" cy="48" r="22" fill="{c1}"/>'
                f'<path d="M62 138 h116 v76 a30 30 0 0 1 -30 30 h-56 a30 30 0 0 1 -30 -30 Z" fill="{c1}"/>'
                f'<circle cx="120" cy="104" r="20" fill="{c2}" opacity=".55"/>')
    elif kind == 1:    # arbol de navidad
        body = (f'<path d="M120 24 l44 60 h-26 l34 48 h-26 l38 56 h-128 l38 -56 h-26 l34 -48 h-26 Z" fill="{c1}"/>'
                f'<rect x="106" y="188" width="28" height="36" fill="{c2}"/>'
                f'<circle cx="120" cy="20" r="12" fill="{c2}"/>')
    elif kind == 2:    # personaje de cuerpo entero
        body = (f'<circle cx="120" cy="56" r="32" fill="{c1}"/>'
                f'<path d="M88 96 h64 l16 72 h-20 l6 76 h-68 l6 -76 h-20 Z" fill="{c1}"/>'
                f'<path d="M88 96 l-28 56 M152 96 l28 56" stroke="{c1}" stroke-width="18" stroke-linecap="round" fill="none"/>'
                f'<path d="M104 132 h32 v26 h-32 Z" fill="{c2}" opacity=".6"/>')
    else:              # letra / numero gigante
        body = (f'<path d="M58 216 L120 32 L182 216 h-34 l-12 -40 h-32 l-12 40 Z" fill="{c1}"/>'
                f'<path d="M110 136 h20 l-10 -34 Z" fill="{c2}"/>')
    return f'<svg viewBox="0 0 240 240" width="100%" height="100%">{body}</svg>'


# --- 1) la escalera de tamanos: cuantas hojas = que pieza -----------------------------------
ESCALERA = [('7 hojas', 'Medio metro', 'Centro de mesa', '#C8622A', '#7A3A14', 0),
            ('20 hojas', 'Un metro', 'Del tamaño de un niño', '#2E6E64', '#17403A', 2),
            ('50 hojas', 'Dos metros', 'Panel y escenario', '#1B2A3A', '#0C1824', 3)]

TAMANOS = hoja(f"""
  <div class="kick">LA MISMA RESMA</div>
  <h1>De un paquete de hojas <em>sale todo</em></h1>
  <div class="ctr" style="margin-top:14px"><span class="pill">IMPRESORA COMÚN · SIN PLOTTER</span></div>
  <div class="hr"></div>
  <div class="esc">""" + ''.join(
    f"""<div class="e"><div class="im">{figura(c1, c2, k)}</div><i>{a}</i><b>{b}</b><span>{c}</span></div>"""
    for a, b, c, c1, c2, k in ESCALERA) + f"""
  </div>
  <div class="tip"><b>LO ÚNICO QUE CAMBIA</b> es cuántas hojas usas y dónde caen las uniones.</div>
""", extra=f"""<style>
.esc{{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}}
.e{{background:#fff;border:2px solid #EBE1D1;border-radius:10px;padding:16px 12px 20px;text-align:center}}
.e .im{{height:210px;display:flex;align-items:center;justify-content:center;padding:6px}}
.e i{{display:block;font-style:normal;font-family:Inter,sans-serif;font-size:21px;letter-spacing:2px;font-weight:900;color:{NARANJA}}}
.e b{{display:block;font-family:Inter,sans-serif;font-size:33px;font-weight:800;color:{TINTA};margin-top:6px}}
.e span{{display:block;font-family:Inter,sans-serif;font-size:21px;color:{GRIS};margin-top:4px}}
.tip{{margin-top:26px;background:#F3E7DA;border-left:8px solid {NARANJA};padding:20px 22px;font-family:Inter,sans-serif;
 font-size:25px;color:{TINTA};line-height:1.35;border-radius:0 8px 8px 0}}
.tip b{{color:{NARANJA};font-weight:900;letter-spacing:1px;margin-right:6px}}
</style>""")


# --- 2) la cuenta, en multiplos (nada de moneda) --------------------------------------------
COSTOS = hoja(f"""
  <div class="kick">LA MISMA PIEZA</div>
  <h1>Lo que cuesta <em>uno</em> afuera</h1>
  <div class="hr"></div>
  <div class="cmp">
    <div class="col fuera">
      <div class="t">EN LA IMPRENTA</div>
      <div class="big">1</div>
      <div class="lab">display de dos metros</div>
      <ul><li>Solo el adhesivo impreso</li><li>Base y soporte aparte</li><li>Tres días de espera</li><li>Mínimo de pedido</li></ul>
    </div>
    <div class="vs">=</div>
    <div class="col casa">
      <div class="t">EN TU CASA</div>
      <div class="big">7</div>
      <div class="lab">displays del mismo tamaño</div>
      <ul><li>Adhesivo, base y soporte</li><li>Impresora común y papel</li><li>El mismo día</li><li>Cuando tú quieras</li></ul>
    </div>
  </div>
  <div class="tip"><b>LA CUENTA REAL</b> no es cuánto ahorras por pieza: es sacar a la imprenta de adentro de tu negocio.</div>
""", extra=f"""<style>
.cmp{{display:flex;align-items:stretch;gap:16px}}
.col{{flex:1;border-radius:12px;padding:26px 20px;text-align:center}}
.fuera{{background:#EDE4D6;border:2px solid #DCCFB9}}
.casa{{background:{TINTA};color:#fff}}
.col .t{{font-family:Inter,sans-serif;font-size:21px;letter-spacing:3px;font-weight:900;color:{NARANJA}}}
.fuera .t{{color:{GRIS}}}
.big{{font-family:Inter,sans-serif;font-size:118px;font-weight:900;line-height:1;margin:6px 0 2px;color:{TINTA}}}
.casa .big{{color:#fff}}
.lab{{font-family:Inter,sans-serif;font-size:22px;color:{GRIS}}}
.casa .lab{{color:#C9D4DF}}
.col ul{{list-style:none;margin-top:18px;text-align:left}}
.col li{{font-family:Inter,sans-serif;font-size:21px;line-height:1.5;padding-left:26px;position:relative;color:{TINTA}}}
.casa li{{color:#E6EDF4}}
.col li:before{{content:"•";position:absolute;left:8px;color:{NARANJA};font-weight:900}}
.vs{{align-self:center;font-family:Inter,sans-serif;font-size:46px;font-weight:900;color:{NARANJA}}}
.tip{{margin-top:26px;background:#F3E7DA;border-left:8px solid {NARANJA};padding:20px 22px;font-family:Inter,sans-serif;
 font-size:24px;color:{TINTA};line-height:1.35;border-radius:0 8px 8px 0}}
.tip b{{color:{NARANJA};font-weight:900;letter-spacing:1px;margin-right:6px}}
</style>""")


# --- 3) la biblioteca de temas --------------------------------------------------------------
TEMAS = [('Navidad', '#C0463C', '#76211B', 1), ('Infantil', '#C8622A', '#7A3A14', 0),
         ('Personajes', '#2E6E64', '#17403A', 2), ('Letras y números', '#4A5A8A', '#232C48', 3),
         ('Baby shower', '#B07FA8', '#5E3C58', 0), ('Comuniones', '#C9A23A', '#7B6118', 2),
         ('Escolares', '#3F7AA8', '#1D3C57', 3), ('Vidrieras', '#8A5A2A', '#4C2F13', 1)]

BIBLIOTECA = hoja(f"""
  <div class="kick">ADENTRO</div>
  <h1>Casi dos mil <em>imágenes</em> listas</h1>
  <div class="ctr" style="margin-top:14px"><span class="pill">POR TEMÁTICA · ALTA RESOLUCIÓN</span></div>
  <div class="hr"></div>
  <div class="gr">""" + ''.join(
    f"""<div class="p"><div class="im">{figura(c1, c2, k)}</div><b>{t}</b></div>"""
    for t, c1, c2, k in TEMAS) + f"""
  </div>
  <div class="tip"><b>Y SI NO ESTÁ</b>, hay un método para armarla igual, sin diseñador y sin programas pagos.</div>
""", extra=f"""<style>
.gr{{display:grid;grid-template-columns:repeat(4,1fr);gap:18px}}
.p{{background:#fff;border:2px solid #EBE1D1;border-radius:10px;padding:12px 10px 16px;text-align:center}}
.p .im{{height:154px;display:flex;align-items:center;justify-content:center;padding:6px}}
.p b{{display:block;font-family:Inter,sans-serif;font-size:21px;font-weight:800;color:{TINTA};margin-top:8px}}
.tip{{margin-top:28px;background:#F3E7DA;border-left:8px solid {NARANJA};padding:20px 22px;font-family:Inter,sans-serif;
 font-size:25px;color:{TINTA};line-height:1.35;border-radius:0 8px 8px 0}}
.tip b{{color:{NARANJA};font-weight:900;letter-spacing:1px;margin-right:6px}}
</style>""")


# --- 4) lo que hay adentro, en el celular ---------------------------------------------------
IND = [('01', 'Curso completo en video', 'Clases cortas, desde el celular'),
       ('02', 'Banco de casi 2.000 imágenes', 'Por temática, alta resolución'),
       ('03', 'Paneles de más de 2 metros', 'Uniones que no se ven'),
       ('04', '13 formas de vender', 'Más allá de las fiestas'),
       ('05', 'Reto de 7 días', 'Publicar y conseguir el primer pedido'),
       ('06', 'Soporte por WhatsApp', 'Acceso de por vida, un solo pago')]

CELULAR = f"""<!doctype html><html><head><meta charset="utf-8">{FONTS}{BASE}
<style>
body{{background:{FONDO}}}
.tel{{position:relative;width:700px;height:1440px;background:#0A1118;border-radius:66px;padding:16px;
 box-shadow:0 50px 90px rgba(0,0,0,.6);border:3px solid #2C3A48}}
.scr{{width:100%;height:100%;background:{PAPEL};border-radius:52px;overflow:hidden;padding:60px 38px}}
.notch{{position:absolute;left:50%;transform:translateX(-50%);top:26px;width:170px;height:30px;background:#0A1118;border-radius:18px;z-index:3}}
.k{{font-family:Inter,sans-serif;font-size:19px;letter-spacing:4px;font-weight:800;color:{NARANJA};text-align:center}}
.t{{font-size:52px;color:{TINTA};text-align:center;margin:10px 0 8px;line-height:1.05}}
.t em{{font-style:italic;color:{NARANJA}}}
.ln{{height:3px;background:{TINTA};opacity:.12;margin:18px 0}}
.it{{display:flex;gap:16px;align-items:flex-start;padding:20px 0;border-bottom:2px solid #E8DECE}}
.it i{{flex:none;width:46px;height:46px;border-radius:10px;background:{NARANJA};color:#fff;font-style:normal;
 font-family:Inter,sans-serif;font-weight:900;font-size:20px;display:flex;align-items:center;justify-content:center}}
.it b{{display:block;font-family:Inter,sans-serif;font-size:28px;font-weight:800;color:{TINTA};line-height:1.15}}
.it span{{display:block;font-family:Inter,sans-serif;font-size:22px;color:{GRIS};margin-top:4px}}
.bt{{margin-top:24px;background:{NARANJA};color:#fff;font-family:Inter,sans-serif;font-weight:900;font-size:26px;
 letter-spacing:1px;text-align:center;padding:22px;border-radius:40px}}
</style></head><body>
<div class="tel"><div class="notch"></div><div class="scr">
  <div class="k">TODO EL PASO A PASO</div>
  <div class="t">Lo que hay <em>adentro</em></div>
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
    bg = Image.blend(bg, Image.new('RGB', (MW, MH), (18, 28, 38)), 0.38)
    bg.paste(im, ((MW - W) // 2, (MH - H) // 2))
    bg.save(f'{OUT}/{name}.png')
    os.remove(f'{OUT}/_{name}.html'); os.remove(f'{OUT}/_{name}.png')
    print(f'{OUT}/{name}.png')


def shot_alpha(html, name):
    p = f'{OUT}/_{name}.html'
    open(p, 'w').write(html.replace(f'background:{FONDO}', 'background:transparent')
                           .replace('body:before{content:"";position:absolute;inset:0;background:radial-gradient(circle at 50% 34%,rgba(200,98,42,.26),transparent 66%)}', ''))
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
    for html, name in [(TAMANOS, 'tamanos'), (COSTOS, 'costos'),
                       (BIBLIOTECA, 'biblioteca'), (CELULAR, 'celular')]:
        shot(html, name)
    shot_alpha(CELULAR, 'celular_solo')
