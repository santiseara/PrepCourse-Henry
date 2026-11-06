# -*- coding: utf-8 -*-
"""Inserts de producto de DanceGo (Argentina, 2026-11-06).

DanceGo (el original brasileño) mete en casi todos sus ads la pantalla de la app en un celular y
la comunidad de WhatsApp. Acá se dibujan las dos por código (HTML + Chrome headless), con la
paleta de nuestra landing: papel crema, tinta y UN acento frambuesa. No cuesta nada y no hace
falta que la app exista para lanzar la tanda.

Cada insert sale sobre un lienzo 1.20x con el sobrante desenfocado, porque el editor le mete a
las fotos fijas un zoom de 1.0 a 1.14 más un golpe de 1.16 por corte y si no se le come la
cabecera y el pie (regla del 2026-11-05).

Uso: python3 gfx_dancego.py
"""
import os, subprocess
from PIL import Image, ImageFilter

OUT = os.path.expanduser('~/Desktop/dancego/anuncios/work/gfx')
os.makedirs(OUT, exist_ok=True)
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
W, H = 1080, 1920
MW, MH = 1296, 2304            # 1.20x

PAPER, INK, ACC, GREEN = '#FBF8F4', '#1C1A19', '#B23A5B', '#216B4F'

CLASES = [
    ('CUMBIA', '10 min', '#B23A5B'),
    ('CUARTETO', '12 min', '#8E4A2E'),
    ('SALSA', '14 min', '#216B4F'),
    ('BACHATA', '10 min', '#3B3A6B'),
    ('REGGAETÓN', '12 min', '#6B2F55'),
    ('SUAVE', '8 min', '#4A5A3A'),
]

APP = f"""<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap" rel="stylesheet">
<style>
*{{margin:0;padding:0;box-sizing:border-box;font-family:Inter,-apple-system,sans-serif}}
body{{width:{W}px;height:{H}px;background:#17141A;display:flex;align-items:center;justify-content:center;overflow:hidden}}
.tel{{width:800px;height:1620px;background:#0B0A0C;border-radius:76px;padding:16px;box-shadow:0 50px 90px rgba(0,0,0,.55)}}
.sc{{width:100%;height:100%;background:{PAPER};border-radius:62px;overflow:hidden;position:relative}}
.top{{padding:52px 44px 18px}}
.hola{{font-size:30px;color:#6B6560;font-weight:600}}
.marca{{font-size:58px;font-weight:800;color:{INK};letter-spacing:-1.5px;margin-top:4px}}
.marca span{{color:{ACC}}}
.des{{margin:26px 44px 0;background:{INK};border-radius:28px;padding:30px 34px;color:#fff}}
.des .k{{font-size:24px;letter-spacing:2.4px;color:#C9A9B4;font-weight:700}}
.des .t{{font-size:44px;font-weight:800;margin-top:8px}}
.bar{{height:16px;background:#3A3537;border-radius:10px;margin-top:22px;overflow:hidden}}
.bar i{{display:block;height:100%;width:39%;background:{ACC};border-radius:10px}}
.des .p{{font-size:26px;color:#BDB6B1;margin-top:14px;font-weight:600}}
.tit{{margin:38px 44px 0;font-size:30px;font-weight:800;color:{INK};letter-spacing:.4px}}
.grid{{margin:20px 44px 0;display:grid;grid-template-columns:1fr 1fr;gap:22px}}
.card{{border-radius:24px;overflow:hidden;background:#fff;border:2px solid #EDE6DD}}
.th{{height:220px;display:flex;align-items:center;justify-content:center;position:relative}}
.th b{{width:78px;height:78px;border-radius:50%;background:rgba(255,255,255,.92);display:flex;align-items:center;justify-content:center}}
.th b:after{{content:"";border-left:26px solid {INK};border-top:16px solid transparent;border-bottom:16px solid transparent;margin-left:7px}}
.cap{{padding:18px 20px}}
.cap .n{{font-size:28px;font-weight:800;color:{INK}}}
.cap .m{{font-size:24px;color:#857D77;font-weight:600;margin-top:2px}}
.vivo{{position:absolute;left:44px;right:44px;bottom:46px;background:{GREEN};color:#fff;border-radius:22px;
       padding:26px 30px;display:flex;align-items:center;gap:16px}}
.dot{{width:18px;height:18px;border-radius:50%;background:#8BE8B6}}
.vivo .a{{font-size:30px;font-weight:800;letter-spacing:.3px}}
.vivo .b2{{margin-left:auto;font-size:26px;font-weight:700;opacity:.9}}
</style></head><body>
<div class="tel"><div class="sc">
  <div class="top"><div class="hola">Hola, Romi 👋</div><div class="marca">Dance<span>Go</span></div></div>
  <div class="des"><div class="k">DESAFÍO DE 28 DÍAS</div><div class="t">Día 11 de 28</div>
    <div class="bar"><i></i></div><div class="p">10 minutos hoy · 7 días seguidos 🔥</div></div>
  <div class="tit">Elegí tu ritmo de hoy</div>
  <div class="grid">
    {''.join(f'<div class="card"><div class="th" style="background:{c}"><b></b></div><div class="cap"><div class="n">{n}</div><div class="m">{m} · principiante</div></div></div>' for n, m, c in CLASES)}
  </div>
  <div class="vivo"><div class="dot"></div><div class="a">CLASE EN VIVO</div><div class="b2">martes 19 h</div></div>
</div></div>
</body></html>"""

