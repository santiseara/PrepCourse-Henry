#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Borra los subtitulos quemados en portugues de un clip del original.

Detecta las letras por color (amarillo o blanco) dentro de la franja donde el
anuncio pone los subtitulos, las agrupa en renglones y solo repinta el rectangulo
de cada renglon. Asi no se toca el resto de la imagen.

Uso: python3 limpia_subs.py entrada.mp4 salida.mp4 amarillo|blanco y0 y1
"""
import sys, os, subprocess, numpy as np, cv2

FF = os.path.expanduser('~/bin/ffmpeg')


def letras(roi, color):
    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    am = ((h > 18) & (h < 38) & (s > 120) & (v > 170))
    bl = ((s < 60) & (v > 210))
    if color == 'amarillo':
        m = am
    elif color == 'blanco':
        m = bl
    elif color == 'todos':
        # algunos anuncios resaltan una palabra en rojo, verde o violeta:
        # cualquier color saturado y brillante cuenta como letra
        m = bl | ((s > 110) & (v > 140))
    else:                      # 'ambos': el anuncio mezcla linea blanca y linea amarilla
        m = am | bl
    m = m.astype(np.uint8) * 255
    oscuro = (v < 125).astype(np.uint8)
    n, lab, st, cen = cv2.connectedComponentsWithStats(m, 8)
    caj = []
    for i in range(1, n):
        x, y, w, hh, area = st[i]
        if not (12 <= hh <= 110 and 5 <= w <= 460 and area > 45 and area / float(w * hh) > 0.14):
            continue
        # una letra de subtitulo SIEMPRE tiene contorno negro alrededor:
        # si el anillo que la rodea no es oscuro, es un brillo de la imagen.
        # el recorte va con margen, si no el anillo queda cortado por la caja
        P = 7
        y0r, y1r = max(0, y - P), min(m.shape[0], y + hh + P)
        x0r, x1r = max(0, x - P), min(m.shape[1], x + w + P)
        comp = (lab[y0r:y1r, x0r:x1r] == i).astype(np.uint8)
        anillo = cv2.dilate(comp, np.ones((11, 11), np.uint8)) - comp
        sub_osc = oscuro[y0r:y1r, x0r:x1r]
        if anillo.sum() == 0:
            continue
        frac = float((anillo & sub_osc).sum()) / float(anillo.sum())
        if frac < 0.10:
            continue
        caj.append((x, y, w, hh, i))
    return caj, lab


def renglones(caj, W):
    """Agrupa las cajas por altura de linea y devuelve los rectangulos de texto."""
    if not caj:
        return []
    caj = sorted(caj, key=lambda c: c[1] + c[3] / 2)
    lineas, cur = [], [caj[0]]
    for c in caj[1:]:
        cy = c[1] + c[3] / 2
        ref = cur[-1][1] + cur[-1][3] / 2
        if abs(cy - ref) < max(26, cur[-1][3] * 0.65):
            cur.append(c)
        else:
            lineas.append(cur); cur = [c]
    lineas.append(cur)
    rects = []
    for l in lineas:
        if len(l) < 2:
            continue
        x0 = min(c[0] for c in l); x1 = max(c[0] + c[2] for c in l)
        y0 = min(c[1] for c in l); y1 = max(c[1] + c[3] for c in l)
        if x1 - x0 < W * 0.12:
            continue
        # un renglon de subtitulo esta centrado y tiene letras de altura pareja;
        # una mancha de pelo o de piel no cumple ni una cosa ni la otra
        centro = (x0 + x1) / 2.0 / W
        if not (0.20 <= centro <= 0.80):
            continue
        alturas = [c[3] for c in l]
        med = sum(alturas) / len(alturas)
        disp = (sum((h - med) ** 2 for h in alturas) / len(alturas)) ** 0.5
        if med > 0 and disp / med > 0.55:
            continue
        rects.append((x0, y0, x1, y1))
    return rects


def limpiar(entrada, salida, color, y0f, y1f):
    cap = cv2.VideoCapture(entrada)
    fps = cap.get(cv2.CAP_PROP_FPS) or 30
    W = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)); H = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    a, b = int(H * y0f), int(H * y1f)
    tmp = salida + '.tmp.mp4'
    p = subprocess.Popen([FF, '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'bgr24',
                          '-s', f'{W}x{H}', '-r', f'{fps}', '-i', '-', '-an',
                          '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '17',
                          '-pix_fmt', 'yuv420p', tmp], stdin=subprocess.PIPE)
    n = 0
    while True:
        ok, f = cap.read()
        if not ok:
            break
        roi = f[a:b]
        caj, lab = letras(roi, color)
        rects = renglones(caj, W)
        if rects:
            hR = roi.shape[0]
            m = np.zeros((hR, W), np.uint8)
            for (x0, yy0, x1, yy1) in rects:
                cv2.rectangle(m, (max(0, x0 - 12), max(0, yy0 - 10)),
                              (min(W - 1, x1 + 12), min(hR - 1, yy1 + 10)), 255, -1)
            # el repintado se hace a 1/3 de resolucion: el parche va desenfocado
            # igual, asi que no se pierde nada y es nueve veces mas rapido
            ch, cw = roi.shape[0] // 3, W // 3
            rp = cv2.resize(roi, (cw, ch), interpolation=cv2.INTER_AREA)
            mp = cv2.resize(m, (cw, ch), interpolation=cv2.INTER_NEAREST)
            pint = cv2.resize(cv2.inpaint(rp, mp, 4, cv2.INPAINT_TELEA),
                              (W, roi.shape[0]), interpolation=cv2.INTER_LINEAR)
            suave = cv2.GaussianBlur(pint, (0, 0), 5)
            # la alfa tiene que valer 1 ADENTRO del rectangulo: si no, el texto
            # original se vuelve a mezclar y queda el fantasma
            m2 = cv2.dilate(m, np.ones((19, 19), np.uint8))
            alfa = cv2.GaussianBlur(m2, (0, 0), 7).astype(np.float32)[..., None] / 255.0
            f[a:b] = (roi * (1 - alfa) + suave * alfa).astype(np.uint8)
        p.stdin.write(f.tobytes()); n += 1
    cap.release(); p.stdin.close(); p.wait()
    os.replace(tmp, salida)
    return n


if __name__ == '__main__':
    e, s, col = sys.argv[1], sys.argv[2], sys.argv[3]
    y0, y1 = float(sys.argv[4]), float(sys.argv[5])
    print(limpiar(e, s, col, y0, y1), 'cuadros ->', s)
