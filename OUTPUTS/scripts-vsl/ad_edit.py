"""Ad de voz en off sobre las visuales del competidor (Kit Patitas Felices, 2026-10-16).
Uso: python3 ad_edit.py <clean.mp4> <vo.mp3> <salida.mp4> [--cut S] [--end kling.mp4] [--skip a-b,c-d]
       [--insert a-b:clip.mp4,...] [--anchor "son las 200"] [--style classic|pop|box|lower|tiktok|story]
       [--zoom] [--bar] [--title "TEXTO"] [--capy 1490]
- Visuales del competidor (sin subtítulos) hasta --cut (donde muestran SU producto). Desde la frase de los "4 bonos"
  (o la frase de --anchor) entra nuestro plano final de Kling con el Kit Patitas Felices.
- --insert reemplaza un tramo del original por un clip nuestro (ej. páginas del libro traducidas al español).
- Voz: silencios recortados y 1.2x fija (pedido de Santiago). Las visuales se re-temporizan para calzar.
- Estilos de subtítulo distintos para variar la edición entre anuncios (pedido de Santiago, 2026-10-16).
"""
import os, re, argparse, subprocess
from faster_whisper import WhisperModel

FF = os.path.expanduser('~/bin/ffmpeg')
MUSIC_PY = '/Users/santiagoseara/PrepCourse-Henry/OUTPUTS/scripts-vsl/music.py'
ap = argparse.ArgumentParser()
ap.add_argument('src'); ap.add_argument('vo'); ap.add_argument('out')
ap.add_argument('--cut', type=float); ap.add_argument('--end'); ap.add_argument('--skip', default='')
ap.add_argument('--insert', default=''); ap.add_argument('--anchor', default='')
ap.add_argument('--style', default='classic'); ap.add_argument('--zoom', action='store_true')
ap.add_argument('--bar', action='store_true'); ap.add_argument('--title', default='')
ap.add_argument('--capy', type=int, default=1490); ap.add_argument('--speed', type=float, default=1.2)
A = ap.parse_args()
tmp = A.out + '_tmp'; os.makedirs(tmp, exist_ok=True)
W, H = 1080, 1920

def run(c): subprocess.run(c, check=True)
def dur(f):
    r = subprocess.run([FF, '-i', f], capture_output=True, text=True).stderr
    h, m, s = re.search(r'Duration: (\d+):(\d+):([\d.]+)', r).groups()
    return int(h) * 3600 + int(m) * 60 + float(s)
def norm(w): return re.sub(r'[^\wáéíóúñü]', '', w.lower())

model = WhisperModel('small', device='cpu', compute_type='int8')
def words(f):
    segs, _ = model.transcribe(f, language='es', word_timestamps=True)
    return [(w.start, w.end, w.word.strip()) for s in segs for w in s.words]

# 1) voz: recorte de silencios y velocidad fija
run([FF, '-v', 'error', '-y', '-i', A.vo, '-af',
     'silenceremove=start_periods=1:start_threshold=-45dB:stop_periods=-1:stop_duration=0.15:stop_threshold=-40dB:stop_silence=0.07,aresample=48000',
     '-ac', '2', f'{tmp}/vo_trim.wav'])
raw = words(f'{tmp}/vo_trim.wav')
D = raw[-1][1] + 0.15
sp = A.speed
run([FF, '-v', 'error', '-y', '-i', f'{tmp}/vo_trim.wav', '-af', f'atempo={sp:.4f}', f'{tmp}/vo.wav'])
L = D / sp + 0.5
wd = [(s / sp, e / sp, w) for s, e, w in raw]

tb = None
if A.end:
    if A.anchor:
        ph = [norm(x) for x in A.anchor.split()]
        for i in range(len(raw) - len(ph) + 1):
            if [norm(raw[i + k][2]) for k in range(len(ph))] == ph: tb = raw[i][0]; break
    else:
        for i, (s, e, w) in enumerate(raw):
            if 'bono' in w.lower():
                j = i
                for k in range(i - 1, max(-1, i - 6), -1):
                    if norm(raw[k][2]) in ('y', 'encima', 'viene', 'te', 'llevás'): j = k
                    if re.search(r'[.:;]$', raw[k - 1][2] if k else '.'): break
                tb = raw[j][0]; break
    tb = tb / sp - 0.3

