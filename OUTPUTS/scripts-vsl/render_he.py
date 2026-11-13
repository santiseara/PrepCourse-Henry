# -*- coding: utf-8 -*-
"""Rehace los 8 anuncios de Scented Stones en HEBREO (RTL).
Base limpia = el video portugues ya renderizado + la banda inpaintada de tmpN del pase portugues
(para los estilos sin pildora) o el video portugues tal cual (la pildora opaca nueva tapa la vieja).
Voz Sulafat hebrea, cama de audio original (stems), subtitulos hebreos con bidi y fuente hebrea.
Uso: python3 render_he.py <1..8> [toma]
"""
import os, re, sys, json, subprocess, difflib
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from bidi.algorithm import get_display

FF    = os.path.expanduser('~/bin/ffmpeg')
HERE  = os.path.dirname(os.path.abspath(__file__))
ADSD  = os.path.expanduser('~/Desktop/scented-stones-ad/anuncios')
SCR   = f'{ADSD}/_assets'
FONTS = f'{SCR}/fonts'
PTW   = f'{ADSD}/portugues/work'
PT    = f'{ADSD}/portugues'

SERIF = f'{FONTS}/NotoSerifHebrew.ttf'
HEEBO = f'{FONTS}/Heebo.ttf'
RUBIK = f'{FONTS}/Rubik.ttf'

ADS = {
 1: dict(base=f'{PT}/SS-PT-1-tenho-58.mp4', band=f'{PTW}/tmp1/band.mp4', stem='orig1', style='serif',
         font=SERIF, wght=900, latfont=f'{FONTS}/Bitter.ttf', latwght=900, latsize=104,
         cy=1719, maxw=1230, box='#E80060', bandy=(1575,1865), out='SS-HE-1-bat-58.mp4'),
 2: dict(base=f'{PT}/SS-PT-2-trinta-segundos.mp4', band=None, stem='orig2', style='pill',
         font=HEEBO, wght=800, latfont=f'{FONTS}/Montserrat-ExtraBold.ttf', latwght=None, latsize=80,
         cy=1926, maxw=860, box='#F21AFA', pill='#C40AF2', pillbox=(212,1842,1229,2011),
         bandy=(1800,2070), out='SS-HE-2-shloshim-shniyot.mp4'),
 3: dict(base=f'{PT}/SS-PT-3-contadora.mp4', band=f'{PTW}/tmp3/band.mp4', stem='orig3', style='serif',
         font=SERIF, wght=900, latfont=f'{FONTS}/Bitter.ttf', latwght=900, latsize=104,
         cy=1601, maxw=1230, box='#E80060', bandy=(1455,1745), out='SS-HE-3-roat-heshbon.mp4'),
 4: dict(base=f'{PT}/SS-PT-4-vizinha.mp4', band=f'{PTW}/tmp4/band.mp4', stem='orig4', style='sans',
         font=RUBIK, wght=800, latfont=f'{FONTS}/Nunito.ttf', latwght=800, latsize=84,
         cy=1695, maxw=1180, box='#F21AFA', bandy=(1560,1810), out='SS-HE-4-hashchena.mp4'),
 5: dict(base=f'{PT}/SS-PT-5-nunca-quis.mp4', band=f'{PTW}/tmp5/band.mp4', stem='orig5', style='kara2',
         font=HEEBO, wght=700, latfont='/System/Library/Fonts/Supplemental/Courier New Bold.ttf',
         latwght=None, latsize=47, bl=1457, lineh=56, maxw=700, stroke=3,
         hi='#EBD414', bandy=(1368,1512), out='SS-HE-5-lo-ratziti-esek.mp4',
         repl=[(['שנים','עשר','אלף','שקל'],'12,000 שקל'), (['תשעים','ותשעה','שקלים'],'99 שקלים')]),
 6: dict(base=f'{PT}/SS-PT-6-tres-coisas.mp4', band=f'{PTW}/tmp6/band.mp4', stem='orig6', style='karaoke',
         font=HEEBO, wght=800, latfont=f'{FONTS}/Nunito.ttf', latwght=800, latsize=56,
         bl=1230, lineh=60, maxw=620, maxw2=2, stroke=6, hi='#FFFF00',
         bandy=(1114,1300), out='SS-HE-6-shlosha-dvarim.mp4',
         repl=[(['חמישים','שקל'],'50 שקל')]),
 7: dict(base=f'{PT}/SS-PT-7-mulheres-da-sua-cidade.mp4', band=None, stem='orig7', style='pillacc',
         font=HEEBO, wght=700, latfont=f'{FONTS}/Nunito.ttf', latwght=800, latsize=50,
         pillbox=(164,1384,917,1511), pill='#F30DC7', xr=831, bl=1436, lineh=62, maxw=580, stroke=5,
         bandy=(1370,1525), out='SS-HE-7-hanashim-bair-shelach.mp4',
         repl=[(['שלושים','וחמש'],'35'), (['וחמש','שנה'],'55')]),
 8: dict(base=f'{PT}/SS-PT-8-bancada-da-cozinha.mp4', band=None, stem='orig8', style='pillword',
         font=HEEBO, wght=900, latfont=f'{FONTS}/Montserrat-ExtraBold.ttf', latwght=None, latsize=148,
         pillbox=(164,1242,1279,1631), pill='#EF3BEC', cx=721, bl=1488, maxw=1000, stroke=8,
         bandy=(1230,1645), out='SS-HE-8-hashaish-bamitbach.mp4',
         repl=[(['אלף','ושלוש','מאות','שקל'],'1,300 שקל'), (['עשרים','וחמש','עד','חמישים'],'25 עד 50'),
               (['מאה','ועשרים'],'120'), (['שבעת','אלפים','שקל'],'7,000 שקל')]),
}
VO = {1:'he1',2:'he2',3:'he3',4:'he4',5:'he5',6:'he6',7:'he7',8:'he8'}

