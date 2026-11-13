# -*- coding: utf-8 -*-
"""Laminas del Kit de Radiestesia dibujadas por codigo (2026-11-13).

El nicho del pendulo no tiene b-roll limpio en TikTok (104 clips bajados, 2 sirvieron), asi que
el visual se arma como el unico ad del ganador SIN persona: fondo violeta estrellado con las
laminas y los biometros en pantalla, paso por paso.

Uso: python3 gfx_pendulo.py   -> escribe los PNG en ~/Desktop/kit-radiestesia/anuncios/work/gfx/
"""
import os, math, random
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1080, 1920
OUT = os.path.expanduser('~/Desktop/kit-radiestesia/anuncios/work/gfx')
FD = os.path.expanduser('~/Desktop/kit-radiestesia/anuncios/work/fonts')
BC = FD + '/BarlowCondensed-ExtraBold.ttf'
BCS = FD + '/BarlowCondensed-SemiBold.ttf'
MX = FD + '/Montserrat-ExtraBold.ttf'
os.makedirs(OUT, exist_ok=True)

VIOLETA = (43, 27, 77)
VIOLETA2 = (24, 14, 46)
PAPEL = (253, 251, 255)
TINTA = (38, 28, 60)
ORO = (232, 201, 106)
CHAKRAS = [('Raíz', (214, 69, 65)), ('Sacro', (232, 136, 58)), ('Plexo', (240, 200, 70)),
           ('Corazón', (106, 190, 120)), ('Garganta', (86, 164, 214)),
           ('Tercer ojo', (92, 102, 190)), ('Corona', (160, 110, 200))]


def f(sz, path=BC): return ImageFont.truetype(path, sz)


def fondo(seed=1):
    im = Image.new('RGB', (W, H), VIOLETA)
    d = ImageDraw.Draw(im)
    for y in range(H):
        t = y / H
        c = tuple(int(VIOLETA[i] * (1 - t) + VIOLETA2[i] * t) for i in range(3))
        d.line([(0, y), (W, y)], fill=c)
    rnd = random.Random(seed)
    for _ in range(170):
        x, y = rnd.randint(0, W), rnd.randint(0, H)
        r = rnd.choice([1, 1, 2, 2, 3])
        a = rnd.randint(60, 210)
        d.ellipse((x - r, y - r, x + r, y + r), fill=(255, 255, 255, a))
    # halo suave arriba
    g = Image.new('L', (W, H), 0)
    ImageDraw.Draw(g).ellipse((-200, -500, W + 200, 700), fill=70)
    im = Image.composite(Image.new('RGB', (W, H), (90, 70, 140)), im, g.filter(ImageFilter.GaussianBlur(120)))
    return im


