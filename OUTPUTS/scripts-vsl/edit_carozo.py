#!/usr/bin/env python3
"""
Montaje del ad "Carozo de palta y artrosis" (clon del #25 de Emma Miller) para Protocolo Limpia Dolor.

Estructura que copia del original:
  ~77 s de anuncio + placa de cierre + ~30 s de cola de reloj.

Lo importante: el original alterna planos a pantalla completa con **pantalla partida**
(el presentador arriba, el b-roll abajo). En los tramos partidos NO se usa el video de
ellos arriba —se le verian los labios en portugues—: arriba va **nuestro avatar** y del
b-roll se superpone **solo la mitad de abajo**, a partir de la linea de division medida
para ese clip (`div` en broll_tiempos.json; `div: 0` = el b-roll va a pantalla completa).

Entradas (en ~/Desktop/limpia-dolor/work/c25/):
  avatar.mp4            video de avatar de HeyGen (1080x1920) con la voz
  broll_limpio/*.mp4    tramos del original ya sin el subtitulo en portugues
  broll_tiempos.json    [{archivo, t0, t1, div}]
  subs.ass              subtitulos propios
  cierre.mp4, reloj.mp4, audio_cierre.m4a, audio_reloj.m4a
  musica.mp3            la musica de suspenso de Santiago (la misma de higado-liviano)
"""
import json, os, subprocess, sys

FF = os.path.expanduser("~/bin/ffmpeg")
# El Escritorio esta en iCloud y tira "Operation timed out" en medio de un render:
# los insumos se copian a disco local (LOCAL/c25/...) y se trabaja desde ahi.
LOCAL = sys.argv[1] if len(sys.argv) > 1 else "/tmp/carozo_render"
W = LOCAL
FONT_PLACA = "/System/Library/Fonts/Supplemental/Arial Bold Italic.ttf"
ROJO = "0xE01018"
MUSICA_VOL = 0.15  # mediano, y ademas baja sola bajo la voz


def run(cmd, que):
    r = subprocess.run(cmd, capture_output=True)
    if r.returncode:
        print(f"FALLO {que}:\n" + r.stderr.decode()[-1800:])
        sys.exit(1)
    print("ok:", que)


def parte1(dest):
    br = json.load(open(os.path.join(W, "c25/broll_tiempos.json")))
    ins = ["-i", os.path.join(W, "c25/avatar.mp4")]
    for b in br:
        ins += ["-i", os.path.join(W, "c25/broll_limpio", b["archivo"])]

    fc = ["[0:v]scale=1080:1920,setsar=1,fps=30[base]"]
    prev = "base"
    for i, b in enumerate(br, start=1):
        d = b["t1"] - b["t0"]
        div = b.get("div", 0)
        if div:   # pantalla partida: solo la mitad de abajo del b-roll
            alto = 1920 - div
            fc.append(f"[{i}:v]scale=1080:1920,setsar=1,fps=30,crop=1080:{alto}:0:{div},"
                      f"trim=0:{d:.3f},setpts=PTS-STARTPTS+{b['t0']:.3f}/TB[b{i}]")
            fc.append(f"[{prev}][b{i}]overlay=0:{div}:enable='between(t,{b['t0']:.3f},{b['t1']:.3f})'[v{i}]")
        else:     # pantalla completa
            fc.append(f"[{i}:v]scale=1080:1920,setsar=1,fps=30,"
                      f"trim=0:{d:.3f},setpts=PTS-STARTPTS+{b['t0']:.3f}/TB[b{i}]")
            fc.append(f"[{prev}][b{i}]overlay=0:0:enable='between(t,{b['t0']:.3f},{b['t1']:.3f})'[v{i}]")
        prev = f"v{i}"

    fc.append(
        f"[{prev}]"
        f"drawbox=x=166:y=867:w=746:h=114:color={ROJO}:t=fill:enable='between(t,0,5.48)',"
        f"drawbox=x=6:y=985:w=1068:h=53:color={ROJO}:t=fill:enable='between(t,0,5.48)',"
        f"drawtext=fontfile='{FONT_PLACA}':text='ARTROSIS':fontcolor=white:fontsize=96:"
        f"borderw=3:bordercolor=white:x=166+(746-text_w)/2:y=867+(114-text_h)/2-8:enable='between(t,0,5.48)',"
        f"drawtext=fontfile='{FONT_PLACA}':text='CÓMO RESOLVERLA EN CASA':fontcolor=white:fontsize=52:"
        f"borderw=2:bordercolor=white:x=6+(1068-text_w)/2:y=985+(53-text_h)/2-5:enable='between(t,0,5.48)'[vf]")

    run([FF, "-v", "error", "-y"] + ins + [
        "-filter_complex", ";".join(fc), "-map", "[vf]", "-map", "0:a",
        "-c:v", "libx264", "-preset", "medium", "-crf", "19", "-pix_fmt", "yuv420p", "-r", "30",
        "-c:a", "aac", "-b:a", "160k", "-ar", "48000", dest], "parte 1 (avatar + b-rolls + placa)")


