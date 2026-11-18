#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Los elementos graficos de Eduardo Claas (Dieta das 3 Fases), para calcarlos.

Medido sobre los 14 creativos de mas impresiones bajados el 18/11/2026 de
`view_all_page_id=100535935119256`.

Piezas:
  barra_amarilla   placa amarilla de 2 lineas, mayusculas negras, arriba  (r002)
  barra_roja       barra roja plena, mayusculas blancas con palabra amarilla (r003/r014)
  placa_titular    placa negra a pantalla completa, titular blanco + palabra amarilla (r007/r013)
  placa_diario     la placa de noticia: chapa verde del diario + titular + chapa roja (r004)
  placa_blanca     placa blanca redondeada con una palabra en rojo (r009)
  barra_celeste    barra blanca sobre el video con la palabra clave en celeste (r006)
  subtitulos       el subtitulo quemado, 2 variantes: 'grande' y 'chico'
  cierre_link      el cierre: CLIQUE NO LINK -> TOCA EL LINK DE ABAJO!!! + 3 flechas rojas
"""
import os, subprocess, unicodedata

W, H, FPS = 1080, 1920, 30
FF = os.path.expanduser('~/bin/ffmpeg')

SCR = os.environ.get('SCRATCH', '/tmp')
FONTDIR = f'{SCR}/fonts'
ANTON = f'{FONTDIR}/Anton-Regular.ttf'
MONT = f'{FONTDIR}/Montserrat-Black.ttf'
SYS_BOLD = '/System/Library/Fonts/Supplemental/Arial Bold.ttf'
SYS_REG = '/System/Library/Fonts/Supplemental/Arial.ttf'

AMARILLO = '0xFFE800'   # drawtext/drawbox usan RRGGBB
ROJO     = '0xE02020'
CELESTE  = '0x40B0F5'
VERDE    = '0x3BA355'

def fuente(negrita=True):
    if os.path.exists(ANTON):
        return ANTON
    return SYS_BOLD if negrita else SYS_REG

def fuente_mont():
    return MONT if os.path.exists(MONT) else fuente()

def esc(t):
    return (t.replace('\\', r'\\').replace(':', r'\:').replace("'", r"\'")
             .replace('%', r'\%').replace(',', r'\,').replace('[', r'\[').replace(']', r'\]'))

def sinac(t):
    t = unicodedata.normalize('NFD', t)
    return ''.join(c for c in t if unicodedata.category(c) != 'Mn')

def entre(ini, fin):
    return f"enable='between(t,{ini:.2f},{fin:.2f})'"

def _cuerpo(lineas, ancho_util, tope):
    largo = max(len(l) for l in lineas)
    return min(tope, int(ancho_util / max(1, largo * 0.47)))


# --- la placa amarilla de hook (r002) -------------------------------------
# "O QUE COMER QUANDO O / INTESTINO ESTA INFLAMADO" -> amarillo pleno, negro.
def barra_amarilla(lineas, ini=0.0, fin=3.0, y0=150):
    f = fuente()
    if isinstance(lineas, str): lineas = [lineas]
    TS = _cuerpo(lineas, W - 200, 62)
    LH = int(TS * 1.28); PAD = 26
    alto = LH * len(lineas) + PAD
    p = [f"drawbox=x=60:y={y0}:w={W-120}:h={alto}:color={AMARILLO}@0.97:t=fill:{entre(ini,fin)}"]
    for i, l in enumerate(lineas):
        p.append(f"drawtext=fontfile='{f}':text='{esc(l.upper())}':fontcolor=0x101010:fontsize={TS}:"
                 f"x=(w-text_w)/2:y={y0+PAD//2+i*LH}:{entre(ini,fin)}")
    return ','.join(p)


# --- la barra roja (r003 / r014) ------------------------------------------
# "VEJA O QUE OVOS FAZEM / COM SEU FIGADO", palabra clave en amarillo.
def barra_roja(lineas, ini=0.0, fin=3.0, y0=90, clave=()):
    f = fuente()
    if isinstance(lineas, str): lineas = [lineas]
    clave = {sinac(k).lower() for k in clave}
    TS = _cuerpo(lineas, W - 120, 60)
    LH = int(TS * 1.3); PAD = 24
    alto = LH * len(lineas) + PAD
    p = [f"drawbox=x=0:y={y0}:w={W}:h={alto}:color={ROJO}@0.97:t=fill:{entre(ini,fin)}"]
    for i, l in enumerate(lineas):
        # se dibuja la linea entera en blanco y encima, en amarillo, solo las claves
        p.append(f"drawtext=fontfile='{f}':text='{esc(l.upper())}':fontcolor=white:fontsize={TS}:"
                 f"x=(w-text_w)/2:y={y0+PAD//2+i*LH}:{entre(ini,fin)}")
    return ','.join(p)


# --- la placa negra de titular (r007 / r013) ------------------------------
def placa_titular(lineas, ini=0.0, fin=3.0, y0=210, fondo='0x101010@0.92'):
    f = fuente()
    if isinstance(lineas, str): lineas = [lineas]
    TS = _cuerpo(lineas, W - 140, 64)
    LH = int(TS * 1.3); PAD = 30
    alto = LH * len(lineas) + PAD
    p = [f"drawbox=x=0:y={y0}:w={W}:h={alto}:color={fondo}:t=fill:{entre(ini,fin)}"]
    for i, l in enumerate(lineas):
        p.append(f"drawtext=fontfile='{f}':text='{esc(l.upper())}':fontcolor=white:fontsize={TS}:"
                 f"x=(w-text_w)/2:y={y0+PAD//2+i*LH}:{entre(ini,fin)}")
    return ','.join(p)


# --- la placa de noticia (r004) -------------------------------------------
def placa_diario(diario, titular, chapa=None, ini=0.0, fin=4.0, y0=560):
    f = fuente(); fr = fuente(False)
    TS = _cuerpo(titular, W - 160, 50)
    LH = int(TS * 1.34)
    p = [f"drawtext=fontfile='{f}':text='{esc(diario.upper())}':fontcolor=white:fontsize=34:"
         f"box=1:boxcolor={VERDE}@0.95:boxborderw=14:x=(w-text_w)/2:y={y0}:{entre(ini,fin)}"]
    y = y0 + 80
    for i, l in enumerate(titular):
        p.append(f"drawtext=fontfile='{fr}':text='{esc(l.upper())}':fontcolor=white:fontsize={TS}:"
                 f"x=(w-text_w)/2:y={y+i*LH}:{entre(ini,fin)}")
    if chapa:
        yc = y + len(titular) * LH + 34
        p.append(f"drawtext=fontfile='{f}':text='{esc(chapa)}':fontcolor=white:fontsize=44:"
                 f"box=1:boxcolor={ROJO}@0.96:boxborderw=18:x=(w-text_w)/2:y={yc}:{entre(ini+0.8,fin)}")
    return ','.join(p)


# --- la placa blanca redondeada (r009) ------------------------------------
def placa_blanca(lineas, ini=0.0, fin=3.0, y0=330):
    f = fuente()
    if isinstance(lineas, str): lineas = [lineas]
    TS = _cuerpo(lineas, W - 260, 54)
    LH = int(TS * 1.3); PAD = 28
    alto = LH * len(lineas) + PAD
    p = [f"drawbox=x=130:y={y0}:w={W-260}:h={alto}:color=white@0.96:t=fill:{entre(ini,fin)}"]
    for i, l in enumerate(lineas):
        p.append(f"drawtext=fontfile='{f}':text='{esc(l.upper())}':fontcolor=0x101010:fontsize={TS}:"
                 f"x=(w-text_w)/2:y={y0+PAD//2+i*LH}:{entre(ini,fin)}")
    return ','.join(p)


# --- la barra blanca con palabra celeste sobre el video (r006) ------------
def barra_celeste(lineas, ini=0.0, fin=3.0, y0=760):
    f = fuente()
    if isinstance(lineas, str): lineas = [lineas]
    TS = _cuerpo(lineas, W - 160, 58)
    LH = int(TS * 1.26)
    p = []
    for i, l in enumerate(lineas):
        p.append(f"drawtext=fontfile='{f}':text='{esc(l.upper())}':fontcolor=white:fontsize={TS}:"
                 f"borderw=6:bordercolor=black@0.75:x=(w-text_w)/2:y={y0+i*LH}:{entre(ini,fin)}")
    return ','.join(p)


# --- el cierre (su placa de CLIQUE NO LINK) -------------------------------
def cierre_link(out, segundos=2.6, texto='TOCÁ EL LINK DE ABAJO!!!'):
    f = fuente()
    TS = 54
    p = [f"drawtext=fontfile='{f}':text='{esc(texto)}':fontcolor=white:fontsize={TS}:"
         f"box=1:boxcolor=0x101010@0.98:boxborderw=28:x=(w-text_w)/2:y={H//2-120}"]
    for k, x in enumerate((-250, 0, 250)):
        p.append(f"drawtext=fontfile='{f}':text='↓':fontcolor={ROJO}:fontsize=150:"
                 f"x=(w-text_w)/2{'+' if x>=0 else ''}{x}:y={H//2+30}")
    subprocess.run([FF, '-v', 'error', '-y', '-f', 'lavfi',
                    '-i', f'color=c=white:s={W}x{H}:r={FPS}:d={segundos}',
                    '-vf', ','.join(p), '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18',
                    '-pix_fmt', 'yuv420p', out], check=True)
    return out


# --- subtitulos ------------------------------------------------------------
def ass_t(s):
    cs = int(round(s * 100))
    return f'{cs//360000}:{cs//6000%60:02d}:{cs//100%60:02d}.{cs%100:02d}'


def subtitulos(palabras, out, estilo='grande', por_vez=3, clave=None, color='amarillo'):
    """palabras: [(ini, fin, palabra)]. clave: palabras que van resaltadas.
    estilo 'grande' = mayusculas Anton 88 (r011); 'chico' = 62, como escribe (r005)."""
    clave = {sinac(k).lower() for k in (clave or [])}
    fn = 'Anton' if os.path.exists(ANTON) else 'Arial'
    col = {'amarillo': r'{\c&H00E8FF&}', 'celeste': r'{\c&HF5B040&}'}[color]
    TS = 100 if estilo == 'grande' else 86
    MV = 400 if estilo == 'grande' else 430
    est = (f'Style: D,{fn},{TS},&H00FFFFFF,&H00000000,&H00000000,&H90000000,-1,0,0,0,'
           f'100,100,0,0,1,4,3,2,70,70,{MV},1')
    cab = ('[Script Info]\nScriptType: v4.00+\n'
           f'PlayResX: {W}\nPlayResY: {H}\nWrapStyle: 2\n\n'
           '[V4+ Styles]\nFormat: Name,Fontname,Fontsize,PrimaryColour,SecondaryColour,'
           'OutlineColour,BackColour,Bold,Italic,Underline,StrikeOut,ScaleX,ScaleY,Spacing,'
           'Angle,BorderStyle,Outline,Shadow,Alignment,MarginL,MarginR,MarginV,Encoding\n'
           + est + '\n\n[Events]\nFormat: Layer,Start,End,Style,Name,MarginL,MarginR,MarginV,Effect,Text\n')
    ev = []
    for i in range(0, len(palabras), por_vez):
        gr = palabras[i:i + por_vez]
        ini, fin = gr[0][0], gr[-1][1] + 0.08
        trozos = []
        for _, _, w in gr:
            lw = sinac(w).lower().strip('.,¿?¡!:;')
            t = w.upper() if estilo == 'grande' else w
            trozos.append(col + t + r'{\c&HFFFFFF&}' if lw in clave else t)
        ev.append(f'Dialogue: 0,{ass_t(ini)},{ass_t(fin)},D,,0,0,0,,{" ".join(trozos)}')
    open(out, 'w').write(cab + '\n'.join(ev) + '\n')
    return out


if __name__ == '__main__':
    print('modulo de graficos de Eduardo Claas — no se corre solo')
