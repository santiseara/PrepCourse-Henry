# -*- coding: utf-8 -*-
"""Planilla Maestra: la hoja de calculo dibujada por codigo (HTML + Chrome headless).

El ganador que se clona (The Sheet Code, ~57 ads en ingles) tiene la planilla llenandose en vivo
durante el 80% de la pantalla: bloques pastel tipo Google Sheets, celda activa con borde azul y
zoom a cada seccion. Aca se dibuja lo mismo con la oferta propia (21 hojas, LATAM), en estados
sucesivos: el mismo bloque vacio, a medio cargar y completo. El editor los encadena con cortes
cortos y da la sensacion de grabacion de pantalla.

Sin simbolo de moneda en ninguna celda: la tanda sale a varios paises (regla del 8/11).

Uso: python3 gfx_planilla.py
"""
import os, subprocess
from PIL import Image, ImageFilter

OUT = os.path.expanduser('~/Desktop/cuentas-claras/anuncios/work/sheet')
os.makedirs(OUT, exist_ok=True)
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
W, H = 1080, 1920
MW, MH = 1296, 2304            # 1.20x, margen para el zoom del editor

VERDE, LILA, CELESTE, AMAR, ROSA, GRIS = '#D9EAD3', '#D9D2E9', '#CFE2F3', '#FFF2CC', '#F4CCCC', '#EFEFEF'

CSS = """<style>
*{margin:0;padding:0;box-sizing:border-box;font-family:Arial,Helvetica,sans-serif}
body{width:1080px;height:1920px;background:#fff;overflow:hidden}
.bar{height:46px;display:flex;align-items:center;gap:14px;padding:0 18px;border-bottom:1px solid #e3e3e3}
.doc{font-size:22px;color:#202124}
.menus{display:flex;gap:18px;font-size:18px;color:#5f6368;margin-left:2px}
.tool{height:54px;display:flex;align-items:center;gap:22px;padding:0 20px;border-bottom:1px solid #e3e3e3;
 font-size:20px;color:#444}
.tool b{font-weight:700}
.fx{height:46px;display:flex;align-items:center;gap:16px;padding:0 14px;border-bottom:1px solid #e3e3e3;
 font-size:19px;color:#555}
.fx .cell{border:1px solid #ddd;border-radius:3px;padding:3px 16px;min-width:90px;text-align:center;color:#222}
.cols{display:flex;height:34px;background:#f8f9fa;border-bottom:1px solid #e3e3e3;font-size:17px;color:#5f6368}
.cols div{display:flex;align-items:center;justify-content:center;border-right:1px solid #e3e3e3}
.cols .rn{width:56px}
.cols .c{flex:1}
.cols .on{background:#d3e3fd;color:#1967d2;font-weight:700}
.grid{position:relative;height:1740px;background:
 repeating-linear-gradient(#fff 0 47px,#e8eaed 47px 48px),
 repeating-linear-gradient(90deg,#fff 0 127px,#e8eaed 127px 128px)}
.rows{position:absolute;left:0;top:0;width:56px;height:100%;background:#f8f9fa;border-right:1px solid #e3e3e3;
 font-size:17px;color:#5f6368}
.rows i{display:flex;align-items:center;justify-content:center;height:48px;font-style:normal;
 border-bottom:1px solid #e8eaed}
.wrap{position:absolute;left:56px;right:0;top:0;bottom:0;padding:0 26px;display:flex;flex-direction:column;justify-content:center}
.blk{margin:0 0 26px;border:1px solid #d7d7d7;background:#fff;box-shadow:0 1px 0 #00000008}
.blk:last-child{margin-bottom:0}
.blk h3{font-size:30px;letter-spacing:2px;font-weight:700;color:#3c4043;padding:14px 18px;text-align:center}
table{width:100%;border-collapse:collapse}
td,th{font-size:26px;padding:11px 16px;border-top:1px solid #e3e3e3;color:#3c4043}
th{font-size:20px;letter-spacing:1px;color:#80868b;text-align:left;font-weight:700;background:#fafafa}
td.n{text-align:right;font-variant-numeric:tabular-nums}
tr.tot td{font-weight:700;background:#fafafa;font-size:27px}
td.dim{color:#bdc1c6}
.sel{outline:3px solid #1a73e8;outline-offset:-3px;position:relative;background:#e8f0fe}
.sel:after{content:"";position:absolute;right:-5px;bottom:-5px;width:9px;height:9px;background:#1a73e8;
 border:1px solid #fff}
.flag{color:#d93025;font-weight:700}
.ok{color:#188038;font-weight:700}
.barcat{display:flex;align-items:center;gap:14px;padding:10px 16px;border-top:1px solid #e3e3e3}
.barcat span{font-size:25px;color:#3c4043;width:230px}
.barcat .t{flex:1;height:26px;background:#eee;border-radius:3px;overflow:hidden}
.barcat .t i{display:block;height:100%}
.barcat em{font-style:normal;font-size:25px;width:90px;text-align:right;font-variant-numeric:tabular-nums}
.cur{position:absolute;width:30px;height:42px;filter:drop-shadow(0 2px 3px rgba(0,0,0,.35))}
.note{font-size:23px;color:#5f6368;padding:12px 18px;border-top:1px solid #e3e3e3;background:#fafafa}
</style>"""