def subtitular(src, dest):
    run([FF, "-v", "error", "-y", "-i", src,
         "-vf", f"subtitles={os.path.join(W,'c25/subs.ass')}:fontsdir=/tmp/assfonts",
         "-c:v", "libx264", "-preset", "medium", "-crf", "19", "-pix_fmt", "yuv420p", "-r", "30",
         "-c:a", "copy", dest], "subtitulos")


def cola(dest_p2, dest_p3):
    for v, a, dest, que in [("cierre.mp4", "audio_cierre.m4a", dest_p2, "cierre"),
                            ("reloj.mp4", "audio_reloj.m4a", dest_p3, "reloj")]:
        run([FF, "-v", "error", "-y", "-i", os.path.join(W, "c25", v), "-i", os.path.join(W, "c25", a),
             "-map", "0:v", "-map", "1:a", "-c:v", "libx264", "-preset", "medium", "-crf", "19",
             "-pix_fmt", "yuv420p", "-r", "30", "-c:a", "aac", "-b:a", "160k", "-ar", "48000",
             "-shortest", dest], que)


def unir(p1, p2, p3, dest):
    lista = os.path.join(LOCAL, "lista.txt")
    with open(lista, "w") as f:
        for p in (p1, p2, p3):
            f.write(f"file '{p}'\n")
    run([FF, "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lista,
         "-c:v", "copy", "-c:a", "aac", "-b:a", "160k", "-ar", "48000", dest], "union")


def con_musica(src, dest):
    """Musica de suspenso de fondo, en volumen mediano y con ducking bajo la voz."""
    run([FF, "-v", "error", "-y", "-i", src, "-stream_loop", "-1", "-i", os.path.join(W, "c25/musica.mp3"),
         "-filter_complex",
         f"[1:a]volume={MUSICA_VOL},afade=t=in:st=0:d=1.5[mus];"
         f"[0:a]asplit=2[voz][sc];"
         f"[mus][sc]sidechaincompress=threshold=0.045:ratio=6:attack=12:release=420[musd];"
         f"[voz][musd]amix=inputs=2:duration=first:dropout_transition=0,"
         f"loudnorm=I=-14:TP=-1.5:LRA=11[a]",
         "-map", "0:v", "-map", "[a]", "-c:v", "copy",
         "-c:a", "aac", "-b:a", "160k", "-ar", "48000", "-shortest", dest], "mezcla con musica")


if __name__ == "__main__":
    os.makedirs(LOCAL, exist_ok=True)
    p1 = os.path.join(LOCAL, "parte1.mp4")
    p1s = os.path.join(LOCAL, "parte1_subs.mp4")
    p2 = os.path.join(LOCAL, "p2.mp4")
    p3 = os.path.join(LOCAL, "p3.mp4")
    sin = os.path.join(LOCAL, "sin_musica.mp4")
    fin = os.path.join(LOCAL, "FINAL.mp4")
    parte1(p1)
    subtitular(p1, p1s)
    cola(p2, p3)
    unir(p1s, p2, p3, sin)
    con_musica(sin, fin)
    print("\nlisto ->", fin)
