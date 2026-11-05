# -*- coding: utf-8 -*-
"""Habilidades Perdidas: toma el ad original en ingles, borra los subtitulos quemados
y los stickers, y lo devuelve con voz en off y subtitulos en espanol neutro.
Uso: python3 render_hp.py A1 [A2 ...]"""
import os, re, sys, json, subprocess, difflib
import numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont, ImageFilter

FF    = os.path.expanduser('~/bin/ffmpeg')
W     = os.path.expanduser('~/Desktop/habilidades-perdidas/trabajo')
OUT   = os.path.expanduser('~/Desktop/habilidades-perdidas/anuncios')
FONTS = '/private/tmp/claude-501/-Users-santiagoseara-PrepCourse-Henry/20caf5cd-289e-40a4-8faa-e4ef9fa33307/scratchpad/fonts'
SUBF  = f'{FONTS}/Montserrat-ExtraBold.ttf'
STKF  = f'{FONTS}/Nunito.ttf'

# banda  = (y0,y1) donde viven los subtitulos quemados
# sticker= lista de (x0,y0,x1,y1, t0,t1, texto_es, size)  -> se tapa y se reescribe
# placas = lista de (x0,y0,x1,y1, t0,t1, texto_es, size, estilo)  estilo: 'light'|'dark'
ADS = {
 'A1': dict(banda=(324,410), fsize=23, cy=355, maxw=326, sticker=[],
            placas=[(0,382,360,437, 0.0, 4.7, '¡SE VIENE UNA OFERTA!', 26, 'dark', True)]),
 'A2': dict(banda=(406,470), fsize=23, cy=437, maxw=330, sticker=[], placas=[]),
 'A3': dict(banda=(288,360), fsize=22, cy=325, maxw=330,
            sticker=[(56,130,356,218, 0.0, 33.8, 'Esto no te lo cuentan…', 19)],
            placas=[(70,70,299,111, 38.2, 46.0, '76% DE DESCUENTO', 18, 'light', False),
                    (95,150,279,193, 33.7, 46.0, '+3 REGALOS GRATIS', 18, 'dark', False)]),
 'A4': dict(banda=(368,436), fsize=23, cy=401, maxw=330,
            sticker=[(12,92,356,230, 0.0, 5.5, '¿Cómo consigues agua potable de la nada?', 20)],
            placas=[]),
 'A5': dict(banda=(346,408), fsize=23, cy=376, maxw=330,
            sticker=[(28,238,338,328, 0.0, 3.0, '¿Qué es el embutido eterno?', 20)],
            placas=[]),
 'A6': dict(banda=(386,446), fsize=23, cy=416, maxw=330,
            sticker=[(18,124,344,190, 0.0, 3.4, '¿La comida eterna?', 20)],
            placas=[]),
}

def run(c): subprocess.run(c, check=True)
def dur(p):
    r = subprocess.run([FF,'-i',p], capture_output=True, text=True).stderr
    h,m,s = re.search(r'Duration: (\d+):(\d+):([\d.]+)', r).groups()
    return int(h)*3600+int(m)*60+float(s)
def rms(p):
    r = subprocess.run([FF,'-hide_banner','-nostats','-v','info','-i',p,'-af','volumedetect','-f','null','-'],
                       capture_output=True, text=True).stderr
    m = re.search(r'mean_volume: ([-\d.]+) dB', r)
    return float(m.group(1)) if m else -25.0

# ---------------------------------------------------------------- mascara de texto
def mascara_texto(band):
    """Pixeles de subtitulo quemado dentro de la banda: glifo claro con borde oscuro."""
    b,g,r = band[...,0].astype(int), band[...,1].astype(int), band[...,2].astype(int)
    bright = ((b>222)&(g>222)&(r>222)) | ((r>188)&(g>160)&(b<120))
    dark   = (b<90)&(g<90)&(r<90)
    bright_u = bright.astype(np.uint8); dark_u = dark.astype(np.uint8)
    k = np.ones((3,3), np.uint8)
    cerca = cv2.dilate(dark_u, k, iterations=2) > 0
    cand = (bright & cerca).astype(np.uint8)
    if not cand.any(): return None
    n, lab, st, _ = cv2.connectedComponentsWithStats(cand, 8)
    keep = np.zeros(n, bool)
    h_band = band.shape[0]
    for i in range(1, n):
        x,y,w,h,a = st[i]
        if 4 <= h <= min(40, h_band-2) and 2 <= w <= 110 and a >= 10:
            keep[i] = True
    m = keep[lab].astype(np.uint8)
    if not m.any(): return None
    m = cv2.dilate(m, k, iterations=3)
    # el borde negro del glifo tambien se va
    m = (m | (dark_u & (cv2.dilate(m, k, iterations=2) > 0))).astype(np.uint8)
    m = cv2.dilate(m, k, iterations=2)
    return m*255

