# -*- coding: utf-8 -*-
"""Rehace un anuncio de Scented Stones en polaco: misma imagen, misma musica, VO polaca y subs polacos.
Uso: python3 render_pl.py <id 1..4>"""
import os, re, sys, json, math, subprocess, difflib
import numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont, ImageFilter

FF   = os.path.expanduser('~/bin/ffmpeg')
HERE = os.path.dirname(os.path.abspath(__file__))
SCR  = '/private/tmp/claude-501/-Users-santiagoseara-PrepCourse-Henry/eb72fe56-6ffd-4dcf-9cef-7bb251ec8d21/scratchpad'
FONTS= f'{SCR}/fonts'
DL   = os.path.expanduser('~/Downloads')

ADS = {
 1: dict(src=f'{DL}/Im 58… .mp4', stem='orig1', style='serif', font=f'{FONTS}/Bitter.ttf', wght=900,
         fsize=104, cy=1719, maxw=1270, box='#E80060', band=(1575,1865), out='SS-PL-1-mam-58.mp4'),
 2: dict(src=f'{DL}/In the next 30.mp4', stem='orig2', style='pill', font=f'{FONTS}/Montserrat-ExtraBold.ttf', wght=None,
         fsize=80, cy=1926, maxw=870, box='#F21AFA', pill='#C40AF2', pillbox=(212,1842,1229,2011),
         band=(1800,2070), out='SS-PL-2-trzydziesci-sekund.mp4'),
 3: dict(src=f'{DL}/My accountant… .mp4', stem='orig3', style='serif', font=f'{FONTS}/Bitter.ttf', wght=900,
         fsize=104, cy=1601, maxw=1270, box='#E80060', band=(1455,1745), out='SS-PL-3-ksiegowa.mp4'),
 4: dict(src=f'{DL}/Ok I need.mp4', stem='orig4', style='sans', font=f'{FONTS}/Nunito.ttf', wght=800,
         fsize=84, cy=1695, maxw=1210, box='#F21AFA', band=(1560,1810), out='SS-PL-4-sasiadka.mp4'),
}

def run(c, **k): subprocess.run(c, check=True, **k)
def dur(p):
    r = subprocess.run([FF,'-i',p], capture_output=True, text=True).stderr
    h,m,s = re.search(r'Duration: (\d+):(\d+):([\d.]+)', r).groups()
    return int(h)*3600+int(m)*60+float(s)
def rgb(h): h=h.lstrip('#'); return tuple(int(h[i:i+2],16) for i in (0,2,4))

