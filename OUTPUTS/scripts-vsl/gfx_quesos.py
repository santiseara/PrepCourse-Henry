# -*- coding: utf-8 -*-
"""Inserts de producto de la cartilla de quesos (LATAM, 2026-11-08).

El ganador brasileño (Queijo de Casa / Cartilha Receitas Lucrativas do Leite) tiene el
cuadernillo espiralado "OURO BRANCO" en pantalla casi la mitad del ad, con un celular encima
mostrando las páginas. Acá se dibujan esas páginas por código (HTML + Chrome headless):
tapa, sumario, los rellenos, el aprovechamiento del suero, el rendimiento de la leche,
el yogur y la carta completa. No hace falta que el producto exista para lanzar la tanda
(regla del 2026-11-05).

Cada insert sale sobre un lienzo 1.10x con el sobrante desenfocado, porque el editor le mete a
las fotos fijas un zoom de 1.0 a 1.14 mas un golpe de 1.16 por corte.

Uso: python3 gfx_quesos.py
"""
import os, subprocess
from PIL import Image, ImageFilter

OUT = os.path.expanduser('~/Desktop/quesos/anuncios/work/gfx')
os.makedirs(OUT, exist_ok=True)
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
W, H = 1080, 1920
MW, MH = 1188, 2112            # 1.10x

PAPEL, TINTA, ORO, VINO, GRIS = '#FCFAF5', '#221F1A', '#C08A28', '#9B3B32', '#6E675E'
MADERA = '#54402E'

BASE = f"""<style>
*{{margin:0;padding:0;box-sizing:border-box;font-family:'Source Serif 4',Georgia,serif}}
body{{width:{W}px;height:{H}px;background:{MADERA};display:flex;align-items:center;justify-content:center;overflow:hidden}}
body:before{{content:"";position:absolute;inset:0;background:
 repeating-linear-gradient(93deg,rgba(0,0,0,.16) 0 3px,rgba(255,255,255,.03) 3px 24px)}}
.hoja{{position:relative;width:960px;height:auto;min-height:1180px;max-height:1820px;background:{PAPEL};padding:86px 60px 70px 104px;
 box-shadow:0 40px 80px rgba(0,0,0,.45);border-radius:4px}}
.esp{{position:absolute;left:28px;top:60px;bottom:60px;width:44px;display:flex;flex-direction:column;
 justify-content:space-between}}
.esp i{{display:block;height:26px;border:5px solid #9A9A9A;border-radius:26px;background:transparent}}
.kick{{font-family:Inter,sans-serif;font-size:26px;letter-spacing:4px;font-weight:800;color:{ORO}}}
h1{{font-size:76px;line-height:1.05;color:{TINTA};margin-top:14px;letter-spacing:-.5px}}
h1 em{{font-style:italic;color:{VINO}}}
.sub{{font-family:Inter,sans-serif;font-size:31px;color:{GRIS};margin-top:16px;line-height:1.45;font-weight:500}}
.hr{{height:3px;background:{TINTA};opacity:.14;margin:30px 0}}
</style>"""

FONTS = ("""<link href="https://fonts.googleapis.com/css2?family=Source+Serif+4:ital,wght@0,400;0,600;0,700;1,400"""
         """&family=Inter:wght@400;600;700;800&display=swap" rel="stylesheet">""")

RELLENOS = [
    ('DULCE DE LECHE', 'El que nunca falta', 'La combinación más vendida. Punto firme para que no se escurra al cortar.', '#8C5A2B'),
    ('FORMA DE CORAZÓN', 'El de regalo', 'Entra en canastas de desayuno y pedidos de empresa. Molde y desmolde.', VINO),
    ('DULCE DE MEMBRILLO', 'El de toda la vida', 'El clásico, pero adentro de la pieza. Proporción exacta queso-dulce.', '#A8502F'),
    ('MERMELADA DE FRESA', 'El que agrega valor', 'Con trozos. Armoniza con el queso fresco y casi no suma costo.', '#B23B55'),
    ('CARNE CON QUESO CREMA', 'El que cambia el juego', 'El sabor que convirtió a cientos de queseros en referencia de su zona.', '#6E4A2C'),
]

SUERO = [
    ('RICOTA', 'Del suero caliente, sin leche nueva', 'Rinde, se vende el mismo día y no necesita cámara.'),
    ('CREMA DE RICOTA', 'Untable, lista para vender en pote', 'Versión salada y versión dulce. La que más gira.'),
    ('BEBIDA LÁCTEA ACHOCOLATADA', 'La botella que se lleva el chico', 'Alto valor percibido, costo casi cero.'),
]