MSJ = [
    ('Vale', '#B23A5B', 'Chicas, día 11 y no falté ni uno 🙌'),
    ('Romi', '#216B4F', 'Yo bailo mientras se hace la cena jajaja'),
    ('Caro', '#8E4A2E', 'Hoy hice la de cumbia con mi hija, terminamos muertas 😂'),
    ('Flor', '#3B3A6B', '¿Alguien va a la clase en vivo del martes?'),
    ('Vale', '#B23A5B', 'Yo! Y ayer puse la de bachata dos veces seguidas'),
    ('Romi', '#216B4F', 'Subí la receta de la tarta liviana al grupo 📎'),
]

WPP = f"""<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap" rel="stylesheet">
<style>
*{{margin:0;padding:0;box-sizing:border-box;font-family:Inter,-apple-system,sans-serif}}
body{{width:{W}px;height:{H}px;background:#17141A;display:flex;align-items:center;justify-content:center;overflow:hidden}}
.tel{{width:800px;height:1620px;background:#0B0A0C;border-radius:76px;padding:16px;box-shadow:0 50px 90px rgba(0,0,0,.55)}}
.sc{{width:100%;height:100%;background:#E7E0D7;border-radius:62px;overflow:hidden;display:flex;flex-direction:column}}
.hd{{background:{INK};color:#fff;padding:54px 36px 26px;display:flex;align-items:center;gap:20px}}
.av{{width:78px;height:78px;border-radius:50%;background:{ACC};display:flex;align-items:center;justify-content:center;font-size:36px;font-weight:800}}
.hd .n{{font-size:36px;font-weight:800}}
.hd .s{{font-size:24px;color:#B9B2AC;margin-top:4px}}
.ch{{flex:1;padding:34px 30px;display:flex;flex-direction:column;gap:26px;justify-content:flex-end}}
.row{{display:flex}}
.b{{max-width:78%;background:#fff;border-radius:22px;padding:20px 24px;box-shadow:0 2px 3px rgba(0,0,0,.09)}}
.who{{font-size:24px;font-weight:800;margin-bottom:6px}}
.tx{{font-size:30px;color:#20201E;line-height:1.3}}
.hr{{font-size:20px;color:#9A938C;text-align:right;margin-top:8px}}
.ft{{background:#DCD4CA;padding:26px 30px;font-size:26px;color:#6E675F}}
</style></head><body>
<div class="tel"><div class="sc">
  <div class="hd"><div class="av">DG</div><div><div class="n">DanceGo · Comunidad</div><div class="s">218 integrantes · en línea</div></div></div>
  <div class="ch">
    {''.join(f'<div class="row"><div class="b"><div class="who" style="color:{c}">{n}</div><div class="tx">{t}</div><div class="hr">20:4{i}</div></div></div>' for i, (n, c, t) in enumerate(MSJ))}
  </div>
  <div class="ft">Escribí un mensaje…</div>
</div></div>
</body></html>"""


def shot(html, name):
    p = f'{OUT}/_{name}.html'
    open(p, 'w').write(html)
    subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--hide-scrollbars',
                    f'--window-size={W},{H}', f'--screenshot={OUT}/_{name}.png',
                    '--virtual-time-budget=4000', 'file://' + p], check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    im = Image.open(f'{OUT}/_{name}.png').convert('RGB').resize((W, H), Image.LANCZOS)
    bg = im.resize((MW, MH), Image.LANCZOS).filter(ImageFilter.GaussianBlur(26))
    bg = Image.blend(bg, Image.new('RGB', (MW, MH), (16, 14, 18)), 0.35)
    bg.paste(im, ((MW - W) // 2, (MH - H) // 2))
    bg.save(f'{OUT}/{name}.png')
    os.remove(f'{OUT}/_{name}.html'); os.remove(f'{OUT}/_{name}.png')
    print(f'{OUT}/{name}.png')


shot(APP, 'app')
shot(WPP, 'wpp')
