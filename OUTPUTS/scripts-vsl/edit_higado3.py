#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Higado Liviano v4: el ad largo, con la estructura de Doutor Nature.

  PARTE A — el avatar a camara, cortado ANTES de su CTA, con los silencios
            afuera, acelerado y con inserts de comida.
  PARTE B — voz en off sobre las visuales: el higado en 3D, la bilis, el
            colesterol, pantallas partidas y b-roll. Sin avatar (el lipsync
            solo sirve para el audio con el que se genero).

Encima de las dos: subtitulo con pop, placas, y la musica que paso Santiago.

Uso:
  python3 edit_higado2.py <avatar.mp4> <vo_extension.wav> <salida.mp4>
     --hook "..." --visA "a,b,c" --visB "d,e,f" [--split "F05-higado-graso|F18-bilis-espesa"]
     [--puntajes "cafe=5"] [--placa "9:TEXTO"]
"""
import argparse, os, re, subprocess, unicodedata

FF = os.path.expanduser('~/.local/bin/ffmpeg')
if not os.path.exists(FF):
    FF = 'ffmpeg'
SCR = ('/private/tmp/claude-501/-Users-santiagoseara-PrepCourse-Henry/'
       '5e3cbc82-95f4-48e0-b893-370e2e57fde2/scratchpad')
FONTDIR = f'{SCR}/fonts'
ANTON = f'{FONTDIR}/Anton-Regular.ttf'
VIS = os.path.expanduser('~/Desktop/higado-liviano/work/visuales')
CLIPS, FOTOS = f'{VIS}/clips1080', f'{VIS}/fotos9x16'
COMIDAS = os.path.expanduser('~/Desktop/higado-liviano/work/comidas')
MUS = os.path.expanduser('~/Downloads/u_6niyix0m9h-musica-de-suspense-335486.mp3.mpeg')

W, H, FPS = 1080, 1920, 30
CAP_Y = 1180
GAP, KEEP = 0.40, 0.15

ap = argparse.ArgumentParser()
ap.add_argument('src'); ap.add_argument('vo'); ap.add_argument('out')
ap.add_argument('--hook', default='')
ap.add_argument('--cierre', default='HIGADO LIVIANO · 21 DIAS')
ap.add_argument('--visA', default='')
ap.add_argument('--visB', default='')
ap.add_argument('--split', default='')      # "izq|der" o varias separadas por ;
ap.add_argument('--puntajes', default='')
ap.add_argument('--placa', default='')
ap.add_argument('--speed', type=float, default=1.25)
ap.add_argument('--cada', type=float, default=4.0)
ap.add_argument('--largo', type=float, default=1.7)
ap.add_argument('--segB', type=float, default=2.6)   # largo de cada plano en la parte B
ap.add_argument('--hooksec', type=float, default=2.2)
ap.add_argument('--cierresec', type=float, default=2.8)
A = ap.parse_args()

T = A.out + '_tmp'
os.makedirs(T, exist_ok=True)
sp = A.speed


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
    o, li = [], ''
    for p in t.split():
        if len(li) + len(p) + 1 > n:
            o.append(li); li = p
        else:
            li = (li + ' ' + p).strip()
    if li:
        o.append(li)
    return o


def ass_t(s):
    cs = int(round(s * 100))
    return f'{cs//360000}:{cs//6000%60:02d}:{cs//100%60:02d}.{cs%100:02d}'


def buscar(n):
    for base in (CLIPS, FOTOS, COMIDAS):
        for e in ('', '.mp4', '.jpg', '.jpeg', '.png', '.webp'):
            p = os.path.join(base, n + e)
            if os.path.exists(p):
                return p
    return None


from faster_whisper import WhisperModel
modelo = WhisperModel('small', device='cpu', compute_type='int8')


def palabras(f):
    segs, _ = modelo.transcribe(f, language='es', word_timestamps=True)
    return [(w.start, w.end, w.word.strip()) for s in segs for w in s.words if w.word.strip()]


def plano(src, L, out, zoom=True):
    """Un plano de L segundos: clip tal cual, o foto con push-in."""
    esc = f'scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},setsar=1,fps={FPS}'
    if src.lower().endswith('.mp4'):
        dc = dur(src)
        off = max(0.0, min(dc - L - 0.1, dc * 0.18))
        run([FF, '-v', 'error', '-y', '-ss', f'{off:.2f}', '-t', f'{L:.2f}', '-i', src,
             '-an', '-vf', esc, '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18',
             '-pix_fmt', 'yuv420p', out])
    else:
        z = f",scale=w='{W}*(1.0+0.10*t/{L:.2f})':h=-1:eval=frame,crop={W}:{H}:(iw-{W})/2:(ih-{H})/2" if zoom else ''
        run([FF, '-v', 'error', '-y', '-loop', '1', '-t', f'{L:.2f}', '-i', src, '-an',
             '-vf', esc + z + f',setsar=1,fps={FPS}',
             '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p', out])
    return out


def split(a, b, L, out):
    """Pantalla partida, como la usa el original cada tanto."""
    half = f'scale={W//2}:{H}:force_original_aspect_ratio=increase,crop={W//2}:{H},setsar=1,fps={FPS}'
    ins, pre = [], []
    for k, s in enumerate((a, b)):
        if s.lower().endswith('.mp4'):
            ins += ['-ss', '1.0', '-t', f'{L:.2f}', '-i', s]
        else:
            ins += ['-loop', '1', '-t', f'{L:.2f}', '-i', s]
        pre.append(f'[{k}:v]{half}[h{k}];')
    run([FF, '-v', 'error', '-y'] + ins + ['-filter_complex',
         ''.join(pre) + '[h0][h1]hstack=inputs=2,'
         f'drawbox=x={W//2-2}:y=0:w=4:h={H}:color=white@0.85:t=fill[v]',
         '-map', '[v]', '-an', '-t', f'{L:.2f}', '-c:v', 'libx264', '-preset', 'veryfast',
         '-crf', '18', '-pix_fmt', 'yuv420p', out])
    return out


def concat(partes, out, audio=None):
    # OJO: el demuxer concat resuelve las rutas de la lista RELATIVAS AL ARCHIVO
    # DE LISTA, no al directorio actual. Si no van absolutas, falla con 254.
    lst = out + '.txt'
    open(lst, 'w').write(''.join(f"file '{os.path.abspath(p)}'\n" for p in partes))
    if audio:
        run([FF, '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', lst, '-i', audio,
             '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k',
             '-shortest', out])
    else:
        run([FF, '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', lst, '-c', 'copy', out])
    return out


# ---------------------------------------------------------------------------
# PARTE A · el avatar, cortado antes de su CTA
# ---------------------------------------------------------------------------
D0 = dur(A.src)
ws = palabras(A.src)
corte = D0
for i in range(len(ws) - 1, 0, -1):
    if sinac(ws[i][2]).lower().strip('.,¿?¡!') in ('abajo', 'instante', 'dia'):
        for j in range(i, 0, -1):
            if ws[j][0] - ws[j - 1][1] > 0.33:
                corte = ws[j][0] - 0.08
                break
        break
print(f'  corto el CTA del avatar en {corte:.1f}s (de {D0:.1f}s)')

tramos, ini = [], 0.0
for i in range(1, len(ws)):
    if ws[i][0] > corte:
        break
    if ws[i][0] - ws[i - 1][1] > GAP:
        fin = ws[i - 1][1] + KEEP
        if fin > ini:
            tramos.append((ini, fin))
        ini = ws[i][0] - KEEP
tramos.append((ini, corte))
tramos = [(max(0, a), min(corte, b)) for a, b in tramos if b - a > 0.12]

pv = ''.join(f'[0:v]trim={a:.3f}:{b:.3f},setpts=PTS-STARTPTS[v{i}];' for i, (a, b) in enumerate(tramos))
pa = ''.join(f'[0:a]atrim={a:.3f}:{b:.3f},asetpts=PTS-STARTPTS[a{i}];' for i, (a, b) in enumerate(tramos))
cc = ''.join(f'[v{i}][a{i}]' for i in range(len(tramos)))
a1 = f'{T}/a1.mp4'
run([FF, '-v', 'error', '-y', '-i', A.src, '-filter_complex',
     pv + pa + cc + f'concat=n={len(tramos)}:v=1:a=1[vc][ac];'
     f'[vc]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},setsar=1,'
     f'setpts=PTS/{sp},fps={FPS}[vs];[ac]atempo={sp}[as]',
     '-map', '[vs]', '-map', '[as]', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18',
     '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k', a1])
DA = dur(a1)

# inserts sobre la parte A
nomA = [x.strip() for x in A.visA.split(',') if x.strip()]
faltan = [n for n in nomA if not buscar(n)]
if faltan:
    raise SystemExit(f'visuales que no existen en --visA: {faltan}')
if len(set(nomA)) != len(nomA):
    raise SystemExit(f'--visA repite visuales: {[n for n in set(nomA) if nomA.count(n) > 1]}')
visA = [buscar(n) for n in nomA]
if visA:
    t0, tf = max(A.hooksec + 0.8, 3.0), DA - 0.8 - A.largo
    cupo = int((tf - t0) // A.cada) + 1 if tf > t0 else 0
    n_ins = min(cupo, len(visA))              # NUNCA mas inserts que visuales
    if n_ins < cupo:
        print(f'  (espacio los inserts: {cupo} huecos pero {len(visA)} visuales)')
    paso = (tf - t0) / max(1, n_ins - 1) if n_ins > 1 else A.cada
    vents = [(t0 + k * paso, t0 + k * paso + A.largo) for k in range(n_ins)]
    piezas = [plano(visA[k], A.largo, f'{T}/ia{k}.mp4') for k in range(n_ins)]
    seq, cur, n = [], 0.0, 0
    for (x, y), pz in zip(vents, piezas):
        if x > cur:
            z = 1.0 if n % 2 == 0 else 1.10
            seg = f'{T}/av{n}.mp4'
            vf = (f'scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H}'
                  if z == 1.0 else
                  f'scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},'
                  f'crop={int(W/z)//2*2}:{int(H/z)//2*2}:(iw-{int(W/z)//2*2})/2:(ih-{int(H/z)//2*2})/3,'
                  f'scale={W}:{H}')
            run([FF, '-v', 'error', '-y', '-ss', f'{cur:.3f}', '-to', f'{x:.3f}', '-i', a1, '-an',
                 '-vf', vf + f',setsar=1,fps={FPS}', '-c:v', 'libx264', '-preset', 'veryfast',
                 '-crf', '18', '-pix_fmt', 'yuv420p', seg])
            seq.append(seg); n += 1
        seq.append(pz); cur = y
    if cur < DA:
        seg = f'{T}/av{n}.mp4'
        run([FF, '-v', 'error', '-y', '-ss', f'{cur:.3f}', '-i', a1, '-an',
             '-vf', f'scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},setsar=1,fps={FPS}',
             '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p', seg])
        seq.append(seg)
    vA = concat(seq, f'{T}/vA.mp4')
    pA = f'{T}/A.mp4'
    run([FF, '-v', 'error', '-y', '-i', vA, '-i', a1, '-map', '0:v', '-map', '1:a',
         '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-shortest', pA])
    print(f'  parte A: {DA:.1f}s con {len(vents)} inserts')
else:
    pA = a1
    print(f'  parte A: {DA:.1f}s')

# ---------------------------------------------------------------------------
# PARTE B · voz en off sobre las visuales
# ---------------------------------------------------------------------------
vob = f'{T}/vo.wav'
run([FF, '-v', 'error', '-y', '-i', A.vo, '-af',
     f'silenceremove=start_periods=1:start_threshold=-45dB:stop_periods=-1:'
     f'stop_duration=0.30:stop_threshold=-40dB:stop_silence=0.14,atempo={sp},aresample=48000',
     vob])
DB = dur(vob)

nomB = [x.strip() for x in A.visB.split(',') if x.strip()]
faltan = [n for n in nomB if not buscar(n)]
if faltan:
    raise SystemExit(f'visuales que no existen en --visB: {faltan}')
rep = [n for n in set(nomB) if nomB.count(n) > 1] + [n for n in set(nomB) & set(nomA)]
if rep:
    raise SystemExit(f'visuales repetidas dentro del anuncio: {sorted(set(rep))}')
visB = [buscar(n) for n in nomB]
splits = []
for par in [x for x in A.split.split(';') if '|' in x]:
    i, d = par.split('|')
    pi, pd = buscar(i.strip()), buscar(d.strip())
    if pi and pd:
        splits.append((pi, pd))

disponibles = len(visB) + len(splits)
nseg = max(1, int(round(DB / A.segB)))
if nseg > disponibles:                        # antes de repetir, alargo los planos
    nseg = disponibles
    print(f'  (alargo los planos: {disponibles} visuales para {DB:.0f}s)')
L = DB / nseg
if L > 4.6:
    raise SystemExit(f'FALTAN VISUALES en la parte B: {nseg} para {DB:.0f}s '
                     f'daria planos de {L:.1f}s. Pasame al menos '
                     f'{int(DB / 3.4) - disponibles} mas en --visB.')
piezas, si, iv = [], 0, 0
for k in range(nseg):
    # una pantalla partida cada 4 planos, como hace el original
    if splits and k % 4 == 2 and si < len(splits):
        piezas.append(split(splits[si][0], splits[si][1], L, f'{T}/sb{k}.mp4')); si += 1
    else:
        piezas.append(plano(visB[iv], L, f'{T}/ib{k}.mp4')); iv += 1
pB = concat(piezas, f'{T}/B.mp4', audio=vob)
print(f'  parte B: {DB:.1f}s en {nseg} planos de {L:.1f}s ({si} pantallas partidas)')

# ---------------------------------------------------------------------------
# A + B, subtitulos, placas y musica
# ---------------------------------------------------------------------------
for p, o in ((pA, f'{T}/nA.mp4'), (pB, f'{T}/nB.mp4')):
    run([FF, '-v', 'error', '-y', '-i', p, '-vf', f'scale={W}:{H},setsar=1,fps={FPS}',
         '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p',
         '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-ac', '2', o])
full = f'{T}/full.mp4'
lst = f'{T}/l.txt'
open(lst, 'w').write(f"file '{os.path.abspath(T)}/nA.mp4'\n"
                     f"file '{os.path.abspath(T)}/nB.mp4'\n")
run([FF, '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', lst, '-c', 'copy', full])
D2 = dur(full)
print(f'  total {D2:.1f}s')

ws2 = palabras(full)
IC = max(0.0, D2 - A.cierresec)
CLAVE = re.compile(r'^(higado|grasa|graso|bilis|hora|horas|cinco|cuatro|tres|dos|cero|nunca|'
                   r'nada|nadie|dieta|cena|fruta|banana|huevos|cafe|aceite|ensalada|detox|'
                   r'manteca|cerveza|panceta|gaseosa|veintiun|dias|link|abajo|peor|mejor|solo|'
                   r'todo|balanza|peso|analisis|colesterol|espesa|detergente|edad|cansancio)$')
CORTA = re.compile(r'[.,;:!?]$')          # la puntuacion cierra el grupo
grupos, i = [], 0
while i < len(ws2):
    bl = [ws2[i]]
    j = i + 1
    while j < len(ws2) and len(bl) < 3:
        if CORTA.search(bl[-1][2]):           # la anterior cerro la frase
            break
        if ws2[j][0] - bl[-1][1] > 0.26:      # hubo una pausa
            break
        largo = sum(len(w[2]) for w in bl) + len(ws2[j][2]) + len(bl)
        if largo > 22:                        # no entra en una linea
            break
        bl.append(ws2[j]); j += 1
    grupos.append((bl[0][0], bl[-1][1], [p[2] for p in bl]))
    i = j

ev = []
for k, (a, b, wl) in enumerate(grupos):
    if a >= IC - 0.05:
        continue
    nxt = grupos[k + 1][0] if k + 1 < len(grupos) else b + 0.3
    fin = min(min(max(b, a + 0.16), nxt), IC - 0.05)
    txt = re.sub(r'[^\w\s¿?¡!%/.]', '', ' '.join(sinac(w).upper() for w in wl)).strip()
    if not txt:
        continue
    col = r'\c&H0054D4FF&' if any(CLAVE.match(sinac(w).lower().strip('.,¿?¡!')) for w in wl) else r'\c&H00FFFFFF&'
    fs = 104 if len(txt) <= 15 else max(74, int(104 * 15 / len(txt)))
    ev.append(f'Dialogue: 1,{ass_t(a)},{ass_t(fin)},S,,0,0,0,,'
              f'{{\\pos(540,{CAP_Y}){col}\\fs{fs}\\fscx70\\fscy70'
              f'\\t(0,70,\\fscx112\\fscy112)\\t(70,140,\\fscx100\\fscy100)}}{txt}')

subs = f'{T}/s.ass'
open(subs, 'w').write(f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 2

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: S,Anton,104,&H00FFFFFF,&H00FFFFFF,&H00000000,&H78000000,0,0,0,0,100,100,0,0,1,8,2,5,40,40,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
""" + '\n'.join(ev) + '\n')

