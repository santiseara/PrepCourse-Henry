"""Deja el quiz de Limpia Dolor autocontenido para el custom_html de ImpulTienda.

Embebe en base64 las imágenes (a WebP, con tope de ancho) y los audios .mp3.
Los videos NO se embeben por defecto: los 6 pesan 1,9 MB y el .txt se iría a ~4 MB.
Con VIDEOS=1 se embeben igual, para probar cuánto aguanta la tienda.

Uso:  python3 empaquetar_limpia_dolor.py <quiz.html> <salida.txt>
Env:  ANCHO_MAX (900) · CALIDAD (80) · VIDEOS (0/1)
"""
import base64, io, os, re, sys
from PIL import Image

ANCHO_MAX = int(os.environ.get("ANCHO_MAX", 900))
CALIDAD   = int(os.environ.get("CALIDAD", 80))
VIDEOS    = os.environ.get("VIDEOS", "0") == "1"

ent, sal = sys.argv[1], sys.argv[2]
base = os.path.dirname(os.path.abspath(ent))
s = open(ent, encoding="utf-8").read()

TIPOS = {".webp":"image/webp", ".png":"image/png", ".jpg":"image/jpeg",
         ".jpeg":"image/jpeg", ".svg":"image/svg+xml", ".mp3":"audio/mpeg", ".mp4":"video/mp4"}
hechas, faltan, pesos = 0, [], {}

def reemplazo(m):
    global hechas
    ruta = m.group(1)
    if ruta.startswith(("data:", "http://", "https://")):
        return m.group(0)
    ext = os.path.splitext(ruta)[1].lower()
    if ext == ".mp4" and not VIDEOS:
        return m.group(0)                      # se queda como URL relativa
    p = os.path.normpath(os.path.join(base, ruta))
    if not os.path.exists(p):
        faltan.append(ruta); return m.group(0)
    datos = open(p, "rb").read()
    tipo = TIPOS.get(ext, "application/octet-stream")
    if ext in (".webp", ".png", ".jpg", ".jpeg"):
        im = Image.open(io.BytesIO(datos))
        if im.width > ANCHO_MAX:
            im = im.resize((ANCHO_MAX, round(im.height * ANCHO_MAX / im.width)), Image.LANCZOS)
        buf = io.BytesIO(); im.save(buf, "WEBP", quality=CALIDAD, method=6)
        if buf.tell() < len(datos):
            datos, tipo = buf.getvalue(), "image/webp"
    hechas += 1
    pesos[os.path.basename(ruta)] = len(datos)
    return '"data:%s;base64,%s"' % (tipo, base64.b64encode(datos).decode())

s = re.sub(r'"((?:\.\./|\./)?[^"\s]+\.(?:webp|png|jpe?g|svg|mp3|mp4))"', reemplazo, s)
open(sal, "w", encoding="utf-8").write(s)

kb = os.path.getsize(sal) // 1024
print("%d archivos embebidos · %d KB → %s" % (hechas, kb, sal))
for n, w in sorted(pesos.items(), key=lambda t: -t[1])[:6]:
    print("   %-26s %5d KB" % (n, w // 1024))
if faltan:
    print("NO ENCONTRADAS:", ", ".join(sorted(set(faltan))))
    sys.exit(1)
