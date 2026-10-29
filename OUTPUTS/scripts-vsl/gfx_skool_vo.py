"""Visuales de los ads de VOZ EN OFF de Skool AI (2026-10-29).
Copia lo que hace el ganador en ese formato: paginas internas a pantalla completa con un badge naranja
de numero de pagina arriba a la derecha y un headline azul encima, y planos del libro apoyado en el
lugar de trabajo de cada uno. Los planos del libro NO se generan: se recortan de las fotos de los
avatares por debajo del menton, asi entra el libro y el entorno real y no entra ninguna cara.
Uso: python3 gfx_skool_vo.py <carpeta_salida> <carpeta_con_las_fotos_de_avatar>
"""
import os, sys, math
from PIL import Image, ImageDraw, ImageFilter, ImageFont

OUT, SRC = sys.argv[1], sys.argv[2]
os.makedirs(OUT, exist_ok=True)
W, H = 1080, 1920
NAVY = (14, 20, 32)
ORANGE = (247, 147, 30)
PAPER = (247, 245, 241)
GREY = (108, 116, 130)
BLACK = os.path.expanduser('~/Desktop/bachas-concreto/work-mark/fonts/Arial Black.ttf')
BOLD = '/System/Library/Fonts/Supplemental/Arial Bold.ttf'
REG = '/System/Library/Fonts/Supplemental/Arial.ttf'
def f(sz, p=BOLD): return ImageFont.truetype(p, sz)

def desk_bg():
    bg = Image.new('RGB', (W, H), (26, 24, 22))
    for y in range(H):
        v = int(16 + 26 * math.sin(math.pi * y / H))
        bg.paste((26 + v, 24 + v, 22 + v), (0, y, W, y + 1))
    return bg

def index_page(num, head, lines, name):
    """Una pagina de la guia con el badge PAGE NN, como las del ad en ingles del ganador."""
    bg = desk_bg()
    pw, ph = 880, 1240
    px, py = (W - pw) // 2, (H - ph) // 2
    sh = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle((px + 10, py + 22, px + pw + 10, py + ph + 22), 10, fill=(0, 0, 0, 170))
    bg.paste(Image.alpha_composite(bg.convert('RGBA'), sh.filter(ImageFilter.GaussianBlur(26))).convert('RGB'), (0, 0))

    sheet = Image.new('RGBA', (pw, ph), PAPER + (255,))
    d = ImageDraw.Draw(sheet)
    d.rectangle((0, 0, pw, 168), fill=NAVY)
    d.rectangle((0, 168, pw, 175), fill=ORANGE)
    fh = f(44, BLACK)
    words, hl, cur = head.upper().split(), [], ''
    for w_ in words:
        t_ = (cur + ' ' + w_).strip()
        if d.textlength(t_, font=fh) > pw - 120 and cur: hl.append(cur); cur = w_
        else: cur = t_
    hl.append(cur)
    for i, l in enumerate(hl):
        d.text(((pw - d.textlength(l, font=fh)) / 2, (168 - len(hl) * 56) / 2 + i * 56), l, font=fh, fill=(255, 255, 255))
    y = 250
    for t in lines:
        d.rounded_rectangle((60, y, pw - 60, y + 150), 14, fill=(255, 255, 255), outline=(222, 220, 214), width=3)
        d.rounded_rectangle((60, y, 72, y + 150), 6, fill=ORANGE)
        fr = f(31, REG); words, ls, cur = t.split(), [], ''
        for w_ in words:
            t_ = (cur + ' ' + w_).strip()
            if d.textlength(t_, font=fr) > pw - 200 and cur: ls.append(cur); cur = w_
            else: cur = t_
        ls.append(cur)
        for i, l in enumerate(ls): d.text((104, y + (150 - len(ls) * 44) / 2 + i * 44), l, font=fr, fill=NAVY)
        y += 172
    bg.paste(sheet.convert('RGB'), (px, py))

    # el badge naranja de numero de pagina, arriba a la derecha, como el del ganador
    ov = Image.new('RGBA', (W, H), (0, 0, 0, 0)); do = ImageDraw.Draw(ov)
    t = f'PAGE {num}'; fb = f(42, BLACK)
    bw = do.textlength(t, font=fb) + 60
    bx, by = px + pw - bw - 10, py - 34
    do.rounded_rectangle((bx + 5, by + 7, bx + bw + 5, by + 85), 40, fill=(0, 0, 0, 120))
    do.rounded_rectangle((bx, by, bx + bw, by + 78), 39, fill=ORANGE + (255,))
    do.text((bx + 30, by + 16), t, font=fb, fill=NAVY)
    bg.paste(Image.alpha_composite(bg.convert('RGBA'), ov).convert('RGB'), (0, 0))
    bg.save(os.path.join(OUT, name + '.png')); print(name)

