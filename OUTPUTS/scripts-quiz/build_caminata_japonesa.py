#!/usr/bin/env python3
"""Clon del quiz de Caminata Oriental (test.caminata-oriental.com) -> Caminata Japonesa.

Regla del 14/11: su HTML, su CSS y su motor; cambian solo palabras, imagenes con marca y config.
Uso: python3 build_caminata_japonesa.py <work-orig> <imagenes-nuevas> <salida.txt>
  work-orig: index.html, app.js, app.css, img/ bajados con curl
"""
import base64, io, os, re, sys
from PIL import Image

ORIG, NUEVAS, SALIDA = sys.argv[1:4]
CHECKOUT = os.environ.get("CHECKOUT", "/checkout")
PIXEL = os.environ.get("PIXEL_ID", "")


def decode(x):
    x = re.sub(r'\\u\{([0-9A-Fa-f]+)\}', lambda m: chr(int(m.group(1), 16)), x)
    x = re.sub(r'\\u([0-9A-Fa-f]{4})', lambda m: chr(int(m.group(1), 16)), x)
    x = re.sub(r'\\x([0-9A-Fa-f]{2})', lambda m: chr(int(m.group(1), 16)), x)
    return x


js = decode(open(os.path.join(ORIG, "app.js"), encoding="utf-8").read())
css = open(os.path.join(ORIG, "app.css"), encoding="utf-8").read()

# ---------- textos: cada par TIENE que aparecer ----------
PARES = [
    ('title:"Caminata Tai Chi para bajar de peso"', 'title:"Caminata Japonesa para bajar de peso"'),
    ('¿Alguna vez probaste la Caminata Tai Chi?', '¿Alguna vez probaste la Caminata Japonesa?'),
    ('<p>La Caminata Tai Chi mejora el equilibrio', '<p>La Caminata Japonesa mejora el equilibrio'),
    ('Combina caminata con movimientos fluidos de Tai Chi.', 'Combina caminata con movimientos suaves de la tradición japonesa.'),
    ('Caminata Tai Chi: movimiento suave, resultados reales', 'Caminata Japonesa: movimiento suave, resultados reales'),
    ('La Caminata Tai Chi consciente te ayuda', 'La Caminata Japonesa consciente te ayuda'),
    ('La Caminata Tai Chi convierte tu casa', 'La Caminata Japonesa convierte tu casa'),
    ('brand:"Caminata Oriental"', 'brand:"Caminata Japonesa"'),
    ('productName:"Plan personalizado de Caminata Tai Chi"', 'productName:"Plan personalizado de Caminata Japonesa"'),
    ('¿Necesito experiencia previa en Caminata Tai Chi?', '¿Necesito experiencia previa en Caminata Japonesa?'),
    ('incluso si nunca practicaste Tai Chi.', 'incluso si nunca practicaste Caminata Japonesa.'),
    ('Tu plan personalizado de Caminata Tai Chi está listo', 'Tu plan personalizado de Caminata Japonesa está listo'),
    # stack del competidor: afuera
    ('metaPixelId:"27539384562427720"', 'metaPixelId:"%s"' % PIXEL),
    ('collectUrl:"api/track.php"', 'collectUrl:""'),
    ('checkoutUrl:"https://pago.caminata-oriental.com/"', 'checkoutUrl:"%s"' % CHECKOUT),
    # checkout relativo: new URL necesita base
    ('t=new URL(v.checkoutUrl);', 't=new URL(v.checkoutUrl,location.href);'),
    # regla 14/11: el quiz arranca SIEMPRE en la portada
    ('JSON.parse(sessionStorage.getItem("co_state")||"{}")', '(sessionStorage.removeItem("co_state"),{})'),
    # su id de sesion no se manda al checkout
    ('t.searchParams.set("quiz_session",e),', ''),
]
for viejo, nuevo in PARES:
    n = js.count(viejo)
    assert n >= 1, "NO MATCHEA: " + viejo
    js = js.replace(viejo, nuevo)
# lo que queda de la marca (alts, semanas, FAQ de acceso, footer)
js = js.replace("Caminata Oriental", "Caminata Japonesa")

# ---------- imagenes embebidas ----------
ROLES_GRANDES = {"testimonial-1", "testimonial-2", "testimonial-3", "app-mockup", "walking"}


