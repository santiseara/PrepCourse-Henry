"""Inserts del producto para los ads de Silvia Fitness · Adiós Panza (2026-11-16).
Copia lo que muestra Belu Fitness en sus videos: la planilla "LUNES", la grilla de comidas, una receta, el video demostrativo,
la app y los bonos. Todo dibujado por código (el producto todavía no existe), tarjetas de 640 px con sombra, PNG con alfa.
Uso: python3 gfx_silvia.py <carpeta_salida> [clip_para_video_demo.mp4]
"""
import os, sys, subprocess
from PIL import Image, ImageDraw, ImageFont, ImageFilter

OUT = sys.argv[1]; os.makedirs(OUT, exist_ok=True)
DEMO = sys.argv[2] if len(sys.argv) > 2 else None
FD = os.path.expanduser("~/PrepCourse-Henry/OUTPUTS/scripts-producto/fonts")
MX = f"{FD}/Montserrat-ExtraBold.ttf"; BB = f"{FD}/Barlow-Bold.ttf"; BS = f"{FD}/Barlow-SemiBold.ttf"; BR = f"{FD}/Barlow-Regular.ttf"
EMO = "/System/Library/Fonts/Apple Color Emoji.ttc"
PLUM, RASP, PINK, SOFT, INK, MUT = (74, 21, 48), (184, 51, 106), (242, 182, 210), (252, 235, 243), (42, 15, 29), (124, 90, 107)
f = lambda p, s: ImageFont.truetype(p, s)


def emoji(ch, size):
    im = Image.new("RGBA", (200, 200), (0, 0, 0, 0))
    ImageDraw.Draw(im).text((0, 0), ch, font=ImageFont.truetype(EMO, 160), embedded_color=True)
    return im.crop(im.getbbox()).resize((size, size), Image.LANCZOS)


def card(w, h, bg=(255, 255, 255)):
    pad = 30
    im = Image.new("RGBA", (w + 2 * pad, h + 2 * pad), (0, 0, 0, 0))
    sh = Image.new("RGBA", im.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle((pad, pad + 8, pad + w, pad + h + 8), 34, fill=(0, 0, 0, 90))
    im = Image.alpha_composite(im, sh.filter(ImageFilter.GaussianBlur(14)))
    ImageDraw.Draw(im).rounded_rectangle((pad, pad, pad + w, pad + h), 34, fill=bg)
    return im, pad


def header(d, pad, w, title, sub):
    d.rounded_rectangle((pad, pad, pad + w, pad + 120), 34, fill=PINK)
    d.rectangle((pad, pad + 80, pad + w, pad + 120), fill=PINK)
    d.text((pad + w / 2, pad + 52), title, font=f(MX, 50), fill=PLUM, anchor="mm")
    d.text((pad + w / 2, pad + 98), sub, font=f(BB, 24), fill=RASP, anchor="mm")


# 1 · planilla LUNES
def planilla():
    w, h = 640, 700; im, p = card(w, h); d = ImageDraw.Draw(im)
    header(d, p, w, "LUNES", "SEMANA 1 · FULL BODY · 30 MIN")
    cols = [p + 24, p + 300, p + 410, p + 530]
    y = p + 150
    for x, t in zip(cols, ["EJERCICIO", "INICIAL", "INTERM.", "AVANZ."]):
        d.text((x, y), t, font=f(BB, 22), fill=RASP)
    rows = [("Sentadillas", "3x10", "3x15", "4x20"), ("Puente de glúteos", "3x12", "3x15", "4x20"),
            ("Estocadas", "2x8", "3x10", "4x12"), ("Plancha", "20 s", "30 s", "45 s"),
            ("Mountain climbers", "2x10", "3x15", "4x20"), ("Bicicleta", "2x12", "3x15", "4x20"),
            ("Jumping jacks", "2x20", "3x30", "4x40")]
    y += 46
    for k, r in enumerate(rows):
        if k % 2 == 0: d.rectangle((p + 12, y - 10, p + w - 12, y + 52), fill=SOFT)
        d.text((cols[0], y + 4), r[0], font=f(BS, 27), fill=INK)
        for x, t in zip(cols[1:], r[1:]): d.text((x, y + 6), t, font=f(BR, 26), fill=INK)
        y += 64
    d.text((p + w / 2, p + h - 34), "+ video demostrativo de cada ejercicio", font=f(BS, 24), fill=MUT, anchor="mm")
    im.save(f"{OUT}/planilla.png")


# 2 · grilla de comidas
def grilla():
    w, h = 640, 700; im, p = card(w, h); d = ImageDraw.Draw(im)
    header(d, p, w, "GRILLA DÍA 1", "14 DÍAS · SIN PASAR HAMBRE")
    items = [("☕", "DESAYUNO", "Tostadas con palta y huevo + café"), ("🥗", "ALMUERZO", "Pollo al horno con calabaza y ensalada"),
             ("🍓", "MERIENDA", "Yogur con frutillas y granola"), ("🍲", "CENA", "Tarta de verduras con ensalada verde")]
    y = p + 160
    for e, t, s in items:
        d.rounded_rectangle((p + 20, y, p + w - 20, y + 112), 22, fill=SOFT)
        im.alpha_composite(emoji(e, 62), (p + 40, y + 25))
        d.text((p + 124, y + 22), t, font=f(BB, 24), fill=RASP)
        d.text((p + 124, y + 56), s, font=f(BS, 26), fill=INK)
        y += 128
    d.text((p + w / 2, p + h - 34), "+ lista del súper y reemplazos", font=f(BS, 24), fill=MUT, anchor="mm")
    im.save(f"{OUT}/grilla.png")


# 3 · receta
def receta():
    w, h = 640, 640; im, p = card(w, h); d = ImageDraw.Draw(im)
    header(d, p, w, "RECETA", "BUDÍN DE AVENA Y BANANA")
    im.alpha_composite(emoji("🍌", 120), (p + w - 170, p + 150))
    d.text((p + 34, p + 160), "INGREDIENTES", font=f(BB, 26), fill=RASP)
    y = p + 205
    for t in ["2 bananas maduras", "2 huevos", "1 taza de avena", "1 cdita de polvo de hornear", "Canela a gusto"]:
        d.text((p + 34, y), "•  " + t, font=f(BS, 28), fill=INK); y += 50
    d.text((p + 34, y + 20), "PASO A PASO", font=f(BB, 26), fill=RASP)
    d.text((p + 34, y + 62), "Pisá, mezclá y al horno 25 minutos.", font=f(BR, 27), fill=INK)
    im.save(f"{OUT}/receta.png")


# 4 · video demostrativo (un cuadro real de Silvia entrenando, dentro de una tarjeta con play)
def video_demo():
    if not DEMO: return
    fr = f"{OUT}/_demo.jpg"
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-ss", "2.5", "-i", DEMO, "-frames:v", "1", fr], check=True)
    ph = Image.open(fr).convert("RGB"); W0, H0 = ph.size
    ph = ph.crop((0, int(H0 * .18), W0, int(H0 * .18) + int(W0 * 1.0))).resize((560, 560), Image.LANCZOS)
    w, h = 600, 660; im, p = card(w, h); d = ImageDraw.Draw(im)
    m = Image.new("L", (560, 560), 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, 559, 559), 24, fill=255)
    im.paste(ph, (p + 20, p + 20), m)
    cx, cy = p + 300, p + 300
    d.ellipse((cx - 56, cy - 56, cx + 56, cy + 56), fill=(255, 255, 255, 230))
    d.polygon([(cx - 18, cy - 30), (cx - 18, cy + 30), (cx + 32, cy)], fill=RASP)
    d.text((p + w / 2, p + 618), "Sentadillas · 3 niveles", font=f(BB, 30), fill=PLUM, anchor="mm")
    im.save(f"{OUT}/video.png")