def papel(im, box, r=34):
    """hoja blanca con sombra"""
    x0, y0, x1, y1 = box
    sh = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle((x0 + 10, y0 + 16, x1 + 10, y1 + 16), r, fill=(0, 0, 0, 130))
    im.paste(Image.alpha_composite(im.convert('RGBA'), sh.filter(ImageFilter.GaussianBlur(18))).convert('RGB'), (0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle(box, r, fill=PAPEL)
    return d


def titulo_lamina(d, txt, y, x0, x1, sz=52, col=TINTA):
    ft = f(sz, BCS)
    lineas, cur = [], ''
    for w_ in txt.split():
        t = (cur + ' ' + w_).strip()
        if d.textlength(t, font=ft) > (x1 - x0 - 80) and cur:
            lineas.append(cur); cur = w_
        else: cur = t
    lineas.append(cur)
    for i, l in enumerate(lineas):
        d.text(((x0 + x1) / 2, y + i * (sz + 8)), l, font=ft, fill=col, anchor='mt')
    return y + len(lineas) * (sz + 8)


def arco(d, cx, cy, R, segs, grosor=58, labels=True):
    """semicirculo dividido en segmentos de color, de izquierda (180) a derecha (0)"""
    n = len(segs)
    for i, (lab, col) in enumerate(segs):
        a0 = 180 + i * (180 / n)
        a1 = 180 + (i + 1) * (180 / n)
        d.pieslice((cx - R, cy - R, cx + R, cy + R), a0, a1, fill=col)
    d.pieslice((cx - R + grosor, cy - R + grosor, cx + R - grosor, cy + R - grosor), 180, 360, fill=PAPEL)
    if labels:
        for i, (lab, col) in enumerate(segs):
            am = math.radians(180 + (i + 0.5) * (180 / n))
            rr = R + 46
            x, y = cx + rr * math.cos(am), cy + rr * math.sin(am)
            ft = f(30, BCS)
            d.text((x, y), lab.upper(), font=ft, fill=TINTA, anchor='mm')


def aguja(im, cx, cy, R, ang_deg, color=(40, 30, 60)):
    """hilo + pendulo apuntando a un angulo (180 = izquierda, 0 = derecha)"""
    d = ImageDraw.Draw(im)
    a = math.radians(ang_deg)
    x, y = cx + (R - 26) * math.cos(a), cy + (R - 26) * math.sin(a)
    d.line([(cx, cy - 300), (x, y)], fill=(70, 55, 100), width=4)
    # cristal
    d.polygon([(x, y - 34), (x - 16, y - 6), (x, y + 40), (x + 16, y - 6)], fill=(176, 148, 230), outline=(90, 70, 150))
    d.ellipse((cx - 9, cy - 309, cx + 9, cy - 291), fill=(90, 70, 150))


def chip(d, txt, cx, y, fill=ORO, col=(40, 30, 10), sz=44):
    ft = f(sz, MX)
    w = d.textlength(txt, font=ft) + 56
    d.rounded_rectangle((cx - w / 2, y, cx + w / 2, y + sz + 34), (sz + 34) // 2, fill=fill)
    d.text((cx, y + 14), txt, font=ft, fill=col, anchor='mt')
    return y + sz + 34


def tick(d, cx, cy, ok=True, r=70):
    col = (60, 150, 105) if ok else (196, 60, 80)
    d.ellipse((cx - r, cy - r, cx + r, cy + r), outline=col, width=10)
    if ok:
        d.line([(cx - 32, cy + 4), (cx - 8, cy + 30), (cx + 34, cy - 28)], fill=col, width=14, joint='curve')
    else:
        d.line([(cx - 28, cy - 28), (cx + 28, cy + 28)], fill=col, width=14)
        d.line([(cx + 28, cy - 28), (cx - 28, cy + 28)], fill=col, width=14)


def guardar(im, nombre):
    im.convert('RGB').save(f'{OUT}/{nombre}.png')
    print(nombre)


# ---------------------------------------------------------------- 1) biometro de chakras
def biometro_chakras(nombre, marca=None, titulo='¿Qué chakra está desarmonizado?'):
    im = fondo(3)
    d = papel(im, (90, 470, W - 90, 1450))
    y = titulo_lamina(d, titulo, 530, 90, W - 90)
    arco(d, W // 2, 1180, 360, CHAKRAS)
    d.text((W // 2, 1230), 'BIÓMETRO DE CHAKRAS', font=f(34, MX), fill=(120, 110, 140), anchor='mt')
    if marca is not None:
        ang = 180 + (marca + 0.5) * (180 / len(CHAKRAS))
        aguja(im, W // 2, 1180, 360, ang)
        d2 = ImageDraw.Draw(im)
        chip(d2, CHAKRAS[marca][0].upper(), W // 2, 1300, fill=CHAKRAS[marca][1], col=(255, 255, 255))
    guardar(im, nombre)


# ---------------------------------------------------------------- 2) biometro de porcentaje
def biometro_pct(nombre, valor, titulo='¿En qué porcentaje?'):
    im = fondo(5)
    d = papel(im, (90, 470, W - 90, 1450))
    titulo_lamina(d, titulo, 530, 90, W - 90)
    segs = [(str(i * 10), (int(214 - i * 10), int(69 + i * 12), int(65 + i * 6))) for i in range(10)]
    arco(d, W // 2, 1180, 360, segs, labels=False)
    for i in range(11):
        a = math.radians(180 + i * 18)
        rr = 360 + 42
        d.text((W // 2 + rr * math.cos(a), 1180 + rr * math.sin(a)), str(i * 10),
               font=f(30, BCS), fill=TINTA, anchor='mm')
    ang = 180 + (valor / 100) * 180
    aguja(im, W // 2, 1180, 360, ang)
    d2 = ImageDraw.Draw(im)
    d2.text((W // 2, 1250), f'{valor}%', font=f(120, MX), fill=TINTA, anchor='mt')
    guardar(im, nombre)


# ---------------------------------------------------------------- 3) biometro de bloqueo
def biometro_bloqueo(nombre, marca=None):
    causas = ['Miedo', 'Duelo', 'Aislamiento', 'Culpa', 'Exigencia']
    cols = [(120, 130, 190), (140, 120, 170), (196, 102, 120), (210, 140, 90), (150, 170, 120)]
    im = fondo(7)
    d = papel(im, (90, 430, W - 90, 1470))
    titulo_lamina(d, '¿Qué está generando el bloqueo?', 490, 90, W - 90)
    segs = [(c.replace('\n', ' '), cols[i]) for i, c in enumerate(causas)]
    arco(d, W // 2, 1200, 350, segs)
    d.text((W // 2, 1250), 'MOTIVO DEL BLOQUEO', font=f(34, MX), fill=(120, 110, 140), anchor='mt')
    if marca is not None:
        ang = 180 + (marca + 0.5) * (180 / len(causas))
        aguja(im, W // 2, 1200, 350, ang)
        d2 = ImageDraw.Draw(im)
        chip(d2, causas[marca].replace('\n', ' ').upper(), W // 2, 1320, fill=cols[marca], col=(255, 255, 255))
    guardar(im, nombre)


# ---------------------------------------------------------------- 4) lamina de chakras en el cuerpo
def lamina_cuerpo(nombre, encendidos=7):
    im = fondo(11)
    d = papel(im, (140, 360, W - 140, 1560))
    titulo_lamina(d, 'Los 7 chakras principales', 420, 140, W - 140)
    cx, top, bot = W // 2, 620, 1420
    d.rounded_rectangle((cx - 90, top, cx + 90, bot), 90, fill=(238, 234, 248))
    d.ellipse((cx - 70, top - 120, cx + 70, top + 20), fill=(238, 234, 248))
    for i, (lab, col) in enumerate(reversed(CHAKRAS)):
        y = top + 40 + i * ((bot - top - 80) / 6)
        on = i < encendidos
        r = 36 if on else 28
        d.ellipse((cx - r, y - r, cx + r, y + r), fill=col if on else (225, 222, 232))
        d.text((cx + 130, y), lab.upper(), font=f(38, BCS), fill=TINTA if on else (170, 165, 185), anchor='lm')
        d.text((cx - 130, y), f'{7 - i}', font=f(40, MX), fill=(150, 145, 170), anchor='rm')
    guardar(im, nombre)


# ---------------------------------------------------------------- 5) lamina del animal
def lamina_animal(nombre, extra=False):
    im = fondo(13)
    d = papel(im, (90, 420, W - 90, 1500))
    titulo_lamina(d, 'Los 10 chakras de tu animal' if extra else 'Los 7 chakras de tu animal', 480, 90, W - 90)
    # silueta simple de perro de perfil
    cx, cy = W // 2, 1050
    cuerpo = (cx - 240, cy - 70, cx + 160, cy + 130)
    d.rounded_rectangle(cuerpo, 90, fill=(238, 234, 248))
    d.ellipse((cx + 120, cy - 170, cx + 300, cy + 10), fill=(238, 234, 248))      # cabeza
    d.polygon([(cx + 150, cy - 150), (cx + 120, cy - 250), (cx + 215, cy - 185)], fill=(238, 234, 248))  # oreja
    d.rounded_rectangle((cx - 300, cy - 30, cx - 200, cy + 40), 40, fill=(238, 234, 248))  # cola
    for i, dx in enumerate([-170, -60, 40, 120]):                                  # patas
        d.rounded_rectangle((cx + dx - 28, cy + 90, cx + dx + 28, cy + 250), 26, fill=(238, 234, 248))
    pts = [(cx - 120, cy - 40, CHAKRAS[0][1]), (cx - 60, cy - 50, CHAKRAS[1][1]), (cx - 10, cy - 55, CHAKRAS[2][1]),
           (cx + 50, cy - 60, CHAKRAS[3][1]), (cx + 130, cy - 90, CHAKRAS[4][1]),
           (cx + 215, cy - 110, CHAKRAS[5][1]), (cx + 250, cy - 140, CHAKRAS[6][1])]
    for x, y, c in pts:
        d.ellipse((x - 26, y - 26, x + 26, y + 26), fill=c)
    if extra:
        marcas = [((cx + 95, cy - 130), 'BRAQUIAL', 'ls'), ((cx + 300, cy - 150), 'MENORES', 'ms'),
                  ((cx - 60, cy + 250), 'PATAS', 'mt')]
        for (x, y), lab, anc in marcas:
            d.ellipse((x - 30, y - 30, x + 30, y + 30), outline=(214, 69, 120), width=8)
            if anc == 'ls':
                d.text((x - 46, y - 10), lab, font=f(34, MX), fill=(214, 69, 120), anchor='rm')
            elif anc == 'ms':
                d.text((x, y - 48), lab, font=f(34, MX), fill=(214, 69, 120), anchor='mb')
            else:
                d.text((x, y + 48), lab, font=f(34, MX), fill=(214, 69, 120), anchor='mt')
        d2 = ImageDraw.Draw(im)
        chip(d2, '+3 QUE SOLO TIENEN ELLOS', W // 2, 1370, fill=(214, 69, 120), col=(255, 255, 255))
    guardar(im, nombre)


# ---------------------------------------------------------------- 6) lamina del hogar
def lamina_hogar(nombre, marcado=None):
    amb = [('Sala', 82), ('Cocina', 74), ('Cuarto 1', 38), ('Cuarto 2', 80), ('Baño', 66), ('Entrada', 71)]
    im = fondo(17)
    d = papel(im, (90, 430, W - 90, 1500))
    titulo_lamina(d, 'Medición del hogar, ambiente por ambiente', 490, 90, W - 90)
    x0, y0, cw, ch = 160, 700, 380, 240
    for i, (lab, pct) in enumerate(amb):
        cx0 = x0 + (i % 2) * (cw + 30)
        cy0 = y0 + (i // 2) * (ch + 30)
        bajo = marcado is not None and i == marcado
        d.rounded_rectangle((cx0, cy0, cx0 + cw, cy0 + ch), 22,
                            fill=(252, 232, 236) if bajo else (240, 238, 248),
                            outline=(214, 69, 120) if bajo else (215, 212, 228), width=6 if bajo else 3)
        d.text((cx0 + cw / 2, cy0 + 34), lab.upper(), font=f(40, BCS), fill=TINTA, anchor='mt')
        if marcado is not None:
            d.text((cx0 + cw / 2, cy0 + 100), f'{pct}%', font=f(78, MX),
                   fill=(214, 69, 120) if bajo else (120, 115, 145), anchor='mt')
    guardar(im, nombre)


# ---------------------------------------------------------------- 7) preguntas
def tarjetas_pregunta(nombre, modo):
    im = fondo(19)
    d = papel(im, (90, 560, W - 90, 1360))
    if modo == 'mal':
        titulo_lamina(d, 'Pregunta mal formulada', 620, 90, W - 90, sz=46, col=(196, 60, 80))
        tick(d, W // 2, 830, ok=False)
        titulo_lamina(d, '"¿Me va a ir bien?"', 950, 90, W - 90, sz=66)
        d.text((W // 2, 1140), 'Bien ¿en qué? ¿cuándo? ¿comparado con qué?',
               font=f(36, BCS), fill=(130, 125, 150), anchor='mt')
    elif modo == 'bien':
        titulo_lamina(d, 'Pregunta bien formulada', 620, 90, W - 90, sz=46, col=(60, 150, 105))
        tick(d, W // 2, 830, ok=True)
        titulo_lamina(d, '"¿Es favorable para mí ir a esa entrevista?"', 950, 90, W - 90, sz=58)
        d.text((W // 2, 1200), 'Un tema · una situación · un momento',
               font=f(36, BCS), fill=(130, 125, 150), anchor='mt')
    else:  # dos cosas
        titulo_lamina(d, 'Dos cosas en una pregunta', 620, 90, W - 90, sz=46, col=(196, 60, 80))
        tick(d, W // 2, 830, ok=False)
        titulo_lamina(d, '"¿Me mudo o me quedo?"', 950, 90, W - 90, sz=62)
        d.text((W // 2, 1140), 'El péndulo confirma o descarta de a una por vez',
               font=f(36, BCS), fill=(130, 125, 150), anchor='mt')
    guardar(im, nombre)


# ---------------------------------------------------------------- 8) desorden vs carpeta
def graficos(nombre, orden):
    im = fondo(23)
    d = ImageDraw.Draw(im)
    rnd = random.Random(4)
    if not orden:
        d.text((W // 2, 300), 'LO QUE TIENES HOY', font=f(56, MX), fill=(255, 255, 255), anchor='mt')
        for i in range(9):
            x = 120 + (i % 3) * 300 + rnd.randint(-40, 40)
            y = 520 + (i // 3) * 360 + rnd.randint(-40, 40)
            card = Image.new('RGB', (250, 300), PAPEL)
            cd = ImageDraw.Draw(card)
            cd.arc((20, 60, 230, 270), 180, 360, fill=(190, 185, 205), width=16)
            cd.line([(125, 165), (125 + rnd.randint(-70, 70), 80)], fill=(150, 145, 170), width=3)
            card = card.rotate(rnd.randint(-14, 14), expand=True, fillcolor=VIOLETA2)
            im.paste(card, (x, y))
        d.text((W // 2, 1500), 'capturas sueltas · sin pregunta · sin orden',
               font=f(40, BCS), fill=(210, 205, 230), anchor='mt')
    else:
        d.text((W // 2, 300), 'LO QUE TRAE EL KIT', font=f(56, MX), fill=ORO, anchor='mt')
        for i in range(12):
            x = 110 + (i % 3) * 300
            y = 480 + (i // 3) * 300
            d.rounded_rectangle((x, y, x + 250, y + 250), 16, fill=PAPEL)
            cx, cy = x + 125, y + 190
            d.arc((cx - 100, cy - 100, cx + 100, cy + 100), 180, 360, fill=CHAKRAS[i % 7][1], width=18)
            d.text((cx, y + 24), ['AURA', 'CHAKRAS', 'EMOCIONES', 'ANIMALES', 'HOGAR', 'PLANTAS',
                                  'AUTO', 'OBJETOS', 'ARCÁNGELES', 'CRISTALES', 'CIRCUITOS', 'ALIMENTOS'][i],
                   font=f(30, MX), fill=TINTA, anchor='mt')
        chip(d, '37 BIÓMETROS · 52 GRÁFICOS · 7 CIRCUITOS', W // 2, 1480, sz=38)
    guardar(im, nombre)


# ---------------------------------------------------------------- 9) placas de paso y portada
def placa_paso(nombre, n, txt):
    im = fondo(29)
    d = ImageDraw.Draw(im)
    chip(d, f'PASO {n}', W // 2, 760, sz=52)
    ft = f(96, BC)
    lineas, cur = [], ''
    for w_ in txt.upper().split():
        t = (cur + ' ' + w_).strip()
        if d.textlength(t, font=ft) > W - 220 and cur: lineas.append(cur); cur = w_
        else: cur = t
    lineas.append(cur)
    for i, l in enumerate(lineas):
        d.text((W // 2, 920 + i * 110), l, font=ft, fill=(255, 255, 255), anchor='mt')
    guardar(im, nombre)


def portada(nombre):
    im = fondo(31)
    d = papel(im, (120, 520, W - 120, 1400))
    titulo_lamina(d, 'KIT DE RADIESTESIA', 600, 120, W - 120, sz=92, col=TINTA)
    d.text((W // 2, 760), 'Aprende a usar tu péndulo paso a paso', font=f(44, BCS), fill=(120, 115, 145), anchor='mt')
    items = ['37 biómetros con la pregunta impresa', '52 gráficos radiónicos', '7 circuitos listos',
             'Aura · chakras · animales · hogar', 'Listo para imprimir en A4']
    for i, it in enumerate(items):
        y = 900 + i * 90
        d.ellipse((190, y + 10, 220, y + 40), fill=(60, 150, 105))
        d.text((250, y), it, font=f(44, BCS), fill=TINTA)
    guardar(im, nombre)


if __name__ == '__main__':
    biometro_chakras('bio_chakras')
    biometro_chakras('bio_chakras_corazon', marca=3)
    biometro_pct('bio_pct_alto', 80)
    biometro_pct('bio_pct_bajo', 20)
    biometro_pct('bio_pct_sube', 90, titulo='Vuelves a medir: ¿subió?')
    biometro_bloqueo('bio_bloqueo')
    biometro_bloqueo('bio_bloqueo_aisl', marca=2)
    lamina_cuerpo('cuerpo_7')
    lamina_cuerpo('cuerpo_3', encendidos=3)
    lamina_animal('animal_7')
    lamina_animal('animal_10', extra=True)
    lamina_hogar('hogar')
    lamina_hogar('hogar_pct', marcado=2)
    tarjetas_pregunta('preg_mal', 'mal')
    tarjetas_pregunta('preg_bien', 'bien')
    tarjetas_pregunta('preg_dos', 'dos')
    graficos('graf_desorden', False)
    graficos('graf_kit', True)
    placa_paso('paso1', 1, '¿Qué chakra está bajo?')
    placa_paso('paso2', 2, '¿Qué lo está bloqueando?')
    placa_paso('paso3', 3, 'Oración y vuelves a medir')
    portada('portada')