def book_in_place(src, name, top):
    """El libro en el lugar de trabajo: se recorta la foto del avatar DESDE el menton hacia abajo."""
    im = Image.open(os.path.join(SRC, src)).convert('RGB')
    w, h = im.size
    y0 = int(h * top)
    ch = h - y0
    cw = int(ch * 9 / 16)
    if cw > w:                      # si no da el ancho, se recorta menos alto
        cw = w; ch = int(cw * 16 / 9); y0 = min(y0, h - ch)
    x0 = max(0, w - cw)            # pegado al borde derecho: ahi esta el libro, entero y sin cortar el titulo
    im.crop((x0, y0, x0 + cw, y0 + ch)).resize((W, H), Image.LANCZOS).save(os.path.join(OUT, name + '.png'))
    print(name)

def closing_card(name):
    """Pago unico + garantia, la placa que el ganador usa antes del CTA."""
    bg = desk_bg(); d = ImageDraw.Draw(bg)
    rows = [('ONE PAYMENT', 'no subscription, no renewals'),
            ('INSTANT DOWNLOAD', 'digital, printable version included'),
            ('7-DAY GUARANTEE', "if it isn't for you, you get your money back")]
    y = 560
    for t1, t2 in rows:
        d.rounded_rectangle((80, y, W - 80, y + 230), 22, fill=(255, 255, 255, 255))
        d.rounded_rectangle((80, y, 96, y + 230), 8, fill=ORANGE)
        d.text((140, y + 48), t1, font=f(52, BLACK), fill=NAVY)
        d.text((140, y + 128), t2, font=f(32, REG), fill=GREY)
        y += 268
    bg.save(os.path.join(OUT, name + '.png')); print(name)

index_page(18, 'Ask about your own files',
           ['Drop in a spreadsheet and ask what changed',
            'Paste a 40-page contract, get ten lines back',
            'Upload a PDF and question it like a person',
            'Nothing to install. It reads what you give it'], 'ix_18')
index_page(24, 'Your inbox, in your own words',
           ['The reply you keep putting off, written for you',
            'Teach it your tone once, it keeps it',
            'Follow-ups that do not sound like a robot',
            'Answer in minutes what used to take an hour'], 'ix_24')
index_page(38, 'Build it once, reuse it forever',
           ['The report you rebuild every single month',
            'Turn your own notes into a fixed template',
            'The quote, the summary, the weekly update',
            'Set it up on Monday, use it all year'], 'ix_38')
index_page(7, 'Start from absolute zero',
           ['Where you type and what you actually say',
            'The four pieces every good request has',
            'Works on the free versions. No card needed',
            'Fifteen minutes and you have used it once'], 'ix_07')
closing_card('cl_terms')
book_in_place('avatar-1-rachel-contadora.png', 'bk_desk', 0.39)
book_in_place('avatar-2-frank-taller.png', 'bk_counter', 0.43)
book_in_place('avatar-4-paul-oficina.png', 'bk_office', 0.45)
book_in_place('avatar-3-diane-abogada.png', 'bk_law', 0.39)
