# -*- coding: utf-8 -*-
"""Rehace en portugues de Brasil los tres anuncios nuevos de Scented Stones (6, 7, 8).
Misma imagen, misma cama de audio, voz Sulafat y subtitulos portugueses con el estilo
medido sobre cada original.

  6  "If you're thinking…"  58,20 s  karaoke sin caja: MAYUSCULAS blancas, palabra activa amarilla
  7  "If you're between…"   44,29 s  pildora fija magenta, palabras que se van sumando (hasta 2 lineas)
  8  "I used to think…"     36,60 s  pildora fija magenta, UNA palabra grande por vez

Uso: python3 render_pt2.py <6|7|8> [toma]
"""
import os, re, sys, json, subprocess, difflib
import numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont, ImageFilter

FF    = os.path.expanduser('~/bin/ffmpeg')
HERE  = os.path.dirname(os.path.abspath(__file__))
SCR   = os.path.expanduser('~/Desktop/scented-stones-ad/anuncios/_assets')
FONTS = f'{SCR}/fonts'
SRCD  = '/private/tmp/claude-501/-Users-santiagoseara-PrepCourse-Henry/e6a513d2-d9ad-49ff-a046-e53619e5bf9f/scratchpad/pt/src'

ADS = {
 # --- 6: karaoke amarillo, sin caja. Medido: cap 42 px, baseline 1230, "THERE ARE THREE" = 505 px
 6: dict(src=f'{SRCD}/a1.mov', stem='orig6', style='karaoke',
         font=f'{FONTS}/Nunito.ttf', wght=800, fsize=56, upper=True,
         base=1230, lineh=60, maxw=620, maxw2=2, stroke=6,
         hi='#FFFF00', band=(1114, 1300),
         repl=[(['setenta','e','cinco','reais'], '75 reais')],
         out='SS-PT-6-tres-coisas.mp4'),
 # --- 7: pildora fija x164-917 y1384-1511, texto que se acumula, 2 lineas, alineado a la izquierda
 7: dict(src=f'{SRCD}/a2.mp4', stem='orig7', style='pillacc',
         font=f'{FONTS}/Nunito.ttf', wght=800, fsize=50, upper=False,
         pillbox=(164, 1384, 917, 1511), pill='#F30DC7',
         x0=250, base=1436, lineh=62, maxw=580, stroke=5,
         band=(1370, 1525),
         repl=[(['trinta','e','cinco'], '35'), (['cinquenta','e','cinco'], '55')],
         out='SS-PT-7-mulheres-da-sua-cidade.mp4'),
 # --- 8: pildora fija x164-1279 y1242-1631, UNA palabra grande centrada, baseline 1488
 8: dict(src=f'{SRCD}/a3.mp4', stem='orig8', style='pillword',
         font=f'{FONTS}/Montserrat-ExtraBold.ttf', wght=None, fsize=148, upper=False,
         pillbox=(164, 1242, 1279, 1631), pill='#EF3BEC',
         cx=721, base=1488, maxw=1000, stroke=8,
         band=(1230, 1645),
         repl=[(['dois','mil','reais'], '2 mil reais'), (['trinta','a','sessenta'], '30 a 60'),
               (['cento','e','oitenta'], '180'), (['dez','mil','reais'], '10 mil reais')],
         out='SS-PT-8-bancada-da-cozinha.mp4'),
}

def run(c, **k): subprocess.run(c, check=True, **k)
def dur(p):
    r = subprocess.run([FF, '-i', p], capture_output=True, text=True).stderr
    h, m, s = re.search(r'Duration: (\d+):(\d+):([\d.]+)', r).groups()
    return int(h)*3600 + int(m)*60 + float(s)
def rgb(h): h = h.lstrip('#'); return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
def norm(w): return re.sub(r'[^\w]', '', w.lower(), flags=re.U)

def aplicar_repl(vw, repl):
    """colapsa 'setenta e cinco reais' -> '75 reais' conservando los tiempos"""
    out, i = [], 0
    while i < len(vw):
        hecho = False
        for seq, rep in repl:
            n = len(seq)
            if [norm(x[2]) for x in vw[i:i+n]] == seq:
                cola = re.sub(r'^[\w\s]+', '', vw[i+n-1][2])      # se queda la coma/punto final
                out.append((vw[i][0], vw[i+n-1][1], rep + cola))
                i += n; hecho = True; break
        if not hecho:
            out.append(vw[i]); i += 1
    return out

