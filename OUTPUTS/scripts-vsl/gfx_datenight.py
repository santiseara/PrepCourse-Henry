# -*- coding: utf-8 -*-
"""Paginas del producto de Noche de Citas Cristiana (Argentina, 2026-11-10).

Clonadas de Date Night Cristao (Ana Cristina, BR, dateparacasais.com.br), que en la segunda
mitad de cada ad muestra las hojas del producto a pantalla completa: el juego de cartas, las
cartas de preguntas, el devocional, las oraciones guiadas, los desafios, el bingo, verdad o
desafio y los 4 temperamentos. Se dibujan por codigo (HTML + Chrome headless), asi que no hace
falta que el producto exista todavia (regla del 2026-11-05 de [[guiones-y-anuncios]]).

Paleta leida de sus hojas: papel crema, vino, dorado y tinta marron.

Cada pagina sale sobre un lienzo 1.10x con el sobrante desenfocado, porque el editor le mete
zoom a los planos fijos.

Uso: python3 gfx_datenight.py
"""
import os, subprocess
from PIL import Image, ImageFilter

OUT = os.path.expanduser('~/Desktop/date-night/anuncios/work/gfx')
os.makedirs(OUT, exist_ok=True)
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
W, H = 1080, 1920
MW, MH = 1188, 2112            # 1.10x

PAPEL, TINTA, VINO, ORO, GRIS = '#FAF5EA', '#2B211C', '#7B1F2B', '#B99448', '#6B6258'
CREMA, FONDO = '#F3E9D6', '#2A1A1C'

FONTS = ('<link href="https://fonts.googleapis.com/css2?'
         'family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,600;1,700'
         '&family=Great+Vibes'
         '&family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">')

BASE = f"""<style>
*{{margin:0;padding:0;box-sizing:border-box;font-family:Inter,sans-serif}}
body{{width:{W}px;height:{H}px;background:{FONDO};display:flex;align-items:center;justify-content:center;overflow:hidden}}
.hoja{{position:relative;width:{W}px;height:{H}px;background:{PAPEL};padding:70px 58px 128px;
 box-shadow:0 40px 90px rgba(0,0,0,.5);display:flex;flex-direction:column;justify-content:space-between}}
.hoja:before{{content:"";position:absolute;inset:26px;border:2px solid {ORO};opacity:.55;pointer-events:none}}
.hoja:after{{content:"";position:absolute;inset:34px;border:1px solid {ORO};opacity:.35;pointer-events:none}}
h1{{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:78px;color:{TINTA};
 text-align:center;letter-spacing:1px;line-height:1}}
h1 .hr{{color:{VINO}}}
.scr{{font-family:'Great Vibes',cursive;font-size:62px;color:{VINO};text-align:center;margin-top:2px;line-height:1}}
.kick{{font-size:23px;letter-spacing:5px;font-weight:800;color:{VINO};text-align:center}}
.rule{{height:2px;background:{ORO};opacity:.5;margin:22px 0}}
.pill{{display:inline-block;background:{VINO};color:#fff;font-weight:800;font-size:21px;
 letter-spacing:3px;padding:9px 22px;border-radius:20px}}
.box{{border:1.5px solid rgba(185,148,72,.65);background:{CREMA};padding:26px 28px;border-radius:8px}}
.lbl{{font-weight:900;font-size:24px;letter-spacing:3px;color:{VINO}}}
.tx{{font-family:'Cormorant Garamond',serif;font-size:35px;line-height:1.35;color:{TINTA}}}
.sm{{font-size:26px;line-height:1.45;color:{GRIS};font-weight:500}}
.pie{{position:absolute;left:0;right:0;bottom:0;background:{VINO};color:#F7E9CE;text-align:center;
 font-family:'Cormorant Garamond',serif;font-size:27px;letter-spacing:2px;padding:16px 0}}
.grid{{display:grid;gap:14px}}
.card{{background:#fff;border:1.5px solid rgba(185,148,72,.7);border-radius:10px;padding:22px 18px;
 font-family:'Cormorant Garamond',serif;font-size:30px;line-height:1.25;color:{TINTA};text-align:center}}
.num{{display:inline-flex;align-items:center;justify-content:center;width:38px;height:38px;border-radius:50%;
 background:{VINO};color:#fff;font-weight:800;font-size:20px;margin-bottom:8px}}
.row{{display:flex;align-items:center;gap:16px;border-bottom:1px dashed rgba(185,148,72,.6);padding:16px 2px}}
.row:last-child{{border-bottom:0}}
.chip{{background:{CREMA};border:1px solid rgba(185,148,72,.7);border-radius:16px;padding:5px 14px;
 font-size:19px;font-weight:700;color:{VINO};white-space:nowrap}}
.flex{{flex:1}}
</style>"""