MENUS = ('<div class="bar"><div class="doc">Planilla Maestra 2026</div>'
         '<div class="menus"><span>Archivo</span><span>Editar</span><span>Ver</span><span>Insertar</span>'
         '<span>Formato</span><span>Datos</span><span>Herramientas</span><span>Ayuda</span></div></div>'
         '<div class="tool"><span>100%</span><span>|</span><span><b>B</b></span><span><i>I</i></span>'
         '<span>A</span><span>|</span><span>123</span><span>Arial</span><span>|</span><span>&#8721;</span>'
         '<span>&#9636;</span><span>&#9205;</span></div>')


def marco(cell, valor, cols_on, bloques, rows_from=1):
    cols = '<div class="cols"><div class="rn"></div>'
    for c in 'ABCDEFG':
        cols += '<div class="c%s">%s</div>' % (' on' if c == cols_on else '', c)
    cols += '</div>'
    rows = ''.join('<i>%d</i>' % n for n in range(rows_from, rows_from + 37))
    fx = ('<div class="fx"><div class="cell">%s</div><span>fx</span><span>%s</span></div>'
          % (cell, valor))
    return (CSS + MENUS + fx + cols +
            '<div class="grid"><div class="rows">' + rows + '</div>'
            '<div class="wrap">' + bloques + '</div>'
            '<svg class="cur" style="left:702px;top:1012px" viewBox="0 0 24 34">'
            '<path d="M2 2 L2 26 L8.5 20 L12.5 30 L16.5 28 L12.5 18.5 L21 18 Z" fill="#111" '
            'stroke="#fff" stroke-width="1.6"/></svg>'
            '</div>')


def tabla(titulo, color, cabeceras, filas, nota=''):
    th = ''.join('<th>%s</th>' % c for c in cabeceras)
    tr = ''
    for f in filas:
        cls = ' class="tot"' if f[0] == '__TOT__' else ''
        celdas = f[1:] if f[0] == '__TOT__' else f
        tds = ''
        for i, c in enumerate(celdas):
            klass = []
            if i:
                klass.append('n')
            if c == '':
                klass.append('dim')
            txt = c
            if isinstance(c, tuple):
                txt, extra = c
                klass.append(extra)
            tds += '<td class="%s">%s</td>' % (' '.join(klass), txt)
        tr += '<tr%s>%s</tr>' % (cls, tds)
    return ('<div class="blk"><h3 style="background:%s">%s</h3><table><tr>%s</tr>%s</table>%s</div>'
            % (color, titulo, th, tr, ('<div class="note">%s</div>' % nota) if nota else ''))


def barras(titulo, color, datos):
    filas = ''
    for nombre, pct, col in datos:
        filas += ('<div class="barcat"><span>%s</span><div class="t"><i style="width:%d%%;background:%s"></i>'
                  '</div><em>%d%%</em></div>' % (nombre, pct, col, pct))
    return '<div class="blk"><h3 style="background:%s">%s</h3>%s</div>' % (color, titulo, filas)


