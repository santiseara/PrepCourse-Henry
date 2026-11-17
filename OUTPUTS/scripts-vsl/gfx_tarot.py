"""Páginas del ebook "Your First Tarot Reading in 2 Days" (mercado inglés, 2026-11-17).

Réplica en inglés del diseño de la guía de Soyjulietacelis, leída de la hoja de contactos de sus ads:
  - columna izquierda angosta, panel azul periwinkle, con la carta Rider-Waite arriba, su nombre en
    versalitas espaciadas y una grilla de atributos con glifos dibujados a línea;
  - columna derecha sobre papel crema: título en Didot, cuerpo en EB Garamond centrado,
    y tres secciones con el título entre filetes — SYMBOLISM, AVAILABLE ENERGY, QUESTIONS TO ASK YOURSELF —
    con viñetas circulares violetas y el folio "P NN" en itálica abajo a la derecha.

Las cartas son del Rider-Waite-Smith (1909), dominio público.

Uso:
  python3 gfx_tarot.py <dir_cartas> <dir_fuentes> <dir_salida> [fondo_madera.jpg]

Si se pasa un fondo de madera, además de cada página suelta escribe las TOMAS DE PRODUCTO
(1080x1920): la página apoyada sobre la mesa, con sombra, una pizca de rotación y la carta
real apoyada al lado. Eso es lo que entra al video como inserto.
"""
import os, sys, math, random
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops

CARDS, FONTS, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
WOOD = sys.argv[4] if len(sys.argv) > 4 else None
os.makedirs(OUT, exist_ok=True)

# ---------------------------------------------------------------- paleta
PAPER   = (250, 246, 238)
BLUE    = (169, 192, 222)
BLUE_D  = (139, 165, 200)
INK     = (46, 58, 84)
INK_S   = (96, 108, 134)
VIOLET  = (123, 111, 168)
WHITE   = (255, 255, 255)

W, H = 1000, 1414                      # A4 a 120 dpi
MX    = 52                             # margen
PANEL_W = 318                          # ancho del panel azul

def f(name, size):
    return ImageFont.truetype(os.path.join(FONTS, name), size)

def didot(size, italic=False):
    p = '/System/Library/Fonts/Supplemental/Didot.ttc'
    return ImageFont.truetype(p, size, index=2 if italic else 0)

F_TITLE  = lambda s: didot(s)
F_BODY   = lambda s: f('EBGaramond.ttf', s)
F_IT     = lambda s: f('EBGaramond-Italic.ttf', s)

# ---------------------------------------------------------------- utilidades
def grain(img, amount=5):
    """Grano de papel: ruido suave multiplicado, para que no se vea plano de PDF."""
    n = Image.effect_noise((img.width, img.height), amount * 9).convert('L')
    n = n.filter(ImageFilter.GaussianBlur(0.6))
    return ImageChops.overlay(img, Image.merge('RGB', (n, n, n))) if False else \
           Image.blend(img, ImageChops.multiply(img, Image.merge('RGB', (n, n, n))), 0.055)

def track(d, xy, txt, font, fill, sp=0, anchor_mid=False):
    """Texto con tracking (letter-spacing). Devuelve el ancho dibujado."""
    x, y = xy
    wtot = sum(font.getlength(c) + sp for c in txt) - sp
    if anchor_mid: x -= wtot / 2
    for c in txt:
        d.text((x, y), c, font=font, fill=fill)
        x += font.getlength(c) + sp
    return wtot

def wrap(d, txt, font, maxw):
    out, line = [], ''
    for word in txt.split():
        t = (line + ' ' + word).strip()
        if d.textlength(t, font=font) <= maxw: line = t
        else:
            if line: out.append(line)
            line = word
    if line: out.append(line)
    return out

def para(d, txt, font, cx, y, maxw, fill, lh, center=True):
    for ln in wrap(d, txt, font, maxw):
        wl = d.textlength(ln, font=font)
        d.text((cx - wl / 2 if center else cx, y), ln, font=font, fill=fill)
        y += lh
    return y

