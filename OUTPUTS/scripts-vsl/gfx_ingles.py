# -*- coding: utf-8 -*-
"""Mapas mentales de inglés en ESPAÑOL, dibujados por código (oferta [[ingles-mapas-mentales]], AR).

El producto que modelamos (Fluente com Legenda) es brasileño: todo el cuerpo de sus mapas está en
portugués, así que no hay un solo plano usable de su material para un ad argentino (~85 s limpios
de 1.300 medidos). Estas páginas son el producto en español, con la misma DNA que ellos muestran:
título bilingüe, nivel, nodo central y ramas con significado, estructura, dato rápido, error común
y mini ejercicio. Mismo criterio que los insertos de [[laboratorio-wow]].

La hoja termina en PIE=1500: los últimos 420 px quedan de fondo oscuro para que el subtítulo
quemado del ad no tape ni una línea del material.

Sale a 2x (2160x3840) para que el zoom del editor no pierda filo.
Uso: python3 gfx_ingles.py <dir_salida>
"""
import os, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)
S = 2                       # escala de render
W, H = 1080 * S, 1920 * S
PIE = 1500                  # donde termina la hoja (abajo va la banda del subtítulo)
RUBIK = '/Users/santiagoseara/Library/Fonts/Rubik.ttf'

PAPEL   = (250, 250, 248, 255)
BORDE   = (226, 229, 233, 255)
TINTA   = (17, 24, 39, 255)
GRIS    = (107, 114, 128, 255)
AZUL    = (29, 78, 216, 255)
VERDE   = (22, 163, 74, 255)
NARANJA = (217, 119, 6, 255)
VIOLETA = (109, 40, 217, 255)
ROJO    = (220, 38, 38, 255)
CELESTE = (2, 132, 199, 255)
FONDO   = (16, 24, 39, 255)

def f(size, peso='Regular'):
    fn = ImageFont.truetype(RUBIK, int(size * S))
    try: fn.set_variation_by_name(peso)
    except Exception: pass
    return fn

def pale(c, k=0.12):
    return tuple(int(255 - (255 - v) * k) for v in c[:3]) + (255,)

def sc(*v):
    return tuple(int(x * S) for x in v)

def envolver(d, txt, fn, ancho):
    out, cur = [], ''
    for w in txt.split():
        p = (cur + ' ' + w).strip()
        if d.textlength(p, font=fn) <= ancho * S:
            cur = p
        else:
            if cur: out.append(cur)
            cur = w
    if cur: out.append(cur)
    return out

def hoja(titulo, sub, nivel, color=AZUL, pie=PIE):
    im = Image.new('RGBA', (W, H), FONDO)
    d = ImageDraw.Draw(im)
    sh = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle(sc(44, 72, 1036, pie + 12), int(30 * S), fill=(0, 0, 0, 180))
    im.alpha_composite(sh.filter(ImageFilter.GaussianBlur(int(16 * S))))
    d.rounded_rectangle(sc(40, 60, 1040, pie), int(30 * S), fill=PAPEL, outline=BORDE, width=int(2 * S))
    d.rounded_rectangle(sc(40, 60, 1040, 126), int(30 * S), fill=color)
    d.rectangle(sc(40, 106, 1040, 126), fill=color)
    an = 22 * len(nivel) + 56
    d.rounded_rectangle(sc(78, 152, 78 + an, 214), int(15 * S), fill=pale(color, 0.18))
    d.text(sc(78 + an / 2, 183), nivel, font=f(28, 'Bold'), fill=color, anchor='mm')
    y = 268
    fn_t = f(58, 'ExtraBold')
    for ln in envolver(d, titulo, fn_t, 880):
        d.text(sc(540, y), ln, font=fn_t, fill=TINTA, anchor='mm'); y += 72
    d.text(sc(540, y + 2), sub, font=f(32, 'Medium'), fill=GRIS, anchor='mm')
    return im, d, y + 44

def nodo(d, y, texto, color):
    fn = f(42, 'ExtraBold')
    an = d.textlength(texto, font=fn) / S
    d.rounded_rectangle(sc(540 - an / 2 - 42, y, 540 + an / 2 + 42, y + 88), int(22 * S), fill=color)
    d.text(sc(540, y + 44), texto, font=fn, fill=(255, 255, 255, 255), anchor='mm')
    return y + 88

