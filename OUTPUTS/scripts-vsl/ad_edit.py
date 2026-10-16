"""Ad de voz en off sobre las visuales del competidor (Kit Patitas Felices, 2026-10-16).
Uso: python3 ad_edit.py <clean.mp4> <vo.mp3> <salida.mp4> [corte_producto] [final_kling.mp4] [skip=a-b,c-d] [titulo]
- Las visuales (sin subtítulos) se usan hasta el corte donde el original muestra SU producto; desde la frase
  de los "4 bonos" entra nuestro plano final (Kling con el Kit Patitas Felices).
- La voz se acelera entre 1.0x y 1.3x (sin cambiar el tono) para que el ritmo sea el del original.
- Subtítulos como los del original: MAYÚSCULAS, 3 palabras, blancos con borde negro y la palabra que suena en amarillo,
  a la misma altura que los quemados (tapan cualquier resto del inpainting).
"""
import sys, os, json, subprocess, re
from faster_whisper import WhisperModel

FF = os.path.expanduser('~/bin/ffmpeg')
HERE = os.path.dirname(os.path.abspath(__file__))
MUSIC_PY = '/Users/santiagoseara/PrepCourse-Henry/OUTPUTS/scripts-vsl/music.py'
src, vo, out = sys.argv[1], sys.argv[2], sys.argv[3]
cut = float(sys.argv[4]) if len(sys.argv) > 4 and sys.argv[4] not in ('', '-') else None
endclip = sys.argv[5] if len(sys.argv) > 5 and sys.argv[5] not in ('', '-') else None
skips = [tuple(map(float, s.split('-'))) for s in sys.argv[6].split(',')] if len(sys.argv) > 6 and sys.argv[6] not in ('', '-') else []
title = sys.argv[7] if len(sys.argv) > 7 else ''
tmp = out + '_tmp'; os.makedirs(tmp, exist_ok=True)
W, H = 1080, 1920
CAP_Y = int(os.environ.get('CAP_Y', 1490))

def run(c): subprocess.run(c, check=True)
def dur(f):
    r = subprocess.run([FF, '-i', f], capture_output=True, text=True).stderr
    h, m, s = re.search(r'Duration: (\d+):(\d+):([\d.]+)', r).groups()
    return int(h) * 3600 + int(m) * 60 + float(s)

model = WhisperModel('small', device='cpu', compute_type='int8')
def words(f):
    segs, _ = model.transcribe(f, language='es', word_timestamps=True)
    return [(w.start, w.end, w.word.strip()) for s in segs for w in s.words]

# 1) voz: recorte de silencios (pedido de Santiago) y velocidad fija 1.2x
run([FF, '-v', 'error', '-y', '-i', vo, '-af',
     'silenceremove=start_periods=1:start_threshold=-45dB:stop_periods=-1:stop_duration=0.15:stop_threshold=-40dB:stop_silence=0.07,aresample=48000',
     '-ac', '2', f'{tmp}/vo_trim.wav'])
vo = f'{tmp}/vo_trim.wav'
raw = words(vo)
D = raw[-1][1] + 0.15
vis = dur(src)
seg_len = (cut if cut else vis) - sum(b - a for a, b in skips)
tb_raw = None
if endclip:
    for i, (s, e, w) in enumerate(raw):
        if 'bono' in w.lower():
            # "Y encima viene con 4 bonos": se arranca en la "y"/"encima" más cercana (máx. 5 palabras atrás)
            j = i
            for k in range(i - 1, max(-1, i - 6), -1):
                if re.sub(r'\W', '', raw[k][2].lower()) in ('y', 'encima', 'viene', 'te', 'llevás'): j = k
                if re.search(r'[.:;]$', raw[k - 1][2] if k else '.'): break
            tb_raw = raw[j][0]; break
speed = float(os.environ.get('SPEED', 1.2))
run([FF, '-v', 'error', '-y', '-i', vo, '-af', f'atempo={speed:.4f},aresample=48000', '-ac', '2', f'{tmp}/vo.wav'])
L = D / speed + 0.5
wd = [(s / speed, e / speed, w) for s, e, w in raw]
tb = (tb_raw / speed - 0.3) if endclip else None
print(f'voz {D:.1f}s -> {speed:.2f}x = {L:.1f}s | visual {seg_len:.1f}s | producto en {tb}')

# 2) visual: tramo del competidor (+ saltos) re-temporizado y plano final
fit = 'scale=1080:1920:force_original_aspect_ratio=increase:flags=lanczos,crop=1080:1920,setsar=1,fps=30'
partsA = []
t0, end = 0.0, (cut if cut else vis)
cuts = sorted(skips) + [(end, end)]
for a, b in cuts:
    if a > t0: partsA.append((t0, a))
    t0 = b
