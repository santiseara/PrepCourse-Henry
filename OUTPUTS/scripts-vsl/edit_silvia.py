"""Montaje de los ads de Silvia Fitness · Adiós Panza (2026-11-16), con la edición de Belu Fitness clonada:
  - experta a cámara en tomas de Veo 3.1, jump cut seco entre tomas, zoom alternado 1.00 / 1.10
  - subtítulo de UNA palabra, MAYÚSCULAS, rosa con borde blanco, a media altura, con pop de entrada
  - inserts del producto (planilla, grilla, receta, video, app, bonos) chicos al centro, anclados a la palabra que los nombra
  - cartel de "respuesta a comentario" estilo TikTok (V4/V5) todo el video
  - música original baja debajo de la voz (Belu nunca baja de -45 dB), loudnorm -14 LUFS, 1080x1920 a 30 fps
  - formato mudo (V6): pantalla partida, sentadillas arriba y mate abajo, textos estilo TikTok y banda roja de cupos
Los bordes de cada toma y el tiempo de cada palabra salen de bordes.json (alineación forzada MMS de verif.py), nunca de Whisper.
Uso: python3 edit_silvia.py <proyecto> <V1..V6> <salida.mp4>
"""
import os, sys, json, subprocess, re
sys.path.insert(0, os.path.expanduser("~/.claude/skills/mini-novela/scripts"))
import comun as C
from PIL import Image, ImageDraw, ImageFont, ImageFilter

P, G = C.proyecto(sys.argv[1]); V = sys.argv[2]; OUT = os.path.abspath(sys.argv[3])
B = json.load(open(f"{P}/bordes.json"))
TMP = f"{P}/build/{V}"; os.makedirs(TMP, exist_ok=True)
FF = C.FF; W, H, FPS = 1080, 1920, 30
FD = os.path.expanduser("~/PrepCourse-Henry/OUTPUTS/scripts-producto/fonts")
MUSIC = os.path.expanduser("~/PrepCourse-Henry/OUTPUTS/scripts-vsl/music_activa.py")
EMO = "/System/Library/Fonts/Apple Color Emoji.ttc"
def run(c): subprocess.run(c, check=True)

PLANES = {
    "V1": dict(tomas=["A1", "A2", "A3", "A4", "A5", "A6"],
               ins={"planillas": "planilla", "grilla": "grilla", "recetas": "receta", "regalo": "bonos"}),
    "V2": dict(tomas=["B1", "B2", "B3", "B4", "B5", "B6"],
               ins={"videos": "video", "grilla": "grilla", "recetas": "receta", "bonos": "bonos"}),
    "V3": dict(tomas=["C1", "C2", "C3", "C4", "C5"],
               ins={"planilla": "planilla", "video": "video", "grilla": "grilla", "recetas": "receta", "sumate": "app"}),
    "V4": dict(tomas=["H1", "H2", "H3"], ins={"método": "app"},   # rehecho el 16/11 en el sillón (D era muy brillante)
               comment=("lu.martinez_", "Yo necesito bajar la panza ya, el mes que viene sí o sí arranco el gym 😩")),
    "V5": dict(tomas=["E1", "E2", "E3", "E4"], ins={"nivel": "planilla", "catorce": "grilla"},
               comment=("caro.gomez", "¿Sirve si nunca entrené en mi vida? 🙈")),
}
SP = 1.25   # Belu habla rápido (~3,5 palabras por segundo)


def font(p, s): return ImageFont.truetype(f"{FD}/{p}", s)


def emoji_img(ch, size):
    im = Image.new("RGBA", (200, 200), (0, 0, 0, 0))
    ImageDraw.Draw(im).text((0, 0), ch, font=ImageFont.truetype(EMO, 160), embedded_color=True)
    return im.crop(im.getbbox()).resize((size, size), Image.LANCZOS)


