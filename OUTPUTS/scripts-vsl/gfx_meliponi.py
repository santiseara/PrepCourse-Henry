# -*- coding: utf-8 -*-
"""Inserts de producto de la guía de meliponicultura (LATAM, 2026-11-07).

El ganador brasileño (Meliponicultura Essencial) tiene el cuadernillo espiralado en pantalla
casi la mitad del ad, siempre abierto en la página que nombra la voz. Acá se dibujan esas
páginas por código (HTML + Chrome headless): tapa, calendario de manejo mes a mes, floraciones,
especies para empezar, la caja trampa, el bebedero y la cosecha. No hace falta que el producto
exista para lanzar la tanda (regla del 2026-11-05).

Cada insert sale sobre un lienzo 1.20x con el sobrante desenfocado, porque el editor le mete a
las fotos fijas un zoom de 1.0 a 1.14 más un golpe de 1.16 por corte.

Uso: python3 gfx_meliponi.py
"""
import os, subprocess
from PIL import Image, ImageFilter

OUT = os.path.expanduser('~/Desktop/meliponicultura/anuncios/work/gfx')
os.makedirs(OUT, exist_ok=True)
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
W, H = 1080, 1920
MW, MH = 1188, 2112            # 1.10x

PAPEL, TINTA, MIEL, VERDE, GRIS = '#FCFAF5', '#221F1A', '#C8881A', '#2F6B46', '#6E675E'
MADERA = '#5A4632'

BASE = f"""<style>
*{{margin:0;padding:0;box-sizing:border-box;font-family:'Source Serif 4',Georgia,serif}}
body{{width:{W}px;height:{H}px;background:{MADERA};display:flex;align-items:center;justify-content:center;overflow:hidden}}
body:before{{content:"";position:absolute;inset:0;background:
 repeating-linear-gradient(94deg,rgba(0,0,0,.14) 0 3px,rgba(255,255,255,.03) 3px 26px)}}
.hoja{{position:relative;width:960px;height:auto;min-height:1180px;max-height:1820px;background:{PAPEL};padding:86px 60px 70px 104px;
 box-shadow:0 40px 80px rgba(0,0,0,.45);border-radius:4px}}
.esp{{position:absolute;left:28px;top:60px;bottom:60px;width:44px;display:flex;flex-direction:column;
 justify-content:space-between}}
.esp i{{display:block;height:26px;border:5px solid #9A9A9A;border-radius:26px;background:transparent}}
.kick{{font-family:Inter,sans-serif;font-size:26px;letter-spacing:4px;font-weight:800;color:{MIEL}}}
h1{{font-size:76px;line-height:1.05;color:{TINTA};margin-top:14px;letter-spacing:-.5px}}
h1 em{{font-style:italic;color:{VERDE}}}
.sub{{font-family:Inter,sans-serif;font-size:31px;color:{GRIS};margin-top:16px;line-height:1.45;font-weight:500}}
.hr{{height:3px;background:{TINTA};opacity:.14;margin:30px 0}}
</style>"""

FONTS = ("""<link href="https://fonts.googleapis.com/css2?family=Source+Serif+4:ital,wght@0,400;0,600;0,700;1,400"""
         """&family=Inter:wght@400;600;700;800&display=swap" rel="stylesheet">""")

MESES = [
    ('ENERO', 'Agua y sombra. Control de hormigas.', VERDE),
    ('FEBRERO', 'Revisión de piqueras y humedad.', VERDE),
    ('MARZO', 'Cosecha de potes maduros.', MIEL),
    ('ABRIL', 'Reservas: no vaciar la colonia.', MIEL),
    ('MAYO', 'Aislar y cerrar rendijas.', '#3B5E8C'),
    ('JUNIO', 'Alimentación de refuerzo.', '#3B5E8C'),
    ('JULIO', 'Proteger del frío y del viento.', '#3B5E8C'),
    ('AGOSTO', 'Armar y colgar cajas trampa.', '#8C5A3B'),
    ('SEPTIEMBRE', 'Primera floración: observar.', '#8C5A3B'),
    ('OCTUBRE', 'División de colonias fuertes.', VERDE),
    ('NOVIEMBRE', 'Multiplicar y ampliar cajas.', VERDE),
    ('DICIEMBRE', 'Ventilación y agua limpia.', VERDE),
]

