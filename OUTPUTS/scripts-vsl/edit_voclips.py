"""Voz en off sobre clips de recetas (Pan Sin Picos, 2026-10-19).
Cada plano se ancla a la frase del guion donde empieza; dura hasta el próximo ancla.
Zoom lento por plano, sin audio original, subtítulos de 3 palabras con la activa en amarillo y música baja.
Uso: python3 edit_voclips.py plan.json salida.mp4
plan.json:
{
 "vo": "vo1.wav", "script": "g1.txt", "speed": 1.1, "capy": 1380,
 "shots": [
   {"at": "Mi papá", "src": "v1.mp4", "ss": 0.0},
   {"at": "Y hace quince", "src": "v6.mp4", "ss": 2.0, "crop": [0.78, 0.07]}   # crop: [escala, y0] para sacar logos o franjas
 ]
}
"""
import os, re, sys, json, subprocess, difflib
from faster_whisper import WhisperModel

FF = os.path.expanduser('~/bin/ffmpeg')
MUSIC_PY = '/Users/santiagoseara/PrepCourse-Henry/OUTPUTS/scripts-vsl/music.py'
P = json.load(open(sys.argv[1])); OUT = sys.argv[2]
base = os.path.dirname(os.path.abspath(sys.argv[1]))
def F(p): return p if os.path.isabs(p) else os.path.join(base, p)
tmp = os.path.join(base, os.path.basename(OUT) + '_tmp'); os.makedirs(tmp, exist_ok=True)
W, H, FPS = 1080, 1920, 30
def run(c): subprocess.run(c, check=True)
def norm(w): return re.sub(r'[^\wáéíóúñü]', '', w.lower())
model = WhisperModel('small', device='cpu', compute_type='int8')

# 1) voz: recorte de silencios + velocidad, palabras alineadas al guion
sp = P.get('speed', 1.1)
run([FF, '-v', 'error', '-y', '-i', F(P['vo']), '-af',
     'silenceremove=start_periods=1:start_threshold=-45dB:stop_periods=-1:stop_duration=0.30:stop_threshold=-40dB:stop_silence=0.15,'
     f'atempo={sp:.4f},aresample=48000', '-ac', '2', f'{tmp}/vo.wav'])
segs, _ = model.transcribe(f'{tmp}/vo.wav', language='es', word_timestamps=True)
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
L = int(hh) * 3600 + int(mm) * 60 + float(ss) + 0.35

# 2) anclar cada plano a su frase
nb, starts, k0 = [norm(x[2]) for x in vw], [], 0
for i, sh in enumerate(P['shots']):
    ph = [norm(x) for x in sh['at'].split()]
    k = next(k for k in range(k0, len(nb)) if nb[k:k + len(ph)] == ph)
    starts.append(0.0 if i == 0 else vw[k][0] - 0.08); k0 = k + 1

# 3) cortar los planos (zoom lento, sin audio)
parts = []
for i, sh in enumerate(P['shots']):
    d = (starts[i + 1] if i + 1 < len(starts) else L) - starts[i]
    sc, y0 = sh.get('crop', [1.0, None])
    crop = f'crop=iw*{sc}:ih*{sc}:(iw-iw*{sc})/2:ih*{y0 if y0 is not None else (1 - sc) / 2},' if sc < 1 else ''
    z0, z1 = (1.0, 1.07) if i % 2 == 0 else (1.07, 1.0)
    vf = (f"{crop}scale={W}:{H}:force_original_aspect_ratio=increase:flags=lanczos,crop={W}:{H},"
          f"scale=w='trunc({W}*({z0}+({z1}-{z0})*t/{d:.3f})/2)*2':h=-2:eval=frame:flags=bicubic,"
          f"crop={W}:{H},unsharp=5:5:0.6,fps={FPS},format=yuv420p")
    pc = f'{tmp}/p{i:02d}.mp4'
    run([FF, '-v', 'error', '-y', '-ss', str(sh['ss']), '-t', f'{d:.3f}', '-i', F(sh['src']), '-an', '-vf', vf,
         '-frames:v', str(round(d * FPS)), '-c:v', 'libx264', '-crf', '18', pc])
    parts.append(pc)
lst = f'{tmp}/all.txt'; open(lst, 'w').write(''.join(f"file '{p}'\n" for p in parts))
run([FF, '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', lst, '-c', 'copy', f'{tmp}/cat.mp4'])

# 4) subtítulos (3 palabras, la que suena en amarillo)
def ts(t): t = max(0, t); return f'{int(t // 3600)}:{int(t % 3600 // 60):02d}:{t % 60:05.2f}'
CAPY = P.get('capy', 1380)
STY = 'Arial Black,76,&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,1,0,0,0,100,100,0,0,1,8,2'
HI = '&H0000E1FF&'
ass = [f'''[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: C,{STY},5,70,70,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text''']
def clean(w): return w.replace('…', '').strip(' ,;:"“”').upper()
chunks, cur = [], []
for x in vw:
    cur.append(x)
    if len(cur) == 3 or re.search(r'[.?!…:]$', x[2]): chunks.append(cur); cur = []
if cur: chunks.append(cur)
for ci, ch in enumerate(chunks):
    nxt = chunks[ci + 1][0][0] if ci + 1 < len(chunks) else ch[-1][1] + 0.4
    for wi, (s, e, w) in enumerate(ch):
        e2 = ch[wi + 1][0] if wi + 1 < len(ch) else min(nxt, ch[-1][1] + 0.5)
        txt = ' '.join((f'{{\\c{HI}}}' + clean(x[2]) + '{\\r}') if j == wi else clean(x[2]) for j, x in enumerate(ch))
        ass.append(f'Dialogue: 0,{ts(s)},{ts(e2)},C,,0,0,0,,{{\\pos({W // 2},{CAPY})}}{txt}')
open(f'{tmp}/subs.ass', 'w').write('\n'.join(ass) + '\n')

# 5) música baja + mezcla final
run(['python3', MUSIC_PY, f'{L + 1:.2f}', f'{tmp}/music.wav'])
run([FF, '-v', 'error', '-y', '-i', f'{tmp}/cat.mp4', '-i', f'{tmp}/vo.wav', '-i', f'{tmp}/music.wav', '-filter_complex',
     f"[0:v]ass={tmp}/subs.ass[v];[1:a]apad,atrim=0:{L:.3f},loudnorm=I=-15:TP=-1.5[vo];"
     f"[2:a]volume=0.10,atrim=0:{L:.3f},afade=t=out:st={max(0, L - 1.2):.2f}:d=1.2[m];[vo][m]amix=inputs=2:duration=first:normalize=0[a]",
     '-map', '[v]', '-map', '[a]', '-t', f'{L:.3f}', '-c:v', 'libx264', '-crf', '20', '-maxrate', '8M', '-bufsize', '16M',
     '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k', '-movflags', '+faststart', OUT])
print(f'OK {OUT} {L:.1f}s')