CARTA = [
    ('Queso fresco', 'Base de todo'), ('Queso fresco relleno', 'El que no compite por precio'),
    ('Queso de cuajo tradicional', 'El de siempre, bien hecho'), ('Queso de cuajo relleno', 'La version cara'),
    ('Queso en forma de corazón', 'Regalo y canastas'), ('Queso crema de corte', 'Sale el mismo día'),
    ('Queso crema untable', 'El que repite el cliente'), ('Yogur premium con mermelada', 'Venta diaria'),
    ('Dulce de leche en pasta', 'Para el mostrador'), ('Dulce de leche en barra', 'Para regalar'),
    ('Ricota y crema de ricota', 'Del suero'), ('Bebida láctea achocolatada', 'Del suero'),
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
.top .k{{font-family:Inter,sans-serif;font-size:24px;letter-spacing:6px;font-weight:800;color:{ORO}}}
.top .q{{font-family:Inter,sans-serif;font-size:27px;color:{GRIS};margin-top:18px;letter-spacing:1px}}
.tit{{font-size:112px;line-height:.95;color:{TINTA};letter-spacing:-2px;margin-top:40px}}
.tit b{{display:block;color:{VINO};font-style:italic;font-weight:600;font-size:74px;margin-top:14px}}
.ln{{width:200px;height:4px;background:{ORO};margin:44px auto}}
.met{{font-size:38px;font-style:italic;color:{GRIS}}}
.ru{{display:flex;justify-content:center;gap:14px;margin:60px 0 10px}}
.ru i{{width:120px;height:120px;border-radius:50%;background:#F0E7D2;border:6px solid {ORO};position:relative}}
.ru i:nth-child(2){{background:#F7F2E6;border-color:{VINO};margin-top:30px}}
.ru i:nth-child(3){{background:#EFE3C8}}
.ru i:after{{content:"";position:absolute;left:28px;top:34px;width:16px;height:16px;border-radius:50%;background:rgba(0,0,0,.14);
 box-shadow:34px 10px 0 rgba(0,0,0,.12), 14px 40px 0 rgba(0,0,0,.10)}}
.pie{{font-family:Inter,sans-serif;font-size:27px;letter-spacing:4px;font-weight:800;color:{TINTA}}}
.pie span{{color:{ORO};margin:0 10px}}
</style></head><body>
<div class="hoja">
  <div class="esp">{'<i></i>' * 18}</div>
  <div class="top">
    <div class="k">CARTILLA PRACTICA 2026</div>
    <div class="q">De la cocina de tu casa al mostrador</div>
    <div class="tit">ORO BLANCO<b>Recetas rentables de la leche</b></div>
    <div class="ln"></div>
    <div class="met">Paso a paso, con fotos, sin término difícil</div>
  </div>
  <div class="ru"><i></i><i></i><i></i></div>
  <div class="pie">RECETAS<span>&middot;</span>RENDIMIENTO<span>&middot;</span>VENTA</div>
</div></body></html>"""

SUMARIO = pagina(
    'SUMARIO',
    'Todo lo que <em>vas a aprender</em>',
    'Cuatro bloques, en orden. No es información suelta: es una secuencia que puedes seguir desde hoy.',
    """<ol>
      <li><b>Guía de producción segura y sin desperdicio.</b> Los errores que te hacen perder leche, dinero y calidad.</li>
      <li><b>Los pilares de la rentabilidad de la leche.</b> Cómo subir el rendimiento de cada tanda.</li>
      <li><b>Diez recetas paso a paso.</b> Quesos, rellenos, queso crema, yogur y dulce de leche.</li>
      <li><b>Aprovechamiento del suero.</b> Ricota, crema de ricota y bebida láctea.</li>
    </ol>""",
    extra=f"""<style>
ol{{counter-reset:n;list-style:none}}
li{{counter-increment:n;position:relative;padding-left:110px;margin-bottom:74px;font-size:35px;
 color:{TINTA};line-height:1.45}}
li:before{{content:counter(n);position:absolute;left:0;top:-6px;width:74px;height:74px;border-radius:50%;
 background:{ORO};color:#fff;font-family:Inter,sans-serif;font-weight:800;font-size:40px;
 display:flex;align-items:center;justify-content:center}}
li b{{font-family:Inter,sans-serif;font-weight:800;display:block;margin-bottom:6px}}
</style>""")

REL = pagina(
    'QUESOS RELLENOS',
    'Los cinco que <em>se venden solos</em>',
    'El relleno es lo que te saca de la pelea de precio. Punto del queso, proporción y corte.',
    ''.join(
        f'<div class="e"><div class="bar" style="background:{c}"></div><div class="tx">'
        f'<div class="n">{n}</div><div class="c">{s}</div><div class="d">{d}</div></div></div>'
        for n, s, d, c in RELLENOS),
    extra=f"""<style>
.e{{display:flex;gap:30px;align-items:stretch;margin-bottom:56px}}
.bar{{width:16px;border-radius:8px}}
.e .n{{font-family:Inter,sans-serif;font-size:44px;font-weight:800;color:{TINTA};letter-spacing:.5px}}
.e .c{{font-size:30px;font-style:italic;color:{VINO};margin-top:2px}}
.e .d{{font-size:30px;color:{TINTA};opacity:.78;margin-top:8px;line-height:1.4}}
</style>""")

SUE = pagina(
    'APROVECHAMIENTO DEL SUERO',
    'Lo que la mayoria <em>tira</em>',
    'De cada tanda de queso sale suero. De ese suero salen tres productos más, sin comprar un litro de leche.',
    ''.join(
        f'<div class="f"><div class="n">{n}</div><div class="m">{m}</div><div class="d">{d}</div></div>'
        for n, m, d in SUERO) +
    '<div class="nota">Mismo dia, mismo trabajo, misma leche. La diferencia es que sale tres veces '
    'en vez de una.</div>',
    extra=f"""<style>
.f{{border-bottom:2px dotted #DDD6C9;padding:46px 0}}
.f .n{{font-family:Inter,sans-serif;font-size:42px;font-weight:800;color:{TINTA};letter-spacing:.5px}}
.f .m{{font-size:32px;color:{ORO};font-style:italic;margin-top:4px;font-weight:600}}
.f .d{{font-size:30px;color:{GRIS};margin-top:8px;line-height:1.4}}
.nota{{margin-top:50px;background:#F4EEE1;border-left:9px solid {ORO};padding:34px 32px;
 font-size:30px;color:{TINTA};line-height:1.45;font-style:italic}}
</style>""")

REND = pagina(
    'RENDIMIENTO',
    'Diez litros, <em>dos resultados</em>',
    'La misma leche, el mismo tiempo. Lo único que cambia es qué receta eliges.',
    """<div class="dos">
      <div class="mal"><div class="t">UNA SOLA RECETA</div>
        <div class="p">1 queso fresco tradicional.<br>Una pieza para vender.<br>Precio de mercado, sin margen para mover.</div></div>
      <div class="bien"><div class="t">LA CARTILLA</div>
        <div class="p">3 quesos rellenos de medio kilo.<br>3 botellas de bebida láctea con el suero.<br>Seis piezas, y cada una se paga más.</div></div>
    </div>
    <div class="nota">La diferencia no está en la vaca ni en la cantidad de leche: está en qué sabes
    hacer con ella.</div>""",
    extra=f"""<style>
.dos{{display:flex;gap:26px}}
.mal,.bien{{flex:1;border-radius:12px;padding:38px 32px}}
.mal{{background:#F2EFE8;border:3px solid #B8B0A2}}
.bien{{background:#F6EEDC;border:3px solid {ORO}}}
.t{{font-family:Inter,sans-serif;font-size:26px;font-weight:800;letter-spacing:3px}}
.mal .t{{color:#8A8275}} .bien .t{{color:{ORO}}}
.p{{font-size:31px;color:{TINTA};line-height:1.55;margin-top:16px}}
.nota{{margin-top:50px;background:#F4EEE1;border-left:9px solid {VINO};padding:34px 32px;
 font-size:30px;color:{TINTA};line-height:1.45;font-style:italic}}
</style>""")

YOG = pagina(
    'YOGUR PREMIUM',
    'El que se vende <em>todos los días</em>',
    'No necesita maduración, sale el mismo día y acepta todas las versiones que quieras.',
    """<ol>
      <li><b>El punto exacto.</b> Temperatura, tiempo y cuándo cortar la fermentación.</li>
      <li><b>Textura firme sin aditivo.</b> Qué hacer para que no quede aguado ni se separe.</li>
      <li><b>Mermelada con trozos en el fondo.</b> La capa que lo convierte en premium.</li>
      <li><b>Envase y etiqueta.</b> Cómo se presenta para que valga lo que vale.</li>
      <li><b>Duración y rotación.</b> Cuánto aguanta y cuánto producir por semana.</li>
    </ol>""",
    extra=f"""<style>
ol{{counter-reset:n;list-style:none}}
li{{counter-increment:n;position:relative;padding-left:104px;margin-bottom:62px;font-size:34px;
 color:{TINTA};line-height:1.45}}
li:before{{content:counter(n);position:absolute;left:0;top:-4px;width:72px;height:72px;border-radius:50%;
 background:{VINO};color:#fff;font-family:Inter,sans-serif;font-weight:800;font-size:40px;
 display:flex;align-items:center;justify-content:center}}
li b{{font-family:Inter,sans-serif;font-weight:800}}
</style>""")

CAR = pagina(
    'TU CARTA COMPLETA',
    'Doce productos de <em>un solo tacho</em>',
    'El cliente que viene por el yogur se lleva el queso. El que viene por el queso se lleva el dulce.',
    '<div class="gr">' + ''.join(
        f'<div class="m"><b>{n}</b><span>{t}</span></div>' for n, t in CARTA) + '</div>',
    extra=f"""<style>
.gr{{display:grid;grid-template-columns:1fr 1fr;gap:22px}}
.m{{background:#fff;border:2px solid #EDE7DC;border-radius:10px;padding:26px 22px;border-left:9px solid {ORO}}}
.m:nth-child(even){{border-left-color:{VINO}}}
.m b{{display:block;font-family:Inter,sans-serif;font-size:28px;font-weight:800;color:{TINTA};line-height:1.2}}
.m span{{display:block;font-size:26px;color:{GRIS};margin-top:7px;line-height:1.3}}
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


for html, name in [(TAPA, 'tapa'), (SUMARIO, 'sumario'), (REL, 'rellenos'),
                   (SUE, 'suero'), (REND, 'rendimiento'), (YOG, 'yogur'), (CAR, 'carta')]:
    shot(html, name)
