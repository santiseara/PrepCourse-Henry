# -*- coding: utf-8 -*-
"""Inserts de producto de la oferta de tapizado de sillones (Argentina, 2026-11-11).

Modelada de Caprichos de Mar / aprendeatapizarsillones.impultienda.ar (19 ads activos en AR).
Su edicion es b-roll de sillones antes/despues con una banda blanca de titular arriba y
subtitulos chicos blancos abajo: eso se clona en el editor. Los insertos los dibujamos nosotros,
porque ellos no tienen ninguno: papel lino + tinta + un solo acento verde azulado.

Es una oferta de UN solo pais, asi que si entra una cifra va en pesos, una sola por guion y
enmarcada como precio de mercado (regla del 2026-11-07). En estos insertos no entra ninguna.

Uso: python3 gfx_tapizar.py
"""
import os, subprocess
from PIL import Image, ImageFilter

OUT = os.path.expanduser('~/Desktop/tapizar-sillones/anuncios/work/gfx')
os.makedirs(OUT, exist_ok=True)
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
W, H = 1080, 1920
MW, MH = 1188, 2112

PAPEL, TINTA, VERDE, GRIS = '#F4EFE7', '#23201C', '#2F6B6A', '#6E675C'
FONDO = '#171511'

FONTS = ('<link href="https://fonts.googleapis.com/css2?family=Bitter:ital,wght@0,500;0,700;1,600'
         '&family=Inter:wght@400;600;700;800;900&display=swap" rel="stylesheet">')

BASE = f"""<style>
*{{margin:0;padding:0;box-sizing:border-box;font-family:Bitter,Georgia,serif}}
body{{width:{W}px;height:{H}px;background:{FONDO};display:flex;align-items:center;justify-content:center;overflow:hidden}}
body:before{{content:"";position:absolute;inset:0;background:radial-gradient(circle at 50% 34%,rgba(47,107,106,.28),transparent 66%)}}
.hoja{{position:relative;width:980px;background:{PAPEL};padding:62px 56px 56px;border-radius:6px;
 box-shadow:0 44px 90px rgba(0,0,0,.55)}}
.kick{{font-family:Inter,sans-serif;font-size:24px;letter-spacing:5px;font-weight:800;color:{VERDE};text-align:center}}
h1{{font-size:68px;line-height:1.03;color:{TINTA};margin-top:12px;text-align:center;letter-spacing:-1px}}
h1 em{{font-style:italic;color:{VERDE}}}
.hr{{height:3px;background:{TINTA};opacity:.12;margin:28px 0}}
.pill{{display:inline-block;background:{VERDE};color:#fff;font-family:Inter,sans-serif;font-weight:800;
 font-size:24px;letter-spacing:3px;padding:12px 26px;border-radius:30px}}
.ctr{{text-align:center}}
.tip{{margin-top:26px;background:#EAE2D4;border-left:8px solid {VERDE};padding:20px 22px;font-family:Inter,sans-serif;
 font-size:25px;color:{TINTA};line-height:1.35;border-radius:0 8px 8px 0}}
.tip b{{color:{VERDE};font-weight:900;letter-spacing:1px;margin-right:6px}}
</style>"""


def hoja(cuerpo, extra=''):
    return f"""<!doctype html><html><head><meta charset="utf-8">{FONTS}{BASE}{extra}</head><body>
<div class="hoja">{cuerpo}</div></body></html>"""


def icono(kind, c=VERDE):
    """Herramientas y piezas, dibujadas en SVG."""
    if kind == 'martillo':
        d = (f'<rect x="108" y="60" width="26" height="150" rx="8" fill="{c}"/>'
             f'<path d="M62 54 h116 v34 h-26 l-8 24 h-48 l-8 -24 h-26 Z" fill="{c}"/>')
    elif kind == 'engrampadora':
        d = (f'<path d="M40 150 h160 a16 16 0 0 1 16 16 v22 h-192 v-22 a16 16 0 0 1 16 -16 Z" fill="{c}"/>'
             f'<path d="M52 110 h140 a14 14 0 0 1 14 14 v18 h-168 v-18 a14 14 0 0 1 14 -14 Z" fill="{c}" opacity=".75"/>'
             f'<rect x="106" y="192" width="28" height="20" fill="{c}"/>')
    elif kind == 'tijera':
        d = (f'<path d="M72 60 L160 170 M168 60 L80 170" stroke="{c}" stroke-width="16" stroke-linecap="round" fill="none"/>'
             f'<circle cx="72" cy="188" r="22" fill="none" stroke="{c}" stroke-width="14"/>'
             f'<circle cx="168" cy="188" r="22" fill="none" stroke="{c}" stroke-width="14"/>')
    elif kind == 'sillon':
        d = (f'<path d="M34 104 a22 22 0 0 1 44 0 v56 h-44 Z" fill="{c}" opacity=".7"/>'
             f'<path d="M162 104 a22 22 0 0 1 44 0 v56 h-44 Z" fill="{c}" opacity=".7"/>'
             f'<path d="M62 70 h116 a20 20 0 0 1 20 20 v70 h-156 v-70 a20 20 0 0 1 20 -20 Z" fill="{c}"/>'
             f'<rect x="34" y="158" width="172" height="34" rx="10" fill="{c}" opacity=".85"/>'
             f'<rect x="52" y="192" width="18" height="24" fill="{c}"/><rect x="170" y="192" width="18" height="24" fill="{c}"/>')
    else:              # tela / rollo
        d = (f'<rect x="48" y="70" width="144" height="110" rx="10" fill="{c}" opacity=".35"/>'
             f'<path d="M48 70 h144 v24 h-144 Z M48 118 h144 v24 h-144 Z" fill="{c}" opacity=".8"/>'
             f'<rect x="48" y="70" width="144" height="110" rx="10" fill="none" stroke="{c}" stroke-width="5"/>')
    return f'<svg viewBox="0 0 240 240" width="100%" height="100%">{d}</svg>'


