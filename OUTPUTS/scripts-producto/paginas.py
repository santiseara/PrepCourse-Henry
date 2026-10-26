# -*- coding: utf-8 -*-
"""Las cuatro hojas de cada plano."""
from engine import *

ML, MR = 42.0, 42.0
ANCHO = A4W - ML - MR
HOJAS = ['El trabajo', 'El dibujo', 'La lista de cortes', 'El armado']

# ----------------------------------------------------------------- cabecera y pie
def encabezado(c, pl, hoja):
    c.setFillColor(TINTA); c.rect(0, A4H-52, A4W, 52, stroke=0, fill=1)
    c.setFillColor(NARANJA); c.rect(0, A4H-55, A4W, 3, stroke=0, fill=1)
    c.setFont('BC', 9); c.setFillColor(NARANJA)
    c.drawString(ML, A4H-24, 'HERRERO DE FINDE')
    c.setFont('BCM', 7.4); c.setFillColor(HexColor('#9AA2AB'))
    c.drawString(ML, A4H-36, CAT_NOM[pl.cat].upper())
    c.setFont('BC', 17); c.setFillColor(PAPEL)
    c.drawRightString(A4W-MR, A4H-28, 'PLANO ' + pl.codigo)
    c.setFont('BCM', 7.4); c.setFillColor(HexColor('#9AA2AB'))
    c.drawRightString(A4W-MR, A4H-40, ('HOJA %d DE 4 · ' % hoja) + HOJAS[hoja-1].upper())

def pie(c, pl, hoja):
    linea(c, ML, 58, A4W-MR, GRIS_CL, 0.5)
    c.setFont('BCM', 7); c.setFillColor(GRIS)
    c.drawString(ML, 47, 'Herrero de Finde · Biblioteca de planos')
    c.drawCentredString(A4W/2, 47, '%s · %s' % (pl.codigo, pl.nombre))
    c.drawRightString(A4W-MR, 47, 'pág. %d' % (pl.pagina + hoja - 1))

def titulo_hoja(c, pl, hoja, y=A4H-78):
    c.setFont('BC', 20); c.setFillColor(TINTA)
    c.drawString(ML, y, pl.nombre.upper())
    c.setFont('BCM', 9.6); c.setFillColor(GRIS)
    sub = pl.variante if pl.variante else CAT_NOM[pl.cat]
    c.drawString(ML, y-13, sub)
    c.setFillColor(NARANJA); c.setFont('BC', 9)
    c.drawRightString(A4W-MR, y, HOJAS[hoja-1].upper())
    return y - 26

def seccion(c, x, y, texto, ancho=None, color=TINTA):
    c.setFont('BC', 9); c.setFillColor(color)
    c.drawString(x, y, texto.upper())
    linea(c, x, y-5.5, x + (ancho or ANCHO), GRIS_CL, 0.6)
    return y - 17

