#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Monta un ad de Higado Liviano.

Look de Doutor Nature (subtitulo Anton blanco con la palabra clave en amarillo,
barra negra de hook, chapas de puntaje verdes) con el RITMO de Silvia Fitness
(velocidad 1.25, corte seco cada pocos segundos, zoom alternado y pop en el
subtitulo). El avatar de HeyGen trae la voz adentro; aca no se regraba nada.

  1. jump cut en cada silencio, video y audio juntos
  2. velocidad pareja (el lipsync no se mueve)
  3. inserts del material propio: los .mp4 entran tal cual, las fotos con push-in
  4. subtitulo ASS de 1-2 palabras con pop de entrada
  5. musica audible (0.09, sin sidechain)

Uso:
  python3 edit_higado.py <avatar.mp4> <salida.mp4> --hook "..."
      [--visuales "F04-medico,02-manteca-sarten.jpg,F05-higado-graso"]
      [--puntajes "cafe=5,huevos=3"] [--placa "9:TEXTO"] [--speed 1.25]
      [--cada 4.0] [--largo 1.7] [--cierre "..."]
"""
import argparse, glob, os, re, subprocess, unicodedata

FF = os.path.expanduser('~/.local/bin/ffmpeg')
if not os.path.exists(FF):
    FF = 'ffmpeg'
SCR = ('/private/tmp/claude-501/-Users-santiagoseara-PrepCourse-Henry/'
       '5e3cbc82-95f4-48e0-b893-370e2e57fde2/scratchpad')
FONTDIR = f'{SCR}/fonts'
CLIPS = f'{SCR}/zip_clips/clips1080'
FOTOS = f'{SCR}/zip_fotos/fotos9x16'
MUSICA = '/Users/santiagoseara/PrepCourse-Henry/OUTPUTS/scripts-vsl/music_activa.py'

W, H, FPS = 1080, 1920, 30
CAP_Y = 1180          # subtitulo a la altura de las manos
GAP, KEEP = 0.40, 0.15

ap = argparse.ArgumentParser()
ap.add_argument('src'); ap.add_argument('out')
ap.add_argument('--hook', default='')
ap.add_argument('--cierre', default='HIGADO LIVIANO · 21 DIAS')
ap.add_argument('--visuales', default='')
ap.add_argument('--puntajes', default='')
ap.add_argument('--placa', default='')
ap.add_argument('--speed', type=float, default=1.25)
ap.add_argument('--cada', type=float, default=4.0)
ap.add_argument('--largo', type=float, default=1.7)
ap.add_argument('--hooksec', type=float, default=2.2)
ap.add_argument('--cierresec', type=float, default=2.8)
A = ap.parse_args()

TMP = A.out + '_tmp'
os.makedirs(TMP, exist_ok=True)


def run(c):
    subprocess.run(c, check=True)


def dur(f):
    r = subprocess.run([FF, '-i', f], capture_output=True, text=True).stderr
    h, m, s = re.search(r'Duration: (\d+):(\d+):([\d.]+)', r).groups()
    return int(h) * 3600 + int(m) * 60 + float(s)


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


def ass_t(s):
    cs = int(round(s * 100))
    return f'{cs//360000}:{cs//6000%60:02d}:{cs//100%60:02d}.{cs%100:02d}'


from faster_whisper import WhisperModel
modelo = WhisperModel('small', device='cpu', compute_type='int8')


def palabras(f):
    segs, _ = modelo.transcribe(f, language='es', word_timestamps=True)
    return [(w.start, w.end, w.word.strip()) for s in segs for w in s.words if w.word.strip()]


# --- 1. silencios fuera + velocidad -----------------------------------------
D0 = dur(A.src)
ws = palabras(A.src)
tramos, ini = [], 0.0
for i in range(1, len(ws)):
    if ws[i][0] - ws[i - 1][1] > GAP:
        fin = ws[i - 1][1] + KEEP
        if fin > ini:
            tramos.append((ini, fin))
        ini = ws[i][0] - KEEP
tramos.append((ini, D0))
tramos = [(max(0, a), min(D0, b)) for a, b in tramos if b - a > 0.12]

sp = A.speed
pv = ''.join(f'[0:v]trim={a:.3f}:{b:.3f},setpts=PTS-STARTPTS[v{i}];' for i, (a, b) in enumerate(tramos))
pa = ''.join(f'[0:a]atrim={a:.3f}:{b:.3f},asetpts=PTS-STARTPTS[a{i}];' for i, (a, b) in enumerate(tramos))
cv = ''.join(f'[v{i}][a{i}]' for i in range(len(tramos)))
p1 = f'{TMP}/1.mp4'
run([FF, '-v', 'error', '-y', '-i', A.src, '-filter_complex',
     pv + pa + cv + f'concat=n={len(tramos)}:v=1:a=1[vc][ac];'
     f'[vc]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},setsar=1,'
     f'setpts=PTS/{sp},fps={FPS}[vs];[ac]atempo={sp}[as]',
     '-map', '[vs]', '-map', '[as]', '-c:v', 'libx264', '-preset', 'veryfast',
     '-crf', '18', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k', p1])
D1 = dur(p1)
print(f'  {D0:.1f}s -> {D1:.1f}s  ({len(tramos)-1} jump cuts, speed {sp})')


# --- 2. inserts del material propio -----------------------------------------
def buscar(nombre):
    for base, exts in ((CLIPS, ('.mp4',)), (FOTOS, ('.jpg', '.jpeg', '.png', '.webp'))):
        for e in ('',) + exts:
            p = os.path.join(base, nombre + e)
            if os.path.exists(p):
                return p
        hit = [f for f in glob.glob(os.path.join(base, nombre + '*'))
               if not os.path.basename(f).startswith('._')]
        if hit:
            return sorted(hit)[0]
    return None


pedidos = [x.strip() for x in A.visuales.split(',') if x.strip()]
vis = []
for n in pedidos:
    p = buscar(n)
    if p:
        vis.append(p)
    else:
        print('  ! no encuentro visual:', n)

p2 = p1
if vis:
    t, vents = max(A.hooksec + 0.8, 3.0), []
    while t + A.largo < D1 - A.cierresec - 0.8:
        vents.append((t, t + A.largo)); t += A.cada
    usados = [vis[i % len(vis)] for i in range(len(vents))]

    # cada insert se pre-renderiza: los clips tal cual, las fotos con push-in
    piezas = []
    for k, ((a, b), src) in enumerate(zip(vents, usados)):
        L = b - a
        pz = f'{TMP}/ins{k}.mp4'
        if src.lower().endswith('.mp4'):
            dc = dur(src)
            off = max(0.0, min(dc - L - 0.1, dc * 0.2))
            run([FF, '-v', 'error', '-y', '-ss', f'{off:.2f}', '-t', f'{L:.2f}', '-i', src,
                 '-an', '-vf', f'scale={W}:{H}:force_original_aspect_ratio=increase,'
                 f'crop={W}:{H},setsar=1,fps={FPS}',
                 '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p', pz])
        else:
            # push-in lineal: la foto nunca queda quieta
            run([FF, '-v', 'error', '-y', '-loop', '1', '-t', f'{L:.2f}', '-i', src, '-an',
                 '-vf', f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},"
                        f"scale=w='{W}*(1.0+0.09*t/{L:.2f})':h=-1:eval=frame,"
                        f"crop={W}:{H}:(iw-{W})/2:(ih-{H})/2,setsar=1,fps={FPS}",
                 '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p', pz])
        piezas.append(pz)

    plan, cur = [], 0.0
    for (a, b), pz in zip(vents, piezas):
        if a > cur:
            plan.append(('av', cur, a))
        plan.append(('in', pz))
        cur = b
    if cur < D1:
        plan.append(('av', cur, D1))

    ins, partes, idx, n = ['-i', p1], [], 1, 0
    for p in plan:
        if p[0] == 'av':
            a, b = p[1], p[2]
            z = 1.0 if n % 2 == 0 else 1.10
            if z == 1.0:
                partes.append(f'[0:v]trim={a:.3f}:{b:.3f},setpts=PTS-STARTPTS,fps={FPS}[p{n}];')
            else:
                cw, ch = int(W / z) // 2 * 2, int(H / z) // 2 * 2
                partes.append(f'[0:v]trim={a:.3f}:{b:.3f},setpts=PTS-STARTPTS,'
                              f'crop={cw}:{ch}:(iw-{cw})/2:(ih-{ch})/3,scale={W}:{H},'
                              f'setsar=1,fps={FPS}[p{n}];')
        else:
            ins += ['-i', p[1]]
            partes.append(f'[{idx}:v]setpts=PTS-STARTPTS,fps={FPS}[p{n}];')
            idx += 1
        n += 1
    p2 = f'{TMP}/2.mp4'
    run([FF, '-v', 'error', '-y'] + ins + ['-filter_complex',
         ''.join(partes) + ''.join(f'[p{i}]' for i in range(n)) + f'concat=n={n}:v=1:a=0[vv]',
         '-map', '[vv]', '-map', '0:a', '-c:v', 'libx264', '-preset', 'veryfast',
         '-crf', '18', '-pix_fmt', 'yuv420p', '-c:a', 'copy', '-shortest', p2])
    print(f'  {len(vents)} inserts de {A.largo}s ({len(set(usados))} visuales)')

D2 = dur(p2)

# --- 3. subtitulos ASS con pop, placas y musica ------------------------------
ws2 = palabras(p2)
IC = max(0.0, D2 - A.cierresec)   # el subtitulo no pisa la placa final
CLAVE = re.compile(r'^(higado|grasa|graso|hora|horas|cinco|cuatro|tres|dos|cero|nunca|nada|'
                   r'nadie|gratis|dieta|alarma|noche|cena|fruta|banana|huevos|cafe|aceite|'
                   r'ensalada|detox|manteca|cerveza|panceta|gaseosa|veintiun|dias|link|abajo|'
                   r'peor|mejor|solo|todo|balanza|peso|bilis|analisis|colesterol)$')

grupos, i = [], 0
while i < len(ws2):
    n = 2 if len(ws2) - i >= 2 else 1
    if n == 2 and ws2[i + 1][0] - ws2[i][1] > 0.26:
        n = 1
    bl = ws2[i:i + n]
    grupos.append((bl[0][0], bl[-1][1], [p[2] for p in bl]))
    i += n

ev = []
for k, (a, b, wl) in enumerate(grupos):
    if a >= IC - 0.05:
        continue
    nxt = grupos[k + 1][0] if k + 1 < len(grupos) else b + 0.3
    fin = min(min(max(b, a + 0.16), nxt), IC - 0.05)
    txt = re.sub(r'[^\w\s¿?¡!%/.]', '', ' '.join(sinac(w).upper() for w in wl)).strip()
    if not txt:
        continue
    clave = any(CLAVE.match(sinac(w).lower().strip('.,¿?¡!')) for w in wl)
    col = r'\c&H0054D4FF&' if clave else r'\c&H00FFFFFF&'   # amarillo / blanco (BGR)
    fs = 104 if len(txt) <= 15 else max(74, int(104 * 15 / len(txt)))
    # el pop de Silvia: entra al 70%, pasa de largo al 112 y asienta en 100
    ev.append(f'Dialogue: 1,{ass_t(a)},{ass_t(fin)},S,,0,0,0,,'
              f'{{\\pos(540,{CAP_Y}){col}\\fs{fs}\\fscx70\\fscy70'
              f'\\t(0,70,\\fscx112\\fscy112)\\t(70,140,\\fscx100\\fscy100)}}{txt}')

ASS = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 2

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: S,Anton,104,&H00FFFFFF,&H00FFFFFF,&H00000000,&H78000000,0,0,0,0,100,100,0,0,1,8,2,5,40,40,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
subs = f'{TMP}/subs.ass'
open(subs, 'w').write(ASS + '\n'.join(ev) + '\n')

F = []
if A.hook:
    ls = partir(A.hook, 20)
    F.append(f"drawbox=x=0:y=104:w={W}:h={86*len(ls)+34}:color=black@0.85:t=fill:"
             f"enable='between(t,0,{A.hooksec})'")
    for n, l in enumerate(ls):
        F.append(f"drawtext=fontfile='{FONTDIR}/Anton-Regular.ttf':"
                 f"text='{sinac(l).upper()}':fontcolor=white:fontsize=68:"
                 f"x=(w-text_w)/2:y={122+n*86}:enable='between(t,0,{A.hooksec})'")

if A.placa:
    pt, ptx = A.placa.split(':', 1)
    pt = float(pt)
    ls = partir(ptx, 18)
    F.append(f"drawbox=x=0:y={int(H*0.30)}:w={W}:h={94*len(ls)+38}:color=0xC02617@0.92:t=fill:"
             f"enable='between(t,{pt:.2f},{pt+2.2:.2f})'")
    for n, l in enumerate(ls):
        F.append(f"drawtext=fontfile='{FONTDIR}/Anton-Regular.ttf':text='{sinac(l).upper()}':"
                 f"fontcolor=white:fontsize=76:x=(w-text_w)/2:y={int(H*0.30)+20+n*94}:"
                 f"enable='between(t,{pt:.2f},{pt+2.2:.2f})'")

if A.puntajes:
    plano = [sinac(w).lower().strip('.,¿?¡!') for _, _, w in ws2]
    usado, hall = 0, []
    for it in [x for x in A.puntajes.split(',') if '=' in x]:
        cl, val = [y.strip() for y in it.split('=')]
        pos = next((i for i in range(usado, len(plano)) if plano[i] == cl), None)
        if pos is None:
            print('  ! puntaje sin ancla:', cl); continue
        usado = pos + 1
        hall.append((ws2[pos][1] + 0.15, val))
    print('  puntajes:', ' '.join(f'{t:.0f}s={v}' for t, v in hall) or '(ninguno)')
    for t, v in hall:
        F.append(f"drawtext=fontfile='{FONTDIR}/Anton-Regular.ttf':text='{v}/10':"
                 f"fontcolor=0x27D17F:fontsize=118:borderw=11:bordercolor=black@0.9:"
                 f"x=(w-text_w)/2:y={int(H*0.40)}:enable='between(t,{t:.2f},{t+2.2:.2f})'")

ic = IC
F.append(f"drawbox=x=0:y=0:w={W}:h={H}:color=0x0E1216@0.97:t=fill:enable='gte(t,{ic:.2f})'")
lc = partir(A.cierre, 16)
cc = 86 if len(lc) > 1 else 78
for n, l in enumerate(lc):
    F.append(f"drawtext=fontfile='{FONTDIR}/Anton-Regular.ttf':text='{sinac(l).upper()}':"
             f"fontcolor=white:fontsize={cc}:x=(w-text_w)/2:y={int(H*0.40)+n*(cc+16)}:"
             f"enable='gte(t,{ic:.2f})'")
F.append(f"drawtext=fontfile='{FONTDIR}/Anton-Regular.ttf':text='EL LINK ESTA ABAJO':"
         f"fontcolor=0xFFD400:fontsize=58:x=(w-text_w)/2:"
         f"y={int(H*0.40)+len(lc)*(cc+16)+28}:enable='gte(t,{ic:.2f})'")

mus = f'{TMP}/mus.wav'
run(['python3', MUSICA, f'{D2+1:.1f}', mus])

vf = f'{TMP}/vf.txt'
open(vf, 'w').write(
    '[0:v]' + ','.join(F) + f",subtitles='{subs}':fontsdir='{FONTDIR}'[v];"
    f"[1:a]volume=0.22,atrim=0:{D2:.2f},afade=t=out:st={max(0,D2-1.0):.2f}:d=1.0[m];"
    "[0:a][m]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11[a]")

print(f'  {len(ev)} subtitulos con pop · musica 0.22')
run([FF, '-v', 'error', '-y', '-i', p2, '-i', mus, '-filter_complex_script', vf,
     '-map', '[v]', '-map', '[a]', '-c:v', 'libx264', '-preset', 'medium', '-crf', '21',
     '-pix_fmt', 'yuv420p', '-r', str(FPS), '-c:a', 'aac', '-b:a', '192k',
     '-movflags', '+faststart', A.out])
print(f'OK  {A.out}  {dur(A.out):.1f}s')
