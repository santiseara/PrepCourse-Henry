# -*- coding: utf-8 -*-
"""Ventanas limpias del pool de TikTok de la oferta de displays de papel (2026-11-11).

95 clips bajados de #displaydefesta, #displaydepapel, #paineldefesta y #displaydenatal.
El tag es engañoso: "display" en TikTok trae sobre todo **expositores de carton de punto de
venta** y **paneles de MDF**, que no son lo que vendemos. El filtro de la regla del 4/11
(¿se ve lo que vendemos?) dejo afuera dos tercios del pool.

Despues se le paso OCR de Vision a cuadro por segundo (`scan_carteles.py`). Se cayeron por
marca de agua del creador: 69781 (@minifestajardimencantado), 43973 (HELENA),
34053 (@lorenamoraesarts), 94290 (@VIVI_DANDODICAS + "Assistam ate o final").
Por cartel quemado de punta a punta: 27781, 53176 ("Eu mesma faco meus displays de Festa"),
24054 ("3 secretos") y, ya en la hoja del render, 19925 ("um detalhe que faz diferenca na sua
decoracao de natal") y 37326 ("Christmas lovers are obsessed with it"): en los dos el cartel seguia
vivo despues del segundo en el que yo habia abierto la ventana. Y en varios clips el OCR mostro tramos de **captura de pantalla** que la
hoja de contactos no delataba (el dialogo de impresion de la Epson en 60422, el Rasterbator en
52629 y una publicacion de Mercado Livre con precios): esos tramos quedaron fuera de la ventana,
porque la regla prohibe la captura de pantalla como plano.

El texto que SI se deja es el del producto: el nombre recortado en papel ("Sarah"), "PAW PATROL",
"ROBLOX", "ROUTE 66" y los "Feliz Natal" impresos en los paneles.

VENT[clave] = (nombre del archivo sin .mp4, inicio, fin, extras del clip)
"""
VENT = {
    # --- limpios de punta a punta ---
    'a': ('7200805607979388165', 0.0, 14.0, dict(fam='dino')),        # mujer armando un dinosaurio gigante rosa
    'c': ('7381673385878719750', 0.0, 15.0, dict(fam='pawcolgados')), # recortes de Paw Patrol colgados, recien impresos
    'h': ('7390551504114994437', 4.0, 18.0, dict(fam='safari')),      # 0-3 s dice "Displays Mdf Safari"; fila de displays safari de tamano real
    'k': ('7536277715226299654', 0.0, 17.0, dict(fam='backnavidad')), # escenario navideno impreso, bastones y regalos
    'm': ('7602288385704627474', 3.0, 18.0, dict(fam='cars')),        # display de Cars y semaforo sobre la mesa
    'q': ('7630110064413576466', 0.0, 55.0, dict(fam='sarah')),       # el nombre "Sarah" recortado a mano en papel
    'u': ('7680490871179070740', 0.0, 32.0, dict(fam='casanavidad')), # casa con Papa Noel y bastones gigantes afuera
    'w': ('7682846720056773896', 0.0, 8.0, dict(fam='feliznatal')),   # panel impreso "Feliz Natal" con la mesa servida
    'y': ('7702655190825979157', 0.0, 10.0, dict(fam='comunion')),    # panel impreso de comunion, gigante
    'A': ('7702481800764935438', 0.0, 20.0, dict(fam='arbol')),       # arbol de navidad armado en el living

    # --- recortados: el cartel o la captura de pantalla viven afuera de la ventana ---
    'b': ('7301316436016860422', 60.0, 175.0, dict(fam='luigi')),     # 0-57 s es el dialogo de impresion de la Epson
    'd': ('7483943414535605509', 0.0, 48.0, dict(fam='castillo')),    # a los 50 s entra la marca "silkart"
    'i': ('7317647989638581510', 45.0, 88.0, dict(fam='luigi2')),     # 0-44 s es captura de pantalla
    'p': ('7620413737853390101', 25.0, 64.0, dict(fam='pawarmado')),  # 0-24 s es el Rasterbator en la laptop
    'r': ('7658854280933264648', 12.0, 30.0, dict(fam='futbolista')), # 0-11 s se lee la grabadora laser; a los 33 s entra un volante de imprenta
    's': ('7665444817870015752', 10.0, 98.0, dict(fam='powerpuff')),  # 0-9 s dice "MEUS PRIMEIROS DISPLAYS"
    't': ('7677363517216869650', 5.0, 50.0, dict(fam='graduada')),    # 0-4 s dice "Display de mesa"
    'v': ('7681890476122852629', 155.0, 230.0, dict(fam='pooh')),     # hasta 132 s es el Rasterbator; 233-235 s es Mercado Livre con precios
    'z': ('7703001815066938631', 4.0, 19.0, dict(fam='roblox')),      # 0-3 s dice "Painel Roblox"
}
