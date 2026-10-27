"""Captura de chat de WhatsApp para el testimonio del VSL de Calistenia Rusa.
Arma el HTML, lo captura con Chrome headless y genera el clip con scroll lento.
Uso: python3 gfx_wpp_calistenia_rusa.py
"""
import os, subprocess, sys

W = os.path.expanduser('~/Desktop/calistenia-rusa/vsl')
WORK = f'{W}/work/wpp'
os.makedirs(WORK, exist_ok=True)
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
FF = os.path.expanduser('~/bin/ffmpeg')

ALTO = 1920          # una pantalla de teléfono exacta: el chat entra entero
IN, OUT = 'in', 'out'

MSJ = [
    (OUT, 'Sergio, ¿cómo venís con los 28 días?', '8:12'),
    (IN,  'Coach, después de los 50 esa panza no se iba por nada y la espalda me vivía doliendo', '8:40'),
    (IN,  'Los movimientos de bajo impacto fueron mi salvación 🙏', '8:40'),
    (IN,  'Los dolores bajaron y bajé 8 kilos en 21 días', '8:41'),
    (IN,  'Tengo 58 y hace años que no me sentía así. Gracias', '8:42'),
]

def burbujas():
    # la colita va solo en el primero de cada tanda del mismo lado, como en WhatsApp
    h, previo = [], None
    for lado, txt, hora in MSJ:
        tick = '<span class="tick">✓✓</span>' if lado == OUT else ''
        cola = ('<svg class="cola" viewBox="0 0 12 18"><path d="M12 0 C12 10 8 16 0 18 L12 18 Z"/></svg>'
                if lado != previo else '')
        h.append(f'<div class="fila {lado}"><div class="b {lado}{"" if cola else " seguida"}">'
                 f'<div class="t">{txt}</div>'
                 f'<div class="meta">{hora}{tick}</div>{cola}</div></div>')
        previo = lado
    return '\n'.join(h)

HTML = f"""<!doctype html><html><head><meta charset="utf-8"><style>
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{ width:1080px; height:{ALTO}px; font-family:-apple-system,"Helvetica Neue",sans-serif;
        background:#E4DDD4; overflow:hidden; }}
.bg {{ position:absolute; inset:0; background:#E4DDD4;
       background-image:radial-gradient(circle at 12% 18%, rgba(0,0,0,.028) 0 7px, transparent 8px),
                        radial-gradient(circle at 63% 41%, rgba(0,0,0,.025) 0 5px, transparent 6px),
                        radial-gradient(circle at 88% 77%, rgba(0,0,0,.028) 0 9px, transparent 10px),
                        radial-gradient(circle at 34% 88%, rgba(0,0,0,.022) 0 6px, transparent 7px);
       background-size:420px 420px; }}
header {{ position:relative; height:168px; background:#075E54; display:flex; align-items:center;
          padding:0 34px; color:#fff; gap:26px; }}
.flecha {{ font-size:54px; opacity:.95; margin-right:-6px; }}
.av {{ width:104px; height:104px; border-radius:50%; background:#C8D6D2; color:#4A6B63;
       display:flex; align-items:center; justify-content:center; font-size:48px; font-weight:600; }}
.nom {{ font-size:46px; font-weight:600; letter-spacing:-.3px; }}
.est {{ font-size:30px; opacity:.78; margin-top:5px; }}
.chat {{ position:relative; padding:30px 30px 0; }}
.dia {{ text-align:center; margin:8px 0 26px; }}
.dia span {{ background:#DDECDA; color:#5C6B64; font-size:28px; font-weight:500;
             padding:12px 28px; border-radius:12px; box-shadow:0 1px 1px rgba(0,0,0,.09); }}
.fila {{ display:flex; margin-bottom:17px; }}
.fila.in {{ justify-content:flex-start; }}
.fila.out {{ justify-content:flex-end; }}
.b {{ position:relative; max-width:740px; padding:20px 26px 15px; border-radius:18px;
      box-shadow:0 1px 1.5px rgba(0,0,0,.13); }}
.b.in {{ background:#fff; border-top-left-radius:4px; }}
.b.in.seguida {{ border-top-left-radius:18px; }}
.b.out {{ background:#DCF8C6; border-top-right-radius:4px; }}
.b.out.seguida {{ border-top-right-radius:18px; }}
.t {{ font-size:37px; line-height:1.3; color:#111B21; }}
.meta {{ font-size:24px; color:#667781; text-align:right; margin-top:6px; }}
.tick {{ color:#53BDEB; margin-left:8px; font-size:28px; letter-spacing:-5px; }}
.cola {{ position:absolute; top:0; width:12px; height:18px; }}
.barra {{ position:absolute; left:0; right:0; bottom:0; height:150px; display:flex;
          align-items:center; gap:22px; padding:0 28px; }}
.campo {{ flex:1; height:94px; background:#fff; border-radius:47px; display:flex; align-items:center;
          padding:0 38px; font-size:36px; color:#8696A0; box-shadow:0 1px 1.5px rgba(0,0,0,.12); }}
.mic {{ width:94px; height:94px; border-radius:50%; background:#00A884; display:flex;
        align-items:center; justify-content:center; font-size:44px; }}
.b.in .cola {{ left:-10px; transform:scaleX(-1); fill:#fff; }}
.b.out .cola {{ right:-10px; fill:#DCF8C6; }}
</style></head><body>
<div class="bg"></div>
<header><div class="flecha">‹</div><div class="av">S</div>
  <div><div class="nom">Sergio</div><div class="est">en línea</div></div></header>
<div class="chat"><div class="dia"><span>HOY</span></div>
{burbujas()}
</div>
<div class="barra"><div class="campo">Mensaje</div><div class="mic">🎤</div></div>
</body></html>"""

html = f'{WORK}/chat.html'
open(html, 'w').write(HTML)

png = f'{WORK}/chat.png'
subprocess.run([CHROME, '--headless=old', '--disable-gpu', '--no-sandbox', '--hide-scrollbars',
                f'--user-data-dir={WORK}/cd', f'--window-size=1080,{ALTO}',
f'--screenshot={png}', f'file://{html}'],
               capture_output=True)
if not os.path.exists(png):
    print('no salió la captura'); sys.exit(1)
from PIL import Image
im = Image.open(png)
print('captura:', im.size)

# clip: zoom lentísimo, el texto tiene que quedar legible todo el tiempo
SCROLL, HOLD = 26.0, 0.0
vf = ("scale=2160:-2,zoompan=z='min(1.0008^on,1.07)':d=780:s=1080x1920:fps=30,format=yuv420p")
mp4 = f'{W}/broll/wpp-testimonio.mp4'
r = subprocess.run([FF, '-y', '-v', 'error', '-loop', '1', '-framerate', '30', '-i', png,
                    '-t', f'{SCROLL + HOLD}', '-vf', vf, '-c:v', 'libx264', '-crf', '20',
                    '-preset', 'medium', '-pix_fmt', 'yuv420p', mp4], capture_output=True, text=True)
if r.returncode:
    print(r.stderr[-1500:]); sys.exit(1)
import shutil
shutil.copy(mp4, f'{W}/work/brolls/wpp-testimonio.mp4')
print('clip:', mp4, f'{SCROLL + HOLD:.0f}s')