F = []
if A.hook:
    ls = partir(A.hook, 20)
    F.append(f"drawbox=x=0:y=104:w={W}:h={86*len(ls)+34}:color=black@0.85:t=fill:enable='between(t,0,{A.hooksec})'")
    for n, l in enumerate(ls):
        F.append(f"drawtext=fontfile='{ANTON}':text='{sinac(l).upper()}':fontcolor=white:fontsize=68:"
                 f"x=(w-text_w)/2:y={122+n*86}:enable='between(t,0,{A.hooksec})'")
if A.placa:
    pt, ptx = A.placa.split(':', 1); pt = float(pt)
    ls = partir(ptx, 18)
    F.append(f"drawbox=x=0:y={int(H*0.30)}:w={W}:h={94*len(ls)+38}:color=0xC02617@0.92:t=fill:"
             f"enable='between(t,{pt:.2f},{pt+2.2:.2f})'")
    for n, l in enumerate(ls):
        F.append(f"drawtext=fontfile='{ANTON}':text='{sinac(l).upper()}':fontcolor=white:fontsize=76:"
                 f"x=(w-text_w)/2:y={int(H*0.30)+20+n*94}:enable='between(t,{pt:.2f},{pt+2.2:.2f})'")
if A.puntajes:
    pl = [sinac(w).lower().strip('.,¿?¡!') for _, _, w in ws2]
    u, hall = 0, []
    for it in [x for x in A.puntajes.split(',') if '=' in x]:
        cl, val = [y.strip() for y in it.split('=')]
        pos = next((i for i in range(u, len(pl)) if pl[i] == cl), None)
        if pos is None:
            print('  ! puntaje sin ancla:', cl); continue
        u = pos + 1; hall.append((ws2[pos][1] + 0.15, val))
    print('  puntajes:', ' '.join(f'{t:.0f}s={v}' for t, v in hall) or '(ninguno)')
    for t, v in hall:
        F.append(f"drawtext=fontfile='{ANTON}':text='{v}/10':fontcolor=0x27D17F:fontsize=118:"
                 f"borderw=11:bordercolor=black@0.9:x=(w-text_w)/2:y={int(H*0.40)}:"
                 f"enable='between(t,{t:.2f},{t+2.2:.2f})'")

