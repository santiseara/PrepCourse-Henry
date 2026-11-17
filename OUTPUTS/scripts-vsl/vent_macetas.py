# -*- coding: utf-8 -*-
"""Ventanas limpias del pool de Macetas de Cemento (AR, 2026-11-17).

Pool: 201 clips bajados de #macetasdecemento y #concreteplanter (más 30 de @ali.diyideas, el creador
del plano insignia que usa Aula Digital). Entraron 30. Filtro: hoja de contactos de 4 cuadros por
clip + OCR de Vision a 1 cuadro cada 1-2 s sobre TODO el pool.

Por qué se cayeron los demás (los casos que vale la pena recordar):
  - 7643815340312481042 · "No compres macetas antes de ver nuestros videos por YouTube" en 21 de 61
    cuadros: leyenda del creador que dura casi todo el clip.
  - 7652731350587378951 · 41 cuadros con texto de 61: es un ad de otro infoproducto de macetas.
  - 7679237... / 7396310... / 7401617... · lo mismo, ads de competencia con subtítulo quemado.
  - 7663079634287807766, 7672363907406695713 · marca de agua "The Timelapse Builder" permanente.
  - 7681294531366538527 · MAKE & REBORN en 20 de 21 cuadros. Es, literalmente, uno de los clips que
    Aula Digital usa CON la marca de agua puesta. Nosotros no.
  - 7697019132939734278 · "Látex Profesional" en 65 cuadros.
  - 7598917871309196566, 7652279454286236942, 7670612057321999638 · marca de agua del creador que
    desaparece y VUELVE (regla del 11/11): se caen enteras.
  - 7304782..., 7197409..., 7292757... · cara hablando a cámara.
  - 7695045909272382727 · limpio de texto, pero el creador aparece de frente media toma: se cae por la
    regla de "nada de caras a cámara".
  - 7566054270987029768, 7031901340251065606, 7478940655419510022 · LETTERBOX. Los tres pasaron
    cropdetect y aparecieron igual como franja negra en el render. El cropdetect de ffmpeg no sirve
    para esto cuando la barra no es negro puro: lo que funcionó fue medir 10 cuadros por clip con
    numpy (filas con luminancia media < 14) y calcular el alto útil. Salieron 33 %, 62 % y 30 % de
    barra. El zoom que los taparía (1,6 a 2,6) amplía tanto la fuente que la deja borrosa, así que
    los tres se caen en vez de corregirse. El medidor quedó en `scripts-vsl/medir_barras.py`.
  - 7510957013254311190 · se cayó en la hoja de contactos del PRIMER render: viene cuadrado con fondo
    difuminado (barras borrosas arriba y abajo) y en los 50 s de la ventana no se ve una sola maceta,
    solo el balde con la mezcla. Falla el primer filtro: ¿se ve lo que vendemos?

Formato: id -> [id, inicio, fin, extras]
"""

VENT = {
    # ---- el plano insignia: el mismo clip que corre en los 58 ads de Aula Digital ----
    'ali': ['7678821416162184478', 0.3, 23.6],          # proceso completo: mezcla, toalla, globo, desmolde, pintura, moño, flores

    # ---- limpios de punta a punta ----
    'alt': ['7367336252384775429', 0.3, 10.4],          # macetas blancas altas con plantas en el jardín
    'des': ['7494769297647013127', 0.3, 10.5],          # desmolde de una maceta grande
    'mol': ['7603864801437043982', 6.0, 240.0],         # taller: molde, colada y desmolde (4:40, sobra material)
    'cor': ['7658383169061686542', 0.3, 28.1],          # maples de huevo, maceta corazón
    'car': ['7672501914583436576', 0.3, 16.2],          # molde de cartón + pintura a rodillo
    'pie': ['7666355422189718798', 0.3, 15.9],          # maceta forrada en piedras
    'tal': ['7392432458748218629', 0.3, 20.0],          # taller, macetas terminadas
    'bow': ['7638292906297675015', 0.3, 16.8],          # colada en bowl -> maceta con flores

    # ---- con ventana (el texto vive fuera de ella) ----
    'fab': ['7516986350910983480', 0.3, 9.0],           # fábrica de macetas blancas (texto desde s10)
    'fib': ['7558208141406506252', 5.0, 12.8],          # macetas de fibrocemento con plantas (cartel s0-s4)
    'per': ['7649512888075422994', 9.0, 15.0],          # patio con macetas (cartel de tránsito s0-8, placa final s16)
    'hum': ['7637218721341230367', 6.0, 27.0],          # maceta de tela + hortensias ("Humans vs AI" s0-4, cartel s29)
    'zur': ['7268271040793775366', 0.3, 12.0],          # jardineras rectangulares (pasos escritos desde s13)

    # ---- OCR limpio, revisados a mano después ----
    'pat': ['7142980513391742214', 0.5, 57.0],          # macetas blancas en el patio
    'pal': ['7154029409102499114', 0.3, 10.8],          # macetas y bacha sobre pallets
    'fil': ['7248638003000839470', 0.3, 13.4],          # fila de jardineras blancas
    'int': ['7299627252482985221', 0.3, 14.2],          # jardineras con plantas en interior
    'alz': ['7467949774021414149', 0.3, 17.2],          # macetas blancas con plantas + alisado
    'fb2': ['7578817210785893650', 0.3, 10.6],          # fábrica: pilas de macetas y jardineras
    'jar': ['7588863996220984583', 0.3, 12.5],          # jardineras de cemento a estrenar
    'par': ['7597947205458136338', 0.3, 21.1],          # macetas en fila en el parque
    'tel': ['7600003658071149842', 0.5, 58.0],          # taller: tela embebida en cemento
    'rel': ['7633093088914738446', 0.3, 27.5],          # maceta con relieve + suculentas
    'tla': ['7677235828652838165', 0.3, 19.3],          # remera embebida en cemento -> pieza de tela
}

if __name__ == '__main__':
    print(len(VENT), 'clips en el pool')
