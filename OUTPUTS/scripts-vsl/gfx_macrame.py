# -*- coding: utf-8 -*-
"""Insertos de producto de Navidad en Macrame (LATAM, 2026-11-14).

Modelado de "emprender con manualidades" / navidadenmacrame.impultienda.ar: 26 creativos
activos desde el 15 de octubre, 58 copias. Sus ads muestran el producto dos veces por video
(la tapa del ebook apoyada en una mesa y capturas de las paginas internas del PDF), asi que
nosotros tambien lo mostramos, pero dibujado por codigo (regla del 2026-11-05, Orzzen).

La jerarquia y el vocabulario salen de la landing que paso Santiago: +100 proyectos en 6
categorias, los 4 nudos base, cada proyecto con materiales, metros de cuerda y paso a paso
con fotos, 8 bonos de regalo, descarga inmediata y garantia de 7 dias. Lo unico que no se
copia es el precio (regla fija), y **no va ninguna cifra en moneda** porque la tanda sale a
varios paises de LATAM a la vez (regla del 2026-11-08).

Uso: python3 gfx_macrame.py
"""
import os, subprocess
from PIL import Image, ImageFilter

OUT = os.path.expanduser('~/Desktop/navidad-macrame/anuncios/work/gfx')
os.makedirs(OUT, exist_ok=True)
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
W, H = 1080, 1920
MW, MH = 1188, 2112            # 1.10x: el editor le mete zoom a las fotos fijas y se come los bordes

PAPEL, TINTA, ROJO, DORADO, GRIS = '#F6EFE2', '#1E3A2F', '#B5452F', '#B98A36', '#6E6457'
FONDO = '#10201A'

FONTS = ('<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600'
         '&family=Inter:wght@400;600;700;800;900&display=swap" rel="stylesheet">')

BASE = f"""<style>
*{{margin:0;padding:0;box-sizing:border-box;font-family:'Cormorant Garamond',Georgia,serif}}
body{{width:{W}px;height:{H}px;background:{FONDO};display:flex;align-items:center;justify-content:center;overflow:hidden}}
body:before{{content:"";position:absolute;inset:0;background:radial-gradient(circle at 50% 36%,rgba(185,138,54,.26),transparent 64%)}}
.hoja{{position:relative;width:980px;background:{PAPEL};padding:60px 54px 54px;border-radius:6px;
 box-shadow:0 44px 90px rgba(0,0,0,.55)}}
.kick{{font-family:Inter,sans-serif;font-size:23px;letter-spacing:5px;font-weight:800;color:{ROJO};text-align:center}}
h1{{font-size:76px;line-height:1.02;color:{TINTA};margin-top:10px;text-align:center;letter-spacing:-1px}}
h1 em{{font-style:italic;color:{ROJO}}}
.hr{{height:3px;background:{TINTA};opacity:.12;margin:26px 0}}
.pill{{display:inline-block;background:{ROJO};color:#fff;font-family:Inter,sans-serif;font-weight:800;
 font-size:23px;letter-spacing:3px;padding:12px 26px;border-radius:30px}}
.ctr{{text-align:center}}
.tip{{margin-top:26px;background:#EFE2D0;border-left:8px solid {ROJO};padding:20px 22px;font-family:Inter,sans-serif;
 font-size:24px;color:{TINTA};line-height:1.35;border-radius:0 8px 8px 0}}
.tip b{{color:{ROJO};font-weight:900;letter-spacing:1px;margin-right:6px}}
</style>"""


def hoja(cuerpo, extra=''):
    return f"""<!doctype html><html><head><meta charset="utf-8">{FONTS}{BASE}{extra}</head><body>
<div class="hoja">{cuerpo}</div></body></html>"""