def ramas(im, d, y0, items, color):
    """items: [(color, TITULO, [lineas])]. '*' = negrita · '-' = cruz roja · '+' = tilde verde."""
    fn_h = f(30, 'ExtraBold'); fn_b = f(29, 'Regular'); fn_m = f(29, 'SemiBold')
    bloques = []
    for c, head, lineas in items:
        ls = []
        for ln in lineas:
            marca = ln[0] if ln[:1] in ('*', '-', '+') else ''
            fn = fn_m if marca else fn_b
            for i, t in enumerate(envolver(d, ln[1:] if marca else ln, fn, 690 if marca in ('-', '+') else 730)):
                ls.append((t, marca if i == 0 else ('*' if marca == '*' else ' ')))
        bloques.append((c, head, ls, 24 + 40 + 6 + len(ls) * 38 + 20))
    total = sum(b[3] for b in bloques)
    libre = PIE - 34 - y0 - total
    gap = max(12, min(26, libre / max(len(bloques) - 1, 1)))
    y = y0 + 18
    ex = 150
    d.line([sc(ex, y0 + 6)[0:2], sc(ex, y + total + gap * (len(bloques) - 1) - 40)[0:2]],
           fill=pale(color, 0.45), width=int(5 * S))
    for c, head, ls, alto in bloques:
        cy = y + 38
        d.line([sc(ex, cy)[0:2], sc(196, cy)[0:2]], fill=pale(c, 0.55), width=int(5 * S))
        d.ellipse(sc(ex - 11, cy - 11, ex + 11, cy + 11), fill=c)
        d.rounded_rectangle(sc(196, y, 1000, y + alto), int(18 * S), fill=pale(c, 0.09))
        d.rounded_rectangle(sc(196, y, 208, y + alto), int(6 * S), fill=c)
        d.rectangle(sc(202, y + 8, 208, y + alto - 8), fill=c)
        d.text(sc(230, y + 20), head, font=fn_h, fill=c)
        yy = y + 20 + 40 + 6
        for t, marca in ls:
            x = 230
            if marca in ('-', '+'):
                cm = ROJO if marca == '-' else VERDE
                cx, cy2 = 246, yy + 16
                if marca == '-':
                    for dx in (1, -1):
                        d.line([sc(cx - 10 * dx, cy2 - 10)[0:2], sc(cx + 10 * dx, cy2 + 10)[0:2]],
                               fill=cm, width=int(5 * S))
                else:
                    d.line([sc(cx - 11, cy2 + 1)[0:2], sc(cx - 4, cy2 + 9)[0:2], sc(cx + 11, cy2 - 10)[0:2]],
                           fill=cm, width=int(5 * S), joint='curve')
                x = 274
            d.text(sc(x, yy), t, font=fn_m if marca else fn_b,
                   fill=TINTA if marca else (55, 65, 81, 255))
            yy += 38
        y += alto + gap
    return im

SEGURO = 0.86   # el editor hace zoom hasta 1,16 sobre la foto fija: si la hoja ocupa todo el
                # cuadro, ese zoom le come el borde y corta el texto. Se guarda al 86 %.

def guardar(im, nombre):
    chica = im.resize((int(W * SEGURO), int(H * SEGURO)), Image.LANCZOS)
    base = Image.new('RGBA', (W, H), FONDO)
    base.paste(chica, (int((W - W * SEGURO) / 2), int(12 * S)))
    base.convert('RGB').save(os.path.join(OUT, nombre + '.png'), quality=95)
    print(nombre)

def encuadres(im, nombre, x0=180, x1=1010):
    """Dos reencuadres de la misma hoja (arriba y abajo) para que el texto entre mas grande.
    Con un solo plano por hoja el ad se duerme; con tres el corte cada 2,4 s tiene de donde elegir."""
    CW, DW = x1 - x0, 1040      # recorte en coordenadas de diseno -> ancho de destino
    k = DW / CW
    for suf, y_top, CH in (('_a', 58, 1010), ('_b', 384, 1104)):
        DH = int(CH * k)
        base = Image.new('RGBA', (W, H), FONDO)
        trozo = im.crop(sc(x0, y_top, x0 + CW, y_top + CH)).resize(sc(DW, DH), Image.LANCZOS)
        y0 = int(60 + (1440 - DH) / 2)
        sh = Image.new('RGBA', (W, H), (0, 0, 0, 0))
        ImageDraw.Draw(sh).rounded_rectangle(sc(24, y0 + 8, 24 + DW, y0 + 8 + DH), int(26 * S), fill=(0, 0, 0, 170))
        base.alpha_composite(sh.filter(ImageFilter.GaussianBlur(int(14 * S))))
        mask = Image.new('L', sc(DW, DH), 0)
        ImageDraw.Draw(mask).rounded_rectangle((0, 0, DW * S - 1, DH * S - 1), int(22 * S), fill=255)
        base.paste(trozo, sc(20, y0), mask)
        guardar(base, nombre + suf)


