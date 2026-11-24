# -*- coding: utf-8 -*-
"""Saca el autor de TikTok de cada clip que paso el filtro, para que el editor no ponga
dos planos seguidos del mismo creador (la clave "fam" del plan).

Usa el oembed publico de TikTok (gratis y rapido); si falla, cae a tikwm.
Salida: <workdir>/autores.json  {'<id>': '<usuario>'}
Uso: python3 autores_alivio.py <workdir>
"""
import json, os, re, sys, time, urllib.request
from concurrent.futures import ThreadPoolExecutor

W = sys.argv[1]
sys.path.insert(0, W)
from vent_alivio import VENT

UA = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/131.0 Safari/537.36'}
out_path = os.path.join(W, 'autores.json')
ya = json.load(open(out_path)) if os.path.exists(out_path) else {}
ids = sorted({v[0] for v in VENT.values()} - set(ya))


def uno(vid):
    for url, campo in (
            (f'https://www.tiktok.com/oembed?url=https://www.tiktok.com/@x/video/{vid}', 'author_url'),
            (f'https://www.tikwm.com/api/?url=https://www.tiktok.com/@x/video/{vid}', None)):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=25) as r:
                d = json.load(r)
            if campo:
                m = re.search(r'@([\w.\-]+)', d.get(campo, '') or '')
                if m: return vid, m.group(1)
            else:
                u = ((d or {}).get('data') or {}).get('author', {}).get('unique_id')
                if u: return vid, u
        except Exception:
            time.sleep(1.0)
    return vid, None


with ThreadPoolExecutor(max_workers=6) as ex:
    for vid, autor in ex.map(uno, ids):
        if autor: ya[vid] = autor

json.dump(ya, open(out_path, 'w'), ensure_ascii=False, indent=1)
faltan = [v[0] for v in VENT.values() if v[0] not in ya]
print('autores: %d de %d clips (%d sin autor, quedan con su propio id como familia)'
      % (len(ya), len({v[0] for v in VENT.values()}), len(faltan)))