# ----------------------------------------------------------------- hoja 1
def hoja_1(c, pl):
    encabezado(c, pl, 1); pie(c, pl, 1)
    y = titulo_hoja(c, pl, 1)
    W, D, H = pl.medidas()
    c.setFont('BCM', 9); c.setFillColor(TINTA2)
    c.drawRightString(A4W-MR, y+10, 'Medida terminada: %d x %d x %d mm' % (round(W), round(D), round(H)))

    # ---- isometrico
    caja = (ML, 492, ANCHO, 236)
    c.setFillColor(CREMA); c.roundRect(caja[0], caja[1], caja[2], caja[3], 4, stroke=0, fill=1)
    dibujar_iso(c, pl.piezas, (caja[0]+10, caja[1]+14, caja[2]-20, caja[3]-26), pad=4)
    chip(c, caja[0]+10, caja[1]+caja[3]-18, 'ASÍ TERMINA', bg=TINTA, fg=PAPEL)

    # ---- fichas
    y = 466
    datos = [('TIEMPO DE TRABAJO', '%d a %d h' % pl.horas),
             ('NIVEL', pl.nivel),
             ('HIERRO QUE LLEVA', pesos(pl.costo_material())),
             ('LO VENDÉS A', pesos(pl.precio_venta()[0]))]
    w = (ANCHO - 3*6) / 4.0
    for i, (lab, val) in enumerate(datos):
        x = ML + i*(w+6)
        ultimo = (i == 3)
        c.setFillColor(VERDE_CL if ultimo else CREMA)
        c.roundRect(x, y-34, w, 38, 3, stroke=0, fill=1)
        c.setFont('BCM', 6.6); c.setFillColor(VERDE if ultimo else GRIS)
        c.drawString(x+9, y-11, lab)
        c.setFont('BC', 14.5); c.setFillColor(VERDE if ultimo else TINTA)
        c.drawString(x+9, y-28, val)
    y -= 52

    # ---- que es / quien lo compra
    col = (ANCHO - 16) / 2.0
    yy = seccion(c, ML, y, 'Qué es', col)
    parrafo(c, pl.resumen, ML, yy, col, 'B', 8.3, 11.2)
    yy2 = seccion(c, ML+col+16, y, 'Quién te lo compra', col)
    parrafo(c, pl.quien, ML+col+16, yy2, col, 'B', 8.3, 11.2)
    y -= 78

    # ---- compra
    filas, _ = pl.compra()
    y = seccion(c, ML, y, 'Lo que pedís en la casa de hierros')
    c.setFont('BCM', 6.8); c.setFillColor(GRIS)
    c.drawString(ML, y, 'MATERIAL'); c.drawString(ML+300, y, 'PEDÍS'); c.drawString(ML+400, y, 'NETO')
    c.drawRightString(A4W-MR, y, 'PRECIO')
    y -= 4
    linea(c, ML, y, A4W-MR, GRIS_CL, 0.4); y -= 12
    for f in filas:
        c.setFont('B', 8.2); c.setFillColor(TINTA)
        c.drawString(ML, y, M[f['mat']]['nom'])
        c.setFont('BM', 8.2); c.drawString(ML+300, y, f['cant'])
        c.setFillColor(GRIS); c.setFont('B', 7.6); c.drawString(ML+400, y, f['detalle'])
        c.setFont('BM', 8.2); c.setFillColor(TINTA); c.drawRightString(A4W-MR, y, pesos(f['precio']))
        y -= 13.5
    for (desc, cant, precio) in pl.extras:
        c.setFont('B', 8.2); c.setFillColor(TINTA); c.drawString(ML, y, desc)
        c.setFont('BM', 8.2); c.drawString(ML+300, y, cant)
        c.drawRightString(A4W-MR, y, pesos(precio))
        y -= 13.5
    linea(c, ML, y+4, A4W-MR, TINTA, 0.8); y -= 9
    c.setFont('BC', 10); c.setFillColor(TINTA)
    c.drawString(ML, y, 'LO QUE PAGÁS EN EL MOSTRADOR')
    c.drawRightString(A4W-MR, y, pesos(pl.costo_compra()))
    y -= 12
    c.setFont('B', 7.4); c.setFillColor(GRIS)
    sobra = pl.costo_compra() - pl.costo_material()
    c.drawString(ML, y, 'Este trabajo consume %s. Los %s que sobran quedan en recortes que te sirven para el próximo.'
                 % (pesos(pl.costo_material()), pesos(max(sobra, 0))))
    y -= 20

    # ---- precio sugerido
    alto_caja = 96
    c.setFillColor(CREMA); c.roundRect(ML, y-alto_caja, ANCHO, alto_caja, 4, stroke=0, fill=1)
    c.setFillColor(VERDE); c.rect(ML, y-alto_caja, 3.5, alto_caja, stroke=0, fill=1)
    bajo, alto = pl.precio_venta()
    hx = ML + 14
    c.setFont('BC', 10); c.setFillColor(TINTA)
    c.drawString(hx, y-18, 'SI LO HACÉS PARA VENDER')
    c.setFont('B', 8); c.setFillColor(TINTA2)
    filas_p = [('Hierro y chapa', pesos(pl.costo_material())),
               ('Discos, gas, alambre, antióxido y pintura (12 %)', pesos(pl.insumos())),
               ('Tu mano de obra: %d h × %s' % (pl.horas[0], pesos(VALOR_HORA)), pesos(pl.horas[0]*VALOR_HORA))]
    yy = y - 34
    for lab, val in filas_p:
        c.setFont('B', 8); c.setFillColor(TINTA2); c.drawString(hx, yy, lab)
        c.setFont('BM', 8); c.setFillColor(TINTA); c.drawRightString(ML+300, yy, val)
        yy -= 12
    c.setFont('BC', 9); c.setFillColor(GRIS)
    c.drawString(ML+330, y-34, 'PRECIO SUGERIDO')
    c.setFont('BC', 21); c.setFillColor(VERDE)
    c.drawString(ML+330, y-56, '%s a %s' % (pesos(bajo), pesos(alto)))
    c.setFont('B', 7.4); c.setFillColor(GRIS)
    c.drawString(ML+330, y-70, 'Te queda en el bolsillo: %s' % pesos(bajo - pl.costo_material()))
    c.setFont('B', 7); c.setFillColor(GRIS)
    c.drawString(hx, y-alto_caja+10, 'Precios de referencia de octubre de 2026. Si el hierro se movió, '
                 'cambiá el valor de la barra y el resto se acomoda solo.')
    y -= alto_caja + 18

    # ---- herramientas
    y = seccion(c, ML, y, 'Con esto alcanza')
    x = ML
    for h in pl.herramientas:
        w = chip(c, x, y-8, h.upper(), bg=HexColor('#ECEFF2'), fg=TINTA2, size=6.4, alto=12)
        x += w + 5
        if x > A4W - MR - 90:
            x = ML; y -= 16

