"""Cama musical tranquila y original para ads de voz en off: piano de fieltro + pad, 64 BPM,
Am-F-C-G, sin percusion. Uso: python3 music_calma.py <segundos> <salida.wav>"""
import sys, numpy as np
from scipy.signal import butter, sosfilt, fftconvolve
from scipy.io import wavfile

SR = 44100
BPM = 64
BEAT = 60 / BPM            # 0.9375 s
BAR = 4 * BEAT             # 3.75 s
dur_total = float(sys.argv[1]); out = sys.argv[2]
rng = np.random.default_rng(11)

def lp(x, f, order=2): return sosfilt(butter(order, f, 'low', fs=SR, output='sos'), x)
def hp(x, f, order=2): return sosfilt(butter(order, f, 'high', fs=SR, output='sos'), x)
def hz(m): return 440 * 2 ** ((m - 69) / 12)

def piano(m, dur=2.6, vel=1.0):
    """Nota de piano suave: fundamental + 2 armonicos debiles + golpe de martillo filtrado."""
    n = int(dur * SR); t = np.arange(n) / SR
    f = hz(m)
    x = (np.sin(2 * np.pi * f * t) * np.exp(-t / 1.7)
         + 0.30 * np.sin(2 * np.pi * 2 * f * t + 0.3) * np.exp(-t / 0.75)
         + 0.10 * np.sin(2 * np.pi * 3.01 * f * t) * np.exp(-t / 0.35))
    hammer = lp(rng.standard_normal(n), min(f * 5, 6000)) * np.exp(-t / 0.012) * 0.05
    atk = np.minimum(1, t / 0.012)
    return (x + hammer) * atk * vel * 0.26

def pad(ms, dur, vel=1.0):
    """Pad calido: dos saw desafinadas muy filtradas, con swell lento."""
    n = int(dur * SR); t = np.arange(n) / SR
    x = np.zeros(n)
    for m in ms:
        f = hz(m)
        for det in (-0.004, 0.004):
            ph = (t * f * (1 + det)) % 1
            x = x + (2 * ph - 1)
    x = lp(x / (2 * len(ms)), 620)
    swell = np.sin(np.pi * np.clip(t / dur, 0, 1)) ** 0.8
    return x * swell * vel * 0.16

def bajo(m, dur=3.4, vel=1.0):
    n = int(dur * SR); t = np.arange(n) / SR
    f = hz(m)
    x = np.sin(2 * np.pi * f * t) * np.exp(-t / 1.6) + 0.18 * np.sin(2 * np.pi * 2 * f * t) * np.exp(-t / 0.5)
    return x * np.minimum(1, t / 0.02) * vel * 0.22

# Am - F - C - G, dos compases cada uno
PROG = [([69, 72, 76, 72], [57, 60, 64], 45),
        ([65, 69, 72, 69], [53, 57, 60], 41),
        ([67, 72, 76, 72], [55, 60, 64], 48),
        ([67, 71, 74, 71], [55, 59, 62], 43)]

ciclo = len(PROG) * 2 * BAR                      # 30 s
n_tot = int((dur_total + 4) * SR)
L = np.zeros(n_tot); R = np.zeros(n_tot)

def add(buf, x, pos):
    i = int(pos * SR); j = min(i + len(x), len(buf))
    if i < len(buf): buf[i:j] += x[:j - i]

bar = 0
while bar * BAR < dur_total + 4:
    arp, acorde, raiz = PROG[(bar // 2) % len(PROG)]
    t0 = bar * BAR
    add(L, bajo(raiz), t0); add(R, bajo(raiz), t0 + 0.004)
    add(L, pad(acorde, 2 * BAR), t0); add(R, pad(acorde, 2 * BAR), t0 + 0.012)
    for k in range(8):                            # corcheas, el patron de 4 notas dos veces
        m = arp[k % 4] + (12 if (bar % 2 == 1 and k >= 6) else 0)
        vel = 1.0 if k % 2 == 0 else 0.62         # acento en el pulso
        pos = t0 + k * BEAT / 2
        pan = 0.5 + 0.18 * np.sin(k * 0.8)        # el arpegio se abre en estereo
        nota = piano(m, vel=vel)
        add(L, nota * (1 - pan) * 2 * 0.5, pos)
        add(R, nota * pan * 2 * 0.5, pos + 0.006)
    bar += 1

# reverb: convolucion con ruido que decae (sala chica y suave)
ir_n = int(1.9 * SR); ir_t = np.arange(ir_n) / SR
ir = lp(rng.standard_normal(ir_n), 4200) * np.exp(-ir_t / 0.55)
ir[:int(0.012 * SR)] = 0
ir /= np.abs(ir).sum() / 8
Lw = fftconvolve(L, ir)[:n_tot]; Rw = fftconvolve(R, ir * 0.96)[:n_tot]
L = 0.74 * L + 0.26 * Lw; R = 0.74 * R + 0.26 * Rw
L = hp(L, 45); R = hp(R, 45)

x = np.stack([L, R], 1)[:int(dur_total * SR)]
x *= 0.70 / max(1e-9, np.abs(x).max())
f_in = int(1.2 * SR); f_out = int(2.5 * SR)
x[:f_in] *= np.linspace(0, 1, f_in)[:, None]
x[-f_out:] *= np.linspace(1, 0, f_out)[:, None]
wavfile.write(out, SR, (x * 32767).astype(np.int16))
print(out, round(len(x) / SR, 2), 's', BPM, 'BPM')