FLORES = [
    ('EUCALIPTO', 'Mayo · Julio', 'Floración larga, sostiene la colonia en frío'),
    ('CÍTRICOS', 'Agosto · Septiembre', 'Arranque fuerte de néctar, buena para dividir'),
    ('ACACIA', 'Septiembre · Octubre', 'Pico de polen: la colonia gana población'),
    ('GIRASOL', 'Noviembre · Enero', 'Mucho polen, poca agua: reforzar bebedero'),
    ('MORA / AGUACATE', 'Febrero · Marzo', 'Potes llenos: ventana de cosecha'),
]

ESPECIES = [
    ('ANGELITA', 'Tetragonisca angustula', 'Mansa, chica, se adapta a cualquier patio', VERDE),
    ('MELIPONA', 'Melipona spp.', 'La de mayor producción de miel', MIEL),
    ('MOSQUITA', 'Plebeia spp.', 'Ideal para espacios muy chicos', '#3B5E8C'),
    ('BORÁ', 'Tetragona clavipes', 'Colonias grandes, buena defensa', '#8C5A3B'),
]


def pagina(kick, titulo, sub, cuerpo, extra=''):
    return f"""<!doctype html><html><head><meta charset="utf-8">{FONTS}{BASE}{extra}</head><body>
<div class="hoja">
  <div class="esp">{'<i></i>' * 18}</div>
  <div class="kick">{kick}</div>
  <h1>{titulo}</h1>
  <div class="sub">{sub}</div>
  <div class="hr"></div>
  {cuerpo}
</div></body></html>"""


TAPA = f"""<!doctype html><html><head><meta charset="utf-8">{FONTS}{BASE}
<style>
.hoja{{height:1700px;display:flex;flex-direction:column;justify-content:space-between;text-align:center;padding:140px 80px 100px 110px}}
.top .k{{font-family:Inter,sans-serif;font-size:24px;letter-spacing:6px;font-weight:800;color:{MIEL}}}
.top .q{{font-family:Inter,sans-serif;font-size:27px;color:{GRIS};margin-top:18px;letter-spacing:1px}}
.tit{{font-size:116px;line-height:.95;color:{TINTA};letter-spacing:-2px;margin-top:40px}}
.tit b{{display:block;color:{VERDE};font-style:italic;font-weight:600}}
.ln{{width:200px;height:4px;background:{MIEL};margin:44px auto}}
.met{{font-size:38px;font-style:italic;color:{GRIS}}}
.hex{{display:flex;justify-content:center;gap:0;margin:56px 0 10px}}
.hex i{{width:92px;height:106px;background:{MIEL};opacity:.9;margin:0 -6px;
 clip-path:polygon(50% 0,100% 25%,100% 75%,50% 100%,0 75%,0 25%)}}
.hex i:nth-child(2){{background:#E3B65A;margin-top:52px}}
.hex i:nth-child(3){{background:{MIEL}}}
.hex i:nth-child(4){{background:#E3B65A;margin-top:52px}}
.pie{{font-family:Inter,sans-serif;font-size:28px;letter-spacing:5px;font-weight:800;color:{TINTA}}}
.pie span{{color:{MIEL};margin:0 10px}}
</style></head><body>
<div class="hoja">
  <div class="esp">{'<i></i>' * 18}</div>
  <div class="top">
    <div class="k">GUÍA PRÁCTICA 2026</div>
    <div class="q">Del patio al mercado</div>
    <div class="tit">ABEJAS<b>sin aguijón</b></div>
    <div class="ln"></div>
    <div class="met">El método completo en 12 meses</div>
  </div>
  <div class="hex"><i></i><i></i><i></i><i></i></div>
  <div class="pie">CIENCIA<span>·</span>MANEJO<span>·</span>RENTA</div>
</div></body></html>"""

CAL = pagina(
    'CALENDARIO DE MANEJO',
    'Qué hacer <em>en cada mes</em> del año',
    'La tabla que te dice cuándo dividir, cuándo cosechar y cuándo alimentar. '
    'Dejas de adivinar y sigues un orden.',
    '<div class="gr">' + ''.join(
        f'<div class="m" style="border-left:9px solid {c}"><b>{n}</b><span>{t}</span></div>'
        for n, t, c in MESES) + '</div>',
    extra=f"""<style>
.gr{{display:grid;grid-template-columns:1fr 1fr;gap:24px}}
.m{{background:#fff;border:2px solid #EDE7DC;border-radius:10px;padding:28px 24px}}
.m b{{display:block;font-family:Inter,sans-serif;font-size:30px;font-weight:800;color:{TINTA};letter-spacing:1px}}
.m span{{display:block;font-size:29px;color:{GRIS};margin-top:8px;line-height:1.35}}
</style>""")

