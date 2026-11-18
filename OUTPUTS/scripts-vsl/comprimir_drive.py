#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Recomprime un mp4 a 9,3 MB con x264 en dos pasadas, para que entre por el
conector de Drive (corta en 10 MB). Regla fija del 17/11/2026: el peso no es
excusa para no subir una tanda.

Uso: python3 comprimir_drive.py entrada.mp4 salida.mp4 [MB]
"""
import os, re, subprocess, sys

FF = os.path.expanduser('~/bin/ffmpeg')


def dur(f):
    s = subprocess.run([FF, '-i', f], capture_output=True, text=True).stderr
    m = re.search(r'Duration: (\d+):(\d+):([\d.]+)', s)
    h, mi, se = m.groups()
    return int(h) * 3600 + int(mi) * 60 + float(se)


def comprimir(entrada, salida, mb=9.3):
    d = dur(entrada)
    kbps = int((mb * 8192) / d - 130)
    if kbps < 200:
        kbps = 200
    base = ['-y', '-loglevel', 'error', '-i', entrada, '-c:v', 'libx264',
            '-preset', 'veryslow', '-b:v', f'{kbps}k', '-pix_fmt', 'yuv420p']
    log = salida + '.2pass'
    subprocess.run([FF] + base + ['-pass', '1', '-passlogfile', log, '-an',
                    '-f', 'mp4', '/dev/null'], check=True)
    subprocess.run([FF] + base + ['-pass', '2', '-passlogfile', log,
                    '-c:a', 'aac', '-b:a', '128k', '-ar', '48000', '-ac', '2',
                    '-movflags', '+faststart', salida], check=True)
    for ext in ('-0.log', '-0.log.mbtree', '.log', '.log.mbtree'):
        p = log + ext
        if os.path.exists(p):
            os.remove(p)
    return os.path.getsize(salida)


if __name__ == '__main__':
    e, s = sys.argv[1], sys.argv[2]
    mb = float(sys.argv[3]) if len(sys.argv) > 3 else 9.3
    n = comprimir(e, s, mb)
    print(f'{s}  {n//1024} KB  ({dur(s):.1f}s)')
