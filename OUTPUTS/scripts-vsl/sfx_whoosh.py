"""Whooshes suaves para las transiciones a B-roll. Nada de SFX de dibujito.

Son barridos de ruido filtrado: entran y salen en menos de medio segundo y viven
arriba de los 700 Hz, asi que no se pisan con la voz. Se generan dos tipos:
  in.wav  — barrido que sube, para entrar al B-roll
  out.wav — barrido que baja, para volver a la cara

Uso: python3 sfx_whoosh.py <carpeta_salida>
"""
import os
import sys

import numpy as np
from scipy.io import wavfile
from scipy.signal import butter, sosfilt

SR = 44100
rng = np.random.default_rng(3)


def bp(x, f0, f1):
    return sosfilt(butter(2, [f0, f1], 'band', fs=SR, output='sos'), x)


def whoosh(sube=True, dur=0.45):
    n = int(dur * SR)
    t = np.arange(n) / SR
    base = rng.standard_normal(n)
    # el barrido se arma por tramos: cada uno filtrado a una banda distinta
    out = np.zeros(n)
    tramos = 24
    for i in range(tramos):
        a, b = int(i * n / tramos), int((i + 1) * n / tramos)
        k = i / (tramos - 1)
        if not sube:
            k = 1 - k
        f0 = 700 + 5200 * k
        seg = bp(base[a:b], f0, min(f0 * 2.4, SR / 2 - 500))
        out[a:b] = seg
    env = np.sin(np.pi * np.clip(t / dur, 0, 1)) ** 1.4
    out *= env
    out /= max(1e-9, np.abs(out).max())
    st = np.stack([out * 0.95, out], 1) * 0.42
    return st


def main():
    d = sys.argv[1]
    os.makedirs(d, exist_ok=True)
    for nombre, sube in (('whoosh_in.wav', True), ('whoosh_out.wav', False)):
        x = whoosh(sube)
        p = os.path.join(d, nombre)
        wavfile.write(p, SR, (x * 32767).astype(np.int16))
        print(p, round(len(x) / SR, 2), 's')


if __name__ == '__main__':
    main()
