# -*- coding: utf-8 -*-
"""Inserts de producto de Your First Wooden Automaton, dibujados por codigo (2026-11-05).
Replica lo que Orzzen mete en sus ads: la tapa del ebook, una hoja de planos, la biblioteca de
mecanismos, las fases del proceso y la pantalla de la app simuladora. Cuesta cero y no hace falta
que el producto exista todavia. Uso: python3 gfx_automata.py"""
import os, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

OUT = os.path.expanduser('~/Desktop/wooden-automaton/anuncios/work/gfx')
FD = os.path.expanduser('~/Desktop/wooden-automaton/anuncios/work/fonts')
os.makedirs(OUT, exist_ok=True)
W, H = 1080, 1920
BC, BCB = FD + '/BarlowCondensed-ExtraBold.ttf', FD + '/BarlowCondensed-SemiBold.ttf'
MX, MB = FD + '/Montserrat-ExtraBold.ttf', FD + '/Montserrat-Black.ttf'
WOOD, INK, AMBER, CREAM = (59, 36, 22), (28, 24, 20), (214, 143, 51), (246, 239, 228)
PAPER, LINE, SAGE = (252, 250, 246), (120, 110, 98), (122, 158, 118)
f = lambda p, s: ImageFont.truetype(p, s)
# El editor le mete a las fotos fijas un zoom de 1.0 a 1.14, mas un golpe de 1.16 que dura 0,22 s en
# cada corte. Si el grafico mide justo 1080x1920 se come la cabecera y el pie. Por eso cada insert va
# sobre un lienzo 1.20x, con el contenido nitido centrado y el sobrante desenfocado: entra entero y
# sigue siendo legible en el telefono. Con 1.41x quedaba completo pero demasiado chico para leerlo.
MW, MH = 1296, 2304   # 1.20x: con el zoom de 1.14 el insert llena la pantalla y todavia se lee


