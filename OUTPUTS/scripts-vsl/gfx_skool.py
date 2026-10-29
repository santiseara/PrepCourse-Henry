"""Paginas internas de la guia Skool AI, para los inserts del medio del ad (2026-10-29).
El ganador corta del avatar a una pagina del libro con chips de herramientas encima; esto las dibuja
con la paleta de la tapa (azul noche + naranja) sobre papel, con sombra, para que parezca una hoja real.
Uso: python3 gfx_skool.py <carpeta_salida>
"""
import os, sys, math
from PIL import Image, ImageDraw, ImageFilter, ImageFont

OUT = sys.argv[1]; os.makedirs(OUT, exist_ok=True)
W, H = 1080, 1920
NAVY = (14, 20, 32)
ORANGE = (247, 147, 30)
PAPER = (247, 245, 241)
GREY = (108, 116, 130)
BLACK = os.path.expanduser('~/Desktop/bachas-concreto/work-mark/fonts/Arial Black.ttf')
BOLD = '/System/Library/Fonts/Supplemental/Arial Bold.ttf'
REG = '/System/Library/Fonts/Supplemental/Arial.ttf'
def f(sz, p=BOLD): return ImageFont.truetype(p, sz)

def page(draw_body, name):
    """Una hoja de papel centrada sobre un escritorio oscuro, con sombra."""
    bg = Image.new('RGB', (W, H), (26, 24, 22))
    for y in range(H):                                  # degradado tipo luz de escritorio
        v = int(16 + 26 * math.sin(math.pi * y / H))
        bg.paste((26 + v, 24 + v, 22 + v), (0, y, W, y + 1))
    pw, ph = 880, 1240
    px, py = (W - pw) // 2, (H - ph) // 2
    sh = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle((px + 10, py + 22, px + pw + 10, py + ph + 22), 10, fill=(0, 0, 0, 170))
    bg.paste(Image.alpha_composite(bg.convert('RGBA'), sh.filter(ImageFilter.GaussianBlur(26))).convert('RGB'), (0, 0))
    sheet = Image.new('RGBA', (pw, ph), PAPER + (255,))
    draw_body(ImageDraw.Draw(sheet), pw, ph, sheet)
    bg.paste(sheet.convert('RGB'), (px, py))
    bg.save(os.path.join(OUT, name + '.png'))
    print(name)

def header(d, pw, t1, t2):
    d.rectangle((0, 0, pw, 150), fill=NAVY)
    d.rectangle((0, 150, pw, 157), fill=ORANGE)
    ft = f(50, BLACK)
    d.text(((pw - d.textlength(t1, font=ft)) / 2, 38), t1, font=ft, fill=(255, 255, 255))
    fs = f(27, BOLD)
    d.text(((pw - d.textlength(t2, font=fs)) / 2, 100), t2, font=fs, fill=ORANGE)

# 1) la formula maestra: los 4 bloques de un prompt
def p_formula(d, pw, ph, im):
    header(d, pw, 'THE MASTER FORMULA', 'ASK ANY AI AND GET EXACTLY WHAT YOU NEED')
    rows = [('ROLE', 'You are a bookkeeper with 20 years of experience'),
            ('CONTEXT', 'I run a small practice. These are my client notes'),
            ('TASK', 'Write the reply. Keep it short and friendly'),
            ('FORMAT', 'Three paragraphs. Plain English. No jargon')]
    y = 230
    for k, (lab, ex) in enumerate(rows):
        d.rounded_rectangle((60, y, pw - 60, y + 190), 14, fill=(255, 255, 255), outline=(222, 220, 214), width=3)
        d.rounded_rectangle((60, y, 74, y + 190), 7, fill=ORANGE)
        d.text((108, y + 30), f'{k+1}. {lab}', font=f(38, BLACK), fill=NAVY)
        fr = f(27, REG); words, lines, cur = ex.split(), [], ''
        for w_ in words:
            t_ = (cur + ' ' + w_).strip()
            if d.textlength(t_, font=fr) > pw - 220 and cur: lines.append(cur); cur = w_
            else: cur = t_
        lines.append(cur)
        for i, l in enumerate(lines): d.text((108, y + 90 + i * 40), l, font=fr, fill=GREY)
        y += 215