def mapa(nombre, titulo, sub, nivel, centro, items, color=AZUL):
    im, d, y = hoja(titulo, sub, nivel, color)
    y = nodo(d, y, centro, color)
    im = ramas(im, d, y, items, color)
    guardar(im, nombre)
    encuadres(im, nombre, 58, 1022)

# ======================================================================= MAPAS
mapa('mapa_much_many', 'MUCH Y MANY', 'Much and Many', 'NIVEL A2', 'MUCHO / MUCHOS', [
    (AZUL, 'SIGNIFICADO', ['Los dos significan mucho o muchos.',
                           'Lo que cambia es el sustantivo que va detrás.']),
    (VERDE, 'ESTRUCTURA', ['*MANY + contables:  books, friends, apples',
                           '*MUCH + incontables:  money, water, time']),
    (NARANJA, 'DATO RÁPIDO', ['En afirmativo casi siempre se usa a lot of:',
                              '*I have a lot of friends.']),
    (ROJO, 'ERROR COMÚN', ['-much friends', '+many friends']),
    (VIOLETA, 'MINI EJERCICIO', ['How ____ sugar do you want?',
                                 'How ____ eggs do you need?']),
], AZUL)

mapa('mapa_was_were', 'WAS Y WERE', 'Was and Were', 'NIVEL A2', 'PASADO DE TO BE', [
    (AZUL, 'ESTRUCTURA', ['*WAS  ->  I, he, she, it', '*WERE  ->  you, we, they']),
    (VERDE, 'AFIRMATIVA Y NEGATIVA', ['I was tired.  /  I wasn’t tired.',
                                      'They were at home.  /  They weren’t at home.']),
    (CELESTE, 'PREGUNTA Y RESPUESTA CORTA', ['Were you there?',
                                             '*Yes, I was.  /  No, I wasn’t.']),
    (NARANJA, 'DATO RÁPIDO', ['En inglés formal siempre va were:',
                              '*If I were you...']),
    (ROJO, 'ERROR COMÚN', ['-They was', '+They were']),
    (VIOLETA, 'MINI EJERCICIO', ['She ____ at school yesterday.',
                                 'We ____ very happy.']),
], VERDE)

mapa('mapa_have_has', 'HAVE Y HAS', 'Have and Has', 'NIVEL A1', 'TENER', [
    (AZUL, 'ESTRUCTURA', ['*HAVE  ->  I, you, we, they', '*HAS  ->  he, she, it']),
    (VERDE, 'AFIRMATIVA', ['I have a car.  /  She has a car.']),
    (CELESTE, 'NEGATIVA Y PREGUNTA', ['I don’t have time.  /  He doesn’t have time.',
                                      'Do you have a pen?  /  Does she have a pen?']),
    (NARANJA, 'LAS QUE MÁS SE USAN', ['have breakfast, have a shower, have fun']),
    (ROJO, 'ERROR COMÚN', ['-He have  /  He doesn’t has', '+He has  /  He doesn’t have']),
    (VIOLETA, 'MINI EJERCICIO', ['My brother ____ two dogs.']),
], CELESTE)

mapa('mapa_aeropuerto', 'EN EL AEROPUERTO', 'At the Airport', 'NIVEL A2', 'VIAJAR SIN TRABARTE', [
    (AZUL, 'PALABRAS CLAVE', ['boarding pass (tarjeta de embarque) · gate (puerta)',
                              'luggage (equipaje) · delayed (demorado)']),
    (VERDE, 'FRASES QUE VAS A NECESITAR', ['Where is gate 12?',
                                           'Is the flight delayed?']),
    (CELESTE, 'MINI DIÁLOGO', ['Your passport, please.', '*Here you are.']),
    (NARANJA, 'TIP', ['luggage no tiene plural: nunca luggages.']),
    (ROJO, 'ERROR COMÚN', ['-I lost my baggages', '+I lost my luggage']),
    (VIOLETA, 'MINI EJERCICIO', ['My flight is ____ (demorado).']),
], VIOLETA)

