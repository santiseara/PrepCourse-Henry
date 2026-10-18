"""Ad de voz en off sobre B-roll de terceros (Bachas de concreto, 2026-10-18).
Voz (Google AI Studio TTS) recortada de silencios y acelerada, cortes de visual cada ~4-5 s
alineados al final de una palabra, zoom suave alternado, whoosh en cada corte, subtítulos de
3 palabras con la activa en amarillo y música baja.
Uso: python3 edit_broll.py plan.json salida.mp4
plan.json:
{
 "vo": "A.wav", "script": "A.txt", "speed": 1.2, "lang": "en",
 "clips": {"Y": {"src": "tt_7541.mp4", "ranges": [[0, 25]]},
           "M": {"src": "tt_7639.mp4", "ranges": [[0, 13]], "zoom": 1.3, "ybias": 1.0}},  # ybias 1 = recorte abajo
 "shots": [["Y", 0], ["G", 0], ["K", 7]],   # orden fijo de visuales (clave, segundo de arranque)
 "pool": [["K", 0, 5], ["T", 2, 6.5]],       # o en vez de "shots": recortes que se reparten solos
 "first": ["Y", 0], "usage": "usage.json", "seed": 1,
 "sfx": [["chaching", "dollars", 0], ["ding", "order.", 0], ["pop", "Learn", 0]],  # sonido, palabra, n.º de aparición
 "whoosh": [1],                               # índices de corte con whoosh (no en todos)
 "cut": [3.6, 4.4, 5.2]                       # mínimo, ideal y máximo de cada plano
}
Con "pool": un recorte no se repite en el mismo video, nunca van dos planos seguidos del mismo
clip y se priorizan los menos usados en videos anteriores (usage.json). Si uno ya se usó, va espejado.
"""
import os, re, sys, json, subprocess, difflib
from faster_whisper import WhisperModel

FF = os.path.expanduser('~/bin/ffmpeg')
DIR = os.path.dirname(os.path.abspath(__file__))
P = json.load(open(sys.argv[1])); OUT = sys.argv[2]
base = os.path.dirname(os.path.abspath(sys.argv[1]))
def F(p): return p if os.path.isabs(p) else os.path.join(base, p)
tmp = os.path.join(base, os.path.basename(OUT) + '_tmp'); os.makedirs(tmp, exist_ok=True)
W, H, FPS = 1080, 1920, 30
def run(c): subprocess.run(c, check=True)
def norm(w): return re.sub(r'[^\w]', '', w.lower())

# 1) voz: recorte de silencios + velocidad, palabras alineadas al guion
sp = P.get('speed', 1.2)
run([FF, '-v', 'error', '-y', '-i', F(P['vo']), '-af',
     'silenceremove=start_periods=1:start_threshold=-45dB:stop_periods=-1:stop_duration=0.25:stop_threshold=-40dB:stop_silence=0.12,'
     f'atempo={sp:.4f},aresample=48000', '-ac', '2', f'{tmp}/vo.wav'])
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
r = subprocess.run([FF, '-i', f'{tmp}/vo.wav'], capture_output=True, text=True).stderr
hh, mm, ss = re.search(r'Duration: (\d+):(\d+):([\d.]+)', r).groups()
L = int(hh) * 3600 + int(mm) * 60 + float(ss) + 0.3

# 2) puntos de corte: cerca del ideal, siempre al final de una palabra (mejor si cierra frase)
mn, ideal, mx = P.get('cut', [3.6, 4.4, 5.2])
cuts, t = [0.0], 0.0
while L - t > mx:
    cand = [w for w in vw if t + mn <= w[1] <= t + mx]
    if not cand: t += ideal; cuts.append(t); continue
    best = min(cand, key=lambda w: abs(w[1] - (t + ideal)) - (0.6 if re.search(r'[.?!,]$', w[2]) else 0))
    t = best[1] + 0.04; cuts.append(t)
cuts.append(L)

# 3) cada plano: recorte 9:16, zoom suave alternado, sin audio
def dur(p):
    r = subprocess.run([FF, '-i', p], capture_output=True, text=True).stderr
    h, m, s = re.search(r'Duration: (\d+):(\d+):([\d.]+)', r).groups(); return int(h) * 3600 + int(m) * 60 + float(s)
import random
rnd = random.Random(P.get('seed', 0))
upath = F(P['usage']) if 'usage' in P else None
usage = json.load(open(upath)) if upath and os.path.exists(upath) else {}
used, plan = set(), []
for n in range(len(cuts) - 1):
    d = cuts[n + 1] - cuts[n]
    if 'pool' not in P:
        key, st = P['shots'][n % len(P['shots'])]
        c = P['clips'][key]
        end = next((r1 for r0, r1 in c.get('ranges', [[0, 1e9]]) if r0 <= st < r1), 1e9)
        plan.append((key, st, end, False)); continue
    prev = [p[0] for p in plan[-2:]]
    if n == 0 and 'first' in P:
        seg = next(s for s in P['pool'] if s[0] == P['first'][0] and s[1] == P['first'][1])
    else:
        cand = [s for s in P['pool'] if f'{s[0]}@{s[1]}' not in used and s[0] not in prev[-1:]]
        here = {k: sum(1 for p in plan if p[0] == k) for k in P['clips']}
        def score(s):
            return (usage.get(f'{s[0]}@{s[1]}', 0) * 10 + here.get(s[0], 0) * 4 + (3 if s[0] in prev else 0)
                    + (6 if s[2] - s[1] < d * 0.75 else 0) + rnd.random())
        seg = min(cand, key=score)
    sid = f'{seg[0]}@{seg[1]}'; used.add(sid)
    plan.append((seg[0], seg[1], seg[2], usage.get(sid, 0) % 2 == 1))
    usage[sid] = usage.get(sid, 0) + 1
