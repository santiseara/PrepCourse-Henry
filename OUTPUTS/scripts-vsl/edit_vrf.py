# -*- coding: utf-8 -*-
"""Ads de The VRF Field System (mercado ingles, 2026-11-23): clon de la edicion de
"Carlos Medina" / EXEMIO (vrf.impultienda.ar), medida sobre 10 de sus creativos de mas
impresiones (bajados el 23/11).

Su edicion, tal cual:
  - 24 a 58 s, 9:16, voz en off de hombre, sin SFX.
  - SUBTITULO quemado en condensada MAYUSCULA blanca con UNA palabra en AMARILLO, tercio inferior.
  - Tres formatos, que aca son los tres modos:
      vo     = 100 % b-roll, voz en off (el que mas corren)
      avatar = avatar a camara en sala de maquinas, sin b-roll
      pip    = b-roll a pantalla completa con el avatar recortado chico abajo
  - Insertos de las hojas del manual anclados a la palabra que los nombra.
  - Cierran con la tapa del ebook, los 3 bonos y el boton.

Uso: python3 edit_vrf.py plan.json salida.mp4
"""
import os, re, sys, json, random, difflib, subprocess
from faster_whisper import WhisperModel
from PIL import Image

FF = os.path.expanduser('~/bin/ffmpeg')
DIR = os.path.dirname(os.path.abspath(__file__))
P = json.load(open(sys.argv[1])); OUT = sys.argv[2]
base = os.path.dirname(os.path.abspath(sys.argv[1]))
def F(p): return p if os.path.isabs(p) else os.path.join(base, p)
tmp = os.path.join(base, os.path.basename(OUT) + '_tmp'); os.makedirs(tmp, exist_ok=True)
W, H, FPS = 1080, 1920, 30
MODE = P.get('mode', 'vo')
def run(c): subprocess.run(c, check=True)
def norm(w): return re.sub(r'[^\w]', '', w.lower())
def dur(p):
    r = subprocess.run([FF, '-i', p], capture_output=True, text=True).stderr
    h, m, s = re.search(r'Duration: (\d+):(\d+):([\d.]+)', r).groups()
    return int(h) * 3600 + int(m) * 60 + float(s)

# ---------- 1) audio ----------
if MODE == 'vo':
    sp = P.get('speed', 1.20)
    sd, ss_ = P.get('silence', [0.26, 0.12])
    run([FF, '-v', 'error', '-y', '-i', F(P['vo']), '-af',
         f'silenceremove=start_periods=1:start_threshold=-55dB:stop_periods=-1:stop_duration={sd}:'
         f'stop_threshold=-55dB:stop_silence={ss_},atempo={sp:.4f},aresample=48000,afade=t=in:d=0.02',
         '-ac', '2', f'{tmp}/vo.wav'])
else:      # el avatar ya trae la voz final: no se toca, rompe el lipsync
    run([FF, '-v', 'error', '-y', '-i', F(P['avatar']), '-vn', '-ac', '2', '-ar', '48000', f'{tmp}/vo.wav'])
VOZ = dur(f'{tmp}/vo.wav')
CIERRE = P.get('cierre', 3.2)          # segundos de placa final despues de la voz
L = VOZ + CIERRE

# ---------- 2) palabras alineadas al guion ----------
model = WhisperModel('small', device='cpu', compute_type='int8')
segs, _ = model.transcribe(f'{tmp}/vo.wav', language=P.get('lang', 'en'), word_timestamps=True)
wd = [(w.start, w.end, w.word.strip()) for s in segs for w in s.words]
sw = open(F(P['script'])).read().split()
a, b = [norm(x[2]) for x in wd], [norm(x) for x in sw]
vw = []
for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
    if op == 'equal':
        vw += [(wd[i1 + k][0], wd[i1 + k][1], sw[j1 + k]) for k in range(i2 - i1)]
    elif j2 > j1:
        s0 = wd[i1][0] if i1 < len(wd) else (vw[-1][1] if vw else 0)
        e0 = wd[i2 - 1][1] if i2 > i1 else s0 + 0.3 * (j2 - j1)
        st = max(0.05, (e0 - s0) / (j2 - j1))
        vw += [(s0 + k * st, s0 + (k + 1) * st, sw[j1 + k]) for k in range(j2 - j1)]