mapa('mapa_cuerpo', 'PARTES DEL CUERPO', 'Parts of the Body', 'NIVEL A1', 'MI CUERPO', [
    (AZUL, 'LA CABEZA', ['head (cabeza) · hair (pelo) · eyes (ojos)',
                         'nose (nariz) · mouth (boca) · ear (oreja)']),
    (VERDE, 'EL CUERPO', ['hand (mano) · arm (brazo) · leg (pierna)',
                          'foot / feet (pie / pies) · back (espalda)']),
    (CELESTE, 'ESTRUCTURA', ['*My + parte del cuerpo + hurts.',
                             'My head hurts. (me duele la cabeza)']),
    (NARANJA, 'DATO RÁPIDO', ['*foot -> feet      tooth -> teeth']),
    (ROJO, 'ERROR COMÚN', ['-my foots', '+my feet']),
    (VIOLETA, 'MINI EJERCICIO', ['____ hurts. (me duele la espalda)']),
], NARANJA)

mapa('mapa_there_is', 'THERE IS Y THERE ARE', 'There is and There are', 'NIVEL A1', 'HAY', [
    (AZUL, 'SIGNIFICADO', ['Los dos se traducen hay.',
                           'Cambia si lo que hay es uno o varios.']),
    (VERDE, 'ESTRUCTURA', ['*THERE IS + singular:  There is a problem.',
                           '*THERE ARE + plural:  There are two problems.']),
    (CELESTE, 'NEGATIVA', ['There isn’t any milk.', 'There aren’t any eggs.']),
    (ROJO, 'ERROR COMÚN', ['-There is many people', '+There are many people']),
    (VIOLETA, 'MINI EJERCICIO', ['____ a cat in the garden.']),
], ROJO)

# ======================================================================= BONUS
def tabla_frases(nombre, titulo, sub, badge, filas, color=AZUL, nota=''):
    im, d, y = hoja(titulo, sub, badge, color)
    fn_h = f(22, 'ExtraBold'); fn_a = f(29, 'SemiBold'); fn_b = f(26, 'Regular')
    x0, x1, x2, x3 = 70, 418, 742, 1010
    d.rounded_rectangle(sc(x0, y, x3, y + 56), int(12 * S), fill=color)
    for xx, t in ((x0 + 16, 'FRASE EN INGLÉS'), (x1 + 16, 'SE PRONUNCIA'), (x2 + 16, 'TRADUCCIÓN')):
        d.text(sc(xx, y + 28), t, font=fn_h, fill=(255, 255, 255, 255), anchor='lm')
    yy = y + 56
    alto = min(104, int((PIE - 80 - yy) / max(len(filas), 1)))
    anchos = {x0 + 16: x1 - x0 - 32, x1 + 16: x2 - x1 - 32, x2 + 16: x3 - x2 - 32}
    for i, (en, pr, es) in enumerate(filas):
        if i % 2 == 0:
            d.rectangle(sc(x0, yy, x3, yy + alto), fill=pale(color, 0.07))
        d.line([sc(x0, yy + alto)[0:2], sc(x3, yy + alto)[0:2]], fill=BORDE, width=int(2 * S))
        for xx, t, fn, col in ((x0 + 16, en, fn_a, TINTA), (x1 + 16, pr, fn_b, color),
                               (x2 + 16, es, fn_b, (55, 65, 81, 255))):
            lineas = envolver(d, t, fn, anchos[xx])
            ty = yy + alto / 2 - (len(lineas) - 1) * 18
            for ln in lineas:
                d.text(sc(xx, ty), ln, font=fn, fill=col, anchor='lm'); ty += 36
        yy += alto
    for xx in (x1, x2):
        d.line([sc(xx, y)[0:2], sc(xx, yy)[0:2]], fill=BORDE, width=int(2 * S))
    if nota:
        d.text(sc(540, yy + 40), nota, font=f(28, 'SemiBold'), fill=GRIS, anchor='mm')
    guardar(im, nombre)
    encuadres(im, nombre, 58, 1022)

