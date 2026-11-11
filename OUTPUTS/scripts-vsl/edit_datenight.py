# -*- coding: utf-8 -*-
"""Ads de Noche de Citas Cristiana (Argentina, 2026-11-10): montaje SIN voz en off.

Clona la edicion de Date Night Cristao (Ana Cristina, BR):
  - 15 s exactos, 9:16, cortes de ~1,5 s.
  - SIN locucion y SIN subtitulos: solo musica y carteles fijos.
  - Cartel 1 (el hook) fijo sobre el b-roll de la pareja; cartel 2 (que es) fijo sobre las
    hojas del producto a pantalla completa; cierre con caja blanca de CTA sobre pareja feliz.
  - Tipografia Poppins SemiBold blanca con borde negro, centrada, 2 a 4 lineas, con emoji.

Uso: python3 edit_datenight.py plan.json salida.mp4
"""
import os, re, sys, json, subprocess

from PIL import Image, ImageDraw, ImageFont

FF = os.path.expanduser('~/bin/ffmpeg')
P = json.load(open(sys.argv[1])); OUT = sys.argv[2]
base = os.path.dirname(os.path.abspath(sys.argv[1]))
def F(p): return p if os.path.isabs(p) else os.path.join(base, p)
tmp = os.path.join(base, os.path.basename(OUT) + '_tmp'); os.makedirs(tmp, exist_ok=True)

W, H, FPS = 1080, 1920, 30
FD = os.path.expanduser('~/Desktop/date-night/anuncios/work/fonts')
POP = FD + '/Poppins-SemiBold.ttf'
POPB = FD + '/Poppins-Bold.ttf'
EMOJI = '/System/Library/Fonts/Apple Color Emoji.ttc'
EMRE = re.compile('([\U0001F300-\U0001FAFF☀-➿⬀-⯿️❤]+)')