targetA = tb if endclip else L
fA = targetA / seg_len           # >1 = un poco más lento, <1 = más rápido
fc, ins, k = [], ['-i', src], 0
for i, (a, b) in enumerate(partsA):
    fc.append(f'[0:v]trim={a}:{b},setpts=(PTS-STARTPTS)*{fA:.4f},{fit}[a{i}]')
labels = ''.join(f'[a{i}]' for i in range(len(partsA)))
if endclip:
    ins += ['-i', endclip]
    need = L - tb
    ed = dur(endclip)
    if need <= ed * 1.2:
        fE = max(1.0, need / ed)
        fc.append(f'[1:v]setpts=(PTS-STARTPTS)*{fE:.4f},{fit},tpad=stop_mode=clone:stop_duration=0.5,trim=0:{need:.3f}[e]')
    else:   # ida y vuelta del plano final: sin congelar el cuadro
        fE = max(1.0, need / (2 * ed))
        fc.append(f'[1:v]setpts=(PTS-STARTPTS)*{fE:.4f},{fit},split[e1][e2];[e2]reverse[er];[e1][er]concat=n=2:v=1:a=0,'
                  f'tpad=stop_mode=clone:stop_duration=0.5,trim=0:{need:.3f}[e]')
    labels += '[e]'
    n = len(partsA) + 1
else:
    n = len(partsA)
fc.append(f'{labels}concat=n={n}:v=1:a=0,trim=0:{L:.3f},setpts=PTS-STARTPTS[v]')
run([FF, '-v', 'error', '-y', *ins, '-filter_complex', ';'.join(fc), '-map', '[v]', '-c:v', 'libx264', '-crf', '17', '-pix_fmt', 'yuv420p', f'{tmp}/vis.mp4'])

# 3) subtítulos (ASS)
def ts(t):
    t = max(0, t); return f'{int(t // 3600)}:{int(t % 3600 // 60):02d}:{t % 60:05.2f}'
ass = [f'''[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 2

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: C,Arial Black,72,&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,1,0,0,0,100,100,0,0,1,7,2,5,40,40,0,1
Style: T,Arial Black,92,&H0000E1FF,&H00FFFFFF,&H00000000,&H64000000,1,0,0,0,100,100,0,0,1,8,3,5,60,60,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text''']
def clean(w): return w.upper().replace('…', '').strip(' ,;:"“”')
chunks, cur = [], []
for x in wd:
    cur.append(x)
    if len(cur) == 3 or re.search(r'[.?!]$', x[2]): chunks.append(cur); cur = []
if cur: chunks.append(cur)
for ci, ch in enumerate(chunks):
    nxt = chunks[ci + 1][0][0] if ci + 1 < len(chunks) else ch[-1][1] + 0.4
    for wi, (s, e, w) in enumerate(ch):
        e2 = ch[wi + 1][0] if wi + 1 < len(ch) else min(nxt, ch[-1][1] + 0.6)
        txt = ' '.join(('{\\c&H0000E1FF&}' + clean(x[2]) + '{\\c&H00FFFFFF&}') if j == wi else clean(x[2]) for j, x in enumerate(ch))
        ass.append(f'Dialogue: 0,{ts(s)},{ts(e2)},C,,0,0,0,,{{\\pos({W // 2},{CAP_Y})}}{txt}')
if title:
    ass.append(f'Dialogue: 1,{ts(0)},{ts(2.6)},T,,0,0,0,,{{\\pos({W // 2},300)\\fad(0,200)}}{title}')
open(f'{tmp}/subs.ass', 'w').write('\n'.join(ass) + '\n')

# 4) música + mezcla + quemado
run(['python3', MUSIC_PY, f'{L + 1:.1f}', f'{tmp}/music.wav'])
run([FF, '-v', 'error', '-y', '-i', f'{tmp}/vis.mp4', '-i', f'{tmp}/vo.wav', '-i', f'{tmp}/music.wav',
     '-filter_complex', f"[2:a]volume=0.10,afade=t=out:st={L - 1:.2f}:d=1[m];[1:a]volume=1.0[v];[v][m]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5[a];"
     f"[0:v]ass={tmp}/subs.ass[vv]",
     '-map', '[vv]', '-map', '[a]', '-t', f'{L:.2f}', '-c:v', 'libx264', '-crf', '20', '-maxrate', '8M', '-bufsize', '12M',
     '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k', '-movflags', '+faststart', out])
print('OK', out, f'{dur(out):.1f}s')
