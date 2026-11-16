#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Monta un ad de Higado Liviano sobre el MP4 del avatar de HeyGen.

El avatar ya viene con la voz adentro (HeyGen la lipsincroniza desde el wav),
asi que aca no se toca el audio: se alinea con Whisper y se le pone encima la
edicion de Doutor Nature — placa de hook arriba, subtitulo corto quemado abajo,
chapas de puntaje y recuadros de comida, y placa final de CTA.

Uso:
  python3 edit_higado.py <avatar.mp4> <salida.mp4>
      --hook "MIRA LO QUE HACEN LOS HUEVOS CON TU HIGADO"
      [--cierre "HIGADO LIVIANO · 21 DIAS"]
      [--puntajes "cafe=5,huevos=3,aceite=4,ensalada=2,detox=0"]
      [--broll "12.0-15.5:clip1.mp4,22.0-25.0:clip2.mp4"]
      [--inset "5.0-8.0:cafe.mp4"]        recuadro de comida sobre el pecho
"""
import argparse, os, re, subprocess, unicodedata

FF = os.path.expanduser('~/.local/bin/ffmpeg')
if not os.path.exists(FF):
    FF = 'ffmpeg'
SCRATCH = ('/private/tmp/claude-501/-Users-santiagoseara-PrepCourse-Henry/'
           '5e3cbc82-95f4-48e0-b893-370e2e57fde2/scratchpad')
FUENTE = f'{SCRATCH}/fonts/Anton-Regular.ttf'
if not os.path.exists(FUENTE):
    FUENTE = '/System/Library/Fonts/Supplemental/Impact.ttf'

W, H = 1080, 1920
CAP_Y = int(H * 0.66)       # subtitulo a la altura de las manos (tapa el delator)
AMARILLO = 'FFD400'

ap = argparse.ArgumentParser()
ap.add_argument('src')
ap.add_argument('out')
ap.add_argument('--hook', default='')
ap.add_argument('--cierre', default='HIGADO LIVIANO · 21 DIAS')
ap.add_argument('--puntajes', default='')
ap.add_argument('--broll', default='')
ap.add_argument('--inset', default='')
ap.add_argument('--hooksec', type=float, default=2.6)
ap.add_argument('--cierresec', type=float, default=3.0)
A = ap.parse_args()

tmp = A.out + '_tmp'
os.makedirs(tmp, exist_ok=True)


def run(cmd):
    subprocess.run(cmd, check=True)


def dur(f):
    r = subprocess.run([FF, '-i', f], capture_output=True, text=True).stderr
    h, m, s = re.search(r'Duration: (\d+):(\d+):([\d.]+)', r).groups()
    return int(h) * 3600 + int(m) * 60 + float(s)


def esc(t):
    """Escapa para drawtext."""
    return (t.replace('\\', r'\\\\').replace(':', r'\:')
             .replace("'", r"\'").replace('%', r'\%')
             .replace(',', r'\,').replace('[', r'\[').replace(']', r'\]'))


def sinacentos(t):
    t = unicodedata.normalize('NFD', t)
    return ''.join(c for c in t if unicodedata.category(c) != 'Mn')


# ---------------------------------------------------------------------------
# 1. Palabras con tiempo, desde el audio del propio avatar
# ---------------------------------------------------------------------------
from faster_whisper import WhisperModel
modelo = WhisperModel('small', device='cpu', compute_type='int8')
segs, _ = modelo.transcribe(A.src, language='es', word_timestamps=True)
palabras = [(w.start, w.end, w.word.strip()) for s in segs for w in s.words if w.word.strip()]
D = dur(A.src)
print(f'  {len(palabras)} palabras · {D:.1f}s')

# ---------------------------------------------------------------------------
# 2. Subtitulos de 2-3 palabras, MAYUSCULAS, la clave en amarillo
# ---------------------------------------------------------------------------
CLAVE = re.compile(r'^(higado|grasa|hora|horas|cinco|cuatro|tres|dos|cero|nunca|nada|'
                   r'nadie|gratis|dieta|alarma|noche|cena|fruta|banana|huevos|cafe|'
                   r'aceite|ensalada|detox|manteca|cerveza|panceta|gaseosa|veintiun|'
                   r'dias|link|abajo|peor|mejor|solo|todo)$')

grupos = []
i = 0
while i < len(palabras):
    n = 3 if len(palabras) - i >= 3 else len(palabras) - i
    # cortar antes si hay un salto de tiempo grande (fin de frase)
    for k in range(1, n):
        if palabras[i + k][0] - palabras[i + k - 1][1] > 0.38:
            n = k
            break
    bloque = palabras[i:i + n]
    grupos.append((bloque[0][0], bloque[-1][1], [p[2] for p in bloque]))
    i += n

filtros = []
for ini, fin, ws in grupos:
    fin = max(fin, ini + 0.28)
    texto = ' '.join(sinacentos(w).upper() for w in ws)
    texto = re.sub(r'[^\w\s¿?¡!%/.]', '', texto).strip()
    if not texto:
        continue
    hay_clave = any(CLAVE.match(sinacentos(w).lower().strip('.,¿?¡!')) for w in ws)
    color = AMARILLO if hay_clave else 'FFFFFF'
    filtros.append(
        f"drawtext=fontfile='{FUENTE}':text='{esc(texto)}':"
        f"fontcolor=0x{color}:fontsize=74:borderw=9:bordercolor=black@0.92:"
        f"x=(w-text_w)/2:y={CAP_Y}:enable='between(t,{ini:.2f},{fin:.2f})'")

# ---------------------------------------------------------------------------
# 3. Placa de hook arriba (la caja negra de ellos) y placa final
# ---------------------------------------------------------------------------
def partir(texto, ancho):
    out, linea = [], ''
    for p in texto.split():
        if len(linea) + len(p) + 1 > ancho:
            out.append(linea); linea = p
        else:
            linea = (linea + ' ' + p).strip()
    if linea:
        out.append(linea)
    return out


if A.hook:
    lineas = partir(A.hook, 20)
    cuerpo, salto = 70, 88
    alto = salto * len(lineas) + 38
    filtros.append(
        f"drawbox=x=0:y=118:w={W}:h={alto}:color=black@0.84:t=fill:"
        f"enable='between(t,0,{A.hooksec})'")
    for n, l in enumerate(lineas):
        filtros.append(
            f"drawtext=fontfile='{FUENTE}':text='{esc(sinacentos(l).upper())}':"
            f"fontcolor=white:fontsize={cuerpo}:x=(w-text_w)/2:y={137 + n*salto}:"
            f"enable='between(t,0,{A.hooksec})'")

# chapas de puntaje: "5/10" grande en verde arriba del recuadro de comida
if A.puntajes:
    for item in A.puntajes.split(','):
        if '=' not in item:
            continue
        rango, val = item.split('=')
        a, b = [float(x) for x in rango.split('-')]
        filtros.append(
            f"drawtext=fontfile='{FUENTE}':text='{val}/10':fontcolor=0x27D17F:"
            f"fontsize=118:borderw=10:bordercolor=black@0.9:"
            f"x=(w-text_w)/2:y={int(H*0.53)}:enable='between(t,{a},{b})'")

# placa final
ini_cierre = max(0.0, D - A.cierresec)
filtros.append(
    f"drawbox=x=0:y=0:w={W}:h={H}:color=0x0E1216@0.97:t=fill:"
    f"enable='gte(t,{ini_cierre})'")
lc = partir(A.cierre, 16)
cuerpo_c = 86 if len(lc) > 1 else 78
for n, l in enumerate(lc):
    filtros.append(
        f"drawtext=fontfile='{FUENTE}':text='{esc(sinacentos(l).upper())}':"
        f"fontcolor=white:fontsize={cuerpo_c}:x=(w-text_w)/2:"
        f"y={int(H*0.40) + n*(cuerpo_c+16)}:enable='gte(t,{ini_cierre})'")
filtros.append(
    f"drawtext=fontfile='{FUENTE}':text='EL LINK ESTA ABAJO':"
    f"fontcolor=0x{AMARILLO}:fontsize=58:x=(w-text_w)/2:"
    f"y={int(H*0.40) + len(lc)*(cuerpo_c+16) + 28}:enable='gte(t,{ini_cierre})'")

# ---------------------------------------------------------------------------
# 4. Armado
# ---------------------------------------------------------------------------
base = (f"scale={W}:{H}:force_original_aspect_ratio=increase,"
        f"crop={W}:{H},setsar=1,fps=30")
cadena = base + ',' + ','.join(filtros)
vf = f'{tmp}/vf.txt'
open(vf, 'w').write(cadena)

print(f'  {len(grupos)} subtitulos · placa de hook: {"si" if A.hook else "no"}')
run([FF, '-v', 'error', '-y', '-i', A.src,
     '-filter_complex_script', vf,
     '-c:v', 'libx264', '-preset', 'medium', '-crf', '21',
     '-pix_fmt', 'yuv420p', '-r', '30',
     '-c:a', 'aac', '-b:a', '128k', '-af', 'loudnorm=I=-14:TP=-1.5:LRA=11',
     '-movflags', '+faststart', A.out])

print(f'OK  {A.out}  {dur(A.out):.1f}s')