# ----------------------------------------------------------------- hoja 2
def hoja_2(c, pl):
    encabezado(c, pl, 2); pie(c, pl, 2)
    y = titulo_hoja(c, pl, 2)
    c.setFont('BCM', 9); c.setFillColor(TINTA2)
    c.drawRightString(A4W-MR, y+10, 'Cada medida en milímetros y en pulgadas')

    x1,x2,y1,y2,z1,z2 = pl.bbox()
    W_, D_ = (x2-x1), (y2-y1)
    frac = min(0.76, max(0.46, (W_ + 60.0) / (W_ + D_ + 120.0)))
    wiz = (ANCHO - 12) * frac
    wde = ANCHO - 12 - wiz
    bx_f = (ML, 432, wiz, 268)
    bx_l = (ML+wiz+12, 432, wde, 268)
    bx_p = (ML, 128, wiz, 258)
    bx_d = (ML+wiz+12, 128, wde, 258)
    for b in (bx_f, bx_l, bx_p, bx_d):
        c.setFillColor(PAPEL); c.setStrokeColor(GRIS_CL); c.setLineWidth(0.6)
        c.rect(b[0], b[1], b[2], b[3], stroke=1, fill=1)

    pad = 30
    marcos, k = escala_comun(pl.piezas, [('frente', bx_f), ('lateral', bx_l), ('planta', bx_p)], pad)
    for vista, bx, nom in [('frente', bx_f, 'FRENTE'), ('lateral', bx_l, 'LATERAL'), ('planta', bx_p, 'PLANTA')]:
        dibujar_vista(c, pl.piezas, vista, bx, mk=marcos[vista])
        chip(c, bx[0]+7, bx[1]+bx[3]-17, nom, bg=TINTA, fg=PAPEL)

    # cotas generales
    cota_h(c, marcos['frente'], x1, x2, z1, mm_y_pulg(x2-x1), off=-17, lado=1)
    cota_v(c, marcos['frente'], z1, z2, x2, mm_y_pulg(z2-z1), off=17)
    cota_h(c, marcos['lateral'], -y2, -y1, z1, mm_y_pulg(y2-y1), off=-17, lado=1)
    cota_h(c, marcos['planta'], x1, x2, -y2, mm_y_pulg(x2-x1), off=-17, lado=1)
    cota_v(c, marcos['planta'], -y2, -y1, x2, mm_y_pulg(y2-y1), off=17)
    # cotas del plano
    for d in pl.dims:
        v = d['vista']; mk = marcos[v]
        txt = d.get('txt') or mm_y_pulg(abs(d['b']-d['a']))
        if d['tipo'] == 'h':
            cota_h(c, mk, d['a'], d['b'], d['ref'], txt, off=d.get('off', 14), lado=d.get('lado', 1))
        else:
            cota_v(c, mk, d['a'], d['b'], d['ref'], txt, off=d.get('off', 14), lado=d.get('lado', 1))

    # ---- detalle ampliado
    det = pl.detalle or dict(vista='frente', cx=x1 + 0.13*(x2-x1), cy=z2 - 0.10*(z2-z1),
                             r=0.11*max(x2-x1, z2-z1),
                             nota='La unión de arriba a la izquierda. Si esta esquina está a escuadra, el resto se acomoda.')
    mkv = marcos[det['vista']]
    cen = mkv((det['cx'], det['cy'])); rr = det['r']*k
    c.setStrokeColor(NARANJA); c.setLineWidth(1.0); c.setFillColor(PAPEL)
    c.circle(cen[0], cen[1], rr, stroke=1, fill=0)
    c.setFont('BC', 8); c.setFillColor(NARANJA)
    c.drawString(cen[0]+rr+2, cen[1]+rr-2, 'A')
    # zoom
    rz = min(bx_d[2], bx_d[3])/2.0 - 24
    czx, czy = bx_d[0]+bx_d[2]/2.0, bx_d[1]+bx_d[3]/2.0 - 6
    kz = rz/det['r']
    c.saveState()
    pth = c.beginPath(); pth.circle(czx, czy, rz); c.clipPath(pth, stroke=0, fill=0)
    mkz = Marco(czx-rz, czy-rz, 2*rz, 2*rz, det['cx']-det['r'], det['cx']+det['r'],
                det['cy']-det['r'], det['cy']+det['r'], 0, kz)
    dibujar_vista(c, pl.piezas, det['vista'], bx_d, mk=mkz, lw=0.9)
    c.restoreState()
    c.setStrokeColor(NARANJA); c.setLineWidth(1.0)
    c.circle(czx, czy, rz, stroke=1, fill=0)
    chip(c, bx_d[0]+7, bx_d[1]+bx_d[3]-17, 'DETALLE A · %dx' % max(2, int(round(kz/k))), bg=NARANJA, fg=PAPEL)
    c.setFont('B', 7.2); c.setFillColor(TINTA2)
    for i, l in enumerate(envolver(c, det['nota'], 'B', 7.2, bx_d[2]-20)[:2]):
        c.drawCentredString(bx_d[0]+bx_d[2]/2.0, bx_d[1]+12 - i*9, l)

    # ---- nota de escala
    escala = int(round(1.0/k)) if k else 0
    c.setFont('BCM', 7.6); c.setFillColor(GRIS)
    c.drawString(ML, 108, 'Escala aproximada 1:%d. Medí por los números, nunca con la regla sobre el papel.' % escala)
    c.drawString(ML, 97, 'Las tres vistas están a la misma escala. Lo punteado es una pieza que tapa a las de abajo.')
    c.drawRightString(A4W-MR, 108, 'Medidas en mm  ·  pulgadas entre paréntesis')
    c.drawRightString(A4W-MR, 97, 'Tolerancia de taller: ± 2 mm')

