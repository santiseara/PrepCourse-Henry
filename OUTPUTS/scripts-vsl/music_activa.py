"""Cama musical ACTIVA y original para ads sin locucion o con voz en off: pluck de marimba,
bajo redondo, palmas y hi-hat, 104 BPM, Do-Sol-Lam-Fa. Nada de samples: todo sintetizado.

Nace el 2026-11-10 para los organicos de Noche de Citas Cristiana, porque Santiago pidio
"musica activa, no la de siempre". Hermana de music_calma.py.

Uso: python3 music_activa.py <segundos> <salida.wav>
"""
import sys, numpy as np
from scipy.signal import butter, sosfilt, fftconvolve
from scipy.io import wavfile

SR = 44100
BPM = 104
BEAT = 60 / BPM
BAR = 4 * BEAT
dur_total = float(sys.argv[1]); out = sys.argv[2]
rng = np.random.default_rng(7)


def lp(x, f, order=2): return sosfilt(butter(order, f, 'low', fs=SR, output='sos'), x)
def hp(x, f, order=2): return sosfilt(butter(order, f, 'high', fs=SR, output='sos'), x)
def bp(x, a, b): return sosfilt(butter(2, [a, b], 'band', fs=SR, output='sos'), x)
def hz(m): return 440 * 2 ** ((m - 69) / 12)


def pluck(m, dur=0.9, vel=1.0):
    """Marimba/pluck: fundamental + cuarta armonica corta, ataque rapido."""
    n = int(dur * SR); t = np.arange(n) / SR
    f = hz(m)
    x = (np.sin(2 * np.pi * f * t) * np.exp(-t / 0.34)
         + 0.42 * np.sin(2 * np.pi * 4.01 * f * t) * np.exp(-t / 0.055)
         + 0.16 * np.sin(2 * np.pi * 9.2 * f * t) * np.exp(-t / 0.02))
    return x * np.minimum(1, t / 0.004) * vel * 0.30


def bajo(m, dur=BEAT * 0.9, vel=1.0):
    n = int(dur * SR); t = np.arange(n) / SR
    f = hz(m)
    x = np.sin(2 * np.pi * f * t) + 0.25 * np.sin(2 * np.pi * 2 * f * t) * np.exp(-t / 0.12)
    env = np.minimum(1, t / 0.008) * np.exp(-t / (dur * 0.55))
    return lp(x, 900) * env * vel * 0.34


def bombo(vel=1.0):
    n = int(0.26 * SR); t = np.arange(n) / SR
    f = 110 * np.exp(-t / 0.028) + 48
    x = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.13)
    return x * vel * 0.52


def palma(vel=1.0):
    n = int(0.22 * SR); t = np.arange(n) / SR
    x = bp(rng.standard_normal(n), 1100, 3400) * np.exp(-t / 0.055)
    eco = np.zeros(n); d = int(0.012 * SR)
    eco[d:] = x[:-d] * 0.6
    return (x + eco) * vel * 0.26


def hat(vel=1.0, abierto=False):
    n = int((0.16 if abierto else 0.055) * SR); t = np.arange(n) / SR
    x = hp(rng.standard_normal(n), 7200) * np.exp(-t / (0.055 if abierto else 0.014))
    return x * vel * 0.12


# Do - Sol - Lam - Fa, un compas cada uno
PROG = [([72, 76, 79, 76], [48]), ([71, 74, 79, 74], [43]),
        ([72, 76, 81, 76], [45]), ([72, 77, 81, 77], [41])]

n_tot = int((dur_total + 4) * SR)
L = np.zeros(n_tot); R = np.zeros(n_tot)


def add(buf, x, pos):
    i = int(pos * SR); j = min(i + len(x), len(buf))
    if i < len(buf): buf[i:j] += x[:j - i]


bar = 0
while bar * BAR < dur_total + 4:
    arp, (raiz,) = PROG[bar % len(PROG)]
    t0 = bar * BAR
    for k in range(4):                                  # bajo en negras, con sincopa
        add(L, bajo(raiz), t0 + k * BEAT); add(R, bajo(raiz), t0 + k * BEAT + 0.003)
    add(L, bajo(raiz + 12, vel=0.55), t0 + 3.5 * BEAT)
    add(R, bajo(raiz + 12, vel=0.55), t0 + 3.5 * BEAT + 0.003)
    for k in range(8):                                  # pluck en corcheas
        m = arp[k % 4] + (12 if k >= 6 and bar % 2 else 0)
        vel = 1.0 if k % 2 == 0 else 0.55
        pos = t0 + k * BEAT / 2
        pan = 0.5 + 0.22 * np.sin(k * 1.1)
        nota = pluck(m, vel=vel)
        add(L, nota * (1 - pan) * 2 * 0.5, pos)
        add(R, nota * pan * 2 * 0.5, pos + 0.005)
    for k in range(4):                                  # bombo en 1 y 3, palma en 2 y 4
        add(L, bombo(1.0 if k % 2 == 0 else 0.0), t0 + k * BEAT)
        add(R, bombo(1.0 if k % 2 == 0 else 0.0), t0 + k * BEAT)
        if k % 2 == 1:
            p = palma()
            add(L, p * 1.05, t0 + k * BEAT); add(R, p * 0.95, t0 + k * BEAT + 0.004)
    for k in range(8):                                  # hats en corcheas
        h = hat(0.9 if k % 2 == 0 else 0.5, abierto=(k == 7))
        add(L, h * 0.9, t0 + k * BEAT / 2); add(R, h, t0 + k * BEAT / 2 + 0.003)
    bar += 1

ir_n = int(1.1 * SR); ir_t = np.arange(ir_n) / SR
ir = lp(rng.standard_normal(ir_n), 5200) * np.exp(-ir_t / 0.28)
ir[:int(0.008 * SR)] = 0
ir /= np.abs(ir).sum() / 7
Lw = fftconvolve(L, ir)[:n_tot]; Rw = fftconvolve(R, ir * 0.95)[:n_tot]
L = 0.84 * L + 0.16 * Lw; R = 0.84 * R + 0.16 * Rw
L = hp(L, 38); R = hp(R, 38)

x = np.stack([L, R], 1)[:int(dur_total * SR)]
x *= 0.72 / max(1e-9, np.abs(x).max())
f_in = int(0.5 * SR); f_out = int(1.6 * SR)
x[:f_in] *= np.linspace(0, 1, f_in)[:, None]
x[-f_out:] *= np.linspace(1, 0, f_out)[:, None]
wavfile.write(out, SR, (x * 32767).astype(np.int16))
print(out, round(dur_total, 1), 's', BPM, 'BPM')