# 5 · la app
def app():
    w, h = 560, 760; pad = 30
    im = Image.new("RGBA", (w + 2 * pad, h + 2 * pad), (0, 0, 0, 0))
    sh = Image.new("RGBA", im.size, (0, 0, 0, 0)); ImageDraw.Draw(sh).rounded_rectangle((pad, pad + 8, pad + w, pad + h + 8), 60, fill=(0, 0, 0, 100))
    im = Image.alpha_composite(im, sh.filter(ImageFilter.GaussianBlur(14))); d = ImageDraw.Draw(im)
    d.rounded_rectangle((pad, pad, pad + w, pad + h), 60, fill=(17, 17, 17))
    x0, y0 = pad + 16, pad + 16; d.rounded_rectangle((x0, y0, pad + w - 16, pad + h - 16), 46, fill=SOFT)
    d.text((x0 + 34, y0 + 46), "SILVIA FITNESS · ADIÓS PANZA", font=f(BB, 22), fill=RASP)
    d.text((x0 + 34, y0 + 80), "Adiós panza", font=f(MX, 52), fill=PLUM)
    d.text((x0 + 34, y0 + 148), "Entrenamiento + alimentación + mentalidad", font=f(BR, 24), fill=MUT)
    y = y0 + 200
    for e, t, s in [("💪", "ENTRENAMIENTO", "Rutinas con video"), ("🥗", "ALIMENTACIÓN", "14 días repetibles"),
                    ("🧠", "MENTALIDAD", "Crear el hábito"), ("🎁", "BONUS", "9 regalos")]:
        d.rounded_rectangle((x0 + 20, y, pad + w - 36, y + 108), 24, fill=(255, 255, 255))
        im.alpha_composite(emoji(e, 54), (x0 + 42, y + 27))
        d.text((x0 + 120, y + 22), t, font=f(BB, 21), fill=RASP); d.text((x0 + 120, y + 52), s, font=f(BS, 30), fill=INK)
        y += 124
    im.save(f"{OUT}/app.png")


# 6 · bonos
def bonos():
    w, h = 640, 600; im, p = card(w, h); d = ImageDraw.Draw(im)
    header(d, p, w, "9 BONOS", "DE REGALO · HOY GRATIS")
    y = p + 150
    for t in ["Cómo evitar atracones", "Meal prep en 90 minutos", "25 antojos dulces", "50 recetas saludables",
              "Lista del súper", "Rutina de movilidad"]:
        im.alpha_composite(emoji("🎁", 36), (p + 34, y + 2)); d.text((p + 86, y), t, font=f(BS, 30), fill=INK); y += 56
    d.text((p + w / 2, p + h - 34), "+ 3 bonos más", font=f(BB, 26), fill=RASP, anchor="mm")
    im.save(f"{OUT}/bonos.png")


for fn in (planilla, grilla, receta, video_demo, app, bonos): fn()
print("OK", sorted(os.listdir(OUT)))
