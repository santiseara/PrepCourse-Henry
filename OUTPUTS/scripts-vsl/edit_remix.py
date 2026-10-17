"""Remix de un ad de diálogo del competidor (Secreto de la Insulina, 2026-10-17).
Voz en off nueva (ElevenLabs) sobre cuadros congelados con zoom + fragmentos originales con su audio
(labios sincronizados) + cierre con el montaje final del original. Subtítulos nuevos en toda la pieza.
Uso: python3 edit_remix.py plan.json salida.mp4
plan.json:
{
 "src": "clean.mp4",            # original sin subtítulos
 "vo": "vo.mp3", "script": "vo.txt",
 "speed": 1.2, "capy": 1085, "style": "classic",
 "timeline": [
   {"type": "vo", "until": "culpa.", "frames": [26.0, 30.5]},     # tramo de voz hasta esa palabra, sobre cuadros congelados
   {"type": "orig", "a": 0.0, "b": 5.25, "text": "¿Así nomás? ..."}, # fragmento original con su audio
   {"type": "vo", "until": "mañana.", "frames": [8.0, 38.0, 16.0]},
   {"type": "vo", "until": "END", "clip": [72.0, 90.0]}             # voz sobre video corrido del original (mudo)
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
sp = P.get('speed', 1.2)
run([FF, '-v', 'error', '-y', '-i', F(P['vo']), '-af',
     'silenceremove=start_periods=1:start_threshold=-45dB:stop_periods=-1:stop_duration=0.25:stop_threshold=-40dB:stop_silence=0.13,'
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

# 2) cortar la voz en tramos según "until"
vo_parts, idx = [], 0
for it in P['timeline']:
    if it['type'] != 'vo': continue
    if it['until'] == 'END': j = len(vw) - 1
    else:
        j = next(k for k in range(idx, len(vw)) if vw[k][2] == it['until'])
    s = vw[idx][0] - 0.05 if idx else 0.0
    e = vw[j][1] + 0.12
    vo_parts.append((max(0, s), e, vw[idx:j + 1])); idx = j + 1

# 3) armar cada segmento (video 1080x1920 + audio)
segfiles, subs, t0, vi = [], [], 0.0, 0
for n, it in enumerate(P['timeline']):
    out = f'{tmp}/seg{n:02d}.mp4'
    if it['type'] == 'orig':
        d = it['b'] - it['a']
        run([FF, '-v', 'error', '-y', '-ss', str(it['a']), '-t', f'{d:.3f}', '-i', F(P['src']),
             '-vf', f'scale={W}:{H}:flags=lanczos,fps={FPS},format=yuv420p', '-af', 'aresample=48000,volume=1.15', '-ac', '2',
             '-c:v', 'libx264', '-crf', '17', '-c:a', 'aac', '-b:a', '192k', out])
        ws, _ = model.transcribe(out, language='es', word_timestamps=True)
        ow = [(w.start, w.end, w.word.strip()) for s in ws for w in s.words]
        txt = it['text'].split()
        oa, ob = [norm(x[2]) for x in ow], [norm(x) for x in txt]
        al = []
        for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, oa, ob, autojunk=False).get_opcodes():
            if op == 'equal': al += [(ow[i1 + k][0], ow[i1 + k][1], txt[j1 + k]) for k in range(i2 - i1)]
            elif j2 > j1:
                s0 = ow[i1][0] if i1 < len(ow) else (al[-1][1] if al else 0); e0 = ow[i2 - 1][1] if i2 > i1 else s0 + 0.3 * (j2 - j1)
                st = max(0.05, (e0 - s0) / (j2 - j1)); al += [(s0 + k * st, s0 + (k + 1) * st, txt[j1 + k]) for k in range(j2 - j1)]
        subs += [(t0 + s, t0 + e, w, it.get('capy', P.get('capy', 1085))) for s, e, w in al]
    else:
        s, e, words = vo_parts[vi]; vi += 1; d = e - s
        run([FF, '-v', 'error', '-y', '-ss', f'{s:.3f}', '-t', f'{d:.3f}', '-i', f'{tmp}/vo.wav', f'{tmp}/vo{n:02d}.wav'])
        if 'clip' in it:
            c0 = it['clip'][0]
            run([FF, '-v', 'error', '-y', '-ss', str(c0), '-t', f'{d:.3f}', '-i', F(it.get('src', P['src'])), '-i', f'{tmp}/vo{n:02d}.wav',
                 '-map', '0:v', '-map', '1:a', '-vf', f'scale={W}:{H}:flags=lanczos,fps={FPS},format=yuv420p',
                 '-c:v', 'libx264', '-crf', '17', '-c:a', 'aac', '-b:a', '192k', '-shortest', out])
        else:
            fr = it['frames']; k = len(fr); each = d / k; parts = []
            for m, ft in enumerate(fr):
                png = f'{tmp}/f{n:02d}_{m}.png'
                run([FF, '-v', 'error', '-y', '-ss', str(ft), '-i', F(P['src']), '-frames:v', '1', '-vf', f'scale={W*2}:{H*2}:flags=lanczos', png])
                nf = int(round(each * FPS)) + 1
                zin = (m % 2 == 0)
                z = "min(zoom+0.0009,1.12)" if zin else "if(eq(on,0),1.12,max(zoom-0.0009,1.0))"
                pc = f'{tmp}/p{n:02d}_{m}.mp4'
                run([FF, '-v', 'error', '-y', '-loop', '1', '-i', png, '-vf',
                     f"zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={nf}:s={W}x{H}:fps={FPS},format=yuv420p",
                     '-frames:v', str(nf), '-c:v', 'libx264', '-crf', '17', pc])
                parts.append(pc)
            lst = f'{tmp}/l{n:02d}.txt'; open(lst, 'w').write(''.join(f"file '{p}'\n" for p in parts))
            run([FF, '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', lst, '-i', f'{tmp}/vo{n:02d}.wav',
                 '-map', '0:v', '-map', '1:a', '-c:v', 'libx264', '-crf', '17', '-c:a', 'aac', '-b:a', '192k',
                 '-t', f'{d:.3f}', out])
        cy = it.get('capy', P.get('capy', 1085))
        subs += [(t0 + (x - s), t0 + (y - s), w, cy) for x, y, w in words]
    r = subprocess.run([FF, '-i', out], capture_output=True, text=True).stderr
    hh, mm, ss = re.search(r'Duration: (\d+):(\d+):([\d.]+)', r).groups()
    t0 += int(hh) * 3600 + int(mm) * 60 + float(ss); segfiles.append(out)
L = t0
lst = f'{tmp}/all.txt'; open(lst, 'w').write(''.join(f"file '{p}'\n" for p in segfiles))
run([FF, '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', lst, '-c:v', 'libx264', '-crf', '17', '-c:a', 'aac', '-b:a', '192k', f'{tmp}/cat.mp4'])

# 4) subtítulos (3 palabras, la que suena en amarillo, a la altura de los viejos para tapar restos)
def ts(t): t = max(0, t); return f'{int(t // 3600)}:{int(t % 3600 // 60):02d}:{t % 60:05.2f}'
CAPY = P.get('capy', 1085)
STY = {'classic': 'Arial Black,74,&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,1,0,0,0,100,100,0,0,1,8,2',
       'pop': 'Arial Black,96,&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,1,0,0,0,100,100,0,0,1,9,3'}[P.get('style', 'classic')]
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
for x in subs:
    cur.append(x)
    if len(cur) == 3 or re.search(r'[.?!…]$', x[2]) or (len(cur) > 1 and cur[-2][3] != x[3]):
        if len(cur) > 1 and cur[-2][3] != x[3]: chunks.append(cur[:-1]); cur = [x]; continue
        chunks.append(cur); cur = []
if cur: chunks.append(cur)
for ci, ch in enumerate(chunks):
    nxt = chunks[ci + 1][0][0] if ci + 1 < len(chunks) else ch[-1][1] + 0.4
    for wi, (s, e, w, cy) in enumerate(ch):
        e2 = ch[wi + 1][0] if wi + 1 < len(ch) else min(nxt, ch[-1][1] + 0.5)
        txt = ' '.join((f'{{\\c{HI}}}' + clean(x[2]) + '{\\r}') if j == wi else clean(x[2]) for j, x in enumerate(ch))
        ass.append(f'Dialogue: 0,{ts(s)},{ts(e2)},C,,0,0,0,,{{\\pos({W // 2},{cy})}}{txt}')
open(f'{tmp}/subs.ass', 'w').write('\n'.join(ass) + '\n')

# 5) música de fondo baja + mezcla final
run(['python3', MUSIC_PY, f'{L + 1:.2f}', f'{tmp}/music.wav'])
run([FF, '-v', 'error', '-y', '-i', f'{tmp}/cat.mp4', '-i', f'{tmp}/music.wav', '-filter_complex',
     f"[0:v]ass={tmp}/subs.ass[v];[1:a]volume=0.10,afade=t=out:st={max(0, L - 1.2):.2f}:d=1.2[m];[0:a][m]amix=inputs=2:duration=first:normalize=0[a]",
     '-map', '[v]', '-map', '[a]', '-c:v', 'libx264', '-crf', '18', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k',
     '-movflags', '+faststart', OUT])
print(f'OK {OUT} {L:.1f}s')