# ----------------------------------------------------------------- hoja 3
def hoja_3(c, pl):
    encabezado(c, pl, 3); pie(c, pl, 3)
    y = titulo_hoja(c, pl, 3)
    items = pl.cortes()
    c.setFont('BCM', 9); c.setFillColor(TINTA2)
    c.drawRightString(A4W-MR, y+10, '%d piezas en total' % sum(i['cant'] for i in items))

    y = seccion(c, ML, y, 'Cortá estas piezas')
    cols = [ML, ML+28, ML+56, ML+236, ML+310, ML+382, ML+428]
    c.setFont('BCM', 6.8); c.setFillColor(GRIS)
    for x, t in zip(cols, ['PIEZA', 'CANT', 'MATERIAL', 'LARGO', 'PULGADAS', 'CORTE', 'DÓNDE VA']):
        c.drawString(x, y, t)
    y -= 4; linea(c, ML, y, A4W-MR, GRIS_CL, 0.4); y -= 13
    alto = 14.6 if len(items) <= 20 else 12.4
    fs = 8.2 if len(items) <= 20 else 7.4
    for i, it in enumerate(items):
        if i % 2 == 0:
            c.setFillColor(HexColor('#F7F8F9')); c.rect(ML-4, y-4, ANCHO+8, alto, stroke=0, fill=1)
        c.setFillColor(NARANJA); c.setFont('BC', fs+1.4); c.drawString(cols[0], y, it['letra'])
        c.setFillColor(TINTA); c.setFont('BM', fs); c.drawString(cols[1], y, '%d' % it['cant'])
        c.setFont('B', fs); c.drawString(cols[2], y, M[it['mat']]['nom'])
        if it['ancho']:
            c.setFont('BM', fs); c.drawString(cols[3], y, '%d x %d mm' % (it['largo'], it['ancho']))
            c.setFont('B', fs); c.setFillColor(TINTA2)
            c.drawString(cols[4], y, '%s x %s' % (pulg(it['largo']), pulg(it['ancho'])))
        else:
            c.setFont('BM', fs); c.drawString(cols[3], y, '%d mm' % it['largo'])
            c.setFont('B', fs); c.setFillColor(TINTA2); c.drawString(cols[4], y, pulg(it['largo']))
        c.setFont('B', fs); c.setFillColor(TINTA2)
        c.drawString(cols[5], y, 'a escuadra' if it['ancho'] else it['corte'])
        rol = it['rol']
        while c.stringWidth(rol, 'B', fs) > ANCHO - (cols[6]-ML) and len(rol) > 4:
            rol = rol[:-2]
        c.drawString(cols[6], y, rol)
        y -= alto
    y -= 10

    # ---- aprovechamiento
    _, nest = pl.compra()
    y = seccion(c, ML, y, 'Cómo sale de las barras de 6 m')
    total_barras = sum(len(b) for _, b in nest)
    c.setFont('B', 7.6); c.setFillColor(GRIS)
    c.drawRightString(A4W-MR, y+17, 'Corte de sierra contemplado: 3 mm por corte')
    letras = {}
    for it in items:
        letras[(it['mat'], it['largo'])] = it['letra']
    esc = ANCHO / 6000.0
    for mat, barras in nest:
        if y < 120: break
        c.setFont('BC', 8); c.setFillColor(TINTA)
        c.drawString(ML, y, M[mat]['nom'].upper())
        c.setFont('B', 7.4); c.setFillColor(GRIS)
        c.drawRightString(A4W-MR, y, '%d barra%s' % (len(barras), '' if len(barras)==1 else 's'))
        y -= 13
        for b in barras:
            if y < 108: break
            x = ML
            c.setFillColor(HexColor('#EDEFF1')); c.setStrokeColor(GRIS_CL); c.setLineWidth(0.4)
            c.rect(ML, y-9, ANCHO, 13, stroke=1, fill=1)
            for L in b['cortes']:
                w = L*esc
                c.setFillColor(HexColor('#DCE2E7')); c.setStrokeColor(TINTA2); c.setLineWidth(0.4)
                c.rect(x, y-9, w, 13, stroke=1, fill=1)
                let = letras.get((mat, L), '')
                if w > 13:
                    c.setFont('BC', 6.6); c.setFillColor(TINTA)
                    c.drawCentredString(x + w/2.0, y-5.5, let)
                if w > 42:
                    c.setFont('BCM', 5.8); c.setFillColor(TINTA2)
                    c.drawCentredString(x + w/2.0, y-13.5+1.2, '%d' % L)
                x += w + 3*esc
            sobra = 6000 - sum(b['cortes']) - 3*len(b['cortes'])
            if sobra*esc > 26:
                c.setFont('BCM', 5.8); c.setFillColor(GRIS)
                c.drawCentredString(x + sobra*esc/2.0, y-5.5, 'sobra %d mm' % sobra)
            y -= 24
        y -= 2
    c.setFont('B', 7.6); c.setFillColor(TINTA2)
    c.drawString(ML, 76, 'Comprás %d barra%s de 6 m en total. Cortá siempre de mayor a menor: lo que sobra de una barra larga todavía sirve.'
                 % (total_barras, '' if total_barras == 1 else 's'))

    # ---- donde va cada letra + control
    if y > 290:
        y -= 6
        col = (ANCHO - 16) * 0.52
        yy = seccion(c, ML, y, 'Dónde va cada letra', col)
        caja = (ML, max(100, yy - 160), col, min(158, yy - 104))
        c.setFillColor(CREMA); c.roundRect(caja[0], caja[1], caja[2], caja[3], 3, stroke=0, fill=1)
        letras_iso(c, pl, (caja[0]+8, caja[1]+8, caja[2]-16, caja[3]-16), pad=10)
        x0 = ML + col + 16
        anc = ANCHO - col - 16
        yy = seccion(c, x0, y, 'Antes de hacer el primer corte', anc)
        checks = [
            'Medí la barra entera antes de cortar: muchas vienen 5,95 m y no 6 m.',
            'Marcá con punta de metal, no con fibra: la fibra se corre 2 mm.',
            'Cortá de mayor a menor y escribí la letra en cada pieza apenas la cortás.',
            'Desbastá la rebaba de cada corte antes de presentar: si no, nada apoya derecho.',
            'Presentá todo en seco y recién ahí puntéa.']
        for t in checks:
            c.setStrokeColor(GRIS); c.setLineWidth(0.6)
            c.rect(x0, yy-1.5, 6.5, 6.5, stroke=1, fill=0)
            c.setFont('B', 7.8); c.setFillColor(TINTA2)
            for l in envolver(c, t, 'B', 7.8, anc-14):
                c.drawString(x0+13, yy, l); yy -= 9.8
            yy -= 5