def pagina(cuerpo, pie=None):
    p = f'<div class="pie">{pie}</div>' if pie else ''
    return f'<!doctype html><html><head><meta charset="utf-8">{FONTS}{BASE}</head><body>' \
           f'<div class="hoja">{cuerpo}{p}</div></body></html>'


def head(kick, titulo, script=None, sub=None):
    s = f'<div class="scr">{script}</div>' if script else ''
    u = f'<div class="sm" style="text-align:center;margin-top:10px">{sub}</div>' if sub else ''
    return f'<div class="kick">{kick}</div><h1>{titulo}</h1>{s}{u}<div class="rule"></div>'


# ------------------------------------------------------------------ 1) cartas de la gratitud
CART1 = head('&#9829; JUEGO DE CARTAS #1', 'Cartas de la <span class="hr">Gratitud</span>',
             'para agradecer de a dos') + """
<div class="box" style="margin-bottom:22px">
  <div class="lbl">OBJETIVO</div>
  <div class="tx" style="margin-top:8px">Reconocer juntos las bendiciones de este a&ntilde;o y volver a
  nombrar en voz alta lo que ya tienen.</div>
</div>
<div class="lbl" style="text-align:center;margin-bottom:14px">EJEMPLOS DE CARTAS</div>
<div class="grid" style="grid-template-columns:1fr 1fr 1fr">
  <div class="card"><div class="num">1</div><br>Deci tres cosas por las que hoy agradec&eacute;s a tu pareja.</div>
  <div class="card"><div class="num">2</div><br>Contale una oraci&oacute;n que Dios te respondi&oacute; este a&ntilde;o.</div>
  <div class="card"><div class="num">3</div><br>&iquest;Cu&aacute;l fue la bendici&oacute;n m&aacute;s grande que vivieron juntos?</div>
  <div class="card"><div class="num">4</div><br>Complet&aacute;: &laquo;Hoy le agradezco a Dios por vos porque...&raquo;</div>
  <div class="card"><div class="num">5</div><br>&iquest;Qu&eacute; momento dif&iacute;cil fortaleci&oacute; m&aacute;s la fe de los dos?</div>
  <div class="card"><div class="num">6</div><br>Nombr&aacute; algo chiquito de la rutina que te hace feliz.</div>
</div>
<div class="box" style="margin-top:24px">
  <div class="lbl">C&Oacute;MO JUGAR</div>
  <div class="sm" style="margin-top:8px">Mezclen las cartas y d&eacute;jenlas boca abajo &middot; cada uno saca una por turno &middot;
  se lee en voz alta y el otro escucha sin interrumpir &middot; cierran con una oraci&oacute;n corta de gracias.</div>
</div>
"""

# ------------------------------------------------------------------ 2) pregúntale a tu pareja
CART2 = head('&#9829; CARTAS', '&laquo;Pregunt&aacute;le a tu pareja&raquo;', None,
             'NIVEL 1 &mdash; CONOCERNOS DE NUEVO &middot; 10 CARTAS') + """
<div class="grid" style="grid-template-columns:1fr 1fr;margin-top:4px">
  <div class="card"><div class="num">1</div><br>&iquest;Qu&eacute; te hizo saber que yo era la persona?</div>
  <div class="card"><div class="num">2</div><br>&iquest;Cu&aacute;l es tu recuerdo favorito de nosotros dos?</div>
  <div class="card"><div class="num">3</div><br>&iquest;Qu&eacute; hago yo que te hace sentir cuidado?</div>
  <div class="card"><div class="num">4</div><br>&iquest;En qu&eacute; &aacute;rea de la casa sent&iacute;s que somos un equipo?</div>
  <div class="card"><div class="num">5</div><br>&iquest;Qu&eacute; costumbre nuestra te gustar&iacute;a no perder nunca?</div>
  <div class="card"><div class="num">6</div><br>Si pudi&eacute;ramos repetir un d&iacute;a juntos, &iquest;cu&aacute;l eleg&iacute;s?</div>
  <div class="card"><div class="num">7</div><br>&iquest;Qu&eacute; me ves hacer que te da orgullo y nunca te digo?</div>
  <div class="card"><div class="num">8</div><br>&iquest;Qu&eacute; regalo m&iacute;o te marc&oacute; m&aacute;s y por qu&eacute;?</div>
  <div class="card"><div class="num">9</div><br>&iquest;Qu&eacute; momento de nuestro matrimonio te acerc&oacute; m&aacute;s a Dios?</div>
  <div class="card"><div class="num">10</div><br>&iquest;Qu&eacute; es lo que m&aacute;s esperanza te da del a&ntilde;o que viene?</div>
</div>
<div class="box" style="margin-top:22px">
  <div class="lbl">AL FINAL</div>
  <div class="sm" style="margin-top:8px">No hagan ninguna correcci&oacute;n. Solo escuchar, agradecer y orar juntos por
  lo que acaban de escuchar.</div>
</div>
"""

