#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Los elementos gráficos de Fausto Almeida, para replicarlos tal cual.

Cada función devuelve un trozo de filtergraph de ffmpeg (string) que se encadena
sobre el video. Todo medido sobre los 12 creativos bajados el 17/11/2026.

Piezas:
  barra_roja      la firma: dos líneas en mayúsculas sobre fondo rojo pleno, arriba
  placa_blanca    placa blanca redondeada arriba, para las frases largas
  puntaje         chapa `N/10` en verde (r001) o naranja (r013)
  chapa_nombre    `Rosa, 61` en chapa blanca arriba a la izquierda
  tacha_roja      la X roja gigante sobre un alimento
  placa_mito      `MITO 1 · VIENE DE LA COMIDA` en placa roja (r040)
  no_rojo         el `NO` rojo gigante sobre la doctora
  caja_comentario la caja de comentario de Instagram (r015)
  boton_final     placa negra + botón azul MÁS INFORMACIÓN
"""
import os, subprocess, unicodedata

W, H, FPS = 1080, 1920, 30
FF = os.path.expanduser('~/bin/ffmpeg')

SCR = os.environ.get('SCRATCH', '/tmp')
FONTDIR = f'{SCR}/fonts'
ANTON = f'{FONTDIR}/Anton-Regular.ttf'
# fuentes del sistema como respaldo
SYS_BOLD = '/System/Library/Fonts/Supplemental/Arial Bold.ttf'
SYS_REG = '/System/Library/Fonts/Supplemental/Arial.ttf'


def fuente(negrita=True):
    if os.path.exists(ANTON):
        return ANTON
    return SYS_BOLD if negrita else SYS_REG


def esc(t):
    """Escapa texto para drawtext."""
    return (t.replace('\\', r'\\').replace(':', r'\:').replace("'", r"\'")
             .replace('%', r'\%').replace(',', r'\,').replace('[', r'\[').replace(']', r'\]'))


def sinac(t):
    t = unicodedata.normalize('NFD', t)
    return ''.join(c for c in t if unicodedata.category(c) != 'Mn')


def entre(ini, fin):
    return f"enable='between(t,{ini:.2f},{fin:.2f})'"


# ---------------------------------------------------------------------------
# La barra roja: `MIRÁ LO QUE HACE LA BANANA / CON TU COLESTEROL`
# Medida en r005/r008/r040: ocupa el ancho entero, arranca en y≈0,
# dos líneas, mayúsculas, fondo rojo pleno (#D81E1E), texto blanco.
# La primera línea entra sola y la segunda aparece ~0,6 s después.
# ---------------------------------------------------------------------------
def barra_roja(l1, l2, ini=0.0, fin=2.4, desfase=0.6):
    f = fuente()
    # Anton es condensada: ~0.46 del cuerpo por caracter. Se achica si no entra.
    largo = max(len(l1), len(l2))
    TS = min(58, int((W - 80) / max(1, largo * 0.47)))
    PAD = 20
    alto = TS + PAD * 2
    y1, y2 = 8, 8 + alto + 4
    p = []
    # línea 1 (fondo oscuro, no rojo: en el original la de arriba es gris oscuro)
    p.append(f"drawbox=x=0:y={y1}:w={W}:h={alto}:color=0x111111@0.92:t=fill:{entre(ini+desfase,fin)}")
    p.append(f"drawtext=fontfile='{f}':text='{esc(l1.upper())}':fontcolor=white:fontsize={TS}:"
             f"x=(w-text_w)/2:y={y1+PAD}:{entre(ini+desfase,fin)}")
    # línea 2 (la roja)
    p.append(f"drawbox=x=0:y={y2}:w={W}:h={alto}:color=0xD81E1E@0.97:t=fill:{entre(ini,fin)}")
    p.append(f"drawtext=fontfile='{f}':text='{esc(l2.upper())}':fontcolor=white:fontsize={TS}:"
             f"x=(w-text_w)/2:y={y2+PAD}:{entre(ini,fin)}")
    return ','.join(p)


# ---------------------------------------------------------------------------
# Placa blanca redondeada arriba (r011, r030, r013, r028)
# ---------------------------------------------------------------------------
def placa_blanca(lineas, ini=0.0, fin=3.6, y0=70):
    f = fuente()
    TS, LH = 46, 62
    if isinstance(lineas, str):
        lineas = [lineas]
    alto = LH * len(lineas) + 30
    p = [f"drawbox=x=50:y={y0}:w={W-100}:h={alto}:color=white@0.95:t=fill:{entre(ini,fin)}"]
    for i, l in enumerate(lineas):
        p.append(f"drawtext=fontfile='{f}':text='{esc(l)}':fontcolor=0x111111:fontsize={TS}:"
                 f"x=(w-text_w)/2:y={y0+15+i*LH}:{entre(ini,fin)}")
    return ','.join(p)


# ---------------------------------------------------------------------------
# Puntaje `5/10`. Verde en r001, naranja en r013. Entra con un pop.
# ---------------------------------------------------------------------------
def puntaje(n, ini, fin, color='verde', x=None, y=330):
    f = fuente()
    col = {'verde': '0x22C55E', 'naranja': '0xF97316'}[color]
    TS = 96
    xx = x if x is not None else '(w-text_w)/2'
    return (f"drawtext=fontfile='{f}':text='{esc(str(n))}/10':fontcolor={col}:fontsize={TS}:"
            f"borderw=5:bordercolor=black@0.55:x={xx}:y={y}:{entre(ini,fin)}")


# ---------------------------------------------------------------------------
# Chapa de nombre y edad: `Rosa, 61` (r013), blanca, arriba a la izquierda
# ---------------------------------------------------------------------------
def chapa_nombre(txt, ini, fin, x=60, y=150):
    f = fuente()
    TS = 44
    return (f"drawtext=fontfile='{f}':text='{esc(txt)}':fontcolor=0x111111:fontsize={TS}:"
            f"box=1:boxcolor=white@0.95:boxborderw=16:x={x}:y={y}:{entre(ini,fin)}")


# ---------------------------------------------------------------------------
# La X roja gigante sobre un alimento (r005) + la etiqueta abajo
# ---------------------------------------------------------------------------
def tacha_roja(etiqueta, ini, fin, grosor=26):
    """Dos líneas cruzadas con drawbox rotado no existe en ffmpeg, así que se
    arma con dos cajas finas rotadas vía geq sería caro: se usa el truco de
    dibujar la X con dos 'drawtext' de una barra Unicode escalada."""
    f = fuente()
    # X grande centrada
    p = [f"drawtext=fontfile='{f}':text='X':fontcolor=0xD81E1E@0.92:fontsize=620:"
         f"x=(w-text_w)/2:y=(h-text_h)/2-120:{entre(ini,fin)}"]
    if etiqueta:
        TS = 50
        y = H - 640
        p.append(f"drawtext=fontfile='{f}':text='{esc(etiqueta.upper())}':fontcolor=white:fontsize={TS}:"
                 f"box=1:boxcolor=0xD81E1E@0.95:boxborderw=16:x=(w-text_w)/2:y={y}:{entre(ini,fin)}")
    return ','.join(p)


# ---------------------------------------------------------------------------
# Placa de mito, roja, redondeada (r040): `MITO 1 · VIENE DE LA COMIDA`
# ---------------------------------------------------------------------------
def placa_mito(txt, ini, fin, y=700, sub=None):
    f = fuente()
    TS, BW = 46, 18
    p = [f"drawtext=fontfile='{f}':text='{esc(txt.upper())}':fontcolor=white:fontsize={TS}:"
         f"box=1:boxcolor=0xD81E1E@0.96:boxborderw={BW}:x=(w-text_w)/2:y={y}:{entre(ini,fin)}"]
    if sub:
        y2 = y + TS + BW * 2 + 14
        p.append(f"drawtext=fontfile='{f}':text='{esc(sub.upper())}':fontcolor=white:fontsize={TS}:"
                 f"box=1:boxcolor=0xD81E1E@0.96:boxborderw={BW}:x=(w-text_w)/2:y={y2}:{entre(ini+0.9,fin)}")
    return ','.join(p)


# ---------------------------------------------------------------------------
# El `NO` rojo gigante sobre la doctora (r008, r015)
# ---------------------------------------------------------------------------
def no_rojo(ini, fin):
    f = fuente()
    return (f"drawtext=fontfile='{f}':text='NO':fontcolor=0xD81E1E:fontsize=240:"
            f"borderw=7:bordercolor=black@0.4:x=(w-text_w)/2:y=(h-text_h)/2:{entre(ini,fin)}")


# ---------------------------------------------------------------------------
# Caja de comentario de Instagram (r015)
# ---------------------------------------------------------------------------
def caja_comentario(usuario, pregunta, ini=0.0, fin=2.4, y0=60):
    f = fuente()
    TSu, TSp, PAD = 28, 40, 20
    lineas = []
    li = ''
    for p in pregunta.split():
        if len(li) + len(p) + 1 > 34:
            lineas.append(li); li = p
        else:
            li = (li + ' ' + p).strip()
    if li:
        lineas.append(li)
    alto = PAD * 2 + TSu + 14 + len(lineas) * (TSp + 8)
    out = [f"drawbox=x=50:y={y0}:w={W-100}:h={alto}:color=white@0.95:t=fill:{entre(ini,fin)}",
           f"drawtext=fontfile='{fuente(False)}':text='{esc('Respuesta a ' + usuario)}':"
           f"fontcolor=0x666666:fontsize={TSu}:x=110:y={y0+PAD}:{entre(ini,fin)}"]
    for i, l in enumerate(lineas):
        out.append(f"drawtext=fontfile='{f}':text='{esc(l)}':fontcolor=0x111111:fontsize={TSp}:"
                   f"x=(w-text_w)/2:y={y0+PAD+TSu+14+i*(TSp+8)}:{entre(ini,fin)}")
    return ','.join(out)


# ---------------------------------------------------------------------------
# El cierre: placa negra con el botón azul MÁS INFORMACIÓN
# ---------------------------------------------------------------------------
def boton_final(out, segundos=2.6, texto='MÁS INFORMACIÓN'):
    f = fuente()
    TS = 46
    filtro = (f"drawtext=fontfile='{f}':text='{esc(texto)}':fontcolor=white:fontsize={TS}:"
              f"box=1:boxcolor=0x2D7FF9@0.98:boxborderw=34:"
              f"x=(w-text_w)/2:y=(h-text_h)/2")
    subprocess.run([FF, '-v', 'error', '-y', '-f', 'lavfi',
                    '-i', f'color=c=black:s={W}x{H}:r={FPS}:d={segundos}',
                    '-vf', filtro, '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18',
                    '-pix_fmt', 'yuv420p', out], check=True)
    return out


# ---------------------------------------------------------------------------
# Subtítulo: las tres variantes que usa Fausto
#   'blanco'  — blanco liso con borde (cuerpo cocina)
#   'caja'    — blanco sobre caja negra (r022, r016)
#   'rojo'    — mayúsculas con la palabra clave en rojo (cuerpo doctora)
#   'podcast' — alterna amarillo/blanco por hablante (r028)
# Se devuelve un .ass, que es mucho más barato que mil drawtext.
# ---------------------------------------------------------------------------
def ass_t(s):
    cs = int(round(s * 100))
    return f'{cs//360000}:{cs//6000%60:02d}:{cs//100%60:02d}.{cs%100:02d}'


def subtitulos(palabras, out, estilo='blanco', por_vez=3, clave=None, hablantes=None):
    """palabras: [(ini, fin, palabra)].  clave: set de palabras que van en rojo."""
    clave = {sinac(k).lower() for k in (clave or [])}
    fn = 'Anton' if os.path.exists(ANTON) else 'Arial'
    if estilo == 'caja':
        est = f'Style: D,{fn},86,&H00FFFFFF,&H00000000,&H00000000,&HC0000000,-1,0,0,0,100,100,0,0,3,0,0,2,70,70,420,1'
    elif estilo == 'rojo':
        est = f'Style: D,{fn},88,&H00FFFFFF,&H00000000,&H00000000,&H90000000,-1,0,0,0,100,100,0,0,1,4,2,2,70,70,420,1'
    else:
        est = f'Style: D,{fn},86,&H00FFFFFF,&H00000000,&H00000000,&H90000000,-1,0,0,0,100,100,0,0,1,4,2,2,70,70,420,1'
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
            if estilo == 'rojo':
                t = w.upper()
                trozos.append(r'{\c&H0000D8&}' + t + r'{\c&HFFFFFF&}' if lw in clave else t)
            else:
                trozos.append(w)
        txt = ' '.join(trozos)
        if estilo == 'podcast' and hablantes:
            col = r'{\c&H00FFFF&}' if hablantes(ini) == 'b' else r'{\c&HFFFFFF&}'
            txt = col + txt
        ev.append(f'Dialogue: 0,{ass_t(ini)},{ass_t(fin)},D,,0,0,0,,{txt}')
    open(out, 'w').write(cab + '\n'.join(ev) + '\n')
    return out


if __name__ == '__main__':
    print('modulo de graficos de Fausto — no se corre solo')