def barra_solida(band):
    """Filas de caja oscura opaca con texto claro (el 'Big offer incoming!')."""
    b,g,r = band[...,0].astype(int), band[...,1].astype(int), band[...,2].astype(int)
    dark = ((b<70)&(g<70)&(r<70))
    fil = dark.mean(1) > 0.55
    if not fil.any(): return None
    m = np.zeros(band.shape[:2], np.uint8)
    m[fil] = 1
    m = cv2.dilate(m, np.ones((5,5),np.uint8), iterations=2)
    return m*255

def limpiar_banda(src, A, tmp, FPS, Wd, H):
    BY0, BY1 = A['banda']; BH = BY1-BY0
    salida = f'{tmp}/band.mp4'
    if os.path.exists(salida): return salida
    cap = cv2.VideoCapture(src)
    pipe = subprocess.Popen([FF,'-v','error','-y','-f','rawvideo','-pix_fmt','bgr24','-s',f'{Wd}x{BH}',
        '-r',str(FPS),'-i','-','-c:v','libx264','-crf','10','-preset','veryfast','-pix_fmt','yuv420p', salida],
        stdin=subprocess.PIPE)
    nf = 0
    while True:
        ok, f = cap.read()
        if not ok: break
        band = f[BY0:BY1].copy()
        m = mascara_texto(band)
        bs = barra_solida(band)
        if bs is not None: m = bs if m is None else np.maximum(m, bs)
        if m is not None and m.any():
            band = cv2.inpaint(band, m, 6, cv2.INPAINT_TELEA)
            band = cv2.inpaint(band, cv2.dilate(m, np.ones((3,3),np.uint8), 1), 4, cv2.INPAINT_TELEA)
            # blur difuminado sobre lo borrado: mata cualquier resto legible del texto ingles
            ancho = cv2.dilate(m, np.ones((5,5), np.uint8), iterations=3)
            suave = cv2.GaussianBlur(band, (0,0), 7)
            alfa = cv2.GaussianBlur(ancho.astype(np.float32)/255.0, (0,0), 5)[..., None]
            alfa = np.clip(alfa*1.25, 0, 1)
            band = (band*(1-alfa) + suave*alfa).astype(np.uint8)
        pipe.stdin.write(band.tobytes()); nf += 1
    cap.release(); pipe.stdin.close(); pipe.wait()
    print(f'   banda limpia: {nf} cuadros')
    return salida

# ---------------------------------------------------------------- capa de texto
def ajustar(draw, texto, font, maxw):
    pal = texto.split(); lineas=[]; cur=''
    for p in pal:
        t = (cur+' '+p).strip()
        if cur and draw.textbbox((0,0), t, font=font)[2] > maxw: lineas.append(cur); cur=p
        else: cur=t
    if cur: lineas.append(cur)
    return lineas