def wt(word, occ=0):
    ts_ = [w for w in vw if norm(w[2]) == norm(word)]
    if occ >= len(ts_): print(f'aviso: "{word}" n.o {occ} no aparece'); return None
    return ts_[occ]

# ---------- 3) cortes ----------
if MODE == 'avatar':
    cuts = [0.0, VOZ, L]
else:
    mn, ideal, mx = P.get('cut', [1.9, 2.4, 2.9])
    cuts, t = [0.0], 0.0
    while VOZ - t > mx:
        cand = [w for w in vw if t + mn <= w[1] <= t + mx]
        if not cand: t += ideal; cuts.append(t); continue
        best = min(cand, key=lambda w: abs(w[1] - (t + ideal)) - (0.5 if re.search(r'[.?!,]$', w[2]) else 0))
        t = best[1] + 0.04; cuts.append(t)
    cuts.append(VOZ); cuts.append(L)
    for word, occ, key in P.get('anchors', []):
        w = wt(word, occ)
        if not w: continue
        tg = w[0] - 0.06
        j = min(range(1, len(cuts) - 2), key=lambda i: abs(cuts[i] - tg))
        if abs(cuts[j] - tg) < 0.08: continue
        if abs(cuts[j] - tg) < 0.8 and cuts[j - 1] + 0.7 < tg < cuts[j + 1] - 0.7: cuts[j] = tg
        else:
            k = max(i for i in range(len(cuts) - 1) if cuts[i] <= tg)
            if cuts[k] + 0.7 < tg < cuts[k + 1] - 0.7: cuts.insert(k + 1, tg)

# ---------- 4) que plano va en cada corte ----------
def fam(k): return (P['clips'].get(k, {}).get('fam') or k) if k else ''
rnd = random.Random(P.get('seed', 0))
upath = F(P['usage']) if 'usage' in P else None
usage = json.load(open(upath)) if upath and os.path.exists(upath) else {}
NC = len(cuts) - 1                       # el ultimo tramo es siempre la placa de cierre
plan, used, forced = [], set(), {}
if MODE != 'avatar':
    for word, occ, key in P.get('anchors', []):
        w = wt(word, occ)
        if not w: continue
        n = max(i for i in range(NC - 1) if cuts[i] <= w[0] + 0.05)
        if n in forced or forced.get(n - 1, [''])[0] == key or forced.get(n + 1, [''])[0] == key:
            print(f'aviso: el ancla "{word}" choca en el plano {n}, se ignora'); continue
        forced[n] = next(s for s in P['pool'] if s[0] == key)
    for s in forced.values(): used.add(f'{s[0]}@{s[1]}')
    for n in range(NC - 1):
        d = cuts[n + 1] - cuts[n]
        prev = [p[0] for p in plan[-2:]]
        if n in forced: seg = forced[n]
        elif n == 0 and P.get('first'): seg = next(s for s in P['pool'] if s[0] == P['first'])
        else:
            nxt = forced[n + 1][0] if n + 1 in forced else None
            # los insertos del producto entran SOLO por ancla: si entran por sorteo salen dos hojas seguidas
            libre = [s for s in P['pool'] if not P['clips'][s[0]].get('still')]
            cand = [s for s in libre if f'{s[0]}@{s[1]}' not in used
                    and fam(s[0]) not in [fam(q) for q in prev[-1:]] and fam(s[0]) != fam(nxt)]
            if not cand: cand = [s for s in libre if f'{s[0]}@{s[1]}' not in used] or list(libre)
            here = {}
            for p in plan: here[fam(p[0])] = here.get(fam(p[0]), 0) + 1
            def score(s):
                return (usage.get(f'{s[0]}@{s[1]}', 0) * 10 + here.get(fam(s[0]), 0) * 3
                        + (3 if s[0] in prev else 0) + (6 if s[2] - s[1] < d * 0.75 else 0) + rnd.random())
            seg = min(cand, key=score)
        sid = f'{seg[0]}@{seg[1]}'; used.add(sid)
        plan.append((seg[0], seg[1], seg[2],
                     usage.get(sid, 0) % 2 == 1 and not P['clips'][seg[0]].get('still')))
        usage[sid] = usage.get(sid, 0) + 1
    if upath: json.dump(usage, open(upath, 'w'), indent=0)
    print('planos:', ' '.join(f'{k}:{s:g}' for k, s, e, f in plan))

