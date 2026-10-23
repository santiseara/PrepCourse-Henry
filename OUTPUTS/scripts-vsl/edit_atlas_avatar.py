"""Ad UGC con avatar de HeyGen para The Women's Cutting Atlas (2026-10-23).
Misma estetica que edit_atlas.py (subtitulos en caja fucsia, chips rosas, placa final), pero la base
es el video de la avatar: habla a camara todo el tiempo y se corta a B-roll o a una foto del producto
solo en las palabras marcadas. La voz sale del propio video, asi que no se recortan silencios: video y
audio se aceleran juntos para que no se pierda el lipsync.
Uso: python3 edit_atlas_avatar.py plan.json salida.mp4
plan.json:
 "avatar": "../heygen/V14_avatar.mp4", "script": "../vo/V14.txt", "speed": 1.08, "lang": "en",
 "clips": {...}  (igual que edit_atlas.py),
 "cutaways": [["stylist", 0, "E", 0, 2.0], ...]   # palabra, ocurrencia, clip, segundo de inicio, duracion
 "hook": "...", "overlays": [...], "capy": 1240
"""
import os, re, sys, json, subprocess, difflib
from faster_whisper import WhisperModel
from PIL import Image, ImageDraw, ImageFont

FF = os.path.expanduser('~/bin/ffmpeg')
DIR = os.path.dirname(os.path.abspath(__file__))
P = json.load(open(sys.argv[1])); OUT = sys.argv[2]
base = os.path.dirname(os.path.abspath(sys.argv[1]))
def F(p): return p if os.path.isabs(p) else os.path.join(base, p)
tmp = os.path.join(base, os.path.basename(OUT) + '_tmp'); os.makedirs(tmp, exist_ok=True)
W, H, FPS = 1080, 1920, 30
ORANGE = (224, 28, 130)   # fucsia de la marca (se deja el nombre para no tocar el resto)
GOLD = (227, 190, 114)
PLUM = (59, 27, 57)
FONT = os.path.expanduser('~/Desktop/bachas-concreto/work-mark/fonts/Arial Black.ttf')
FONT_B = '/System/Library/Fonts/Supplemental/Arial Bold.ttf'
EMOJI = '/System/Library/Fonts/Apple Color Emoji.ttc'
ICONF = '/System/Library/Fonts/Supplemental/Arial Unicode.ttf'
def run(c): subprocess.run(c, check=True)
def norm(w): return re.sub(r'[^\w]', '', w.lower())
def dur(p):
    r = subprocess.run([FF, '-i', p], capture_output=True, text=True).stderr
    h, m, s = re.search(r'Duration: (\d+):(\d+):([\d.]+)', r).groups(); return int(h) * 3600 + int(m) * 60 + float(s)

# 1) avatar y voz: se aceleran juntos (sin recortar silencios, para no romper el lipsync)
sp = P.get('speed', 1.08)
AV = F(P['avatar'])
run([FF, '-v', 'error', '-y', '-i', AV, '-an', '-vf',
     f"setpts=PTS/{sp:.4f},fps={FPS},scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},setsar=1,format=yuv420p",
     '-c:v', 'libx264', '-crf', '18', '-preset', 'fast', f'{tmp}/av.mp4'])
run([FF, '-v', 'error', '-y', '-i', AV, '-vn', '-af',
     f'atempo={sp:.4f},aresample=48000,afade=t=in:d=0.02', '-ac', '2', f'{tmp}/vo.wav'])
AVL = dur(f'{tmp}/av.mp4')

# 2) palabras del guion alineadas al audio
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
L = dur(f'{tmp}/vo.wav') + 0.5
def wt(word, occ=0):
    ts_ = [w for w in vw if norm(w[2]) == norm(word)]
    if occ >= len(ts_): print(f'aviso: "{word}" n.º {occ} no aparece'); return None
    return ts_[occ]

