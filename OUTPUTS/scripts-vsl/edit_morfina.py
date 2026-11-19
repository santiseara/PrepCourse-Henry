#!/usr/bin/env python3
"""
Montaje del ad #09 de Emma Miller ("Acaba com dor na coluna… com menos de R$8") para Limpia Dolor.

Este ad NO es un presentador a camara: es **voz en off sobre escena**, con dos pacientes
(doña Maria y don Antonio) que hacen pruebas de movilidad, y **tres voces**.

Por eso el armado va al reves que el del carozo: la linea de tiempo se construye **siguiendo
el audio**, no copiando los tiempos del original.
  - El audio del doctor sale de un solo video de avatar de HeyGen y se **corta en bloques**
    por sus pausas reales (silencedetect).
  - Entre bloque y bloque se intercalan las lineas de los pacientes, generadas aparte con las
    voces de la casa (Sulafat / Orus).
  - Cada tramo de video se **estira o encoge** para calzar con su bloque de audio, repartiendo
    la diferencia entre la velocidad del clip y la del audio para que no se note.
"""
import json, os, subprocess, sys

FF = os.path.expanduser("~/bin/ffmpeg")
LOCAL = sys.argv[1] if len(sys.argv) > 1 else "/tmp/morfina_render"
FONT = "/System/Library/Fonts/Supplemental/Arial Bold Italic.ttf"
ROJO = "0xE01018"

# bloques del doctor dentro del avatar, cortados en el medio de cada pausa
DOCTOR = [("A", 0.00, 7.30), ("B", 7.30, 18.12), ("C", 18.12, 22.84),
          ("D", 22.84, 31.04), ("E", 31.04, 35.24), ("F", 35.24, 72.04)]

# que se ve en cada bloque. fuente: "avatar" o un b-roll; None = sigue el avatar
PLAN = [
    ("A", "avatar",               None),
    ("B", "01_maria_presenta",    None),
    ("maria1", "02_maria_dice_no", "maria1"),
    ("C", "03_maria_toma",        None),
    ("maria2", "04_maria_logra",  "maria2"),
    ("D", "05_antonio_presenta",  None),
    ("antonio1", "06_antonio_dice_no", "antonio1"),
    ("E", "07_antonio_toma",      None),
    ("antonio2", "08_antonio_camina",  "antonio2"),
    ("F1", "09_explica",          None),
    ("F2", "avatar",              None),
]



def tramo_video(d_video, objetivo):
    """Filtro para que un clip de d_video segundos dure `objetivo`.

    Nunca acelera: si el clip sobra se recorta solo, y si falta se estira hasta 1,15
    y el resto se cubre congelando el ultimo cuadro (tpad).
    """
    base = "fps=30,scale=1080:1920,setsar=1"
    if d_video >= objetivo:
        return base
    factor = min(objetivo / d_video, 1.15)
    estirado = d_video * factor
    falta = objetivo - estirado
    f = f"setpts={factor:.4f}*PTS,{base}"
    if falta > 0.04:
        f += f",tpad=stop_mode=clone:stop_duration={falta + 0.2:.3f}"
    return f


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
    W = LOCAL
    os.makedirs(os.path.join(W, "piezas"), exist_ok=True)
    AV = os.path.join(W, "avatar.mp4")
    BR = os.path.join(W, "broll")
    VOZ = os.path.join(W, "voces")

    bloques = {k: (a, b) for k, a, b in DOCTOR}
    # el bloque F se parte en dos: lo que cubre el b-roll de "explica" y el resto a camara
    fa, fb = bloques["F"]
    d_explica = dur(os.path.join(BR, "09_explica.mp4"))
    bloques["F1"] = (fa, fa + d_explica)
    bloques["F2"] = (fa + d_explica, fb)

    piezas = []
    for i, (clave, fuente, voz) in enumerate(PLAN):
        out = os.path.join(W, "piezas", f"{i:02d}_{clave}.mp4")
        if voz:  # linea de un paciente: el audio manda
            wav = os.path.join(VOZ, voz + ".wav")
            d_audio = dur(wav)
            src = os.path.join(BR, fuente + ".mp4")
            d_video = dur(src)
            # el audio manda. el video NUNCA se acelera (se ve mal): si sobra metraje se
            # recorta, y si falta se estira hasta 1,15 y lo que reste se cubre congelando
            # el ultimo cuadro, que en una escena quieta no se nota.
            objetivo = d_audio
            vf = tramo_video(d_video, objetivo)
            run([FF, "-v", "error", "-y", "-i", src, "-i", wav,
                 "-filter_complex",
                 f"[0:v]{vf}[v];[1:a]aresample=48000[a]",
                 "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-preset", "medium", "-crf", "19",
                 "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k", "-t", f"{objetivo:.3f}", out],
                f"{clave} ({objetivo:.2f}s, video {d_video:.2f}s)")
        else:  # bloque del doctor: el audio sale del avatar
            a, b = bloques[clave]
            d_bloque = b - a
            if fuente == "avatar":
                run([FF, "-v", "error", "-y", "-ss", f"{a:.3f}", "-t", f"{d_bloque:.3f}", "-i", AV,
                     "-vf", "fps=30,scale=1080:1920,setsar=1",
                     "-c:v", "libx264", "-preset", "medium", "-crf", "19", "-pix_fmt", "yuv420p",
                     "-c:a", "aac", "-b:a", "160k", "-ar", "48000", out], f"{clave} avatar ({d_bloque:.2f}s)")
            else:
                src = os.path.join(BR, fuente + ".mp4")
                d_video = dur(src)
                vf = tramo_video(d_video, d_bloque)
                run([FF, "-v", "error", "-y", "-i", src, "-ss", f"{a:.3f}", "-t", f"{d_bloque:.3f}", "-i", AV,
                     "-filter_complex", f"[0:v]{vf}[v]",
                     "-map", "[v]", "-map", "1:a", "-c:v", "libx264", "-preset", "medium", "-crf", "19",
                     "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k", "-ar", "48000",
                     "-t", f"{d_bloque:.3f}", out], f"{clave} {fuente} ({d_bloque:.2f}s, video {d_video:.2f}s)")
        piezas.append(out)

    lista = os.path.join(W, "lista.txt")
    with open(lista, "w") as f:
        for p in piezas:
            f.write(f"file '{p}'\n")
    run([FF, "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lista,
         "-c:v", "libx264", "-preset", "medium", "-crf", "19", "-pix_fmt", "yuv420p", "-r", "30",
         "-c:a", "aac", "-b:a", "160k", "-ar", "48000", os.path.join(W, "ad_sin_placas.mp4")], "union")
    print("\nlisto ->", os.path.join(W, "ad_sin_placas.mp4"), f"({dur(os.path.join(W,'ad_sin_placas.mp4')):.2f}s)")


if __name__ == "__main__":
    main()
