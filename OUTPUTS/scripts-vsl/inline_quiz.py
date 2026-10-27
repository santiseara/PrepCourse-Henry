"""Deja un quiz autocontenido: mete cada imagen de CONFIG.IMG como data URI.
Así el HTML se pega entero en el custom_html de ImpulTienda sin subir nada aparte.
Uso: python3 inline_quiz.py <quiz.html> <salida.txt>
"""
import base64, io, mimetypes, os, re, sys
from PIL import Image

ANCHO_MAX = 1000     # el quiz es mobile: más de 1000 px no se ve y pesa el doble
CALIDAD = 86

ent, sal = sys.argv[1], sys.argv[2]
base = os.path.dirname(os.path.abspath(ent))
s = open(ent, encoding='utf-8').read()

tipos = {'.webp': 'image/webp', '.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.svg': 'image/svg+xml'}
hechas, faltan = 0, []

def reemplazo(m):
    global hechas
    ruta = m.group(1)
    if ruta.startswith(('data:', 'http://', 'https://')):
        return m.group(0)
    p = os.path.normpath(os.path.join(base, ruta))
    if not os.path.exists(p):
        faltan.append(ruta); return m.group(0)
    ext = os.path.splitext(p)[1].lower()
    datos = open(p, 'rb').read()
    tipo = tipos.get(ext) or mimetypes.guess_type(p)[0] or 'application/octet-stream'
    if ext != '.svg':
        # todo a webp y con tope de ancho: un PNG de 1,1 MB se vuelve 1,5 MB en base64
        im = Image.open(io.BytesIO(datos))
        if im.width > ANCHO_MAX:
            im = im.resize((ANCHO_MAX, round(im.height * ANCHO_MAX / im.width)), Image.LANCZOS)
        buf = io.BytesIO()
        im.save(buf, 'WEBP', quality=CALIDAD, method=6)
        if buf.tell() < len(datos) or ext == '.png':
            datos, tipo = buf.getvalue(), 'image/webp'
    hechas += 1
    return '"data:%s;base64,%s"' % (tipo, base64.b64encode(datos).decode())

s = re.sub(r'"((?:\.\./|\./)?[^"\s]+\.(?:webp|png|jpe?g|svg))"', reemplazo, s)
open(sal, 'w', encoding='utf-8').write(s)
print(f'{hechas} imágenes embebidas · {os.path.getsize(sal)//1024} KB → {sal}')
if faltan: print('NO ENCONTRADAS:', ', '.join(faltan))