# 3) linea de tiempo: la avatar de base, cortes a B-roll solo en las palabras marcadas
cw = []
for word, occ, key, st, d in P.get('cutaways', []):
    w = wt(word, occ)
    if not w: continue
    t0 = max(0.0, w[0] - 0.08)
    cw.append([t0, min(L, t0 + d), key, st])
cw.sort()
cut = []
for c in cw:
    if cut and c[0] < cut[-1][1] + 0.5:
        print(f'aviso: corte a {c[2]} en {c[0]:.1f}s pisa al anterior, se ignora'); continue
    cut.append(c)
if cut and cut[-1][1] > L - 0.6: cut[-1][1] = L     # el ultimo (la placa final) llega hasta el final
segments = []    # (tipo, t0, t1, key, st)
pos = 0.0
for t0, t1, key, st in cut:
    if t0 - pos > 0.5: segments.append(('av', pos, t0, None, None))
    elif t0 > pos: t0 = pos                           # tramo de avatar muy corto: el corte se adelanta
    segments.append(('br', t0, t1, key, st)); pos = t1
if L - pos > 0.3: segments.append(('av', pos, L, None, None))
print('planos:', ' '.join(f'{s[3] or "AVATAR"}:{s[2]-s[1]:.1f}s' for s in segments))

parts = []
for n, (kind, t0, t1, key, st) in enumerate(segments):
    d = t1 - t0
    pc = f'{tmp}/s{n:02d}.mp4'
    if kind == 'av':
        run([FF, '-v', 'error', '-y', '-ss', f'{t0:.3f}', '-t', f'{min(d, max(0.1, AVL - t0)):.3f}', '-i', f'{tmp}/av.mp4',
             '-an', '-vf', f'fps={FPS},setsar=1,format=yuv420p', '-t', f'{d:.3f}',
             '-c:v', 'libx264', '-crf', '18', '-preset', 'fast', pc])
        parts.append(pc); continue
    c = P['clips'][key]; src = F(c['src'])
    if c.get('still'):
        z = f"(1+0.07*t/{d:.3f})" if n % 2 == 0 else f"(1.07-0.07*t/{d:.3f})"
        vf = (f"[0:v]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS},"
              f"scale=w='{2*W}*{z}':h=-2:eval=frame:flags=bicubic,crop={2*W}:{2*H}:(iw-{2*W})/2:(ih-{2*H})/2,"
              f"scale={W}:{H}:flags=lanczos,setsar=1,format=yuv420p")
        run([FF, '-v', 'error', '-y', '-loop', '1', '-t', f'{d:.3f}', '-i', src, '-filter_complex', vf,
             '-t', f'{d:.3f}', '-r', str(FPS), '-c:v', 'libx264', '-crf', '18', '-preset', 'fast', pc])
        parts.append(pc); continue
    avail = max(0.1, min(dur(src) - st, 60))
    slow = max(1.0, d / avail)
    z0 = c.get('zoom', 1.0); yb = c.get('ybias', 0.5)
    vf = (f"setpts={slow:.4f}*(PTS-STARTPTS),fps={FPS},"
          f"scale=w='ceil(max({W}/iw,{H}/ih)*iw*{z0}/2)*2':h=-2:flags=lanczos,"
          f"crop={W}:{H}:(iw-{W})/2:(ih-{H})*{yb},setsar=1,format=yuv420p")
    run([FF, '-v', 'error', '-y', '-ss', str(st), '-t', f'{min(avail, d / slow) + 0.1:.3f}', '-i', src, '-an',
         '-vf', vf, '-t', f'{d:.3f}', '-c:v', 'libx264', '-crf', '18', '-preset', 'fast', pc])
    parts.append(pc)
lst = f'{tmp}/all.txt'; open(lst, 'w').write(''.join(f"file '{p}'\n" for p in parts))
run([FF, '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', lst, '-c', 'copy', f'{tmp}/cat.mp4'])

