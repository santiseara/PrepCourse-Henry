#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cabello Fuerte — replica anuncio por anuncio los creativos de Fernanda Lucas.

Reconstruye la MISMA linea de tiempo del original:
  · cada plano del original se conserva en su lugar, escalado por k = dur_nuestra / dur_original
  · los planos donde hablaba la presentadora se reemplazan por nuestro avatar de HeyGen
  · los planos de B-roll se reusan del original en 720p y se suben a 1080x1920
  · los subtitulos se rehacen en castellano con el estilo exacto de cada anuncio (gfx_cabello)
  · el audio es nuestra voz en off (Gemini TTS, ya acelerada)

Reglas que no se rompen:
  · despues de loudnorm va SIEMPRE aresample=48000, y el muxeo lleva -ar 48000 -ac 2
  · las rutas del demuxer concat van absolutas
  · se verifica que el mp4 existe y pesa antes de decir que esta listo

Uso: python3 edit_cabello.py plan.json
"""
import json, os, subprocess, sys, tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gfx_cabello as G

FF = os.path.expanduser('~/bin/ffmpeg')
W, H, FPS = 1080, 1920, 30
BASE = os.path.expanduser('~/Desktop/cabello-fuerte/work')


def run(c, mostrar=False):
    r = subprocess.run(c, capture_output=True, text=True)
    if r.returncode:
        sys.stderr.write(' '.join(str(x) for x in c[:18]) + '\n' + r.stderr[-1800:] + '\n')
        raise SystemExit(f'ffmpeg fallo ({r.returncode})')
    return r


def dur(f, defecto=None):
    import re
    s = subprocess.run([FF, '-i', f], capture_output=True, text=True).stderr
    m = re.search(r'Duration: (\d+):(\d+):([\d.]+)', s)
    if not m:
        # los planos de 1 o 2 cuadros del original a veces salen ilegibles
        if defecto is not None:
            return defecto
        raise SystemExit(f'no pude leer la duracion de {f}')
    h, mi, se = m.groups()
    return int(h) * 3600 + int(mi) * 60 + float(se)


# ------------------------------------------------------------------ planos

def tiene_video(f):
    s = subprocess.run([FF, '-i', f], capture_output=True, text=True).stderr
    return 'Video:' in s


def plano_broll(src, t_out, out, tarjeta=False):
    """Un plano de B-roll del original, escalado a 1080x1920 y estirado a t_out."""
    d = dur(src, 0.12)
    pts = max(0.25, t_out) / max(0.08, d)
    if tarjeta:
        # fondo oscuro desenfocado + tarjeta redondeada con halo blanco
        vf = (f"[0:v]setpts={pts:.5f}*PTS,fps={FPS},split=2[bg][fg];"
              f"[bg]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},"
              f"boxblur=28:2,eq=brightness=-0.22[b];"
              f"[fg]scale={int(W*0.845)}:-2[f];"
              f"[b][f]overlay=(W-w)/2:(H-h)/2:format=auto[v]")
    else:
        vf = (f"[0:v]setpts={pts:.5f}*PTS,fps={FPS},"
              f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H}[v]")
    run([FF, '-y', '-loglevel', 'error', '-i', src, '-filter_complex', vf,
         '-map', '[v]', '-an', '-t', f'{t_out:.3f}',
         '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18',
         '-pix_fmt', 'yuv420p', '-r', str(FPS), out])


def plano_avatar(src, t0, t_out, out):
    """Un tramo del render de HeyGen, del segundo t0, de t_out de largo."""
    run([FF, '-y', '-loglevel', 'error', '-ss', f'{t0:.3f}', '-i', src,
         '-t', f'{t_out:.3f}',
         '-vf', f"fps={FPS},scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H}",
         '-an', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18',
         '-pix_fmt', 'yuv420p', '-r', str(FPS), out])


# -------------------------------------------------------------- subtitulos

# la franja donde caen todos los subtitulos: recortarla ahorra 60 % de disco y
# de tiempo de render contra guardar la placa entera de 1080x1920
BANDA_Y0, BANDA_Y1 = 980, 1780


def capa_subtitulos(tarjetas, total, tmp, out):
    """tarjetas = [(t0, t1, imagen PIL RGBA)] -> un MOV con alfa de `total` segundos."""
    d = os.path.join(tmp, 'subs')
    os.makedirs(d, exist_ok=True)
    alto = BANDA_Y1 - BANDA_Y0
    vacio = G.Image.new('RGBA', (G.W, alto), (0, 0, 0, 0))
    piezas = []   # (png, duracion)
    t = 0.0
    for (t0, t1, img) in tarjetas:
        if t0 > t + 0.02:
            piezas.append((None, t0 - t))
        piezas.append((img, max(0.05, t1 - t0)))
        t = t1
    if total > t + 0.02:
        piezas.append((None, total - t))
    lista = os.path.join(d, 'lista.txt')
    vacio_png = os.path.join(d, 'vacio.png')
    vacio.save(vacio_png)
    with open(lista, 'w') as f:
        for i, (img, dd) in enumerate(piezas):
            if img is None:
                p = vacio_png
            else:
                p = os.path.join(d, f'{i:05d}.png')
                img.crop((0, BANDA_Y0, G.W, BANDA_Y1)).save(p)
            f.write(f"file '{os.path.abspath(p)}'\nduration {dd:.3f}\n")
        f.write(f"file '{os.path.abspath(p)}'\n")
    run([FF, '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', lista,
         '-vf', f'fps={FPS},format=rgba', '-c:v', 'qtrle', '-t', f'{total:.3f}', out])


def agrupar(palabras, n):
    """Agrupa las palabras alineadas de a n para armar cada placa."""
    out = []
    for i in range(0, len(palabras), n):
        g = palabras[i:i + n]
        out.append((g[0]['start'], g[-1]['end'], ' '.join(p['word'].strip() for p in g)))
    return out


def tarjetas_de(estilo, palabras):
    """Devuelve [(t0,t1,img)] segun el estilo de cada anuncio."""
    t = []
    if estilo == 'minuscula':
        for p in palabras:
            t.append((p['start'], p['end'], G.minuscula(p['word'].strip())))
    elif estilo == 'amarillo':
        for (a, b, txt) in agrupar(palabras, 3):
            t.append((a, b, G.amarillo(txt)))
    elif estilo == 'banda':
        for (a, b, txt) in agrupar(palabras, 6):
            t.append((a, b, G.banda(txt)))
    elif estilo in ('azul', 'violeta', 'verde'):
        fn = {'azul': G.azul, 'violeta': G.violeta, 'verde': G.verde}[estilo]
        n = 4 if estilo == 'azul' else 4
        for i in range(0, len(palabras), n):
            g = palabras[i:i + n]
            txt = ' '.join(p['word'].strip() for p in g)
            for j, p in enumerate(g):
                t.append((p['start'], p['end'], fn(txt, j)))
    elif estilo == 'ninguno':
        return []       # el anuncio 8 no lleva subtitulos corridos
    else:
        raise SystemExit('estilo desconocido: ' + estilo)
    # sin huecos negativos
    limpio = []
    for (a, b, im) in t:
        if limpio and a < limpio[-1][1]:
            a = limpio[-1][1]
        if b <= a:
            b = a + 0.08
        limpio.append((a, b, im))
    return limpio


def capa_extras(extras, total, tmp, out):
    """Todas las placas fijas en un solo MOV con alfa.

    Se arma la linea de tiempo de los cortes de todas las placas, se compone
    lo que este activo en cada tramo y se recorta a la franja util: una sola
    entrada para ffmpeg en vez de una por placa.
    """
    hechas = []
    for ex in extras:
        t0 = ex['t0'] * total if ex['t0'] <= 1 else ex['t0']
        t1 = ex['t1'] * total if ex['t1'] <= 1 else ex['t1']
        hechas.append((min(t0, total), min(t1, total),
                       getattr(G, ex['fn'])(*ex.get('args', []))))
    cortes = sorted({0.0, total} | {t for (a, b, _) in hechas for t in (a, b)})
    tramos = []           # (t0, t1, imagen o None)
    for a, b in zip(cortes, cortes[1:]):
        if b - a < 0.02:
            continue
        activas = [im for (x, y, im) in hechas if x <= a + 0.001 and y >= b - 0.001]
        if not activas:
            tramos.append((a, b, None))
            continue
        comp = activas[0].copy()
        for im in activas[1:]:
            comp = G.Image.alpha_composite(comp, im)
        tramos.append((a, b, comp))
    # franja util: la caja que contiene todo lo que se dibuja
    y0, y1 = G.H, 0
    for (_, _, im) in tramos:
        if im is None:
            continue
        caja = im.getbbox()
        if caja:
            y0, y1 = min(y0, caja[1]), max(y1, caja[3])
    if y1 <= y0:
        y0, y1 = 0, 2
    y0, y1 = max(0, y0 - 2), min(G.H, y1 + 2)
    d = os.path.join(tmp, 'extras')
    os.makedirs(d, exist_ok=True)
    vacio_png = os.path.join(d, 'vacio.png')
    G.Image.new('RGBA', (G.W, y1 - y0), (0, 0, 0, 0)).save(vacio_png)
    lista = os.path.join(d, 'lista.txt')
    with open(lista, 'w') as f:
        p = vacio_png
        for i, (a, b, im) in enumerate(tramos):
            if im is None:
                p = vacio_png
            else:
                p = os.path.join(d, f'{i:05d}.png')
                im.crop((0, y0, G.W, y1)).save(p)
            f.write(f"file '{os.path.abspath(p)}'\nduration {b - a:.3f}\n")
        f.write(f"file '{os.path.abspath(p)}'\n")
    run([FF, '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', lista,
         '-vf', f'fps={FPS},format=rgba', '-c:v', 'qtrle', '-t', f'{total:.3f}', out])
    return y0


# ------------------------------------------------------------------ montaje

def montar(plan):
    pid = plan['id']
    gid = plan['guion']
    cortes = json.load(open(f'{BASE}/cortes.json'))[pid]
    segs = cortes['segs']
    D = cortes['dur']
    voz = f"{BASE}/voz/{gid}.wav"
    avatar = plan.get('avatar')
    Dp = dur(voz)
    k = Dp / D
    # un anuncio puede tener varios presentadores (el 5 tiene tres):
    # cada avatar corre con el mismo reloj y se muestra en sus propios planos
    avatares = plan.get('avatares') or [{'archivo': avatar, 'idx': plan['presentador']}]
    de_quien = {}
    for a in avatares:
        for i in a['idx']:
            de_quien[i] = a['archivo']
    pres = set(de_quien)
    # si ya existe el concat de una corrida anterior, se reusa: rehacer solo
    # los subtitulos no justifica volver a codificar 60 planos
    if plan.get('base') and os.path.exists(plan['base']):
        tmp = os.path.dirname(plan['base'])
        base = plan['base']
        total = dur(base)
        return _terminar(plan, gid, tmp, base, total, voz, D, Dp / D)
    tmp = tempfile.mkdtemp(prefix=f'cab_{gid}_', dir='/private/tmp')
    piezas = []
    ultimo_bueno = None
    t_av = 0.0        # cuanto del avatar llevamos consumido
    reloj = 0.0
    for i, (a, b, dd) in enumerate(segs):
        t_out = round(max(0.25, dd * k), 3)
        out = f'{tmp}/p{i:03d}.mp4'
        if i in pres:
            plano_avatar(de_quien[i], t_av, t_out, out)
        else:
            # el clip sin los subtitulos en portugues; si no se limpio, el crudo
            src = f'{BASE}/planos_limpios/{pid}/{i:03d}.mp4'
            if not os.path.exists(src):
                src = f'{BASE}/planos/{pid}/{i:03d}.mp4'
            # los planos de uno o dos cuadros a veces salen sin pista de video:
            # se alarga el ultimo plano bueno en vez de cortar el montaje
            if not tiene_video(src):
                if ultimo_bueno is None:
                    continue
                src = ultimo_bueno
            else:
                ultimo_bueno = src
            plano_broll(src, t_out, out, tarjeta=plan.get('tarjeta', False))
        t_av += t_out     # el avatar corre con el reloj aunque no se vea
        reloj += t_out
        piezas.append(out)
    lista = f'{tmp}/lista.txt'
    with open(lista, 'w') as f:
        for p in piezas:
            f.write(f"file '{os.path.abspath(p)}'\n")
    base = f'{tmp}/base.mp4'
    run([FF, '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', lista,
         '-c', 'copy', base])
    total = dur(base)
    return _terminar(plan, gid, tmp, base, total, voz, D, k)


def _terminar(plan, gid, tmp, base, total, voz, D, k):
    """Subtitulos, placas y muxeo final sobre el concat ya armado."""
    # subtitulos
    palabras = json.load(open(f'{BASE}/alineacion/{gid}.json'))
    tarjetas = tarjetas_de(plan['estilo'], palabras)
    subs = f'{tmp}/subs.mov'
    if tarjetas:
        capa_subtitulos(tarjetas, total, tmp, subs)
    else:
        # lavfi con alpha 0 sale negro opaco en qtrle: hay que partir de un PNG
        d = os.path.join(tmp, 'subs'); os.makedirs(d, exist_ok=True)
        vacio = os.path.join(d, 'vacio.png')
        G.Image.new('RGBA', (G.W, BANDA_Y1 - BANDA_Y0), (0, 0, 0, 0)).save(vacio)
        run([FF, '-y', '-loglevel', 'error', '-loop', '1', '-i', vacio,
             '-t', f'{total:.3f}', '-vf', f'fps={FPS},format=rgba',
             '-c:v', 'qtrle', subs])

    # placas fijas (boton, caja de hook, ranking): van todas en UNA capa.
    # un -loop 1 por placa hace que ffmpeg retenga los cuadros de cada PNG de
    # 1080x1920 y el anuncio 8, con 9 placas y 171 s, se lo llevo el OOM killer.
    extras = plan.get('extras', [])
    entradas = ['-i', base, '-i', subs, '-i', voz]
    fc = f'[0:v][1:v]overlay=0:{BANDA_Y0}[v1]'
    ult = 'v1'
    if extras:
        capa = f'{tmp}/extras.mov'
        y0 = capa_extras(extras, total, tmp, capa)
        entradas += ['-i', capa]
        fc += f";[{ult}][3:v]overlay=0:{y0}[v2]"
        ult = 'v2'
    fc += (f";[2:a]loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000[a]")
    out = plan['salida']
    run([FF, '-y', '-loglevel', 'error'] + entradas +
        ['-filter_complex', fc, '-map', f'[{ult}]', '-map', '[a]',
         '-c:v', 'libx264', '-preset', 'medium', '-crf', '20', '-pix_fmt', 'yuv420p',
         '-c:a', 'aac', '-b:a', '160k', '-ar', '48000', '-ac', '2',
         '-shortest', '-movflags', '+faststart', out])
    if not os.path.exists(out) or os.path.getsize(out) < 200000:
        raise SystemExit('el mp4 no se genero o pesa de menos: ' + out)
    print(f'LISTO {out}  {dur(out):.1f}s  {os.path.getsize(out)//1024} KB  (original {D:.1f}s, k={k:.3f})')


if __name__ == '__main__':
    plan = json.load(open(sys.argv[1]))
    for p in (plan if isinstance(plan, list) else [plan]):
        montar(p)