FLO = pagina(
    'FLORACIONES',
    'Cuándo florece <em>tu región</em>',
    'Reconocer la floración es saber cuándo la colonia gana fuerza y cuándo necesita una mano.',
    ''.join(
        f'<div class="f"><div class="n">{n}</div><div class="m">{m}</div><div class="d">{d}</div></div>'
        for n, m, d in FLORES) +
    '<div class="nota">Anota en el margen las dos floraciones fuertes de tu zona: '
    'con eso ya tienes el calendario de divisiones.</div>',
    extra=f"""<style>
.f{{border-bottom:2px dotted #DDD6C9;padding:42px 0}}
.f .n{{font-family:Inter,sans-serif;font-size:42px;font-weight:800;color:{TINTA};letter-spacing:1px}}
.f .m{{font-size:32px;color:{MIEL};font-style:italic;margin-top:4px;font-weight:600}}
.f .d{{font-size:30px;color:{GRIS};margin-top:8px;line-height:1.4}}
.nota{{margin-top:46px;background:#F4EEE1;border-left:9px solid {MIEL};padding:34px 32px;
 font-size:30px;color:{TINTA};line-height:1.45;font-style:italic}}
</style>""")

ESP = pagina(
    'ESPECIES PARA EMPEZAR',
    'Con cuál <em>arrancar</em>',
    'Las mansas, las que se adaptan a un patio chico y las que más salida tienen cuando quieres vender.',
    ''.join(
        f'<div class="e"><div class="bar" style="background:{c}"></div><div class="tx">'
        f'<div class="n">{n}</div><div class="c">{c2}</div><div class="d">{d}</div></div></div>'
        for n, c2, d, c in ESPECIES),
    extra=f"""<style>
.e{{display:flex;gap:30px;align-items:stretch;margin-bottom:72px}}
.bar{{width:16px;border-radius:8px}}
.e .n{{font-family:Inter,sans-serif;font-size:50px;font-weight:800;color:{TINTA};letter-spacing:1px}}
.e .c{{font-size:32px;font-style:italic;color:{GRIS};margin-top:2px}}
.e .d{{font-size:32px;color:{TINTA};opacity:.78;margin-top:10px;line-height:1.4}}
</style>""")

TRAMPA = pagina(
    'CAPTURA DE ENJAMBRES',
    'Dónde <em>colgar</em> la caja trampa',
    'El secreto no está en la caja: está en el lugar. Tres condiciones y el enjambre entra solo.',
    """<div class="dg">
      <div class="arb"><i class="tr"></i><i class="cj"></i><div class="et">1,5 a 2,5 m del suelo</div></div>
      <ul>
        <li><b>Sombra la mayor parte del día.</b> Al sol directo el nido se recalienta y no entran.</li>
        <li><b>Cerca de agua y de floración.</b> A menos de 300 m de lo que ya visitan.</li>
        <li><b>Piquera mirando al este.</b> Sol temprano, resguardo del viento fuerte.</li>
        <li><b>Quieta.</b> Una vez colgada no se mueve ni se abre por 30 días.</li>
      </ul>
    </div>""",
    extra=f"""<style>
.dg{{display:flex;gap:34px}}
.arb{{position:relative;width:260px;height:700px;flex:none;background:#F4EEE1;border-radius:12px}}
.tr{{position:absolute;left:106px;top:0;bottom:150px;width:48px;background:#7A5E41;border-radius:6px}}
.cj{{position:absolute;left:66px;top:250px;width:128px;height:160px;background:{TINTA};border-radius:8px;
 box-shadow:0 10px 20px rgba(0,0,0,.25)}}
.cj:after{{content:"";position:absolute;left:52px;top:68px;width:24px;height:24px;background:{MIEL};border-radius:50%}}
.et{{position:absolute;left:0;right:0;bottom:48px;text-align:center;font-family:Inter,sans-serif;
 font-size:23px;font-weight:700;color:{GRIS}}}
ul{{list-style:none}}
li{{font-size:34px;color:{TINTA};line-height:1.45;margin-bottom:46px;padding-left:40px;position:relative}}
li:before{{content:"";position:absolute;left:0;top:13px;width:17px;height:17px;background:{MIEL};
 clip-path:polygon(50% 0,100% 25%,100% 75%,50% 100%,0 75%,0 25%)}}
li b{{font-family:Inter,sans-serif;font-weight:800}}
</style>""")

