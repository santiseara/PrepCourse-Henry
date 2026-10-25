"""Placas del VSL de Protocolo Chía 28D, copiando las del competidor (Protocolo Chía 4S).
Uso: python3 gfx_chia.py <carpeta_trabajo>   (escribe en <carpeta_trabajo>/gfx/)
Hace: chips de fase, checklist verde acumulativa, anclas tachadas, placa de precio, escudo de garantía,
badge fijo de precio, botón de CTA y placa final."""
import os, sys
from PIL import Image, ImageDraw, ImageFont

WD = sys.argv[1]
OUT = os.path.join(WD, 'gfx'); os.makedirs(OUT, exist_ok=True)
FONTS = os.path.join(WD, 'fonts')
VERDE, VERDE_OSC, CREMA, ROJO = (33, 166, 90, 255), (22, 122, 66, 255), (247, 243, 233, 255), (214, 40, 40, 255)

def f(name, size): return ImageFont.truetype(os.path.join(FONTS, name), size)
BLACK = 'Arial Black.ttf'; ROUND = 'Arial Rounded Bold.ttf'

def emoji(ch, size):
    try:
        ft = ImageFont.truetype('/System/Library/Fonts/Apple Color Emoji.ttc', 160)
        im = Image.new('RGBA', (220, 220), (0, 0, 0, 0))
        ImageDraw.Draw(im).text((10, 10), ch, font=ft, embedded_color=True)
        im = im.crop(im.getbbox())
        return im.resize((size, int(im.height * size / im.width)), Image.LANCZOS)
    except Exception:
        return None

def save(im, name):
    im.save(os.path.join(OUT, name + '.png')); print('gfx', name, im.size)