def main(i):
    A = ADS[i]; src = A['src']
    tmp = os.path.join(HERE, f'tmp{i}'); os.makedirs(tmp, exist_ok=True)
    cap = cv2.VideoCapture(src); FPS = cap.get(cv2.CAP_PROP_FPS)
    W = int(cap.get(3)); H = int(cap.get(4)); NF = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)); cap.release()
    L = dur(src)
    print(f'[{i}] {W}x{H} {FPS}fps {L:.2f}s')

    WJ = f'{tmp}/words.json'
    # ---------- 1) voz rusa: sin silencios y ajustada al largo del original ----------
    vo_raw = f'{HERE}/vo/pl{i}.wav'
    if os.path.exists(WJ) and os.path.exists(f'{tmp}/mix.wav'):
        vw = [tuple(x) for x in json.load(open(WJ))]
        print(f'[{i}] reuso voz y tiempos ya calculados')
    else:
        run([FF,'-v','error','-y','-i',vo_raw,'-af',
             'silenceremove=start_periods=1:start_threshold=-45dB:stop_periods=-1:stop_duration=0.32:stop_threshold=-40dB:stop_silence=0.16,'
             'aresample=48000','-ac','1',f'{tmp}/vo_trim.wav'])
        d0 = dur(f'{tmp}/vo_trim.wav')
        LEAD, TAIL = 0.22, 0.25
        target = L - LEAD - TAIL
        sp = d0 / target
        chain = []
        s = sp
        while s > 2.0: chain.append(2.0); s /= 2.0
        while s < 0.5: chain.append(0.5); s /= 0.5
        chain.append(s)
        at = ','.join(f'atempo={x:.6f}' for x in chain)
        run([FF,'-v','error','-y','-i',f'{tmp}/vo_trim.wav','-af',
             f'{at},adelay={int(LEAD*1000)}|{int(LEAD*1000)},apad,aresample=48000','-ac','1','-t',f'{L:.3f}',f'{tmp}/vo.wav'])
        print(f'[{i}] VO {d0:.2f}s -> tempo {sp:.3f} -> {dur(f"{tmp}/vo.wav"):.2f}s')

        # nivel: igualar el RMS de la voz original
        def rms(p):
            r = subprocess.run([FF,'-hide_banner','-nostats','-v','info','-i',p,'-af','volumedetect','-f','null','-'],capture_output=True,text=True).stderr
            m = re.search(r'mean_volume: ([-\d.]+) dB', r); return float(m.group(1))
        voc = f'{SCR}/stems/htdemucs/{A["stem"]}/vocals.wav'
        g = rms(voc) - rms(f'{tmp}/vo.wav')
        run([FF,'-v','error','-y','-i',f'{tmp}/vo.wav','-af',f'volume={g:.2f}dB,alimiter=limit=0.95',f'{tmp}/vo_lvl.wav'])
        print(f'[{i}] nivel VO {g:+.2f} dB')

        # ---------- 2) palabras con tiempos ----------
        from faster_whisper import WhisperModel
        model = WhisperModel('medium', device='cpu', compute_type='int8')
        segs,_ = model.transcribe(f'{tmp}/vo_lvl.wav', language='pl', word_timestamps=True, beam_size=5)
        wd = [(w.start, w.end, w.word.strip()) for s_ in segs for w in s_.words]
        sw = open(f'{HERE}/vo/pl{i}.txt').read().split()
        def norm(w): return re.sub(r'[^\w]', '', w.lower(), flags=re.U)
        a = [norm(x[2]) for x in wd]; b = [norm(x) for x in sw]
        vw = []
        for op,i1,i2,j1,j2 in difflib.SequenceMatcher(None,a,b,autojunk=False).get_opcodes():
            if op=='equal':
                vw += [(wd[i1+k][0], wd[i1+k][1], sw[j1+k]) for k in range(i2-i1)]
            elif j2>j1:
                s0 = wd[i1][0] if i1 < len(wd) else (vw[-1][1] if vw else 0)
                e0 = wd[i2-1][1] if i2>i1 else s0 + 0.30*(j2-j1)
                st = max(0.05,(e0-s0)/(j2-j1))
                vw += [(s0+k*st, s0+(k+1)*st, sw[j1+k]) for k in range(j2-j1)]
        print(f'[{i}] whisper {len(wd)} palabras / guion {len(sw)} -> alineadas {len(vw)}')
        json.dump(vw, open(f'{tmp}/words.json','w'), ensure_ascii=False)

    # ---------- 3) lineas ----------
    f_size = A['fsize']
    font = ImageFont.truetype(A['font'], f_size)
    if A['wght']:
        try: font.set_variation_by_axes([A['wght']])
        except Exception as e: print('var:', e)
    probe = ImageDraw.Draw(Image.new('RGB',(10,10)))
    def wsize(t): 
        bb = probe.textbbox((0,0), t, font=font); return bb[2]-bb[0]
    SPACE = wsize('a a') - 2*wsize('a')
    lines, cur = [], []
    for x in vw:
        test = cur + [x]
        txt = ' '.join(y[2] for y in test)
        if cur and (wsize(txt) > A['maxw'] or len(test) > 6):
            lines.append(cur); cur = [x]
        else:
            cur = test
        if re.search(r'[.?!]$', x[2]) and len(cur) >= 3:
            lines.append(cur); cur = []
    if cur: lines.append(cur)
    print(f'[{i}] {len(lines)} lineas')
    json.dump([[w[2] for w in l] for l in lines], open(f'{tmp}/lines.json','w'), ensure_ascii=False, indent=0)

    # ---------- 4) PNG por estado ----------
    BY0, BY1 = A['band']; BH = BY1-BY0
    cyl = A['cy'] - BY0
    BOX = rgb(A['box'])
    blank = Image.new('RGBA',(W,BH),(0,0,0,0))
    states = []   # (png, t0, t1)
    n = 0
    for li,ln in enumerate(lines):
        words = [w[2] for w in ln]
        widths = [wsize(w) for w in words]
        total = sum(widths) + SPACE*(len(words)-1)
        x0 = (W-total)//2
        nxt = lines[li+1][0][0] if li+1 < len(lines) else ln[-1][1]+0.45
        xs, x = [], x0
        for ww in widths: xs.append(x); x += ww + SPACE
        # capa de texto: se dibuja una sola vez por linea (el stroke de PIL es lento)
        tl = blank.copy(); dt = ImageDraw.Draw(tl)
        sw_, sc_ = ((10,(0,0,0,255)) if A['style']=='serif'
                    else (5,(25,0,40,255)) if A['style']=='pill' else (5,(45,30,55,235)))
        for k,ww in enumerate(words):
            dt.text((xs[k],cyl), ww, font=font, anchor='lm', fill=(255,255,255,255),
                    stroke_width=sw_, stroke_fill=sc_)
        base = blank.copy()
        if A['style']=='pill':
            db = ImageDraw.Draw(base)
            px0,py0,px1,py1 = A['pillbox']; py0-=BY0; py1-=BY0
            sh = Image.new('RGBA',(W,BH),(0,0,0,0)); ds=ImageDraw.Draw(sh)
            ds.rounded_rectangle([px0,py0+10,px1,py1+12], radius=(py1-py0)//2, fill=(90,0,120,150))
            base.alpha_composite(sh.filter(ImageFilter.GaussianBlur(10)))
            db.rounded_rectangle([px0,py0,px1,py1], radius=(py1-py0)//2, fill=rgb(A['pill'])+(255,))
        for wi,(s,e,w) in enumerate(ln):
            t0 = s if wi else max(0, s-0.06)
            t1 = ln[wi+1][0] if wi+1 < len(ln) else min(nxt, ln[-1][1]+0.5)
            if t1 - t0 < 0.02: continue
            im = base.copy(); d = ImageDraw.Draw(im)
            bx0 = xs[wi]-18; bx1 = xs[wi]+widths[wi]+18
            if A['style']=='serif':
                by0 = cyl-78; by1 = cyl+78
                d.rounded_rectangle([bx0,by0,bx1,by1], radius=12, fill=BOX+(255,))
            else:
                by0 = cyl-54; by1 = cyl+54
                d.rounded_rectangle([bx0-4,by0,bx1+4,by1], radius=22, fill=BOX+(255,))
            im.alpha_composite(tl)
            p = f'{tmp}/s{n:04d}.png'; im.save(p); states.append((p,t0,t1)); n += 1
    # pista alfa
    empty = f'{tmp}/empty.png'; blank.save(empty)
    ev, prev = [], 0.0          # (instante, png) en tiempo absoluto, sin solapes
    for p,t0,t1 in states:
        t0 = max(t0, prev); t1 = max(t1, t0+0.05)
        if t0 >= L: break
        if t0 > prev + 0.02: ev.append((prev, empty))
        ev.append((t0, p)); prev = min(t1, L)
    if prev < L - 0.01: ev.append((prev, empty))
    seq = []
    for k,(ts_,p) in enumerate(ev):
        te = ev[k+1][0] if k+1 < len(ev) else L
        if te - ts_ >= 0.016: seq.append((p, te-ts_))
    with open(f'{tmp}/caps.txt','w') as fh:
        for p,dd in seq: fh.write(f"file '{p}'\nduration {dd:.3f}\n")
        fh.write(f"file '{seq[-1][0]}'\n")
    run([FF,'-v','error','-y','-f','concat','-safe','0','-i',f'{tmp}/caps.txt','-vsync','cfr','-r',str(FPS),
         '-c:v','qtrle','-pix_fmt','argb',f'{tmp}/caps.mov'])
    print(f'[{i}] {len(states)} estados de subtitulo')

    # ---------- 5) tapar los subtitulos ingleses ----------
    need_clean = A['style'] != 'pill'
    if need_clean and not os.path.exists(f'{tmp}/band.mp4'):
        cap = cv2.VideoCapture(src)
        pipe = subprocess.Popen([FF,'-v','error','-y','-f','rawvideo','-pix_fmt','bgr24','-s',f'{W}x{BH}',
            '-r',str(FPS),'-i','-','-c:v','libx264','-crf','12','-preset','veryfast','-pix_fmt','yuv420p',
            f'{tmp}/band.mp4'], stdin=subprocess.PIPE)
        k3 = np.ones((3,3), np.uint8); nf=0
        while True:
            ok,f = cap.read()
            if not ok: break
            band = f[BY0:BY1].copy()
            hsv = cv2.cvtColor(band, cv2.COLOR_BGR2HSV)
            b,g_,r = band[...,0].astype(int), band[...,1].astype(int), band[...,2].astype(int)
            white = (b>205)&(g_>205)&(r>205)
            pink  = (hsv[...,1]>110)&(hsv[...,2]>110)&(hsv[...,0]>125)&(hsv[...,0]<180)
            light = (white|pink).astype(np.uint8)
            dark  = ((b<85)&(g_<85)&(r<85)).astype(np.uint8)
            near  = cv2.dilate(light,k3,iterations=4)
            m = (light | (dark & near)).astype(np.uint8)
            both = cv2.dilate(light,k3,iterations=5) & cv2.dilate(dark,k3,iterations=5)
            m = (m & cv2.dilate(both,k3,iterations=3)) | pink.astype(np.uint8)
            m = cv2.dilate(m,k3,iterations=4)
            if m.any(): band = cv2.inpaint(band, m*255, 6, cv2.INPAINT_TELEA)
            pipe.stdin.write(band.tobytes()); nf+=1
        cap.release(); pipe.stdin.close(); pipe.wait()
        print(f'[{i}] banda limpia: {nf} frames')

    # ---------- 6) audio: cama original + voz rusa ----------
    mus = f'{SCR}/stems/htdemucs/{A["stem"]}/no_vocals.wav'
    if not os.path.exists(f'{tmp}/mix.wav'): run([FF,'-v','error','-y','-i',f'{tmp}/vo_lvl.wav','-i',mus,'-filter_complex',
         '[0:a]aformat=sample_rates=48000:channel_layouts=stereo[v];[1:a]aformat=sample_rates=48000:channel_layouts=stereo[m];'
         '[v][m]amix=inputs=2:duration=longest:normalize=0,alimiter=limit=0.97[a]',
         '-map','[a]','-ac','2','-t',f'{L:.3f}',f'{tmp}/mix.wav'])

    # ---------- 7) armado final ----------
    outp = os.path.join(os.path.dirname(HERE), A['out'])
    if need_clean:
        run([FF,'-v','error','-y','-i',src,'-i',f'{tmp}/band.mp4','-i',f'{tmp}/caps.mov','-i',f'{tmp}/mix.wav',
             '-filter_complex',f'[0:v][1:v]overlay=0:{BY0}[b];[b][2:v]overlay=0:{BY0}:format=auto[v]',
             '-map','[v]','-map','3:a','-c:v','libx264','-crf','18','-preset','medium','-pix_fmt','yuv420p',
             '-r',str(FPS),'-c:a','aac','-b:a','192k','-movflags','+faststart','-shortest',outp])
    else:
        run([FF,'-v','error','-y','-i',src,'-i',f'{tmp}/caps.mov','-i',f'{tmp}/mix.wav',
             '-filter_complex',f'[0:v][1:v]overlay=0:{BY0}:format=auto[v]',
             '-map','[v]','-map','2:a','-c:v','libx264','-crf','18','-preset','medium','-pix_fmt','yuv420p',
             '-r',str(FPS),'-c:a','aac','-b:a','192k','-movflags','+faststart','-shortest',outp])
    print(f'[{i}] LISTO -> {outp}  ({dur(outp):.2f}s)')

if __name__ == '__main__':
    main(int(sys.argv[1]))
