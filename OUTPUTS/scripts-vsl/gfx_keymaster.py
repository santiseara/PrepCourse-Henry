# -*- coding: utf-8 -*-
"""Maquetas de la app de KeyMaster Hub, dibujadas por codigo (nada de capturas).

El competidor muestra su plataforma dos o tres veces por video: el catalogo, la
busqueda y la ficha tecnica del vehiculo. Son el plano que vende, porque es lo
unico que demuestra que el producto existe.

Se dibujan en vez de capturarse por dos razones: su app esta en espanol y con
vehiculos latinoamericanos (HB20, Gol, Onix), y nosotros vamos al mercado
ingles, donde el parque es otro.

Uso: python3 gfx_keymaster.py <carpeta_salida>
"""
import os, sys
from PIL import Image, ImageDraw, ImageFont

OUT = sys.argv[1] if len(sys.argv) > 1 else '.'
os.makedirs(OUT, exist_ok=True)

W, H = 1080, 1920                      # vertical 9:16, igual que ellos
BG      = (13, 16, 22)
PANEL   = (22, 26, 34)
PANEL2  = (28, 33, 43)
LINE    = (44, 51, 64)
TXT     = (232, 236, 243)
MUTED   = (138, 148, 166)
GOLD    = (240, 178, 60)               # su acento
GREEN   = (52, 199, 123)

F = '/Users/santiagoseara/PrepCourse-Henry/OUTPUTS/scripts-producto/fonts/'
def font(name, size):
    for p in (F + name, '/System/Library/Fonts/Supplemental/Arial.ttf'):
        try: return ImageFont.truetype(p, size)
        except Exception: pass
    return ImageFont.load_default()

BOLD   = lambda s: font('Barlow-Bold.ttf', s)
SEMI   = lambda s: font('Barlow-SemiBold.ttf', s)
MED    = lambda s: font('Barlow-Medium.ttf', s)
REG    = lambda s: font('Barlow-Regular.ttf', s)


def base():
    im = Image.new('RGB', (W, H), BG)
    d = ImageDraw.Draw(im)
    # barra de estado
    d.text((54, 40), '9:41', font=SEMI(34), fill=TXT)
    d.rounded_rectangle([W-150, 42, W-54, 70], 8, outline=MUTED, width=3)
    d.rounded_rectangle([W-146, 46, W-80, 66], 5, fill=GREEN)
    # cabecera de la app
    d.text((54, 112), 'KeyMaster', font=BOLD(46), fill=TXT)
    d.text((300, 112), 'Hub', font=BOLD(46), fill=GOLD)
    d.text((56, 166), 'AUTOMOTIVE KEY DATABASE', font=SEMI(24), fill=MUTED)
    for i in range(3):
        d.ellipse([W-86, 124+i*18, W-72, 138+i*18], fill=MUTED)
    d.line([(0, 222), (W, 222)], fill=LINE, width=2)
    return im, d


def barra_busqueda(d, y, texto, cursor=False):
    d.rounded_rectangle([54, y, W-54, y+96], 18, fill=PANEL2,
                        outline=GOLD if cursor else LINE, width=3)
    d.ellipse([86, y+34, 116, y+64], outline=MUTED, width=4)
    d.line([(112, y+60), (126, y+74)], fill=MUTED, width=4)
    d.text((152, y+28), texto, font=MED(38), fill=TXT if cursor else MUTED)
    if cursor:
        x = 152 + d.textlength(texto, font=MED(38)) + 6
        d.line([(x, y+26), (x, y+70)], fill=GOLD, width=4)


def fila_vehiculo(d, y, marca, modelo, anios, tipo, chip):
    d.rounded_rectangle([54, y, W-54, y+168], 18, fill=PANEL, outline=LINE, width=2)
    d.rounded_rectangle([82, y+30, 166, y+114], 14, fill=PANEL2, outline=LINE, width=2)
    ini = ''.join(p[0] for p in marca.split()[:2]).upper()
    wv = d.textlength(ini, font=BOLD(40))
    d.text((124-wv/2, y+52), ini, font=BOLD(40), fill=GOLD)
    d.text((196, y+30), marca, font=SEMI(30), fill=MUTED)
    d.text((196, y+66), modelo, font=BOLD(42), fill=TXT)
    d.text((196, y+118), anios, font=MED(28), fill=MUTED)
    for i, (et, v) in enumerate((('KEY', tipo), ('CHIP', chip))):
        yy = y + 36 + i*54
        d.text((W-330, yy), et, font=SEMI(24), fill=MUTED)
        wv = d.textlength(v, font=SEMI(30))
        d.text((W-96-wv, yy-6), v, font=SEMI(30), fill=GOLD)


def dato(d, y, etiqueta, valor, destacado=False):
    d.text((86, y), etiqueta, font=MED(30), fill=MUTED)
    f = BOLD(34) if destacado else SEMI(34)
    w = d.textlength(valor, font=f)
    d.text((W-86-w, y-4), valor, font=f, fill=GOLD if destacado else TXT)
    d.line([(86, y+52), (W-86, y+52)], fill=LINE, width=2)


def tabs(d):
    y = H - 150
    d.line([(0, y), (W, y)], fill=LINE, width=2)
    etiquetas = ['Vehicles', 'Transponders', 'Blanks', 'Remotes']
    for i, t in enumerate(etiquetas):
        cx = W/8 + i*W/4
        col = GOLD if i == 0 else MUTED
        d.rounded_rectangle([cx-20, y+34, cx+20, y+66], 7, outline=col, width=3)
        w = d.textlength(t, font=MED(24))
        d.text((cx-w/2, y+82), t, font=MED(24), fill=col)