# 2) segmentos del original (+ saltos e insertos)
vis = dur(A.src)
end = A.cut if A.cut else vis
skips = [tuple(map(float, s.split('-'))) for s in A.skip.split(',') if s]
inserts = []
for s in [x for x in A.insert.split(',') if x]:
    rng, f = s.split(':', 1); a, b = map(float, rng.split('-')); inserts.append((a, b, f))
cuts = sorted([(a, b, None) for a, b in skips] + inserts)
segs, t0 = [], 0.0
for a, b, f in cuts + [(end, end, None)]:
    if a > t0: segs.append(('src', t0, a))
    if f: segs.append((f, a, b))
    t0 = max(t0, b)
seg_len = sum(b - a for _, a, b in segs)
targetA = tb if A.end else L
fA = targetA / seg_len
print(f'voz {D:.1f}s -> {sp:.2f}x = {L:.1f}s | visual {seg_len:.1f}s x{fA:.2f} | producto en {tb}')

fit = 'scale=1080:1920:force_original_aspect_ratio=increase:flags=lanczos,crop=1080:1920,setsar=1,fps=30'
def kb(i, n):   # zoom lento (Ken Burns), alterna adentro/afuera
    if not A.zoom: return ''
    z = f"1+0.10*on/{n}" if i % 2 == 0 else f"1.10-0.10*on/{n}"
    return f",zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1080x1920:fps=30"
ins, fc, labels = ['-i', A.src], [], ''
files = {}
for i, (f, a, b) in enumerate(segs):
    n = max(1, int((b - a) * fA * 30))
    if f == 'src':
        fc.append(f'[0:v]trim={a}:{b},setpts=(PTS-STARTPTS)*{fA:.4f},{fit}{kb(i, n)}[s{i}]')
    else:
        if f not in files: files[f] = len(files) + 1; ins += ['-i', f]
        k = files[f]; need = (b - a) * fA; cd = dur(f)
        fE = max(need / cd, 0.6)
        fc.append(f'[{k}:v]setpts=(PTS-STARTPTS)*{fE:.4f},{fit},tpad=stop_mode=clone:stop_duration=1,trim=0:{need:.3f},setpts=PTS-STARTPTS{kb(i, n)}[s{i}]')
    labels += f'[s{i}]'
n = len(segs)
if A.end:
    ins += ['-i', A.end]; k = len(files) + 1
    need = L - tb; ed = dur(A.end)
    if need <= ed * 1.2:
        fc.append(f'[{k}:v]setpts=(PTS-STARTPTS)*{max(1.0, need / ed):.4f},{fit},tpad=stop_mode=clone:stop_duration=0.5,trim=0:{need:.3f}[e]')
    else:
        fc.append(f'[{k}:v]setpts=(PTS-STARTPTS)*{max(1.0, need / (2 * ed)):.4f},{fit},split[e1][e2];[e2]reverse[er];[e1][er]concat=n=2:v=1:a=0,'
                  f'tpad=stop_mode=clone:stop_duration=0.5,trim=0:{need:.3f}[e]')
    labels += '[e]'; n += 1
fc.append(f'{labels}concat=n={n}:v=1:a=0,trim=0:{L:.3f},setpts=PTS-STARTPTS[v]')
run([FF, '-v', 'error', '-y', *ins, '-filter_complex', ';'.join(fc), '-map', '[v]', '-c:v', 'libx264', '-crf', '16', '-pix_fmt', 'yuv420p', f'{tmp}/vis.mp4'])