def pieza(kind, c=TINTA, c2=ROJO):
    """Siluetas de las piezas navideñas de macramé, dibujadas en SVG."""
    if kind == 'arbol':
        body = (f'<path d="M120 26 L156 92 H84 Z" fill="{c}"/><path d="M120 76 L170 150 H70 Z" fill="{c}"/>'
                f'<path d="M120 128 L184 208 H56 Z" fill="{c}"/><rect x="108" y="208" width="24" height="26" fill="{c2}"/>'
                + ''.join(f'<line x1="{x}" y1="212" x2="{x}" y2="232" stroke="{c}" stroke-width="5"/>' for x in range(64, 180, 11)))
    elif kind == 'estrella':
        body = (f'<circle cx="120" cy="120" r="96" fill="none" stroke="{c2}" stroke-width="9"/>'
                f'<path d="M120 42 l21 50 54 5 -41 36 12 53 -46 -28 -46 28 12 -53 -41 -36 54 -5 Z" fill="none" stroke="{c}" stroke-width="11" stroke-linejoin="round"/>')
    elif kind == 'copo':
        body = ''.join(f'<g transform="rotate({a} 120 120)"><line x1="120" y1="120" x2="120" y2="30" stroke="{c}" stroke-width="10"/>'
                       f'<line x1="120" y1="56" x2="98" y2="36" stroke="{c}" stroke-width="8"/>'
                       f'<line x1="120" y1="56" x2="142" y2="36" stroke="{c}" stroke-width="8"/></g>' for a in range(0, 360, 60))
    elif kind == 'corona':
        body = (f'<circle cx="120" cy="124" r="80" fill="none" stroke="{c}" stroke-width="26"/>'
                + ''.join(f'<line x1="120" y1="204" x2="{x}" y2="232" stroke="{c}" stroke-width="6"/>' for x in (100, 112, 124, 136))
                + f'<path d="M96 40 q24 18 48 0 q-12 26 0 40 q-24 -16 -48 0 q12 -22 0 -40 Z" fill="{c2}"/>')
    elif kind == 'camino':
        body = (f'<rect x="20" y="84" width="200" height="72" fill="{c}" rx="4"/>'
                + ''.join(f'<line x1="{x}" y1="156" x2="{x}" y2="196" stroke="{c}" stroke-width="6"/>' for x in range(28, 216, 12))
                + ''.join(f'<line x1="{x}" y1="44" x2="{x}" y2="84" stroke="{c}" stroke-width="6"/>' for x in range(28, 216, 12)))
    elif kind == 'regalo':
        body = (f'<rect x="48" y="104" width="144" height="110" fill="{c}" rx="6"/>'
                f'<rect x="38" y="78" width="164" height="36" fill="{c2}" rx="6"/>'
                f'<rect x="108" y="78" width="24" height="136" fill="{PAPEL}"/>'
                f'<path d="M120 78 q-40 -46 -56 -14 q10 20 56 14 Z" fill="{c2}"/>'
                f'<path d="M120 78 q40 -46 56 -14 q-10 20 -56 14 Z" fill="{c2}"/>')
    else:   # muñeco / gnomo
        body = (f'<path d="M120 36 L186 170 H54 Z" fill="{c}"/><circle cx="120" cy="150" r="24" fill="{PAPEL}"/>'
                f'<path d="M54 170 h132 v18 a18 18 0 0 1 -18 18 H72 a18 18 0 0 1 -18 -18 Z" fill="{c2}"/>')
    return f'<svg viewBox="0 0 240 240" width="100%" height="100%">{body}</svg>'


# --- 1) la tapa del ebook -------------------------------------------------------------------
TAPA = f"""<!doctype html><html><head><meta charset="utf-8">{FONTS}{BASE}
<style>
body:before{{background:radial-gradient(circle at 50% 40%,rgba(185,138,54,.3),transparent 62%)}}
.lib{{position:relative;width:840px;height:1180px;background:{PAPEL};border-radius:10px;
 box-shadow:0 60px 110px rgba(0,0,0,.62);padding:70px 60px 54px;text-align:center;
 border:1px solid #E3D6C0}}
.lib:after{{content:"";position:absolute;left:0;top:0;bottom:0;width:26px;border-radius:10px 0 0 10px;
 background:linear-gradient(90deg,rgba(0,0,0,.20),rgba(0,0,0,0))}}
.cinta{{position:absolute;right:-14px;bottom:58px;background:{ROJO};color:#fff;font-family:Inter,sans-serif;
 font-weight:900;font-size:26px;letter-spacing:3px;padding:16px 26px;box-shadow:0 10px 24px rgba(0,0,0,.3)}}
.sello{{font-family:Inter,sans-serif;font-size:21px;letter-spacing:6px;font-weight:800;color:{DORADO}}}
.tit{{font-size:118px;line-height:.94;color:{TINTA};margin:16px 0 6px;letter-spacing:-2px}}
.tit em{{display:block;font-style:italic;color:{ROJO}}}
.baj{{font-family:Inter,sans-serif;font-size:27px;color:{GRIS};letter-spacing:1px}}
.fig{{height:430px;display:flex;align-items:center;justify-content:center;gap:16px;margin:26px 0 10px}}
.fig>div{{width:190px;height:190px}}
.ln{{height:3px;background:{TINTA};opacity:.14;margin:14px 60px}}
.pie{{font-family:Inter,sans-serif;font-size:25px;color:{TINTA};font-weight:700;line-height:1.5}}
.pie span{{color:{ROJO};font-weight:900}}
</style></head><body>
<div class="lib"><div class="cinta">EDICIÓN NAVIDAD</div>
  <div class="sello">PASO A PASO · CON FOTOS</div>
  <div class="tit">NAVIDAD<em>en macramé</em></div>
  <div class="baj">+100 proyectos navideños para el árbol, la puerta y la mesa</div>
  <div class="fig"><div>{pieza('arbol')}</div><div>{pieza('estrella')}</div><div>{pieza('corona')}</div></div>
  <div class="ln"></div>
  <div class="pie">Los <span>4 nudos base</span> · materiales y metros de cuerda<br>de cada pieza · <span>8 bonos de regalo</span></div>
</div></body></html>"""


