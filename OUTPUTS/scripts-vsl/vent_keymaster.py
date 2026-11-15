# -*- coding: utf-8 -*-
"""Ventanas limpias del pool de KeyMaster Hub (ingles, 2026-11-14).

147 clips bajados de #automotivelocksmith. El nicho esta sucio en el mismo sentido que el de
Party Box Vault: casi todo es **video con subtitulo quemado de punta a punta** (el creador
contando el trabajo) y, ademas, **marcas de agua de cerrajerias con telefono**: MENDEZ LOCKSMITH
(23 de 23 cuadros), QUICK KEY LOCKSMITH, CITYWIDE AUTO LOCKSMITH, DALLAS LOCKSMITH, IRON PRO,
YUMAN AUTO KEYS, "Loksmith the wizard" con el 312 399-0516 y "MIDLAND TX EMERGENCY LOCKOUT"
con el 432-248-6243.

Tambien se cayo bastante material en **espanol** (el tag mezcla los dos idiomas): "PIN CODE QUE
ES?" (22 de 22), "Apertura de Ford F150", "Se Habla Espanol", "no sabes que es quedate que te lo
explico".

Lo que SI se deja es el texto del OBJETO, que ademas en este nicho juega a favor: los codigos de
espadin (HON66, HU92, TOY48, HU162T), "2-in-1 Pick", CR2032, CARDOT del remote tester, Milwaukee
PACKOUT de la caja y MaxiIM de la herramienta de Autel. Es exactamente lo que mira un cerrajero.

VENT[clave] = (nombre del archivo sin .mp4, inicio, fin, extras del clip)

Descartados en el control de la hoja de contactos (3 cuadros por ventana): seis con **cara hablando
a camara** (el creador presentandose), dos con **bandas negras** quemadas arriba y abajo, y tres que
no aportaban nada al relato (cielo, un capo estatico y un encuadre ambiguo).
"""
VENT = {
#    'n': ('7664069780214713618', 0.0, 58.0, dict(fam='13618')),   # manos en el tablero — OCR en cero   <-- FUERA: cara a camara
#    'o': ('7628072062770285837', 0.0, 54.0, dict(fam='85837')),   # herramienta en la manija — OCR en cero   <-- FUERA: bandas negras
    'w': ('7484339026904796446', 0.0, 22.5, dict(fam='96446')),   # juego de llaves sobre la mesa — OCR en cero
    'z': ('7664998381315460383', 0.0, 7.9, dict(fam='60383')),   # llave apuntando al auto — OCR en cero
#    'I': ('7598220836343909662', 0.0, 60.0, dict(fam='09662')),   # caja de herramientas abierta — OCR en cero   <-- FUERA: cara a camara
    'a': ('7574102976185388319', 2.0, 62.0, dict(fam='88319')),   # espadin HON66 y ganzua 2-in-1 (texto de objeto)
    'p': ('7245088120885153070', 2.0, 52.0, dict(fam='53070')),   # placa del control + remote tester CARDOT (texto de objeto)
    'x': ('7696855640714661133', 2.5, 14.0, dict(fam='61133')),   # set de espadines HU92 / TOY48 / HU162T (texto de objeto)
#    'M': ('7499223994139184406', 0.0, 60.0, dict(fam='84406')),   # ganzua 2-in-1 trabajando   <-- FUERA: encuadre ambiguo
    'O': ('7613324352175705346', 0.0, 55.0, dict(fam='05346')),   # caja Milwaukee PACKOUT en la van
    'K': ('7607686958575340807', 0.0, 55.0, dict(fam='40807')),   # programadora — MaxiIM entra recien a los 57 s
#    'y': ('7688423256432315670', 0.0, 11.0, dict(fam='15670')),   # herramientas sobre el asiento   <-- FUERA: bandas negras
    'q': ('7466947961562369313', 0.0, 20.0, dict(fam='69313')),   # fresadora azul — TikTok @usuario a los 24 s
    'r': ('7249913207198879019', 16.0, 30.0, dict(fam='79019')),   # cuna en la ventanilla — telefono quemado 0-15 s
    't': ('7588982806097759495', 0.0, 19.0, dict(fam='59495')),   # duplicadora — "Ford" a los 21 s
#    'j': ('7610333979136265502', 8.0, 55.0, dict(fam='65502')),   # llavero y fobs — MIDLAND TX a los 3 y 63 s   <-- FUERA: cara a camara
#    'P': ('7614297180270103839', 0.0, 25.0, dict(fam='03839')),   # interior oscuro — una marca a los 27 s   <-- FUERA: cara a camara
#    'N': ('7463602534985288978', 0.0, 22.0, dict(fam='88978')),   # capo y cerradura — marca a los 24 s   <-- FUERA: capo estatico, no aporta
    'L': ('7495256587615882539', 40.0, 68.0, dict(fam='82539')),   # cuna de aire — AIRSHIM.COM a los 36 s
#    'B': ('7551581186661944606', 10.0, 68.0, dict(fam='44606')),   # ventanilla y herramienta   <-- FUERA: cielo, no aporta
    'F': ('7590570018958593287', 0.0, 55.0, dict(fam='93287')),   # banco de trabajo con el fob abierto
    'H': ('7595225093110779156', 0.0, 50.0, dict(fam='79156')),   # programando desde el asiento
#    'R': ('7652008798105652501', 0.0, 48.0, dict(fam='52501')),   # playa de autos   <-- FUERA: personas y chalecos
#    'D': ('7580484934935121183', 0.0, 55.0, dict(fam='21183')),   # puerta y herramienta   <-- FUERA: cara a camara
    'Q': ('7616134148985457934', 0.0, 50.0, dict(fam='57934')),   # columna de direccion
}

# Las maquetas de la app van como un plano mas del montaje, igual que ellos.
APP = {
    'A1': '../gfx/app-catalogo.png',
    'A2': '../gfx/app-buscando.png',
    'A3': '../gfx/app-ficha.png',
    'A4': '../gfx/app-secciones.png',
}