# ----------------------------------------------------------------- hoja 4
def hoja_4(c, pl):
    encabezado(c, pl, 4); pie(c, pl, 4)
    y = titulo_hoja(c, pl, 4)
    c.setFont('BCM', 9); c.setFillColor(TINTA2)
    c.drawRightString(A4W-MR, y+10, 'En naranja, lo que sumás en cada paso')

    pasos = pl.pasos[:12]
    filas = int(math.ceil(len(pasos)/3.0))
    y = seccion(c, ML, y - 10, 'Soldá en este orden')
    top = y + 6
    alto_fila = min(250.0, (top - 196) / max(filas, 1))
    ancho_cel = (ANCHO - 2*10) / 3.0
    mk = marco_para(pl.piezas, 'iso', (0, 0, ancho_cel-10, alto_fila-56), pad=4)
    acumulado = []
    for i, (texto, tags) in enumerate(pasos):
        col = i % 3; fil = i // 3
        x = ML + col*(ancho_cel+10)
        yy = top - fil*alto_fila
        c.setFillColor(CREMA); c.roundRect(x, yy-alto_fila+10, ancho_cel, alto_fila-12, 3, stroke=0, fill=1)
        caja = (x+5, yy-alto_fila+18, ancho_cel-10, alto_fila-78)
        mkl = Marco(caja[0], caja[1], caja[2], caja[3],
                    *caja_vista(pl.piezas, 'iso'), pad=4)
        vis = [p for p in pl.piezas if p.tag in acumulado or p.tag in tags]
        dibujar_iso(c, vis, caja, mk=mkl, resaltar=tags)
        c.setFillColor(NARANJA); c.circle(x+13, yy-9, 8, stroke=0, fill=1)
        c.setFont('BC', 9); c.setFillColor(PAPEL)
        c.drawCentredString(x+13, yy-12, '%d' % (i+1))
        c.setFont('B', 7.3); c.setFillColor(TINTA2)
        ls = envolver(c, texto, 'B', 7.3, ancho_cel-32)[:4]
        for j, l in enumerate(ls):
            c.drawString(x+26, yy-11 - j*9.0, l)
        acumulado.extend(tags)

    # ---- avisos
    y = top - filas*alto_fila - 2
    if y < 176: y = 176
    col = (ANCHO - 16)/2.0
    yy = seccion(c, ML, y, 'Dos cosas que te van a arruinar el trabajo', col)
    for i, a in enumerate(pl.avisos[:3]):
        c.setFillColor(NARANJA); c.circle(ML+3, yy+2.6, 2.2, stroke=0, fill=1)
        yy = parrafo(c, a, ML+11, yy, col-11, 'B', 7.8, 10.2) - 13
    yy2 = seccion(c, ML+col+16, y, 'Terminación y entrega', col)
    cierre = ('Desbastá la escoria, pasá disco de láminas por cada cordón y matá los cantos vivos. '
              'Desengrasá, una mano de fondo antióxido y dos de esmalte sintético. Si va a la intemperie, '
              'dejá 24 h entre manos y no pintes con humedad. Sacale fotos con el trabajo limpio y de día: '
              'esa foto es la que te vende el próximo.')
    parrafo(c, cierre, ML+col+16, yy2, col, 'B', 7.8, 10.2)

    c.setFillColor(TINTA); c.roundRect(ML, 72, ANCHO, 42, 3, stroke=0, fill=1)
    c.setFont('BC', 11); c.setFillColor(NARANJA)
    c.drawString(ML+14, 98, 'YA LO TENÉS TERMINADO. ¿CUÁNTO COBRÁS?')
    bajo, alto = pl.precio_venta()
    c.setFont('B', 8.2); c.setFillColor(PAPEL)
    c.drawString(ML+14, 84, 'Este trabajo se vende entre %s y %s. El hierro te costó %s. Sacale la foto y publicalo hoy.'
                 % (pesos(bajo), pesos(alto), pesos(pl.costo_material())))

def hojas(c, pl):
    for f in (hoja_1, hoja_2, hoja_3, hoja_4):
        f(c, pl); c.showPage()
