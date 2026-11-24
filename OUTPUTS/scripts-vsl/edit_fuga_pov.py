# -*- coding: utf-8 -*-
"""Molde A de FUGA PERFECTA: el ad corto SIN voz, calcado de casocriminal.shop.
Medido sobre sus 10 ads: 7 a 16 s, musica viral sola, UNA placa POV arriba fija todo el video,
UN banner de oferta abajo fijo todo el video, jump cuts de ~1 s sobre la mesa, sin placa final.
Uso: python3 edit_fuga_pov.py plan.json salida.mp4"""
import os, re, sys, json, subprocess, random
from PIL import Image, ImageDraw, ImageFont

FF = os.path.expanduser('~/bin/ffmpeg')
DIR = os.path.dirname(os.path.abspath(__file__))
P = json.load(open(sys.argv[1])); OUT = sys.argv[2]
base = os.path.dirname(os.path.abspath(sys.argv[1]))
def F(p): return p if os.path.isabs(p) else os.path.join(base, p)
tmp = os.path.join(base, os.path.basename(OUT) + '_tmp'); os.makedirs(tmp, exist_ok=True)
W, H, FPS = 1080, 1920, 30
FD = os.path.join(DIR, 'fonts')
FONT_B = FD + '/Montserrat-ExtraBold.ttf'
def run(c): subprocess.run(c, check=True)
def font(sz, p=FONT_B): return ImageFont.truetype(p, sz)
def dur(p):
    r = subprocess.run([FF, '-i', p], capture_output=True, text=True).stderr
    h, m, s = re.search(r'Duration: (\d+):(\d+):([\d.]+)', r).groups()
    return int(h) * 3600 + int(m) * 60 + float(s)

# 1) plan de planos: cortes parejos, sin repetir ventana, sin dos clips seguidos del mismo origen
L = float(P.get('dur', 12))
paso = P.get('cut', 1.15)
n = max(4, round(L / paso))
cuts = [round(L * i / n, 3) for i in range(n + 1)]
rnd = random.Random(P.get('seed', 0))
upath = F(P['usage']) if 'usage' in P else None
usage = json.load(open(upath)) if upath and os.path.exists(upath) else {}
def fam(k): return P['clips'].get(k, {}).get('fam') or k
plan, used = [], set()
for i in range(n):
    d = cuts[i + 1] - cuts[i]
    prev = plan[-1][0] if plan else None
    if i == 0 and P.get('first'):
        seg = next(s for s in P['pool'] if s[0] == P['first'][0] and s[1] == P['first'][1])
    else:
        cand = [s for s in P['pool'] if f'{s[0]}@{s[1]}' not in used and fam(s[0]) != fam(prev)]
        if not cand: cand = [s for s in P['pool'] if fam(s[0]) != fam(prev)] or P['pool']
        cand.sort(key=lambda s: (usage.get(f'{s[0]}@{s[1]}', 0) * 10
                                 + (6 if s[2] - s[1] < d * 0.8 else 0) + rnd.random()))
        seg = cand[0]
    sid = f'{seg[0]}@{seg[1]}'; used.add(sid)
    usage[sid] = usage.get(sid, 0) + 1
    plan.append(seg)
if upath: json.dump(usage, open(upath, 'w'), indent=0)
print('planos:', ' '.join(f'{k}:{s:g}' for k, s, e in plan))

parts = []
for i, (key, st, end) in enumerate(plan):
    d = cuts[i + 1] - cuts[i]
    c = P['clips'][key]; src = F(c['src'])
    end = min(end, dur(src)); avail = end - st
    slow = max(1.0, d / avail) if avail > 0 else 1.0
    z0 = c.get('zoom', 1.0); yb = c.get('ybias', 0.5)
    punch = "(1+0.14*max(0,1-t/0.20))" if i > 0 else "1"
    vf = (f"setpts={slow:.4f}*(PTS-STARTPTS),fps={FPS},"
          f"scale=w='ceil(max({W}/iw,{H}/ih)*iw*{z0}*(1+0.05*t/{d:.3f})*{punch}/2)*2':h=-2:eval=frame:flags=bicubic,"
          f"crop={W}:{H}:(iw-{W})/2:(ih-{H})*{yb},setsar=1,format=yuv420p")
    pc = f'{tmp}/s{i:02d}.mp4'
    run([FF, '-v', 'error', '-y', '-ss', str(st), '-t', f'{min(avail, d / slow) + 0.1:.3f}', '-i', src,
         '-an', '-vf', vf, '-t', f'{d:.3f}', '-c:v', 'libx264', '-crf', '18', '-preset', 'fast', pc])
    parts.append(pc)