# 3) subtítulos (ASS) según el estilo
def ts(t): t = max(0, t); return f'{int(t // 3600)}:{int(t % 3600 // 60):02d}:{t % 60:05.2f}'
ST = {   # nombre: (palabras por bloque, estilo ASS, color palabra activa, mayúsculas, pop)
    'classic': (3, 'Arial Black,72,&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,1,0,0,0,100,100,0,0,1,7,2', '&H0000E1FF&', True, False),
    'pop':     (2, 'Arial Black,100,&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,1,0,0,0,100,100,0,0,1,9,3', '&H0050FF7A&', True, True),
    'box':     (5, 'Arial Black,58,&H00111111,&H00111111,&H00FFFFFF,&H00FFFFFF,1,0,0,0,100,100,0,0,3,14,0', '&H00D06A00&', True, False),
    'lower':   (2, 'Arial Black,86,&H0000E1FF,&H0000E1FF,&H00000000,&H64000000,1,0,0,0,100,100,0,0,1,8,2', '&H00FFFFFF&', True, True),
    'tiktok':  (3, 'Helvetica Neue,76,&H00FFFFFF,&H00FFFFFF,&H00000000,&H96000000,1,0,0,0,100,100,0,0,1,0,5', '&H0000E1FF&', False, False),
    'story':   (6, 'Arial,60,&H00FFFFFF,&H00FFFFFF,&H00000000,&H96000000,1,0,0,0,100,100,0,0,1,0,4', None, False, False),
}
nw, sty, hi, upper, pop = ST[A.style]
ass = [f'''[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: C,{sty},5,70,70,0,1
Style: T,Arial Black,64,&H00111111,&H00111111,&H00FFFFFF,&H00FFFFFF,1,0,0,0,100,100,0,0,3,18,0,5,80,80,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text''']
def clean(w):
    w = w.replace('…', '').strip(' ,;:"“”')
    if not upper: return w.lower().strip('.')
    return w.upper()
chunks, cur = [], []
for x in wd:
    cur.append(x)
    if len(cur) == nw or re.search(r'[.?!]$', x[2]): chunks.append(cur); cur = []
if cur: chunks.append(cur)
for ci, ch in enumerate(chunks):
    nxt = chunks[ci + 1][0][0] if ci + 1 < len(chunks) else ch[-1][1] + 0.4
    if hi is None:   # 'story': frase entera, sin palabra activa
        txt = ' '.join(clean(x[2]) for x in ch)
        txt = txt[:1].upper() + txt[1:]
        ass.append(f'Dialogue: 0,{ts(ch[0][0])},{ts(min(nxt, ch[-1][1] + 0.6))},C,,0,0,0,,{{\\pos({W // 2},{A.capy})}}{txt}')
        continue
    for wi, (s, e, w) in enumerate(ch):
        e2 = ch[wi + 1][0] if wi + 1 < len(ch) else min(nxt, ch[-1][1] + 0.6)
        txt = ' '.join((f'{{\\c{hi}}}' + clean(x[2]) + '{\\r}') if j == wi else clean(x[2]) for j, x in enumerate(ch))
        fx = '\\fscx118\\fscy118\\t(0,90,\\fscx100\\fscy100)' if pop and wi == 0 else ''
        ass.append(f'Dialogue: 0,{ts(s)},{ts(e2)},C,,0,0,0,,{{\\pos({W // 2},{A.capy}){fx}}}{txt}')
if A.title:
    ass.append(f'Dialogue: 1,{ts(0)},{ts(3.0)},T,,0,0,0,,{{\\pos({W // 2},330)\\fad(0,250)}}{A.title}')
open(f'{tmp}/subs.ass', 'w').write('\n'.join(ass) + '\n')

# 4) música + mezcla + barra de progreso + quemado
run(['python3', MUSIC_PY, f'{L + 1:.1f}', f'{tmp}/music.wav'])
vf = f"[0:v]ass={tmp}/subs.ass[vs]"
extra = []
if A.bar:
    extra = ['-f', 'lavfi', '-i', f'color=c=0xFFE100:s=1080x16:d={L + 1:.1f}']
    vf = f"[0:v]ass={tmp}/subs.ass[vs0];[3:v]format=rgba[bar];[vs0][bar]overlay=x='-W+W*t/{L:.2f}':y=0:eval=frame[vs]"
run([FF, '-v', 'error', '-y', '-i', f'{tmp}/vis.mp4', '-i', f'{tmp}/vo.wav', '-i', f'{tmp}/music.wav', *extra,
     '-filter_complex', f"[2:a]volume=0.10,afade=t=out:st={L - 1:.2f}:d=1[m];[1:a][m]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5[a];{vf}",
     '-map', '[vs]', '-map', '[a]', '-t', f'{L:.2f}', '-c:v', 'libx264', '-crf', '19', '-maxrate', '9M', '-bufsize', '14M',
     '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k', '-movflags', '+faststart', A.out])
print('OK', A.out, f'{dur(A.out):.1f}s')