AGUA = pagina(
    'ERRORES SILENCIOSOS',
    'El agua, <em>bien ofrecida</em>',
    'Sin una fuente segura cerca, la pecoreadora sale lejos y muchas no vuelven. Se pierde población sin que lo veas.',
    """<div class="dos">
      <div class="mal"><div class="t">ASÍ NO</div>
        <div class="p">Plato hondo con agua limpia y nada donde pararse. Se ahogan.</div></div>
      <div class="bien"><div class="t">ASÍ SÍ</div>
        <div class="p">Recipiente bajo, lleno de piedritas o corchos que sobresalgan del agua,
        a la sombra y a menos de 10 m de las cajas. Se cambia cada dos días.</div></div>
    </div>
    <div class="nota">Y éste es apenas uno: el jarabe sin gotas de limón fermenta, la caja al sol
    recalienta el nido y la revisión en día frío enfría la cría.</div>""",
    extra=f"""<style>
.dos{{display:flex;gap:26px}}
.mal,.bien{{flex:1;border-radius:12px;padding:38px 32px}}
.mal{{background:#F7E9E6;border:3px solid #C0553F}}
.bien{{background:#E9F2EA;border:3px solid {VERDE}}}
.t{{font-family:Inter,sans-serif;font-size:28px;font-weight:800;letter-spacing:3px}}
.mal .t{{color:#C0553F}} .bien .t{{color:{VERDE}}}
.p{{font-size:30px;color:{TINTA};line-height:1.45;margin-top:16px}}
.nota{{margin-top:46px;background:#F4EEE1;border-left:9px solid {MIEL};padding:34px 32px;
 font-size:30px;color:{TINTA};line-height:1.45;font-style:italic}}
</style>""")

VENTA = pagina(
    'COSECHA Y VENTA',
    'De los potes <em>al frasco</em>',
    'Cosechar sin dañar el nido, madurar la miel y presentarla para que se pague lo que vale.',
    """<ol>
      <li><b>Abrir solo con potes operculados.</b> Nunca la melgueira entera: se deja reserva.</li>
      <li><b>Succión o corte limpio.</b> Sin tocar la cría ni el involucro.</li>
      <li><b>Maduración y filtrado.</b> Humedad alta: la miel de nativas no se trata como la de apis.</li>
      <li><b>Frasco chico y etiqueta.</b> Especie, zona y fecha de cosecha.</li>
      <li><b>Dónde se vende.</b> Dietéticas, ferias, herbolarios y el boca a boca del barrio.</li>
    </ol>""",
    extra=f"""<style>
ol{{counter-reset:n;list-style:none}}
li{{counter-increment:n;position:relative;padding-left:104px;margin-bottom:62px;font-size:34px;
 color:{TINTA};line-height:1.45}}
li:before{{content:counter(n);position:absolute;left:0;top:-4px;width:72px;height:72px;border-radius:50%;
 background:{MIEL};color:#fff;font-family:Inter,sans-serif;font-weight:800;font-size:40px;
 display:flex;align-items:center;justify-content:center}}
li b{{font-family:Inter,sans-serif;font-weight:800}}
</style>""")


def shot(html, name):
    p = f'{OUT}/_{name}.html'
    open(p, 'w').write(html)
    subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--hide-scrollbars',
                    f'--window-size={W},{H}', f'--screenshot={OUT}/_{name}.png',
                    '--virtual-time-budget=6000', 'file://' + p], check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    im = Image.open(f'{OUT}/_{name}.png').convert('RGB').resize((W, H), Image.LANCZOS)
    bg = im.resize((MW, MH), Image.LANCZOS).filter(ImageFilter.GaussianBlur(26))
    bg = Image.blend(bg, Image.new('RGB', (MW, MH), (40, 30, 20)), 0.35)
    bg.paste(im, ((MW - W) // 2, (MH - H) // 2))
    bg.save(f'{OUT}/{name}.png')
    os.remove(f'{OUT}/_{name}.html'); os.remove(f'{OUT}/_{name}.png')
    print(f'{OUT}/{name}.png')


for html, name in [(TAPA, 'tapa'), (CAL, 'calendario'), (FLO, 'floraciones'),
                   (ESP, 'especies'), (TRAMPA, 'trampa'), (AGUA, 'agua'), (VENTA, 'venta')]:
    shot(html, name)