page = page  # noqa

# 2) la ruta de 7 dias
def p_path(d, pw, ph, im):
    header(d, pw, 'YOUR 7-DAY PATH', '15 MINUTES A DAY')
    days = ['Talk to it properly', 'Email and messages', 'Long documents', 'Find what you need',
            'Sort out your work', 'Your own templates', 'Make it a habit']
    y = 220
    for i, t in enumerate(days):
        d.rounded_rectangle((60, y, pw - 60, y + 128), 14, fill=(255, 255, 255), outline=(222, 220, 214), width=3)
        d.ellipse((92, y + 30, 160, y + 98), fill=NAVY)
        fd = f(34, BLACK); s = str(i + 1)
        d.text((126 - d.textlength(s, font=fd) / 2, y + 44), s, font=fd, fill=ORANGE)
        d.text((190, y + 34), f'DAY {i+1}', font=f(22, BOLD), fill=ORANGE)
        d.text((190, y + 64), t, font=f(33, BOLD), fill=NAVY)
        y += 146

# 3) con que herramientas funciona
def p_tools(d, pw, ph, im):
    header(d, pw, 'WORKS WITH', 'THE FREE VERSIONS TOO')
    tools = ['ChatGPT', 'Gemini', 'Claude', 'Copilot', 'Perplexity', 'Canva', 'NotebookLM', 'Grok']
    y = 230
    for i in range(0, len(tools), 2):
        for j, t in enumerate(tools[i:i + 2]):
            x = 60 + j * ((pw - 120) // 2 + 10)
            bw = (pw - 130) // 2
            d.rounded_rectangle((x, y, x + bw, y + 150), 20, fill=(255, 255, 255), outline=(222, 220, 214), width=3)
            d.ellipse((x + 26, y + 44, x + 88, y + 106), fill=ORANGE)
            fi = f(32, BLACK)
            d.text((x + 57 - d.textlength(t[0], font=fi) / 2, y + 58), t[0], font=fi, fill=NAVY)
            d.text((x + 106, y + 58), t, font=f(31, BOLD), fill=NAVY)
        y += 168
    fn = f(27, REG); n = 'No subscriptions needed to start.'
    d.text(((pw - d.textlength(n, font=fn)) / 2, y + 16), n, font=fn, fill=GREY)

# 4) los prompts listos para copiar
def p_prompts(d, pw, ph, im):
    header(d, pw, '101 PROMPTS', 'READY TO COPY AND PASTE')
    items = ['Reply to this client without sounding cold',
             'Summarise this 40-page contract in ten lines',
             'Turn these notes into a quote I can send',
             'Clean up this spreadsheet and flag what is missing',
             'Draft the follow-up I keep putting off',
             'Explain this document to me like I am in a hurry']
    y = 235
    for t in items:
        d.rounded_rectangle((60, y, pw - 60, y + 160), 14, fill=(255, 255, 255), outline=(222, 220, 214), width=3)
        d.text((92, y + 26), '“', font=f(64, BLACK), fill=ORANGE)
        fr = f(30, REG); words, lines, cur = t.split(), [], ''
        for w_ in words:
            t_ = (cur + ' ' + w_).strip()
            if d.textlength(t_, font=fr) > pw - 230 and cur: lines.append(cur); cur = w_
            else: cur = t_
        lines.append(cur)
        for i, l in enumerate(lines): d.text((150, y + 42 + i * 42), l, font=fr, fill=NAVY)
        y += 178

for fn_, nm in [(p_formula, 'pg_formula'), (p_path, 'pg_path'), (p_tools, 'pg_tools'), (p_prompts, 'pg_prompts')]:
    page(fn_, nm)