# --- 1) el sistema: los seis pasos ----------------------------------------------------------
PASOS = [('Desarmar', 'Con fotos y cada pieza numerada'),
         ('Medir', 'La tela vieja es el molde de la nueva'),
         ('Cortar', 'Sin desperdiciar medio metro'),
         ('Estirar', 'Donde se decide que no haga arrugas'),
         ('Grapar', 'El orden de los lados importa'),
         ('Rematar', 'Esquinas, apoyabrazos y terminación')]

SISTEMA = hoja(f"""
  <div class="kick">NO ES TALENTO, ES UN ORDEN</div>
  <h1>El sillón se hace <em>en seis pasos</em></h1>
  <div class="hr"></div>
  <div class="st">""" + ''.join(
    f"""<div class="s"><i>{i+1}</i><div><b>{t}</b><span>{d}</span></div></div>""" for i, (t, d) in enumerate(PASOS)) + f"""
  </div>
  <div class="tip"><b>SIEMPRE EN ESTE ORDEN</b> Por eso el sillón se puede dejar a medio hacer el martes y retomar el sábado.</div>
""", extra=f"""<style>
.st{{display:flex;flex-direction:column;gap:14px}}
.s{{display:flex;gap:20px;align-items:center;background:#fff;border:2px solid #E7DECE;border-radius:10px;padding:16px 20px}}
.s i{{flex:none;width:58px;height:58px;border-radius:50%;background:{VERDE};color:#fff;font-style:normal;
 font-family:Inter,sans-serif;font-weight:900;font-size:28px;display:flex;align-items:center;justify-content:center}}
.s b{{display:block;font-family:Inter,sans-serif;font-size:36px;font-weight:800;color:{TINTA}}}
.s span{{display:block;font-family:Inter,sans-serif;font-size:24px;color:{GRIS};margin-top:2px}}
</style>""")


# --- 2) las tres herramientas y la lista de "sin" -------------------------------------------
HERRAMIENTAS = hoja(f"""
  <div class="kick">TODO EL EQUIPO</div>
  <h1>Tres herramientas, <em>nada más</em></h1>
  <div class="hr"></div>
  <div class="gr">
    <div class="p"><div class="im">{icono('martillo')}</div><b>Martillo</b></div>
    <div class="p"><div class="im">{icono('engrampadora')}</div><b>Engrampadora</b></div>
    <div class="p"><div class="im">{icono('tijera')}</div><b>Tijera</b></div>
  </div>
  <div class="hr"></div>
  <div class="sin">
    <div class="n">Sin coser</div><div class="n">Sin máquina</div>
    <div class="n">Sin taller</div><div class="n">Sin fuerza</div>
  </div>
  <div class="tip"><b>TAPIZAR NO SE COSE</b> Se clava. Por eso se puede hacer en un rincón de tu casa.</div>
""", extra=f"""<style>
.gr{{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}}
.p{{background:#fff;border:2px solid #E7DECE;border-radius:10px;padding:18px 12px 22px;text-align:center}}
.p .im{{height:200px;display:flex;align-items:center;justify-content:center;padding:8px}}
.p b{{display:block;font-family:Inter,sans-serif;font-size:28px;font-weight:800;color:{TINTA};margin-top:8px}}
.sin{{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}}
.n{{background:{TINTA};color:#fff;font-family:Inter,sans-serif;font-weight:800;font-size:25px;
 text-align:center;padding:18px 6px;border-radius:30px}}
</style>""")


# --- 3) todo lo que recibís -----------------------------------------------------------------
COMBO = [('Curso en video', 'Un sillón de dos cuerpos, de punta a punta', 'INCLUIDO'),
         ('Almohadones', 'Confección paso a paso, con fotos', 'DE REGALO'),
         ('La tela y la medida', 'Cuál elegir, cuánta comprar, cómo cortar', 'DE REGALO'),
         ('Empezar a cobrar', 'Cómo presupuestar un trabajo', 'DE REGALO'),
         ('Grupo de WhatsApp', 'Preguntás con la foto de tu sillón', 'INCLUIDO'),
         ('Garantía de 7 días', 'Lo mirás y decidís', 'INCLUIDO')]