def run(c, **k): subprocess.run(c, check=True, **k)
def dur(p):
    r = subprocess.run([FF,'-i',p], capture_output=True, text=True).stderr
    h,m,s = re.search(r'Duration: (\d+):(\d+):([\d.]+)', r).groups()
    return int(h)*3600+int(m)*60+float(s)
def rgb(h): h=h.lstrip('#'); return tuple(int(h[i:i+2],16) for i in (0,2,4))
def norm(w): return re.sub(r'[^\w]', '', w.lower(), flags=re.U)
def rms(p):
    r = subprocess.run([FF,'-hide_banner','-nostats','-v','info','-i',p,'-af','volumedetect','-f','null','-'],
                       capture_output=True, text=True).stderr
    return float(re.search(r'mean_volume: ([-\d.]+) dB', r).group(1))
def vis(t): return get_display(t)

def cargar(path, size, wght):
    f = ImageFont.truetype(path, size)
    if wght:
        try: f.set_variation_by_axes([wght])
        except Exception: pass
    return f

def tam_hebreo(A):
    """fsize hebreo que iguala la altura de letra del subtitulo latino original"""
    probe = ImageDraw.Draw(Image.new('RGB',(10,10)))
    lat = cargar(A['latfont'], A['latsize'], A.get('latwght'))
    bb = probe.textbbox((0,0),'H',font=lat); target = bb[3]-bb[1]
    S = A['latsize']
    for _ in range(40):
        f = cargar(A['font'], S, A.get('wght'))
        bb = probe.textbbox((0,0),'אבן',font=f); h = bb[3]-bb[1]
        if abs(h-target) <= 1: break
        S = max(8, int(round(S*target/max(h,1))))
    print(f'   fuente hebrea {os.path.basename(A["font"])} {S}px (altura {h}px ~ latina {target}px)')
    return S

def aplicar_repl(vw, repl):
    out, i = [], 0
    while i < len(vw):
        hecho = False
        for seq, rep in repl:
            n = len(seq)
            if [norm(x[2]) for x in vw[i:i+n]] == seq:
                cola = re.sub(r'^[\w\s]+','', vw[i+n-1][2])
                out.append((vw[i][0], vw[i+n-1][1], rep + cola)); i += n; hecho = True; break
        if not hecho: out.append(vw[i]); i += 1
    return out

