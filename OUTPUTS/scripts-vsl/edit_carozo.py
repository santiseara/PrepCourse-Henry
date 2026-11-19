#!/usr/bin/env python3
"""
Montaje del ad "Carozo de palta y artrosis" (clon del #25 de Emma Miller) para Protocolo Limpia Dolor.

Estructura que copia del original:
  - ~77 s de anuncio  +  ~30 s de cola de reloj
  - placa roja de apertura, b-rolls y renders 3D del original en sus tiempos,
    subtitulos propios (blanco + palabra clave amarilla, 63,5 % del alto),
    placa roja final con las 3 flechas.

Entradas (en ~/Desktop/limpia-dolor/work/):
  c25/avatar.mp4          video de avatar de HeyGen (1080x1920, 25 fps) con la voz
  c25/broll/*.mp4         tramos recortados del original (720x1280)
  c25/base-reloj.mp4      la cola de reloj del original
  c25/subtitulos.json     [{"t0":..,"t1":..,"texto":"..","clave":".."}]
"""
import json, os, subprocess, sys

FFMPEG = os.path.expanduser("~/bin/ffmpeg")
W = os.path.expanduser("~/Desktop/limpia-dolor/work")
FONT_PLACA = "/System/Library/Fonts/Supplemental/Arial Bold Italic.ttf"
FONT_SUB = os.path.expanduser("~/Library/Fonts/Rubik.ttf")
ROJO = "0xE01018"

# --- b-rolls: archivo -> (inicio, fin) en el tiempo del video NUEVO -------------
# Se completan desde broll_tiempos.json, que se calcula alineando el audio del avatar.
def cargar(nombre, defecto):
    p = os.path.join(W, "c25", nombre)
    if os.path.exists(p):
        return json.load(open(p))
    return defecto


def esc(t):
    """Escapa texto para drawtext."""
    return (t.replace("\\", "\\\\").replace(":", "\\:").replace("'", "’")
             .replace("%", "\\%").replace(",", "\\,"))


def construir(brolls, subs, salida, placa_fin_desde):
    inputs = ["-i", os.path.join(W, "c25/avatar.mp4")]
    for b in brolls:
        inputs += ["-i", os.path.join(W, "c25/broll", b["archivo"])]

    fc = []
    # base: el avatar ya viene 1080x1920
    fc.append("[0:v]scale=1080:1920,setsar=1,fps=30[base]")
    prev = "base"
    for i, b in enumerate(brolls, start=1):
        dur = b["t1"] - b["t0"]
        # el b-roll se escala, se recorta a la duracion y se corre al tiempo t0
        fc.append(
            f"[{i}:v]scale=1080:1920,setsar=1,fps=30,trim=0:{dur:.3f},"
            f"setpts=PTS-STARTPTS+{b['t0']:.3f}/TB[b{i}]"
        )
        fc.append(
            f"[{prev}][b{i}]overlay=0:0:enable='between(t,{b['t0']:.3f},{b['t1']:.3f})'[v{i}]"
        )
        prev = f"v{i}"

    # --- placa roja de apertura (sobre el primer b-roll, 0 a 5.2 s) -----------
    fc.append(
        f"[{prev}]drawbox=x=166:y=867:w=746:h=114:color={ROJO}:t=fill:enable='between(t,0,5.19)',"
        f"drawbox=x=6:y=985:w=1068:h=53:color={ROJO}:t=fill:enable='between(t,0,5.19)',"
        f"drawtext=fontfile='{FONT_PLACA}':text='ARTROSIS':fontcolor=white:fontsize=96:"
        f"borderw=3:bordercolor=white:x=166+(746-text_w)/2:y=867+(114-text_h)/2-8:enable='between(t,0,5.19)',"
        f"drawtext=fontfile='{FONT_PLACA}':text='CÓMO RESOLVERLA EN CASA':fontcolor=white:fontsize=52:"
        f"borderw=2:bordercolor=white:x=6+(1068-text_w)/2:y=985+(53-text_h)/2-5:enable='between(t,0,5.19)'[pa]"
    )
    prev = "pa"

    # --- placa roja final + 3 flechas ----------------------------------------
    f0 = placa_fin_desde
    fc.append(
        f"[{prev}]drawbox=x=40:y=1150:w=1000:h=92:color={ROJO}:t=fill:enable='gte(t,{f0:.2f})',"
        f"drawbox=x=40:y=1248:w=1000:h=92:color={ROJO}:t=fill:enable='gte(t,{f0:.2f})',"
        f"drawtext=fontfile='{FONT_PLACA}':text='RECETA COMPLETA':fontcolor=white:fontsize=74:"
        f"borderw=2:bordercolor=white:x=(w-text_w)/2:y=1150+(92-text_h)/2-6:enable='gte(t,{f0:.2f})',"
        f"drawtext=fontfile='{FONT_PLACA}':text='DEBAJO DEL VIDEO':fontcolor=white:fontsize=74:"
        f"borderw=2:bordercolor=white:x=(w-text_w)/2:y=1248+(92-text_h)/2-6:enable='gte(t,{f0:.2f})'[pf]"
    )
    prev = "pf"

    # --- subtitulos ----------------------------------------------------------
    partes = []
    for s in subs:
        txt = esc(s["texto"])
        partes.append(
            f"drawtext=fontfile='{FONT_SUB}':text='{txt}':fontcolor=white:fontsize=70:"
            f"borderw=7:bordercolor=black@0.85:shadowx=0:shadowy=4:shadowcolor=black@0.5:"
            f"x=(w-text_w)/2:y=1190:enable='between(t,{s['t0']:.2f},{s['t1']:.2f})'"
        )
    if partes:
        fc.append(f"[{prev}]" + ",".join(partes) + "[vf]")
        prev = "vf"
    else:
        fc.append(f"[{prev}]null[vf]")
        prev = "vf"

    cmd = [FFMPEG, "-v", "error", "-y"] + inputs + [
        "-filter_complex", ";".join(fc),
        "-map", f"[{prev}]", "-map", "0:a",
        "-c:v", "libx264", "-preset", "medium", "-crf", "19",
        "-pix_fmt", "yuv420p", "-r", "30",
        "-c:a", "aac", "-b:a", "160k", "-ar", "48000",
        salida,
    ]
    print("montando…")
    r = subprocess.run(cmd, capture_output=True)
    if r.returncode:
        print(r.stderr.decode()[-3000:])
        sys.exit(1)
    print("ok ->", salida)


if __name__ == "__main__":
    brolls = cargar("broll_tiempos.json", [])
    subs = cargar("subtitulos.json", [])
    fin = float(sys.argv[1]) if len(sys.argv) > 1 else 72.8
    construir(brolls, subs, os.path.join(W, "c25/ad_sin_reloj.mp4"), fin)
