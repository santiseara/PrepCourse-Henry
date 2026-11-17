#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Monta un ad de Higado Liviano con la edicion de Doutor Nature.

El avatar de HeyGen ya trae la voz adentro. Sobre eso se hace lo que hacen ellos:

  1. se le sacan los silencios (jump cut), video y audio juntos, para que no haya aire muerto
  2. se acelera todo parejo, asi el lipsync no se mueve
  3. se corta a B-ROLL DE COMIDA cada pocos segundos, sin tocar la voz, que sigue corriendo
  4. los tramos de avatar alternan plano normal y punch-in
  5. encima van el subtitulo corto, la placa de hook, las chapas de puntaje y la placa final
  6. y abajo una cama musical con ducking

Uso:
  python3 edit_higado.py <avatar.mp4> <salida.mp4> --hook "..." [--cierre "..."]
      [--puntajes "a-b=5,..."] [--broll carpeta] [--cada 6.5] [--largo 2.0]
      [--speed 1.12] [--placa "12.0:LOS TRES PEORES"] [--sinbroll]
"""
import argparse, glob, os, random, re, subprocess, unicodedata

FF = os.path.expanduser('~/.local/bin/ffmpeg')
if not os.path.exists(FF):
    FF = 'ffmpeg'
SCRATCH = ('/private/tmp/claude-501/-Users-santiagoseara-PrepCourse-Henry/'
           '5e3cbc82-95f4-48e0-b893-370e2e57fde2/scratchpad')
FUENTE = f'{SCRATCH}/fonts/Anton-Regular.ttf'
if not os.path.exists(FUENTE):
    FUENTE = '/System/Library/Fonts/Supplemental/Impact.ttf'
MUSICA = '/Users/santiagoseara/PrepCourse-Henry/OUTPUTS/scripts-vsl/music_activa.py'

W, H = 1080, 1920
CAP_Y = int(H * 0.66)
AMARILLO = 'FFD400'
GAP, KEEP = 0.46, 0.17          # silencio minimo a recortar / aire que se deja

ap = argparse.ArgumentParser()
ap.add_argument('src'); ap.add_argument('out')
ap.add_argument('--hook', default='')
ap.add_argument('--cierre', default='HIGADO LIVIANO · 21 DIAS')
ap.add_argument('--puntajes', default='')
ap.add_argument('--placa', default='')
ap.add_argument('--broll', default=os.path.expanduser('~/Desktop/higado-liviano/work/broll_ia'))
ap.add_argument('--clips', default='', help='nombres sin .mp4, en orden: cafe,huevos,aceite')
ap.add_argument('--cada', type=float, default=6.5)
ap.add_argument('--largo', type=float, default=2.0)
ap.add_argument('--speed', type=float, default=1.12)
ap.add_argument('--hooksec', type=float, default=2.4)
ap.add_argument('--cierresec', type=float, default=3.0)
ap.add_argument('--sinbroll', action='store_true')
ap.add_argument('--seed', type=int, default=7)
A = ap.parse_args()

tmp = A.out + '_tmp'
os.makedirs(tmp, exist_ok=True)
rng = random.Random(A.seed)


def run(c):
    subprocess.run(c, check=True)


def dur(f):
    r = subprocess.run([FF, '-i', f], capture_output=True, text=True).stderr
    h, m, s = re.search(r'Duration: (\d+):(\d+):([\d.]+)', r).groups()
    return int(h) * 3600 + int(m) * 60 + float(s)


def esc(t):
    return (t.replace('\\', r'\\\\').replace(':', r'\:').replace("'", r"\'")
             .replace('%', r'\%').replace(',', r'\,').replace('[', r'\[').replace(']', r'\]'))


def sinac(t):
    t = unicodedata.normalize('NFD', t)
    return ''.join(c for c in t if unicodedata.category(c) != 'Mn')


def partir(t, n):
    out, li = [], ''
    for p in t.split():
        if len(li) + len(p) + 1 > n:
            out.append(li); li = p
        else:
            li = (li + ' ' + p).strip()
    if li:
        out.append(li)
    return out


from faster_whisper import WhisperModel
modelo = WhisperModel('small', device='cpu', compute_type='int8')


def palabras(f):
    segs, _ = modelo.transcribe(f, language='es', word_timestamps=True)
    return [(w.start, w.end, w.word.strip()) for s in segs for w in s.words if w.word.strip()]


# ---------------------------------------------------------------------------
# PASO 1 · sacar los silencios (video y audio juntos) y acelerar parejo
# ---------------------------------------------------------------------------
D0 = dur(A.src)
ws = palabras(A.src)
tramos, ini = [], 0.0
for i in range(1, len(ws)):
    hueco = ws[i][0] - ws[i - 1][1]
    if hueco > GAP:
        fin = ws[i - 1][1] + KEEP
        # se guarda SIEMPRE: un tramo corto suele ser una palabra suelta entre dos
        # pausas (un "Tres." de puntaje). Descartarlo por corto se come la palabra.
        if fin > ini:
            tramos.append((ini, fin))
        ini = ws[i][0] - KEEP
tramos.append((ini, D0))
tramos = [(max(0, a), min(D0, b)) for a, b in tramos if b - a > 0.12]
quitado = D0 - sum(b - a for a, b in tramos)
print(f'  silencios: {len(tramos)-1} cortes, -{quitado:.1f}s')

sp = A.speed
pv = ''.join(f'[0:v]trim={a:.3f}:{b:.3f},setpts=PTS-STARTPTS[v{i}];' for i, (a, b) in enumerate(tramos))
pa = ''.join(f'[0:a]atrim={a:.3f}:{b:.3f},asetpts=PTS-STARTPTS[a{i}];' for i, (a, b) in enumerate(tramos))
cv = ''.join(f'[v{i}][a{i}]' for i in range(len(tramos)))
fc = (pv + pa + cv + f'concat=n={len(tramos)}:v=1:a=1[vc][ac];'
      f'[vc]setpts=PTS/{sp},fps=30[vs];[ac]atempo={sp}[as]')
paso1 = f'{tmp}/1_rapido.mp4'
run([FF, '-v', 'error', '-y', '-i', A.src, '-filter_complex', fc,
     '-map', '[vs]', '-map', '[as]', '-c:v', 'libx264', '-preset', 'veryfast',
     '-crf', '18', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '160k', paso1])
D = dur(paso1)
print(f'  {D0:.1f}s -> {D:.1f}s  (speed {sp})')

# ---------------------------------------------------------------------------
# PASO 2 · intercalar b-roll de comida sin tocar la voz, y punch-in en el avatar
# ---------------------------------------------------------------------------
paso2 = f'{tmp}/2_cortado.mp4'
if A.sinbroll:
    pool = []
elif A.clips:
    pool = [os.path.join(A.broll, c.strip() + '.mp4') for c in A.clips.split(',') if c.strip()]
    falta = [p for p in pool if not os.path.exists(p)]
    if falta:
        raise SystemExit('no encuentro: ' + ', '.join(os.path.basename(f) for f in falta))
else:
    pool = sorted(glob.glob(os.path.join(A.broll, '*.mp4')))

if pool:
    # ventanas de b-roll: arrancan despues del hook y paran antes del cierre
    t = max(A.hooksec + 1.2, 4.0)
    vents = []
    while t + A.largo < D - A.cierresec - 1.0:
        vents.append((t, t + A.largo))
        t += A.cada
    if not A.clips:
        rng.shuffle(pool)          # sin lista, se reparten al azar pero sin repetir seguido
    elegidos = [pool[i % len(pool)] for i in range(len(vents))]

    # plan: tramos de avatar y tramos de b-roll, cubriendo [0, D]
    plan, cur = [], 0.0
    for (a, b), cl in zip(vents, elegidos):
        if a > cur:
            plan.append(('av', cur, a))
        plan.append(('br', a, b, cl))
        cur = b
    if cur < D:
        plan.append(('av', cur, D))

    ins = ['-i', paso1]
    for p in plan:
        if p[0] == 'br':
            ins += ['-i', p[3]]
    partes, idx, n = [], 1, 0
    for p in plan:
        if p[0] == 'av':
            a, b = p[1], p[2]
            z = 1.0 if n % 2 == 0 else 1.16      # alterna plano y punch-in
            # todo tramo sale a 1080x1920/30fps: el concat exige que coincidan
            esc_ = (f'scale={W}:{H}:force_original_aspect_ratio=increase,'
                    f'crop={W}:{H},setsar=1,fps=30')
            if z == 1.0:
                partes.append(f'[0:v]trim={a:.3f}:{b:.3f},setpts=PTS-STARTPTS,{esc_}[p{n}];')
            else:
                cw, ch = int(W / z) // 2 * 2, int(H / z) // 2 * 2
                partes.append(f'[0:v]trim={a:.3f}:{b:.3f},setpts=PTS-STARTPTS,{esc_},'
                              f'crop={cw}:{ch}:(iw-{cw})/2:(ih-{ch})/3,scale={W}:{H},setsar=1[p{n}];')
        else:
            a, b, cl = p[1], p[2], p[3]
            dc = dur(cl)
            off = max(0.0, min(dc - (b - a) - 0.2, dc * 0.25))
            partes.append(f'[{idx}:v]trim={off:.2f}:{off + (b - a):.2f},setpts=PTS-STARTPTS,'
                          f'scale={W}:{H}:force_original_aspect_ratio=increase,'
                          f'crop={W}:{H},setsar=1,fps=30[p{n}];')
            idx += 1
        n += 1
    fc2 = ''.join(partes) + ''.join(f'[p{i}]' for i in range(n)) + f'concat=n={n}:v=1:a=0[vv]'
    run([FF, '-v', 'error', '-y'] + ins + ['-filter_complex', fc2,
         '-map', '[vv]', '-map', '0:a', '-c:v', 'libx264', '-preset', 'veryfast',
         '-crf', '18', '-pix_fmt', 'yuv420p', '-c:a', 'copy', '-shortest', paso2])
    print(f'  b-roll: {len(vents)} cortes de {A.largo}s')
else:
    paso2 = paso1
    print('  b-roll: ninguno')

# ---------------------------------------------------------------------------
# PASO 3 · subtitulos, placas y musica
# ---------------------------------------------------------------------------
ws2 = palabras(paso2)
CLAVE = re.compile(r'^(higado|grasa|hora|horas|cinco|cuatro|tres|dos|cero|nunca|nada|'
                   r'nadie|gratis|dieta|alarma|noche|cena|fruta|banana|huevos|cafe|'
                   r'aceite|ensalada|detox|manteca|cerveza|panceta|gaseosa|veintiun|'
                   r'dias|link|abajo|peor|mejor|solo|todo|balanza|peso)$')
grupos, i = [], 0
while i < len(ws2):
    n = 3 if len(ws2) - i >= 3 else len(ws2) - i
    for k in range(1, n):
        if ws2[i + k][0] - ws2[i + k - 1][1] > 0.3:
            n = k; break
    bl = ws2[i:i + n]
    grupos.append((bl[0][0], bl[-1][1], [p[2] for p in bl]))
    i += n

F = []
for a, b, wsx in grupos:
    b = max(b, a + 0.26)
    txt = re.sub(r'[^\w\s¿?¡!%/.]', '', ' '.join(sinac(w).upper() for w in wsx)).strip()
    if not txt:
        continue
    col = AMARILLO if any(CLAVE.match(sinac(w).lower().strip('.,¿?¡!')) for w in wsx) else 'FFFFFF'
    F.append(f"drawtext=fontfile='{FUENTE}':text='{esc(txt)}':fontcolor=0x{col}:"
             f"fontsize=76:borderw=9:bordercolor=black@0.92:x=(w-text_w)/2:y={CAP_Y}:"
             f"enable='between(t,{a:.2f},{b:.2f})'")

if A.hook:
    ls = partir(A.hook, 20)
    F.append(f"drawbox=x=0:y=112:w={W}:h={88*len(ls)+36}:color=black@0.84:t=fill:"
             f"enable='between(t,0,{A.hooksec})'")
    for n, l in enumerate(ls):
        F.append(f"drawtext=fontfile='{FUENTE}':text='{esc(sinac(l).upper())}':fontcolor=white:"
                 f"fontsize=70:x=(w-text_w)/2:y={131+n*88}:enable='between(t,0,{A.hooksec})'")

if A.placa:
    pt, ptx = A.placa.split(':', 1)
    pt = float(pt) / sp
    ls = partir(ptx, 18)
    F.append(f"drawbox=x=0:y={int(H*0.30)}:w={W}:h={96*len(ls)+40}:color=0xC02617@0.90:t=fill:"
             f"enable='between(t,{pt:.2f},{pt+2.4:.2f})'")
    for n, l in enumerate(ls):
        F.append(f"drawtext=fontfile='{FUENTE}':text='{esc(sinac(l).upper())}':fontcolor=white:"
                 f"fontsize=78:x=(w-text_w)/2:y={int(H*0.30)+22+n*96}:"
                 f"enable='between(t,{pt:.2f},{pt+2.4:.2f})'")

# Puntajes anclados a la COMIDA, no al numero: el corte de silencios y la velocidad
# mueven todos los tiempos, y Whisper escribe los puntajes como digitos ("5.") o
# directamente se come alguno. El nombre del alimento, en cambio, lo transcribe bien.
# Formato: --puntajes "cafe=5,huevos=3,aceite=4,ensalada=2"
if A.puntajes:
    plano = [sinac(w).lower().strip('.,¿?¡!') for _, _, w in ws2]
    usado, hall = 0, []
    for it in [x for x in A.puntajes.split(',') if '=' in x]:
        clave, val = [y.strip() for y in it.split('=')]
        pos = next((i for i in range(usado, len(plano)) if plano[i] == clave), None)
        if pos is None:
            print(f'  ! puntaje sin ancla: {clave}')
            continue
        usado = pos + 1
        hall.append((ws2[pos][1] + 0.2, val))
    print('  puntajes:', ' '.join(f'{t:.0f}s={v}' for t, v in hall) or '(ninguno)')
    for t, v in hall:
        F.append(f"drawtext=fontfile='{FUENTE}':text='{v}/10':fontcolor=0x27D17F:fontsize=122:"
                 f"borderw=11:bordercolor=black@0.9:x=(w-text_w)/2:y={int(H*0.50)}:"
                 f"enable='between(t,{t:.2f},{t+2.6:.2f})'")

D2 = dur(paso2)
ic = max(0.0, D2 - A.cierresec)
F.append(f"drawbox=x=0:y=0:w={W}:h={H}:color=0x0E1216@0.97:t=fill:enable='gte(t,{ic:.2f})'")
lc = partir(A.cierre, 16)
cc = 86 if len(lc) > 1 else 78
for n, l in enumerate(lc):
    F.append(f"drawtext=fontfile='{FUENTE}':text='{esc(sinac(l).upper())}':fontcolor=white:"
             f"fontsize={cc}:x=(w-text_w)/2:y={int(H*0.40)+n*(cc+16)}:enable='gte(t,{ic:.2f})'")
F.append(f"drawtext=fontfile='{FUENTE}':text='EL LINK ESTA ABAJO':fontcolor=0x{AMARILLO}:"
         f"fontsize=58:x=(w-text_w)/2:y={int(H*0.40)+len(lc)*(cc+16)+28}:enable='gte(t,{ic:.2f})'")

mus = f'{tmp}/mus.wav'
run(['python3', MUSICA, f'{D2+1:.1f}', mus])

vf = f'{tmp}/vf.txt'
open(vf, 'w').write(
    f"[0:v]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},setsar=1,fps=30,"
    + ','.join(F) + "[v];"
    "[0:a]aformat=channel_layouts=stereo,asplit=2[voz][sc];"
    f"[1:a]aformat=channel_layouts=stereo,volume=0.085,atrim=0:{D2:.2f}[m];"
    "[m][sc]sidechaincompress=threshold=0.03:ratio=9:attack=6:release=320[md];"
    "[voz][md]amix=inputs=2:duration=first:weights=1 0.9,loudnorm=I=-14:TP=-1.5:LRA=11[a]")

print(f'  {len(grupos)} subtitulos · musica con ducking')
run([FF, '-v', 'error', '-y', '-i', paso2, '-i', mus, '-filter_complex_script', vf,
     '-map', '[v]', '-map', '[a]', '-c:v', 'libx264', '-preset', 'medium', '-crf', '21',
     '-pix_fmt', 'yuv420p', '-r', '30', '-c:a', 'aac', '-b:a', '160k',
     '-movflags', '+faststart', A.out])
print(f'OK  {A.out}  {dur(A.out):.1f}s')