tabla_frases('bonus_frases_1', '500 FRASES MÁS USADAS', 'The 500 most used phrases', 'BONUS 2 de 5', [
    ('How are you?', 'jáu ar iú', '¿Cómo estás?'),
    ('What time is it?', 'guát táim is it', '¿Qué hora es?'),
    ('I don’t understand.', 'ái dont anderstánd', 'No entiendo.'),
    ('Can you help me?', 'kén iú jélp mi', '¿Me podés ayudar?'),
    ('See you later.', 'sí iú léiter', 'Nos vemos.'),
    ('I’m on my way.', 'áim on mái uéi', 'Estoy en camino.'),
    ('How much is it?', 'jáu mách is it', '¿Cuánto cuesta?'),
], AZUL, 'Tema 1 de 40  ·  conversación del día a día')

tabla_frases('bonus_frases_2', 'TRABAJO Y ESTUDIO', 'Work and study phrases', 'BONUS 2 de 5', [
    ('I’m looking for a job.', 'áim lúkin for a yob', 'Estoy buscando trabajo.'),
    ('Can we schedule a meeting?', 'ken ui skédiul a míting', '¿Podemos agendar una reunión?'),
    ('I’ll send you the file.', 'áil send iú de fáil', 'Te mando el archivo.'),
    ('Could you repeat that?', 'kud iú ripít dat', '¿Lo podés repetir?'),
    ('I’m studying English.', 'áim stádiin ínglish', 'Estoy estudiando inglés.'),
    ('I need more time.', 'ái nid mor táim', 'Necesito más tiempo.'),
    ('Let me check.', 'let mi chek', 'Dejame ver.'),
], CELESTE, 'Tema 12 de 40  ·  trabajo, oficina y estudio')

def ruta_fluidez(nombre):
    im, d, y = hoja('RUTA DE LA FLUIDEZ', 'Your day by day plan', 'BONUS 3 de 5', VERDE)
    d.text(sc(540, y + 16), 'Plan diario: qué estudiar y en qué orden',
           font=f(30, 'SemiBold'), fill=GRIS, anchor='mm')
    y += 56
    semanas = [
        ('SEMANA 1  ·  ARRANQUE', [('El verbo TO BE (am, is, are)', 1), ('Pronombres personales', 1),
                                   ('Artículos a / an / the', 1), ('Números y colores', 1)]),
        ('SEMANA 2  ·  TU DÍA A DÍA', [('Present simple', 1), ('HAVE y HAS', 1),
                                       ('Rutina: 60 frases', 0), ('Partes del cuerpo', 0)]),
        ('SEMANA 3  ·  HABLAR DEL PASADO', [('WAS y WERE', 0), ('Past simple regulares', 0),
                                            ('Verbos irregulares top 30', 0)]),
    ]
    alto_f = 64
    for tit, items in semanas:
        d.rounded_rectangle(sc(70, y, 1010, y + 50), int(12 * S), fill=VERDE)
        d.text(sc(94, y + 25), tit, font=f(28, 'ExtraBold'), fill=(255, 255, 255, 255), anchor='lm')
        y += 50
        for txt, hecho in items:
            if hecho:
                d.rectangle(sc(70, y, 1010, y + alto_f), fill=pale(VERDE, 0.06))
            d.line([sc(70, y + alto_f)[0:2], sc(1010, y + alto_f)[0:2]], fill=BORDE, width=int(2 * S))
            bx, by = 108, y + alto_f / 2
            d.rounded_rectangle(sc(bx - 20, by - 20, bx + 20, by + 20), int(7 * S),
                                fill=VERDE if hecho else (255, 255, 255, 255),
                                outline=VERDE if hecho else (180, 186, 196, 255), width=int(3 * S))
            if hecho:
                d.line([sc(bx - 10, by + 1)[0:2], sc(bx - 3, by + 9)[0:2], sc(bx + 11, by - 9)[0:2]],
                       fill=(255, 255, 255, 255), width=int(6 * S), joint='curve')
            d.text(sc(152, by), txt, font=f(29, 'SemiBold' if hecho else 'Medium'),
                   fill=TINTA if hecho else (55, 65, 81, 255), anchor='lm')
            y += alto_f
        y += 18
    d.text(sc(540, PIE - 48), 'Tildás lo que ya estudiaste y nunca más te perdés',
           font=f(28, 'SemiBold'), fill=VERDE, anchor='mm')
    guardar(im, nombre)
    encuadres(im, nombre, 58, 1022)