TODO = hoja(f"""
  <div class="kick">LO QUE RECIBÍS</div>
  <h1>Todo junto y <em>de una vez</em></h1>
  <div class="ctr" style="margin-top:14px"><span class="pill">UN SOLO PAGO · ACCESO DE POR VIDA</span></div>
  <div class="hr"></div>
  <div class="lst">""" + ''.join(
    f"""<div class="it"><div><b>{t}</b><span>{d}</span></div><i class="{'reg' if e=='DE REGALO' else ''}">{e}</i></div>"""
    for t, d, e in COMBO) + """
  </div>
""", extra=f"""<style>
.lst{{display:flex;flex-direction:column;gap:12px}}
.it{{display:flex;align-items:center;justify-content:space-between;gap:16px;background:#fff;
 border:2px solid #E7DECE;border-radius:10px;padding:18px 22px}}
.it b{{display:block;font-family:Inter,sans-serif;font-size:32px;font-weight:800;color:{TINTA}}}
.it span{{display:block;font-family:Inter,sans-serif;font-size:22px;color:{GRIS};margin-top:2px}}
.it i{{flex:none;font-style:normal;font-family:Inter,sans-serif;font-weight:900;font-size:19px;letter-spacing:2px;
 color:{GRIS};border:2px solid #D9CEBA;border-radius:24px;padding:9px 16px}}
.it i.reg{{color:#fff;background:{VERDE};border-color:{VERDE}}}
</style>""")


# --- 4) el celular con el indice ------------------------------------------------------------
IND = [('01', 'Desarmar sin romper nada', 'Fotos, numeración y la tela vieja'),
       ('02', 'Medir y calcular la tela', 'Cuánta comprar sin tirar de más'),
       ('03', 'Estirar y grapar', 'El orden que evita las arrugas'),
       ('04', 'Esquinas y apoyabrazos', 'Lo que separa lo prolijo de lo casero'),
       ('05', 'Almohadones', 'Confección paso a paso'),
       ('06', 'Presupuestar un trabajo', 'Qué cobrar y cómo pasarlo')]

CELULAR = f"""<!doctype html><html><head><meta charset="utf-8">{FONTS}{BASE}
<style>
body{{background:{FONDO}}}
.tel{{position:relative;width:700px;height:1440px;background:#0E0D0B;border-radius:66px;padding:16px;
 box-shadow:0 50px 90px rgba(0,0,0,.6);border:3px solid #3A352C}}
.scr{{width:100%;height:100%;background:{PAPEL};border-radius:52px;overflow:hidden;padding:60px 38px}}
.notch{{position:absolute;left:50%;transform:translateX(-50%);top:26px;width:170px;height:30px;background:#0E0D0B;border-radius:18px;z-index:3}}
.k{{font-family:Inter,sans-serif;font-size:19px;letter-spacing:4px;font-weight:800;color:{VERDE};text-align:center}}
.t{{font-size:52px;color:{TINTA};text-align:center;margin:10px 0 8px;line-height:1.05}}
.t em{{font-style:italic;color:{VERDE}}}
.ln{{height:3px;background:{TINTA};opacity:.12;margin:18px 0}}
.it{{display:flex;gap:16px;align-items:flex-start;padding:20px 0;border-bottom:2px solid #E6DED0}}
.it i{{flex:none;width:46px;height:46px;border-radius:10px;background:{VERDE};color:#fff;font-style:normal;
 font-family:Inter,sans-serif;font-weight:900;font-size:20px;display:flex;align-items:center;justify-content:center}}
.it b{{display:block;font-family:Inter,sans-serif;font-size:28px;font-weight:800;color:{TINTA};line-height:1.15}}
.it span{{display:block;font-family:Inter,sans-serif;font-size:22px;color:{GRIS};margin-top:4px}}
.bt{{margin-top:24px;background:{VERDE};color:#fff;font-family:Inter,sans-serif;font-weight:900;font-size:26px;
 letter-spacing:1px;text-align:center;padding:22px;border-radius:40px}}
</style></head><body>
<div class="tel"><div class="notch"></div><div class="scr">
  <div class="k">CLASES EN VIDEO</div>
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
    bg = Image.blend(bg, Image.new('RGB', (MW, MH), (23, 21, 17)), 0.38)
    bg.paste(im, ((MW - W) // 2, (MH - H) // 2))
    bg.save(f'{OUT}/{name}.png')
    os.remove(f'{OUT}/_{name}.html'); os.remove(f'{OUT}/_{name}.png')
    print(f'{OUT}/{name}.png')


def shot_alpha(html, name):
    p = f'{OUT}/_{name}.html'
    open(p, 'w').write(html.replace(f'background:{FONDO}', 'background:transparent')
                           .replace('body:before{content:"";position:absolute;inset:0;background:radial-gradient(circle at 50% 34%,rgba(47,107,106,.28),transparent 66%)}', ''))
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
    for html, name in [(SISTEMA, 'sistema'), (HERRAMIENTAS, 'herramientas'),
                       (TODO, 'todo'), (CELULAR, 'celular')]:
        shot(html, name)
    shot_alpha(CELULAR, 'celular_solo')
