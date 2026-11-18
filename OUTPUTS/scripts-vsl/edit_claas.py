#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dieta de las 3 Fases — monta un anuncio con la estructura exacta de Eduardo Claas.

Su estructura, medida en los 14 creativos de mas impresiones (18/11/2026):
  HOOK    0 -> 2-4 s   b-roll o render 3D con la barra/placa encima
  CUERPO               el avatar a camara, con inserts de b-roll y tramos de PANTALLA PARTIDA
  CIERRE  2,6 s        placa blanca con TOCA EL LINK DE ABAJO!!! y tres flechas rojas

Reglas que no se rompen:
  . despues de loudnorm va SIEMPRE aresample=48000, y el muxeo lleva -ar 48000 -ac 2
  . las rutas del demuxer concat van con os.path.abspath
  . NUNCA se repite una visual dentro del mismo anuncio
  . se verifica que el mp4 existe y pesa antes de decir que esta listo

Uso: python3 edit_claas.py plan.json
"""
import json, os, re, subprocess, sys, unicodedata

SCR = os.environ.get('SCRATCH', '/tmp')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('SCRATCH', SCR)
import gfx_claas as G

FF = os.path.expanduser('~/bin/ffmpeg')
W, H, FPS = 1080, 1920, 30
BASE = os.path.expanduser('~/Desktop/dieta-3-fases/work')
VIS = [f'{BASE}/broll/veo', f'{BASE}/broll/sel', f'{BASE}/broll/clips_tk', f'{BASE}/broll/clips_med']
MUS = os.environ.get('MUSICA', '')


def run(c):
    r = subprocess.run(c, capture_output=True, text=True)
    if r.returncode:
        sys.stderr.write(' '.join(c[:14]) + '\n' + r.stderr[-1600:] + '\n')
        raise SystemExit(f'ffmpeg fallo ({r.returncode})')
    return r


def dur(f):
    r = subprocess.run([FF, '-i', f], capture_output=True, text=True).stderr
    m = re.search(r'Duration: (\d+):(\d+):([\d.]+)', r)
    if not m:
        raise SystemExit(f'no pude leer la duracion de {f}')
    h, mi, s = m.groups()
    return int(h) * 3600 + int(mi) * 60 + float(s)


def buscar(nombre):
    for d in VIS:
        for e in ('', '.mp4', '.mov', '.png', '.jpg', '.jpeg', '.webp'):
            p = os.path.join(d, nombre + e)
            if os.path.exists(p):
                return p
    return None


def bandas(mp4):
    """Franjas lisas que a veces deja HeyGen arriba y abajo del lienzo 9:16.
    18/11/2026: con los renders de Avatar IV a 720x1280 el detector da FALSO POSITIVO
    (301 px arriba y abajo sobre un cuadro lleno), porque el escalado a 120x1920 alisa
    los degrade del fondo. Esos renders ya vienen 9:16 limpios, asi que se apaga."""
    return 0, 0
    import tempfile
    tmp = tempfile.mktemp(suffix='.raw')
    subprocess.run([FF, '-nostdin', '-loglevel', 'error', '-ss', '5', '-i', mp4,
                    '-frames:v', '1', '-vf', f'scale=120:{H},format=gray',
                    '-f', 'rawvideo', tmp], capture_output=True)
    try:
        d = open(tmp, 'rb').read()
    except OSError:
        return 0, 0
    finally:
        if os.path.exists(tmp): os.remove(tmp)
    W2 = 120
    filas = [d[i*W2:(i+1)*W2] for i in range(len(d)//W2)]
    if not filas: return 0, 0
    liso = lambda f: (max(f) - min(f)) < 10
    arr = 0
    while arr < len(filas) and liso(filas[arr]): arr += 1
    ab = 0
    while ab < len(filas) - arr and liso(filas[len(filas)-1-ab]): ab += 1
    if arr + ab < 40 or (len(filas) - arr - ab) < 400:
        return 0, 0
    return arr, ab


def plano(src, L, out, off=None, zoom=True):
    """Un plano de L segundos a 1080x1920."""
    esc = f'scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},setsar=1,fps={FPS}'
    if src.lower().endswith(('.mp4', '.mov', '.webm')):
        dc = dur(src)
        o = off if off is not None else max(0.0, min(dc - L - 0.1, dc * 0.12))
        run([FF, '-v', 'error', '-y', '-ss', f'{o:.2f}', '-t', f'{L:.2f}', '-i', src,
             '-an', '-vf', esc, '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18',
             '-pix_fmt', 'yuv420p', out])
    else:
        z = (f",scale=w='{W}*(1.0+0.09*t/{L:.2f})':h=-1:eval=frame,"
             f"crop={W}:{H}:(iw-{W})/2:(ih-{H})/2") if zoom else ''
        run([FF, '-v', 'error', '-y', '-loop', '1', '-t', f'{L:.2f}', '-i', src, '-an',
             '-vf', esc + z + f',setsar=1,fps={FPS}', '-c:v', 'libx264', '-preset', 'veryfast',
             '-crf', '18', '-pix_fmt', 'yuv420p', out])
    return out


def partida(avatar, visual, t0, L, out):
    """Su firma: el render 3D arriba (40 % del alto) y el avatar abajo (60 %)."""
    HA, HB = int(H * 0.42), H - int(H * 0.42)
    dc = dur(visual)
    o = max(0.0, min(dc - L - 0.1, dc * 0.1))
    run([FF, '-v', 'error', '-y',
         '-ss', f'{t0:.3f}', '-t', f'{L:.3f}', '-i', avatar,
         '-ss', f'{o:.2f}', '-t', f'{L:.3f}', '-stream_loop', '0', '-i', visual,
         '-filter_complex',
         f'[1:v]scale={W}:{HA}:force_original_aspect_ratio=increase,crop={W}:{HA},setsar=1,fps={FPS}[a];'
         f'[0:v]scale={W}:{HB}:force_original_aspect_ratio=increase,crop={W}:{HB},setsar=1,fps={FPS}[b];'
         f'[a][b]vstack=inputs=2,setsar=1[v]',
         '-map', '[v]', '-an', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18',
         '-pix_fmt', 'yuv420p', out])
    return out


def concat(partes, out):
    lst = out + '.txt'
    open(lst, 'w').write(''.join(f"file '{os.path.abspath(p)}'\n" for p in partes))
    run([FF, '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', lst, '-c', 'copy', out])
    return out


def sinac(t):
    t = unicodedata.normalize('NFD', t)
    return ''.join(c for c in t if unicodedata.category(c) != 'Mn')


_wm = None
def palabras(f):
    global _wm
    if _wm is None:
        from faster_whisper import WhisperModel
        _wm = WhisperModel('base', device='cpu', compute_type='int8')
    segs, _ = _wm.transcribe(f, language='es', word_timestamps=True)
    return [(w.start, w.end, w.word.strip()) for s in segs for w in (s.words or []) if w.word.strip()]


def montar(plan):
    nom, out = plan['nombre'], plan['salida']
    T = out + '_tmp'
    os.makedirs(T, exist_ok=True)
    print(f'=== {nom} ===', flush=True)

    # 1. el cuerpo: el avatar, acelerado
    sp = plan.get('speed', 1.20)
    av = plan['avatar']
    cuerpo = f'{T}/cuerpo.mp4'
    arr, ab = bandas(av)
    # bandas() mide sobre el lienzo ya escalado a 1080x1920: primero se escala y despues se recorta
    post = f'crop={W}:{H-arr-ab}:0:{arr},scale={W}:{H},' if (arr or ab) else ''
    if post:
        print(f'  recorto banda del render: {arr}px arriba, {ab}px abajo', flush=True)
    run([FF, '-v', 'error', '-y', '-i', av, '-filter_complex',
         f'[0:v]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},{post}setsar=1,'
         f'setpts=PTS/{sp},fps={FPS}[v];[0:a]atempo={sp},aresample=48000[a]',
         '-map', '[v]', '-map', '[a]', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18',
         '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-ac', '2', cuerpo])
    DC = dur(cuerpo)
    print(f'  cuerpo: {DC:.1f}s', flush=True)

    # 2. inserts y pantallas partidas sobre el cuerpo, sin repetir visual
    trozos_def = sorted(plan.get('inserts', []) + plan.get('partidas', []), key=lambda x: x['t'])
    usados = [i['vis'] for i in trozos_def]
    faltan = [v for v in usados if not buscar(v)]
    if faltan:
        raise SystemExit(f'  FALTAN visuales: {sorted(set(faltan))}')
    if len(usados) != len(set(usados)):
        rep = sorted({v for v in usados if usados.count(v) > 1})
        raise SystemExit(f'  visual REPETIDA dentro del anuncio: {rep}')

    cap = cuerpo
    if trozos_def:
        trozos, cursor = [], 0.0
        for k, i in enumerate(trozos_def, 1):
            t0 = max(0.0, min(i['t'], DC))
            L = min(i.get('dura', 1.8), max(0.0, DC - t0))
            if L <= 0.05:
                continue
            if t0 > cursor + 0.04:
                tr = f'{T}/av{k}.mp4'
                run([FF, '-v', 'error', '-y', '-ss', f'{cursor:.3f}', '-t', f'{t0-cursor:.3f}',
                     '-i', cuerpo, '-an', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18',
                     '-pix_fmt', 'yuv420p', '-vf', f'fps={FPS},scale={W}:{H},setsar=1', tr])
                trozos.append(tr)
            src = buscar(i['vis'])
            if i.get('modo') == 'partida':
                trozos.append(partida(cuerpo, src, t0, L, f'{T}/par{k}.mp4'))
            else:
                trozos.append(plano(src, L, f'{T}/ins{k}.mp4'))
            cursor = t0 + L
        if cursor < DC - 0.04:
            tr = f'{T}/avfin.mp4'
            run([FF, '-v', 'error', '-y', '-ss', f'{cursor:.3f}', '-i', cuerpo, '-an',
                 '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p',
                 '-vf', f'fps={FPS},scale={W}:{H},setsar=1', tr])
            trozos.append(tr)
        mudo = concat(trozos, f'{T}/conins_mudo.mp4')
        cap = f'{T}/conins.mp4'
        run([FF, '-v', 'error', '-y', '-i', mudo, '-i', cuerpo, '-map', '0:v', '-map', '1:a',
             '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-ac', '2',
             '-shortest', cap])

    # 3. el hook
    hk = plan.get('hook')
    partes = []
    if hk:
        src = buscar(hk['vis'])
        if not src:
            raise SystemExit(f'  falta la visual del hook: {hk["vis"]}')
        L = hk.get('dura', 2.6)
        hp = plano(src, L, f'{T}/hook_raw.mp4', off=hk.get('off'))
        gfx = []
        if hk.get('amarilla'):  gfx.append(G.barra_amarilla(hk['amarilla'], 0, L))
        if hk.get('roja'):      gfx.append(G.barra_roja(hk['roja'], 0, L))
        if hk.get('titular'):   gfx.append(G.placa_titular(hk['titular'], 0, L))
        if hk.get('blanca'):    gfx.append(G.placa_blanca(hk['blanca'], 0, L))
        if hk.get('barra'):     gfx.append(G.barra_celeste(hk['barra'], 0, L, 700))
        if hk.get('diario'):    gfx.append(G.placa_diario(hk['diario'][0], hk['diario'][1],
                                                          hk['diario'][2] if len(hk['diario']) > 2 else None, 0, L))
        hf = f'{T}/hook.mp4'
        run([FF, '-v', 'error', '-y', '-i', hp, '-vf', ','.join(gfx) if gfx else 'null',
             '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p',
             '-an', hf])
        partes.append(hf)

    # 4. graficos sobre el cuerpo
    gfx = []
    for b in plan.get('barras', []):
        gfx.append(G.barra_celeste(b['txt'], b['ini'], b['fin'], b.get('y', 760)))
    for p in plan.get('placas', []):
        gfx.append(G.placa_titular(p['txt'], p['ini'], p['fin'], p.get('y', 210)))

    # 5. subtitulos
    ws = palabras(cap)
    ass = G.subtitulos(ws, f'{T}/sub.ass', plan.get('sub', 'grande'),
                       plan.get('por_vez', 3), plan.get('clave'), plan.get('color', 'amarillo'))
    vf = (','.join(gfx) + ',' if gfx else '') + f"subtitles='{ass}':fontsdir='{G.FONTDIR}'"
    conGfx = f'{T}/cuerpo_gfx.mp4'
    run([FF, '-v', 'error', '-y', '-i', cap, '-vf', vf, '-c:v', 'libx264', '-preset', 'veryfast',
         '-crf', '18', '-pix_fmt', 'yuv420p', '-c:a', 'copy', conGfx])
    partes.append(conGfx)

    # 6. el cierre
    partes.append(G.cierre_link(f'{T}/cierre.mp4', plan.get('cierre_seg', 2.6)))

    # 7. pegar
    mudos = []
    for k, p in enumerate(partes):
        m = f'{T}/m{k}.mp4'
        run([FF, '-v', 'error', '-y', '-i', p, '-an', '-c:v', 'libx264', '-preset', 'veryfast',
             '-crf', '18', '-pix_fmt', 'yuv420p', '-vf', f'fps={FPS},scale={W}:{H},setsar=1', m])
        mudos.append(m)
    vfinal = concat(mudos, f'{T}/video.mp4')
    DV = dur(vfinal)

    off = dur(partes[0]) if hk else 0.0
    aud = f'{T}/audio.m4a'
    if MUS and os.path.exists(MUS):
        filtro = (f'[0:a]adelay={int(off*1000)}|{int(off*1000)},'
                  f'loudnorm=I=-16:TP=-1.5:LRA=11,aresample=48000,apad=whole_dur={DV:.2f}[v];'
                  f'[1:a]volume=0.13,afade=t=in:st=0:d=1.2,'
                  f'afade=t=out:st={max(0.1,DV-1.6):.2f}:d=1.4,aresample=48000[m];'
                  f'[v][m]amix=inputs=2:duration=first:dropout_transition=0,aresample=48000[a]')
        run([FF, '-v', 'error', '-y', '-i', cap, '-stream_loop', '-1', '-i', MUS,
             '-filter_complex', filtro, '-map', '[a]', '-t', f'{DV:.2f}',
             '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-ac', '2', aud])
    else:
        run([FF, '-v', 'error', '-y', '-i', cap, '-filter_complex',
             f'[0:a]adelay={int(off*1000)}|{int(off*1000)},loudnorm=I=-16:TP=-1.5:LRA=11,'
             f'aresample=48000,apad=whole_dur={DV:.2f}[a]', '-map', '[a]', '-t', f'{DV:.2f}',
             '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-ac', '2', aud])

    run([FF, '-v', 'error', '-y', '-i', vfinal, '-i', aud, '-map', '0:v', '-map', '1:a',
         '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-ac', '2',
         '-t', f'{DV:.2f}', out])

    # 8. control
    if not os.path.exists(out) or os.path.getsize(out) < 200_000:
        raise SystemExit(f'  EL ARCHIVO NO SE GENERO O PESA NADA: {out}')
    info = subprocess.run([FF, '-i', out], capture_output=True, text=True).stderr
    if '48000 Hz' not in info:
        raise SystemExit(f'  AUDIO MAL: no dice 48000 Hz')
    if f'{W}x{H}' not in info:
        raise SystemExit(f'  RESOLUCION MAL: no es {W}x{H}')
    print(f'  LISTO {out}  {dur(out):.1f}s  {os.path.getsize(out)/1e6:.1f} MB', flush=True)
    return out


if __name__ == '__main__':
    planes = json.load(open(sys.argv[1]))
    if isinstance(planes, dict):
        planes = [planes]
    for p in planes:
        montar(p)