def shot(html, name):
    p = '%s/_%s.html' % (OUT, name)
    open(p, 'w').write(html)
    subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--hide-scrollbars',
                    '--window-size=%d,%d' % (W, H), '--screenshot=%s/_%s.png' % (OUT, name),
                    '--virtual-time-budget=4000', 'file://' + p], check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    im = Image.open('%s/_%s.png' % (OUT, name)).convert('RGB').resize((W, H), Image.LANCZOS)
    bg = im.resize((MW, MH), Image.LANCZOS).filter(ImageFilter.GaussianBlur(22))
    bg = Image.blend(bg, Image.new('RGB', (MW, MH), (250, 250, 250)), 0.45)
    bg.paste(im, ((MW - W) // 2, (MH - H) // 2))
    bg.save('%s/%s.png' % (OUT, name))
    os.remove(p); os.remove('%s/_%s.png' % (OUT, name))
    print('%s/%s.png' % (OUT, name))


# ---------------------------------------------------------------- escenas
V = ''   # celda vacia

ING_VACIO = [['Sueldo (1ra quincena)', V, V], ['Sueldo (2da quincena)', V, V], ['Otros ingresos', V, V],
             ['__TOT__', 'TOTAL QUE ENTRA', V, V]]
ING_1 = [['Sueldo (1ra quincena)', '12 nov', ('1.250', 'sel')], ['Sueldo (2da quincena)', '26 nov', V],
         ['Otros ingresos', V, V], ['__TOT__', 'TOTAL QUE ENTRA', '', '1.250']]
ING_2 = [['Sueldo (1ra quincena)', '12 nov', '1.250'], ['Sueldo (2da quincena)', '26 nov', '1.250'],
         ['Otros ingresos', '—', '—'], ['__TOT__', 'TOTAL QUE ENTRA', '', '2.500']]

FIJ_VACIO = [['Alquiler', '5 nov', V], ['Luz', '14 nov', V], ['Internet', '18 nov', V],
             ['Celular', '22 nov', V], ['__TOT__', 'TOTAL FIJOS', '', V]]
FIJ_1 = [['Alquiler', '5 nov', '850'], ['Luz', '14 nov', ('95', 'sel')], ['Internet', '18 nov', V],
         ['Celular', '22 nov', V], ['__TOT__', 'TOTAL FIJOS', '', '945']]
FIJ_2 = [['Alquiler', '5 nov', '850'], ['Luz', '14 nov', '95'], ['Internet', '18 nov', '60'],
         ['Celular', '22 nov', '45'], ['__TOT__', 'TOTAL FIJOS', '', '1.050']]

SUS = [['Streaming de series', '15 nov', '12'], [('Gimnasio · sin usar', 'flag'), '9 nov', ('15', 'flag')],
       ['Música', '3 nov', '9'], [('Nube de fotos · sin usar', 'flag'), '21 nov', ('7', 'flag')],
       [('App de edición · sin usar', 'flag'), '27 nov', ('10', 'flag')],
       ['__TOT__', 'TOTAL SUSCRIPCIONES', '', '53']]

VAR_1 = [['Supermercado', 'Necesidad', '420'], ['Transporte', 'Necesidad', ('110', 'sel')],
         ['Comida pedida', 'Gusto', V], ['Ropa', 'Gusto', V], ['__TOT__', 'TOTAL VARIABLES', '', '530']]
VAR_2 = [['Supermercado', 'Necesidad', '420'], ['Transporte', 'Necesidad', '110'],
         ['Comida pedida', 'Gusto', '95'], ['Ropa', 'Gusto', '120'],
         ['__TOT__', 'TOTAL VARIABLES', '', '745']]

RES = [['Entró en el mes', '', '2.500'], ['Salió en el mes', '', '1.848'],
       ['__TOT__', 'TE QUEDÓ LIBRE', '', '652']]

DIST = [('Necesidades', 58, '#6aa84f'), ('Gustos', 16, '#e69138'), ('Ahorro y deudas', 26, '#3d85c6')]

G3_ING = [['Sueldo de ella', '10 nov', '1.600'], ['Sueldo de él', '5 nov', '1.350'],
          ['Trabajo extra', '—', '250'], ['__TOT__', 'TOTAL QUE ENTRA', '', '3.200']]
G3_FIJ = [['Alquiler', '5 nov', '980'], ['Cuota del auto', '12 nov', '290'],
          ['Seguros', '16 nov', '120'], ['Celulares', '22 nov', '70'],
          ['__TOT__', 'TOTAL FIJOS', '', '1.460']]
G3_SUS = [['Streaming', '15 nov', '14'], [('Gimnasio de los dos · sin usar', 'flag'), '9 nov', ('28', 'flag')],
          ['Música', '3 nov', '12'], ['Nube', '21 nov', '10'], ['__TOT__', 'TOTAL SUSCRIPCIONES', '', '64']]
G3_VAR = [['Supermercado', 'Necesidad', '560'], ['Transporte', 'Necesidad', '180'],
          ['Salidas', 'Gusto', '150'], ['Ropa', 'Gusto', '130'], ['__TOT__', 'TOTAL VARIABLES', '', '1.020']]
G3_DEU = [['Tarjeta 1', '72% anual', '180'], ['Tarjeta 2', '58% anual', '120'],
          ['Préstamo', '45% anual', '210'], ['__TOT__', 'PAGO MENSUAL', '', '510']]
G3_LIB = [['Entró', '', '3.200'], ['Fijos, suscripciones y variables', '', '2.544'],
          ['Deudas', '', '510'], ['__TOT__', 'LIBRE PARA ASIGNAR AL AHORRO', '', ('146', 'ok')]]
G3_PLAN = [['Deuda total', '', '8.400'], ['Pago mensual', '', '510'],
           ['Extra del ahorro', '', '146'], ['Meses que faltan', '', '13'],
           ['__TOT__', 'LIBRES DE DEUDA EN', '', ('diciembre 2027', 'ok')]]

G5_PAT = [['Cuenta de sueldo', '', '1.240'], ['Ahorros', '', '3.800'], ['Efectivo', '', '160'],
          ['Tarjetas', '', '-1.430'], ['Préstamo', '', '-2.600'],
          ['__TOT__', 'PATRIMONIO NETO', '', '1.170']]
G5_CAT = [['Supermercado', 'Necesidad', '420'], ['Transporte', 'Necesidad', '110'],
          ['Comida pedida', 'Gusto', '95'], ['Ropa', 'Gusto', '120'],
          ['Fondo de emergencia', 'Ahorro', '200'], ['__TOT__', 'SE CALCULA SOLO', '', '945']]
G5_MET = [('El viaje', 45, '#3d85c6'), ('Fondo de emergencia', 28, '#6aa84f'),
          ('Salir de la tarjeta', 62, '#e69138')]

CAB3 = ['CONCEPTO', 'FECHA', 'MONTO']
CAB3C = ['CONCEPTO', 'CATEGORÍA', 'MONTO']
CAB2 = ['CONCEPTO', '', 'MONTO']

MES = ('<div class="blk"><h3 style="background:%s">TABLERO MENSUAL</h3>'
       '<table><tr><th>MES</th><th>ESTADO</th><th>CARGADO</th></tr>'
       '<tr><td class="sel">Noviembre 2026</td><td class="n">En curso</td><td class="n">—</td></tr>'
       '<tr><td>Octubre 2026</td><td class="n">Cerrado</td><td class="n">100%%</td></tr>'
       '<tr><td>Septiembre 2026</td><td class="n">Cerrado</td><td class="n">100%%</td></tr></table>'
       '<div class="note">Elegí el mes y la planilla arma el tablero sola.</div></div>') % CELESTE if False else None

ESCENAS = [
    # --- Guion 1: dia de pago
    ('g1_mes', 'B4', 'Noviembre 2026', 'B',
     tabla('TABLERO MENSUAL', CELESTE, ['MES', 'ESTADO', 'CARGADO'],
           [[('Noviembre 2026', 'sel'), 'En curso', '—'], ['Octubre 2026', 'Cerrado', '100%'],
            ['Septiembre 2026', 'Cerrado', '100%']],
           'Elegís el mes y el tablero se arma solo.')),
    ('g1_ing0', 'D6', '', 'D', tabla('INGRESOS DEL MES', VERDE, CAB3, ING_VACIO)),
    ('g1_ing1', 'D6', '1250', 'D', tabla('INGRESOS DEL MES', VERDE, CAB3, ING_1)),
    ('g1_ing2', 'D7', '1250', 'D', tabla('INGRESOS DEL MES', VERDE, CAB3, ING_2)),
    ('g1_fij0', 'D12', '', 'D', tabla('GASTOS FIJOS', LILA, CAB3, FIJ_VACIO)),
    ('g1_fij1', 'D13', '95', 'D', tabla('GASTOS FIJOS', LILA, CAB3, FIJ_1)),
    ('g1_fij2', 'D15', '=SUMA(D12:D15)', 'D', tabla('GASTOS FIJOS', LILA, CAB3, FIJ_2)),
    ('g1_sus', 'B20', 'Gimnasio', 'B',
     tabla('SUSCRIPCIONES', CELESTE, CAB3, SUS, 'Tres que se cobraban todos los meses sin usarse.')),
    ('g1_var1', 'D26', '110', 'D', tabla('GASTOS VARIABLES', AMAR, CAB3C, VAR_1)),
    ('g1_var2', 'D29', '=SUMA(D26:D29)', 'D', tabla('GASTOS VARIABLES', AMAR, CAB3C, VAR_2)),
    ('g1_dist', 'F8', '=D26/D$6', 'F', barras('NECESIDADES · GUSTOS · AHORRO', VERDE, DIST)),
    ('g1_res', 'D34', '=D6-D31', 'D', tabla('RESUMEN DEL MES', VERDE, CAB2, RES)),
    # --- Guion 3: la pareja
    ('g3_ing', 'D6', '1600', 'D', tabla('INGRESOS DE LOS DOS', VERDE, CAB3, G3_ING)),
    ('g3_fij', 'D12', '980', 'D', tabla('GASTOS FIJOS', LILA, CAB3, G3_FIJ)),
    ('g3_sus', 'B18', 'Gimnasio', 'B', tabla('SUSCRIPCIONES', CELESTE, CAB3, G3_SUS)),
    ('g3_var', 'D24', '560', 'D', tabla('GASTOS VARIABLES', AMAR, CAB3C, G3_VAR)),
    ('g3_deu', 'C30', '72%', 'C', tabla('DEUDAS Y PRÉSTAMOS', ROSA, ['CONCEPTO', 'TASA', 'CUOTA'], G3_DEU)),
    ('g3_lib', 'D36', '=D6-D31-D34', 'D', tabla('LO QUE QUEDA', VERDE, CAB2, G3_LIB)),
    ('g3_dist', 'F8', '=D24/D$6', 'F', barras('NECESIDADES · GUSTOS · AHORRO', VERDE, DIST)),
    ('g3_plan', 'D40', '=FECHA.SALIDA', 'D',
     tabla('PLAN DE SALIDA DE DEUDAS', ROSA, CAB2, G3_PLAN, 'Trece meses, no los cinco años que imaginaban.')),
    # --- Guion 5: anotar no es presupuestar
    ('g5_pat', 'D10', '=SUMA(D4:D9)', 'D',
     tabla('SALDOS Y PATRIMONIO NETO', LILA, CAB2, G5_PAT, 'Cuentas, efectivo, tarjetas y deudas en un solo número.')),
    ('g5_cat', 'C14', '=BUSCARV(B14;Categorías!A:B;2)', 'C',
     tabla('CATEGORÍAS AUTOMÁTICAS', AMAR, CAB3C, G5_CAT)),
    ('g5_met', 'E20', '=D20/C20', 'E', barras('AHORRO POR OBJETIVOS', CELESTE, G5_MET)),
    ('g5_res', 'D34', '=D6-D31', 'D', tabla('RESUMEN DEL MES', VERDE, CAB2, RES)),
]

if __name__ == '__main__':
    for name, cell, valor, col, bloque in ESCENAS:
        shot(marco(cell, valor, col, bloque), name)