def rule_heading(d, txt, cx, y, maxw, font, fill=INK, sp=3.0):
    """Título de sección con un filete a cada lado, como en la guía original."""
    wtxt = sum(font.getlength(c) + sp for c in txt) - sp
    track(d, (cx - wtxt / 2, y), txt, font, fill, sp)
    yl = y + font.size * 0.62
    gap = wtxt / 2 + 22
    for x0, x1 in ((cx - maxw / 2, cx - gap), (cx + gap, cx + maxw / 2)):
        if x1 > x0: d.line([(x0, yl), (x1, yl)], fill=INK_S, width=1)
    return y + font.size * 1.75

# ---------------------------------------------------------------- glifos a línea
def glyph(d, kind, cx, cy, r, fill=WHITE, w=2):
    bb = [cx - r, cy - r, cx + r, cy + r]
    if kind == 'sun':
        d.ellipse([cx-r*.5, cy-r*.5, cx+r*.5, cy+r*.5], outline=fill, width=w)
        for i in range(8):
            a = i * math.pi / 4
            d.line([(cx+math.cos(a)*r*.72, cy+math.sin(a)*r*.72),
                    (cx+math.cos(a)*r, cy+math.sin(a)*r)], fill=fill, width=w)
    elif kind == 'moon':
        d.arc(bb, 300, 120, fill=fill, width=w)
        d.arc([cx-r*.35, cy-r, cx+r*1.25, cy+r], 290, 130, fill=fill, width=w)
    elif kind == 'fire':
        d.polygon([(cx, cy-r), (cx+r*.86, cy+r*.5), (cx-r*.86, cy+r*.5)], outline=fill, width=w)
    elif kind == 'water':
        d.polygon([(cx, cy+r), (cx+r*.86, cy-r*.5), (cx-r*.86, cy-r*.5)], outline=fill, width=w)
    elif kind == 'air':
        d.polygon([(cx, cy-r), (cx+r*.86, cy+r*.5), (cx-r*.86, cy+r*.5)], outline=fill, width=w)
        d.line([(cx-r*.5, cy), (cx+r*.5, cy)], fill=fill, width=w)
    elif kind == 'earth':
        d.polygon([(cx, cy+r), (cx+r*.86, cy-r*.5), (cx-r*.86, cy-r*.5)], outline=fill, width=w)
        d.line([(cx-r*.5, cy), (cx+r*.5, cy)], fill=fill, width=w)
    elif kind == 'mars':
        d.ellipse([cx-r*.55, cy-r*.25, cx+r*.45, cy+r*.75], outline=fill, width=w)
        d.line([(cx+r*.3, cy-r*.1), (cx+r*.85, cy-r*.7)], fill=fill, width=w)
        d.line([(cx+r*.45, cy-r*.7), (cx+r*.85, cy-r*.7)], fill=fill, width=w)
        d.line([(cx+r*.85, cy-r*.3), (cx+r*.85, cy-r*.7)], fill=fill, width=w)
    elif kind == 'star':
        pts = []
        for i in range(10):
            a = -math.pi/2 + i*math.pi/5
            rr = r if i % 2 == 0 else r*.42
            pts.append((cx+math.cos(a)*rr, cy+math.sin(a)*rr))
        d.polygon(pts, outline=fill, width=w)
    elif kind == 'cup':
        d.arc([cx-r*.7, cy-r*.8, cx+r*.7, cy+r*.4], 0, 180, fill=fill, width=w)
        d.line([(cx, cy+r*.4), (cx, cy+r*.72)], fill=fill, width=w)
        d.line([(cx-r*.45, cy+r*.72), (cx+r*.45, cy+r*.72)], fill=fill, width=w)
    elif kind == 'wand':
        d.line([(cx-r*.6, cy+r*.7), (cx+r*.6, cy-r*.7)], fill=fill, width=w)
        for t in (0.0, 0.5, 1.0):
            x = cx-r*.6 + t*r*1.2; y = cy+r*.7 - t*r*1.4
            d.line([(x-r*.13, y-r*.13), (x+r*.13, y+r*.13)], fill=fill, width=max(1, w-1))
    elif kind == 'sword':
        d.line([(cx, cy-r), (cx, cy+r*.55)], fill=fill, width=w)
        d.line([(cx-r*.5, cy+r*.2), (cx+r*.5, cy+r*.2)], fill=fill, width=w)
        d.line([(cx-r*.18, cy+r*.9), (cx+r*.18, cy+r*.9)], fill=fill, width=w)
    elif kind == 'pentacle':
        d.ellipse(bb, outline=fill, width=w)
        pts = [(cx+math.cos(-math.pi/2+i*2*math.pi/5)*r*.78,
                cy+math.sin(-math.pi/2+i*2*math.pi/5)*r*.78) for i in range(5)]
        for i in range(5): d.line([pts[i], pts[(i+2) % 5]], fill=fill, width=max(1, w-1))
    elif kind == 'num':
        d.ellipse(bb, outline=fill, width=w)
    else:
        d.ellipse(bb, outline=fill, width=w)

