"""V6 de tarot: el POV SIN VOZ, clonado del ad de 0:24 de Soyjulietacelis.

Su formato: musica sola, un unico cartel fijo en serif arriba durante todo el video, cortes
calmos de ASMR (hojear, barajar, subrayar) y nada mas. El "guion" es el texto en pantalla
(regla del 10/11, Date Night). Cierra con una placa sobre la tapa del ebook.

Uso: python3 edit_tarot_pov.py <dir_work> <salida.mp4>
"""
import os, sys, json, subprocess, random
from PIL import Image, ImageDraw, ImageFont

WD, OUT = sys.argv[1], sys.argv[2]
FF = os.path.expanduser('~/bin/ffmpeg')
if not os.path.exists(FF): FF = 'ffmpeg'
W, H = 1080, 1920
tmp = os.path.join(WD, os.path.basename(OUT) + '_tmp')
os.makedirs(tmp, exist_ok=True)

CARTEL = 'POV: the tarot guide that finally made it click'
END1, END2 = 'Your first reading in 2 days', 'Tap Learn more'

# orden de planos: ASMR, como el suyo — abrir, hojear, barajar, subrayar, cerrar sobre el producto
SEQ = [
    ('ia/drift.mp4',   0.3, 2.9),
    ('ia/pages.mp4',   0.4, 3.0),
    ('ebook/shot_cover.jpg', 0, 2.5),
    ('ia/fan.mp4',     1.6, 4.3),
    ('ebook/shot_tower.jpg', 0, 2.5),
    ('ia/marker.mp4',  0.5, 3.1),
    ('ia/shuffle.mp4', 1.0, 3.6),
    ('ebook/shot_star.jpg', 0, 2.4),
    ('ia/gather.mp4',  2.0, 4.6),
]
END_SHOT = ('ebook/shot_cover.jpg', 0, 3.2)

def F(p): return os.path.join(WD, p)

DID = '/System/Library/Fonts/Supplemental/Didot.ttc'
def didot(sz, it=False): return ImageFont.truetype(DID, sz, index=2 if it else 0)

def png_cartel(path):
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    f = didot(50)
    # dos lineas centradas, con sombra suave para que se lea sobre cualquier plano
    words, lines, cur = CARTEL.split(), [], ''
    for w in words:
        t = (cur + ' ' + w).strip()
        if d.textlength(t, font=f) <= W - 150: cur = t
        else: lines.append(cur); cur = w
    lines.append(cur)
    y = 300
    for ln in lines:
        x = (W - d.textlength(ln, font=f)) / 2
        for dx, dy in ((2, 3), (-2, 3), (0, 4)):
            d.text((x + dx, y + dy), ln, font=f, fill=(0, 0, 0, 110))
        d.text((x, y), ln, font=f, fill=(255, 255, 255, 242))
        y += 64
    im.save(path)

def png_end(path):
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rectangle([0, 0, W, H], fill=(16, 12, 10, 120))
    f1, f2 = didot(68), didot(44)
    y = 760
    for ln, f in ((END1, f1), (END2, f2)):
        x = (W - d.textlength(ln, font=f)) / 2
        d.text((x, y), ln, font=f, fill=(255, 255, 255, 248))
        y += 110
    d.line([(W/2 - 90, 900), (W/2 + 90, 900)], fill=(255, 255, 255, 170), width=1)
    im.save(path)

png_cartel(f'{tmp}/cartel.png')
png_end(f'{tmp}/end.png')

# --- cortar cada plano a 1080x1920
parts = []
for i, (src, a, b) in enumerate(SEQ + [END_SHOT]):
    out = f'{tmp}/p{i:02d}.mp4'
    d = b - a
    still = src.endswith(('.jpg', '.png'))
    zin = i % 2 == 0
    z = (f"(1+0.10*t/{d:.3f})" if zin else f"(1.10-0.10*t/{d:.3f})")
    if still:
        vf = (f"scale={W*2}:-1,crop={W*2}:{H*2}:0:(ih-{H*2})/2,"
              f"scale=w=iw*{z}:h=ih*{z}:eval=frame,crop={W}:{H},setsar=1,fps=30")
        cmd = [FF, '-v', 'error', '-y', '-loop', '1', '-t', f'{d:.3f}', '-i', F(src),
               '-vf', vf, '-frames:v', str(int(d * 30)), '-c:v', 'libx264', '-crf', '17',
               '-pix_fmt', 'yuv420p', out]
    else:
        vf = (f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},"
              f"scale=w=iw*{z}:h=ih*{z}:eval=frame,crop={W}:{H},setsar=1,fps=30")
        cmd = [FF, '-v', 'error', '-y', '-ss', f'{a:.3f}', '-t', f'{d:.3f}', '-i', F(src),
               '-vf', vf, '-an', '-c:v', 'libx264', '-crf', '17', '-pix_fmt', 'yuv420p', out]
    subprocess.run(cmd, check=True)
    parts.append(out)

with open(f'{tmp}/list.txt', 'w') as f:
    for p in parts: f.write(f"file '{os.path.basename(p)}'\n")

L = sum(b - a for _, a, b in SEQ) + (END_SHOT[2] - END_SHOT[1])
t_end = L - (END_SHOT[2] - END_SHOT[1])

# --- pegar, poner el cartel fijo, la placa final y la musica
subprocess.run([
    FF, '-v', 'error', '-y',
    '-f', 'concat', '-safe', '0', '-i', f'{tmp}/list.txt',
    '-i', f'{tmp}/cartel.png', '-i', f'{tmp}/end.png',
    '-i', F('music/bed.wav'),
    '-filter_complex',
    f"[0:v][1:v]overlay=0:0:enable='lt(t,{t_end:.2f})'[a];"
    f"[a][2:v]overlay=0:0:enable='gte(t,{t_end:.2f})'[v];"
    f"[3:a]atrim=0:{L:.2f},afade=t=in:st=0:d=1.2,afade=t=out:st={L-1.4:.2f}:d=1.4,volume=-7dB[aud]",
    '-map', '[v]', '-map', '[aud]', '-t', f'{L:.2f}',
    '-c:v', 'libx264', '-crf', '19', '-preset', 'medium', '-pix_fmt', 'yuv420p',
    '-c:a', 'aac', '-b:a', '160k', OUT], check=True)
print(f'OK {OUT} {L:.1f}s, {len(parts)} planos, sin voz')