ruta_fluidez('bonus_ruta')

def lista_doble(nombre, titulo, sub, badge, items, color, nota=''):
    im, d, y = hoja(titulo, sub, badge, color)
    fn_a = f(29, 'ExtraBold'); fn_b = f(26, 'Regular')
    n = (len(items) + 1) // 2
    alto = min(96, int((PIE - 70 - y) / n))
    for i, (en, es) in enumerate(items):
        col, fila = i // n, i % n
        x = 70 + col * 480
        yy = y + fila * alto
        d.rounded_rectangle(sc(x, yy, x + 460, yy + alto - 10), int(12 * S), fill=pale(color, 0.08))
        d.rounded_rectangle(sc(x, yy, x + 10, yy + alto - 10), int(5 * S), fill=color)
        d.rectangle(sc(x + 5, yy + 6, x + 10, yy + alto - 16), fill=color)
        d.text(sc(x + 26, yy + 26), en, font=fn_a, fill=color, anchor='lm')
        d.text(sc(x + 26, yy + 60), es, font=fn_b, fill=(55, 65, 81, 255), anchor='lm')
    if nota:
        d.text(sc(540, PIE - 44), nota, font=f(28, 'SemiBold'), fill=GRIS, anchor='mm')
    guardar(im, nombre)
    encuadres(im, nombre, 58, 1022)

lista_doble('bonus_phrasal', '100 PHRASAL VERBS', 'The 100 you really need', 'BONUS 4 de 5', [
    ('get up', 'levantarse'), ('give up', 'rendirse'), ('look for', 'buscar'),
    ('turn on', 'encender'), ('turn off', 'apagar'), ('take off', 'despegar / quitarse'),
    ('run out of', 'quedarse sin'), ('find out', 'enterarse'), ('pick up', 'pasar a buscar'),
    ('put on', 'ponerse'), ('come back', 'volver'), ('work out', 'entrenar / funcionar'),
    ('hang out', 'juntarse'), ('get along', 'llevarse bien'), ('show up', 'aparecer'),
    ('look after', 'cuidar'),
], AZUL, '16 de los 100, ordenados por lo que más se usa')

lista_doble('bonus_expresiones', '150 EXPRESIONES Y MODISMOS', 'Idioms and expressions', 'BONUS 5 de 5', [
    ('a piece of cake', 'pan comido'), ('once in a while', 'de vez en cuando'),
    ('on purpose', 'a propósito'), ('make up your mind', 'decidite'),
    ('it’s up to you', 'como quieras'), ('I’m broke', 'estoy sin plata'),
    ('hang in there', 'aguantá'), ('no big deal', 'no es para tanto'),
    ('out of the blue', 'de la nada'), ('under the weather', 'medio enfermo'),
    ('break the ice', 'romper el hielo'), ('call it a day', 'dejarlo por hoy'),
    ('cost an arm and a leg', 'salir carísimo'), ('get the hang of it', 'agarrarle la mano'),
    ('sooner or later', 'tarde o temprano'), ('as far as I know', 'por lo que sé'),
], VIOLETA, '16 de las 150 que vas a escuchar todo el tiempo')

def grilla_ebooks(nombre):
    im, d, y = hoja('82 EBOOKS Y AUDIOLIBROS', 'Reading and listening library', 'BONUS 1 de 5', NARANJA)
    titulos = ['THE GIFT OF THE MAGI', 'A CHRISTMAS CAROL', 'THE LITTLE PRINCE', 'ALICE IN WONDERLAND',
               'THE TELL-TALE HEART', 'PETER PAN', 'THE UGLY DUCKLING', 'ROBINSON CRUSOE',
               'THE JUNGLE BOOK', 'OLIVER TWIST', 'TREASURE ISLAND', 'THE TIME MACHINE']
    cols = [AZUL, VERDE, NARANJA, VIOLETA, ROJO, CELESTE]
    fn = f(20, 'ExtraBold')
    ax, ay = 212, 268
    for i, t in enumerate(titulos):
        c, r = i % 4, i // 4
        x = 92 + c * (ax + 24); yy = y + 16 + r * (ay + 24)
        col = cols[(i * 5) % len(cols)]
        sh = Image.new('RGBA', (W, H), (0, 0, 0, 0))
        ImageDraw.Draw(sh).rounded_rectangle(sc(x + 4, yy + 8, x + ax + 4, yy + ay + 8), int(10 * S),
                                             fill=(0, 0, 0, 90))
        im.alpha_composite(sh.filter(ImageFilter.GaussianBlur(int(7 * S))))
        d.rounded_rectangle(sc(x, yy, x + ax, yy + ay), int(10 * S), fill=col)
        d.rectangle(sc(x, yy, x + 14, yy + ay), fill=tuple(int(v * 0.72) for v in col[:3]) + (255,))
        tyy = yy + 52
        for ln in envolver(d, t, fn, 150):
            d.text(sc(x + 34, tyy), ln, font=fn, fill=(255, 255, 255, 255)); tyy += 26
        d.line([sc(x + 34, yy + ay - 52)[0:2], sc(x + 104, yy + ay - 52)[0:2]],
               fill=(255, 255, 255, 170), width=int(3 * S))
        d.text(sc(x + 34, yy + ay - 40), 'PDF + AUDIO', font=f(15, 'Bold'), fill=(255, 255, 255, 210))
    d.text(sc(540, PIE - 42), '12 de los 82 que te llevás', font=f(28, 'SemiBold'), fill=GRIS, anchor='mm')
    guardar(im, nombre)
    encuadres(im, nombre, 58, 1022)

