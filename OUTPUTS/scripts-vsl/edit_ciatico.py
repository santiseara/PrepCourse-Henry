#!/usr/bin/env python3
"""
Montaje del ad #21 de Emma Miller ("Dor forte no ciatico e nas costas?") para Limpia Dolor.

Es un **podcast de dos personas**: el doctor mayor y el entrevistador joven se van turnando.
Por eso hay dos videos de avatar, cada uno con su voz:
  - el mayor, con la voz `damian` de la cuenta de HeyGen
  - el joven, con **Orus** generado por API y subido a HeyGen como audio propio, para que
    le haga el lip sync (en la cuenta hay una sola voz masculina y hacian falta dos)

Como en el #09, la linea de tiempo la manda el audio: cada avatar se corta en sus bloques
por las pausas reales y se van intercalando, con los b-rolls del original encima.
"""
import json, os, subprocess, sys

FF = os.path.expanduser("~/bin/ffmpeg")
S = sys.argv[1] if len(sys.argv) > 1 else "/tmp/ciatico_render"

# bloques de cada avatar, cortados en el medio de sus pausas
MAYOR = [("M1", 0.00, 11.05), ("M2", 11.05, 37.60), ("M3", 37.60, 51.08)]
JOVEN = [("J1", 0.00, 4.00), ("J2", 4.00, 5.70), ("J3", 5.70, 13.00)]

# orden del ad: (bloque, de que avatar, que b-roll encima o None = se ve el avatar)
# Casi todos los "b-rolls" de este ad son **el presentador de ellos hablando** con un
# grafico encima, no b-rolls puros. Si se superponen enteros, arriba queda su boca
# moviendose en portugues. Por eso cada uno lleva `div`:
#   div=0   -> el clip va a pantalla completa (es un b-roll de verdad)
#   div=N   -> solo se superpone **de y=N para abajo**; arriba queda nuestro avatar
#   None    -> el clip se descarta (es solo el presentador hablando, sin grafico que valga)
BROLL = {
    "01_espalda":      0,     # otro actor mostrando la espalda: va entero
    "02_ibuprofeno":   None,  # es el mayor hablando
    "03_reloj":        900,   # la licuadora con el jugo, abajo
    "04_ingredientes": 1150,  # el reloj azul flotando
    "05_parasito":     None,  # el mayor con un parasito translucido encima
    "06_tension":      930,   # la taza de te, abajo
    "07_rodilla":      1000,  # la pierna, abajo
    "08_licuadora":    980,   # la caja de remedios, abajo
    "09_boton":        None,  # es el joven hablando: queda nuestro avatar
}

PLAN = [
    ("M1", "mayor", ["01_espalda", "02_ibuprofeno"]),
    ("J1", "joven", None),
    ("M2", "mayor", ["03_reloj", "04_ingredientes", "05_parasito", "06_tension", "07_rodilla"]),
    ("J2", "joven", None),
    ("M3", "mayor", ["08_licuadora"]),
    ("J3", "joven", ["09_boton"]),
]


def dur(path):
    out = subprocess.run([FF, "-hide_banner", "-i", path], capture_output=True).stderr.decode()
    for ln in out.splitlines():
        if "Duration:" in ln:
            h, m, s = ln.split("Duration:")[1].split(",")[0].strip().split(":")
            return int(h) * 3600 + int(m) * 60 + float(s)
    return 0.0


def run(cmd, que):
    r = subprocess.run(cmd, capture_output=True)
    if r.returncode:
        print(f"FALLO {que}:\n" + r.stderr.decode()[-1500:])
        sys.exit(1)
    print("  ok:", que)


def main():
    os.makedirs(os.path.join(S, "piezas"), exist_ok=True)
    bloques = {k: (a, b) for k, a, b in MAYOR + JOVEN}
    piezas = []
    for i, (clave, quien, brolls) in enumerate(PLAN):
        a, b = bloques[clave]
        d = b - a
        src = os.path.join(S, f"avatar_{quien}.mp4")
        out = os.path.join(S, "piezas", f"{i:02d}_{clave}.mp4")
        if not brolls:
            run([FF, "-v", "error", "-y", "-ss", f"{a:.3f}", "-t", f"{d:.3f}", "-i", src,
                 "-vf", "fps=30,scale=1080:1920,setsar=1",
                 "-c:v", "libx264", "-preset", "medium", "-crf", "19", "-pix_fmt", "yuv420p",
                 "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2", out], f"{clave} ({d:.2f}s)")
        else:
            # el avatar es la base y los b-rolls se superponen uno tras otro
            ins = ["-ss", f"{a:.3f}", "-t", f"{d:.3f}", "-i", src]
            for n in brolls:
                ins += ["-i", os.path.join(S, "broll", n + ".mp4")]
            fc = ["[0:v]fps=30,scale=1080:1920,setsar=1[base]"]
            prev, t = "base", 0.0
            for j, n in enumerate(brolls, start=1):
                db = min(dur(os.path.join(S, "broll", n + ".mp4")), max(0.1, d - t))
                div = BROLL.get(n, 0)
                if div is None:   # descartado: se ve nuestro avatar y el tiempo igual corre
                    t += db
                    if t >= d:
                        break
                    continue
                if div:           # solo de la linea para abajo
                    alto = 1920 - div
                    fc.append(f"[{j}:v]fps=30,scale=1080:1920,setsar=1,crop=1080:{alto}:0:{div},"
                              f"trim=0:{db:.3f},setpts=PTS-STARTPTS+{t:.3f}/TB[b{j}]")
                    fc.append(f"[{prev}][b{j}]overlay=0:{div}:"
                              f"enable='between(t,{t:.3f},{t+db:.3f})'[v{j}]")
                else:             # pantalla completa
                    fc.append(f"[{j}:v]fps=30,scale=1080:1920,setsar=1,trim=0:{db:.3f},"
                              f"setpts=PTS-STARTPTS+{t:.3f}/TB[b{j}]")
                    fc.append(f"[{prev}][b{j}]overlay=0:0:enable='between(t,{t:.3f},{t+db:.3f})'[v{j}]")
                prev = f"v{j}"
                t += db
                if t >= d:
                    break
            fc.append(f"[{prev}]null[vf]")
            run([FF, "-v", "error", "-y"] + ins + ["-filter_complex", ";".join(fc),
                 "-map", "[vf]", "-map", "0:a", "-c:v", "libx264", "-preset", "medium", "-crf", "19",
                 "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
                 "-t", f"{d:.3f}", out], f"{clave} ({d:.2f}s, {len(brolls)} b-rolls)")
        piezas.append(out)

    lista = os.path.join(S, "lista.txt")
    with open(lista, "w") as f:
        for p in piezas:
            f.write(f"file '{p}'\n")
    run([FF, "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lista,
         "-c:v", "libx264", "-preset", "medium", "-crf", "19", "-pix_fmt", "yuv420p", "-r", "30",
         "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2", os.path.join(S, "ad.mp4")], "union")
    print("\nlisto ->", os.path.join(S, "ad.mp4"), f"({dur(os.path.join(S,'ad.mp4')):.2f}s)")


if __name__ == "__main__":
    main()
