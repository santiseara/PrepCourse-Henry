# Rehace la banda limpia del anuncio 4. La del pase ruso dejaba un fantasma rosa de la caja
# magenta inglesa: el TELEA se comia el nucleo saturado pero no el antialias ni la sombra.
# Respecto del script original cambian dos cosas y nada mas:
#   1) la mascara del magenta es mas laxa (S>35, hue 135-170) para agarrar el antialias
#   2) despues del inpaint va un segundo inpaint y un blur difuminado SOLO sobre la mascara
# El filtro "blanco Y borde oscuro juntos" se mantiene tal cual: sin el, la tela blanca
# del video entra en la mascara y se borronea media banda.
import os, subprocess, numpy as np, cv2
FF  = os.path.expanduser('~/bin/ffmpeg')
SRC = os.path.expanduser('~/Downloads/Ok I need.mp4')
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tmp4', 'band.mp4')
BY0, BY1 = 1560, 1810
cap = cv2.VideoCapture(SRC); FPS = cap.get(cv2.CAP_PROP_FPS); W = int(cap.get(3))
BH = BY1 - BY0
pipe = subprocess.Popen([FF,'-v','error','-y','-f','rawvideo','-pix_fmt','bgr24','-s',f'{W}x{BH}',
    '-r',str(FPS),'-i','-','-c:v','libx264','-crf','10','-preset','veryfast','-pix_fmt','yuv420p',OUT],
    stdin=subprocess.PIPE)
k3 = np.ones((3,3), np.uint8); nf = 0
while True:
    ok, f = cap.read()
    if not ok: break
    band = f[BY0:BY1].copy()
    hsv = cv2.cvtColor(band, cv2.COLOR_BGR2HSV)
    b, g, r = band[...,0].astype(int), band[...,1].astype(int), band[...,2].astype(int)
    H, S, V = hsv[...,0].astype(int), hsv[...,1].astype(int), hsv[...,2].astype(int)
    white = (b>205)&(g>205)&(r>205)
    mag   = (H>135)&(H<170)&(S>35)&(V>70)        # mas laxo que el original (era S>110)
    light = (white|mag).astype(np.uint8)
    dark  = ((b<85)&(g<85)&(r<85)).astype(np.uint8)
    near  = cv2.dilate(light,k3,iterations=4)
    m = (light | (dark & near)).astype(np.uint8)
    both = cv2.dilate(light,k3,iterations=5) & cv2.dilate(dark,k3,iterations=5)
    m = (m & cv2.dilate(both,k3,iterations=3)) | mag.astype(np.uint8)   # el filtro que faltaba
    m = cv2.dilate(m,k3,iterations=5)
    if m.any():
        mm = m*255
        band = cv2.inpaint(band, mm, 7, cv2.INPAINT_TELEA)
        band = cv2.inpaint(band, cv2.dilate(mm,k3,iterations=1), 4, cv2.INPAINT_TELEA)
        suave = cv2.GaussianBlur(band,(0,0),6)
        alfa  = cv2.GaussianBlur(m.astype(np.float32),(0,0),4)[...,None]
        alfa  = np.clip(alfa*1.3, 0, 1)
        band = (band*(1-alfa) + suave*alfa).astype(np.uint8)
    pipe.stdin.write(band.tobytes()); nf += 1
cap.release(); pipe.stdin.close(); pipe.wait()
print(f'banda 4 rehecha: {nf} cuadros -> {OUT}')