# ---------------------------------------------------------------------------
# 1 · catalogo
# ---------------------------------------------------------------------------
im, d = base()
d.text((54, 262), 'Vehicle Catalog', font=BOLD(56), fill=TXT)
d.text((56, 334), 'Technical database  ·  412 vehicles', font=MED(30), fill=MUTED)
barra_busqueda(d, 396, 'Search vehicle...')
y = 528
for marca, modelo, anios, tipo, chip in [
        ('FORD',      'F-150',     '2015 - 2020', 'Smart Key',   'ID49'),
        ('CHEVROLET', 'Silverado', '2014 - 2018', 'Transponder', 'ID46'),
        ('HONDA',     'Civic',     '2016 - 2021', 'Smart Key',   'ID47'),
        ('TOYOTA',    'Camry',     '2018 - 2024', 'Smart Key',   'H-Chip'),
        ('RAM',       '1500',      '2013 - 2018', 'Fobik',       'ID46')]:
    fila_vehiculo(d, y, marca, modelo, anios, tipo, chip)
    y += 192
tabs(d)
im.save(os.path.join(OUT, 'app-catalogo.png'))

# ---------------------------------------------------------------------------
# 2 · buscando
# ---------------------------------------------------------------------------
im, d = base()
d.text((54, 262), 'Vehicle Catalog', font=BOLD(56), fill=TXT)
d.text((56, 334), 'Technical database  ·  412 vehicles', font=MED(30), fill=MUTED)
barra_busqueda(d, 396, 'silver', cursor=True)
y = 528
fila_vehiculo(d, y, 'CHEVROLET', 'Silverado', '2014 - 2018', 'Transponder', 'ID46')
fila_vehiculo(d, y+192, 'CHEVROLET', 'Silverado HD', '2015 - 2019', 'Smart Key', 'ID46')
d.text((86, y+420), '2 results', font=MED(30), fill=MUTED)
tabs(d)
im.save(os.path.join(OUT, 'app-buscando.png'))

# ---------------------------------------------------------------------------
# 3 · ficha tecnica (el plano que vende)
# ---------------------------------------------------------------------------
im, d = base()
d.rounded_rectangle([54, 270, 150, 366], 16, fill=PANEL2, outline=LINE, width=2)
d.text((76, 296), 'CH', font=BOLD(40), fill=GOLD)
d.text((176, 272), 'CHEVROLET', font=SEMI(30), fill=MUTED)
d.text((176, 308), 'Silverado', font=BOLD(58), fill=TXT)
d.rounded_rectangle([176, 388, 400, 440], 26, fill=(40, 34, 20), outline=GOLD, width=2)
d.text((200, 396), '2014 - 2018', font=SEMI(28), fill=GOLD)
d.text((440, 396), '★  Save', font=MED(28), fill=MUTED)

d.text((86, 500), 'TECHNICAL SPECS', font=BOLD(28), fill=MUTED)
d.rounded_rectangle([54, 548, W-54, 1196], 20, fill=PANEL, outline=LINE, width=2)
y = 598
for et, v, dest in [('Key type',     'Transponder', False),
                    ('Transponder',  'ID46 / PCF7936', True),
                    ('FCC ID',       'OHT01060512',   True),
                    ('Frequency',    '315 MHz',       True),
                    ('Key blank',    'B111-PT',       True),
                    ('Buttons',      '4 buttons',     False),
                    ('Battery',      'CR2032',        False),
                    ('Programming',  'OBD',           False)]:
    dato(d, y, et, v, dest)
    y += 78

d.rounded_rectangle([54, 1240, W-54, 1420], 20, fill=(40, 34, 20), outline=GOLD, width=2)
d.text((90, 1272), '⚠  NOTES', font=BOLD(28), fill=GOLD)
d.text((90, 1322), 'Check exact year before cutting.', font=MED(32), fill=TXT)
d.text((90, 1364), 'Separate remote on some trims.', font=MED(32), fill=TXT)
tabs(d)
im.save(os.path.join(OUT, 'app-ficha.png'))

# ---------------------------------------------------------------------------
# 4 · menu lateral (las secciones = la promesa del producto)
# ---------------------------------------------------------------------------
im, d = base()
d.text((54, 262), 'Browse', font=BOLD(56), fill=TXT)
y = 372
for i, (ic, t, sub) in enumerate([
        ('VE', 'Vehicles',     '412 models, year by year'),
        ('TR', 'Transponders', 'Cross-reference by chip'),
        ('BL', 'Key blanks',   'Full visual library'),
        ('RE', 'Remotes',      'FCC ID, frequency, buttons'),
        ('SH', 'Shells',       'Compatible housings'),
        ('BA', 'Batteries',    'What fits what'),
        ('PR', 'Procedures',   'Step-by-step programming')]):
    d.rounded_rectangle([54, y, W-54, y+150], 18, fill=PANEL, outline=LINE, width=2)
    d.rounded_rectangle([84, y+34, 166, y+116], 14, fill=PANEL2, outline=LINE, width=2)
    w = d.textlength(ic, font=BOLD(34))
    d.text((125-w/2, y+56), ic, font=BOLD(34), fill=GOLD)
    d.text((196, y+36), t, font=BOLD(40), fill=TXT)
    d.text((196, y+88), sub, font=MED(28), fill=MUTED)
    d.text((W-110, y+56), '›', font=BOLD(44), fill=MUTED)
    y += 170
im.save(os.path.join(OUT, 'app-secciones.png'))

print('listas 4 maquetas en', OUT)
