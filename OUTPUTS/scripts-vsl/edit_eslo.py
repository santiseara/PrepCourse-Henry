#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Monta el formato "¿ESTO O ESTO?" de Fausto Almeida (su creativo de 0:51).

Estructura medida en su video:
  0,0 – 4,8   comida a pantalla completa + título "¿ESTO O ESTO?" y la aclaración
  4,8 – 38,4  cinco pares: comida arriba, comida abajo, cartel blanco con el nombre,
              cruz roja en la mala y tilde verde + marco verde en la buena
  38,4 – 43,8 el shot rojo a pantalla completa
  43,8 – fin  el avatar solo, con el botón amarillo y los chevrones

El avatar se ve SIEMPRE adelante: va recortado (Robust Video Matting) encima de todo.

Uso: SCRATCH=... python3 edit_eslo.py plan.json
"""
import json, os, re, subprocess, sys

SCR = os.environ.get('SCRATCH', '/tmp')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('SCRATCH', SCR)
import gfx_fausto as G
import gfx_eslo as E

FF = os.path.expanduser('~/bin/ffmpeg')
W, H, FPS = 1080, 1920, 30
MUS = os.path.expanduser('~/Downloads/u_6niyix0m9h-musica-de-suspense-335486.mp3.mpeg')
RVM = f'{SCR}/rvm_mobilenetv3_fp32.onnx'


def run(c):
    r = subprocess.run(c, capture_output=True, text=True)
    if r.returncode:
        sys.stderr.write(' '.join(str(x) for x in c[:16]) + '\n' + r.stderr[-1800:] + '\n')
        raise SystemExit(f'ffmpeg fallo ({r.returncode})')
    return r


def dur(f):
    s = subprocess.run([FF, '-i', f], capture_output=True, text=True).stderr
    m = re.search(r'Duration: (\d+):(\d+):([\d.]+)', s)
    if not m:
        raise SystemExit(f'no pude leer {f}')
    h, mi, se = m.groups()
    return int(h) * 3600 + int(mi) * 60 + float(se)


def bandas(mp4):
    import tempfile
    tmp = tempfile.mktemp(suffix='.raw')
    subprocess.run([FF, '-nostdin', '-loglevel', 'error', '-ss', '3', '-i', mp4,
                    '-frames:v', '1', '-vf', f'scale=120:{H},format=gray',
                    '-f', 'rawvideo', tmp], capture_output=True)
    try:
        d = open(tmp, 'rb').read()
    except OSError:
        return 0, 0
    finally:
        if os.path.exists(tmp): os.remove(tmp)
    filas = [d[i*120:(i+1)*120] for i in range(len(d)//120)]
    if not filas: return 0, 0
    liso = lambda f: (max(f) - min(f)) < 10
    arr = 0
    while arr < len(filas) and liso(filas[arr]): arr += 1
    ab = 0
    while ab < len(filas) - arr and liso(filas[len(filas)-1-ab]): ab += 1
    if arr + ab < 40 or (len(filas) - arr - ab) < 400:
        return 0, 0
    return arr, ab


_wm = None
def palabras(f):
    global _wm
    if _wm is None:
        from faster_whisper import WhisperModel
        _wm = WhisperModel(os.environ.get('WHISPER_MODEL', 'base'),
                           device='cpu', compute_type='int8')
    segs, _ = _wm.transcribe(f, language='es', word_timestamps=True)
    return [(w.start, w.end, w.word.strip()) for s in segs for w in (s.words or []) if w.word.strip()]


def encajar(ws, texto):
    """Pone las palabras del GUION sobre los tiempos del transcriptor.

    Whisper escribe lo que le parece ("mal medidas no hacen nada" por "mal medido no
    hace nada", "30" por "treinta"), y ese texto es el que se quema en pantalla. Acá se
    alinean las dos listas y se queda el guion, que es lo que realmente se dice.
    """
    import difflib
    gw = texto.split()
    if not gw or not ws:
        return ws
    na = [G.sinac(w).lower().strip('.,¿?¡!:;') for _, _, w in ws]
    nb = [G.sinac(w).lower().strip('.,¿?¡!:;') for w in gw]
    sm = difflib.SequenceMatcher(a=na, b=nb, autojunk=False)
    out = []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == 'equal':
            for k in range(i2 - i1):
                out.append((ws[i1 + k][0], ws[i1 + k][1], gw[j1 + k]))
        elif tag == 'replace':
            t0, t1 = ws[i1][0], ws[i2 - 1][1]
            n = j2 - j1
            paso = (t1 - t0) / max(1, n)
            for k in range(n):
                out.append((t0 + k * paso, t0 + (k + 1) * paso, gw[j1 + k]))
        elif tag == 'insert':
            # palabras que el transcriptor se comió: se reparten en el hueco
            t0 = out[-1][1] if out else (ws[0][0] if ws else 0.0)
            t1 = ws[i1][0] if i1 < len(ws) else t0 + 0.4 * (j2 - j1)
            if t1 <= t0:
                t1 = t0 + 0.25 * (j2 - j1)
            paso = (t1 - t0) / max(1, j2 - j1)
            for k in range(j2 - j1):
                out.append((t0 + k * paso, t0 + (k + 1) * paso, gw[j1 + k]))
        # 'delete' = el transcriptor oyó algo que el guion no tiene: se descarta
    return out


def ancla(ws, frase, desde=0.0):
    """Primer segundo en que arranca `frase` (normalizada) después de `desde`."""
    obj = [G.sinac(x).lower().strip('.,¿?¡!:;') for x in frase.split()]
    for i in range(len(ws)):
        if ws[i][0] < desde:
            continue
        cand = [G.sinac(w).lower().strip('.,¿?¡!:;') for _, _, w in ws[i:i+len(obj)]]
        if cand == obj:
            return ws[i][0]
    raise SystemExit(f'  no encontré el ancla "{frase}" después de {desde:.1f}s')


def recorte(av, out):
    """Avatar con alfa (persona recortada) usando Robust Video Matting."""
    if os.path.exists(out) and os.path.getsize(out) > 100_000:
        return out
    if not os.path.exists(RVM):
        raise SystemExit(f'  falta el modelo de recorte: {RVM}')
    masc = out + '.mask.mp4'
    aqui = os.path.dirname(os.path.abspath(__file__))
    r = subprocess.run(['python3', f'{aqui}/matte.py', av, RVM, masc, '540'],
                       capture_output=True, text=True)
    if r.returncode or not os.path.exists(masc):
        sys.stderr.write(r.stdout[-800:] + r.stderr[-1200:] + '\n')
        raise SystemExit('  falló el recorte (matte.py)')
    run([FF, '-v', 'error', '-y', '-i', av, '-i', masc, '-filter_complex',
         f'[0:v]scale={W}:{H},setsar=1[v];[1:v]scale={W}:{H},format=gray[m];'
         f'[v][m]alphamerge,format=yuva420p[o]',
         '-map', '[o]', '-c:v', 'qtrle', '-an', out])
    return out


def montar(plan):
    out = plan['salida']
    T = out + '_tmp'
    os.makedirs(T, exist_ok=True)
    print(f"=== {plan['nombre']} ===", flush=True)

    # 1. cuerpo: el avatar a 1,20
    sp = plan.get('speed', 1.20)
    av = plan['avatar']
    arr, ab = bandas(av)
    pre = f'crop={W}:{H-arr-ab}:0:{arr},' if (arr or ab) else ''
    if pre:
        print(f'  recorto banda del render: {arr}px arriba, {ab}px abajo', flush=True)
    cuerpo = f'{T}/cuerpo.mp4'
    run([FF, '-v', 'error', '-y', '-i', av, '-filter_complex',
         f'[0:v]{pre}scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},setsar=1,'
         f'setpts=PTS/{sp},fps={FPS}[v];[0:a]atempo={sp},aresample=48000[a]',
         '-map', '[v]', '-map', '[a]', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18',
         '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-ac', '2', cuerpo])
    DC = dur(cuerpo)
    print(f'  cuerpo: {DC:.1f}s', flush=True)

    # 2. anclas reales de la voz (con el guion encajado encima, si lo hay)
    ws = palabras(cuerpo)
    if plan.get('guion'):
        ws = encajar(ws, open(plan['guion']).read().strip())
    corte = []
    t = 0.0
    for p in plan['pares']:
        t = ancla(ws, p['ancla'], t)
        tv = ancla(ws, p['ancla_veredicto'], t + 0.2)
        corte.append((t, tv, p))
        t = tv
    t_shot = ancla(ws, plan['ancla_shot'], corte[-1][1] + 0.2)
    t_cta = ancla(ws, plan['ancla_cta'], t_shot + 0.2)
    fin_pares = t_shot
    print('  pares en: ' + ', '.join(f'{a:.1f}/{b:.1f}' for a, b, _ in corte), flush=True)
    print(f'  shot {t_shot:.1f}s · cta {t_cta:.1f}s', flush=True)

    # 3. el avatar recortado
    cut = recorte(cuerpo, f'{T}/cutout.mov')

    # 4. armado en una sola pasada
    marcas = E.marcas_png()
    ent = [cuerpo, cut, plan['apertura'], plan['shot']]
    for _, _, p in corte:
        ent += [p['arriba']['vis'], p['abajo']['vis']]
    ent += [marcas['cruz'], marcas['tilde']]
    cmd = [FF, '-v', 'error', '-y']
    for e in ent:
        cmd += ['-i', e]
    I_CUT, I_APE, I_SHOT = 1, 2, 3
    I_PAR = 4
    I_CRUZ = I_PAR + 2 * len(corte)
    I_TILDE = I_CRUZ + 1

    f = []
    # escalados
    f.append(f'[{I_APE}:v]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H}[ape]')
    f.append(f'[{I_SHOT}:v]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H}[shot]')
    for k in range(len(corte)):
        f.append(f'[{I_PAR+2*k}:v]scale={W}:{E.PA_H}:force_original_aspect_ratio=increase,'
                 f'crop={W}:{E.PA_H}[pa{k}]')
        f.append(f'[{I_PAR+2*k+1}:v]scale={E.PB_W}:{E.PB_H}:force_original_aspect_ratio=increase,'
                 f'crop={E.PB_W}:{E.PB_H}[pb{k}]')

    cur = '[0:v]'
    n = 0
    def paso(expr, nuevo):
        nonlocal cur, n
        f.append(f'{cur}{expr}{nuevo}')
        cur = nuevo
    # apertura y shot a pantalla completa
    f.append(f'{cur}[ape]overlay=0:0:enable=\'between(t,0,{corte[0][0]:.2f})\'[v0]'); cur = '[v0]'
    f.append(f'{cur}[shot]overlay=0:0:enable=\'between(t,{t_shot:.2f},{t_cta:.2f})\'[v1]'); cur = '[v1]'
    # los pares
    for k, (a, b, p) in enumerate(corte):
        fin = corte[k+1][0] if k + 1 < len(corte) else fin_pares
        f.append(f'{cur}[pa{k}]overlay=0:{E.PA_Y}:enable=\'between(t,{a:.2f},{fin:.2f})\'[a{k}]')
        cur = f'[a{k}]'
        f.append(f'{cur}[pb{k}]overlay={E.PB_X}:{E.PB_Y}:enable=\'between(t,{a:.2f},{fin:.2f})\'[b{k}]')
        cur = f'[b{k}]'
    # marco verde + carteles + marcas
    dibujos = []
    for k, (a, b, p) in enumerate(corte):
        fin = corte[k+1][0] if k + 1 < len(corte) else fin_pares
        ga = p['arriba'].get('gana'); gb = p['abajo'].get('gana')
        if gb:
            for d in range(E.BORDE):
                dibujos.append(f"drawbox=x={E.PB_X-d}:y={E.PB_Y-d}:w={E.PB_W+2*d}:h={E.PB_H+2*d}:"
                               f"color={E.VERDE}:t=1:{G.entre(b, fin)}")
        if ga:
            for d in range(E.BORDE):
                dibujos.append(f"drawbox=x={-d}:y={E.PA_Y-d}:w={W+2*d}:h={E.PA_H+2*d}:"
                               f"color={E.VERDE}:t=1:{G.entre(b, fin)}")
        dibujos.append(E.chip(p['arriba']['txt'], 40, E.PA_Y + 22, a, fin))
        dibujos.append(E.chip(p['abajo']['txt'], 56, E.PB_Y + E.PB_H - 96, a, fin))
        dibujos.append(E.letra_o(a, fin))
    f.append(f'{cur}' + ','.join(dibujos) + '[vg]')
    cur = '[vg]'
    # las marcas (PNG) entran con el veredicto
    for k, (a, b, p) in enumerate(corte):
        fin = corte[k+1][0] if k + 1 < len(corte) else fin_pares
        for lado, (clave, yy) in (('arriba', ('arriba', E.PA_Y + 12)), ('abajo', ('abajo', E.PB_Y + E.PB_H - 106))):
            q = p[clave]
            idx = I_TILDE if q.get('gana') else I_CRUZ
            xx = 40 + len(q['txt']) * 21 + 70 if clave == 'arriba' else 56 + len(q['txt']) * 21 + 70
            f.append(f'{cur}[{idx}:v]overlay={xx}:{yy}:enable=\'between(t,{b:.2f},{fin:.2f})\''
                     f'[m{k}{clave}]')
            cur = f'[m{k}{clave}]'

    # recién ahora el avatar recortado: chico, abajo a la derecha, adelante de todo
    # (en su video ocupa ~58 % del alto; a tamaño completo taparía las dos comidas).
    ESC = plan.get('escala_avatar', 0.58)
    AW, AH = int(W * ESC) // 2 * 2, int(H * ESC) // 2 * 2
    AX = int(plan.get('centro_avatar', 0.72) * W - AW / 2)
    AY = H - AH
    f.append(f'[{I_CUT}:v]scale={AW}:{AH}[cut]')
    f.append(f"{cur}[cut]overlay={AX}:{AY}:format=auto:enable='lt(t,{t_cta:.2f})'[vc]")
    cur = '[vc]'
    # título de apertura + botón final
    bot = E.boton_amarillo_png(plan.get('boton', 'MIRÁ EL PASO A PASO'))
    cmd += ['-i', bot]
    I_BOT = len(ent)
    f.append(f'{cur}' + E.titulo_eso(plan['titulo'][0], plan['titulo'][1], 0.35, corte[0][0]) + '[vt]')
    cur = '[vt]'
    f.append(f'{cur}[{I_BOT}:v]overlay=0:{H-430}:enable=\'gte(t,{t_cta:.2f})\'[vf]')
    cur = '[vf]'

    cmd += ['-filter_complex', ';'.join(f), '-map', cur, '-map', '0:a',
            '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p',
            '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-ac', '2', f'{T}/compuesto.mp4']
    run(cmd)

    # 5. subtítulos con la palabra clave en amarillo
    ass = E.subtitulos_amarillo(ws, f'{T}/sub.ass', plan.get('por_vez', 3),
                                plan.get('clave'), plan.get('sub_y', 1010))
    conSub = f'{T}/consub.mp4'
    run([FF, '-v', 'error', '-y', '-i', f'{T}/compuesto.mp4', '-vf',
         f"subtitles='{ass}':fontsdir='{G.FONTDIR}'", '-c:v', 'libx264', '-preset', 'veryfast',
         '-crf', '18', '-pix_fmt', 'yuv420p', '-c:a', 'copy', conSub])

    # 6. música por debajo
    DV = dur(conSub)
    run([FF, '-v', 'error', '-y', '-i', conSub, '-stream_loop', '-1', '-i', MUS,
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
    print(f'  LISTO {out}  {dur(out):.1f}s  {os.path.getsize(out)/1e6:.1f} MB', flush=True)
    return out


if __name__ == '__main__':
    pl = json.load(open(sys.argv[1]))
    for p in (pl if isinstance(pl, list) else [pl]):
        montar(p)
