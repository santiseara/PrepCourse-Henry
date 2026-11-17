#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Hígado Liviano v5 — monta un anuncio con la estructura exacta de Fausto Almeida.

Estructura de todos sus creativos:
  HOOK    0 → 2-5 s   imagen shock o b-roll, con barra roja / placa blanca encima
  CUERPO              el avatar a cámara, con inserts de b-roll encima cada N segundos
  CIERRE  2,6 s       placa negra con el botón azul MÁS INFORMACIÓN

Reglas que no se rompen (wiki §10 y §11):
  · después de loudnorm va SIEMPRE aresample=48000, y el muxeo lleva -ar 48000 -ac 2
  · las rutas del demuxer concat van con os.path.abspath
  · NUNCA se repite una visual dentro del mismo anuncio: si faltan, corta y avisa
  · se verifica que el mp4 existe y pesa antes de decir que está listo

Uso:
  python3 edit_fausto.py plan.json
"""
import json, os, re, subprocess, sys, unicodedata

SCR = os.environ.get('SCRATCH',
    '/private/tmp/claude-501/-Users-santiagoseara-PrepCourse-Henry/'
    '1212d877-5027-42d7-a10c-9f1c0e139bc8/scratchpad')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('SCRATCH', SCR)
import gfx_fausto as G

FF = os.path.expanduser('~/bin/ffmpeg')
W, H, FPS = 1080, 1920, 30
BASE = os.path.expanduser('~/Desktop/higado-liviano/work')
VIS = f'{BASE}/visuales_v5'
MUS = os.path.expanduser('~/Downloads/u_6niyix0m9h-musica-de-suspense-335486.mp3.mpeg')


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
    """Busca una visual por nombre en las subcarpetas de visuales_v5."""
    for sub in ('shock', 'organos', 'ecografias', 'broll', 'desayunos', ''):
        d = os.path.join(VIS, sub) if sub else VIS
        for e in ('', '.mp4', '.png', '.jpg', '.jpeg', '.webp'):
            p = os.path.join(d, nombre + e)
            if os.path.exists(p):
                return p
    return None


def plano(src, L, out, zoom=True):
    """Un plano de L segundos, 1080x1920. Foto -> push-in; clip -> tal cual."""
    esc = f'scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},setsar=1,fps={FPS}'
    if src.lower().endswith(('.mp4', '.mov', '.webm')):
        dc = dur(src)
        off = max(0.0, min(dc - L - 0.1, dc * 0.15))
        run([FF, '-v', 'error', '-y', '-ss', f'{off:.2f}', '-t', f'{L:.2f}', '-i', src,
             '-an', '-vf', esc, '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18',
             '-pix_fmt', 'yuv420p', out])
    else:
        # zoompan tiene un bug con d=; el push-in va con scale eval=frame
        z = (f",scale=w='{W}*(1.0+0.09*t/{L:.2f})':h=-1:eval=frame,"
             f"crop={W}:{H}:(iw-{W})/2:(ih-{H})/2") if zoom else ''
        run([FF, '-v', 'error', '-y', '-loop', '1', '-t', f'{L:.2f}', '-i', src, '-an',
             '-vf', esc + z + f',setsar=1,fps={FPS}', '-c:v', 'libx264', '-preset', 'veryfast',
             '-crf', '18', '-pix_fmt', 'yuv420p', out])
    return out


def concat(partes, out):
    lst = out + '.txt'
    # el demuxer concat resuelve las rutas RELATIVAS AL ARCHIVO DE LISTA
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


# ---------------------------------------------------------------------------
def montar(plan):
    nom = plan['nombre']
    out = plan['salida']
    T = out + '_tmp'
    os.makedirs(T, exist_ok=True)
    print(f'=== {nom} ===', flush=True)

    # --- 1. el cuerpo: el avatar, acelerado ---
    sp = plan.get('speed', 1.20)
    av = plan['avatar']
    cuerpo = f'{T}/cuerpo.mp4'
    run([FF, '-v', 'error', '-y', '-i', av, '-filter_complex',
         f'[0:v]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},setsar=1,'
         f'setpts=PTS/{sp},fps={FPS}[v];[0:a]atempo={sp},aresample=48000[a]',
         '-map', '[v]', '-map', '[a]', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18',
         '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-ac', '2', cuerpo])
    DC = dur(cuerpo)
    print(f'  cuerpo: {DC:.1f}s', flush=True)

    # --- 2. los inserts de b-roll sobre el cuerpo, SIN repetir ninguno ---
    ins = plan.get('inserts', [])
    faltan = [i['vis'] for i in ins if not buscar(i['vis'])]
    if faltan:
        raise SystemExit(f'  FALTAN visuales (no se tapa con lo que haya): {faltan}')
    vistos = [i['vis'] for i in ins]
    if len(vistos) != len(set(vistos)):
        rep = [v for v in set(vistos) if vistos.count(v) > 1]
        raise SystemExit(f'  visual REPETIDA dentro del anuncio: {rep}')

    cap = cuerpo
    if ins:
        entradas = ['-i', cuerpo]
        filtros = []
        prev = '0:v'
        for k, i in enumerate(ins, 1):
            src = buscar(i['vis'])
            L = i.get('dura', 1.8)
            pl = plano(src, L, f'{T}/ins{k}.mp4')
            entradas += ['-i', pl]
            filtros.append(f"[{k}:v]scale={W}:{H},setsar=1[i{k}];"
                           f"[{prev}][i{k}]overlay=0:0:enable='between(t,{i['t']:.2f},{i['t']+L:.2f})'[o{k}]")
            prev = f'o{k}'
        cap = f'{T}/conins.mp4'
        run([FF, '-v', 'error', '-y'] + entradas + ['-filter_complex', ';'.join(filtros),
             '-map', f'[{prev}]', '-map', '0:a', '-c:v', 'libx264', '-preset', 'veryfast',
             '-crf', '18', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k',
             '-ar', '48000', '-ac', '2', cap])

    # --- 3. el hook: la visual de apertura con su barra/placa ---
    hk = plan.get('hook')
    partes = []
    if hk:
        src = buscar(hk['vis'])
        if not src:
            raise SystemExit(f'  falta la visual del hook: {hk["vis"]}')
        L = hk.get('dura', 2.4)
        hp = plano(src, L, f'{T}/hook_raw.mp4')
        gfx = []
        if hk.get('barra'):
            gfx.append(G.barra_roja(hk['barra'][0], hk['barra'][1], 0, L))
        if hk.get('placa'):
            gfx.append(G.placa_blanca(hk['placa'], 0, L))
        hf = f'{T}/hook.mp4'
        run([FF, '-v', 'error', '-y', '-i', hp, '-vf', ','.join(gfx) if gfx else 'null',
             '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p',
             '-an', hf])
        # el hook lleva el audio del cuerpo, así que se pega como video mudo adelante
        partes.append(hf)

    # --- 4. los gráficos sobre el cuerpo ---
    gfx = []
    for p in plan.get('puntajes', []):
        gfx.append(G.puntaje(p['n'], p['ini'], p['fin'], p.get('color', 'verde'),
                             p.get('x'), p.get('y', 330)))
    for c in plan.get('chapas', []):
        gfx.append(G.chapa_nombre(c['txt'], c['ini'], c['fin']))
    for t in plan.get('tachas', []):
        gfx.append(G.tacha_roja(t['txt'], t['ini'], t['fin']))
    for m in plan.get('mitos', []):
        gfx.append(G.placa_mito(m['txt'], m['ini'], m['fin'], sub=m.get('sub')))
    for n in plan.get('no', []):
        gfx.append(G.no_rojo(n['ini'], n['fin']))
    if plan.get('comentario'):
        c = plan['comentario']
        gfx.append(G.caja_comentario(c['usuario'], c['pregunta'], 0, c.get('fin', 2.4)))

    # --- 5. subtítulos alineados con la voz ---
    ws = palabras(cap)
    ass = G.subtitulos(ws, f'{T}/sub.ass', plan.get('sub', 'blanco'),
                       plan.get('por_vez', 3), plan.get('clave'))
    vf = (','.join(gfx) + ',' if gfx else '') + f"subtitles='{ass}':fontsdir='{G.FONTDIR}'"
    conGfx = f'{T}/cuerpo_gfx.mp4'
    run([FF, '-v', 'error', '-y', '-i', cap, '-vf', vf, '-c:v', 'libx264', '-preset', 'veryfast',
         '-crf', '18', '-pix_fmt', 'yuv420p', '-c:a', 'copy', conGfx])
    partes.append(conGfx)

    # --- 6. el cierre ---
    cierre = G.boton_final(f'{T}/cierre.mp4', plan.get('cierre_seg', 2.6))
    partes.append(cierre)

    # --- 7. pegar video, y audio con música ---
    mudos = []
    for k, p in enumerate(partes):
        m = f'{T}/m{k}.mp4'
        run([FF, '-v', 'error', '-y', '-i', p, '-an', '-c:v', 'libx264', '-preset', 'veryfast',
             '-crf', '18', '-pix_fmt', 'yuv420p', '-vf', f'fps={FPS},scale={W}:{H},setsar=1', m])
        mudos.append(m)
    vfinal = concat(mudos, f'{T}/video.mp4')
    DV = dur(vfinal)

    # audio: la voz del cuerpo, corrida por el largo del hook, + música de fondo
    off = dur(partes[0]) if hk else 0.0
    aud = f'{T}/audio.m4a'
    filtro = (f'[0:a]adelay={int(off*1000)}|{int(off*1000)},'
              f'loudnorm=I=-16:TP=-1.5:LRA=11,aresample=48000[v];'
              f'[1:a]volume=0.20,afade=t=in:st=0:d=1.2,'
              f'afade=t=out:st={max(0.1,DV-1.6):.2f}:d=1.4,aresample=48000[m];'
              f'[v][m]amix=inputs=2:duration=first:dropout_transition=0,aresample=48000[a]')
    run([FF, '-v', 'error', '-y', '-i', cap, '-stream_loop', '-1', '-i', MUS,
         '-filter_complex', filtro, '-map', '[a]', '-t', f'{DV:.2f}',
         '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-ac', '2', aud])

    run([FF, '-v', 'error', '-y', '-i', vfinal, '-i', aud, '-map', '0:v', '-map', '1:a',
         '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-ac', '2',
         '-shortest', out])

    # --- 8. control: existe, pesa, y el audio dice 48000 Hz ---
    if not os.path.exists(out) or os.path.getsize(out) < 200_000:
        raise SystemExit(f'  EL ARCHIVO NO SE GENERO O PESA NADA: {out}')
    info = subprocess.run([FF, '-i', out], capture_output=True, text=True).stderr
    if '48000 Hz' not in info:
        raise SystemExit(f'  AUDIO MAL: no dice 48000 Hz\n{info[-700:]}')
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