# ---------- 5) fondo ----------
parts = []
def still_part(src, d, n, zin=True, full=False):
    # las hojas del manual entran ENTERAS: se achican al 88 % y el zoom no las recorta
    z = (f"(1+0.05*t/{d:.3f})" if zin else f"(1.05-0.05*t/{d:.3f})")
    inner = W if full else int(W * 0.88)
    vf = (f"[0:v]scale={inner}:{int(H*0.88)}:force_original_aspect_ratio=decrease,"
          f"pad={W}:{H}:(ow-iw)/2:(oh-ih)/2:color=0x0A182C,fps={FPS},"
          f"scale=w='{2*W}*{z}':h=-2:eval=frame:flags=bicubic,"
          f"crop={2*W}:{2*H}:(iw-{2*W})/2:(ih-{2*H})/2,scale={W}:{H}:flags=lanczos,setsar=1,format=yuv420p")
    pc = f'{tmp}/s{n:02d}.mp4'
    run([FF, '-v', 'error', '-y', '-loop', '1', '-t', f'{d:.3f}', '-i', src, '-filter_complex', vf,
         '-t', f'{d:.3f}', '-r', str(FPS), '-c:v', 'libx264', '-crf', '18', '-preset', 'fast', pc])
    return pc

if MODE == 'avatar':
    pc = f'{tmp}/s00.mp4'
    run([FF, '-v', 'error', '-y', '-i', F(P['avatar']), '-an', '-t', f'{VOZ:.3f}',
         '-vf', f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS},setsar=1,format=yuv420p",
         '-c:v', 'libx264', '-crf', '18', '-preset', 'fast', pc])
    parts.append(pc)
else:
    for n in range(NC - 1):
        d = cuts[n + 1] - cuts[n]
        key, st, end, flip = plan[n]
        c = P['clips'][key]; src = F(c['src'])
        punch = "(1+0.16*max(0,1-t/0.22))" if n > 0 else "1"
        if c.get('still'):
            parts.append(still_part(src, d, n, n % 2 == 0)); continue
        end = min(end, dur(src)); avail = end - st
        slow = max(1.0, d / avail) if avail > 0 else 1.0
        z0 = c.get('zoom', 1.0); yb = c.get('ybias', 0.5)
        vf = (f"setpts={slow:.4f}*(PTS-STARTPTS),fps={FPS},"
              f"scale=w='ceil(max({W}/iw,{H}/ih)*iw*{z0}*(1+0.07*t/{d:.3f})*{punch}/2)*2':h=-2:eval=frame:flags=bicubic,"
              f"crop={W}:{H}:(iw-{W})/2:(ih-{H})*{yb},{'hflip,' if flip else ''}setsar=1,format=yuv420p")
        pc = f'{tmp}/s{n:02d}.mp4'
        run([FF, '-v', 'error', '-y', '-ss', str(st), '-t', f'{min(avail, d / slow) + 0.1:.3f}', '-i', src,
             '-an', '-vf', vf, '-t', f'{d:.3f}', '-c:v', 'libx264', '-crf', '18', '-preset', 'fast', pc])
        parts.append(pc)
# placa de cierre
parts.append(still_part(F(P['cierre_png']), cuts[-1] - cuts[-2], 98, True, full=True))
lst = f'{tmp}/all.txt'; open(lst, 'w').write(''.join(f"file '{p}'\n" for p in parts))
run([FF, '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', lst, '-c', 'copy', f'{tmp}/cat.mp4'])

# ---------- 6) avatar recortado encima (modo pip) ----------
BASE = f'{tmp}/cat.mp4'
if MODE == 'pip':
    ah = int(H * P.get('pip_h', 0.52)); aw = int(ah * 9 / 16)
    ax = P.get('pip_x', 0.60); ay = H - ah
    fc = (f"[1:v]scale={aw}:{ah}[fg];[2:v]scale={aw}:{ah},format=gray[mk];"
          f"[fg][mk]alphamerge[cut];[0:v][cut]overlay=x={int(W*ax)-aw//2}:y={ay}:shortest=0[v]")
    run([FF, '-v', 'error', '-y', '-i', BASE, '-i', F(P['avatar']), '-i', F(P['mask']),
         '-filter_complex', fc, '-map', '[v]', '-c:v', 'libx264', '-crf', '18', '-preset', 'fast',
         '-t', f'{L:.3f}', f'{tmp}/pip.mp4'])
    BASE = f'{tmp}/pip.mp4'