# ------------------------------------------------------------------ 3) devocional
DEVO = head('&#9829; DEVOCIONAL 1', 'Dios en el centro<br>del matrimonio') + """
<div class="box" style="margin-bottom:20px">
  <div class="lbl">VERS&Iacute;CULO</div>
  <div class="tx" style="margin-top:10px;font-style:italic">&laquo;Si el Se&ntilde;or no edifica la casa, en vano
  trabajan los que la edifican.&raquo;</div>
  <div class="sm" style="margin-top:8px;color:#7B1F2B;font-weight:700">Salmos 127:1</div>
</div>
<div class="box" style="margin-bottom:20px">
  <div class="lbl">REFLEXI&Oacute;N</div>
  <div class="tx" style="margin-top:10px">Todo matrimonio se construye sobre algo. Muchas parejas apoyan la
  relaci&oacute;n solo en lo que sienten; otras, en la estabilidad del sueldo o en los hijos. Son cosas buenas,
  pero ninguna aguanta sola las temporadas duras.<br><br>
  Poner a Dios en el centro no significa hacer m&aacute;s cosas de la iglesia: significa buscarlo a &Eacute;l antes
  que a la soluci&oacute;n, y que los dos caminen para el mismo lado.</div>
</div>
<div class="box" style="margin-bottom:20px">
  <div class="lbl">APLIC&Aacute;NDOLO ESTA SEMANA</div>
  <div class="sm" style="margin-top:10px">&bull; &iquest;En qu&eacute; parte de la casa se nota m&aacute;s que Dios est&aacute; en el centro?<br>
  &bull; &iquest;Hay algo que todav&iacute;a no le entregamos?<br>
  &bull; &iquest;C&oacute;mo podemos buscarlo juntos esta semana, sin que sea una obligaci&oacute;n?</div>
</div>
<div class="grid" style="grid-template-columns:1fr 1fr">
  <div class="box"><div class="lbl">ORACI&Oacute;N</div>
    <div class="sm" style="margin-top:8px">Se&ntilde;or, queremos que seas el centro de esta casa y no la visita de
    los domingos. Ense&ntilde;anos a buscarte juntos.</div></div>
  <div class="box"><div class="lbl">DESAF&Iacute;O</div>
    <div class="sm" style="margin-top:8px">Diez minutos por d&iacute;a, tres d&iacute;as seguidos: la misma lectura, los dos,
    sin el celular en la mano.</div></div>
</div>
"""

# ------------------------------------------------------------------ 4) oraciones guiadas
ORAC = head('&#9829; ORACIONES', 'Guiadas', None,
            'GRATITUD POR NUESTRO MATRIMONIO') + """
<div class="box" style="margin-bottom:22px">
  <div class="lbl">VERS&Iacute;CULO</div>
  <div class="tx" style="margin-top:10px;font-style:italic">&laquo;Den gracias en todo, porque esta es la voluntad
  de Dios para ustedes.&raquo;</div>
  <div class="sm" style="margin-top:8px;color:#7B1F2B;font-weight:700">1 Tesalonicenses 5:18</div>
</div>
<div class="box">
  <div class="lbl">ORACI&Oacute;N</div>
  <div class="tx" style="margin-top:12px">Se&ntilde;or, hoy queremos empezar este momento agradeciendo por todo lo
  que nos diste y por lo que todav&iacute;a estamos esperando.<br><br>
  Gracias por el d&iacute;a en que nuestros caminos se cruzaron y por cada etapa que vivimos hasta ac&aacute;.<br><br>
  Gracias por lo que nos ense&ntilde;aste cuando no entend&iacute;amos nada, y porque nunca nos soltaste la mano.<br><br>
  Perdonanos las veces que nos hablamos sin mirarnos. Ayudanos a no perder nunca la costumbre de agradecer en voz
  alta lo que el otro hace todos los d&iacute;as y nadie ve.<br><br>
  Que podamos cuidar este matrimonio con respeto y paciencia, en todas las circunstancias.<br><br>
  En el nombre de Jes&uacute;s, am&eacute;n.</div>
</div>
<div class="sm" style="text-align:center;margin-top:22px">Reserven unos minutos juntos, en un lugar tranquilo,
y entreguen a Dios su matrimonio y el a&ntilde;o que viene.</div>
"""

