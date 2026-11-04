"""Cama musical ACTIVA y original para un VSL: pulso suave, 96 BPM, sin melodia
que compita con la voz.

La diferencia con music_calma.py: esta tiene latido. Un shaker de corcheas y un
kick al pulso dan movimiento sin ocupar el rango de la voz (todo lo percusivo
vive arriba de 2 kHz o abajo de 120 Hz). Los acordes son pad y marimba corta,
nunca una melodia: una melodia pelea con la locucion y cansa al minuto.

Progresion Am - F - C - G, que es la misma de la version calma, para que las dos
suenen de la misma casa.

Uso: python3 music_activa.py <segundos> <salida.wav>
"""
import sys

import numpy as np
from scipy.io import wavfile
from scipy.signal import butter, fftconvolve, sosfilt

SR = 44100
BPM = 96
BEAT = 60 / BPM
BAR = 4 * BEAT

dur_total = float(sys.argv[1])
out = sys.argv[2]
rng = np.random.default_rng(7)


def lp(x, f, order=2):
    return sosfilt(butter(order, f, 'low', fs=SR, output='sos'), x)


def hp(x, f, order=2):
    return sosfilt(butter(order, f, 'high', fs=SR, output='sos'), x)


def bp(x, f0, f1, order=2):
    return sosfilt(butter(order, [f0, f1], 'band', fs=SR, output='sos'), x)


def hz(m):
    return 440 * 2 ** ((m - 69) / 12)


def marimba(m, dur=0.75, vel=1.0):
    """Nota corta y redonda: decae rapido, no deja cola que ensucie la voz."""
    n = int(dur * SR)
    t = np.arange(n) / SR
    f = hz(m)
    x = (np.sin(2 * np.pi * f * t) * np.exp(-t / 0.22)
         + 0.22 * np.sin(2 * np.pi * 4 * f * t) * np.exp(-t / 0.05))
    return x * np.minimum(1, t / 0.004) * vel * 0.20


def pad(ms, dur, vel=1.0):
    n = int(dur * SR)
    t = np.arange(n) / SR
    x = np.zeros(n)
    for m in ms:
        f = hz(m)
        for det in (-0.005, 0.005):
            x += (2 * ((t * f * (1 + det)) % 1) - 1)
    x = lp(x / (2 * len(ms)), 520)
    swell = np.sin(np.pi * np.clip(t / dur, 0, 1)) ** 0.7
    return x * swell * vel * 0.13


def bajo(m, dur=1.6, vel=1.0):
    n = int(dur * SR)
    t = np.arange(n) / SR
    f = hz(m)
    x = np.sin(2 * np.pi * f * t) * np.exp(-t / 0.55)
    return x * np.minimum(1, t / 0.008) * vel * 0.26


def shaker(dur=0.14, vel=1.0):
    """Ruido agudo y corto: todo arriba de 4 kHz, lejos de la voz."""
    n = int(dur * SR)
    t = np.arange(n) / SR
    x = bp(rng.standard_normal(n), 4500, 11000) * np.exp(-t / 0.028)
    return x * vel * 0.085


def kick(dur=0.3, vel=1.0):
    """Golpe grave con barrido de tono, sin click: marca el pulso y desaparece."""
    n = int(dur * SR)
    t = np.arange(n) / SR
    f = 95 * np.exp(-t / 0.045) + 42
    x = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.12)
    return x * vel * 0.30


# Am - F - C - G, un compas cada uno
PROG = [([69, 72, 76], [57, 60, 64], 45),
        ([65, 69, 72], [53, 57, 60], 41),
        ([67, 72, 76], [55, 60, 64], 48),
        ([67, 71, 74], [55, 59, 62], 43)]

n_tot = int((dur_total + 4) * SR)
L = np.zeros(n_tot)
R = np.zeros(n_tot)


def add(buf, x, pos, g=1.0):
    i = int(pos * SR)
    j = min(i + len(x), len(buf))
    if i < len(buf):
        buf[i:j] += x[:j - i] * g


bar = 0
while bar * BAR < dur_total + 4:
    arp, acorde, raiz = PROG[bar % len(PROG)]
    t0 = bar * BAR

    add(L, pad(acorde, BAR), t0)
    add(R, pad(acorde, BAR), t0 + 0.011)

    for k in range(4):                              # kick y bajo al pulso
        pos = t0 + k * BEAT
        if k in (0, 2):
            add(L, kick(), pos); add(R, kick(), pos)
        if k in (0, 2, 3):
            add(L, bajo(raiz), pos); add(R, bajo(raiz), pos + 0.004)

    for k in range(8):                              # shaker en corcheas
        pos = t0 + k * BEAT / 2
        vel = 1.0 if k % 2 == 0 else 0.55
        pan = 0.5 + 0.22 * np.sin(k * 1.1)
        s = shaker(vel=vel)
        add(L, s * (1 - pan) * 2 * 0.5, pos)
        add(R, s * pan * 2 * 0.5, pos + 0.004)

    for k, m in enumerate(arp):                     # marimba, tres notas por compas
        pos = t0 + k * BEAT * 1.25
        pan = 0.5 + 0.25 * np.sin(k * 1.7 + bar)
        nota = marimba(m, vel=0.9 if k == 0 else 0.6)
        add(L, nota * (1 - pan) * 2 * 0.5, pos)
        add(R, nota * pan * 2 * 0.5, pos + 0.007)

    bar += 1

# reverb corta: da aire sin emborronar el pulso
ir_n = int(1.1 * SR)
ir_t = np.arange(ir_n) / SR
ir = lp(rng.standard_normal(ir_n), 5200) * np.exp(-ir_t / 0.30)
ir[:int(0.008 * SR)] = 0
ir /= np.abs(ir).sum() / 8
L = 0.84 * L + 0.16 * fftconvolve(L, ir)[:n_tot]
R = 0.84 * R + 0.16 * fftconvolve(R, ir * 0.95)[:n_tot]
L, R = hp(L, 40), hp(R, 40)

x = np.stack([L, R], 1)[:int(dur_total * SR)]
x *= 0.70 / max(1e-9, np.abs(x).max())
f_in, f_out = int(1.0 * SR), int(2.0 * SR)
x[:f_in] *= np.linspace(0, 1, f_in)[:, None]
x[-f_out:] *= np.linspace(1, 0, f_out)[:, None]
wavfile.write(out, SR, (x * 32767).astype(np.int16))
print(out, round(len(x) / SR, 2), 's', BPM, 'BPM')