# --- 2) una pagina de proyecto (lo que ellos muestran como captura del PDF) ------------------
PROYECTO = hoja(f"""
  <div class="cab"><span class="num">02</span><div><b>Estrella con aro</b><i>Para el árbol · Fácil · Una tarde</i></div>
    <div class="fg">{pieza('estrella')}</div></div>
  <div class="hr"></div>
  <div class="cols">
    <div class="bl"><div class="h">MATERIALES</div>
      <ul><li>Aro de madera de 10 cm</li><li>Cuerda de algodón de 3 mm</li><li>Tijera y peine</li></ul></div>
    <div class="bl"><div class="h">METROS DE CUERDA</div>
      <div class="mt">12 <small>m</small></div><span>8 cordones de 1,50 m</span></div>
  </div>
  <div class="h2">PASO A PASO</div>
  <div class="ps">
    <div class="p"><i>1</i><span>Monta los cordones al aro con nudo alondra.</span></div>
    <div class="p"><i>2</i><span>Dos vueltas de nudo plano, de izquierda a derecha.</span></div>
    <div class="p"><i>3</i><span>Cierra las puntas en nudo festón y forma las cinco puntas.</span></div>
    <div class="p"><i>4</i><span>Recorta los flecos parejos y peina.</span></div>
  </div>
  <div class="tip"><b>CADA PROYECTO</b> trae lo mismo: qué comprar, cuántos metros y el paso a paso con fotos.</div>
""", extra=f"""<style>
.cab{{display:flex;align-items:center;gap:22px}}
.num{{flex:none;width:86px;height:86px;border-radius:14px;background:{ROJO};color:#fff;font-family:Inter,sans-serif;
 font-weight:900;font-size:38px;display:flex;align-items:center;justify-content:center}}
.cab b{{display:block;font-size:58px;color:{TINTA};line-height:1}}
.cab i{{display:block;font-family:Inter,sans-serif;font-style:normal;font-size:22px;color:{GRIS};margin-top:6px;letter-spacing:1px}}
.fg{{margin-left:auto;width:126px;height:126px}}
.cols{{display:flex;gap:18px}}
.bl{{flex:1;background:#fff;border:2px solid #E9DECB;border-radius:10px;padding:20px 20px 22px}}
.h{{font-family:Inter,sans-serif;font-size:20px;letter-spacing:3px;font-weight:900;color:{ROJO}}}
.bl ul{{list-style:none;margin-top:12px}}
.bl li{{font-family:Inter,sans-serif;font-size:23px;color:{TINTA};line-height:1.5;padding-left:22px;position:relative}}
.bl li:before{{content:"•";position:absolute;left:4px;color:{DORADO};font-weight:900}}
.mt{{font-family:Inter,sans-serif;font-size:84px;font-weight:900;color:{TINTA};line-height:1;margin:8px 0 2px}}
.mt small{{font-size:34px;color:{GRIS}}}
.bl span{{font-family:Inter,sans-serif;font-size:22px;color:{GRIS}}}
.h2{{font-family:Inter,sans-serif;font-size:20px;letter-spacing:3px;font-weight:900;color:{ROJO};margin:26px 0 10px}}
.ps{{display:grid;gap:12px}}
.p{{display:flex;gap:14px;align-items:flex-start;background:#fff;border:2px solid #E9DECB;border-radius:10px;padding:14px 16px}}
.p i{{flex:none;width:40px;height:40px;border-radius:50%;background:{TINTA};color:#fff;font-style:normal;
 font-family:Inter,sans-serif;font-weight:900;font-size:20px;display:flex;align-items:center;justify-content:center}}
.p span{{font-family:Inter,sans-serif;font-size:23px;color:{TINTA};line-height:1.4}}
</style>""")