# 4) placas en PNG (hook, chips, placa final)
def font(sz, path=FONT): return ImageFont.truetype(path, sz)
def emoji_img(ch, h):
    try:
        f = ImageFont.truetype(EMOJI, 160)
        im = Image.new('RGBA', (200, 200)); ImageDraw.Draw(im).text((0, 0), ch, font=f, embedded_color=True)
        im = im.crop(im.getbbox()); return im.resize((int(im.width * h / im.height), h), Image.LANCZOS)
    except Exception: return None
def split_emoji(txt):
    m = re.search(r'\s*([\U0001F300-\U0001FAFF☀-➿]️?)\s*$', txt)
    return (txt[:m.start()], m.group(1)) if m else (txt, None)
def rrect(d, box, r, fill, outline=None, width=0): d.rounded_rectangle(box, r, fill=fill, outline=outline, width=width)

def png_hook(txt, path):
    im = Image.new('RGBA', (W, H)); d = ImageDraw.Draw(im)
    body, emo = split_emoji(txt); f = font(72, FONT_B)
    words, lines, cur = body.split(), [], ''
    for w_ in words:
        t_ = (cur + ' ' + w_).strip()
        if d.textlength(t_, font=f) > 820 and cur: lines.append(cur); cur = w_
        else: cur = t_
    lines.append(cur)
    em = emoji_img(emo, 68) if emo else None
    lw = [d.textlength(l, font=f) + (em.width + 14 if em and i == len(lines) - 1 else 0) for i, l in enumerate(lines)]
    bw, bh = max(lw) + 90, len(lines) * 88 + 56
    x0, y0 = (W - bw) / 2, 250
    rrect(d, (x0, y0, x0 + bw, y0 + bh), 26, (255, 255, 255, 250))
    for i, l in enumerate(lines):
        y = y0 + 28 + i * 88; x = (W - lw[i]) / 2
        d.text((x, y), l, font=f, fill=PLUM)
        if em and i == len(lines) - 1: im.alpha_composite(em, (int(x + d.textlength(l, font=f) + 14), int(y + 4)))
    im.save(path)

def png_chip(txt, icon, path):
    im = Image.new('RGBA', (W, H)); d = ImageDraw.Draw(im); f = font(50)
    t_ = txt.upper(); fi = font(52, ICONF)
    emo = emoji_img(icon, 56) if icon and ord(icon[0]) > 0x1F000 else None
    iw = (emo.width + 16) if emo else ((d.textlength(icon, font=fi) + 16) if icon else 0)
    tw = d.textlength(t_, font=f) + iw; bw, bh = tw + 70, 96
    x0, y0 = (W - bw) / 2, P.get('chipy', 560)
    rrect(d, (x0, y0, x0 + bw, y0 + bh), 48, ORANGE + (255,))
    if emo: im.alpha_composite(emo, (int(x0 + 35), int(y0 + 20)))
    elif icon: d.text((x0 + 35, y0 + 20), icon, font=fi, fill=(255, 255, 255))
    d.text((x0 + 35 + iw, y0 + 18), t_, font=f, fill=(255, 255, 255))
    im.save(path)

