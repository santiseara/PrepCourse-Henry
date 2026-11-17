#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Monta una mini novela de Hígado Liviano con las tomas de Veo 3.1.

Molde de las novelas de Fausto Almeida (r016 / r002):
  · planos largos, sin cortes rápidos
  · subtítulo blanco con sombra, 2-3 palabras, quemado
  · placa negra de salto temporal ("VEINTITRÉS AÑOS DESPUÉS")
  · cierre con el botón azul MÁS INFORMACIÓN
  · la música de suspenso bajita por debajo del diálogo

Cada toma de Veo trae su propio diálogo: el audio se usa tal cual, no se dobla.

Uso: python3 edit_novela.py novela.json
"""
import json, os, re, subprocess, sys

SCR = os.environ.get('SCRATCH',
    '/private/tmp/claude-501/-Users-santiagoseara-PrepCourse-Henry/'
    '1212d877-5027-42d7-a10c-9f1c0e139bc8/scratchpad')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('SCRATCH', SCR)
import gfx_fausto as G

FF = os.path.expanduser('~/bin/ffmpeg')
W, H, FPS = 1080, 1920, 30
MUS = os.path.expanduser('~/Downloads/u_6niyix0m9h-musica-de-suspense-335486.mp3.mpeg')


def run(c):
    r = subprocess.run(c, capture_output=True, text=True)
    if r.returncode:
        sys.stderr.write(' '.join(c[:12]) + '\n' + r.stderr[-1500:] + '\n')
        raise SystemExit(f'ffmpeg fallo ({r.returncode})')
    return r


def dur(f):
    r = subprocess.run([FF, '-i', f], capture_output=True, text=True).stderr
    m = re.search(r'Duration: (\d+):(\d+):([\d.]+)', r)
    if not m:
        raise SystemExit(f'no pude leer {f}')
    h, mi, s = m.groups()
    return int(h)*3600 + int(mi)*60 + float(s)


_wm = None
def palabras(f):
    global _wm
    if _wm is None:
        from faster_whisper import WhisperModel
        _wm = WhisperModel('base', device='cpu', compute_type='int8')
    segs, _ = _wm.transcribe(f, language='es', word_timestamps=True)
    return [(w.start, w.end, w.word.strip()) for s in segs for w in (s.words or []) if w.word.strip()]


def placa_negra(texto, segundos, out):
    """La placa de salto temporal: fondo negro, texto blanco, línea fina abajo."""
    f = G.fuente()
    filtro = (f"drawtext=fontfile='{f}':text='{G.esc(texto)}':fontcolor=white:fontsize=62:"
              f"x=(w-text_w)/2:y=(h-text_h)/2,"
              f"drawbox=x=(w-240)/2:y=(h/2)+60:w=240:h=3:color=white@0.8:t=fill")
    run([FF, '-v', 'error', '-y', '-f', 'lavfi',
         '-i', f'color=c=black:s={W}x{H}:r={FPS}:d={segundos}',
         '-f', 'lavfi', '-i', f'anullsrc=r=48000:cl=stereo:d={segundos}',
         '-vf', filtro, '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18',
         '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-ac', '2',
         '-shortest', out])
    return out


def montar(plan):
    nom = plan['nombre']
    out = plan['salida']
    T = out + '_tmp'
    os.makedirs(T, exist_ok=True)
    print(f'=== {nom} ===', flush=True)

    TOMAS = os.path.expanduser('~/Desktop/higado-liviano/work/novelas/tomas')
    piezas = []
    for i, item in enumerate(plan['orden']):
        if isinstance(item, dict):            # placa de salto temporal
            p = placa_negra(item['placa'], item.get('dura', 2.4), f'{T}/p{i:02d}.mp4')
            piezas.append(p); continue
        src = f'{TOMAS}/{item}.mp4'
        if not os.path.exists(src):
            raise SystemExit(f'  falta la toma {item}')
        p = f'{T}/t{i:02d}.mp4'
        run([FF, '-v', 'error', '-y', '-i', src, '-vf',
             f'scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},setsar=1,fps={FPS}',
             '-af', 'aresample=48000', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18',
             '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-ac', '2', p])
        piezas.append(p)

    # pegar todo
    lst = f'{T}/lista.txt'
    open(lst, 'w').write(''.join(f"file '{os.path.abspath(p)}'\n" for p in piezas))
    crudo = f'{T}/crudo.mp4'
    run([FF, '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', lst,
         '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-ac', '2', crudo])

    # el cierre
    cierre = f'{T}/cierre.mp4'
    G.boton_final(f'{T}/cierre_mudo.mp4', plan.get('cierre_seg', 2.8))
    run([FF, '-v', 'error', '-y', '-i', f'{T}/cierre_mudo.mp4', '-f', 'lavfi',
         '-i', f'anullsrc=r=48000:cl=stereo', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k',
         '-ar', '48000', '-ac', '2', '-shortest', cierre])
    lst2 = f'{T}/lista2.txt'
    open(lst2, 'w').write(f"file '{os.path.abspath(crudo)}'\nfile '{os.path.abspath(cierre)}'\n")
    pegado = f'{T}/pegado.mp4'
    run([FF, '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', lst2,
         '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-ac', '2', pegado])

    # subtítulos alineados con el diálogo de las propias tomas
    ws = palabras(pegado)
    ass = G.subtitulos(ws, f'{T}/sub.ass', 'caja', 3)
    conSub = f'{T}/consub.mp4'
    run([FF, '-v', 'error', '-y', '-i', pegado,
         '-vf', f"subtitles='{ass}':fontsdir='{G.FONTDIR}'",
         '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p',
         '-c:a', 'copy', conSub])

    # música de suspenso por debajo del diálogo
    DV = dur(conSub)
    run([FF, '-v', 'error', '-y', '-i', conSub, '-stream_loop', '-1', '-i', MUS,
         '-filter_complex',
         f'[0:a]loudnorm=I=-16:TP=-1.5:LRA=11,aresample=48000[v];'
         f'[1:a]volume=0.13,afade=t=in:st=0:d=1.5,'
         f'afade=t=out:st={max(0.1,DV-2.0):.2f}:d=1.8,aresample=48000[m];'
         f'[v][m]amix=inputs=2:duration=first:dropout_transition=0,aresample=48000[a]',
         '-map', '0:v', '-map', '[a]', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k',
         '-ar', '48000', '-ac', '2', '-t', f'{DV:.2f}', out])

    # control
    if not os.path.exists(out) or os.path.getsize(out) < 200_000:
        raise SystemExit(f'  NO SE GENERO: {out}')
    info = subprocess.run([FF, '-i', out], capture_output=True, text=True).stderr
    if '48000 Hz' not in info:
        raise SystemExit('  AUDIO MAL: no dice 48000 Hz')
    if f'{W}x{H}' not in info:
        raise SystemExit(f'  RESOLUCION MAL: no es {W}x{H}')
    print(f'  LISTO {out}  {dur(out):.1f}s  {os.path.getsize(out)/1e6:.1f} MB  48000 Hz', flush=True)
    return out


if __name__ == '__main__':
    planes = json.load(open(sys.argv[1]))
    if isinstance(planes, dict):
        planes = [planes]
    for p in planes:
        montar(p)
