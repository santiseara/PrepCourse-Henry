# -*- coding: utf-8 -*-
"""Genera la Planilla de Cortes (xlsx) con los mismos materiales y precios del PDF."""
import sys, os
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.workbook.defined_name import DefinedName
from engine import M, VALOR_HORA, INSUMOS, FACTOR_ALTO

TINTA = '15181C'; NARANJA = 'F26B21'; CREMA = 'F4F2EE'; VERDE = '1C8C4C'
AMARILLO = 'FFF3CC'; GRIS = '8A9099'; LINEA = 'D7DBDF'
F = 'Arial'


def frac_pulgadas(ref):
    """Formula que pasa mm a pulgadas con fraccion en dieciseisavos, sin usar formatos raros."""
    n = 'ROUND(%s/25.4*16,0)' % ref
    e = 'INT(%s/16)' % n
    r = 'MOD(%s,16)' % n
    fr = ('IF(MOD({r},8)=0,"1/2",IF(MOD({r},4)=0,{r}/4&"/4",'
          'IF(MOD({r},2)=0,{r}/2&"/8",{r}&"/16")))').format(r=r)
    return ('=IF({ref}="","",TRIM(IF({e}=0,"",{e})&IF({r}=0,""," "&{fr}))&CHAR(34))'
            .format(ref=ref, e=e, r=r, fr=fr))

def fuente(**kw): return Font(name=F, **kw)
B_FINA = Border(bottom=Side(style='thin', color=LINEA))

def titulo(ws, fila, texto, bajada=''):
    ws.cell(fila, 1, texto).font = fuente(bold=True, size=16, color=TINTA)
    if bajada:
        ws.cell(fila+1, 1, bajada).font = fuente(size=10, color=GRIS)

def encabezado(ws, fila, cols, anchos=None):
    for i, t in enumerate(cols, start=1):
        c = ws.cell(fila, i, t)
        c.font = fuente(bold=True, size=9, color='FFFFFF')
        c.fill = PatternFill('solid', fgColor=TINTA)
        c.alignment = Alignment(vertical='center', wrap_text=True)
    ws.row_dimensions[fila].height = 28
    if anchos:
        for i, a in enumerate(anchos, start=1):
            ws.column_dimensions[get_column_letter(i)].width = a

def entrada(c, fmt=None):
    c.fill = PatternFill('solid', fgColor=AMARILLO)
    c.font = fuente(size=10, color='0000FF')
    if fmt: c.number_format = fmt

def calculo(c, fmt=None):
    c.font = fuente(size=10, color=TINTA)
    if fmt: c.number_format = fmt

PESOS = '"$"#,##0'
DEC2 = '#,##0.00'
DEC3 = '#,##0.000'