def marco(im, path):
    bg = im.resize((MW, MH), Image.LANCZOS).filter(ImageFilter.GaussianBlur(26))
    bg = Image.blend(bg, Image.new('RGB', (MW, MH), (18, 16, 14)), 0.35)
    bg.paste(im, ((MW - W) // 2, (MH - H) // 2))
    bg.save(path)


def rr(d, box, r, fill, outline=None, width=2):
    d.rounded_rectangle(box, r, fill=fill, outline=outline, width=width)


def wood_bg(dark=True):
    im = Image.new('RGB', (W, H), WOOD if dark else (120, 86, 56))
    d = ImageDraw.Draw(im)
    for i in range(0, H, 7):
        c = 14 + int(10 * math.sin(i / 23.0)) + (6 if (i // 7) % 3 == 0 else 0)
        d.line([(0, i), (W, i + 18)], fill=(WOOD[0] + c, WOOD[1] + c - 2, WOOD[2] + c - 4), width=5)
    return im.filter(ImageFilter.GaussianBlur(3))


def cover():
    im = wood_bg(); d = ImageDraw.Draw(im)
    im.alpha_composite(Image.new('RGBA', (W, H), (0, 0, 0, 70)).convert('RGBA')) if im.mode == 'RGBA' else None
    bx0, by0, bx1, by1 = 120, 330, 960, 1590
    d.rectangle((bx0 + 16, by0 + 20, bx1 + 16, by1 + 20), fill=(0, 0, 0))
    rr(d, (bx0, by0, bx1, by1), 10, (236, 226, 208))
    d.rectangle((bx0, by0, bx0 + 34, by1), fill=(198, 180, 152))      # lomo
    d.rectangle((bx0 + 60, by0 + 70, bx1 - 60, by0 + 78), fill=AMBER)
    d.text((W / 2 + 17, by0 + 140), 'YOUR FIRST', font=f(BC, 120), fill=INK, anchor='mt')
    d.text((W / 2 + 17, by0 + 258), 'AUTOMATON', font=f(BC, 120), fill=(150, 92, 28), anchor='mt')
    d.text((W / 2 + 17, by0 + 400), 'Complete guide to designing and building', font=f(BCB, 44), fill=(92, 84, 72), anchor='mt')
    d.text((W / 2 + 17, by0 + 450), 'wooden automata from scratch', font=f(BCB, 44), fill=(92, 84, 72), anchor='mt')
    # figura: manivela + leva + varilla + pajaro
    cx, cy = W / 2 + 17, by0 + 760
    d.rounded_rectangle((cx - 230, cy + 60, cx + 230, cy + 250), 14, fill=(206, 170, 118), outline=(150, 112, 68), width=5)
    d.ellipse((cx - 70, cy + 110, cx + 70, cy + 206), outline=(120, 86, 48), width=10)
    d.ellipse((cx - 22, cy + 136, cx + 24, cy + 180), fill=(120, 86, 48))
    d.line([(cx, cy + 158), (cx, cy - 60)], fill=(120, 86, 48), width=12)
    d.ellipse((cx - 54, cy - 118, cx + 54, cy - 36), fill=(176, 120, 62))
    d.polygon([(cx - 50, cy - 86), (cx - 210, cy - 150), (cx - 44, cy - 50)], fill=(150, 96, 44))
    d.polygon([(cx + 50, cy - 86), (cx + 210, cy - 150), (cx + 44, cy - 50)], fill=(150, 96, 44))
    d.line([(cx + 230, cy + 170), (cx + 300, cy + 170)], fill=(120, 86, 48), width=12)
    d.ellipse((cx + 286, cy + 150, cx + 326, cy + 190), fill=(120, 86, 48))
    rr(d, (bx0 + 300, by1 - 150, bx1 - 300, by1 - 70), 40, AMBER)
    d.text((W / 2 + 17, by1 - 136), 'MAIN EBOOK', font=f(MX, 36), fill=INK, anchor='mt')
    marco(im, f'{OUT}/cover.png'); print('cover.png')


def sheet(title, sub):
    im = Image.new('RGB', (W, H), PAPER); d = ImageDraw.Draw(im)
    d.rectangle((0, 0, W, 190), fill=INK)
    d.text((60, 56), title, font=f(BC, 72), fill=CREAM)
    d.text((60, 132), sub, font=f(MX, 28), fill=AMBER)
    return im, d


def plans():
    im, d = sheet('PROJECT A-02  ·  BIRD WITH WINGS', 'PLANS · TEMPLATES · EXACT MEASUREMENTS')
    def part(x, y, w_, h_, name, dim, kind='rect'):
        if kind == 'rect': d.rounded_rectangle((x, y, x + w_, y + h_), 8, outline=LINE, width=4)
        elif kind == 'wing': d.polygon([(x, y + h_), (x + w_, y), (x + w_, y + h_ * .7)], outline=LINE, width=4)
        else:
            d.ellipse((x, y, x + w_, y + h_), outline=LINE, width=4)
            d.ellipse((x + w_ / 2 - 12, y + h_ / 2 - 12, x + w_ / 2 + 12, y + h_ / 2 + 12), outline=LINE, width=3)
        d.line([(x, y + h_ + 26), (x + w_, y + h_ + 26)], fill=AMBER, width=3)
        d.line([(x, y + h_ + 18), (x, y + h_ + 34)], fill=AMBER, width=3)
        d.line([(x + w_, y + h_ + 18), (x + w_, y + h_ + 34)], fill=AMBER, width=3)
        d.text((x + w_ / 2, y + h_ + 40), dim, font=f(MX, 24), fill=(140, 96, 40), anchor='mt')
        d.text((x, y - 36), name, font=f(MX, 26), fill=INK)
    part(70, 300, 380, 230, 'BODY', '120 mm')
    part(540, 300, 420, 230, 'WING ×2', '150 mm', 'wing')
    part(70, 660, 230, 230, 'CAM', '70 mm', 'disc')
    part(390, 660, 120, 330, 'PUSH ROD', '38 mm')
    part(620, 660, 340, 330, 'FRAME SIDE ×2', '110 mm')
    part(70, 1120, 890, 180, 'BASE', '280 mm')
    d.rectangle((70, 1420, 1010, 1760), outline=LINE, width=3)
    d.text((95, 1440), 'CUT LIST', font=f(BC, 56), fill=INK)
    rows = [('Body', '120 × 60 × 10 mm', '×1'), ('Wing', '150 × 42 × 6 mm', '×2'),
            ('Cam', 'Ø 70 × 10 mm', '×1'), ('Push rod', '38 × 8 × 6 mm', '×2'),
            ('Frame side', '110 × 90 × 12 mm', '×2'), ('Base', '280 × 90 × 18 mm', '×1')]
    for i, (a, b, c) in enumerate(rows):
        y = 1520 + i * 40
        d.text((100, y), a, font=f(MX, 26), fill=INK)
        d.text((430, y), b, font=f(MX, 26), fill=(100, 92, 80))
        d.text((900, y), c, font=f(MX, 26), fill=AMBER)
    marco(im, f'{OUT}/plans.png'); print('plans.png')


def mechanisms():
    im, d = sheet('MECHANISM LIBRARY', '20+ MECHANISMS EXPLAINED · PLANS + ANIMATIONS')
    names = [('CAM & FOLLOWER', 'up and down'), ('CRANK & ROD', 'turn into push'),
             ('SNAIL CAM', 'slow rise, quick drop'), ('GEAR PAIR', 'change the speed'),
             ('ECCENTRIC WHEEL', 'smooth wobble'), ('BELL CRANK', 'turn the corner')]
    for i, (n, s) in enumerate(names):
        c, r_ = i % 2, i // 2
        x, y = 60 + c * 490, 280 + r_ * 460
        rr(d, (x, y, x + 440, y + 400), 18, (255, 255, 255), LINE, 3)
        cx, cy = x + 220, y + 170
        if i == 0:
            d.ellipse((cx - 80, cy - 50, cx + 60, cy + 90), outline=INK, width=8)
            d.line([(cx - 10, cy - 10), (cx - 10, cy - 120)], fill=AMBER, width=10)
        elif i == 1:
            d.ellipse((cx - 90, cy - 30, cx - 10, cy + 50), outline=INK, width=8)
            d.line([(cx - 50, cy + 10), (cx + 90, cy - 60)], fill=AMBER, width=10)
        elif i == 2:
            d.arc((cx - 90, cy - 70, cx + 70, cy + 90), 200, 110, fill=INK, width=9)
            d.line([(cx + 70, cy + 10), (cx - 10, cy + 10)], fill=AMBER, width=9)
        elif i == 3:
            for k, (ox, rad) in enumerate(((-60, 70), (60, 48))):
                d.ellipse((cx + ox - rad, cy - rad, cx + ox + rad, cy + rad), outline=INK if k == 0 else AMBER, width=8)
                for t in range(10):
                    a = t * 36 * math.pi / 180
                    d.line([(cx + ox + rad * math.cos(a), cy + rad * math.sin(a)),
                            (cx + ox + (rad + 12) * math.cos(a), cy + (rad + 12) * math.sin(a))],
                           fill=INK if k == 0 else AMBER, width=6)
        elif i == 4:
            d.ellipse((cx - 80, cy - 60, cx + 60, cy + 80), outline=INK, width=8)
            d.ellipse((cx - 24, cy - 14, cx + 6, cy + 16), fill=AMBER)
        else:
            d.line([(cx - 90, cy + 60), (cx, cy - 40)], fill=INK, width=10)
            d.line([(cx, cy - 40), (cx + 95, cy + 10)], fill=AMBER, width=10)
            d.ellipse((cx - 14, cy - 54, cx + 14, cy - 26), fill=INK)
        d.text((cx, y + 290), n, font=f(BC, 50), fill=INK, anchor='mt')
        d.text((cx, y + 344), s, font=f(MX, 24), fill=(130, 120, 106), anchor='mt')
    marco(im, f'{OUT}/mechanisms.png'); print('mechanisms.png')


def phases():
    im, d = sheet('THE 6 PHASES OF THE BUILD', 'FROM THE IDEA TO THE PIECE THAT MOVES')
    ph = [('01', 'PLANNING', 'Pick the figure and the\nmovement it will make.'),
          ('02', 'TEMPLATES', 'Print the sheets and\ntransfer them to the wood.'),
          ('03', 'CUTTING', 'Cut, drill and sand\nevery part on the list.'),
          ('04', 'MECHANISM', 'Cam, rod and crank:\nthe part that moves.'),
          ('05', 'ASSEMBLY', 'Frame, base and figure\nput together square.'),
          ('06', 'FINISH', 'Sand, seal and tune\nuntil it runs smooth.')]
    for i, (n, t, s) in enumerate(ph):
        y = 270 + i * 265
        rr(d, (60, y, 1020, y + 225), 18, (255, 255, 255), LINE, 3)
        rr(d, (60, y, 210, y + 225), 18, AMBER)
        d.rectangle((180, y, 210, y + 225), fill=AMBER)
        d.text((135, y + 70), n, font=f(BC, 96), fill=INK, anchor='mt')
        d.text((250, y + 42), t, font=f(BC, 62), fill=INK)
        d.multiline_text((250, y + 115), s, font=f(MX, 27), fill=(118, 108, 96), spacing=12)
    marco(im, f'{OUT}/phases.png'); print('phases.png')


def app():
    im = Image.new('RGB', (W, H), (28, 30, 34)); d = ImageDraw.Draw(im)
    rr(d, (50, 330, 1030, 1600), 26, (246, 247, 249))
    d.rounded_rectangle((50, 330, 1030, 430), 26, fill=(42, 46, 52))
    d.rectangle((50, 400, 1030, 430), fill=(42, 46, 52))
    for k, c in enumerate(((255, 95, 86), (255, 189, 46), (39, 201, 63))):
        d.ellipse((86 + k * 36, 364, 108 + k * 36, 386), fill=c)
    d.text((220, 360), 'Wooden Automata  ·  Mechanism Simulator', font=f(MX, 30), fill=(228, 230, 234))
    d.text((90, 470), 'MECHANISM', font=f(MX, 24), fill=(140, 146, 156))
    rr(d, (90, 510, 990, 596), 14, (255, 255, 255), (206, 210, 216), 3)
    d.text((118, 530), 'Crank & Connecting Rod', font=f(MX, 34), fill=(30, 34, 40))
    d.polygon([(930, 545), (962, 545), (946, 568)], fill=(120, 128, 140))
    d.text((90, 640), 'SCALE', font=f(MX, 24), fill=(140, 146, 156))
    d.rounded_rectangle((90, 686, 760, 702), 8, fill=(216, 220, 226))
    d.rounded_rectangle((90, 686, 520, 702), 8, fill=AMBER)
    d.ellipse((492, 668, 548, 724), fill=(255, 255, 255), outline=AMBER, width=7)
    d.text((800, 672), '1.4×', font=f(MX, 36), fill=(30, 34, 40))
    # dibujo del mecanismo
    rr(d, (90, 770, 990, 1160), 16, (250, 251, 252), (226, 230, 236), 3)
    cx, cy = 360, 985
    d.ellipse((cx - 110, cy - 110, cx + 110, cy + 110), outline=(60, 66, 76), width=9)
    d.ellipse((cx - 14, cy - 14, cx + 14, cy + 14), fill=(60, 66, 76))
    px, py = cx + 78, cy - 78
    d.ellipse((px - 16, py - 16, px + 16, py + 16), fill=AMBER)
    d.line([(px, py), (820, 1050)], fill=AMBER, width=14)
    d.ellipse((804, 1034, 836, 1066), fill=(60, 66, 76))
    d.line([(760, 1100), (900, 1100)], fill=(190, 196, 204), width=8)
    d.text((110, 790), 'LIVE PREVIEW', font=f(MX, 22), fill=(160, 166, 176))
    d.text((90, 1200), 'MEASUREMENTS FOR YOUR WOOD', font=f(MX, 24), fill=(140, 146, 156))
    rows = [('Crank (radius)', '35 mm'), ('Connecting rod', '110 mm'), ('Stroke', '70 mm'),
            ('Guide (length)', '160 mm'), ('Wood thickness', '14 mm')]
    for i, (a, b) in enumerate(rows):
        y = 1252 + i * 52
        d.line([(90, y + 42), (990, y + 42)], fill=(232, 235, 240), width=2)
        d.text((100, y), a, font=f(MX, 28), fill=(54, 60, 70))
        d.text((980, y), b, font=f(MX, 28), fill=(30, 34, 40), anchor='ra')
    rr(d, (90, 1520, 990, 1572), 12, (240, 242, 246))
    d.text((W / 2, 1530), 'Download PDF sheet', font=f(MX, 28), fill=(70, 78, 90), anchor='mt')
    marco(im, f'{OUT}/app.png'); print('app.png')


cover(); plans(); mechanisms(); phases(); app()