def png_end(o, path):
    im = Image.new('RGBA', (W, H)); d = ImageDraw.Draw(im)
    g = Image.new('RGBA', (W, H)); gd = ImageDraw.Draw(g)
    for y in range(0, 1100):
        gd.line([(0, y + 200), (W, y + 200)], fill=(36, 17, 36, int(170 * max(0, 1 - abs(y - 260) / 520))))
    im.alpha_composite(g)
    y = 250
    fa = font(64); t0_ = "THE WOMEN'S"
    d.text(((W - d.textlength(t0_, font=fa)) / 2, y), t0_, font=fa, fill=GOLD)
    fb = font(128)
    for i_, t_ in enumerate(['CUTTING', 'ATLAS']):
        x = (W - d.textlength(t_, font=fb)) / 2; yy = y + 80 + i_ * 140
        for dx, dy in [(-4, 0), (4, 0), (0, -4), (0, 4)]: d.text((x + dx, yy + dy), t_, font=fb, fill=PLUM + (230,))
        d.text((x, yy), t_, font=fb, fill=(255, 255, 255))
    y = y + 160
    fs = font(40); s = o.get('sub', 'Cut Maps + 5 bonuses · instant access')
    tw_ = d.textlength(s, font=fs); rrect(d, ((W - tw_) / 2 - 30, y + 205, (W + tw_) / 2 + 30, y + 270), 32, PLUM + (225,))
    d.text(((W - tw_) / 2, y + 214), s, font=fs, fill=(255, 255, 255))
    y = y + 990
    body, emo = split_emoji(o.get('cta', 'Tap Learn More 👇')); fc = font(58)
    em = emoji_img(emo, 58) if emo else None
    cwid = d.textlength(body, font=fc) + (em.width + 14 if em else 0); bw = cwid + 90
    x0, y0 = (W - bw) / 2, y + 300
    rrect(d, (x0, y0, x0 + bw, y0 + 104), 52, ORANGE + (255,))
    d.text((x0 + 45, y0 + 20), body, font=fc, fill=(255, 255, 255))
    if em: im.alpha_composite(em, (int(x0 + 45 + d.textlength(body, font=fc) + 14), int(y0 + 22)))
    im.save(path)

ovs = []      # (png, t0, t1)
hits = []     # (sonido, t)
if P.get('hook'):
    png_hook(P['hook'], f'{tmp}/o_hook.png'); ovs.append((f'{tmp}/o_hook.png', 0, P.get('hook_dur', 2.8)))
for k, o in enumerate(P.get('overlays', [])):
    w = wt(o['word'], o.get('occ', 0))
    if not w: continue
    t0 = w[0] - 0.05; pth = f'{tmp}/o{k}.png'
    if o['type'] == 'chip': png_chip(o['text'], o.get('icon', ''), pth); hits.append(('pop', t0))
    elif o['type'] == 'end': png_end(o, pth); hits.append(('ding', t0))
    t1 = L if o['type'] == 'end' else t0 + o.get('dur', 2.0)
    ovs.append((pth, t0, t1))
_e0 = min([t0 for p, t0, t1 in ovs if t1 == L] or [L])
ovs = [(p, t0, t1 if t1 == L else min(t1, _e0)) for p, t0, t1 in ovs if t1 == L or t0 < _e0 - 0.2]

# 5) subtitulos (3 palabras, la que suena en fucsia); se ocultan bajo la placa final
def ts(t): t = max(0, t); return f'{int(t // 3600)}:{int(t % 3600 // 60):02d}:{t % 60:05.2f}'
CAPY = P.get('capy', 1240)
HI = '&H0072BEE3&'
end_t = min([t0 for p, t0, t1 in ovs if t1 == L] or [L + 1])
ass = [f'''[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: C,Arial Black,74,&H00FFFFFF,&H00FFFFFF,&H00821CE0,&H00821CE0,0,0,0,0,100,100,0,0,3,14,0,5,60,60,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text''']
def clean(w): return w.replace('…', '').strip(' ,;:"“”').lower()
chunks, cur = [], []
for x in vw:
    cur.append(x)
    if len(cur) == 3 or re.search(r'[.?!…]$', x[2]): chunks.append(cur); cur = []
if cur: chunks.append(cur)
for ci, ch in enumerate(chunks):
    if ch[0][0] >= end_t - 0.05: continue
    nxt = chunks[ci + 1][0][0] if ci + 1 < len(chunks) else ch[-1][1] + 0.4
    for wi, (s, e, w) in enumerate(ch):
        e2 = ch[wi + 1][0] if wi + 1 < len(ch) else min(nxt, ch[-1][1] + 0.5)
        e2 = min(e2, end_t)
        txt = ' '.join((f'{{\\c{HI}}}' + clean(x[2]) + '{\\r}') if j == wi else clean(x[2]) for j, x in enumerate(ch))
        ass.append(f'Dialogue: 0,{ts(s)},{ts(e2)},C,,0,0,0,,{{\\pos({W // 2},{CAPY})}}{txt}')
