"""Saca subtítulos quemados (texto blanco/amarillo con borde negro) por inpainting.
Uso: python3 rmsubs.py in.mp4 out.mp4 [y0=0.70] [y1=0.84]"""
import sys, cv2, numpy as np, subprocess, os
src, dst = sys.argv[1], sys.argv[2]
y0f = float(sys.argv[3]) if len(sys.argv) > 3 else 0.70
y1f = float(sys.argv[4]) if len(sys.argv) > 4 else 0.84
cap = cv2.VideoCapture(src)
fps = cap.get(cv2.CAP_PROP_FPS); W = int(cap.get(3)); H = int(cap.get(4))
y0, y1 = int(H*y0f), int(H*y1f)
tmp = dst + '.noaudio.mp4'
vw = cv2.VideoWriter(tmp, cv2.VideoWriter_fourcc(*'mp4v'), fps, (W, H))
k3 = np.ones((3,3), np.uint8)
while True:
    ok, f = cap.read()
    if not ok: break
    band = f[y0:y1].astype(np.int16)
    b, g, r = band[...,0], band[...,1], band[...,2]
    white = (b > 200) & (g > 200) & (r > 200) & (np.abs(r-b) < 40)
    yellow = (r > 190) & (g > 170) & (b < 110)
    light = (white | yellow).astype(np.uint8)
    dark = ((b < 60) & (g < 60) & (r < 60)).astype(np.uint8)
    near = cv2.dilate(light, k3, iterations=3)
    m = (light | (dark & near))
    # solo grupos de texto: tienen claro y oscuro mezclados en la misma zona
    both = cv2.dilate(light, k3, iterations=4) & cv2.dilate(dark, k3, iterations=4)
    m = m & cv2.dilate(both, k3, iterations=2)
    m = cv2.dilate(m, k3, iterations=2)
    full = np.zeros((H, W), np.uint8); full[y0:y1] = m * 255
    if full.any():
        f = cv2.inpaint(f, full, 4, cv2.INPAINT_TELEA)
    vw.write(f)
vw.release()
subprocess.run([os.path.expanduser('~/bin/ffmpeg'), '-loglevel', 'error', '-y', '-i', tmp, '-i', src,
    '-map', '0:v', '-map', '1:a?', '-c:v', 'libx264', '-crf', '16', '-pix_fmt', 'yuv420p', '-c:a', 'copy', dst], check=True)
os.remove(tmp)
