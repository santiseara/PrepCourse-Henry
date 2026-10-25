"""Render por segmentos y en paralelo del VSL (reemplaza el filtro unico de 70 capas).
Uso: python3 render_rapido.py render.json salida.mkv
Corta la linea de tiempo en los bordes de cada b-roll, placa y zoom; cada segmento
se arma con dos o tres capas en vez de setenta y se renderizan de a varios a la vez."""
import json, os, sys, subprocess, math
from concurrent.futures import ThreadPoolExecutor

D = json.load(open(sys.argv[1])); OUT = sys.argv[2]
FF = os.path.expanduser('~/bin/ffmpeg')
W, H = 1080, 1920
TOT = D['total']; TMP = D['tmp']
os.makedirs(TMP, exist_ok=True)
NUCLEOS = int(os.environ.get('NUCLEOS', max(2, (os.cpu_count() or 4) - 2)))

def seg_ass(s, e, k):
    """subtitulos del segmento, con los tiempos corridos al cero del segmento"""
    cab, ev = open(D['ass'], encoding='utf-8').read().split('[Events]')
    lin = ev.split('\n'); fmt = [l for l in lin if l.startswith('Format:')][0]
    def sec(t):
        h, m, r = t.split(':'); return int(h) * 3600 + int(m) * 60 + float(r)
    def ts(x):
        x = max(0, x); h = int(x // 3600); m = int((x % 3600) // 60)
        return f'{h}:{m:02d}:{x - h * 3600 - m * 60:05.2f}'
    out = []
    for l in lin:
        if not l.startswith('Dialogue:'): continue
        p = l.split(','); a, b = sec(p[1]), sec(p[2])
        if b <= s or a >= e: continue
        p[1], p[2] = ts(a - s), ts(b - s)
        out.append(','.join(p))
    f = f'{TMP}/s{k:04d}.ass'
    open(f, 'w', encoding='utf-8').write(cab + '[Events]\n' + fmt + '\n' + '\n'.join(out) + '\n')
    return f

def activos(s, e):
    m = (s + e) / 2
    br = [b for b in D['brolls'] if b[1] <= m < b[2]]
    st = [x for x in D['stickers'] if x[1] <= m < x[1] + x[2]]
    zm = any(a <= m < b for a, b in D['zoom'])
    return br, st, zm

def render(args):
    k, s, e = args
    dur = e - s
    br, st, zm = activos(s, e)
    inp = ['-ss', f'{s:.3f}', '-t', f'{dur:.3f}', '-i', D['trimmed']]
    fc = []
    if zm:
        fc.append(f"[0:v]fps=30,setpts=PTS-STARTPTS,split=2[base][zs]")
        fc.append("[zs]scale=1210:-2,crop=1080:1920:65:40[zm]")
        fc.append("[base][zm]overlay=0:0[v0]")
    else:
        fc.append("[0:v]fps=30,setpts=PTS-STARTPTS[v0]")
    cur = 'v0'; n = 1
    for f, a, b, ss, modo, cy in br:
        off = ss + (s - a)
        iv = n; n += 1                      # indice de entrada del b-roll
        inp += ['-ss', f'{off:.3f}', '-t', f'{dur + 0.2:.3f}', '-i', f]
        fc.append(f"[{iv}:v]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps=30,"
                  + D['look'] + f"setpts=PTS-STARTPTS[b{iv}]")
        if modo == 'split':
            bh = H - D['split_y']
            im = n; n += 1                  # indice de entrada de la mascara del degrade
            inp += ['-loop', '1', '-t', f'{dur:.3f}', '-i', D['split_mask']]
            fc.append(f"[b{iv}]crop={W}:{bh}:0:{cy},format=rgba[c{iv}]")
            fc.append(f"[{im}:v]format=gray,scale={W}:{bh}[m{iv}]")
            fc.append(f"[c{iv}][m{iv}]alphamerge[bs{iv}]")
            fc.append(f"[{cur}][bs{iv}]overlay=0:{D['split_y']}:eof_action=pass[v{iv}]")
        else:
            fc.append(f"[{cur}][b{iv}]overlay=0:0:eof_action=pass[v{iv}]")
        cur = f'v{iv}'
    for png, t, d_, x, y, w_ in st:
        iv = n; n += 1
        inp += ['-loop', '1', '-t', f'{dur:.3f}', '-i', png]
        fi, fo = max(0, t - s), max(0, t + d_ - 0.2 - s)
        fc.append(f"[{iv}:v]scale={w_}:-1,format=rgba,fade=t=in:st={fi:.2f}:d=0.15:alpha=1,"
                  f"fade=t=out:st={fo:.2f}:d=0.2:alpha=1[st{iv}]")
        fc.append(f"[{cur}][st{iv}]overlay={x}:{y}[v{iv}]")
        cur = f'v{iv}'
    dst0 = f'{TMP}/s{k:04d}.mkv'
    if os.path.exists(dst0) and os.path.getsize(dst0) > 1000 and os.environ.get('REUSAR'):
        return dst0
    ass = seg_ass(s, e, k).replace(':', r'\:')
    fc.append(f"[{cur}]ass='{ass}':fontsdir='{D['fonts']}',format=yuv420p[vout]")
    fcf = f'{TMP}/s{k:04d}.txt'; open(fcf, 'w').write(';\n'.join(fc))
    dst = f'{TMP}/s{k:04d}.mkv'
    r = subprocess.run([FF, '-v', 'error', '-y'] + inp + ['-filter_complex_script', fcf,
                       '-map', '[vout]', '-map', '0:a', '-t', f'{dur:.3f}', '-r', '30',
                       '-c:v', 'libx264', '-crf', '17', '-preset', 'veryfast',
                       '-c:a', 'pcm_s16le', dst], capture_output=True, text=True)
    if r.returncode:
        print(f'  segmento {k} ({s:.2f}-{e:.2f}) FALLO:', r.stderr[-400:], flush=True)
        return None
    return dst

bordes = {0.0, TOT}
for f, a, b, ss, m, cy in D['brolls']: bordes |= {a, b}
for png, t, d_, x, y, w_ in D['stickers']: bordes |= {t, t + d_}
for a, b in D['zoom']: bordes |= {a, b}
bordes = sorted(x for x in bordes if 0 <= x <= TOT)
segs = [(i, bordes[i], bordes[i + 1]) for i in range(len(bordes) - 1) if bordes[i + 1] - bordes[i] > 0.05]
# partir los segmentos largos para repartirlos mejor entre los nucleos
MAX = 25.0
partidos = []
for k, s, e in segs:
    n = max(1, math.ceil((e - s) / MAX)); paso = (e - s) / n
    for j in range(n): partidos.append((len(partidos), s + j * paso, s + (j + 1) * paso))
print(f'{len(partidos)} segmentos, {NUCLEOS} en paralelo', flush=True)
with ThreadPoolExecutor(NUCLEOS) as ex:
    piezas = list(ex.map(render, partidos))
if any(p is None for p in piezas): sys.exit('fallo algun segmento')
lst = f'{TMP}/lista.txt'
open(lst, 'w').write(''.join(f"file '{os.path.abspath(p)}'\n" for p in piezas))
subprocess.run([FF, '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', lst, '-c', 'copy', OUT], check=True)
print('video armado:', OUT, flush=True)