# --- 3) las 6 categorias = los +100 proyectos ------------------------------------------------
CATS = [('Para el árbol', '24', 'arbol'), ('Puerta y paredes', '17', 'corona'),
        ('Mesa navideña', '14', 'camino'), ('Deco para la casa', '11', 'copo'),
        ('Regalos', '9', 'regalo'), ('Para los chicos', '5', 'gnomo')]

CATEGORIAS = hoja(f"""
  <div class="kick">LA COLECCIÓN</div>
  <h1>+100 proyectos <em>navideños</em></h1>
  <div class="ctr" style="margin-top:12px"><span class="pill">6 CATEGORÍAS · PASO A PASO CON FOTOS</span></div>
  <div class="hr"></div>
  <div class="gr">""" + ''.join(
    f"""<div class="c"><div class="im">{pieza(k)}</div><b>{t}</b><i>{n} proyectos</i></div>"""
    for t, n, k in CATS) + f"""
  </div>
  <div class="tip"><b>CADA UNO</b> con sus materiales, los metros de cuerda y el paso a paso.</div>
""", extra=f"""<style>
.gr{{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}}
.c{{background:#fff;border:2px solid #E9DECB;border-radius:10px;padding:16px 10px 18px;text-align:center}}
.c .im{{height:170px;display:flex;align-items:center;justify-content:center;padding:8px}}
.c b{{display:block;font-family:Inter,sans-serif;font-size:24px;font-weight:800;color:{TINTA};margin-top:6px}}
.c i{{display:block;font-family:Inter,sans-serif;font-style:normal;font-size:21px;color:{ROJO};font-weight:700;margin-top:3px}}
</style>""")


# --- 4) los 4 nudos base --------------------------------------------------------------------
def nudo(k):
    s = '<svg viewBox="0 0 240 200" width="100%" height="100%">'
    if k == 0:    # alondra
        s += (f'<line x1="20" y1="44" x2="220" y2="44" stroke="{GRIS}" stroke-width="12"/>'
              f'<path d="M92 44 q0 34 -16 34 q-16 0 -16 -17 q0 -17 32 -17" fill="none" stroke="{TINTA}" stroke-width="12"/>'
              f'<path d="M148 44 q0 34 16 34 q16 0 16 -17 q0 -17 -32 -17" fill="none" stroke="{TINTA}" stroke-width="12"/>'
              f'<line x1="92" y1="60" x2="92" y2="176" stroke="{TINTA}" stroke-width="12"/>'
              f'<line x1="148" y1="60" x2="148" y2="176" stroke="{TINTA}" stroke-width="12"/>')
    elif k == 1:  # plano
        s += (f'<line x1="98" y1="24" x2="98" y2="176" stroke="{GRIS}" stroke-width="12"/>'
              f'<line x1="142" y1="24" x2="142" y2="176" stroke="{GRIS}" stroke-width="12"/>'
              f'<path d="M40 60 q58 -22 160 26 q-58 22 -160 -26" fill="none" stroke="{TINTA}" stroke-width="12"/>'
              f'<path d="M200 118 q-58 -22 -160 26 q58 22 160 -26" fill="none" stroke="{ROJO}" stroke-width="12"/>')
    elif k == 2:  # festón
        s += (f'<line x1="20" y1="54" x2="220" y2="54" stroke="{GRIS}" stroke-width="12"/>'
              + ''.join(f'<path d="M{x} 54 q18 28 0 48 q-18 -20 0 -48" fill="none" stroke="{TINTA}" stroke-width="11"/>'
                        f'<line x1="{x}" y1="102" x2="{x}" y2="176" stroke="{TINTA}" stroke-width="11"/>' for x in (64, 120, 176)))
    else:         # espiral
        s += (f'<line x1="98" y1="24" x2="98" y2="176" stroke="{GRIS}" stroke-width="12"/>'
              f'<line x1="142" y1="24" x2="142" y2="176" stroke="{GRIS}" stroke-width="12"/>'
              + ''.join(f'<path d="M50 {y} q70 -20 140 14" fill="none" stroke="{ROJO if i % 2 else TINTA}" stroke-width="11"/>'
                        for i, y in enumerate((52, 90, 128))))
    return s + '</svg>'