def construir(salida):
    wb = Workbook()
    wb.calculation.fullCalcOnLoad = True

    barras = [(k, d) for k, d in M.items() if d.get('por') != 'm2']
    chapas = [(k, d) for k, d in M.items() if d.get('por') == 'm2']
    barras.sort(key=lambda kd: (kd[1]['fam'], kd[1]['precio']))
    chapas.sort(key=lambda kd: kd[1]['precio'])

    # ====================================================== MATERIALES
    mat = wb.active; mat.title = 'Materiales'
    titulo(mat, 1, 'MATERIALES Y PRECIOS',
           'Precios de referencia de octubre de 2026. Si el hierro se movió, cambiá el factor de abajo y se actualiza toda la planilla.')
    mat['A4'] = 'Factor de actualización'; mat['A4'].font = fuente(bold=True, size=10)
    mat['B4'] = 1.0; entrada(mat['B4'], DEC2)
    mat['C4'] = 'Poné 1,20 si el hierro subió 20 % desde octubre de 2026.'
    mat['C4'].font = fuente(size=9, color=GRIS)
    mat['A6'] = 'Largo de la barra (mm)'; mat['A6'].font = fuente(bold=True, size=10)
    mat['B6'] = 6000; entrada(mat['B6'], '#,##0')
    mat['A7'] = 'Corte de sierra (mm)'; mat['A7'].font = fuente(bold=True, size=10)
    mat['B7'] = 3; entrada(mat['B7'], '#,##0')

    FILA0 = 10
    encabezado(mat, FILA0, ['Material', 'Cómo se pide', 'Tipo', 'kg por metro',
                            'Precio base', 'Precio hoy', 'Lo que pide tu lista',
                            'Barras cortando cada largo aparte', 'Barras combinando largos',
                            'Lo que pagás'],
               [46, 18, 8, 11, 12, 12, 16, 17, 17, 13])
    f = FILA0 + 1
    fila_barra = {}
    for k, d in barras:
        mat.cell(f, 1, d['nom']).font = fuente(size=10)
        mat.cell(f, 2, d['corto']).font = fuente(size=10, color=GRIS)
        mat.cell(f, 3, 'barra').font = fuente(size=10, color=GRIS)
        calculo(mat.cell(f, 4, d.get('kgm', 0)), DEC2)
        calculo(mat.cell(f, 5, d['precio']), PESOS)
        calculo(mat.cell(f, 6, '=E%d*$B$4' % f), PESOS)
        calculo(mat.cell(f, 7, "=SUMIFS('Lista de cortes'!$G$9:$G$58,'Lista de cortes'!$C$9:$C$58,$A%d)" % f), DEC2)
        calculo(mat.cell(f, 8, "=SUMIFS('Lista de cortes'!$I$9:$I$58,'Lista de cortes'!$C$9:$C$58,$A%d)" % f), '#,##0')
        calculo(mat.cell(f, 9, '=IF(G%d=0,0,ROUNDUP(G%d/($B$6/1000),0))' % (f, f)), '#,##0')
        calculo(mat.cell(f, 10, '=H%d*F%d' % (f, f)), PESOS)
        for col in range(1, 11): mat.cell(f, col).border = B_FINA
        fila_barra[k] = f; f += 1
    fin_barras = f - 1
    f += 1
    mat.cell(f, 1, 'CHAPAS Y PLANOS (se venden por m²)').font = fuente(bold=True, size=10, color=NARANJA)
    f += 1
    ini_chapas = f
    for k, d in chapas:
        mat.cell(f, 1, d['nom']).font = fuente(size=10)
        mat.cell(f, 2, d['corto']).font = fuente(size=10, color=GRIS)
        mat.cell(f, 3, 'm²').font = fuente(size=10, color=GRIS)
        mat.cell(f, 4, '').font = fuente(size=10)
        calculo(mat.cell(f, 5, d['precio']), PESOS)
        calculo(mat.cell(f, 6, '=E%d*$B$4' % f), PESOS)
        calculo(mat.cell(f, 7, "=SUMIFS('Lista de cortes'!$G$64:$G$78,'Lista de cortes'!$C$64:$C$78,$A%d)" % f), DEC2)
        mat.cell(f, 8, '—').font = fuente(size=10, color=GRIS)
        mat.cell(f, 9, '—').font = fuente(size=10, color=GRIS)
        calculo(mat.cell(f, 10, '=G%d*1.12*F%d' % (f, f)), PESOS)
        for col in range(1, 11): mat.cell(f, col).border = B_FINA
        f += 1
    fin_chapas = f - 1
    f += 1
    mat.cell(f, 1, 'TOTAL DEL HIERRO DE TU LISTA').font = fuente(bold=True, size=11, color=TINTA)
    calculo(mat.cell(f, 10, '=SUM(J%d:J%d)+SUM(J%d:J%d)' % (FILA0+1, fin_barras, ini_chapas, fin_chapas)), PESOS)
    mat.cell(f, 10).font = fuente(bold=True, size=11, color=VERDE)
    fila_total = f
    mat.cell(f+1, 1, 'Al m² de chapa se le suma un 12 % de recorte, igual que en los planos.').font = fuente(size=9, color=GRIS)
    mat.freeze_panes = 'A%d' % (FILA0+1)

    wb.defined_names.add(DefinedName('MatBarras', attr_text="Materiales!$A$%d:$A$%d" % (FILA0+1, fin_barras)))
    wb.defined_names.add(DefinedName('MatChapas', attr_text="Materiales!$A$%d:$A$%d" % (ini_chapas, fin_chapas)))

    # ====================================================== LISTA DE CORTES
    ws = wb.create_sheet('Lista de cortes')
    titulo(ws, 1, 'LISTA DE CORTES',
           'Cargá las piezas de tu trabajo en las celdas amarillas. La planilla te dice cuántas barras comprar y cuánto sale.')
    ws['A4'] = 'Celdas amarillas: las llenás vos.'; ws['A4'].font = fuente(size=9, color='0000FF')
    ws['C4'] = 'El resto se calcula solo. El material se elige de la lista desplegable.'
    ws['C4'].font = fuente(size=9, color=GRIS)
    ws['F4'] = 'Lo que pagás en el mostrador:'; ws['F4'].font = fuente(bold=True, size=10)
    calculo(ws['H4'], PESOS); ws['H4'] = '=Materiales!J%d' % fila_total
    ws['H4'].font = fuente(bold=True, size=12, color=VERDE)

    FIL = 8
    encabezado(ws, FIL, ['Pieza', 'Dónde va', 'Material', 'Largo (mm)', 'En pulgadas',
                         'Cantidad', 'Metros con corte de sierra', 'Cortes por barra',
                         'Barras para esta pieza', 'Peso aprox. (kg)'],
               [8, 30, 42, 12, 14, 10, 15, 13, 13, 13])
    ejemplo = [('A', 'marco de la tapa', M['TC50']['nom'], 1220, 2),
               ('B', 'patas', M['TC50']['nom'], 875, 4)]
    for i in range(9, 59):
        for col in (1, 2, 3, 4, 6):
            entrada(ws.cell(i, col), '#,##0' if col in (4, 6) else None)
        calculo(ws.cell(i, 5, frac_pulgadas('D%d' % i)))
        calculo(ws.cell(i, 7, '=IF(OR(D%d="",F%d=""),"",(D%d+Materiales!$B$7)*F%d/1000)' % (i, i, i, i)), DEC2)
        calculo(ws.cell(i, 8, '=IF(D%d="","",INT(Materiales!$B$6/(D%d+Materiales!$B$7)))' % (i, i)), '#,##0')
        calculo(ws.cell(i, 9, '=IF(OR(D%d="",F%d="",H%d=0),"",ROUNDUP(F%d/H%d,0))' % (i, i, i, i, i)), '#,##0')
        calculo(ws.cell(i, 10, '=IF(G%d="","",G%d*IFERROR(INDEX(Materiales!$D$%d:$D$%d,MATCH($C%d,Materiales!$A$%d:$A$%d,0)),0))'
                        % (i, i, FILA0+1, fin_barras, i, FILA0+1, fin_barras)), DEC2)
        for col in range(1, 11): ws.cell(i, col).border = B_FINA
    for k, (letra, donde, material, largo, cant) in enumerate(ejemplo):
        r = 9 + k
        ws.cell(r, 1, letra); ws.cell(r, 2, donde); ws.cell(r, 3, material)
        ws.cell(r, 4, largo); ws.cell(r, 6, cant)
    ws.cell(7, 1, 'EJEMPLO CARGADO EN LAS DOS PRIMERAS FILAS: borralo y poné lo tuyo.').font = fuente(size=9, color=NARANJA, italic=True)

    ws.cell(60, 2, 'TOTAL').font = fuente(bold=True, size=10)
    calculo(ws.cell(60, 7, '=SUM(G9:G58)'), DEC2); ws.cell(60, 7).font = fuente(bold=True, size=10)
    calculo(ws.cell(60, 9, '=SUM(I9:I58)'), '#,##0'); ws.cell(60, 9).font = fuente(bold=True, size=10)
    calculo(ws.cell(60, 10, '=SUM(J9:J58)'), DEC2); ws.cell(60, 10).font = fuente(bold=True, size=10)

    ws.cell(62, 1, 'CHAPAS Y PLANOS (se piden por metro cuadrado)').font = fuente(bold=True, size=12, color=TINTA)
    encabezado(ws, 63, ['Pieza', 'Dónde va', 'Material (chapa)', 'Largo (mm)', 'Ancho (mm)',
                        'Cantidad', 'm² que consume', '', '', ''])
    for i in range(64, 79):
        for col in (1, 2, 3, 4, 5, 6):
            entrada(ws.cell(i, col), '#,##0' if col in (4, 5, 6) else None)
        calculo(ws.cell(i, 7, '=IF(OR(D%d="",E%d="",F%d=""),"",D%d*E%d*F%d/1000000)' % (i, i, i, i, i, i)), DEC2)
        for col in range(1, 8): ws.cell(i, col).border = B_FINA
    ws.cell(80, 2, 'TOTAL').font = fuente(bold=True, size=10)
    calculo(ws.cell(80, 7, '=SUM(G64:G78)'), DEC2); ws.cell(80, 7).font = fuente(bold=True, size=10)

    dv1 = DataValidation(type='list', formula1='=MatBarras', allow_blank=True)
    dv2 = DataValidation(type='list', formula1='=MatChapas', allow_blank=True)
    ws.add_data_validation(dv1); ws.add_data_validation(dv2)
    dv1.add('C9:C58'); dv2.add('C64:C78')
    ws.freeze_panes = 'A9'

    # ====================================================== CONVERSOR
    cv = wb.create_sheet('Conversor')
    titulo(cv, 1, 'CONVERSOR DE MEDIDAS',
           'Milímetros, pulgadas, metros y pies. Las celdas amarillas las escribís vos.')
    cv.column_dimensions['A'].width = 26; cv.column_dimensions['B'].width = 14
    cv.column_dimensions['C'].width = 16; cv.column_dimensions['D'].width = 18
    cv.column_dimensions['E'].width = 16; cv.column_dimensions['F'].width = 30

    cv['A4'] = 'DE MILÍMETROS A PULGADAS'; cv['A4'].font = fuente(bold=True, size=11, color=NARANJA)
    encabezado(cv, 5, ['Escribí los mm', 'Pulgadas', 'En fracción', 'En pies', '', ''])
    for i in range(6, 12):
        entrada(cv.cell(i, 1), '#,##0')
        calculo(cv.cell(i, 2, '=IF(A%d="","",A%d/25.4)' % (i, i)), DEC3)
        calculo(cv.cell(i, 3, frac_pulgadas('A%d' % i)))
        calculo(cv.cell(i, 4, '=IF(A%d="","",A%d/304.8)' % (i, i)), DEC2)
    cv['A6'] = 1220

    cv['A14'] = 'DE PULGADAS A MILÍMETROS'; cv['A14'].font = fuente(bold=True, size=11, color=NARANJA)
    encabezado(cv, 15, ['Pulgadas enteras', 'Numerador', 'Denominador', 'Milímetros', '', ''])
    for i in range(16, 22):
        for col in (1, 2, 3): entrada(cv.cell(i, col), '#,##0')
        calculo(cv.cell(i, 4, '=IF(A%d="","",(A%d+IFERROR(B%d/C%d,0))*25.4)' % (i, i, i, i)), '#,##0.0')
    cv['A16'] = 48; cv['B16'] = 1; cv['C16'] = 16

    cv['A24'] = 'METROS Y PIES'; cv['A24'].font = fuente(bold=True, size=11, color=NARANJA)
    encabezado(cv, 25, ['Escribí los metros', 'Pies', 'Escribí los pies', 'Metros', '', ''])
    for i in range(26, 30):
        entrada(cv.cell(i, 1), DEC2)
        calculo(cv.cell(i, 2, '=IF(A%d="","",A%d*3.28084)' % (i, i)), DEC2)
        entrada(cv.cell(i, 3), DEC2)
        calculo(cv.cell(i, 4, '=IF(C%d="","",C%d/3.28084)' % (i, i)), DEC2)
    cv['A26'] = 6; cv['C26'] = 20

    cv['A32'] = 'LAS MEDIDAS QUE MÁS VAS A USAR'; cv['A32'].font = fuente(bold=True, size=11, color=NARANJA)
    encabezado(cv, 33, ['Milímetros', 'Pulgadas', 'En fracción', 'Para qué', '', ''])
    usuales = [(20, 'caño 20 x 20'), (25, 'caño 25 x 25 · 1"'), (30, 'caño 30 x 30'),
               (38, 'caño 1 1/2"'), (40, 'caño 40 x 40'), (50, 'caño 50 x 50 · 2"'),
               (60, 'caño 60 x 60'), (76, 'planchuela de 3"'), (80, 'caño 80 x 80'),
               (100, 'caño 100 x 100 · perfil C'), (120, 'perfil C 120'), (150, ''),
               (200, ''), (250, ''), (300, ''), (406, 'travesaños cada 16"'),
               (500, ''), (600, 'ancho de mesada'), (900, 'altura de mesa'),
               (1000, ''), (1200, 'ancho de chapa'), (1500, ''), (1800, ''),
               (2000, ''), (2440, 'largo de chapa · 8 pies'), (3000, 'media barra'),
               (6000, 'barra entera · 20 pies')]
    r = 34
    for mm, para in usuales:
        calculo(cv.cell(r, 1, mm), '#,##0')
        calculo(cv.cell(r, 2, '=A%d/25.4' % r), DEC2)
        calculo(cv.cell(r, 3, frac_pulgadas('A%d' % r)))
        cv.cell(r, 4, para).font = fuente(size=9, color=GRIS)
        for col in range(1, 5): cv.cell(r, col).border = B_FINA
        r += 1

    cv['F4'] = 'ESPESORES DE CHAPA'; cv['F4'].font = fuente(bold=True, size=11, color=NARANJA)
    encabezado(cv, 5, ['', '', '', '', '', ''])
    cv.cell(5, 6, 'Chapa (mm) · equivalencia').font = fuente(bold=True, size=9, color='FFFFFF')
    esp = [('1,6 mm', 'BWG 16 · 1/16"'), ('2 mm', 'BWG 14 · 5/64"'), ('2,5 mm', 'BWG 12'),
           ('3 mm', '1/8" · la de los fogoneros'), ('4,75 mm', '3/16" · pisos de parrilla'),
           ('6 mm', '1/4" · tapas de mesa de soldar'), ('8 mm', '5/16"'),
           ('12,7 mm', '1/2" · bases de columna')]
    r = 6
    for a, b in esp:
        cv.cell(r, 6, a + '  →  ' + b).font = fuente(size=10)
        cv.cell(r, 6).border = B_FINA
        r += 1
    cv.cell(r+1, 6, 'Un metro cuadrado de chapa de 3 mm pesa unos 23,5 kg.').font = fuente(size=9, color=GRIS)
    cv.cell(r+2, 6, 'La hoja estándar es de 1 x 2 m o de 1,22 x 2,44 m.').font = fuente(size=9, color=GRIS)

    # ====================================================== PRESUPUESTO
    pr = wb.create_sheet('Presupuesto')
    titulo(pr, 1, 'CUÁNTO COBRAR',
           'La misma fórmula que usan los planos de la biblioteca. Cambiá el valor de tu hora y se recalcula todo.')
    pr.column_dimensions['A'].width = 46; pr.column_dimensions['B'].width = 16
    pr.column_dimensions['C'].width = 52
    filas = [
        ('Hierro de tu lista de cortes', '=Materiales!J%d' % fila_total, PESOS, False,
         'Viene de la hoja Lista de cortes. Si cotizás sin cargar la lista, escribí el número a mano.'),
        ('Insumos (discos, gas, alambre, antióxido, pintura)', '=B4*B6', PESOS, False, 'Se calcula con el porcentaje de abajo.'),
        ('Porcentaje de insumos', INSUMOS, '0%', True, 'En la biblioteca usamos 12 %.'),
        ('Horas de trabajo', 6, '#,##0.0', True, 'Las que dice el plano, o las que calculaste vos.'),
        ('Valor de tu hora', VALOR_HORA, PESOS, True, 'Cambialo por el tuyo. Es la celda que más mueve el precio.'),
        ('Mano de obra', '=B7*B8', PESOS, False, ''),
    ]
    r = 4
    for nombre, valor, fmt, es_entrada, nota in filas:
        pr.cell(r, 1, nombre).font = fuente(size=10)
        c = pr.cell(r, 2, valor)
        (entrada if es_entrada else calculo)(c, fmt)
        pr.cell(r, 3, nota).font = fuente(size=9, color=GRIS)
        pr.cell(r, 1).border = B_FINA; pr.cell(r, 2).border = B_FINA
        r += 1
    pr.cell(11, 1, 'PRECIO SUGERIDO (piso)').font = fuente(bold=True, size=12, color=TINTA)
    calculo(pr.cell(11, 2, '=B4+B5+B9'), PESOS); pr.cell(11, 2).font = fuente(bold=True, size=12, color=VERDE)
    pr.cell(11, 3, 'Por debajo de esto estás trabajando gratis.').font = fuente(size=9, color=GRIS)
    pr.cell(12, 1, 'TECHO DEL RANGO').font = fuente(bold=True, size=12, color=TINTA)
    calculo(pr.cell(12, 2, '=B11*%s' % FACTOR_ALTO), PESOS); pr.cell(12, 2).font = fuente(bold=True, size=12, color=VERDE)
    pr.cell(12, 3, 'Con terminación prolija, entrega rápida y el trabajo ya mostrado en fotos.').font = fuente(size=9, color=GRIS)
    pr.cell(14, 1, 'Te queda en el bolsillo').font = fuente(size=10)
    calculo(pr.cell(14, 2, '=B11-B4'), PESOS)
    pr.cell(15, 1, 'Lo que te queda por hora').font = fuente(size=10)
    calculo(pr.cell(15, 2, '=IFERROR((B11-B4)/B7,0)'), PESOS)
    pr.cell(17, 1, 'LO QUE SE COBRA APARTE').font = fuente(bold=True, size=11, color=NARANJA)
    extras = [('Traslado y entrega', 0), ('Instalación o amure', 0), ('Recargo por apuro', 0),
              ('Viajes a medir', 0), ('Pintura especial (epoxi, galvanizado, color)', 0)]
    r = 18
    for nombre, v in extras:
        pr.cell(r, 1, nombre).font = fuente(size=10)
        entrada(pr.cell(r, 2, v), PESOS)
        pr.cell(r, 1).border = B_FINA; pr.cell(r, 2).border = B_FINA
        r += 1
    pr.cell(r, 1, 'TOTAL DEL PRESUPUESTO').font = fuente(bold=True, size=12, color=TINTA)
    calculo(pr.cell(r, 2, '=B11+SUM(B18:B22)'), PESOS)
    pr.cell(r, 2).font = fuente(bold=True, size=14, color=VERDE)
    pr.cell(r+2, 1, 'Pedí el 50 % de adelanto para comprar el material. Nunca pongas plata tuya en el hierro de otro.').font = fuente(size=10, italic=True, color=TINTA)

    # ====================================================== CÓMO SE USA
    cu = wb.create_sheet('Cómo se usa', 0)
    cu.column_dimensions['A'].width = 4
    cu.column_dimensions['B'].width = 110
    titulo(cu, 2, 'PLANILLA DE CORTES · HERRERO DE FINDE',
           'Bonus 1 de la Biblioteca de Planos. Funciona en Excel, en Google Sheets y en Numbers.')
    bloques = [
        ('QUÉ HACE', [
            'Cargás las piezas de un trabajo y te dice cuántas barras de 6 m comprar, cuánto pesa el hierro y cuánto te sale.',
            'Convierte milímetros a pulgadas y al revés, con la fracción en dieciseisavos, que es como se pide en la casa de hierros.',
            'Arma el presupuesto con la misma fórmula que usan los planos: material, insumos, tus horas y el margen.']),
        ('CÓMO SE USA, PASO POR PASO', [
            '1. Abrí la hoja "Lista de cortes". Las celdas amarillas son las únicas que tocás.',
            '2. En cada fila: la letra de la pieza, dónde va, el material (se elige de la lista), el largo en milímetros y cuántas necesitás.',
            '3. La planilla te completa las pulgadas, los metros que consume, cuántos cortes entran en una barra y cuántas barras comprar.',
            '4. Las chapas van en la tabla de abajo, con largo y ancho: se calculan por metro cuadrado.',
            '5. Arriba a la derecha te aparece lo que vas a pagar en el mostrador.',
            '6. Pasá a la hoja "Presupuesto", poné tus horas y el valor de tu hora, y ya tenés el precio para pasarle al cliente.']),
        ('DOS NÚMEROS QUE NO SON LO MISMO', [
            'En la hoja "Materiales" vas a ver dos columnas de barras. "Cortando cada largo aparte" es el número seguro: el que pedís en la casa de hierros y te alcanza seguro.',
            '"Combinando largos" es el mínimo teórico, si lográs meter cortes distintos en la misma barra sin desperdiciar nada. Entre esos dos números está tu habilidad cortando.']),
        ('SI EL HIERRO CAMBIÓ DE PRECIO', [
            'No toques los precios uno por uno. Andá a la hoja "Materiales" y cambiá el factor de actualización: si subió 20 %, poné 1,20. Toda la planilla se recalcula sola.',
            'Si querés cargar los precios exactos de tu casa de hierros, cambiá la columna "Precio base" y dejá el factor en 1.']),
        ('LO QUE ESTA PLANILLA NO HACE', [
            'No decide por vos cómo acomodar los cortes en cada barra. Para eso está el diagrama de corte que trae cada plano de la biblioteca, en la hoja 3.',
            'Los precios son de referencia de octubre de 2026 y de una casa de hierros promedio. El de tu zona puede ser distinto: por eso el factor es editable.']),
    ]
    r = 5
    for tit, items in bloques:
        cu.cell(r, 2, tit).font = fuente(bold=True, size=11, color=NARANJA)
        r += 1
        for it in items:
            c = cu.cell(r, 2, it)
            c.font = fuente(size=10); c.alignment = Alignment(wrap_text=True, vertical='top')
            cu.row_dimensions[r].height = 28
            r += 1
        r += 1
    cu.cell(r+1, 2, 'Herrero de Finde · Planilla de Cortes · edición de octubre de 2026').font = fuente(size=9, color=GRIS)
    cu.cell(r+2, 2, 'Uso personal y comercial de lo que fabriques. Prohibida la reventa o distribución del archivo.').font = fuente(size=9, color=GRIS)

    for hoja in wb.worksheets:
        hoja.sheet_view.showGridLines = False
    wb.save(salida)
    return salida

if __name__ == '__main__':
    s = construir(sys.argv[1] if len(sys.argv) > 1 else 'planilla.xlsx')
    print(s, '%.1f KB' % (os.path.getsize(s)/1024.0))