def main(i, toma=None):
    A = ADS[i]; src = A['src']
    tmp = os.path.join(HERE, f'tmp{i}'); os.makedirs(tmp, exist_ok=True)
    cap = cv2.VideoCapture(src); FPS = cap.get(cv2.CAP_PROP_FPS)
    W = int(cap.get(3)); H = int(cap.get(4)); cap.release()
    L = dur(src)
    print(f'[{i}] {W}x{H} {FPS}fps {L:.2f}s  estilo {A["style"]}')

    # ---------- 1) voz ----------
    vo_raw = f'{HERE}/vo/pt{i}{"_"+toma if toma else ""}.wav'
    run([FF, '-v', 'error', '-y', '-i', vo_raw, '-af',
         'silenceremove=start_periods=1:start_threshold=-45dB:stop_periods=-1:'
         'stop_duration=0.32:stop_threshold=-40dB:stop_silence=0.16,aresample=48000',
         '-ac', '1', f'{tmp}/vo_trim.wav'])
    d0 = dur(f'{tmp}/vo_trim.wav')
    LEAD, TAIL = 0.22, 0.25
    sp = d0 / (L - LEAD - TAIL)
    chain, s = [], sp
    while s > 2.0: chain.append(2.0); s /= 2.0
    while s < 0.5: chain.append(0.5); s /= 0.5
    chain.append(s)
    at = ','.join(f'atempo={x:.6f}' for x in chain)
    run([FF, '-v', 'error', '-y', '-i', f'{tmp}/vo_trim.wav', '-af',
         f'{at},adelay={int(LEAD*1000)}|{int(LEAD*1000)},apad,aresample=48000',
         '-ac', '1', '-t', f'{L:.3f}', f'{tmp}/vo.wav'])
    print(f'[{i}] VO {d0:.2f}s -> tempo {sp:.3f}')

    def rms(p):
        r = subprocess.run([FF, '-hide_banner', '-nostats', '-v', 'info', '-i', p,
                            '-af', 'volumedetect', '-f', 'null', '-'], capture_output=True, text=True).stderr
        return float(re.search(r'mean_volume: ([-\d.]+) dB', r).group(1))
    voc = f'{SCR}/stems/htdemucs/{A["stem"]}/vocals.wav'
    g = rms(voc) - rms(f'{tmp}/vo.wav')
    run([FF, '-v', 'error', '-y', '-i', f'{tmp}/vo.wav', '-af',
         f'volume={g:.2f}dB,alimiter=limit=0.95', f'{tmp}/vo_lvl.wav'])
    print(f'[{i}] nivel VO {g:+.2f} dB')

    # ---------- 2) palabras con tiempos ----------
    from faster_whisper import WhisperModel
    model = WhisperModel('medium', device='cpu', compute_type='int8')
    segs, _ = model.transcribe(f'{tmp}/vo_lvl.wav', language='pt', word_timestamps=True, beam_size=5)
    wd = [(w.start, w.end, w.word.strip()) for s_ in segs for w in s_.words]
    sw = open(f'{HERE}/vo/pt{i}.txt').read().split()
    a = [norm(x[2]) for x in wd]; b = [norm(x) for x in sw]
    vw = []
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if op == 'equal':
            vw += [(wd[i1+k][0], wd[i1+k][1], sw[j1+k]) for k in range(i2-i1)]
        elif j2 > j1:
            s0 = wd[i1][0] if i1 < len(wd) else (vw[-1][1] if vw else 0)
            e0 = wd[i2-1][1] if i2 > i1 else s0 + 0.30*(j2-j1)
            st = max(0.05, (e0-s0)/(j2-j1))
            vw += [(s0+k*st, s0+(k+1)*st, sw[j1+k]) for k in range(j2-j1)]
    print(f'[{i}] whisper {len(wd)} palabras / guion {len(sw)} -> alineadas {len(vw)}')
    vw = aplicar_repl(vw, A.get('repl', []))
    if A['upper']: vw = [(s, e, w.upper()) for s, e, w in vw]
    json.dump(vw, open(f'{tmp}/words.json', 'w'), ensure_ascii=False)

    # ---------- 3) tipografia y agrupado ----------
    font = ImageFont.truetype(A['font'], A['fsize'])
    if A['wght']:
        try: font.set_variation_by_axes([A['wght']])
        except Exception as e: print('var:', e)
    probe = ImageDraw.Draw(Image.new('RGB', (10, 10)))
    def wsize(t):
        bb = probe.textbbox((0, 0), t, font=font); return bb[2]-bb[0]
    SPACE = wsize('a a') - 2*wsize('a')

    bloques = []          # cada bloque = lista de lineas; cada linea = lista de (s,e,texto)
    if A['style'] == 'pillword':
        bloques = [[[w]] for w in vw]
    else:
        nlin = A.get('maxw2', 2)
        cur, lin = [], []
        for w in vw:
            tst = ' '.join(x[2] for x in lin + [w])
            if lin and wsize(tst) > A['maxw']:
                cur.append(lin); lin = []
                if len(cur) == nlin:
                    bloques.append(cur); cur = []
            lin.append(w)
            if re.search(r'[.!?]$', w[2]):
                cur.append(lin); lin = []
                bloques.append(cur); cur = []
        if lin: cur.append(lin)
        if cur: bloques.append(cur)
    print(f'[{i}] {len(bloques)} bloques')
    json.dump([[' '.join(w[2] for w in l) for l in b] for b in bloques],
              open(f'{tmp}/bloques.json', 'w'), ensure_ascii=False, indent=0)

    # ---------- 4) un PNG por estado ----------
    BY0, BY1 = A['band']; BH = BY1 - BY0
    blank = Image.new('RGBA', (W, BH), (0, 0, 0, 0))
    STROKE = (0, 0, 0, 255); SW = A['stroke']
    WHITE = (255, 255, 255, 255)
    HI = rgb(A['hi']) + (255,) if A.get('hi') else WHITE

    # fondo fijo de pildora
    pbase = blank.copy()
    if A['style'] in ('pillacc', 'pillword'):
        px0, py0, px1, py1 = A['pillbox']; py0 -= BY0; py1 -= BY0
        sh = Image.new('RGBA', (W, BH), (0, 0, 0, 0)); ds = ImageDraw.Draw(sh)
        ds.rounded_rectangle([px0, py0+10, px1, py1+12], radius=(py1-py0)//3, fill=(90, 0, 110, 120))
        pbase.alpha_composite(sh.filter(ImageFilter.GaussianBlur(12)))
        ImageDraw.Draw(pbase).rounded_rectangle([px0, py0, px1, py1],
                                                radius=(py1-py0)//3, fill=rgb(A['pill'])+(255,))

    states, n = [], 0
    for bi, b in enumerate(bloques):
        plano = [(li, wi, w) for li, l in enumerate(b) for wi, w in enumerate(l)]
        fin = bloques[bi+1][0][0][0] if bi+1 < len(bloques) else min(L, plano[-1][2][1]+0.5)
        fin = min(fin, plano[-1][2][1] + 0.55)
        # posicion de cada palabra
        pos = {}
        for li, l in enumerate(b):
            ws = [wsize(w[2]) for w in l]
            tot = sum(ws) + SPACE*(len(l)-1)
            if A['style'] == 'pillword':   x = A['cx'] - tot/2
            elif A['style'] == 'pillacc':  x = A['x0']
            else:                          x = (W - tot)/2
            y = A['base'] + A.get('lineh', 0)*li - BY0
            if A['style'] == 'karaoke' and len(b) > 1:
                y -= A['lineh']*(len(b)-1)//2          # bloque centrado en la baseline de referencia
            for k, w in enumerate(l):
                pos[(li, k)] = (x, y); x += ws[k] + SPACE
        for k, (li, wi, w) in enumerate(plano):
            t0 = w[0] if k else max(0, w[0]-0.06)
            t1 = plano[k+1][2][0] if k+1 < len(plano) else fin
            if t1 - t0 < 0.02: continue
            im = pbase.copy(); d = ImageDraw.Draw(im)
            visibles = plano if A['style'] == 'karaoke' else plano[:k+1]
            for lj, lw, ww in visibles:
                col = HI if (A['style'] == 'karaoke' and (lj, lw) == (li, wi)) else WHITE
                d.text(pos[(lj, lw)], ww[2], font=font, anchor='ls', fill=col,
                       stroke_width=SW, stroke_fill=STROKE)
            p = f'{tmp}/s{n:04d}.png'; im.save(p); states.append((p, t0, t1)); n += 1
    print(f'[{i}] {len(states)} estados de subtitulo')

    # pista alfa
    empty = f'{tmp}/empty.png'; (pbase if A['style'] != 'karaoke' else blank).save(empty)
    ev, prev = [], 0.0
    for p, t0, t1 in states:
        t0 = max(t0, prev); t1 = max(t1, t0+0.05)
        if t0 >= L: break
        if t0 > prev + 0.02: ev.append((prev, empty))
        ev.append((t0, p)); prev = min(t1, L)
    if prev < L - 0.01: ev.append((prev, empty))
    seq = []
    for k, (ts_, p) in enumerate(ev):
        te = ev[k+1][0] if k+1 < len(ev) else L
        if te - ts_ >= 0.016: seq.append((p, te-ts_))
    with open(f'{tmp}/caps.txt', 'w') as fh:
        for p, dd in seq: fh.write(f"file '{p}'\nduration {dd:.3f}\n")
        fh.write(f"file '{seq[-1][0]}'\n")
    run([FF, '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', f'{tmp}/caps.txt',
         '-vsync', 'cfr', '-r', str(FPS), '-c:v', 'qtrle', '-pix_fmt', 'argb', f'{tmp}/caps.mov'])

    # ---------- 5) tapar los subtitulos ingleses (solo el que no lleva pildora) ----------
    need_clean = A['style'] == 'karaoke'
    if need_clean and not os.path.exists(f'{tmp}/band.mp4'):
        cap = cv2.VideoCapture(src)
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
            yellow = (hsv[..., 0] > 15) & (hsv[..., 0] < 42) & (hsv[..., 1] > 90) & (hsv[..., 2] > 150)
            light = (white | yellow).astype(np.uint8)
            dark = ((b_ < 95) & (g_ < 95) & (r_ < 95)).astype(np.uint8)
            near = cv2.dilate(light, k3, iterations=4)
            m = (light | (dark & near)).astype(np.uint8)
            both = cv2.dilate(light, k3, iterations=5) & cv2.dilate(dark, k3, iterations=5)
            m = (m & cv2.dilate(both, k3, iterations=3)) | yellow.astype(np.uint8)
            m = cv2.dilate(m, k3, iterations=4)
            if m.any(): band = cv2.inpaint(band, m*255, 6, cv2.INPAINT_TELEA)
            pipe.stdin.write(band.tobytes()); nf += 1
        cap.release(); pipe.stdin.close(); pipe.wait()
        print(f'[{i}] banda limpia: {nf} frames')

    # ---------- 6) audio ----------
    mus = f'{SCR}/stems/htdemucs/{A["stem"]}/no_vocals.wav'
    run([FF, '-v', 'error', '-y', '-i', f'{tmp}/vo_lvl.wav', '-i', mus, '-filter_complex',
         '[0:a]aformat=sample_rates=48000:channel_layouts=stereo[v];'
         '[1:a]aformat=sample_rates=48000:channel_layouts=stereo[m];'
         '[v][m]amix=inputs=2:duration=longest:normalize=0,alimiter=limit=0.97[a]',
         '-map', '[a]', '-ac', '2', '-t', f'{L:.3f}', f'{tmp}/mix.wav'])

    # ---------- 7) armado final ----------
    outp = os.path.join(os.path.dirname(HERE), A['out'])
    if need_clean:
        run([FF, '-v', 'error', '-y', '-i', src, '-i', f'{tmp}/band.mp4', '-i', f'{tmp}/caps.mov',
             '-i', f'{tmp}/mix.wav', '-filter_complex',
             f'[0:v][1:v]overlay=0:{BY0}[b];[b][2:v]overlay=0:{BY0}:format=auto[v]',
             '-map', '[v]', '-map', '3:a', '-c:v', 'libx264', '-crf', '18', '-preset', 'medium',
             '-pix_fmt', 'yuv420p', '-r', str(FPS), '-c:a', 'aac', '-b:a', '192k',
             '-movflags', '+faststart', '-shortest', outp])
    else:
        run([FF, '-v', 'error', '-y', '-i', src, '-i', f'{tmp}/caps.mov', '-i', f'{tmp}/mix.wav',
             '-filter_complex', f'[0:v][1:v]overlay=0:{BY0}:format=auto[v]',
             '-map', '[v]', '-map', '2:a', '-c:v', 'libx264', '-crf', '18', '-preset', 'medium',
             '-pix_fmt', 'yuv420p', '-r', str(FPS), '-c:a', 'aac', '-b:a', '192k',
             '-movflags', '+faststart', '-shortest', outp])
    print(f'[{i}] LISTO -> {outp}  ({dur(outp):.2f}s)')

if __name__ == '__main__':
    main(int(sys.argv[1]), sys.argv[2] if len(sys.argv) > 2 else None)