grilla_ebooks('bonus_ebooks')

def los_cinco_bonus(nombre):
    im, d, y = hoja('LOS 5 BONUS', 'Everything you also get', 'DE REGALO HOY', ROJO)
    items = [
        (NARANJA, '82', 'EBOOKS Y AUDIOLIBROS', 'Leés y escuchás la misma historia'),
        (AZUL, '500', 'FRASES MÁS USADAS', 'Con la pronunciación y la traducción'),
        (VERDE, 'PLAN', 'RUTA DE LA FLUIDEZ', 'Qué estudiar cada día, con checklist'),
        (CELESTE, '100', 'PHRASAL VERBS', 'Los que de verdad se usan al hablar'),
        (VIOLETA, '150', 'EXPRESIONES Y MODISMOS', 'Para no sonar a traducción literal'),
    ]
    yy = y + 14
    alto = int((PIE - 40 - yy) / 5) - 16
    for col, num, tit, baja in items:
        d.rounded_rectangle(sc(70, yy, 1010, yy + alto), int(18 * S), fill=pale(col, 0.1))
        d.rounded_rectangle(sc(70, yy, 250, yy + alto), int(18 * S), fill=col)
        d.rectangle(sc(230, yy, 250, yy + alto), fill=col)
        d.text(sc(160, yy + alto / 2), num, font=f(48 if len(num) < 4 else 36, 'ExtraBold'),
               fill=(255, 255, 255, 255), anchor='mm')
        d.text(sc(282, yy + alto / 2 - 22), tit, font=f(32, 'ExtraBold'), fill=TINTA, anchor='lm')
        d.text(sc(282, yy + alto / 2 + 22), baja, font=f(26, 'Regular'), fill=(75, 85, 99, 255), anchor='lm')
        yy += alto + 16
    guardar(im, nombre)
    encuadres(im, nombre, 58, 1022)

los_cinco_bonus('bonus_los_cinco')

def niveles(nombre):
    im, d, y = hoja('DEL A1 AL C2', 'From zero to fluent', '+300 MAPAS MENTALES', AZUL)
    items = [('A1', 'FUNDACIÓN', 50, AZUL, 'Arrancás de cero'),
             ('A2', 'CONSTRUCCIÓN', 55, CELESTE, 'Ya armás frases solo'),
             ('B1', 'INDEPENDIENTE', 55, VERDE, 'Te manejás sin ayuda'),
             ('B2', 'NATURAL', 55, NARANJA, 'Hablás sin traducir'),
             ('C1', 'AVANZADO', 50, ROJO, 'Entendés todo'),
             ('C2', 'DOMINIO', 45, VIOLETA, 'Como un nativo')]
    yy = y + 12
    alto = int((PIE - 40 - yy) / 6) - 12
    for cod, nom, n, col, baja in items:
        d.rounded_rectangle(sc(70, yy, 1010, yy + alto), int(16 * S), fill=pale(col, 0.1))
        d.rounded_rectangle(sc(70, yy, 212, yy + alto), int(16 * S), fill=col)
        d.rectangle(sc(192, yy, 212, yy + alto), fill=col)
        d.text(sc(141, yy + alto / 2), cod, font=f(50, 'ExtraBold'), fill=(255, 255, 255, 255), anchor='mm')
        d.text(sc(244, yy + alto / 2 - 20), nom, font=f(31, 'ExtraBold'), fill=TINTA, anchor='lm')
        d.text(sc(244, yy + alto / 2 + 22), baja, font=f(25, 'Regular'), fill=(75, 85, 99, 255), anchor='lm')
        d.text(sc(986, yy + alto / 2 - 16), str(n), font=f(42, 'ExtraBold'), fill=col, anchor='rm')
        d.text(sc(986, yy + alto / 2 + 24), 'mapas', font=f(22, 'SemiBold'), fill=GRIS, anchor='rm')
        yy += alto + 12
    guardar(im, nombre)
    encuadres(im, nombre, 58, 1022)

