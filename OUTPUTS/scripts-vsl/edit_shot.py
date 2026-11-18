#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Monta el formato "EL SHOT" de Fausto Almeida (su creativo de 0:24).

  · el avatar en la cocina con el vaso en la mano, a pantalla completa
  · placa negra de tres líneas FIJA arriba (blanca / amarilla / blanca)
  · subtítulo en mayúsculas, blanco con la palabra clave en amarillo
  · un par de inserts cortos y el botón amarillo con chevrones al final

Uso: SCRATCH=... python3 edit_shot.py plan.json
"""
import json, os, re, subprocess, sys

SCR = os.environ.get('SCRATCH', '/tmp')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('SCRATCH', SCR)
import gfx_fausto as G
import gfx_eslo as E
import edit_eslo as X          # reuso dur/bandas/palabras/ancla/run

FF = os.path.expanduser('~/bin/ffmpeg')
W, H, FPS = 1080, 1920, 30
MUS = os.path.expanduser('~/Downloads/u_6niyix0m9h-musica-de-suspense-335486.mp3.mpeg')


def montar(plan):
    out = plan['salida']
    T = out + '_tmp'
    os.makedirs(T, exist_ok=True)
    print(f"=== {plan['nombre']} ===", flush=True)

    sp = plan.get('speed', 1.20)
    av = plan['avatar']
    arr, ab = X.bandas(av)
    pre = f'crop={W}:{H-arr-ab}:0:{arr},' if (arr or ab) else ''
    if pre:
        print(f'  recorto banda del render: {arr}px arriba, {ab}px abajo', flush=True)
    cuerpo = f'{T}/cuerpo.mp4'
    X.run([FF, '-v', 'error', '-y', '-i', av, '-filter_complex',
           f'[0:v]{pre}scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},setsar=1,'
           f'setpts=PTS/{sp},fps={FPS}[v];[0:a]atempo={sp},aresample=48000[a]',
           '-map', '[v]', '-map', '[a]', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18',
           '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-ac', '2', cuerpo])
    DC = X.dur(cuerpo)
    print(f'  cuerpo: {DC:.1f}s', flush=True)

    ws = X.palabras(cuerpo)
    if plan.get('guion'):
        ws = X.encajar(ws, open(plan['guion']).read().strip())
    ins = []
    for i in plan.get('inserts', []):
        t = X.ancla(ws, i['ancla'])
        ins.append({'t': t, 'vis': i['vis'], 'dura': i.get('dura', 1.8)})
    vistos = [i['vis'] for i in ins]
    if len(vistos) != len(set(vistos)):
        raise SystemExit(f'  visual REPETIDA dentro del anuncio: {vistos}')
    print('  inserts en: ' + ', '.join(f"{i['t']:.1f}" for i in ins), flush=True)

    # inserts: se cortan y se pegan (el overlay con PTS desplazado no muestra el clip)
    cap = cuerpo
    if ins:
        trozos, cursor = [], 0.0
        for k, i in enumerate(sorted(ins, key=lambda x: x['t']), 1):
            t0 = max(0.0, min(i['t'], DC))
            L = min(i['dura'], max(0.0, DC - t0))
            if L <= 0.05:
                continue
            if t0 > cursor + 0.04:
                tr = f'{T}/av{k}.mp4'
                X.run([FF, '-v', 'error', '-y', '-ss', f'{cursor:.3f}', '-t', f'{t0-cursor:.3f}',
                       '-i', cuerpo, '-an', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18',
                       '-pix_fmt', 'yuv420p', '-vf', f'fps={FPS},scale={W}:{H},setsar=1', tr])
                trozos.append(tr)
            z = (f",scale=w='{W}*(1.0+0.08*t/{L:.2f})':h=-1:eval=frame,"
                 f"crop={W}:{H}:(iw-{W})/2:(ih-{H})/2")
            p = f'{T}/ins{k}.mp4'
            X.run([FF, '-v', 'error', '-y', '-loop', '1', '-t', f'{L:.2f}', '-i', i['vis'], '-an',
                   '-vf', f'scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},setsar=1'
                          f'{z},setsar=1,fps={FPS}',
                   '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p', p])
            trozos.append(p)
            cursor = t0 + L
        if cursor < DC - 0.04:
            tr = f'{T}/avfin.mp4'
            X.run([FF, '-v', 'error', '-y', '-ss', f'{cursor:.3f}', '-i', cuerpo, '-an',
                   '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p',
                   '-vf', f'fps={FPS},scale={W}:{H},setsar=1', tr])
            trozos.append(tr)
        lst = f'{T}/lista.txt'
        open(lst, 'w').write(''.join(f"file '{os.path.abspath(p)}'\n" for p in trozos))
        mudo = f'{T}/mudo.mp4'
        X.run([FF, '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', lst, '-c', 'copy', mudo])
        cap = f'{T}/conins.mp4'
        X.run([FF, '-v', 'error', '-y', '-i', mudo, '-i', cuerpo, '-map', '0:v', '-map', '1:a',
               '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-ac', '2',
               '-shortest', cap])

    # placa fija de arriba + botón amarillo al final
    DV = X.dur(cap)
    t_cta = X.ancla(ws, plan['ancla_cta'])
    bot = E.boton_amarillo_png(plan.get('boton', 'MIRÁ EL PASO A PASO'))
    placa = E.placa_tres(*plan['placa'])
    comp = f'{T}/comp.mp4'
    X.run([FF, '-v', 'error', '-y', '-i', cap, '-i', bot, '-filter_complex',
           f"[0:v]{placa}[p];[p][1:v]overlay=0:{H-430}:enable='gte(t,{t_cta:.2f})'[v]",
           '-map', '[v]', '-map', '0:a', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18',
           '-pix_fmt', 'yuv420p', '-c:a', 'copy', comp])

    ass = E.subtitulos_amarillo(ws, f'{T}/sub.ass', plan.get('por_vez', 3),
                                plan.get('clave'), plan.get('sub_y', 1300), ts=72, mayus=True)
    conSub = f'{T}/consub.mp4'
    X.run([FF, '-v', 'error', '-y', '-i', comp, '-vf',
           f"subtitles='{ass}':fontsdir='{G.FONTDIR}'", '-c:v', 'libx264', '-preset', 'veryfast',
           '-crf', '18', '-pix_fmt', 'yuv420p', '-c:a', 'copy', conSub])

    DV = X.dur(conSub)
    X.run([FF, '-v', 'error', '-y', '-i', conSub, '-stream_loop', '-1', '-i', MUS,
           '-filter_complex',
           f'[0:a]loudnorm=I=-16:TP=-1.5:LRA=11,aresample=48000,apad=whole_dur={DV:.2f}[v];'
           f'[1:a]volume=0.14,afade=t=in:st=0:d=1.2,afade=t=out:st={max(0.1,DV-1.6):.2f}:d=1.4,'
           f'aresample=48000[m];[v][m]amix=inputs=2:duration=first:dropout_transition=0,'
           f'aresample=48000[a]',
           '-map', '0:v', '-map', '[a]', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k',
           '-ar', '48000', '-ac', '2', '-t', f'{DV:.2f}', out])

    if not os.path.exists(out) or os.path.getsize(out) < 200_000:
        raise SystemExit(f'  NO SE GENERO: {out}')
    info = subprocess.run([FF, '-i', out], capture_output=True, text=True).stderr
    if '48000 Hz' not in info or f'{W}x{H}' not in info:
        raise SystemExit(f'  MAL EL MUXEO:\n{info[-700:]}')
    print(f'  LISTO {out}  {X.dur(out):.1f}s  {os.path.getsize(out)/1e6:.1f} MB', flush=True)
    return out


if __name__ == '__main__':
    pl = json.load(open(sys.argv[1]))
    for p in (pl if isinstance(pl, list) else [pl]):
        montar(p)
