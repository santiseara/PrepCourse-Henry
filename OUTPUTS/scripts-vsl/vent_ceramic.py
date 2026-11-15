# -*- coding: utf-8 -*-
"""Ventanas limpias del pool de The Ceramic Glaze Recipe Bible (mercado ingles, 2026-11-15).

24 clips revisados con hoja de contactos (6 cuadros por clip) de #potteryglaze, #glazing,
#ceramicglaze y #kilnopening. El nicho de ceramica es de los mas lindos que vimos: manos,
piezas y esmalte, casi todo filmado con buena luz y sin cara.

Lo que se cayo (8): "before VS after GLAZE", "Glaze Reveal", "my favorite glaze combo" y
"before glazing / after glazing" (texto quemado de punta a punta), la creadora hablando a
camara con los nombres de los esmaltes comerciales encima, y un clip con la marca AMACO
escrita abajo, justo donde van nuestros subtitulos.

Lo que SI entra con texto es el clip 'm': los potes de esmalte comprado (AMACO Flux Blossom,
Smokey Merlot). Es texto de objeto y ademas es el VILLANO del guion: el frasco que se acaba.

VENT[clave] = (id del archivo, inicio, fin, extras)
"""
VENT = {
    'a': ('7472072150770289942', 0.0, 15.2, dict(fam='89942')),   # pincel sobre bowl texturado, esponja y resultado
    'b': ('7598200400973483295', 0.0, 60.0, dict(fam='83295')),   # vaso en mano: esmaltado, inmersion y brillo final
    'c': ('7609318191659093278', 0.0, 66.0, dict(fam='93278')),   # piezas pastel pintadas con pincel
    'd': ('7611566578206903583', 0.0, 68.0, dict(fam='03583')),   # vasos de barro rojo esmaltados con pincel
    'e': ('7691248283263569183', 0.0, 42.0, dict(fam='69183')),   # vaso rosa: inmersion y rosa brillante final
    'f': ('7580241089689308471', 0.0, 13.5, dict(fam='08471')),   # obvara: la espuma de burbujas sobre la pieza
    'g': ('7443481313752927534', 14.0, 61.0, dict(fam='27534')),  # inmersion en el balde + bowl con flores (desde 14 s: antes se ve la cara)
    'h': ('7589716851895176503', 0.0, 24.6, dict(fam='76503b')),  # plato con pinza dentro del balde + platos pintados
    'i': ('7502173052139031813', 3.5, 19.5, dict(fam='31813')),  # taza borgona con pincel (el 'Let's glaze this thumb cup' esta en los primeros 3 s)
    'j': ('7538471990580071702', 29.0, 33.4, dict(fam='71702')),  # SOLO el plano final: el 'green tea x2' quemado llega hasta los 28 s
    'k': ('7597623991368437023', 6.0, 31.5, dict(fam='37023')),   # lirios pintados sobre el jarron
    'l': ('7688829406105668895', 9.0, 15.0, dict(fam='68895')),  # SOLO el aerografo y el final: antes hay cara a camara y textos grises
    'm': ('7640937007681768725', 6.0, 20.0, dict(fam='68725'), ), # LOS FRASCOS COMPRADOS: el villano del guion
    'n': ('7420120310411840800', 18.0, 24.0, dict(fam='40800')),  # bowl verde terminado (texto hasta los 17 s)
    'o': ('7474688973307268407', 6.0, 16.8, dict(fam='68407')),   # pincel sobre pieza celeste
    #   'p': ('7693695104376179998', 2.0, 10.3, dict(fam='79998')),   # FUERA: 'before'/'after' quemado casi todo el clip
    'q': ('7553326241101876503', 10.0, 21.6, dict(fam='76503a')), # bowl verde moteado en la mano (texto hasta los 9 s)
}
VENT = {k: (v[0], v[1], v[2], v[3]) for k, v in VENT.items() if v[2] > v[1]}