def run(c): subprocess.run(c, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
def font(sz, path=POP): return ImageFont.truetype(path, sz)


def emoji_img(ch, h):
    try:
        f = ImageFont.truetype(EMOJI, 160)   # Apple Color Emoji solo acepta 160, 96 y 64
        im = Image.new('RGBA', (240, 240))
        ImageDraw.Draw(im).text((4, 4), ch, font=f, embedded_color=True)
        bb = im.getbbox()
        if not bb: return None
        im = im.crop(bb)
        return im.resize((max(1, int(im.width * h / im.height)), h), Image.LANCZOS)
    except Exception:
        return None


def trozos(linea):
    """Parte una linea en [(texto|emoji, es_emoji)] para poder dibujar los emojis a color."""
    out = []
    for p in EMRE.split(linea):
        if not p: continue
        out.append((p, bool(EMRE.fullmatch(p))))
    return out


def ancho(d, linea, f, em_h):
    w = 0
    for t, es in trozos(linea):
        if es:
            for ch in t:
                if ch == '️': continue
                im = emoji_img(ch, em_h); w += (im.width + 8) if im else 0
        else:
            w += d.textlength(t, font=f)
    return w


def cortar(d, txt, f, em_h, maxw):
    """Reparte el texto en lineas que entren en maxw, respetando los saltos escritos a mano."""
    lineas = []
    for parrafo in txt.split('\n'):
        act = ''
        for pal in parrafo.split(' '):
            prueba = (act + ' ' + pal).strip()
            if act and ancho(d, prueba, f, em_h) > maxw:
                lineas.append(act); act = pal
            else:
                act = prueba
        if act: lineas.append(act)
    return lineas


def png_cartel(c, path):
    """El cartel fijo del ganador: blanco, borde negro, centrado, con emoji a color."""
    im = Image.new('RGBA', (W, H)); d = ImageDraw.Draw(im)
    txt = c['text'].upper() if c.get('upper') else c['text']
    fs = c.get('fs', 64); maxw = c.get('maxw', 880)
    f = font(fs, POPB if c.get('bold') else POP)
    em = int(fs * 0.95)
    lineas = cortar(d, txt, f, em, maxw)
    while len(lineas) > c.get('maxlin', 4) and fs > 40:
        fs -= 3; f = font(fs, POPB if c.get('bold') else POP); em = int(fs * 0.95)
        lineas = cortar(d, txt, f, em, maxw)
    lh = int(fs * 1.30)
    y = int(H * c.get('y', 0.26))
    bord = c.get('bord', 7)
    for ln in lineas:
        x = (W - ancho(d, ln, f, em)) / 2
        for t, es in trozos(ln):
            if es:
                for ch in t:
                    if ch == '️': continue
                    e = emoji_img(ch, em)
                    if e:
                        im.alpha_composite(e, (int(x), int(y + (lh - em) / 2 - fs * 0.06)))
                        x += e.width + 8
            else:
                d.text((x, y), t, font=f, fill=(255, 255, 255, 255),
                       stroke_width=bord, stroke_fill=(0, 0, 0, 235))
                x += d.textlength(t, font=f)
        y += lh
    im.save(path)


def png_caja(c, path):
    """La caja blanca del cierre: 'CLIQUE NO LINK ABAIXO' del ganador."""
    im = Image.new('RGBA', (W, H)); d = ImageDraw.Draw(im)
    txt = c['text']; fs = c.get('fs', 60)
    f = font(fs, POPB)
    em = int(fs * 0.95)
    lineas = cortar(d, txt, f, em, c.get('maxw', 820))
    lh = int(fs * 1.26)
    anchos = [ancho(d, ln, f, em) for ln in lineas]
    bw = max(anchos) + 76; bh = lh * len(lineas) + 26
    x0 = (W - bw) / 2; y0 = int(H * c.get('y', 0.32))
    d.rounded_rectangle((x0, y0, x0 + bw, y0 + bh), 10, fill=(255, 255, 255, 252))
    y = y0 + 13
    for ln, aw in zip(lineas, anchos):
        x = (W - aw) / 2
        for t, es in trozos(ln):
            if es:
                for ch in t:
                    if ch == '️': continue
                    e = emoji_img(ch, em)
                    if e:
                        im.alpha_composite(e, (int(x), int(y + (lh - em) / 2)))
                        x += e.width + 8
            else:
                d.text((x, y), t, font=f, fill=(14, 14, 14, 255))
                x += d.textlength(t, font=f)
        y += lh
    im.save(path)


def png_sticker(c, path):
    """Cartel estilo TikTok para los organicos: caja negra translucida, texto blanco."""
    im = Image.new('RGBA', (W, H)); d = ImageDraw.Draw(im)
    fs = c.get('fs', 54); f = font(fs, POP); em = int(fs * 0.95)
    lineas = cortar(d, c['text'], f, em, c.get('maxw', 780))
    lh = int(fs * 1.34)
    anchos = [ancho(d, ln, f, em) for ln in lineas]
    y = int(H * c.get('y', 0.22))
    for ln, aw in zip(lineas, anchos):
        x0 = (W - aw) / 2 - 20
        d.rounded_rectangle((x0, y - 8, x0 + aw + 40, y + lh - 6), 8, fill=(0, 0, 0, 150))
        x = (W - aw) / 2
        for t, es in trozos(ln):
            if es:
                for ch in t:
                    if ch == '️': continue
                    e = emoji_img(ch, em)
                    if e:
                        im.alpha_composite(e, (int(x), int(y + (lh - em) / 2 - 4)))
                        x += e.width + 8
            else:
                d.text((x, y), t, font=f, fill=(255, 255, 255, 255))
                x += d.textlength(t, font=f)
        y += lh + 6
    im.save(path)


# ---------------------------------------------------------------- 1) los planos
segs = []
for i, s in enumerate(P['segments']):
    src = F(s['src']); out = os.path.join(tmp, 'seg%02d.mp4' % i); dur = s['dur']
    z = s.get('zoom', 1.0); yb = s.get('ybias', 0.0)
    if src.lower().endswith('.png') or src.lower().endswith('.jpg'):
        # hoja del producto: zoom lento, como los planos fijos del ganador.
        # OJO: zoompan emite d cuadros POR CUADRO DE ENTRADA, asi que la entrada es una sola
        # imagen y el largo se corta con -frames:v. Con -t daba 120 s por hoja.
        n = int(round(dur * FPS))
        zi = ('scale=%d:-1,crop=%d:%d:(iw-%d)/2:(ih-%d)/2+%d,'
              'zoompan=z=\'min(zoom+0.0006,1.07)\':d=%d:s=%dx%d:fps=%d'
              % (int(W * 1.10), W, H, W, H, int(yb * H * 0.08), n, W, H, FPS))
        run([FF, '-y', '-v', 'error', '-loop', '1', '-i', src,
             '-vf', zi + ',format=yuv420p', '-frames:v', str(n), '-r', str(FPS), '-an',
             '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', out])
    else:
        vf = ('scale=%d:%d:force_original_aspect_ratio=increase,crop=%d:%d:(iw-ow)/2:(ih-oh)/2+%d,'
              'setsar=1,format=yuv420p' % (int(W * z), int(H * z), W, H, int(yb * H * 0.08)))
        run([FF, '-y', '-v', 'error', '-ss', str(s.get('in', 0)), '-t', str(dur), '-i', src,
             '-vf', vf, '-r', str(FPS), '-an', '-c:v', 'libx264', '-preset', 'veryfast',
             '-crf', '18', out])
    segs.append(out)

lista = os.path.join(tmp, 'lista.txt')
open(lista, 'w').write(''.join("file '%s'\n" % s for s in segs))
cuerpo = os.path.join(tmp, 'cuerpo.mp4')
run([FF, '-y', '-v', 'error', '-f', 'concat', '-safe', '0', '-i', lista,
     '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-r', str(FPS), '-an', cuerpo])

# ---------------------------------------------------------------- 1b) subtitulos de la voz
def ts(x):
    x = max(0.0, x)
    return '%d:%02d:%05.2f' % (int(x // 3600), int(x % 3600 // 60), x % 60)


def norm(w): return re.sub(r'[^\w]', '', w.lower())


def escribir_subs(ruta_vo, ruta_guion, destino):
    """Alinea la transcripcion con el guion escrito y escribe el .ass de 3 palabras."""
    from faster_whisper import WhisperModel
    import difflib
    model = WhisperModel('small', device='cpu', compute_type='int8')
    segs, _ = model.transcribe(ruta_vo, language='es', word_timestamps=True)
    wd = [(w.start, w.end, w.word.strip()) for s in segs for w in s.words]
    sw = open(ruta_guion).read().split()
    a, b = [norm(x[2]) for x in wd], [norm(x) for x in sw]
    vw = []
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if op == 'equal':
            vw += [(wd[i1 + k][0], wd[i1 + k][1], sw[j1 + k]) for k in range(i2 - i1)]
    if not vw: return False
    HI = P.get('hi', '&H003CB3F2&')        # ambar #F2B33C en BGR: la palabra que suena
    cab = ('[Script Info]\nScriptType: v4.00+\nPlayResX: %d\nPlayResY: %d\nWrapStyle: 0\n\n'
           '[V4+ Styles]\nFormat: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, '
           'OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, '
           'Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, '
           'MarginV, Encoding\n'
           'Style: C,Montserrat ExtraBold,%d,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,'
           '0,0,0,0,100,100,0,0,1,9,5,5,60,60,0,1\n\n'
           '[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, '
           'Effect, Text' % (W, H, P.get('subs_fs', 92)))
    ass = [cab]
    def limpia(w): return w.replace('…', '').strip(' ,;:"“”').upper()
    chunks, cur = [], []
    for x in vw:
        cur.append(x)
        if len(cur) == P.get('words', 3) or re.search(r'[.?!…]$', x[2]):
            chunks.append(cur); cur = []
    if cur: chunks.append(cur)
    capy = P.get('capy', 1330)
    for ci, ch in enumerate(chunks):
        nxt = chunks[ci + 1][0][0] if ci + 1 < len(chunks) else ch[-1][1] + 0.4
        for wi, (s, e, w) in enumerate(ch):
            e2 = ch[wi + 1][0] if wi + 1 < len(ch) else min(nxt, ch[-1][1] + 0.5)
            pop = '{\\fscx116\\fscy116\\t(0,90,\\fscx100\\fscy100)}' if wi == 0 else ''
            txt = pop + ' '.join(('{\\1c%s}' % HI) + limpia(x[2]) + '{\\r}' if j == wi
                                 else limpia(x[2]) for j, x in enumerate(ch))
            ass.append('Dialogue: 0,%s,%s,C,,0,0,0,,{\\pos(%d,%d)}%s'
                       % (ts(s), ts(e2), W // 2, capy, txt))
    open(destino, 'w').write('\n'.join(ass) + '\n')
    return True


subs = None
if P.get('vo') and P.get('subs', True):
    sp = os.path.join(tmp, 'subs.ass')
    guion = F(P.get('guion') or P['vo'].replace('.wav', '.txt'))
    if escribir_subs(F(P['vo']), guion, sp):
        subs = sp

# ---------------------------------------------------------------- 2) carteles
ins, filtros, prev = ['-i', cuerpo], [], '0:v'
for i, c in enumerate(P.get('caps', [])):
    p = os.path.join(tmp, 'cap%d.png' % i)
    {'caja': png_caja, 'sticker': png_sticker}.get(c.get('tipo'), png_cartel)(c, p)
    ins += ['-i', p]
    filtros.append("[%s][%d:v]overlay=0:0:enable='between(t,%s,%s)'[v%d]"
                   % (prev, i + 1, c['t0'], c['t1'], i))
    prev = 'v%d' % i

dur = sum(s['dur'] for s in P['segments'])
mus = F(P['music'])
ins += ['-i', mus]
idx_mus = len(P.get('caps', [])) + 1
salida_mus = '[a]' if not P.get('vo') else '[mu]'
filtros.append('[%d:a]atrim=%s:%s,asetpts=N/SR/TB,volume=%s,afade=t=in:st=0:d=0.5,'
               'afade=t=out:st=%.2f:d=0.9%s'
               % (idx_mus, P.get('music_in', 0), P.get('music_in', 0) + dur,
                  P.get('music_vol', 0.62), dur - 0.9, salida_mus))
if P.get('vo'):
    # con locucion la cama baja y se mezcla sin normalizar (si no, amix le come el nivel a la voz)
    ins += ['-i', F(P['vo'])]
    filtros.append('[%d:a]aresample=48000,volume=%s[vz]' % (idx_mus + 1, P.get('vo_vol', 1.0)))
    filtros.append('[vz][mu]amix=inputs=2:duration=longest:normalize=0[a]')

if subs:
    filtros.append('[%s]ass=%s:fontsdir=%s[vsub]' % (prev, subs, FD))
    prev = 'vsub'

run([FF, '-y', '-v', 'error'] + ins + ['-filter_complex', ';'.join(filtros),
     '-map', '[%s]' % prev, '-map', '[a]', '-t', str(dur),
     '-c:v', 'libx264', '-preset', 'medium', '-crf', '19', '-pix_fmt', 'yuv420p',
     '-c:a', 'aac', '-b:a', '160k', '-movflags', '+faststart', OUT])
print('listo', OUT, round(dur, 2), 's')
