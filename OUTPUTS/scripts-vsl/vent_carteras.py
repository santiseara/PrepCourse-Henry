# -*- coding: utf-8 -*-
"""Ventanas limpias de los clips de TikTok del pool de Carteras Maison (2026-11-10).

Revisadas con hoja de contactos a 1 cuadro cada 1,5 s. Todas las ventanas terminan a los 27 s
como maximo, que es hasta donde llega la hoja; lo que pasa despues no se uso.

Se cayeron, de 60 bajados: los de cara hablando a camara (49200, 57306, 51375, 02497, 90764,
05882, 24238, 10808, 63918), los de subtitulo o cartel quemado de punta a punta (31141, 83535,
92595, 68749, 06188, 06204, 05000, 05002), los de marca de agua centrada que el zoom no alcanza
(28652 @Yariart, 95491 y 96348 @ateliejoanafernandes, 83511 "K pay", 25576 YouTube Shorts,
75059 Hanoure Art + InShOt), los que promocionan su propio curso o kit (93981 "TUTORIAL COMPLETO
EN MI CANAL", 96165 "Comenta MALLA y aprende", 02092 y 02831 "Aprende ingresando al link de mi
perfil" --el 02831 lo atrapo recien el cuadro del segundo 44--, 70172 "SEMINARIO PRESENCIAL de
Plastic Canvas", 79153, 05200 TheevCreation "DM/WHATSAPP TO ORDER"), los que no muestran el
producto (91031 un cesto, 48200 cuadraditos de otono, 49184) y los de calidad mala (71334, 77911).

VENT[clave] = (nombre del archivo sin .mp4, inicio, fin, extras del clip)
"""
VENT = {
    # --- limpios de punta a punta ---
    't': ('7624164455089311007', 0.0, 27.0, dict(fam='negra')),        # ⭐ la cartera negra de boutique, proceso entero
    's': ('7704502682119064853', 0.0, 10.5, dict(fam='negracadena')),  # negra terminada con cadena dorada
    'b': ('7217348138456190234', 0.0, 27.0, dict(fam='rosaproc')),     # rosa: del rollo a los paneles
    'k': ('7631237010509827335', 0.0, 27.0, dict(fam='bordomacro')),   # macro: la puntada bordo sobre el canamazo
    'n': ('7665713894572297490', 0.0, 27.0, dict(fam='cremamacro')),   # macro: el remate crema, agujero por agujero
    'q': ('7523614648701062431', 0.0, 27.0, dict(fam='cisne')),        # verde con el cisne, armado y terminada
    'a': ('7170019206409506094', 0.0, 19.0, dict(fam='frutilla')),     # tote de frutillas, panel y terminada
    'c': ('7405542893319998725', 0.0, 18.0, dict(fam='violeta')),      # violeta trenzada ("it's even better" entra a los 19,5)
    'e': ('7584156498603904278', 0.0, 6.0, dict(fam='mariposa')),      # bordo con mariposa y perlas, de estudio
    'm': ('7657631318854913288', 3.2, 19.0, dict(fam='verdeclutch')),  # clutch verde ("10 hours of work" hasta los 3)
    'o': ('7693352163975662878', 0.0, 19.0, dict(fam='ciervo', zoom=1.30, ybias=1.0)),   # roja con ciervo ("100% Handmade" arriba)
    # --- recortados por texto al principio ---
    'f': ('7595270382798605590', 3.0, 27.0, dict(fam='salvia')),       # verde salvia + forro de flores (texto rumano hasta los 3)
    'g': ('7597963433937505543', 3.0, 17.5, dict(fam='merceria')),     # la merceria: pilas de planchas de canamazo
    'i': ('7618937464962452743', 3.5, 27.0, dict(fam='bordoproc')),    # bordo: cuadradito a cuadradito (cara hasta los 3)
    'l': ('7651711802862079254', 3.5, 27.0, dict(fam='forro')),        # el forro cosido a mano (cartel italiano hasta los 3)
    'd': ('7486075916255284502', 18.0, 27.0, dict(fam='empaque')),     # la beige terminada y su caja (subtitulo ingles hasta los 18)
    'r': ('7632355904033180936', 5.0, 27.0, dict(fam='perlas')),       # perlas cosidas al canamazo (cara hasta los 4,5)
    'u': ('6891671517755755781', 3.0, 27.0, dict(fam='corte')),        # medir, cortar y limar el canamazo
    'v': ('7401857359758232850', 4.0, 27.0, dict(fam='menta')),        # menta: la puntada que llena el panel
    # --- con marca arriba: zoom 1.30 y ybias 1.0 ---
    'h': ('7610362208538725639', 0.0, 27.0, dict(fam='linn', zoom=1.30, ybias=1.0)),
    'p': ('7698587004321139975', 0.0, 27.0, dict(fam='linn', zoom=1.30, ybias=1.0)),
    'j': ('7626794981478632711', 0.0, 27.0, dict(fam='capcut', zoom=1.30, ybias=1.0)),
}