def webp_b64(path, key):
    im = Image.open(path)
    alfa = 'A' in im.getbands() or im.mode == 'P'
    im = im.convert('RGBA' if alfa else 'RGB')
    maxw = 640 if key in ROLES_GRANDES else 720
    if im.width > maxw:
        im = im.resize((maxw, round(im.height * maxw / im.width)), Image.LANCZOS)
    raw = open(path, 'rb').read()
    buf = io.BytesIO()
    im.save(buf, 'WEBP', quality=72, method=6)
    data = buf.getvalue()
    if len(raw) < len(data) and key not in NUEVAS_KEYS:  # el original ya es mas chico
        data = raw
    return 'data:image/webp;base64,' + base64.b64encode(data).decode(), im.size


NUEVAS_KEYS = {f[:-5] for f in os.listdir(NUEVAS) if f.endswith('.webp')}
keys = re.search(r'var Y=\[(.*?)\]', js).group(1)
keys = re.findall(r'"([^"]+)"', keys)
IMG = {}
for k in keys:
    p = os.path.join(NUEVAS, k + '.webp')
    if not os.path.exists(p):
        p = os.path.join(ORIG, 'img', k + '.webp')
    IMG[k], size = webp_b64(p, k)
# el logo cambio de medida
js = js.replace('logo:[800,278]', 'logo:[820,281]')
assert 'logo:[820,281]' in js

# Q() deja de apuntar a img/ y lee del mapa (convertido a blob una vez, regla 16/11)
viejo_q = 'function Q(e){return Se.has(e)?{src:`img/${e}.webp`,fallback:""}:{src:"",fallback:""}}'
assert js.count(viejo_q) == 1
js = js.replace(viejo_q, 'function Q(e){return Se.has(e)&&window.IMG[e]?{src:window.IMG[e],fallback:window.IMGRAW[e]||""}:{src:"",fallback:""}}')
# regla 16/11: nada de lazy en imagenes insertadas por JS
viejo_lazy = """${i?'fetchpriority="high"':'loading="lazy"'} decoding="async">"""
assert js.count(viejo_lazy) == 1
js = js.replace(viejo_lazy, 'loading="eager" decoding="sync" fetchpriority="high">')

img_js = "window.IMGRAW={%s};" % ",".join('"%s":"%s"' % (k, v) for k, v in IMG.items())
img_js += """
(function(){window.IMG={};window.__pre=[];for(var k in IMGRAW){var u=IMGRAW[k];try{var c=u.indexOf(','),b=atob(u.slice(c+1)),a=new Uint8Array(b.length);for(var i=0;i<b.length;i++)a[i]=b.charCodeAt(i);IMG[k]=URL.createObjectURL(new Blob([a],{type:'image/webp'}));}catch(e){IMG[k]=u}var im=new Image();im.src=IMG[k];if(im.decode)im.decode().catch(function(){});__pre.push(im);}})();
"""

# ---------- documento ----------
html = open(os.path.join(ORIG, 'index.html'), encoding='utf-8').read()
html = html.replace('Caminata Oriental · Tu plan de Caminata Tai Chi', 'Caminata Japonesa · Tu plan de Caminata Japonesa')
html = html.replace('plan personalizado de Caminata Tai Chi para mujeres +40', 'plan personalizado de Caminata Japonesa para mujeres +40')
html = re.sub(r'\s*<link rel="preload" as="image" href="img/age-50.webp">', '', html)
html = html.replace('<link rel="icon" href="img/logo.webp">', '')
html = html.replace('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600..700&display=swap">',
                    '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600..700&display=swap" media="print" onload="this.media=\'all\'">')
html = html.replace('<link rel="stylesheet" href="app.css">', '<style>\n' + css + '\n</style>')
html = html.replace('<script type="module" src="app.js"></script>',
                    '<script>\n' + img_js + '</script>\n<script type="module">\n' + js + '\n</script>')
assert '<style>' in html and 'window.IMGRAW' in html

sin_b64 = re.sub(r'data:image/webp;base64,[A-Za-z0-9+/=]+', '', html)
for rastro in ['Tai Chi', 'Oriental', 'caminata-oriental', '27539384562427720', 'track.php', 'img/']:
    assert rastro not in sin_b64, 'QUEDA RASTRO: ' + rastro

open(SALIDA, 'w', encoding='utf-8').write(html)
print('ok', SALIDA, round(len(html.encode()) / 1024), 'KB', len(IMG), 'imagenes')