F.append(f"drawbox=x=0:y=0:w={W}:h={H}:color=0x0E1216@0.97:t=fill:enable='gte(t,{IC:.2f})'")
lc = partir(A.cierre, 16); cs = 86 if len(lc) > 1 else 78
for n, l in enumerate(lc):
    F.append(f"drawtext=fontfile='{ANTON}':text='{sinac(l).upper()}':fontcolor=white:fontsize={cs}:"
             f"x=(w-text_w)/2:y={int(H*0.40)+n*(cs+16)}:enable='gte(t,{IC:.2f})'")
F.append(f"drawtext=fontfile='{ANTON}':text='EL LINK ESTA ABAJO':fontcolor=0xFFD400:fontsize=58:"
         f"x=(w-text_w)/2:y={int(H*0.40)+len(lc)*(cs+16)+28}:enable='gte(t,{IC:.2f})'")

vf = f'{T}/vf.txt'
open(vf, 'w').write(
    '[0:v]' + ','.join(F) + f",subtitles='{subs}':fontsdir='{FONTDIR}'[v];"
    f"[1:a]aformat=channel_layouts=stereo,volume=0.20,atrim=0:{D2:.2f},"
    f"afade=t=in:st=0:d=1.2,afade=t=out:st={max(0,D2-1.4):.2f}:d=1.4[m];"
    "[0:a][m]amix=inputs=2:duration=first:normalize=0,"
    "loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000[a]")

print(f'  {len(ev)} subtitulos · musica de suspenso')
run([FF, '-v', 'error', '-y', '-i', full, '-stream_loop', '-1', '-i', MUS,
     '-filter_complex_script', vf, '-map', '[v]', '-map', '[a]',
     '-c:v', 'libx264', '-preset', 'medium', '-crf', '21', '-pix_fmt', 'yuv420p',
     '-r', str(FPS), '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-ac', '2',
     '-movflags', '+faststart', A.out])
print(f'OK  {A.out}  {dur(A.out):.1f}s')
