# -*- coding: utf-8 -*-
"""Ventanas limpias de los clips de TikTok del pool de The Party Box Vault (2026-11-10).

Pool bajado de #partyfavorbox, #explosionbox, #treatboxes y #papercraftbusiness (84 clips,
43 revisados con hoja de contactos de 6 cuadros + la mitad inferior grande de cada uno).

Se cayeron por texto quemado en ingles de punta a punta: 94443 ("Paper Sized Used", "Box Size
7x4x3"), 48481 ("He said he got a surprise for me"), 22890 ("Spidey and Friends Party Favor
Boxes"), 17041 ("2ND LAYER 4", "Cross again and tie a ribbon"), 71398 ("folding party favor box
loading"), 26710 ("Diy explosion box"), 79169 ("explosion box for dad"), 91178 (el de la
impresora Epson: la leyenda "Birthday Party Prep" entra a los pocos segundos y es el unico
tramo util). Por idioma: 25462 (subtitulos en espanol). Por cartel que no se va nunca: 22591 ("TOY STORY PARTY
FAVOR BOXES" arriba a la izquierda, lo atrapo la hoja del render a los 30 s) y 14198, el tutorial largo de la caja
de carton, que sigue tirando carteles a los 35 s ("Cut another square with added 5cm on each side").
Por marca de agua
centrada que el zoom no alcanza: 52020 (chapa redonda con @usuario en la mitad inferior). Por contradecir el guion:
06878, que muestra la Cricut trabajando cuando el ad dice que no hace falta maquina de corte.
17285 se cayo porque no hay una caja en todo el clip (mariposas de papel).

Despues de dos renders sucios se le paso OCR (Vision, 1 cuadro por segundo) a todas las ventanas:
ahi aparecieron los carteles blancos sobre fondo claro que la hoja de contactos no muestra
("TOY STORY PARTY FAVOR BOXES" en 78094, "KAWAII THEME party favor boxes" en 17451, "Party Favor
boxes" en 49663, "kiddie party favor inspo" en 23598, "Hobby Lobby cardstock" en 51246) y la marca
de agua "Kgoodessentials", que esta en los 70 segundos de 33119 y lo tira entero.

VENT[clave] = (nombre del archivo sin .mp4, inicio, fin, extras del clip)
"""
VENT = {
    # --- limpios de punta a punta ---
    # (los que arrancan despues de 0 llevan el segundo en el que muere el cartel del creador,
    #  medido con OCR de Vision cuadro por cuadro, no a ojo)
    'a': ('7195029783942597931', 0.0, 52.0, dict(fam='stassie')),        # caja personalizada con nombre en relieve
    'b': ('7371939664804023598', 3.0, 59.0, dict(fam='gianistoys')),     # llenando cajitas con juguetes
    'c': ('7376706943748017451', 5.0, 56.0, dict(fam='aria')),           # cajitas rosas ARIA, nombre y confeti
    'd': ('7382393772681792814', 0.0, 29.0, dict(fam='loveyou')),        # caja explosion negra con fotos
    'e': ('7460873668156149038', 0.0, 48.0, dict(fam='valentine')),      # explosion de San Valentin, rojo
    'f': ('7467319804207156522', 0.0, 109.0, dict(fam='scrapbox')),      # explosion scrapbook verde y rojo
    'g': ('7469969112870178094', 3.0, 46.0, dict(fam='livanstory')),     # cajas kraft, rotulado y llenado
    'h': ('7494053689909349663', 7.0, 29.0, dict(fam='mesa')),           # linea de armado sobre la mesa
    'i': ('7502184081241771310', 0.0, 15.0, dict(fam='pawpatrol')),      # cajitas Paw Patrol llenas, plano heroe
    'j': ('7518885099920805142', 0.0, 18.0, dict(fam='goldbow')),        # explosion de chocolates con mono dorado
    'k': ('7527778425914789150', 0.0, 68.0, dict(fam='jazmyn')),         # caja Daisy, recorte y pegado
    'l': ('7582302014399466766', 0.0, 19.0, dict(fam='huntrix')),        # gable box violeta terminada, al sol
    'm': ('7593800428677090591', 0.0, 7.0, dict(fam='marcos')),          # armado de la gable box impresa
    'n': ('7597921886541991199', 0.0, 22.0, dict(fam='pinkexpl')),       # explosion rosa con golosinas
    'o': ('7611806371016740126', 0.0, 18.0, dict(fam='blackgold')),      # cajitas negro y oro de cumpleanos
    'p': ('7614041751795436808', 0.0, 13.0, dict(fam='pinkchoc')),       # explosion rosa con chocolates
    'q': ('7621669292144102686', 5.0, 24.0, dict(fam='carebears')),      # gable boxes Care Bears de colores
    'r': ('7630744151889317150', 0.0, 18.0, dict(fam='moneybox')),       # cajitas negras y oro con billetes
    's': ('7641809693186411806', 0.0, 10.5, dict(fam='cars')),           # cajitas Cars con nombre, plano heroe
    't': ('7649555068928265502', 0.0, 8.5, dict(fam='milani')),          # gable box rosa TWO con mono
    'u': ('7672146435697151246', 5.0, 17.5, dict(fam='diecut')),         # piezas troqueladas sobre la mesa
    'v': ('7704114899319852306', 0.0, 20.0, dict(fam='blueexpl')),       # explosion azul y negra con galletas

    # --- con cartel del creador al principio: arrancan despues ---
    'w': ('7236583771590397230', 12.0, 81.0, dict(fam='amazonfavors')),   # cajitas de autos (0-8 s dice AMAZON PARTY FAVORS)
    'x': ('7317149883436207406', 3.0, 12.0, dict(fam='diygift')),        # gift box pastel (0-3 s dice DIY GIFT BOX)
    'A': ('7544748403683609887', 10.0, 58.0, dict(fam='sofiastoys')),    # kraft SOFIA'S TOYS (el tapete Cricut se lee al principio)
    'C': ('7599112610776141086', 28.0, 110.0, dict(fam='giftidea')),     # monos y flores de papel (dice Gift idea hasta los 22 s)
    'D': ('7705865571413298445', 30.0, 59.0, dict(fam='eliascrane')),    # gable box de obra (hasta 28 s trabaja la Cricut)

    # --- recortado por lo que entra al final ---
    'E': ('7504319570245700906', 0.0, 8.0, dict(fam='mykoturns')),       # hojas impresas y etiquetas (a los 9 s abre un split)
}