def text_with_emoji(d, im, xy, txt, fnt, fill, esize):
    """Escribe texto que puede terminar en un emoji (Barlow no tiene emojis)."""
    m = re.match(r"^(.*?)\s*([\U0001F300-\U0001FAFF☀-➿]+)$", txt)
    body, em = (m.group(1), m.group(2)) if m else (txt, "")
    d.text(xy, body, font=fnt, fill=fill)
    if em:
        x = xy[0] + d.textlength(body + " ", font=fnt)
        im.alpha_composite(emoji_img(em[0], esize), (int(x), int(xy[1] + 4)))


def wrap(d, txt, fnt, maxw):
    out, cur = [], ""
    for w in txt.split():
        t = (cur + " " + w).strip()
        if d.textlength(t, font=fnt) <= maxw: cur = t
        else: out.append(cur); cur = w
    return out + [cur]


def comment_card(user, txt):
    """Cartel de respuesta a comentario estilo TikTok."""
    w = 820; f1 = font("Barlow-SemiBold.ttf", 30); f2 = font("Barlow-Bold.ttf", 42)
    dd = ImageDraw.Draw(Image.new("RGB", (10, 10))); lines = wrap(dd, txt, f2, w - 80)
    h = 96 + 56 * len(lines) + 30
    im = Image.new("RGBA", (w + 40, h + 40), (0, 0, 0, 0))
    sh = Image.new("RGBA", im.size, (0, 0, 0, 0)); ImageDraw.Draw(sh).rounded_rectangle((20, 26, 20 + w, 26 + h), 26, fill=(0, 0, 0, 80))
    im = Image.alpha_composite(im, sh.filter(ImageFilter.GaussianBlur(10))); d = ImageDraw.Draw(im)
    d.rounded_rectangle((20, 20, 20 + w, 20 + h), 26, fill=(255, 255, 255))
    d.ellipse((50, 44, 98, 92), fill=(242, 182, 210)); d.text((74, 68), user[0].upper(), font=font("Montserrat-ExtraBold.ttf", 26), fill=(74, 21, 48), anchor="mm")
    d.text((112, 52), f"Respondé el comentario de {user}", font=f1, fill=(110, 110, 110))
    y = 116
    for k, ln in enumerate(lines):
        if k == len(lines) - 1: text_with_emoji(d, im, (60, y), ln, f2, (20, 20, 20), 42)
        else: d.text((60, y), ln, font=f2, fill=(20, 20, 20))
        y += 56
    p = f"{TMP}/comment.png"; im.save(p); return p


def ass_time(t):
    t = max(0, t); return f"{int(t // 3600)}:{int(t % 3600 // 60):02d}:{t % 60:05.2f}"


