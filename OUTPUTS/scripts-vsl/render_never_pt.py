# -*- coding: utf-8 -*-
"""Rehace el anuncio "I never" de Scented Stones en portugues de Brasil.
Misma imagen, misma cama de audio, voz Sulafat y subtitulos portugueses
con el mismo estilo del original (Courier New Bold 47, blanco con contorno
negro, palabra activa en amarillo, bloques de hasta 2 lineas de 24 caracteres).
Uso: python3 render_never_pt.py [toma]   (toma = a|b|c|d, por defecto la de vo/pt5.wav)
"""
import os, re, sys, json, subprocess, difflib
import numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont

FF    = os.path.expanduser('~/bin/ffmpeg')
HERE  = os.path.dirname(os.path.abspath(__file__))
SCR   = os.path.expanduser('~/Desktop/scented-stones-ad/anuncios/_assets')
DL    = os.path.expanduser('~/Downloads')

SRC   = f'{DL}/i never.mp4'
STEM  = 'orig5'
OUT   = 'SS-PT-5-nunca-quis.mp4'
FONTP = '/System/Library/Fonts/Supplemental/Courier New Bold.ttf'
FSIZE = 47
CHARW = 28.0          # ancho de caracter de la mono, medido en el original
MAXCH = 24            # caracteres por linea en el original
LINEH = 56            # interlineado medido
BASE1 = 1457          # baseline cuando el bloque tiene una sola linea
BAND  = (1368, 1512)  # franja donde viven los subtitulos ingleses
WHITE = (255, 255, 255, 255)
YELLOW= (235, 212, 20, 255)
STROKE= (0, 0, 0, 235)
SW    = 3

# numeros: la voz los dice con todas las letras, el subtitulo los muestra en cifra
REPL = [(['dezoito'], '18'), (['vinte', 'e', 'sete'], '27')]


def run(c, **k): subprocess.run(c, check=True, **k)


def dur(p):
    r = subprocess.run([FF, '-i', p], capture_output=True, text=True).stderr
    h, m, s = re.search(r'Duration: (\d+):(\d+):([\d.]+)', r).groups()
    return int(h) * 3600 + int(m) * 60 + float(s)


def rms(p):
    r = subprocess.run([FF, '-hide_banner', '-nostats', '-v', 'info', '-i', p,
                        '-af', 'volumedetect', '-f', 'null', '-'],
                       capture_output=True, text=True).stderr
    return float(re.search(r'mean_volume: ([-\d.]+) dB', r).group(1))


def aplicar_repl(vw):
    """colapsa 'vinte e sete' -> '27' conservando los tiempos"""
    out, i = [], 0
    norm = lambda w: re.sub(r'[^\w]', '', w.lower(), flags=re.U)
    while i < len(vw):
        hecho = False
        for seq, rep in REPL:
            n = len(seq)
            if [norm(x[2]) for x in vw[i:i + n]] == seq:
                cola = re.sub(r'^\w+', '', vw[i + n - 1][2])   # se queda la coma final
                out.append((vw[i][0], vw[i + n - 1][1], rep + cola))
                i += n; hecho = True; break
        if not hecho:
            out.append(vw[i]); i += 1
    return out


def bloques(vw):
    """agrupa las palabras en bloques de hasta 2 lineas de MAXCH caracteres"""
    bl, cur, lin = [], [], []
    def ancho(l): return len(' '.join(w[2] for w in l))
    for w in vw:
        if lin and ancho(lin + [w]) > MAXCH:
            cur.append(lin); lin = []
            if len(cur) == 2:
                bl.append(cur); cur = []
        lin.append(w)
        if re.search(r'[.!?]$', w[2]):
            cur.append(lin); lin = []
            bl.append(cur); cur = []
    if lin: cur.append(lin)
    if cur: bl.append(cur)
    return bl


