#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Renovación al estilo Fausto: un hook nuevo pegado ADELANTE del anuncio ganador.

El cuerpo validado no se toca (regla de [[renovacion-de-creativos]]): solo se le
antepone una visual nueva con su barra roja y su propia voz, que es exactamente lo
que hace él en r011 (frase propia -> "Mirá lo que hace la banana" -> el mismo cuerpo).

Uso: python3 ren_hook.py plan.json
"""
import json, os, re, subprocess, sys

SCR = os.environ.get('SCRATCH', '/tmp')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gfx_fausto as G

FF = os.path.expanduser('~/bin/ffmpeg')
W, H, FPS = 1080, 1920, 30
MUS = os.path.expanduser('~/Downloads/u_6niyix0m9h-musica-de-suspense-335486.mp3.mpeg')


def run(c):
    r = subprocess.run(c, capture_output=True, text=True)
    if r.returncode:
        sys.stderr.write(' '.join(c[:14]) + '\n' + r.stderr[-1600:] + '\n')
        raise SystemExit(f'ffmpeg fallo ({r.returncode})')
    return r


def dur(f):
    s = subprocess.run([FF, '-i', f], capture_output=True, text=True).stderr
    m = re.search(r'Duration: (\d+):(\d+):([\d.]+)', s)
    if not m:
        raise SystemExit(f'no pude leer {f}')
    h, mi, se = m.groups()
    return int(h) * 3600 + int(mi) * 60 + float(se)


def montar(p):
    out = p['salida']
    T = out + '_tmp'
    os.makedirs(T, exist_ok=True)
    print(f"=== {p['nombre']} ===", flush=True)

    base = p['base']
    for f in (base, p['visual'], p['voz']):
        if not os.path.exists(f):
            raise SystemExit(f'  falta {f}')

    sp = p.get('speed', 1.20)
    # 1. la voz del hook, acelerada
    voz = f'{T}/voz.m4a'
    run([FF, '-v', 'error', '-y', '-i', p['voz'], '-af',
         f'atempo={sp},loudnorm=I=-16:TP=-1.5:LRA=11,aresample=48000',
         '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-ac', '2', voz])
    DV = dur(voz) + p.get('cola', 0.35)
    print(f'  hook: {DV:.2f}s', flush=True)

    # 2. la visual del hook con push-in + la barra roja
    gfx = G.barra_roja(p['barra'][0], p['barra'][1], 0, DV)
    z = (f"scale=w='{W}*(1.0+0.09*t/{DV:.2f})':h=-1:eval=frame,"
         f"crop={W}:{H}:(iw-{W})/2:(ih-{H})/2")
    hook = f'{T}/hook.mp4'
    run([FF, '-v', 'error', '-y', '-loop', '1', '-t', f'{DV:.2f}', '-i', p['visual'], '-an',
         '-vf', f'scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},setsar=1,'
                f'{z},setsar=1,fps={FPS},{gfx}',
         '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p', hook])

    # 3. subtítulo del hook, alineado a su propia voz
    from faster_whisper import WhisperModel
    wm = WhisperModel('base', device='cpu', compute_type='int8')
    segs, _ = wm.transcribe(voz, language='es', word_timestamps=True)
    ws = [(w.start, w.end, w.word.strip()) for s in segs for w in (s.words or []) if w.word.strip()]
    ass = G.subtitulos(ws, f'{T}/sub.ass', p.get('sub', 'blanco'), 3)
    hooksub = f'{T}/hook_sub.mp4'
    run([FF, '-v', 'error', '-y', '-i', hook, '-vf',
         f"subtitles='{ass}':fontsdir='{G.FONTDIR}'", '-c:v', 'libx264', '-preset', 'veryfast',
         '-crf', '18', '-pix_fmt', 'yuv420p', '-an', hooksub])

    # 4. el audio del hook: voz + la misma cama musical, al mismo volumen que el resto
    aud = f'{T}/hook.m4a'
    run([FF, '-v', 'error', '-y', '-i', voz, '-stream_loop', '-1', '-i', MUS,
         '-filter_complex',
         f'[0:a]apad=whole_dur={DV:.2f},aresample=48000[v];'
         f'[1:a]volume=0.14,afade=t=in:st=0:d=1.0,aresample=48000[m];'
         f'[v][m]amix=inputs=2:duration=first:dropout_transition=0,aresample=48000[a]',
         '-map', '[a]', '-t', f'{DV:.2f}', '-c:a', 'aac', '-b:a', '192k',
         '-ar', '48000', '-ac', '2', aud])
    hookfin = f'{T}/hook_fin.mp4'
    run([FF, '-v', 'error', '-y', '-i', hooksub, '-i', aud, '-map', '0:v', '-map', '1:a',
         '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-ac', '2',
         '-t', f'{DV:.2f}', hookfin])

    # 5. el cuerpo ganador, normalizado a los mismos parámetros, y pegado atrás
    cuerpo = f'{T}/cuerpo.mp4'
    run([FF, '-v', 'error', '-y', '-i', base, '-vf', f'scale={W}:{H},setsar=1,fps={FPS}',
         '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p',
         '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-ac', '2', cuerpo])
    lst = f'{T}/lista.txt'
    open(lst, 'w').write(f"file '{os.path.abspath(hookfin)}'\nfile '{os.path.abspath(cuerpo)}'\n")
    run([FF, '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', lst,
         '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-ac', '2', out])

    # 6. control
    if not os.path.exists(out) or os.path.getsize(out) < 200_000:
        raise SystemExit(f'  NO SE GENERO: {out}')
    info = subprocess.run([FF, '-i', out], capture_output=True, text=True).stderr
    if '48000 Hz' not in info or f'{W}x{H}' not in info:
        raise SystemExit(f'  MAL EL MUXEO:\n{info[-700:]}')
    print(f'  LISTO {out}  {dur(out):.1f}s  {os.path.getsize(out)/1e6:.1f} MB', flush=True)
    return out


if __name__ == '__main__':
    pl = json.load(open(sys.argv[1]))
    for p in (pl if isinstance(pl, list) else [pl]):
        montar(p)
