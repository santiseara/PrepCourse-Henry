# -*- coding: utf-8 -*-
"""Baja clips de TikTok sin marca de agua con yt-dlp por la API movil.
24/11/2026: tikwm se cayo (502 sostenido) y no hay plan B por navegador (TikTok sirve
el stream por blob/MSE). Lo que si anda, con el yt-dlp 2025.10.14 que corre en el
Python 3.9 del sistema, es forzar el hostname de la API movil:
    --extractor-args "tiktok:api_hostname=api22-normal-c-useast2a.tiktokv.com"
Sin ese flag el extractor va al webpage y muere con "Unable to extract webpage video data".
Con el flag igual es intermitente (TikTok contesta distinto segun el intento), asi que
cada id se reintenta varias veces. Da 540x960, no 1080: alcanza para b-roll con zoom bajo.
Uso: python3 dl_tiktok_ytdlp.py ids.txt destino/ [hilos]"""
import os, subprocess, sys
from concurrent.futures import ThreadPoolExecutor

ids = [l.strip() for l in open(sys.argv[1]) if l.strip() and not l.startswith('#')]
dst = sys.argv[2]; os.makedirs(dst, exist_ok=True)
HILOS = int(sys.argv[3]) if len(sys.argv) > 3 else 4
HOSTS = ['api22-normal-c-useast2a.tiktokv.com', 'api16-normal-c-useast1a.tiktokv.com']

def baja(vid):
    out = os.path.join(dst, vid + '.mp4')
    if os.path.exists(out) and os.path.getsize(out) > 150000:
        return 'skip'
    for intento in range(6):
        host = HOSTS[intento % len(HOSTS)]
        try:
            r = subprocess.run([sys.executable, '-m', 'yt_dlp', '--no-warnings', '-q',
                                            '--socket-timeout', '25', '--no-playlist',
                                            '--extractor-args', f'tiktok:api_hostname={host}',
                                            '--format-sort', 'res,br',
                                '-o', os.path.join(dst, '%(id)s.%(ext)s'),
                                f'https://www.tiktok.com/@_/video/{vid}'],
                               capture_output=True, text=True, timeout=90)
        except subprocess.TimeoutExpired:
            for resto in os.listdir(dst):
                if resto.startswith(vid) and resto.endswith('.part'):
                    os.remove(os.path.join(dst, resto))
            continue
        if os.path.exists(out) and os.path.getsize(out) > 150000:
            return 'ok'
    return 'fail'

res = {'ok': 0, 'fail': 0, 'skip': 0}
with ThreadPoolExecutor(HILOS) as ex:
    for i, r in enumerate(ex.map(baja, ids)):
        res[r] += 1
        if (i + 1) % 10 == 0:
            print(f'{i+1}/{len(ids)}  ok={res["ok"]} fail={res["fail"]} skip={res["skip"]}', flush=True)
print('listo:', res)
