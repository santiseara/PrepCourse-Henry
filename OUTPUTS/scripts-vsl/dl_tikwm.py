# -*- coding: utf-8 -*-
"""Baja clips de TikTok sin marca de agua con tikwm, de a uno y con pausa.
Uso: python3 dl_tikwm.py ids.txt destino/"""
import json, os, sys, time, urllib.request

ids = [l.strip() for l in open(sys.argv[1]) if l.strip() and not l.startswith('#')]
dst = sys.argv[2]; os.makedirs(dst, exist_ok=True)
UA = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/131.0 Safari/537.36'}
ok = fail = skip = 0
for i, vid in enumerate(ids):
    out = os.path.join(dst, vid + '.mp4')
    if os.path.exists(out) and os.path.getsize(out) > 200000:
        skip += 1; continue
    url = f'https://www.tikwm.com/api/?hd=1&url=https://www.tiktok.com/@x/video/{vid}'
    got = False
    for intento in range(4):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=45) as r:
                d = json.load(r)
            data = (d or {}).get('data') or {}
            link = data.get('hdplay') or data.get('play')
            if not link:
                time.sleep(2.0); continue
            if link.startswith('/'): link = 'https://www.tikwm.com' + link
            with urllib.request.urlopen(urllib.request.Request(link, headers=UA), timeout=180) as r, open(out + '.part', 'wb') as f:
                f.write(r.read())
            if os.path.getsize(out + '.part') < 120000:
                os.remove(out + '.part'); time.sleep(2.0); continue
            os.replace(out + '.part', out); got = True; break
        except Exception as e:
            time.sleep(2.0)
    print(('OK  ' if got else 'FAIL') + f' {i+1}/{len(ids)} {vid}', flush=True)
    ok += got; fail += not got
    time.sleep(1.2)
print(f'listo: {ok} bajados, {skip} ya estaban, {fail} fallaron')
