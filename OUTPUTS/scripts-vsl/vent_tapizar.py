# -*- coding: utf-8 -*-
"""Ventanas limpias del pool de TikTok de la oferta de tapizado de sillones (2026-11-11).

96 clips bajados de #tapiceria, #tapizado, #reformadesofa y #restauraciondemuebles. El tag
#restauraciondemuebles trae sobre todo **pintura de muebles de madera** (chalk paint), que no es
lo que vendemos: se cayo casi entero por el primer filtro de la regla del 4/11. Tambien se fueron
los de **tapizado de autos**, que en estos tags pesan bastante.

Despues se le paso OCR de Vision cuadro por segundo (`scan_carteles.py`). Se cayeron por marca de
agua del creador: 32262 (@jessicafernanda.ofc, en los 78 segundos) y 87710 (TAPICES FORRY'S, en
los 24 de 26). Y 26999 se cayo en la hoja del render: tenia 34 cuadros con texto de 60, o sea
cartel casi todo el tiempo, y yo le habia recortado la ventana en vez de tirarlo (la regla del
11/11: cuando la proporcion es alta, el clip se cae entero). Siete ventanas arrancan mas tarde porque el cartel del creador vive al principio.

El texto que SI se deja es el del oficio: marcas de herramientas (CONSEW, STANLEY, KOMELON),
etiquetas de tela ("matte", "natural", "PVCouro") y los numeros de una regla.

VENT[clave] = (nombre del archivo sin .mp4, inicio, fin, extras del clip)
"""
VENT = {
    'a': ('7156468334777634050', 0.0, 22.0, dict(fam='34050')),   # sillon blanco retapizado con engrampadora, antes y despues
    'b': ('7205005223297961262', 0.0, 60.0, dict(fam='61262')),   # tapiceria real: estructura con resortes, tela verde, remate
    'c': ('7210339726908312837', 0.0, 16.0, dict(fam='12837')),   # antes y despues de un sillon, marron a azul
    'd': ('7136526604049894702', 0.0, 9.0, dict(fam='94702')),   # cuero del sillon tratado con cera y cepillo
    'e': ('7172370224753200390', 0.0, 31.0, dict(fam='00390')),   # reparacion y retoque de un sillon de cuero oscuro
    'f': ('7345127280580185350', 0.0, 34.0, dict(fam='85350')),   # sillon verde oliva capitone terminado, panoramicas
    'g': ('7350431841385549061', 0.0, 33.0, dict(fam='49061')),   # estructura, espuma y el sillon blanco ya armado
    'h': ('7361865130176548102', 0.0, 45.0, dict(fam='48102')),   # espuma rosa montada sobre la estructura
    'i': ('7361904759701425454', 0.0, 19.0, dict(fam='25454')),   # sillon negro terminado, colocado en el living
    'j': ('7425424792494427398', 0.0, 30.0, dict(fam='27398')),   # sillones boucle blancos, montaje de patas
    'k': ('7428422180733537542', 8.0, 20.0, dict(fam='37542')),   # relleno de un sillon azul (0-7 s marca de CapCut, 21 s cartel del creador)
    'l': ('7434258232178134305', 0.0, 23.0, dict(fam='34305')),   # limpieza y aspirado profundo de un sillon claro
    'n': ('7469781941223476486', 0.0, 17.0, dict(fam='76486')),   # engrampadora neumatica sobre la estructura, plano del oficio
    'o': ('7379999598451969285', 0.0, 175.0, dict(fam='69285')),   # asiento redondo tapizado: medir con regla, engrampar, rematar
    'p': ('7405749784356654341', 4.0, 64.0, dict(fam='54341')),   # cinchas sobre la estructura y rollos de tela (0-3 s dice "Parte 2")
    'r': ('7414323918724435206', 8.0, 20.0, dict(fam='35206')),   # sillon gris capitone terminado (cartel a los 4 s y a los 21 s)
    's': ('7483231886483967263', 0.0, 62.0, dict(fam='67263')),   # detalle del perforado y la costura de un sillon de cuero
    't': ('7492292983124004138', 0.0, 230.0, dict(fam='04138')),   # restauracion de un sillon de cuero marron, de principio a fin
    'u': ('7502095977369586966', 0.0, 270.0, dict(fam='86966')),   # tapiceria de un sillon blanco: espuma, tela y engrampadora
    'w': ('7558682894990871838', 0.0, 56.0, dict(fam='71838')),   # sillon antiguo desarmado y retapizado en amarillo capitone
    'x': ('7570454319145995538', 0.0, 60.0, dict(fam='95538')),   # puff redondo tapizado en fucsia capitone
}