open(f'{tmp}/subs.ass', 'w').write('\n'.join(ass) + '\n')

# 6) musica baja + efectos puntuales
run(['python3', os.path.join(DIR, 'music.py'), f'{L + 1:.2f}', f'{tmp}/music.wav'])
if not os.path.exists(f'{tmp}/sfx/whoosh.wav'): run(['python3', os.path.join(DIR, 'sfx.py'), f'{tmp}/sfx'])
VOL = {'chaching': 0.30, 'ding': 0.26, 'pop': 0.26, 'whoosh': 0.18}
hits += [('whoosh', s[1] - 0.18) for s in segments if s[0] == 'br' and s[1] > 0.5]
edges = sorted({0.0, L} | {max(0, min(L, x)) for _, t0, t1 in ovs for x in (t0, t1)})
blank = Image.new('RGBA', (W, H)); cache, lines_ = {}, []
for k in range(len(edges) - 1):
    a_, b_ = edges[k], edges[k + 1]
    if b_ - a_ < 0.01: continue
    act = tuple(i for i, (p_, t0, t1) in enumerate(ovs) if t0 <= a_ + 1e-3 and t1 >= b_ - 1e-3)
    if act not in cache:
        im = blank.copy()
        for i in act: im.alpha_composite(Image.open(ovs[i][0]).convert('RGBA'))
        cache[act] = f'{tmp}/ov_{len(cache)}.png'; im.save(cache[act])
    lines_.append(f"file '{cache[act]}'\nduration {b_ - a_:.3f}\n")
lines_.append(f"file '{cache[act]}'\n")
open(f'{tmp}/ov.txt', 'w').write(''.join(lines_))
run([FF, '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', f'{tmp}/ov.txt', '-vf', f'fps={FPS},format=argb',
     '-t', f'{L:.2f}', '-c:v', 'qtrle', f'{tmp}/ov.mov'])
run([FF, '-v', 'error', '-y', '-i', f'{tmp}/cat.mp4', '-i', f'{tmp}/ov.mov', '-filter_complex',
     f"[0:v][1:v]overlay=0:0:format=auto[ov];[ov]ass={tmp}/subs.ass[v]", '-map', '[v]',
     '-c:v', 'libx264', '-crf', '18', '-pix_fmt', 'yuv420p', '-t', f'{L:.2f}', f'{tmp}/video.mp4'])
ains = ['-i', f'{tmp}/vo.wav', '-i', f'{tmp}/music.wav'] + sum([['-i', f'{tmp}/sfx/{s_}.wav'] for s_, _ in hits], [])
afc = [f"[1:a]aresample=48000,volume=0.08,afade=t=out:st={max(0, L - 1.2):.2f}:d=1.2[m]"]
for k, (s_, t) in enumerate(hits):
    ms = int(max(0, t) * 1000)
    afc.append(f"[{2 + k}:a]aresample=48000,volume={VOL[s_]},adelay={ms}|{ms}[w{k}]")
afc.append(f"[0:a]apad=pad_dur=1[vo];[vo][m]{''.join(f'[w{k}]' for k in range(len(hits)))}amix=inputs={2 + len(hits)}:duration=first:normalize=0[a]")
run([FF, '-v', 'error', '-y'] + ains + ['-filter_complex', ';'.join(afc), '-map', '[a]', '-t', f'{L:.2f}', f'{tmp}/mix.wav'])
run([FF, '-v', 'error', '-y', '-i', f'{tmp}/video.mp4', '-i', f'{tmp}/mix.wav', '-map', '0:v', '-map', '1:a',
     '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-t', f'{L:.2f}', '-movflags', '+faststart', OUT])
print(f'OK {OUT} {L:.1f}s, {len(segments)} planos')