# ---------- 7) subtitulos: condensada blanca, la palabra que suena en AMARILLO ----------
def ts(t): t = max(0, t); return f'{int(t // 3600)}:{int(t % 3600 // 60):02d}:{t % 60:05.2f}'
CAPY = P.get('capy', 1395)
HI = P.get('hi', '&H0000E4FF&')            # amarillo (BGR)
FNAME = P.get('font', 'Barlow Condensed ExtraBold')
FSZ = P.get('fsize', 92)
ass = [f'''[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: C,{FNAME},{FSZ},&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,0,0,0,0,100,100,2,0,1,5,4,5,60,60,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text''']
def clean(w): return w.replace('…', '').strip(' ,;:"“”').upper()
chunks, cur = [], []
for x in vw:
    cur.append(x)
    if len(cur) == P.get('words', 3) or re.search(r'[.?!…]$', x[2]): chunks.append(cur); cur = []
if cur: chunks.append(cur)
end_t = VOZ + 0.25
for ci, ch in enumerate(chunks):
    if ch[0][0] >= end_t: continue
    nxt = chunks[ci + 1][0][0] if ci + 1 < len(chunks) else ch[-1][1] + 0.4
    for wi, (s, e, w) in enumerate(ch):
        e2 = min(ch[wi + 1][0] if wi + 1 < len(ch) else min(nxt, ch[-1][1] + 0.5), end_t)
        txt = ' '.join((f'{{\\1c{HI}}}' + clean(x[2]) + '{\\r}') if j == wi else clean(x[2])
                       for j, x in enumerate(ch))
        ass.append(f'Dialogue: 0,{ts(s)},{ts(e2)},C,,0,0,0,,{{\\pos({W // 2},{CAPY})}}{txt}')
open(f'{tmp}/subs.ass', 'w').write('\n'.join(ass) + '\n')

# ---------- 8) musica + mezcla ----------
FONTS = os.environ.get('VRF_FONTS', os.path.join(DIR, 'fonts'))
if P.get('music'):
    import numpy as np, soundfile as sf
    m_, sr_ = sf.read(F(P['music'])); v_, _ = sf.read(f'{tmp}/vo.wav')
    if m_.ndim == 1: m_ = np.stack([m_, m_], 1)
    need = int((L + 1) * sr_); xf = int(1.0 * sr_)
    while len(m_) < need:
        a2 = m_[int(4 * sr_):]; r_ = np.linspace(0, 1, xf)[:, None]
        m_ = np.concatenate([m_[:-xf], m_[-xf:] * (1 - r_) + a2[:xf] * r_, a2[xf:]])
    m_ = m_[:need]
    rv = np.sqrt(np.mean(v_[v_.any(1)] ** 2)); rm = np.sqrt(np.mean(m_ ** 2))
    m_ = m_ * (rv / rm) * 10 ** (P.get('music_db', -9) / 20)
    sf.write(f'{tmp}/music.wav', np.clip(m_, -1, 1), sr_)
    run([FF, '-v', 'error', '-y', '-i', f'{tmp}/vo.wav', '-i', f'{tmp}/music.wav', '-filter_complex',
         f'[0:a]apad=whole_dur={L:.3f}[v];[1:a]atrim=0:{L:.3f},afade=t=out:st={L-1.2:.2f}:d=1.2[m];'
         f'[v][m]amix=inputs=2:duration=first:dropout_transition=0:normalize=0[a]',
         '-map', '[a]', '-ac', '2', '-ar', '48000', f'{tmp}/mix.wav'])
else:
    run([FF, '-v', 'error', '-y', '-i', f'{tmp}/vo.wav', '-af', f'apad=whole_dur={L:.3f}',
         '-ac', '2', '-ar', '48000', f'{tmp}/mix.wav'])

run([FF, '-v', 'error', '-y', '-i', BASE, '-i', f'{tmp}/mix.wav',
     '-vf', f"subtitles={tmp}/subs.ass:fontsdir={FONTS}",
     '-map', '0:v', '-map', '1:a', '-c:v', 'libx264', '-crf', '19', '-preset', 'medium',
     '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '128k', '-t', f'{L:.3f}', OUT])
print('OK', OUT, round(L, 2), 's')