NUDOS = hoja(f"""
  <div class="kick">ANTES DE EMPEZAR</div>
  <h1>Con <em>4 nudos</em> se hacen todos</h1>
  <div class="ctr" style="margin-top:12px"><span class="pill">EXPLICADOS CON FOTOS, DESDE CERO</span></div>
  <div class="hr"></div>
  <div class="gr">""" + ''.join(
    f"""<div class="n"><div class="im">{nudo(i)}</div><b>{t}</b></div>"""
    for i, t in enumerate(['Nudo alondra', 'Nudo plano', 'Nudo festón', 'Nudo espiral'])) + f"""
  </div>
  <div class="tip"><b>NO HACE FALTA EXPERIENCIA</b>: se practican una vez y ya sirven para las +100 piezas.</div>
""", extra=f"""<style>
.gr{{display:grid;grid-template-columns:repeat(2,1fr);gap:20px}}
.n{{background:#fff;border:2px solid #E9DECB;border-radius:10px;padding:18px 14px 20px;text-align:center}}
.n .im{{height:220px;display:flex;align-items:center;justify-content:center;padding:6px}}
.n b{{display:block;font-family:Inter,sans-serif;font-size:27px;font-weight:800;color:{TINTA};margin-top:8px}}
</style>""")


# --- 5) los 8 bonos -------------------------------------------------------------------------
BONS = [('Calculadora de hilo', 'Cuántos cordones y metros lleva cada adorno'),
        ('Colgantes para regalar', 'Portamacetas y colgantes con detalle navideño'),
        ('Vende tus adornos', 'Qué precio poner, qué vender primero y dónde'),
        ('Terminaciones de fiesta', 'Flecos parejos, cuentas e hilos dorados'),
        ('Regalos express', '10 piezas de menos de una hora cada una'),
        ('Planificador de diciembre', 'Qué hacer cada semana hasta el 24'),
        ('Dónde comprar materiales', 'Cuerda, aros, cuentas y luces, al mejor precio'),
        ('Etiquetas y packaging', 'Tags navideños listos para imprimir')]

BONOS = hoja(f"""
  <div class="kick">SE SUMAN SIN COSTO</div>
  <h1>8 bonos <em>de regalo</em></h1>
  <div class="hr"></div>
  <div class="ls">""" + ''.join(
    f"""<div class="b"><i>{i}</i><div><b>{t}</b><span>{s}</span></div><em>GRATIS</em></div>"""
    for i, (t, s) in enumerate(BONS, 1)) + f"""
  </div>
  <div class="tip"><b>TODO JUNTO</b>, al instante y tuyo para siempre.</div>
""", extra=f"""<style>
.ls{{display:grid;gap:11px}}
.b{{display:flex;gap:14px;align-items:center;background:#fff;border:2px solid #E9DECB;border-radius:10px;padding:13px 16px}}
.b i{{flex:none;width:44px;height:44px;border-radius:10px;background:{TINTA};color:#fff;font-style:normal;
 font-family:Inter,sans-serif;font-weight:900;font-size:21px;display:flex;align-items:center;justify-content:center}}
.b b{{display:block;font-family:Inter,sans-serif;font-size:26px;font-weight:800;color:{TINTA};line-height:1.15}}
.b span{{display:block;font-family:Inter,sans-serif;font-size:20px;color:{GRIS};margin-top:2px}}
.b em{{margin-left:auto;font-style:normal;font-family:Inter,sans-serif;font-size:19px;font-weight:900;
 letter-spacing:2px;color:{ROJO};border:2px solid {ROJO};border-radius:20px;padding:6px 12px}}
</style>""")


def shot(html, name):
    p = f'{OUT}/_{name}.html'
    open(p, 'w').write(html)
    subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--hide-scrollbars',
                    f'--window-size={W},{H}', f'--screenshot={OUT}/_{name}.png',
                    '--virtual-time-budget=9000', 'file://' + p], check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    im = Image.open(f'{OUT}/_{name}.png').convert('RGB').resize((W, H), Image.LANCZOS)
    bg = im.resize((MW, MH), Image.LANCZOS).filter(ImageFilter.GaussianBlur(28))
    bg = Image.blend(bg, Image.new('RGB', (MW, MH), (16, 32, 26)), 0.38)
    bg.paste(im, ((MW - W) // 2, (MH - H) // 2))
    bg.save(f'{OUT}/{name}.png')
    os.remove(f'{OUT}/_{name}.html'); os.remove(f'{OUT}/_{name}.png')
    print(f'{OUT}/{name}.png')


if __name__ == '__main__':
    for html, name in [(TAPA, 'tapa'), (PROYECTO, 'proyecto'),
                       (CATEGORIAS, 'categorias'), (NUDOS, 'nudos'), (BONOS, 'bonos')]:
        shot(html, name)