# ------------------------------------------------------------------ 5) desafíos de conexión
DESA = head('&#9829; DESAF&Iacute;OS', 'de Conexi&oacute;n', None,
            'UNA MISI&Oacute;N POR NOCHE &middot; SIN SALIR DE CASA') + """
<div class="box" style="padding:10px 20px">
  <div class="row"><span class="pill">01</span>
    <div class="flex"><div class="tx" style="font-weight:600">Carta de amor</div>
      <div class="sm">Escrib&iacute; a mano algo que nunca le dijiste. Se lee en voz alta, sin aclaraciones.</div></div>
    <span class="chip">20 min</span></div>
  <div class="row"><span class="pill">02</span>
    <div class="flex"><div class="tx" style="font-weight:600">Te admiro por esto</div>
      <div class="sm">Diez cosas que admir&aacute;s del otro. Despu&eacute;s cambian las hojas y las guardan.</div></div>
    <span class="chip">25 min</span></div>
  <div class="row"><span class="pill">03</span>
    <div class="flex"><div class="tx" style="font-weight:600">Gracias por ense&ntilde;arme</div>
      <div class="sm">Lo que aprendiste de &eacute;l o de ella y hoy us&aacute;s sin darte cuenta.</div></div>
    <span class="chip">20 min</span></div>
  <div class="row"><span class="pill">04</span>
    <div class="flex"><div class="tx" style="font-weight:600">La noche sin pantallas</div>
      <div class="sm">Celulares en un caj&oacute;n, una vela y las cartas de preguntas arriba de la mesa.</div></div>
    <span class="chip">40 min</span></div>
  <div class="row"><span class="pill">05</span>
    <div class="flex"><div class="tx" style="font-weight:600">Oramos por el otro</div>
      <div class="sm">Cada uno ora en voz alta por el sue&ntilde;o del otro, no por el propio.</div></div>
    <span class="chip">15 min</span></div>
</div>
<div class="box" style="margin-top:22px">
  <div class="lbl">C&Oacute;MO USAR</div>
  <div class="sm" style="margin-top:8px">Una misi&oacute;n por encuentro, en orden. Si una noche no llegan, la retoman
  la semana que viene: el orden importa m&aacute;s que la velocidad.</div>
</div>
"""

# ------------------------------------------------------------------ 6) bingo
CAS = ['Or&oacute; por vos sin que se lo pidieras', 'Te hizo re&iacute;r esta semana', 'Cocin&oacute; algo que te gusta',
       'Te mand&oacute; un vers&iacute;culo', 'Guard&oacute; el celular para escucharte',
       'Te agradeci&oacute; algo en voz alta', 'Puso la mesa sin que le digas', 'Te abraz&oacute; de la nada',
       'Dijo &laquo;perd&oacute;n&raquo; primero', 'Te acompa&ntilde;&oacute; a la iglesia', 'Te defendi&oacute; delante de otro',
       'Te despert&oacute; con mate', 'Se acord&oacute; de algo que contaste', 'Te eligi&oacute; una canci&oacute;n',
       'Hizo algo de la casa sin quejarse', 'Te escuch&oacute; sin dar consejos', 'Te dijo que est&aacute; orgulloso',
       'Apag&oacute; la tele para hablar', 'Te mand&oacute; un audio largo', 'Rez&oacute; con vos antes de dormir',
       'Te dej&oacute; dormir m&aacute;s', 'Se banc&oacute; un mal d&iacute;a tuyo', 'Te hizo un regalo chiquito',
       'Te mir&oacute; como el primer d&iacute;a', 'Dijo &laquo;gracias, Se&ntilde;or&raquo; en voz alta']
CELDAS = ''.join(f'<div class="card" style="font-size:23px;padding:14px 9px;line-height:1.18">{c}</div>' for c in CAS)
BINGO = head('&#9829; BINGO', 'Cristiano de Pareja', None,
             'MARC&Aacute; LO QUE PAS&Oacute; ESTA SEMANA') + f"""
<div class="grid" style="grid-template-columns:repeat(5,1fr);gap:10px">{CELDAS}</div>
<div class="box" style="margin-top:22px">
  <div class="lbl">C&Oacute;MO JUGAR</div>
  <div class="sm" style="margin-top:8px">Cada uno con su cart&oacute;n. Se marca solo lo que hizo el otro, nunca lo
  propio. El primero que completa una l&iacute;nea elige el pr&oacute;ximo encuentro de la semana.</div>
</div>
"""