niveles('niveles')

def grilla_mapas(nombre):
    """La vista de +300: miniaturas de hojas, para el plano de volumen."""
    im = Image.new('RGBA', (W, H), FONDO)
    d = ImageDraw.Draw(im)
    titulos = ['MUCH Y MANY', 'WAS Y WERE', 'HAVE Y HAS', 'THERE IS / ARE', 'PRESENT SIMPLE',
               'PAST SIMPLE', 'A / AN / THE', 'CAN Y CAN’T', 'GOING TO', 'WILL',
               'PRESENT PERFECT', 'COMPARATIVOS', 'SUPERLATIVOS', 'SOME Y ANY', 'DO Y DOES',
               'THIS / THAT', 'PREPOSICIONES', 'IN / ON / AT', 'SAY Y TELL', 'MAKE Y DO',
               'VERBOS IRREGULARES', 'EN EL AEROPUERTO', 'PARTES DEL CUERPO', 'LA COMIDA',
               'LA ROPA', 'LA FAMILIA', 'LOS NÚMEROS', 'LA HORA', 'EL CLIMA', 'EL TRABAJO']
    cols = [AZUL, VERDE, NARANJA, VIOLETA, ROJO, CELESTE]
    aw, ah = 162, 226
    gx, gy = 22, 20
    x0 = (1080 - (5 * aw + 4 * gx)) / 2
    y0 = 60
    fn = f(15, 'ExtraBold')
    for i, t in enumerate(titulos):
        c, r = i % 5, i // 5
        x = x0 + c * (aw + gx); yy = y0 + r * (ah + gy)
        col = cols[(i * 2 + r) % len(cols)]
        sh = Image.new('RGBA', (W, H), (0, 0, 0, 0))
        ImageDraw.Draw(sh).rounded_rectangle(sc(x + 3, yy + 6, x + aw + 3, yy + ah + 6), int(8 * S),
                                             fill=(0, 0, 0, 110))
        im.alpha_composite(sh.filter(ImageFilter.GaussianBlur(int(6 * S))))
        d.rounded_rectangle(sc(x, yy, x + aw, yy + ah), int(8 * S), fill=PAPEL)
        d.rounded_rectangle(sc(x, yy, x + aw, yy + 16), int(8 * S), fill=col)
        d.rectangle(sc(x, yy + 10, x + aw, yy + 16), fill=col)
        ty = yy + 32
        for ln in envolver(d, t, fn, 130):
            d.text(sc(x + aw / 2, ty), ln, font=fn, fill=TINTA, anchor='mm'); ty += 19
        cy = ty + 14
        d.rounded_rectangle(sc(x + 40, cy, x + aw - 40, cy + 17), int(5 * S), fill=col)
        yy2 = cy + 28
        for k in range(4):
            d.rounded_rectangle(sc(x + 16, yy2, x + aw - 16, yy2 + 21), int(4 * S), fill=pale(col, 0.14))
            d.rounded_rectangle(sc(x + 16, yy2, x + 20, yy2 + 21), int(2 * S), fill=col)
            d.line([sc(x + 28, yy2 + 7)[0:2], sc(x + aw - 30, yy2 + 7)[0:2]],
                   fill=(160, 168, 180, 255), width=int(2 * S))
            d.line([sc(x + 28, yy2 + 14)[0:2], sc(x + aw - 60, yy2 + 14)[0:2]],
                   fill=(190, 196, 206, 255), width=int(2 * S))
            yy2 += 25
    guardar(im, nombre)

grilla_mapas('grilla_mapas')