def ornament(d, cx, y, col=VIOLET):
    """Pequeño ornamento floral al pie, como el de la guía."""
    d.line([(cx-66, y), (cx-18, y)], fill=col, width=1)
    d.line([(cx+18, y), (cx+66, y)], fill=col, width=1)
    for s in (-1, 1):
        d.arc([cx-11, y-13, cx+11, y+3], 180 if s < 0 else 0, 360 if s < 0 else 180, fill=col, width=1)
    d.line([(cx, y-16), (cx, y+8)], fill=col, width=1)
    d.ellipse([cx-2.5, y-20, cx+2.5, y-15], outline=col, width=1)

# ---------------------------------------------------------------- la página
def page(card, path):
    img = Image.new('RGB', (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- panel azul, con degradé vertical continuo (sin bandas)
    px0, px1 = MX, MX + PANEL_W
    ph = H - 2*MX
    grad = Image.new('RGB', (1, ph))
    gp = grad.load()
    for i in range(ph):
        a = (i / ph) ** 1.35
        gp[0, i] = tuple(int(BLUE[k] + (BLUE_D[k]-BLUE[k])*a) for k in range(3))
    img.paste(grad.resize((PANEL_W, ph), Image.BILINEAR), (px0, MX))

    # ---- la carta, con marco blanco
    cim = Image.open(os.path.join(CARDS, card['img'])).convert('RGB')
    cw = PANEL_W - 104
    cim = cim.resize((cw, int(cw * cim.height / cim.width)), Image.LANCZOS)
    cx0, cy0 = px0 + 52, MX + 46
    d.rectangle([cx0-7, cy0-7, cx0+cw+7, cy0+cim.height+7], fill=WHITE)
    img.paste(cim, (cx0, cy0))

    pcx = (px0 + px1) // 2
    y = cy0 + cim.height + 34
    track(d, (pcx, y), card['name'].upper(), F_BODY(21), WHITE, 4.2, anchor_mid=True)
    y += 40
    d.line([(pcx-54, y), (pcx+54, y)], fill=WHITE, width=1)
    y += 34
    track(d, (pcx, y), 'ATTRIBUTES', F_BODY(17), WHITE, 4.0, anchor_mid=True)
    y += 46

    # ---- grilla de atributos 2 x N
    fa_l = F_BODY(14); fa_v = F_BODY(16)
    for i, (gk, lab, val) in enumerate(card['attrs']):
        col, row = i % 2, i // 2
        gx = px0 + 86 + col * 146
        gy = y + row * 128
        glyph(d, gk, gx, gy, 19, WHITE, 2)
        track(d, (gx, gy + 32), lab.upper(), fa_l, (255, 255, 255, 200), 2.2, anchor_mid=True)
        wv = d.textlength(val, font=fa_v)
        d.text((gx - wv/2, gy + 52), val, font=fa_v, fill=WHITE)

    # ---- frase clave al pie del panel, para que no quede hueco
    y = y + ((len(card['attrs']) + 1) // 2) * 128 + 6
    d.line([(pcx-54, y), (pcx+54, y)], fill=WHITE, width=1)
    y += 30
    track(d, (pcx, y), 'IF IT COMES UP', F_BODY(16), WHITE, 3.6, anchor_mid=True)
    y += 36
    fk = F_IT(21)
    for ln in wrap(d, card['keyline'], fk, PANEL_W - 76):
        d.text((pcx - d.textlength(ln, font=fk)/2, y), ln, font=fk, fill=WHITE)
        y += 30
    y += 18
    fu = F_BODY(15)
    for ln in wrap(d, card['upright'], fu, PANEL_W - 76):
        d.text((pcx - d.textlength(ln, font=fu)/2, y), ln, font=fu, fill=(241, 246, 252))
        y += 22
    ornament(d, pcx, H - MX - 52, WHITE)

    # ---- columna derecha
    rx0, rx1 = px1 + 56, W - MX
    rcx = (rx0 + rx1) // 2
    rw  = rx1 - rx0

    ft = F_TITLE(54)
    wt_ = sum(ft.getlength(c) + 5 for c in card['name'].upper()) - 5
    track(d, (rx1 - wt_, MX + 44), card['name'].upper(), ft, INK, 5)
    y = MX + 44 + 74
    d.line([(rx1 - wt_, y), (rx1, y)], fill=INK_S, width=1)
    y += 30

    fi = F_IT(19)
    y = para(d, card['tagline'], fi, rcx, y, rw, INK_S, 27)
    y += 26

    fb = F_BODY(20)
    y = para(d, card['body'], fb, rcx, y, rw, INK, 29)
    y += 34

    fh = F_BODY(19)
    for head, lines in (('SYMBOLISM', card['symbolism']),
                        ('AVAILABLE ENERGY', card['energy'])):
        y = rule_heading(d, head, rcx, y, rw, fh)
        for ln in lines:
            y = para(d, ln, fb, rcx, y, rw - 40, INK, 29)
            y += 7
        y += 26

    y = rule_heading(d, 'QUESTIONS TO ASK YOURSELF', rcx, y, rw, fh, VIOLET)
    fq = F_BODY(19)
    for q in card['questions']:
        d.ellipse([rx0+4, y+6, rx0+16, y+18], fill=VIOLET)
        for k, ln in enumerate(wrap(d, q, fq, rw - 34)):
            d.text((rx0 + 28, y), ln, font=fq, fill=INK)
            y += 26
        y += 6

    ornament(d, rcx, H - MX - 74)
    fp = F_IT(21)
    pn = 'P %d' % card['page']
    d.text((rx1 - d.textlength(pn, font=fp), H - MX - 36), pn, font=fp, fill=INK_S)

    img = grain(img)
    img.save(path, quality=95)
    return img

# ---------------------------------------------------------------- la tapa
def cover(path):
    img = Image.new('RGB', (W, H), PAPER)
    d = ImageDraw.Draw(img)
    cx = W // 2

    d.ellipse([cx-26, 150, cx+26, 202], outline=BLUE_D, width=2)
    d.ellipse([cx-10, 148, cx+42, 200], fill=PAPER)

    y = 268
    track(d, (cx, y), 'YOUR FIRST', F_TITLE(74), INK, 5, anchor_mid=True)
    y += 96
    ti = didot(90, italic=True)
    wt_ = ti.getlength('tarot reading')
    d.text((cx - wt_/2, y), 'tarot reading', font=ti, fill=(104, 132, 176))
    y += 112
    track(d, (cx, y), 'IN 2 DAYS', F_TITLE(96), INK, 6, anchor_mid=True)
    y += 142

    para(d, 'A PRACTICAL GUIDE TO CONNECT WITH YOUR INTUITION AND READ THE CARDS WITH CONFIDENCE',
         F_BODY(19), cx, y, 560, INK_S, 29)
    y += 110

    # tres cartas abajo
    trio = [('star.jpg', 'THE STAR'), ('death.jpg', 'DEATH'), ('magician.jpg', 'THE MAGICIAN')]
    cw = 196
    for i, (fn, lab) in enumerate(trio):
        im = Image.open(os.path.join(CARDS, fn)).convert('RGB')
        im = im.resize((cw, int(cw * im.height / im.width)), Image.LANCZOS)
        x = cx - int(cw*1.62) + i * int(cw*1.62)  - cw//2 + cw//2
        x = cx + (i - 1) * (cw + 34) - cw // 2
        d.rectangle([x-5, y-5, x+cw+5, y+im.height+5], fill=WHITE)
        img.paste(im, (x, y))
        track(d, (x + cw//2, y + im.height + 18), lab, F_BODY(15), INK_S, 2.6, anchor_mid=True)

    y += 400
    for i, lab in enumerate(('78', 'CARDS', 'BONUS')):
        gx = cx + (i - 1) * 132
        d.ellipse([gx-29, y-29, gx+29, y+29], outline=BLUE_D, width=2)
        glyph(d, ('moon', 'cup', 'star')[i], gx, y, 14, BLUE_D, 2)
        track(d, (gx, y + 42), lab, F_BODY(14), INK_S, 2.2, anchor_mid=True)

    img = grain(img)
    img.save(path, quality=95)
    return img

# ---------------------------------------------------------------- toma de producto
def shot(page_img, card_file, path, seed=0, wood=None):
    """La página apoyada sobre la mesa, con sombra y la carta real al lado. 1080x1920."""
    rnd = random.Random(seed)
    SW, SH = 1080, 1920
    if wood:
        bg = Image.open(wood).convert('RGB')
        s = max(SW / bg.width, SH / bg.height) * 1.08
        bg = bg.resize((int(bg.width*s), int(bg.height*s)), Image.LANCZOS)
        bg = bg.crop(((bg.width-SW)//2, (bg.height-SH)//2,
                      (bg.width-SW)//2+SW, (bg.height-SH)//2+SH))
        bg = bg.filter(ImageFilter.GaussianBlur(5.5))
        bg = Image.blend(bg, Image.new('RGB', (SW, SH), (54, 36, 22)), 0.18)
    else:
        bg = Image.new('RGB', (SW, SH), (92, 62, 38))

    # viñeta cálida
    v = Image.new('L', (SW, SH), 0)
    ImageDraw.Draw(v).ellipse([-SW*0.3, -SH*0.18, SW*1.3, SH*1.18], fill=255)
    v = v.filter(ImageFilter.GaussianBlur(190))
    bg = Image.composite(bg, ImageChops.multiply(bg, Image.new('RGB', (SW, SH), (150, 134, 120))), v)

    pw = int(SW * 0.80)
    pg = page_img.resize((pw, int(pw * page_img.height / page_img.width)), Image.LANCZOS)
    ang = rnd.uniform(-2.6, 2.6)
    pg = pg.rotate(ang, Image.BICUBIC, expand=True, fillcolor=(0, 0, 0))
    mask = Image.new('L', (pw, int(pw * page_img.height / page_img.width)), 255)\
        .rotate(ang, Image.BICUBIC, expand=True, fillcolor=0)

    px = (SW - pg.width) // 2
    py = int(SH * 0.46 - pg.height * 0.5) + rnd.randint(-22, 22)

    sh = Image.new('L', (SW, SH), 0)
    sh.paste(mask, (px + 12, py + 20))
    sh = sh.filter(ImageFilter.GaussianBlur(26))
    bg = Image.composite(ImageChops.multiply(bg, Image.new('RGB', (SW, SH), (86, 78, 70))), bg, sh)
    bg.paste(pg, (px, py), mask)

    if card_file and os.path.exists(os.path.join(CARDS, card_file)):
        ci = Image.open(os.path.join(CARDS, card_file)).convert('RGB')
        cw2 = int(SW * 0.27)
        ci = ci.resize((cw2, int(cw2 * ci.height / ci.width)), Image.LANCZOS)
        ca = rnd.uniform(-13, -5)
        cm = Image.new('L', ci.size, 255).rotate(ca, Image.BICUBIC, expand=True, fillcolor=0)
        ci = ci.rotate(ca, Image.BICUBIC, expand=True, fillcolor=(0, 0, 0))
        bx, by = int(SW * 0.58), py + pg.height - int(ci.height * 0.28)
        s2 = Image.new('L', (SW, SH), 0); s2.paste(cm, (bx + 8, by + 12))
        s2 = s2.filter(ImageFilter.GaussianBlur(16))
        bg = Image.composite(ImageChops.multiply(bg, Image.new('RGB', (SW, SH), (96, 88, 80))), bg, s2)
        bg.paste(ci, (bx, by), cm)

    bg.save(path, quality=94)

# ---------------------------------------------------------------- contenido
CARDS_DATA = [
 dict(key='tower', keyline='Something is ending the way it should.', upright='Upright: rupture, revelation, a foundation giving way. Reversed: a collapse you are postponing.', img='tower.jpg', name='The Tower', page=16,
   attrs=[('mars','planet','Mars'), ('fire','element','Fire'),
          ('num','number','16'), ('star','keyword','Rupture')],
   tagline='Sudden change · Revelation · The structure that could not hold',
   body='The Tower is the collapse of something built on a foundation that was never true. '
        'It does not arrive to punish you. It arrives because the story you were telling about '
        'that structure finally ran out of room.',
   symbolism=[
     'The crown falling from the top is a borrowed identity, an idea of yourself that was handed to you and never really fit.',
     'The lightning is sudden information. One thing is seen and cannot be unseen.',
     'The two figures fall outward, away from the tower. They are leaving it, not being buried under it.',
     'The flames take the windows first, the places where you looked out and saw only what you wanted to see.'],
   energy=[
     'A clearing. What breaks here was already cracked, and you were the one holding it upright.',
     'The energy available is the honesty that comes after you stop defending something, and the strange lightness of putting it down.'],
   questions=[
     'What am I holding up that would fall on its own if I let go?',
     'What have I already seen clearly and keep explaining away?',
     'If this collapsed tomorrow, what would I finally be free to build?',
     'Who am I without the title I am protecting?']),

 dict(key='death', keyline='Stop maintaining what already closed.', upright='Upright: endings, transition, clearing. Reversed: resistance, holding a finished thing open.', img='death.jpg', name='Death', page=13,
   attrs=[('water','sign','Scorpio'), ('water','element','Water'),
          ('num','number','13'), ('moon','keyword','Closure')],
   tagline='Endings · Transformation · Making room',
   body='Death almost never speaks about a body. It speaks about a cycle that has already finished, '
        'and about the part of you that keeps showing up to it anyway.',
   symbolism=[
     'The skeleton is what remains when everything temporary is gone: the structure underneath.',
     'The white rose on the black flag is renewal. The ending is not the opposite of life, it is the condition for it.',
     'The horse moves at a steady walk. This is not violence, it is procession.',
     'Between the two towers in the distance a sun is rising, not setting.'],
   energy=[
     'A closing that makes room. The energy here is release rather than loss.',
     'You are being asked to stop maintaining something out of habit, so the next thing has somewhere to arrive.'],
   questions=[
     'What has already ended that I am still attending to?',
     'What am I afraid to call finished?',
     'What would I make room for if I let this close?',
     'Which version of me is ready to be left behind?']),

 dict(key='cups04', keyline='Look up. It is already on the table.', upright='Upright: apathy, saturation, a missed offer. Reversed: attention returning, renewed interest.', img='cups04.jpg', name='Four of Cups', page=52,
   attrs=[('cup','suit','Cups'), ('water','element','Water'),
          ('num','number','4'), ('moon','keyword','Pause')],
   tagline='Cups is what you feel · Four is the pause',
   body='A figure sits under a tree with three cups in front of him, arms crossed, looking at none of them. '
        'A fourth cup is being offered from a cloud and he has not noticed it yet.',
   symbolism=[
     'The crossed arms are not refusal, they are saturation. He has had enough of what is already there.',
     'The three cups on the ground are everything he already received and stopped tasting.',
     'The hand in the cloud is an offer arriving from outside his line of sight.',
     'The tree gives shade, which is comfortable, and also keeps him seated.'],
   energy=[
     'A quiet discontent that is doing a job: it is telling you that what used to feed you does not anymore.',
     'The energy available is attention. Nothing new needs to be built. Something is already being handed to you.'],
   questions=[
     'What is being offered to me that I keep looking past?',
     'Where have I confused comfort with contentment?',
     'What stopped feeding me, and when did I notice?',
     'What would change if I simply looked up?']),

 dict(key='wands08', keyline='What you launched is about to land.', upright='Upright: speed, messages, convergence. Reversed: delays, scattered effort, haste.', img='wands08.jpg', name='Eight of Wands', page=68,
   attrs=[('wand','suit','Wands'), ('fire','element','Fire'),
          ('num','number','8'), ('air','keyword','Speed')],
   tagline='Wands is what you do · Eight is the speed',
   body='Eight wands fly through open sky over a green valley. There is no figure in this card. '
        'Nothing is being decided here, everything is already in motion.',
   symbolism=[
     'The wands are in the air, not in anyone\'s hands. What was launched is no longer yours to steer.',
     'They fly parallel, all in one direction: things converging instead of scattering.',
     'The ground below is green and settled, which is what makes the speed safe.',
     'They are tipped downward, beginning to land. Arrival, not departure.'],
   energy=[
     'Momentum. Messages, answers and movement that all show up at once after a long flat stretch.',
     'The energy available is readiness, not effort. The work was done earlier.'],
   questions=[
     'What have I set in motion that is about to land?',
     'Where am I pushing something that is already moving on its own?',
     'Am I ready to receive several answers at the same time?',
     'What would I do this week if the waiting ended tomorrow?']),

 dict(key='pents02', keyline='You are carrying more than you agreed to.', upright='Upright: juggling, adaptability, rhythm. Reversed: overload, a choice made for you.', img='pents02.jpg', name='Two of Pentacles', page=74,
   attrs=[('pentacle','suit','Pentacles'), ('earth','element','Earth'),
          ('num','number','2'), ('water','keyword','Balance')],
   tagline='Pentacles is what you build · Two is the balance',
   body='A figure juggles two pentacles bound by a ribbon shaped like an endless loop, '
        'while behind him two ships rise and fall on a heavy sea.',
   symbolism=[
     'The ribbon is a lemniscate: this is not chaos, it is a rhythm that can be sustained for a while.',
     'He is standing on one foot. It works, and it is not a resting position.',
     'The ships in the background rise and fall, which is the part he does not control.',
     'Both pentacles stay in the air because he keeps moving. Stopping is what drops them.'],
   energy=[
     'Agility. You are managing more than one thing well, and the cost of that is not visible yet.',
     'The energy available is honesty about capacity, before the choice gets made for you.'],
   questions=[
     'What am I keeping in the air that I have not agreed to carry?',
     'Which of these two would I drop if I had to choose today?',
     'Where am I calling it balance when it is really speed?',
     'What would rest look like if nothing fell?']),

 dict(key='magician', keyline='You already have the four tools.', upright='Upright: initiative, capacity, focus. Reversed: scattered will, talent left unused.', img='magician.jpg', name='The Magician', page=1,
   attrs=[('sun','planet','Mercury'), ('air','element','Air'),
          ('num','number','1'), ('star','keyword','Will')],
   tagline='Beginnings · Capacity · Everything already on the table',
   body='The Magician stands at a table holding a cup, a wand, a sword and a pentacle. '
        'Everything he needs is already in front of him. The card is about using it.',
   symbolism=[
     'One hand points up and one points down: what you think about is what you end up building.',
     'The four suits on the table are the four tools you already have, not ones you need to find.',
     'The lemniscate above his head is capacity without an obvious limit.',
     'Roses and lilies at his feet: desire and clarity growing from the same ground.'],
   energy=[
     'Initiative. The beginning of something you are genuinely equipped for.',
     'The energy available is focus, which is the only thing that turns the four tools into one result.'],
   questions=[
     'What do I already have that I keep treating as missing?',
     'What am I waiting to be given permission for?',
     'Where is my attention actually going?',
     'What is the smallest first move I could make today?']),

 dict(key='star', keyline='What comes after there is nothing to defend.', upright='Upright: hope, repair, clarity. Reversed: borrowed faith, hope held at a distance.', img='star.jpg', name='The Star', page=17,
   attrs=[('star','sign','Aquarius'), ('air','element','Air'),
          ('num','number','17'), ('water','keyword','Hope')],
   tagline='Renewal · Clarity · The quiet after the rupture',
   body='The Star comes directly after The Tower, and that order is the whole message. '
        'It is what becomes possible once there is nothing left to defend.',
   symbolism=[
     'She has one foot on land and one in the water: grounded and feeling at the same time.',
     'She pours from two jugs, giving back to the pond and to the earth. Nothing is being hoarded.',
     'She is uncovered. There is no longer anything that needs hiding.',
     'Eight stars above her, one larger: many small reasons and one clear direction.'],
   energy=[
     'Repair that does not need to be forced. Slow, legible, honest.',
     'The energy available is trust, earned rather than borrowed.'],
   questions=[
     'What has been quietly healing while I was not watching?',
     'What am I ready to stop hiding?',
     'Where could I give without it costing me?',
     'What is the one star I am actually walking toward?']),

 dict(key='moon', keyline='You are not lost, you are early.', upright='Upright: intuition, uncertainty, the unsaid. Reversed: confusion lifting, truth surfacing.', img='moon.jpg', name='The Moon', page=18,
   attrs=[('moon','sign','Pisces'), ('water','element','Water'),
          ('num','number','18'), ('moon','keyword','Uncertainty')],
   tagline='Intuition · Confusion · What is not being said',
   body='The Moon is the card people most often read as a warning. It is closer to a description: '
        'you are walking a road you can only partly see, and that is not the same as being lost.',
   symbolism=[
     'A dog and a wolf howl at the moon: the tame and the untamed reacting to the same thing.',
     'A crayfish climbs out of the pool, something from underneath coming up to be looked at.',
     'The path runs between two towers and keeps going past them, into what is not drawn.',
     'The moon has a face and also phases: what you are seeing is real and also incomplete.'],
   energy=[
     'Heightened intuition and lowered visibility, at the same time.',
     'The energy available is patience. Decisions made here are usually made again later.'],
   questions=[
     'What do I know that I have not let myself say plainly?',
     'Which fear here is memory and which is information?',
     'What am I filling in because I cannot see it?',
     'What could wait until there is more light?']),
]

# ---------------------------------------------------------------- correr
if __name__ == '__main__':
    cover(os.path.join(OUT, 'cover.jpg'))
    print('cover.jpg')
    for i, c in enumerate(CARDS_DATA):
        p = os.path.join(OUT, 'page_%s.jpg' % c['key'])
        im = page(c, p)
        print(os.path.basename(p))
        if WOOD:
            shot(im, c['img'], os.path.join(OUT, 'shot_%s.jpg' % c['key']), seed=i, wood=WOOD)
            print('  shot_%s.jpg' % c['key'])
    if WOOD:
        cv = Image.open(os.path.join(OUT, 'cover.jpg'))
        shot(cv, None, os.path.join(OUT, 'shot_cover.jpg'), seed=99, wood=WOOD)
        print('  shot_cover.jpg')