# ------------------------------------------------------------------ 7) verdad o desafío
VERD = head('&#9829; VERDAD O DESAF&Iacute;O &#9829;', 'Cristiano', None,
            '30 CARTAS DE VERDAD &middot; 30 DE DESAF&Iacute;O') + """
<div class="grid" style="grid-template-columns:1fr 1fr">
  <div class="box">
    <div class="lbl">VERDAD</div>
    <div class="sm" style="margin-top:10px;line-height:1.55">
    &bull; &iquest;Qu&eacute; es lo que m&aacute;s te cuesta pedirme?<br>
    &bull; &iquest;Hay algo que callaste esta semana?<br>
    &bull; &iquest;Cu&aacute;ndo fue la &uacute;ltima vez que te sentiste solo en esto?<br>
    &bull; &iquest;Qu&eacute; parte de m&iacute; te saca una sonrisa cuando nadie ve?<br>
    &bull; &iquest;En qu&eacute; sent&iacute;s que nos distanciamos sin darnos cuenta?<br>
    &bull; &iquest;Qu&eacute; te gustar&iacute;a que te pregunte m&aacute;s seguido?</div>
  </div>
  <div class="box">
    <div class="lbl">DESAF&Iacute;O</div>
    <div class="sm" style="margin-top:10px;line-height:1.55">
    &bull; Deci tres cosas que admir&aacute;s del otro, mir&aacute;ndolo a los ojos.<br>
    &bull; Or&aacute; en voz alta por su trabajo.<br>
    &bull; Mand&aacute;le ahora un mensaje que no espera.<br>
    &bull; Elegi un vers&iacute;culo para &eacute;l o para ella y expl&iacute;cale por qu&eacute;.<br>
    &bull; Pedile perd&oacute;n por algo chiquito que nunca nombraste.<br>
    &bull; Agendemos la pr&oacute;xima noche antes de levantarnos de la mesa.</div>
  </div>
</div>
<div class="box" style="margin-top:22px">
  <div class="lbl">C&Oacute;MO JUGAR</div>
  <div class="sm" style="margin-top:8px">Diez rondas. El que elige &laquo;verdad&raquo; responde sin bromear; el que elige
  &laquo;desaf&iacute;o&raquo; lo hace en el momento. Nada de lo que se diga ac&aacute; se usa despu&eacute;s en una discusi&oacute;n.</div>
</div>
<div class="sm" style="text-align:center;margin-top:20px">Cierran siempre con una oraci&oacute;n corta, tomados de la mano.</div>
"""

PAGS = {'cartas1': (CART1, 'CONVERSAR EDIFICA &middot; EL AMOR CRECE &middot; DIOS EN EL CENTRO'),
        'cartas2': (CART2, 'ESCUCHAR SIN CORREGIR ES LA MITAD DEL TRABAJO'),
        'devocional': (DEVO, 'CUANDO DIOS EST&Aacute; EN EL CENTRO, EL AMOR PERMANECE'),
        'oraciones': (ORAC, 'DOS EN CRISTO, UN SOLO PROP&Oacute;SITO'),
        'desafios': (DESA, 'UNA MISI&Oacute;N POR NOCHE, Y LA SEMANA CAMBIA'),
        'bingo': (BINGO, 'LO QUE SE AGRADECE, SE REPITE'),
        'verdad': (VERD, 'DOS EN CRISTO, UN SOLO PROP&Oacute;SITO')}


def render(nombre, html):
    tmp = os.path.join(OUT, '_' + nombre + '.html')
    png = os.path.join(OUT, '_' + nombre + '.png')
    open(tmp, 'w', encoding='utf-8').write(html)
    subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--hide-scrollbars',
                    f'--window-size={W},{H}', '--virtual-time-budget=6000',
                    f'--screenshot={png}', 'file://' + tmp], check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    im = Image.open(png).convert('RGB').resize((W, H), Image.LANCZOS)
    lienzo = im.resize((MW, MH), Image.LANCZOS).filter(ImageFilter.GaussianBlur(26))
    lienzo.paste(im, ((MW - W) // 2, (MH - H) // 2))
    final = os.path.join(OUT, nombre + '.png')
    lienzo.save(final)
    os.remove(tmp); os.remove(png)
    print('ok', nombre, lienzo.size)


if __name__ == '__main__':
    for nombre, (cuerpo, pie) in PAGS.items():
        render(nombre, pagina(cuerpo, pie))