if upath: json.dump(usage, open(upath, 'w'), indent=0)
print('planos:', ' '.join(f'{k}{s:g}{"↔" if f else ""}' for k, s, e, f in plan))

parts = []
for n in range(len(cuts) - 1):
    d = cuts[n + 1] - cuts[n]
    key, st, end, flip = plan[n]
    c = P['clips'][key]; src = F(c['src'])
    end = min(end, dur(src))
    avail = end - st
    slow = max(1.0, d / avail) if avail > 0 else 1.0          # si el tramo es corto, se estira un poco
    z0 = c.get('zoom', 1.0); yb = c.get('ybias', 0.5)
    zin = n % 2 == 0
    zexp = f"{z0}*(1+0.07*t/{d:.3f})" if zin else f"{z0}*(1.07-0.07*t/{d:.3f})"
    vf = (f"setpts={slow:.4f}*(PTS-STARTPTS),fps={FPS},"
          f"scale=w='max({W}/iw,{H}/ih)*iw*{zexp}':h=-2:eval=frame:flags=bicubic,"
          f"crop={W}:{H}:(iw-{W})/2:(ih-{H})*{yb},{'hflip,' if flip else ''}setsar=1,format=yuv420p")
    pc = f'{tmp}/s{n:02d}.mp4'
    run([FF, '-v', 'error', '-y', '-ss', str(st), '-t', f'{min(avail, d / slow) + 0.1:.3f}', '-i', src, '-an',
         '-vf', vf, '-t', f'{d:.3f}', '-c:v', 'libx264', '-crf', '18', '-preset', 'fast', pc])
    parts.append(pc)
lst = f'{tmp}/all.txt'; open(lst, 'w').write(''.join(f"file '{p}'\n" for p in parts))
run([FF, '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', lst, '-c', 'copy', f'{tmp}/cat.mp4'])

# 4) subtítulos (3 palabras, la que suena en amarillo)
def ts(t): t = max(0, t); return f'{int(t // 3600)}:{int(t % 3600 // 60):02d}:{t % 60:05.2f}'
CAPY = P.get('capy', 1250)
HI = '&H0000E1FF&'
ass = [f'''[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: C,Arial Black,80,&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,1,0,0,0,100,100,0,0,1,8,3,5,70,70,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text''']
def clean(w): return w.replace('…', '').strip(' ,;:"“”').upper()
chunks, cur = [], []
for x in vw:
    cur.append(x)
    if len(cur) == 3 or re.search(r'[.?!…]$', x[2]): chunks.append(cur); cur = []
if cur: chunks.append(cur)
for ci, ch in enumerate(chunks):
    nxt = chunks[ci + 1][0][0] if ci + 1 < len(chunks) else ch[-1][1] + 0.4
    for wi, (s, e, w) in enumerate(ch):
        e2 = ch[wi + 1][0] if wi + 1 < len(ch) else min(nxt, ch[-1][1] + 0.5)
        txt = ' '.join((f'{{\\c{HI}}}' + clean(x[2]) + '{\\r}') if j == wi else clean(x[2]) for j, x in enumerate(ch))
        ass.append(f'Dialogue: 0,{ts(s)},{ts(e2)},C,,0,0,0,,{{\\pos({W // 2},{CAPY})}}{txt}')
open(f'{tmp}/subs.ass', 'w').write('\n'.join(ass) + '\n')

# 5) música baja + efectos puntuales (cha-ching en la plata, ding, pop; whoosh solo en algunos cortes)
run(['python3', os.path.join(DIR, 'music.py'), f'{L + 1:.2f}', f'{tmp}/music.wav'])
if not os.path.exists(f'{tmp}/sfx/whoosh.wav'): run(['python3', os.path.join(DIR, 'sfx.py'), f'{tmp}/sfx'])
VOL = {'chaching': 0.32, 'ding': 0.28, 'pop': 0.30, 'whoosh': 0.20, 'sello': 0.28}
hits = [('whoosh', cuts[i] - 0.18) for i in P.get('whoosh', [1]) if 0 < i < len(cuts) - 1]
for snd, word, occ in P.get('sfx', []):
    ts_ = [w[0] for w in vw if norm(w[2]) == norm(word)]
    if occ < len(ts_): hits.append((snd, ts_[occ] - 0.05))
    else: print(f'aviso: "{word}" n.º {occ} no aparece')
ins = ['-i', f'{tmp}/cat.mp4', '-i', f'{tmp}/vo.wav', '-i', f'{tmp}/music.wav'] + sum([['-i', f'{tmp}/sfx/{s}.wav'] for s, _ in hits], [])
fc = [f"[0:v]ass={tmp}/subs.ass[v]", f"[2:a]volume=0.10,afade=t=out:st={max(0, L - 1.2):.2f}:d=1.2[m]"]
for k, (s, t) in enumerate(hits):
    ms = int(max(0, t) * 1000)
    fc.append(f"[{3 + k}:a]volume={VOL[s]},adelay={ms}|{ms}[w{k}]")
fc.append(f"[1:a][m]{''.join(f'[w{k}]' for k in range(len(hits)))}amix=inputs={2 + len(hits)}:duration=first:normalize=0[a]")
run([FF, '-v', 'error', '-y'] + ins + ['-filter_complex', ';'.join(fc), '-map', '[v]', '-map', '[a]',
     '-c:v', 'libx264', '-crf', '18', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k', '-t', f'{L:.2f}',
     '-movflags', '+faststart', OUT])
print(f'OK {OUT} {L:.1f}s, {len(cuts) - 1} planos (promedio {L / (len(cuts) - 1):.1f}s)')
