# -*- coding: utf-8 -*-
"""Ventanas limpias del pool de TikTok de From Concrete to Cash (2026-11-11).

Pool bajado de #concreteplanter, #cementplanter, #concretepot y #concretecrafts (75 clips).
OCR de Vision a 1 cuadro cada 2 s sobre los primeros 26 s de los 75: 35 sin una letra, 40 con texto.

Se cayeron enteros por marca de agua o cartel de punta a punta (regla del 11/11: cuando la cuenta
del OCR dice N de N, el clip se cae entero): 256901 (@manosalconcreto, 13/13, ademas en espanol),
129502 ("WE POURED / THICK", 12/12), 538527 ("MAKE & REBORN", 11/11), 877294 (10/10), 218795
("LUA+STONE", 8/8), 301831 (7/7), 350150 ("DIY CONCRETE GARDEN POT" + polaco, 6/6), 902305 (4/4),
575646 ("ATRIUM CRAFT" en la remera y en placa), 317662 y 625694 (porta velas, no macetas),
838165 ("INNA FRAME"), 051213, 203854, 695713 y 579021 ("The Timelapse Builder"), 451021/986573
("BUZZQO"), 531086 ("sereneDly"), 147350 (epoxi), 904462 ("Build A Space").

Se cayeron por NO mostrar el producto: 848299 y 262081 (bandejas y posavasos), 903455 (cabeza de
leon), 884758 (vereda estampada), 586922 y 784225 (banco y mesa de concreto), 193813 (posavasos),
355533 (tortuga), 065606 (molde de silicona), 956587 (porta velas de AD), 318925 (estanteria de
bloques), 776910 (bordura de pasto sin pieza).

🆕 Se cayeron por ser video generado con IA: 436576, 321950, 596558, 060054, 263519, 007455,
995744, 135520, 198049, 184478, 314766, 577184, 311118. El tag #concreteplanter esta tomado por
cuentas de "satisfying DIY" hechas con IA (globos que salen perfectos, gente impecable, procesos
imposibles). Se reconocen por el proceso que no puede pasar y por la piel y la ropa sin una mancha.

Formato: clave -> (archivo, desde, hasta, extras)
"""
# 🆕 El cartel semitransparente "Dont waste money / Instead..." de 47606 sigue vivo despues de los 4 s
# y el OCR cada 2 s no lo vio: aparecio en la hoja de contactos del render. El clip se cayo entero.
VENT.update({
    # --- vivero / produccion real: el producto terminado en cantidad ---
    'a': ('7154029409102499114', 0.0, 11.0, {'fam': 'vivero'}),      # bowls grandes en el patio de venta
    'b': ('7248638003000839470', 0.0, 13.6, {'fam': 'vivero'}),      # jardineras largas en fila
    # --- proceso en casa, persona real ---
    'c': ('7634929390056377613', 0.0, 25.8, {'fam': 'bolsas'}),      # molde de bolsas de arena en el garage
    'd': ('7639099719993658638', 0.0, 24.0, {'fam': 'sandia'}),      # molde de sandia -> bowls con suculentas
    'e': ('7657581272167927053', 0.0, 26.0, {'fam': 'cajon'}),       # molde de cajon, taller
    'f': ('7658383169061686542', 0.0, 28.3, {'fam': 'maple'}),       # molde de maples de huevo
    'g': ('7659504081995648270', 0.0, 28.9, {'fam': 'corazon'}),     # molde de carton + maceta calada
    'h': ('7665159540706512142', 0.0, 27.7, {'fam': 'flor'}),        # moldes de flor, pintadas
    'i': ('7666355422189718798', 0.0, 16.0, {'fam': 'piedras'}),     # cajon + piedras pegadas
    'j': ('7694578423347285270', 0.0, 15.8, {'fam': 'paraguas'}),    # molde de paraguas
    'k': ('7630881719054388502', 0.0, 21.8, {'fam': 'toalla'}),      # toalla sobre balde, taller con macetas
    'l': ('7678755000666869000', 0.0, 10.4, {'fam': 'paraguas2'}),   # paraguas + piedras; despues de 10,5 s es un fogon encendido, no una maceta
    'm': ('7682811526025153805', 0.0, 14.9, {'fam': 'bolsa'}),       # bolsa de nylon -> maceta con moño
    # --- manos, mesa, piezas chicas (planos de detalle) ---
    'n': ('7672812203048848658', 0.0, 14.2, {'fam': 'vasitos'}),     # vasos de papel + puntilla
    'o': ('7676148635658128658', 0.0, 11.2, {'fam': 'media'}),       # media como molde; el final es la maceta encendida como farol, de noche
    'p': ('7677260746358623509', 0.0, 12.6, {'fam': 'puntilla'}),    # maceta rosa con puntilla
    'q': ('7120592176064548101', 0.0, 20.0, {'fam': 'bowl'}),        # bowl de vidrio; a los 22,5 s entra un cartel de TV
    # --- con ventana por cartel del creador ---
    's': ('7652279454286236942', 0.0, 11.0, {'fam': 'maple2'}),      # "Designs" a los 12,5 s
    't': ('7679840829208317202', 4.0, 13.7, {'fam': 'formline'}),    # la caja "FORMLINE" se lee hasta los 3 s
})