def main(i, toma=None):
    A = ADS[i]
    tmp = os.path.join(HERE, f'tmp{i}'); os.makedirs(tmp, exist_ok=True)
    import cv2
    cap = cv2.VideoCapture(A['base']); FPS = cap.get(cv2.CAP_PROP_FPS)
    W = int(cap.get(3)); H = int(cap.get(4)); cap.release()
    L = dur(A['base'])
    print(f'[{i}] {W}x{H} {FPS}fps {L:.2f}s  estilo {A["style"]}')

    # ---------- 1) voz ----------
    vo_raw = f'{HERE}/vo/{VO[i]}_{toma or "a"}.wav'
    run([FF,'-v','error','-y','-i',vo_raw,'-af',
         'silenceremove=start_periods=1:start_threshold=-45dB:stop_periods=-1:stop_duration=0.32:'
         'stop_threshold=-40dB:stop_silence=0.16,aresample=48000','-ac','1',f'{tmp}/vo_trim.wav'])
    d0 = dur(f'{tmp}/vo_trim.wav')
    LEAD, TAIL = (0.18,0.18) if i==5 else (0.22,0.25)
    sp = d0/(L-LEAD-TAIL)
    chain, s = [], sp
    while s > 2.0: chain.append(2.0); s /= 2.0
    while s < 0.5: chain.append(0.5); s /= 0.5
    chain.append(s)
    at = ','.join(f'atempo={x:.6f}' for x in chain)
    run([FF,'-v','error','-y','-i',f'{tmp}/vo_trim.wav','-af',
         f'{at},adelay={int(LEAD*1000)}|{int(LEAD*1000)},apad,aresample=48000','-ac','1','-t',f'{L:.3f}',f'{tmp}/vo.wav'])
    print(f'[{i}] VO {d0:.2f}s -> tempo {sp:.3f}')
    voc = f'{SCR}/stems/htdemucs/{A["stem"]}/vocals.wav'
    g = rms(voc) - rms(f'{tmp}/vo.wav')
    run([FF,'-v','error','-y','-i',f'{tmp}/vo.wav','-af',f'volume={g:.2f}dB,alimiter=limit=0.95',f'{tmp}/vo_lvl.wav'])
    print(f'[{i}] nivel VO {g:+.2f} dB')

    # ---------- 2) palabras con tiempos ----------
    from faster_whisper import WhisperModel
    model = WhisperModel('medium', device='cpu', compute_type='int8')
    segs,_ = model.transcribe(f'{tmp}/vo_lvl.wav', language='he', word_timestamps=True, beam_size=5)
    wd = [(w.start, w.end, w.word.strip()) for s_ in segs for w in s_.words]
    sw = open(f'{HERE}/vo/{VO[i]}.txt', encoding='utf-8').read().split()
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
    if A.get('repl'): vw = aplicar_repl(vw, A['repl'])
    json.dump(vw, open(f'{tmp}/words.json','w'), ensure_ascii=False)

    # ---------- 3) tipografia ----------
    FS = tam_hebreo(A)
    font = cargar(A['font'], FS, A.get('wght'))
    probe = ImageDraw.Draw(Image.new('RGB',(10,10)))
    def wsize(t):
        bb = probe.textbbox((0,0), vis(t), font=font); return bb[2]-bb[0]
    SPACE = max(8, int(round(FS*0.26)))
    BY0, BY1 = A['bandy']; BH = BY1-BY0
    blank = Image.new('RGBA',(W,BH),(0,0,0,0))
    WHITE = (255,255,255,255)
    HI = rgb(A['hi'])+(255,) if A.get('hi') else WHITE

    # ---------- 4) agrupado en lineas / bloques ----------
    if A['style'] in ('serif','sans','pill'):
        lines, cur = [], []
        for x in vw:
            test = cur + [x]
            if cur and (wsize(' '.join(y[2] for y in test)) > A['maxw'] or len(test) > 6):
                lines.append(cur); cur = [x]
            else: cur = test
            if re.search(r'[.?!]$', x[2]) and len(cur) >= 3:
                lines.append(cur); cur = []
        if cur: lines.append(cur)
        bloques = [[l] for l in lines]
    elif A['style'] == 'pillword':
        bloques = [[[w]] for w in vw]
    else:
        nlin = A.get('maxw2', 2); bloques, cur, lin = [], [], []
        for w in vw:
            if lin and wsize(' '.join(x[2] for x in lin+[w])) > A['maxw']:
                cur.append(lin); lin = []
                if len(cur) == nlin: bloques.append(cur); cur = []
            lin.append(w)
            if re.search(r'[.!?]$', w[2]):
                cur.append(lin); lin = []; bloques.append(cur); cur = []
        if lin: cur.append(lin)
        if cur: bloques.append(cur)
    json.dump([[' '.join(w[2] for w in l) for l in b] for b in bloques],
              open(f'{tmp}/bloques.json','w'), ensure_ascii=False, indent=0)
    print(f'[{i}] {len(bloques)} bloques')

    # fondo fijo de pildora (un poco mas grande, para tapar la portuguesa)
    pbase = blank.copy()
    if A['style'] in ('pill','pillacc','pillword'):
        px0,py0,px1,py1 = A['pillbox']; py0 -= BY0; py1 -= BY0
        M = 6
        rad = (py1-py0)//2 if A['style']=='pill' else (py1-py0)//3
        sh = Image.new('RGBA',(W,BH),(0,0,0,0)); ds = ImageDraw.Draw(sh)
        ds.rounded_rectangle([px0-M,py0+10,px1+M,py1+12], radius=rad, fill=(90,0,115,140))
        pbase.alpha_composite(sh.filter(ImageFilter.GaussianBlur(11)))
        ImageDraw.Draw(pbase).rounded_rectangle([px0-M,py0-M,px1+M,py1+M], radius=rad, fill=rgb(A['pill'])+(255,))

    # ---------- 5) un PNG por estado ----------
    states, n = [], 0
    SW_ = A.get('stroke')
    for bi, b in enumerate(bloques):
        plano = [(li,wi,w) for li,l in enumerate(b) for wi,w in enumerate(l)]
        fin = bloques[bi+1][0][0][0] if bi+1 < len(bloques) else min(L, plano[-1][2][1]+0.5)
        fin = min(fin, plano[-1][2][1]+0.55)
        pos = {}
        for li,l in enumerate(b):
            ws = [wsize(w[2]) for w in l]
            tot = sum(ws) + SPACE*(len(l)-1)
            if A['style']=='pillword':   xr = A['cx'] + tot/2
            elif A['style']=='pillacc':  xr = A['xr']
            else:                        xr = (W + tot)/2
            if A['style'] in ('serif','sans','pill'):
                y = A['cy'] - BY0
            else:
                y = A['bl'] + A.get('lineh',0)*li - BY0
                if A['style']=='karaoke' and len(b) > 1: y -= A['lineh']*(len(b)-1)//2
                if A['style']=='kara2':  y = A['bl'] - (A['lineh']//2)*(len(b)-1) + A['lineh']*li - BY0
            x = xr
            for k,w in enumerate(l):
                x -= ws[k]; pos[(li,k)] = (x, y, ws[k]); x -= SPACE
        for k,(li,wi,w) in enumerate(plano):
            t0 = w[0] if k else max(0, w[0]-0.06)
            t1 = plano[k+1][2][0] if k+1 < len(plano) else fin
            if t1-t0 < 0.02: continue
            im = pbase.copy(); d = ImageDraw.Draw(im)
            if A['style'] in ('serif','sans','pill'):
                x0_,y0_,ww_ = pos[(li,wi)]
                if A['style']=='serif':
                    d.rounded_rectangle([x0_-18, y0_-78, x0_+ww_+18, y0_+78], radius=12, fill=rgb(A['box'])+(255,))
                else:
                    d.rounded_rectangle([x0_-22, y0_-54, x0_+ww_+22, y0_+54], radius=22, fill=rgb(A['box'])+(255,))
                sw2, sc2 = ((10,(0,0,0,255)) if A['style']=='serif'
                            else (5,(25,0,40,255)) if A['style']=='pill' else (5,(45,30,55,235)))
                for lj,lw,ww in plano:
                    x_,y_,_ = pos[(lj,lw)]
                    d.text((x_,y_), vis(ww[2]), font=font, anchor='lm', fill=WHITE,
                           stroke_width=sw2, stroke_fill=sc2)
            else:
                visibles = plano if A['style'] in ('karaoke','kara2') else plano[:k+1]
                for lj,lw,ww in visibles:
                    x_,y_,_ = pos[(lj,lw)]
                    col = HI if (A['style'] in ('karaoke','kara2') and (lj,lw)==(li,wi)) else WHITE
                    d.text((x_,y_), vis(ww[2]), font=font, anchor='ls', fill=col,
                           stroke_width=SW_, stroke_fill=(0,0,0,235))
            p = f'{tmp}/s{n:04d}.png'; im.save(p); states.append((p,t0,t1)); n += 1
    print(f'[{i}] {len(states)} estados de subtitulo')

    # ---------- 6) pista alfa ----------
    empty = f'{tmp}/empty.png'; (pbase if A['style'] in ('pill','pillacc','pillword') else blank).save(empty)
    ev, prev = [], 0.0
    for p,t0,t1 in states:
        t0 = max(t0, prev); t1 = max(t1, t0+0.05)
        if t0 >= L: break
        if t0 > prev + 0.02: ev.append((prev, empty))
        ev.append((t0,p)); prev = min(t1, L)
    if prev < L-0.01: ev.append((prev, empty))
    seq = []
    for k,(ts_,p) in enumerate(ev):
        te = ev[k+1][0] if k+1 < len(ev) else L
        if te-ts_ >= 0.016: seq.append((p, te-ts_))
    with open(f'{tmp}/caps.txt','w') as fh:
        for p,dd in seq: fh.write(f"file '{p}'\nduration {dd:.3f}\n")
        fh.write(f"file '{seq[-1][0]}'\n")
    run([FF,'-v','error','-y','-f','concat','-safe','0','-i',f'{tmp}/caps.txt','-vsync','cfr','-r',str(FPS),
         '-c:v','qtrle','-pix_fmt','argb',f'{tmp}/caps.mov'])

    # ---------- 7) audio: cama original + voz hebrea ----------
    mus = f'{SCR}/stems/htdemucs/{A["stem"]}/no_vocals.wav'
    run([FF,'-v','error','-y','-i',f'{tmp}/vo_lvl.wav','-i',mus,'-filter_complex',
         '[0:a]aformat=sample_rates=48000:channel_layouts=stereo[v];'
         '[1:a]aformat=sample_rates=48000:channel_layouts=stereo[m];'
         '[v][m]amix=inputs=2:duration=longest:normalize=0,alimiter=limit=0.97[a]',
         '-map','[a]','-ac','2','-t',f'{L:.3f}',f'{tmp}/mix.wav'])

    # ---------- 8) armado final ----------
    outp = os.path.join(os.path.dirname(HERE), A['out'])
    if A.get('band'):
        run([FF,'-v','error','-y','-i',A['base'],'-i',A['band'],'-i',f'{tmp}/caps.mov','-i',f'{tmp}/mix.wav',
             '-filter_complex',f'[0:v][1:v]overlay=0:{BY0}[b];[b][2:v]overlay=0:{BY0}:format=auto[v]',
             '-map','[v]','-map','3:a','-c:v','libx264','-crf','18','-preset','medium','-pix_fmt','yuv420p',
             '-r',str(FPS),'-c:a','aac','-b:a','192k','-movflags','+faststart','-shortest',outp])
    else:
        run([FF,'-v','error','-y','-i',A['base'],'-i',f'{tmp}/caps.mov','-i',f'{tmp}/mix.wav',
             '-filter_complex',f'[0:v][1:v]overlay=0:{BY0}:format=auto[v]',
             '-map','[v]','-map','2:a','-c:v','libx264','-crf','18','-preset','medium','-pix_fmt','yuv420p',
             '-r',str(FPS),'-c:a','aac','-b:a','192k','-movflags','+faststart','-shortest',outp])
    print(f'[{i}] LISTO -> {outp}  ({dur(outp):.2f}s)')

if __name__ == '__main__':
    main(int(sys.argv[1]), sys.argv[2] if len(sys.argv) > 2 else None)
