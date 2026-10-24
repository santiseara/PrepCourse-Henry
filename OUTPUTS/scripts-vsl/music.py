"""Pista original activa para el VSL (118 BPM, Am-F-C-G). Uso: python3 music.py <segundos> <salida.wav>"""
import sys, numpy as np
from scipy.signal import butter, sosfilt
from scipy.io import wavfile

SR = 44100
BPM = 118
BEAT = 60 / BPM
BAR = 4 * BEAT
dur_total = float(sys.argv[1]); out = sys.argv[2]
rng = np.random.default_rng(7)

def lp(x, f, order=2):
    return sosfilt(butter(order, f, 'low', fs=SR, output='sos'), x)
def hp(x, f, order=2):
    return sosfilt(butter(order, f, 'high', fs=SR, output='sos'), x)
def env(n, a=0.005, d=0.2, s=0.0, total=None):
    t = np.arange(n) / SR
    e = np.minimum(1, t / a) * (s + (1 - s) * np.exp(-t / d))
    return e
def note_hz(m): return 440 * 2 ** ((m - 69) / 12)
def saw(f, n, det=0.0):
    t = np.arange(n) / SR
    out = 0
    for dd in (-det, 0, det):
        ph = (t * f * (1 + dd)) % 1
        out = out + (2 * ph - 1)
    return out / 3

# ---- sonidos ----
def kick():
    n = int(0.35 * SR); t = np.arange(n) / SR
    f = 50 + 90 * np.exp(-t / 0.04)
    ph = 2 * np.pi * np.cumsum(f) / SR
    return np.sin(ph) * np.exp(-t / 0.12) * 0.9
def clap():
    n = int(0.25 * SR); x = rng.standard_normal(n)
    x = hp(lp(x, 4000), 900)
    t = np.arange(n) / SR
    e = np.exp(-t / 0.07) * (1 + 0.6 * (np.sin(2 * np.pi * 90 * t) > 0))
    return x * e * 0.35
def hat(open_=False):
    n = int((0.18 if open_ else 0.05) * SR); x = hp(rng.standard_normal(n), 7000, 4)
    t = np.arange(n) / SR
    return x * np.exp(-t / (0.06 if open_ else 0.015)) * 0.18

KICK, CLAP, HAT, OHAT = kick(), clap(), hat(), hat(True)

# progresión: Am F C G  (raíces MIDI)
prog = [[57, 60, 64], [53, 57, 60], [48, 52, 55], [55, 59, 62]]
roots = [45, 41, 48, 43]

def bars(nbars, arp=True, drums=True, bass=True, intro=False):
    n = int(nbars * BAR * SR)
    L = np.zeros(n); R = np.zeros(n); K = np.zeros(n)
    def add(buf, x, t0, g=1.0):
        i = int(t0 * SR); j = min(n, i + len(x))
        if i < n: buf[i:j] += x[:j - i] * g
    pump = np.ones(n)
    for b in range(nbars):
        chord = prog[b % 4]; root = roots[b % 4]; t_bar = b * BAR
        # pad (acorde sostenido, filtrado)
        m = int(BAR * SR)
        pad = sum(saw(note_hz(c + 12), m, 0.004) for c in chord) / 3
        pad = lp(pad, 1800 if not intro else 1100) * env(m, a=0.08, d=10, s=0.8) * 0.16
        add(L, pad, t_bar); add(R, np.roll(pad, 300), t_bar)
        for q in range(4):
            tb = t_bar + q * BEAT
            if drums:
                add(K, KICK, tb)
                ip = int(tb * SR); k = int(0.22 * SR)
                if ip < n:
                    seg = pump[ip:ip + k]; seg *= np.linspace(0.35, 1, len(seg)) ** 1.5
                if q in (1, 3):
                    add(L, CLAP, tb, 0.9); add(R, CLAP, tb + 0.004, 0.9)
            # hats en contratiempo (también en la intro, más suaves)
            h = OHAT if (q == 3 and b % 2 == 1) else HAT
            add(L, h, tb + BEAT / 2, 0.6 if intro else 1.0); add(R, h, tb + BEAT / 2 + 0.002, 0.8 if intro else 1.1)
            if drums:
                add(L, HAT, tb, 0.45); add(R, HAT, tb, 0.35)
            # bajo en corcheas
            if bass:
                for e8 in range(2):
                    nb = int(BEAT / 2 * SR * 0.9)
                    x = lp(saw(note_hz(root + (12 if e8 == 1 else 0)), nb, 0.002), 380) * env(nb, a=0.004, d=0.18) * 0.42
                    add(L, x, tb + e8 * BEAT / 2); add(R, x, tb + e8 * BEAT / 2)
            # arpegio en semicorcheas
            if arp:
                for s16 in range(4):
                    idx = (q * 4 + s16)
                    pitch = chord[[0, 1, 2, 1][idx % 4]] + 24 + (12 if idx % 8 == 7 else 0)
                    ns = int(BEAT / 4 * SR)
                    t = np.arange(ns) / SR
                    tri = 2 * np.abs(2 * ((t * note_hz(pitch)) % 1) - 1) - 1
                    x = tri * np.exp(-t / 0.07) * 0.085
                    pan = 0.5 + 0.35 * np.sin(idx)
                    add(L, x, tb + s16 * BEAT / 4, 1.4 * (1 - pan)); add(R, x, tb + s16 * BEAT / 4, 1.4 * pan)
    # efecto "pump" (sidechain) sobre todo menos el bombo
    L = L * pump + K; R = R * pump + K
    return np.stack([L, R], 1)

# estructura: intro 2 compases, después bloques de 8 alternando arpegio
parts = [bars(2, arp=False, drums=False, bass=False, intro=True)]
total = 2 * BAR; k = 0
while total < dur_total + BAR:
    parts.append(bars(8, arp=(k % 3 != 0), drums=True, bass=True)); total += 8 * BAR; k += 1
mix = np.concatenate(parts)[: int((dur_total) * SR)]
# fade out de 2.5 s y normalización suave
fo = int(2.5 * SR); mix[-fo:] *= np.linspace(1, 0, fo)[:, None]
mix = np.tanh(mix * 1.2) / np.tanh(1.2)
mix /= np.max(np.abs(mix)) * 1.05
wavfile.write(out, SR, (mix * 32767).astype(np.int16))
print('ok', out, round(len(mix) / SR, 1), 's')
