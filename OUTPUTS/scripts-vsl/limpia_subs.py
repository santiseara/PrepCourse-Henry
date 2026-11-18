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
        if frac < 0.10 and not _anillo_plano(roi[y0r:y1r, x0r:x1r], anillo):
            continue
        caj.append((x, y, w, hh, i))
    return caj, lab


def _anillo_plano(trozo, anillo):
    """Una letra sobre caja de color (azul, violeta, verde) o sobre banda gris
    no tiene contorno negro, pero SI tiene alrededor un color plano.

    Sin esto quedaron enteros los subtitulos en portugues de los anuncios 3, 4
    y 7 ("PODE", "GRATUITA", "NA PROXIMA TERCA FEIRA"): el filtro del contorno
    negro los daba por brillos de la imagen.
    """
    pix = trozo[anillo.astype(bool)]
    if len(pix) < 40:
        return False
    return float(pix.reshape(-1, 3).std(axis=0).mean()) < 11.0


def _estirar_a_la_caja(roi, rect, margen=14):
    """Agranda el rectangulo del renglon hasta cubrir la caja de color entera.

    Repintar solo las letras deja el recuadro azul o la banda gris del
    competidor a la vista; se crece mientras el borde siga siendo del mismo
    color plano que rodea al texto.
    """
    H, W = roi.shape[:2]
    x0, y0, x1, y1 = rect
    borde = []
    for (a, b, c, d) in ((x0, y0 - 6, x1, y0 - 2), (x0, y1 + 2, x1, y1 + 6)):
        a, c = max(0, a), min(W, c)
        b, d = max(0, b), min(H, d)
        if d > b and c > a:
            borde.append(roi[b:d, a:c].reshape(-1, 3))
    if not borde:
        return rect
    ref = np.concatenate(borde).astype(np.float32)
    if ref.std(axis=0).mean() > 16.0:
        return rect          # no hay caja: el fondo es la imagen
    col = ref.mean(axis=0)

    def igual(franja):
        if franja.size == 0:
            return False
        f = franja.reshape(-1, 3).astype(np.float32)
        return float(np.abs(f - col).mean()) < 16.0

    TOPE = 44          # la caja del competidor nunca sobresale mas que esto;
    oy0, oy1, ox0, ox1 = y0, y1, x0, x1   # sin tope, un fondo liso se come la imagen
    while y0 > 1 and oy0 - y0 < TOPE and igual(roi[y0 - 2:y0, x0:x1]):
        y0 -= 2
    while y1 < H - 1 and y1 - oy1 < TOPE and igual(roi[y1:y1 + 2, x0:x1]):
        y1 += 2
    while x0 > 1 and ox0 - x0 < TOPE and igual(roi[y0:y1, x0 - 2:x0]):
        x0 -= 2
    while x1 < W - 1 and x1 - ox1 < TOPE and igual(roi[y0:y1, x1:x1 + 2]):
        x1 += 2
    return (max(0, x0 - 2), max(0, y0 - 2), min(W - 1, x1 + 2), min(H - 1, y1 + 2))


def cajas_de_color(roi):
    """Los recuadros llenos de color (azul, violeta, verde) que el competidor
    pone detras de la palabra resaltada.

    Como el recuadro entero es "color saturado", el detector de letras lo toma
    como UNA letra gigante y el test del anillo lo descarta: asi sobrevivieron
    los "PODE" y "AO" del anuncio 4. Aca se lo busca por lo que es: un
    rectangulo lleno, ancho, con letras blancas adentro.
    """
    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    h, sa, v = cv2.split(hsv)
    # solo color saturado: si se suman los pixeles oscuros, el pelo negro del
    # anuncio 4 se pega al recuadro y la componente deja de ser un rectangulo
    sat = ((sa > 90) & (v > 110)).astype(np.uint8) * 255
    blanco = ((sa < 70) & (v > 195))
    H, W = roi.shape[:2]
    n, lab, st, _ = cv2.connectedComponentsWithStats(sat, 8)
    out = []
    for i in range(1, n):
        x, y, w, hh, area = st[i]
        if not (W * 0.05 <= w <= W * 0.95 and 22 <= hh <= 130):
            continue
        if area / float(w * hh) < 0.47 or w / float(hh) < 1.2:
            continue
        centro = (x + w / 2.0) / W
        if not (0.15 <= centro <= 0.85):
            continue
        dentro = blanco[y:y + hh, x:x + w]
        if dentro.mean() < 0.045:      # sin letras blancas adentro no es subtitulo
            continue
        out.append((x, y, x + w, y + hh))
    return out


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
        # un renglon corto igual hay que borrarlo: el "NA" suelto del anuncio 3
        # sobrevivio al pedir 12 % del ancho
        if x1 - x0 < W * 0.045:
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
        rects = renglones(caj, W) + cajas_de_color(roi)
        if rects:
            hR = roi.shape[0]
            m = np.zeros((hR, W), np.uint8)
            for r in rects:
                (x0, yy0, x1, yy1) = _estirar_a_la_caja(roi, r)
                cv2.rectangle(m, (max(0, x0 - 12), max(0, yy0 - 10)),
                              (min(W - 1, x1 + 12), min(hR - 1, yy1 + 10)), 255, -1)
            # el repintado se hace a 1/3 de resolucion: el parche va desenfocado
            # igual, asi que no se pierde nada y es nueve veces mas rapido
            ch, cw = roi.shape[0] // 2, W // 2
            rp = cv2.resize(roi, (cw, ch), interpolation=cv2.INTER_AREA)
            mp = cv2.resize(m, (cw, ch), interpolation=cv2.INTER_NEAREST)
            pint = cv2.resize(cv2.inpaint(rp, mp, 4, cv2.INPAINT_TELEA),
                              (W, roi.shape[0]), interpolation=cv2.INTER_LINEAR)
            suave = cv2.GaussianBlur(pint, (0, 0), 3)
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