lst = f'{tmp}/all.txt'; open(lst, 'w').write(''.join(f"file '{p}'\n" for p in parts))
run([FF, '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', lst, '-c', 'copy', f'{tmp}/cat.mp4'])

# 2) la placa POV de arriba y el banner de abajo, los dos fijos todo el video
ov = Image.new('RGBA', (W, H)); d = ImageDraw.Draw(ov)
def caja(txt, y0, size, ancho, bg, fg, pad, radio):
    lines = [l.strip() for l in txt.split('|') if l.strip()]
    f = font(size)
    while max(d.textlength(l, font=f) for l in lines) > ancho and f.size > 26:
        f = font(f.size - 2)
    lh = int(f.size * 1.30); bh = len(lines) * lh + pad
    if radio:
        bw = max(d.textlength(l, font=f) for l in lines) + pad * 2
        x0 = (W - bw) / 2
        d.rounded_rectangle((x0 + 5, y0 + 7, x0 + bw + 5, y0 + bh + 7), radio, fill=(0, 0, 0, 80))
        d.rounded_rectangle((x0, y0, x0 + bw, y0 + bh), radio, fill=bg)
    else:
        d.rectangle((0, y0, W, y0 + bh), fill=bg)
    for i, l in enumerate(lines):
        d.text((W / 2, y0 + pad // 2 + i * lh), l, font=f, fill=fg, anchor='mt')
oscuro = P.get('pov_bg', 'blanco') == 'negro'
caja(P['pov'], P.get('pov_y', 150), P.get('pov_size', 56), 780,
     (18, 18, 18, 215) if oscuro else (255, 255, 255, 248),
     (255, 255, 255) if oscuro else (16, 16, 16), 26, 12)
caja(P['banner'].upper(), P.get('banner_y', 1610), P.get('banner_size', 46), 940,
     (14, 14, 14, 205), (255, 255, 255), 30, 0)
ov.save(f'{tmp}/ov.png')

# 3) musica sola, al frente (no hay voz que tapar)
import numpy as np, soundfile as sf
m_, sr_ = sf.read(F(P['music']))
if m_.ndim == 1: m_ = np.stack([m_, m_], 1)
need = int((L + 0.4) * sr_); xf = int(1.0 * sr_)
while len(m_) < need:
    a2 = m_[int(4 * sr_):]; r_ = np.linspace(0, 1, xf)[:, None]
    m_ = np.concatenate([m_[:-xf], m_[-xf:] * (1 - r_) + a2[:xf] * r_, a2[xf:]])
off = int(P.get('music_start', 0) * sr_)
m_ = np.concatenate([m_[off:], m_[:off]])[:need]
m_ = m_ / max(1e-6, np.abs(m_).max()) * 10 ** (P.get('music_db', -3) / 20)
fo = int(1.0 * sr_); m_[-fo:] *= np.linspace(1, 0, fo)[:, None]
sf.write(f'{tmp}/music.wav', np.clip(m_, -1, 1), sr_)

run([FF, '-v', 'error', '-y', '-i', f'{tmp}/cat.mp4', '-i', f'{tmp}/ov.png', '-i', f'{tmp}/music.wav',
     '-filter_complex', '[0:v][1:v]overlay=0:0:format=auto[v]', '-map', '[v]', '-map', '2:a',
     '-c:v', 'libx264', '-crf', '18', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k',
     '-t', f'{L:.2f}', '-movflags', '+faststart', OUT])
print(f'OK {OUT} {L:.1f}s, {n} planos (promedio {L/n:.2f}s)')
