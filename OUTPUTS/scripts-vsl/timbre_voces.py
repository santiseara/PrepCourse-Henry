"""Chequeo de voces cruzadas sin librosa: MFCC medio por linea (torchaudio) y distancia coseno
entre lineas del mismo personaje vs. del otro. Uso: python3 timbre.py <proyecto>"""
import json, os, sys, subprocess, numpy as np, torch, torchaudio
P = os.path.abspath(sys.argv[1]); FF = os.path.expanduser("~/bin/ffmpeg")
BOR = json.load(open(f"{P}/bordes.json")); TMP = "/tmp/timbre.wav"
MF = torchaudio.transforms.MFCC(sample_rate=16000, n_mfcc=20, melkwargs={"n_fft": 400, "hop_length": 160, "n_mels": 40})
segs = []
for tid, b in BOR.items():
    for (l0, l1, p, txt, _) in b.get("lineas", []):
        subprocess.run([FF, "-v", "error", "-y", "-ss", str(l0), "-to", str(l1), "-i", f"{P}/clips/{tid}.mp4",
                        "-ac", "1", "-ar", "16000", "-f", "wav", TMP], check=True)
        y, sr = torchaudio.load(TMP)
        m = MF(y)[0]
        v = m.mean(1).numpy(); v = v / np.linalg.norm(v)
        segs.append((tid, p, v, txt[:45]))
print(f"{len(segs)} lineas")
for i, (t1, p1, v1, x1) in enumerate(segs):
    prop = [(float(np.dot(v1, v2)), p2, t2) for j, (t2, p2, v2, _) in enumerate(segs) if j != i]
    prop.sort(reverse=True)
    mejor = prop[0]
    mismo = np.mean([s for s, p2, _ in prop if p2 == p1]) if any(p2 == p1 for _, p2, _ in prop) else float("nan")
    otro = np.mean([s for s, p2, _ in prop if p2 != p1]) if any(p2 != p1 for _, p2, _ in prop) else float("nan")
    flag = "  <- SOSPECHA" if otro > mismo else ""
    print(f"{t1:4} [{p1}] mismo={mismo:.3f} otro={otro:.3f} top={mejor[1]}({mejor[2]}) {mejor[0]:.3f}{flag}  «{x1}»")