def capa_sticker(Wd, H, A):
    """Una capa RGBA por sticker/placa. La caja dibujada cubre SIEMPRE el rectangulo
    original completo, asi no queda nada del cartel en ingles asomando."""
    capas = []
    items = [(it, 'light', False) for it in A['sticker']]
    items += [((it[0],it[1],it[2],it[3],it[4],it[5],it[6],it[7]), it[8], it[9]) for it in A['placas']]
    for item, est, bold in items:
        x0,y0,x1,y1,t0,t1,txt,fs = item
        font = ImageFont.truetype(SUBF if bold else STKF, fs)
        if not bold:
            try: font.set_variation_by_axes([800])
            except Exception: pass
        im = Image.new('RGBA',(Wd,H),(0,0,0,0)); d = ImageDraw.Draw(im)
        pad = 9
        lineas = ajustar(d, txt, font, max(60,(x1-x0)-2*pad))
        lh = int(fs*1.34)
        bh = lh*len(lineas) + 2*pad
        bw = max(d.textbbox((0,0),l,font=font)[2] for l in lineas) + 2*pad
        cx = (x0+x1)//2; cy = (y0+y1)//2
        # la caja = union entre lo que necesita el texto y el rectangulo original
        bx0 = min(cx-bw//2, x0); bx1 = max(cx+bw//2, x1)
        by0 = min(cy-bh//2, y0); by1 = max(cy+bh//2, y1)
        bx0 = max(0,bx0); by0 = max(0,by0); bx1 = min(Wd,bx1); by1 = min(H,by1)
        fill = (255,255,255,255) if est=='light' else (12,12,12,255)
        fg   = (18,18,18,255)    if est=='light' else (255,255,255,255)
        rad  = 4 if (bx1-bx0) >= Wd-6 else 11
        d.rounded_rectangle([bx0,by0,bx1,by1], radius=rad, fill=fill)
        tcy = (by0+by1)//2 - lh*(len(lineas)-1)//2
        for i,l in enumerate(lineas):
            d.text(((bx0+bx1)//2, tcy+i*lh), l, font=font, anchor='mm', fill=fg)
        capas.append(dict(t0=t0, t1=t1, img=im))
    return capas

def estados_subs(vw, A, Wd, H):
    """PNG por palabra resaltada, estilo karaoke blanco con borde negro y palabra activa amarilla."""
    BY0, BY1 = A['banda']; BH = BY1-BY0
    font = ImageFont.truetype(SUBF, A['fsize'])
    probe = ImageDraw.Draw(Image.new('RGB',(10,10)))
    def wsz(t): bb = probe.textbbox((0,0), t, font=font); return bb[2]-bb[0]
    SP = wsz('a a') - 2*wsz('a')
    lineas, cur = [], []
    for x in vw:
        test = cur + [x]
        if cur and (wsz(' '.join(y[2] for y in test)) > A['maxw'] or len(test) > 3):
            lineas.append(cur); cur = [x]
        else: cur = test
    if cur: lineas.append(cur)
    cyl = A['cy'] - BY0
    blank = Image.new('RGBA',(Wd,BH),(0,0,0,0))
    estados = []
    for li, ln in enumerate(lineas):
        pal = [w[2].upper() for w in ln]
        anchos = [wsz(w) for w in pal]
        total = sum(anchos) + SP*(len(pal)-1)
        x = (Wd-total)//2; xs=[]
        for a in anchos: xs.append(x); x += a + SP
        nxt = lineas[li+1][0][0] if li+1 < len(lineas) else ln[-1][1]+0.40
        for wi,(s,e,_) in enumerate(ln):
            t0 = s if wi else max(0, s-0.05)
            t1 = ln[wi+1][0] if wi+1 < len(ln) else min(nxt, ln[-1][1]+0.45)
            if t1-t0 < 0.02: continue
            im = blank.copy(); d = ImageDraw.Draw(im)
            for k,w in enumerate(pal):
                col = (255,214,10,255) if k==wi else (255,255,255,255)
                d.text((xs[k], cyl), w, font=font, anchor='lm', fill=col,
                       stroke_width=4, stroke_fill=(0,0,0,255))
            estados.append((im, t0, t1))
    return estados

def pista_alfa(estados, extra, L, FPS, Wd, H, tmp, nombre, offset_y):
    """Arma un .mov RGBA con los estados del subtitulo (en coordenadas de banda)."""
    empty = Image.new('RGBA',(Wd, estados[0][0].height if estados else H),(0,0,0,0))
    ev, prev = [], 0.0; n=0; paths={}
    def guardar(im):
        nonlocal n
        p = f'{tmp}/{nombre}{n:04d}.png'; im.save(p); n += 1; return p
    pe = guardar(empty)
    seq = []
    for im,t0,t1 in estados:
        t0 = max(t0, prev); t1 = max(t1, t0+0.05)
        if t0 >= L: break
        if t0 > prev + 0.02: ev.append((prev, pe))
        ev.append((t0, guardar(im))); prev = min(t1, L)
    if prev < L-0.01: ev.append((prev, pe))
    if not ev: ev=[(0.0,pe)]
    for k,(ts,p) in enumerate(ev):
        te = ev[k+1][0] if k+1 < len(ev) else L
        if te-ts >= 0.016: seq.append((p, te-ts))
    with open(f'{tmp}/{nombre}.txt','w') as fh:
        for p,dd in seq: fh.write(f"file '{p}'\nduration {dd:.3f}\n")
        fh.write(f"file '{seq[-1][0]}'\n")
    mov = f'{tmp}/{nombre}.mov'
    run([FF,'-v','error','-y','-f','concat','-safe','0','-i',f'{tmp}/{nombre}.txt','-vsync','cfr','-r',str(FPS),
         '-c:v','qtrle','-pix_fmt','argb', mov])
    return mov

# ---------------------------------------------------------------- principal
def main(n):
    A = dict(ADS[n]); src = f'{W}/{n}.mp4'
    by0, by1 = A['banda']
    if (by1-by0) % 2: by1 += 1
    A['banda'] = (by0, by1)
    tmp = f'{W}/tmp/{n}'; os.makedirs(tmp, exist_ok=True); os.makedirs(OUT, exist_ok=True)
    cap = cv2.VideoCapture(src); FPS = round(cap.get(cv2.CAP_PROP_FPS),3)
    Wd = int(cap.get(3)); H = int(cap.get(4)); cap.release()
    L = dur(src)
    print(f'[{n}] {Wd}x{H} {FPS}fps {L:.2f}s')

    # 1) voz: sacar silencios y calzar al largo del video
    vo_raw = f'{W}/vo/{n}.wav'
    if not os.path.exists(f'{tmp}/vo_lvl.wav'):
        run([FF,'-v','error','-y','-i',vo_raw,'-af',
             'silenceremove=start_periods=1:start_threshold=-45dB:stop_periods=-1:stop_duration=0.30:'
             'stop_threshold=-40dB:stop_silence=0.14,aresample=48000','-ac','1',f'{tmp}/vo_trim.wav'])
        d0 = dur(f'{tmp}/vo_trim.wav')
        LEAD, TAIL = 0.25, 0.45
        target = L - LEAD - TAIL
        sp = d0/target
        chain=[]; s=sp
        while s > 2.0: chain.append(2.0); s/=2.0
        while s < 0.5: chain.append(0.5); s/=0.5
        chain.append(s)
        at = ','.join(f'atempo={x:.6f}' for x in chain)
        run([FF,'-v','error','-y','-i',f'{tmp}/vo_trim.wav','-af',
             f'{at},adelay={int(LEAD*1000)}|{int(LEAD*1000)},apad,aresample=48000','-ac','1','-t',f'{L:.3f}',
             f'{tmp}/vo.wav'])
        voc = f'{W}/stems/htdemucs/{n}/vocals.wav'
        g = (rms(voc) - rms(f'{tmp}/vo.wav')) if os.path.exists(voc) else 0.0
        g = max(-9.0, min(9.0, g))
        run([FF,'-v','error','-y','-i',f'{tmp}/vo.wav','-af',f'volume={g:.2f}dB,alimiter=limit=0.95',
             f'{tmp}/vo_lvl.wav'])
        print(f'   VO {d0:.2f}s -> tempo {sp:.3f} -> {dur(f"{tmp}/vo.wav"):.2f}s, nivel {g:+.1f} dB')

    # 2) palabras con tiempo
    if os.path.exists(f'{tmp}/words.json'):
        vw = [tuple(x) for x in json.load(open(f'{tmp}/words.json'))]
    else:
        from faster_whisper import WhisperModel
        model = WhisperModel('small', device='cpu', compute_type='int8')
        segs,_ = model.transcribe(f'{tmp}/vo_lvl.wav', language='es', word_timestamps=True, beam_size=5)
        wd = [(w.start, w.end, w.word.strip()) for s_ in segs for w in s_.words]
        sw = open(f'{W}/vo/{n}.txt').read().split()
        norm = lambda w: re.sub(r'[^\w]', '', w.lower(), flags=re.U)
        a = [norm(x[2]) for x in wd]; b = [norm(x) for x in sw]
        vw = []
        for op,i1,i2,j1,j2 in difflib.SequenceMatcher(None,a,b,autojunk=False).get_opcodes():
            if op=='equal':
                vw += [(wd[i1+k][0], wd[i1+k][1], sw[j1+k]) for k in range(i2-i1)]
            elif j2>j1:
                s0 = wd[i1][0] if i1 < len(wd) else (vw[-1][1] if vw else 0)
                e0 = wd[i2-1][1] if i2>i1 else s0 + 0.28*(j2-j1)
                st = max(0.05,(e0-s0)/(j2-j1))
                vw += [(s0+k*st, s0+(k+1)*st, sw[j1+k]) for k in range(j2-j1)]
        print(f'   whisper {len(wd)} palabras / guion {len(sw)} -> {len(vw)} alineadas')
        json.dump(vw, open(f'{tmp}/words.json','w'), ensure_ascii=False)

    # 3) banda limpia
    band = limpiar_banda(src, A, tmp, FPS, Wd, H)

    # 4) subtitulos nuevos
    est = estados_subs(vw, A, Wd, H)
    subs = pista_alfa(est, None, L, FPS, Wd, H, tmp, 's', A['banda'][0])
    print(f'   {len(est)} estados de subtitulo')

    # 5) stickers / placas
    caps = capa_sticker(Wd, H, A)
    stk_movs = []
    for ci,c in enumerate(caps):
        # tapar lo de abajo con inpaint grueso: se resuelve pintando la caja opaca encima,
        # pero el rectangulo original puede ser mas grande -> se agrega un velo difuminado
        velo = Image.new('RGBA',(Wd,H),(0,0,0,0))
        est_c = [(c['img'], c['t0'], min(c['t1'], L))]
        mv = pista_alfa(est_c, None, L, FPS, Wd, H, tmp, f'k{ci}_', 0)
        stk_movs.append((mv, c))

    # 6) audio
    mus = f'{W}/stems/htdemucs/{n}/no_vocals.wav'
    if not os.path.exists(f'{tmp}/mix.wav'):
        if os.path.exists(mus):
            run([FF,'-v','error','-y','-i',f'{tmp}/vo_lvl.wav','-i',mus,'-filter_complex',
                 '[0:a]aformat=sample_rates=48000:channel_layouts=stereo[v];'
                 '[1:a]aformat=sample_rates=48000:channel_layouts=stereo,volume=-2dB[m];'
                 '[v][m]amix=inputs=2:duration=longest:normalize=0,alimiter=limit=0.97[a]',
                 '-map','[a]','-ac','2','-t',f'{L:.3f}',f'{tmp}/mix.wav'])
        else:
            run([FF,'-v','error','-y','-i',f'{tmp}/vo_lvl.wav','-ac','2','-t',f'{L:.3f}',f'{tmp}/mix.wav'])

    # 7) armado
    outp = f'{OUT}/{n}-habilidades-perdidas-es.mp4'
    ins = ['-i',src,'-i',band,'-i',subs] + sum([['-i',m] for m,_ in stk_movs], []) + ['-i',f'{tmp}/mix.wav']
    fc = f'[0:v][1:v]overlay=0:{A["banda"][0]}[b];[b][2:v]overlay=0:{A["banda"][0]}:format=auto[v0]'
    last = 'v0'
    for i,(m,c) in enumerate(stk_movs):
        idx = 3+i
        fc += f';[{last}][{idx}:v]overlay=0:0:format=auto:enable=\'between(t,{c["t0"]},{min(c["t1"],L):.2f})\'[v{i+1}]'
        last = f'v{i+1}'
    aidx = 3+len(stk_movs)
    run([FF,'-v','error','-y'] + ins + ['-filter_complex', fc, '-map', f'[{last}]', '-map', f'{aidx}:a',
         '-c:v','libx264','-crf','18','-preset','medium','-pix_fmt','yuv420p','-r',str(FPS),
         '-c:a','aac','-b:a','160k','-movflags','+faststart','-shortest','-t',f'{L:.3f}', outp])
    print(f'[{n}] LISTO -> {outp}  ({dur(outp):.2f}s)')

if __name__ == '__main__':
    for n in sys.argv[1:]: main(n)