def main(toma=None):
    cap = cv2.VideoCapture(SRC); FPS = cap.get(cv2.CAP_PROP_FPS)
    W = int(cap.get(3)); H = int(cap.get(4)); cap.release()
    L = dur(SRC)
    tmp = f'{HERE}/tmp5'; os.makedirs(tmp, exist_ok=True)
    print(f'[5] {W}x{H} {FPS}fps {L:.2f}s')

    vo_raw = f'{HERE}/vo/pt5{"_" + toma if toma else ""}.wav'

    # ---------- 1) voz: sin silencios y calzada al largo del original ----------
    run([FF, '-v', 'error', '-y', '-i', vo_raw, '-af',
         'silenceremove=start_periods=1:start_threshold=-45dB:stop_periods=-1:'
         'stop_duration=0.32:stop_threshold=-40dB:stop_silence=0.16,aresample=48000',
         '-ac', '1', f'{tmp}/vo_trim.wav'])
    d0 = dur(f'{tmp}/vo_trim.wav')
    LEAD, TAIL = 0.18, 0.18
    sp = d0 / (L - LEAD - TAIL)
    chain = []; s = sp
    while s > 2.0: chain.append(2.0); s /= 2.0
    while s < 0.5: chain.append(0.5); s /= 0.5
    chain.append(s)
    at = ','.join(f'atempo={x:.6f}' for x in chain)
    run([FF, '-v', 'error', '-y', '-i', f'{tmp}/vo_trim.wav', '-af',
         f'{at},adelay={int(LEAD*1000)}|{int(LEAD*1000)},apad,aresample=48000',
         '-ac', '1', '-t', f'{L:.3f}', f'{tmp}/vo.wav'])
    print(f'[5] VO {d0:.2f}s -> tempo {sp:.3f} -> {dur(f"{tmp}/vo.wav"):.2f}s')

    voc = f'{SCR}/stems/htdemucs/{STEM}/vocals.wav'
    g = rms(voc) - rms(f'{tmp}/vo.wav')
    run([FF, '-v', 'error', '-y', '-i', f'{tmp}/vo.wav', '-af',
         f'volume={g:.2f}dB,alimiter=limit=0.95', f'{tmp}/vo_lvl.wav'])
    print(f'[5] nivel VO {g:+.2f} dB')

    # ---------- 2) palabras con tiempos ----------
    from faster_whisper import WhisperModel
    model = WhisperModel('medium', device='cpu', compute_type='int8')
    segs, _ = model.transcribe(f'{tmp}/vo_lvl.wav', language='pt',
                               word_timestamps=True, beam_size=5)
    wd = [(w.start, w.end, w.word.strip()) for s_ in segs for w in s_.words]
    sw = open(f'{HERE}/vo/pt5.txt').read().split()
    norm = lambda w: re.sub(r'[^\w]', '', w.lower(), flags=re.U)
    a = [norm(x[2]) for x in wd]; b = [norm(x) for x in sw]
    vw = []
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if op == 'equal':
            vw += [(wd[i1 + k][0], wd[i1 + k][1], sw[j1 + k]) for k in range(i2 - i1)]
        elif j2 > j1:
            s0 = wd[i1][0] if i1 < len(wd) else (vw[-1][1] if vw else 0)
            e0 = wd[i2 - 1][1] if i2 > i1 else s0 + 0.30 * (j2 - j1)
            st = max(0.05, (e0 - s0) / (j2 - j1))
            vw += [(s0 + k * st, s0 + (k + 1) * st, sw[j1 + k]) for k in range(j2 - j1)]
    print(f'[5] whisper {len(wd)} palabras / guion {len(sw)} -> alineadas {len(vw)}')
    vw = aplicar_repl(vw)
    json.dump(vw, open(f'{tmp}/words.json', 'w'), ensure_ascii=False)

    # ---------- 3) bloques de 2 lineas ----------
    bl = bloques(vw)
    json.dump([[' '.join(w[2] for w in l) for l in b_] for b_ in bl],
              open(f'{tmp}/bloques.json', 'w'), ensure_ascii=False, indent=0)
    print(f'[5] {len(bl)} bloques')

    # ---------- 4) un PNG por estado ----------
    font = ImageFont.truetype(FONTP, FSIZE)
    BY0, BY1 = BAND; BH = BY1 - BY0
    blank = Image.new('RGBA', (W, BH), (0, 0, 0, 0))
    states, n = [], 0
    for bi, b_ in enumerate(bl):
        nl = len(b_)
        ancho = max(len(' '.join(w[2] for w in l)) for l in b_) * CHARW
        x0 = (W - ancho) / 2
        y0 = BASE1 - (LINEH // 2) * (nl - 1) - BY0
        plano = [(li, wi, w) for li, l in enumerate(b_) for wi, w in enumerate(l)]
        fin_bloque = bl[bi + 1][0][0][0] if bi + 1 < len(bl) else min(L, plano[-1][2][1] + 0.5)
        fin_bloque = min(fin_bloque, plano[-1][2][1] + 0.55)
        for k, (li, wi, w) in enumerate(plano):
            t0 = w[0] if k else max(0, w[0] - 0.06)
            t1 = plano[k + 1][2][0] if k + 1 < len(plano) else fin_bloque
            if t1 - t0 < 0.02: continue
            im = blank.copy(); d = ImageDraw.Draw(im)
            for lj, lw, ww in plano[:k + 1]:
                x = x0 + len(' '.join(y[2] for y in b_[lj][:lw])) * CHARW
                if lw: x += CHARW                     # el espacio que separa
                y = y0 + LINEH * lj
                d.text((x, y), ww[2], font=font, anchor='ls',
                       fill=YELLOW if (lj, lw) == (li, wi) else WHITE,
                       stroke_width=SW, stroke_fill=STROKE)
            p = f'{tmp}/s{n:04d}.png'; im.save(p); states.append((p, t0, t1)); n += 1
    print(f'[5] {len(states)} estados de subtitulo')

    # pista alfa
    empty = f'{tmp}/empty.png'; blank.save(empty)
    ev, prev = [], 0.0
    for p, t0, t1 in states:
        t0 = max(t0, prev); t1 = max(t1, t0 + 0.05)
        if t0 >= L: break
        if t0 > prev + 0.02: ev.append((prev, empty))
        ev.append((t0, p)); prev = min(t1, L)
    if prev < L - 0.01: ev.append((prev, empty))
    seq = []
    for k, (ts_, p) in enumerate(ev):
        te = ev[k + 1][0] if k + 1 < len(ev) else L
        if te - ts_ >= 0.016: seq.append((p, te - ts_))
    with open(f'{tmp}/caps.txt', 'w') as fh:
        for p, dd in seq: fh.write(f"file '{p}'\nduration {dd:.3f}\n")
        fh.write(f"file '{seq[-1][0]}'\n")
    run([FF, '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', f'{tmp}/caps.txt',
         '-vsync', 'cfr', '-r', str(FPS), '-c:v', 'qtrle', '-pix_fmt', 'argb', f'{tmp}/caps.mov'])

    # ---------- 5) tapar los subtitulos ingleses ----------
    if not os.path.exists(f'{tmp}/band.mp4'):
        cap = cv2.VideoCapture(SRC)
        pipe = subprocess.Popen([FF, '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgr24',
                                 '-s', f'{W}x{BH}', '-r', str(FPS), '-i', '-', '-c:v', 'libx264',
                                 '-crf', '12', '-preset', 'veryfast', '-pix_fmt', 'yuv420p',
                                 f'{tmp}/band.mp4'], stdin=subprocess.PIPE)
        k3 = np.ones((3, 3), np.uint8); nf = 0
        while True:
            ok, f = cap.read()
            if not ok: break
            band = f[BY0:BY1].copy()
            hsv = cv2.cvtColor(band, cv2.COLOR_BGR2HSV)
            b_, g_, r_ = band[..., 0].astype(int), band[..., 1].astype(int), band[..., 2].astype(int)
            white = (b_ > 205) & (g_ > 205) & (r_ > 205)
            yellow = (hsv[..., 0] > 15) & (hsv[..., 0] < 40) & (hsv[..., 1] > 90) & (hsv[..., 2] > 140)
            light = (white | yellow).astype(np.uint8)
            dark = ((b_ < 95) & (g_ < 95) & (r_ < 95)).astype(np.uint8)
            near = cv2.dilate(light, k3, iterations=4)
            m = (light | (dark & near)).astype(np.uint8)
            both = cv2.dilate(light, k3, iterations=5) & cv2.dilate(dark, k3, iterations=5)
            m = (m & cv2.dilate(both, k3, iterations=3)) | yellow.astype(np.uint8)
            m = cv2.dilate(m, k3, iterations=4)
            if m.any(): band = cv2.inpaint(band, m * 255, 6, cv2.INPAINT_TELEA)
            pipe.stdin.write(band.tobytes()); nf += 1
        cap.release(); pipe.stdin.close(); pipe.wait()
        print(f'[5] banda limpia: {nf} frames')

    # ---------- 6) audio: cama original + voz nueva ----------
    mus = f'{SCR}/stems/htdemucs/{STEM}/no_vocals.wav'
    run([FF, '-v', 'error', '-y', '-i', f'{tmp}/vo_lvl.wav', '-i', mus, '-filter_complex',
         '[0:a]aformat=sample_rates=48000:channel_layouts=stereo[v];'
         '[1:a]aformat=sample_rates=48000:channel_layouts=stereo[m];'
         '[v][m]amix=inputs=2:duration=longest:normalize=0,alimiter=limit=0.97[a]',
         '-map', '[a]', '-ac', '2', '-t', f'{L:.3f}', f'{tmp}/mix.wav'])

    # ---------- 7) armado final ----------
    outp = os.path.join(os.path.dirname(HERE), OUT)
    run([FF, '-v', 'error', '-y', '-i', SRC, '-i', f'{tmp}/band.mp4', '-i', f'{tmp}/caps.mov',
         '-i', f'{tmp}/mix.wav', '-filter_complex',
         f'[0:v][1:v]overlay=0:{BY0}[b];[b][2:v]overlay=0:{BY0}:format=auto[v]',
         '-map', '[v]', '-map', '3:a', '-c:v', 'libx264', '-crf', '18', '-preset', 'medium',
         '-pix_fmt', 'yuv420p', '-r', str(FPS), '-c:a', 'aac', '-b:a', '192k',
         '-movflags', '+faststart', '-shortest', outp])
    print(f'[5] LISTO -> {outp}  ({dur(outp):.2f}s)')


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else None)