def chip_fase(n, titulo, ic, name):
    w, h = 640, 150
    im = Image.new('RGBA', (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle([0, 0, w - 1, h - 1], 36, fill=VERDE)
    e = emoji(ic, 64)
    x = 42
    if e: im.alpha_composite(e, (x, h // 2 - e.height // 2)); x += e.width + 26
    d.text((x, 38), f'SEMANA {n}', font=f(ROUND, 34), fill=(235, 255, 240, 255))
    d.text((x, 72), titulo.upper(), font=f(BLACK, 56), fill=(255, 255, 255, 255))
    save(im, name)

def grid_fases():
    w, h = 760, 330
    im = Image.new('RGBA', (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    celdas = [('🌱', 'Sembrar'), ('💚', 'Sanar'), ('🔥', 'Soltar'), ('⭐', 'Sumar')]
    for i, (ic, t) in enumerate(celdas):
        cx, cy = (i % 2) * 390, (i // 2) * 175
        d.rounded_rectangle([cx, cy, cx + 360, cy + 140], 30, fill=VERDE)
        e = emoji(ic, 54)
        x = cx + 30
        if e: im.alpha_composite(e, (x, cy + 43)); x += e.width + 18
        d.text((x, cy + 70), t, font=f(BLACK, 48), fill=(255, 255, 255, 255), anchor='lm')
    save(im, 'grid_fases')

def checklist(n):
    items = ['Protocolo 28D personalizado', 'App exclusiva + seguimiento',
             'BONO: Recetario Cero Culpa', 'BONO: WhatsApp del equipo 24/7']
    w = 820; hh = 86; h = 92 + hh * n
    im = Image.new('RGBA', (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle([0, 0, w - 1, h - 1], 26, fill=(255, 255, 255, 250))
    d.rounded_rectangle([0, 0, w - 1, 84], 26, fill=VERDE)
    d.rectangle([0, 58, w - 1, 84], fill=VERDE)
    d.text((w // 2, 42), 'TODO LO QUE RECIBES', font=f(BLACK, 40), fill=(255, 255, 255, 255), anchor='mm')
    for i in range(n):
        y = 92 + i * hh
        e = emoji('✅', 46)
        if e: im.alpha_composite(e, (34, y + 10))
        d.text((104, y + 34), items[i], font=f(ROUND, 42), fill=(25, 30, 28, 255), anchor='lm')
    save(im, f'check{n}')

def anclas(n):
    vals = ['$140', '$97', '$70']
    w, h = 460, 100 * n
    im = Image.new('RGBA', (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    for i in range(n):
        y = i * 100
        d.rounded_rectangle([0, y + 8, w - 1, y + 86], 40, fill=(255, 255, 255, 250), outline=(40, 40, 40, 255), width=4)
        d.text((w // 2, y + 47), vals[i], font=f(BLACK, 54), fill=(30, 30, 30, 255), anchor='mm')
        d.line([40, y + 47, w - 40, y + 47], fill=ROJO, width=9)
    save(im, f'anclas{n}')

def precio():
    w, h = 700, 420
    im = Image.new('RGBA', (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle([0, 0, w - 1, h - 1], 40, fill=CREMA, outline=VERDE, width=7)
    d.rounded_rectangle([w // 2 - 170, 34, w // 2 + 170, 116], 42, fill=VERDE)
    d.text((w // 2, 75), 'HOY SOLO', font=f(BLACK, 46), fill=(255, 255, 255, 255), anchor='mm')
    d.text((w // 2, 230), '$17', font=f(BLACK, 190), fill=(24, 32, 28, 255), anchor='mm')
    d.text((w // 2, 340), 'pago único  |  acceso inmediato', font=f(ROUND, 36), fill=(70, 80, 74, 255), anchor='mm')
    save(im, 'precio')

def garantia():
    w, h = 880, 330
    im = Image.new('RGBA', (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle([0, 0, w - 1, h - 1], 34, fill=CREMA, outline=(212, 175, 55, 255), width=7)
    e = emoji('🛡️', 120)
    if e: im.alpha_composite(e, (56, 95))
    d.text((230, 120), '60 DÍAS', font=f(BLACK, 92), fill=(24, 32, 28, 255), anchor='lm')
    d.text((230, 196), 'DE GARANTÍA TOTAL', font=f(BLACK, 46), fill=VERDE_OSC, anchor='lm')
    d.text((230, 252), 'Si no te sirve, te devolvemos cada centavo', font=f(ROUND, 26), fill=(80, 88, 82, 255), anchor='lm')
    save(im, 'garantia')

def badge():
    w, h = 680, 92
    im = Image.new('RGBA', (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle([0, 0, w - 1, h - 1], 46, fill=VERDE)
    e = emoji('💳', 48)
    x = 34
    if e: im.alpha_composite(e, (x, 22)); x += e.width + 18
    d.text((x, h // 2), '$17 USD · PAGO ÚNICO', font=f(BLACK, 40), fill=(255, 255, 255, 255), anchor='lm')
    save(im, 'badge_precio')

def boton():
    w, h = 760, 190
    im = Image.new('RGBA', (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    e = emoji('👇', 86)
    if e: im.alpha_composite(e, (w // 2 - 43, 0))
    d.rounded_rectangle([0, 96, w - 1, h - 1], 46, fill=VERDE)
    d.text((w // 2, 143), 'QUIERO MI PROTOCOLO', font=f(BLACK, 48), fill=(255, 255, 255, 255), anchor='mm')
    save(im, 'boton_cta')

def final():
    w, h = 1080, 1920
    im = Image.new('RGBA', (w, h), VERDE); d = ImageDraw.Draw(im)
    d.text((w // 2, 330), 'ESTA ES TU', font=f(BLACK, 110), fill=(255, 255, 255, 255), anchor='mm')
    d.text((w // 2, 460), 'ÚLTIMA OPORTUNIDAD', font=f(BLACK, 74), fill=(255, 255, 255, 255), anchor='mm')
    d.rounded_rectangle([90, 600, w - 90, 760], 30, fill=(255, 255, 255, 235))
    d.text((w // 2, 648), 'Desbloquea tu acceso al', font=f(ROUND, 44), fill=(30, 40, 34, 255), anchor='mm')
    d.text((w // 2, 712), 'PROTOCOLO CHÍA 28D', font=f(BLACK, 56), fill=VERDE_OSC, anchor='mm')
    d.text((w // 2, 900), 'Y no te preocupes:', font=f(ROUND, 48), fill=(255, 255, 255, 255), anchor='mm')
    d.text((w // 2, 975), 'tienes 60 DÍAS de garantía', font=f(BLACK, 54), fill=(255, 255, 255, 255), anchor='mm')
    d.text((w // 2, 1150), 'ESTÁS A UN CLIC', font=f(BLACK, 72), fill=(255, 255, 255, 255), anchor='mm')
    d.text((w // 2, 1240), 'DE CAMBIAR TU VIDA', font=f(BLACK, 72), fill=(255, 255, 255, 255), anchor='mm')
    d.rounded_rectangle([110, 1420, w - 110, 1580], 48, fill=(255, 255, 255, 250))
    d.text((w // 2, 1500), 'TOCA EL BOTÓN DE ABAJO', font=f(BLACK, 56), fill=VERDE_OSC, anchor='mm')
    e = emoji('👇', 150)
    if e: im.alpha_composite(e, (w // 2 - 75, 1640))
    save(im.convert('RGBA'), 'placa_final')

chip_fase(1, 'Sembrar', '🌱', 'fase1')
chip_fase(2, 'Sanar', '💚', 'fase2')
chip_fase(3, 'Soltar', '🔥', 'fase3')
chip_fase(4, 'Sumar', '⭐', 'fase4')
grid_fases()
for n in (1, 2, 3, 4): checklist(n)
for n in (1, 2, 3): anclas(n)
precio(); garantia(); badge(); boton(); final()
print('listo ->', OUT)