ASS_HEAD = """[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 2

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: W,Montserrat ExtraBold,{fs},&H00B84FFF,&H00FFFFFF,&H00FFFFFF,&H64000000,-1,0,0,0,100,100,0,0,1,7,3,5,40,40,0,1
{extra}
[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""


def speech_plan(plan):
    """Corta cada toma a sus bordes, la acelera y devuelve los segmentos + palabras con tiempos en el video final."""
    segs, words, t0 = [], [], 0.0
    for k, tid in enumerate(plan["tomas"]):
        b = B[tid]; a, z = b["a"], b["b"]; clip = f"{P}/clips/{tid}.mp4"
        zoom = 1.0 if k % 2 == 0 else 1.10
        cw, ch = int(720 / zoom) // 2 * 2, int(1280 / zoom) // 2 * 2
        seg = f"{TMP}/s{k}.mp4"
        run([FF, "-loglevel", "error", "-y", "-ss", f"{a:.3f}", "-to", f"{z:.3f}", "-i", clip,
             "-vf", f"scale=720:1280,crop={cw}:{ch}:(iw-{cw})/2:(ih-{ch})/3,scale={W}:{H},setpts=PTS/{SP},fps={FPS}",
             "-af", f"atempo={SP},aresample=48000", "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-c:a", "aac", "-b:a", "192k", seg])
        d = C.dur(seg)
        line = b["lineas"][0]; txt = line[3]; wt = line[4]
        orig = [w for w in txt.split() if C.norm(w)]
        j = 0
        for w in orig:
            n = len(C.norm(w)); ws = wt[j:j + n]; j += n
            if not ws: continue
            s, e = (ws[0][0] - a) / SP + t0, (ws[-1][1] - a) / SP + t0
            words.append((s, e, w))
        segs.append(seg); t0 += d
    return segs, words, t0


def build_talk(plan):
    segs, words, total = speech_plan(plan)
    lst = f"{TMP}/list.txt"; open(lst, "w").write("".join(f"file '{s}'\n" for s in segs))
    cat = f"{TMP}/cat.mp4"; run([FF, "-loglevel", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", cat])
    total = C.dur(cat)
    # subtítulos de una palabra (con pop)
    ycen = 960 if plan.get("comment") else 1010
    ev = []
    for k, (s, e, w) in enumerate(words):
        nxt = words[k + 1][0] if k + 1 < len(words) else e + 0.3
        end = min(max(e, s + 0.18), nxt) if nxt - e < 0.6 else e + 0.15
        clean = re.sub(r"[¿?¡!.,:;\"«»]", "", w).upper()
        fs = 92 if len(clean) <= 11 else int(92 * 11 / len(clean))
        ev.append(f"Dialogue: 1,{ass_time(s)},{ass_time(end)},W,,0,0,0,,{{\\pos(540,{ycen})\\fs{fs}\\fscx70\\fscy70\\t(0,70,\\fscx112\\fscy112)\\t(70,140,\\fscx100\\fscy100)}}{clean}")
    ass = f"{TMP}/subs.ass"; open(ass, "w").write(ASS_HEAD.format(fs=92, extra="") + "\n".join(ev) + "\n")
    # inserts anclados a la palabra
    ov, inputs = [], []
    used = set()
    for key, img in plan["ins"].items():
        hit = next(((s, e, w) for s, e, w in words if C.norm(w) and C.norm(w)[0] == C.norm(key)[0] and img not in used), None)
        if not hit: print("  (sin palabra para insert)", key); continue
        used.add(img); s = hit[0] - 0.05
        inputs += ["-i", f"{P}/gfx/{img}.png"]; ov.append((len(inputs) // 2, s, min(s + 2.0, total - 0.1)))
    cm = plan.get("comment")
    if cm: inputs += ["-i", comment_card(*cm)]; cidx = len(inputs) // 2
    # música
    mus = f"{TMP}/music.wav"; run(["python3", MUSIC, f"{total + 1:.1f}", mus])
    inputs += ["-i", mus]; midx = len(inputs) // 2
    fc = []; last = "[0:v]"
    if cm:
        fc.append(f"{last}[{cidx}:v]overlay=(W-w)/2:1040[vc]"); last = "[vc]"
    for n, (idx, s, e) in enumerate(ov):
        y = 1075 if not cm else 1290   # borde de arriba de la tarjeta, debajo del subtítulo (y del cartel)
        fc.append(f"[{idx}:v]scale=560:-1[g{n}];{last}[g{n}]overlay=(W-w)/2:{y}:enable='between(t,{s:.2f},{e:.2f})'[v{n}]"); last = f"[v{n}]"
    fc.append(f"{last}subtitles={ass}:fontsdir={FD}[vout]")
    fc.append(f"[{midx}:a]volume=0.09,atrim=0:{total:.2f}[m];[0:a][m]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11[aout]")
    run([FF, "-loglevel", "error", "-y", "-i", cat] + inputs + ["-filter_complex", ";".join(fc), "-map", "[vout]", "-map", "[aout]",
         "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p", "-r", str(FPS), "-c:a", "aac", "-b:a", "192k",
         "-movflags", "+faststart", OUT])
    print("OK", V, f"{C.dur(OUT):.1f}s", OUT)


def build_mute():
    """V6: pantalla partida como los ads mudos de Belu."""
    top, bot = f"{P}/clips/F1.mp4", f"{P}/clips/G1.mp4"
    d = min(C.dur(top), C.dur(bot)) - 0.1
    half = H // 2
    extra = ("Style: T,Montserrat ExtraBold,62,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,-1,0,0,0,100,100,0,0,1,5,0,5,60,60,0,1\n"
             "Style: P,Montserrat ExtraBold,44,&H00B84FFF,&H00FFFFFF,&H00FFFFFF,&H00000000,-1,0,0,0,100,100,0,0,1,4,0,5,60,60,0,1\n"
             "Style: R,Montserrat ExtraBold,44,&H00FFFFFF,&H00FFFFFF,&H001E1EDC,&H001E1EDC,-1,0,0,0,100,100,0,0,3,14,0,5,60,60,0,1\n"
             "Style: CR,Montserrat ExtraBold,46,&H00FFFFFF,&H00FFFFFF,&H001E1EDC,&H001E1EDC,-1,0,0,0,100,100,0,0,3,12,0,5,60,60,0,1\n"
             "Style: CG,Montserrat ExtraBold,46,&H00FFFFFF,&H00FFFFFF,&H003C9A2F,&H003C9A2F,-1,0,0,0,100,100,0,0,3,12,0,5,60,60,0,1\n")
    ev = [f"Dialogue: 2,{ass_time(0)},{ass_time(d)},T,,0,0,0,,{{\\pos(540,{half - 40})}}IMAGINATE CÓMO TE VA\\NA QUEDAR LA BIKINI EN\\NENERO SI EMPEZÁS HOY",
          f"Dialogue: 2,{ass_time(0)},{ass_time(d)},P,,0,0,0,,{{\\pos(540,{half + 130})}}Con rutinas cortas +\\Nalimentación balanceada +\\Nmentalidad antiabandono",
          f"Dialogue: 2,{ass_time(0)},{ass_time(d)},R,,0,0,0,,{{\\pos(540,{H - 120})}}ÚLTIMOS CUPOS CON 50% OFF",
          f"Dialogue: 2,{ass_time(0)},{ass_time(d / 2)},CR,,0,0,0,,{{\\pos(270,110)}}NIVEL INICIAL",
          f"Dialogue: 2,{ass_time(d / 2)},{ass_time(d)},CG,,0,0,0,,{{\\pos(300,110)}}NIVEL AVANZADO"]
    ass = f"{TMP}/subs.ass"
    open(ass, "w").write(ASS_HEAD.format(fs=60, extra=extra) + "\n".join(ev) + "\n")
    mus = f"{TMP}/music.wav"; run(["python3", MUSIC, f"{d + 1:.1f}", mus])
    fc = (f"[0:v]scale=1080:-2,crop=1080:{half}:0:(ih-{half})*0.45,setpts=PTS-STARTPTS[t];"
          f"[1:v]scale=1080:-2,crop=1080:{half}:0:(ih-{half})*0.25,setpts=PTS-STARTPTS[b];"
          f"[t][b]vstack=2,fps={FPS},subtitles={ass}:fontsdir={FD}[vout];"
          f"[2:a]volume=0.8,atrim=0:{d:.2f},afade=t=out:st={d - 0.6:.2f}:d=0.6,loudnorm=I=-14:TP=-1.5[aout]")
    run([FF, "-loglevel", "error", "-y", "-t", f"{d:.2f}", "-i", top, "-t", f"{d:.2f}", "-i", bot, "-i", mus, "-filter_complex", fc,
         "-map", "[vout]", "-map", "[aout]", "-t", f"{d:.2f}", "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p",
         "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", OUT])
    print("OK", V, f"{C.dur(OUT):.1f}s", OUT)



# ---------- V7 · formato espejo (los 8 ads más nuevos de Belu) ----------
HOOKS = {"V7a": "NOVIEMBRE ES ESFUERZO, ENERO ES RESULTADO 💪",
         "V7b": "A SOLO 45 DÍAS DE ESTRENAR BIKINI 👙",
         "V7c": "TE POSTERGASTE MUCHOS VERANOS. ESTE ES EL TUYO ☀️"}
SUP = "/System/Library/Fonts/Supplemental"


def box_text(im, cx, y, lines, fnt, fg, bg, padx=26, pady=12, gap=0, radius=18, emo=None, esize=0):
    """Caja de color con texto centrado (estilo texto de historia de Instagram). Devuelve el y de abajo."""
    d = ImageDraw.Draw(im); lh = fnt.size + 10
    ws = [d.textlength(l, font=fnt) + (esize + 10 if (emo and k == len(lines) - 1) else 0) for k, l in enumerate(lines)]
    w = max(ws) + 2 * padx; h = lh * len(lines) + 2 * pady
    d.rounded_rectangle((cx - w / 2, y, cx + w / 2, y + h), radius, fill=bg)
    for k, l in enumerate(lines):
        tx = cx - ws[k] / 2; ty = y + pady + k * lh
        d.text((tx, ty), l, font=fnt, fill=fg)
        if emo and k == len(lines) - 1:
            im.alpha_composite(emoji_img(emo, esize), (int(tx + d.textlength(l, font=fnt) + 10), int(ty + (fnt.size - esize) / 2 + 4)))
    return y + h


def pills(im, cx, y, rows, fnt, esize):
    """Pastillas negras apiladas, una por renglón, con emoji al final."""
    d = ImageDraw.Draw(im); lh = fnt.size + 18
    for k, (t, e) in enumerate(rows):
        w = d.textlength(t, font=fnt) + (esize + 12 if e else 0) + 50
        d.rounded_rectangle((cx - w / 2, y + k * lh, cx + w / 2, y + k * lh + lh + 2), lh / 2, fill=(12, 12, 12))
        x = cx - w / 2 + 25; d.text((x, y + k * lh + 9), t, font=fnt, fill=(255, 255, 255))
        if e: im.alpha_composite(emoji_img(e, esize), (int(x + d.textlength(t, font=fnt) + 10), int(y + k * lh + (lh - esize) / 2)))
    return y + len(rows) * lh


def neon_arrow(im, pts, color=(255, 92, 190)):
    lay = Image.new("RGBA", im.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    d.line(pts, fill=color + (255,), width=7, joint="curve")
    x1, y1 = pts[-1]; x0, y0 = pts[-2]
    import math
    a = math.atan2(y1 - y0, x1 - x0)
    for s in (2.5, -2.5):
        d.line([(x1, y1), (x1 - 34 * math.cos(a + s / 3), y1 - 34 * math.sin(a + s / 3))], fill=color + (255,), width=7)
    glow = lay.filter(ImageFilter.GaussianBlur(10))
    im.alpha_composite(glow); im.alpha_composite(glow); im.alpha_composite(lay)


def mirror_overlay(hook):
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); cx = W // 2
    txt, em = re.match(r"^(.*?)\s*([\U0001F300-\U0001FAFF\u2600-\u27BF\uFE0F]*)$", hook).groups()
    fh = ImageFont.truetype(f"{SUP}/Arial Bold.ttf", 56)
    dd = ImageDraw.Draw(im); lines = wrap(dd, txt, fh, 860)
    y = box_text(im, cx, 150, lines, fh, (12, 12, 12), (255, 255, 255), padx=34, pady=18, radius=22, emo=em[:1] if em else None, esize=52)
    fp = ImageFont.truetype(f"{SUP}/Arial Bold.ttf", 37)
    y = box_text(im, cx, y + 26, ["SI EN VERANO QUERÉS PONERTE LA BIKINI", "Y TENER EL CUERPO DE TUS SUEÑOS..."], fp, (255, 255, 255), (232, 96, 196), radius=14)
    fr = ImageFont.truetype(f"{SUP}/Arial Bold.ttf", 40)
    y_red = y + 22
    y = box_text(im, cx, y_red, ["¡TENÉS QUE EMPEZAR YA!"], fr, (255, 255, 255), (226, 18, 28), radius=8, emo="⏰", esize=44)
    fpl = ImageFont.truetype(f"{SUP}/Arial Bold.ttf", 38)
    y = pills(im, cx, y + 18, [("RUTINAS CORTAS Y EFECTIVAS", "💪"), ("+ ALIMENTACIÓN COMPLETA", "🥗"), ("+ MENTALIDAD ANTIABANDONO", "🧘")], fpl, 36)
    neon_arrow(im, [(70, 300), (40, 400), (60, 500), (150, y_red + 34)])
    neon_arrow(im, [(1020, 380), (1050, 460), (1040, 560), (935, y_red + 30)])
    fd = ImageFont.truetype(f"{SUP}/DIN Condensed Bold.ttf", 50)
    yp = 1180   # a la altura de la cadera: más arriba le tapa la cara cuando Veo se acerca
    yp = box_text(im, 800, yp, ["PRECIO REGULAR: $33.980"], fd, (40, 40, 40), (255, 222, 232), padx=20, pady=8, radius=4)
    fd2 = ImageFont.truetype(f"{SUP}/DIN Condensed Bold.ttf", 76)
    box_text(im, 780, yp + 12, ["PRECIO HOY X $16.990"], fd2, (255, 255, 255), (226, 18, 28), padx=24, pady=6, radius=4)
    fc = ImageFont.truetype(f"{SUP}/Times New Roman.ttf", 48)
    box_text(im, cx, H - 300, ["¡ÚLTIMOS 7 CUPOS CON", "50% DE DESCUENTO!"], fc, (255, 255, 255), (226, 18, 28), padx=40, pady=18, radius=2)
    p = f"{TMP}/mirror.png"; im.save(p); return p


def build_mirror(hook):
    clips = [c for c in (f"{P}/clips/M1.mp4", f"{P}/clips/M2.mp4") if os.path.exists(c)]   # M1 la bloqueó el filtro 4 veces
    segs = []
    for k, c in enumerate(clips):
        sg = f"{TMP}/m{k}.mp4"; d = C.dur(c) - 0.1
        run([FF, "-loglevel", "error", "-y", "-t", f"{d:.2f}", "-i", c, "-vf", f"scale={W}:{H},fps={FPS},setpts=PTS-STARTPTS", "-an",
             "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", sg]); segs.append(sg)
    lst = f"{TMP}/list.txt"; open(lst, "w").write("".join(f"file '{x}'\n" for x in segs))
    cat = f"{TMP}/cat.mp4"; run([FF, "-loglevel", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", cat])
    d = C.dur(cat); ov = mirror_overlay(hook)
    mus = f"{TMP}/music.wav"; run(["python3", MUSIC, f"{d + 1:.1f}", mus])
    fc = (f"[0:v][1:v]overlay=0:0[vout];[2:a]volume=0.8,atrim=0:{d:.2f},afade=t=out:st={d - 0.8:.2f}:d=0.8,loudnorm=I=-14:TP=-1.5[aout]")
    run([FF, "-loglevel", "error", "-y", "-i", cat, "-i", ov, "-i", mus, "-filter_complex", fc, "-map", "[vout]", "-map", "[aout]",
         "-t", f"{d:.2f}", "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k",
         "-movflags", "+faststart", OUT])
    print("OK", V, f"{C.dur(OUT):.1f}s", OUT)


if V == "V6": build_mute()
elif V in HOOKS: build_mirror(HOOKS[V])
else: build_talk(PLANES[V])
