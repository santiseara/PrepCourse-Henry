# -*- coding: utf-8 -*-
"""Ventanas limpias del pool de TikTok de The Plaster & Concrete Guide (2026-11-13).

75 clips de #jesmonite, #plastercrafts, #concretecandle, #terrazzotray y #plasterofparis.
OCR de Vision a 1 cuadro cada 2 s sobre los primeros 28 s: 33 sin una letra, 30 pasaron la revision
visual. Se cayeron ademas 7188316949430963462 (chicos bailando), 7522949727738957078 (marca "AA" fija
abajo) y 7690850905687657780 (lienzo texturado, no es una pieza).
Los clips largos se cortan en 26 s porque la revision llega hasta ahi.
VENT[clave] = (id, desde, hasta, extras)
"""
VENT = {
 '922497': ('7129652038710922497', 0.0, 26.0, {}),   # yeso y agua medidos en bol azul
 '803141': ('7212508479351803141', 0.0, 17.0, {}),   # colado verde menta y desmolde de portavela
 '581957': ('7213499423991581957', 0.0, 13.5, {}),   # chips en bandeja ovalada + colado
 '677703': ('7233756424671677703', 0.0, 26.0, {}),   # terrazo verde: pigmentos y bandeja moteada
 '145178': ('7245365938072145178', 0.0, 7.5, {}),    # colado en molde redondo + plato terrazo
 '026657': ('7264128626164026657', 0.0, 26.0, {}),   # masa rosa y mesa con piezas deco
 '736709': ('7266320175253736709', 0.0, 14.0, {}),   # bandeja con marmolado negro
 '319841': ('7293597661943319841', 0.0, 26.0, {}),   # moldes bundt y mini figuras
 '032353': ('7297659259939032353', 0.0, 26.0, {}),   # bandeja con manchas de color
 '285857': ('7341358179378285857', 0.0, 18.5, {}),   # globo verde como molde
 '535393': ('7359275250703535393', 0.0, 22.5, {}),   # pigmento negro y colado gris de cemento
 '734917': ('7360828342481734917', 0.0, 16.5, {}),   # lijado y piezas moteadas: el acabado
 '892229': ('7400490493831892229', 0.0, 10.5, {}),   # jarron, bandeja y cuentas terminadas
 '845921': ('7416374371259845921', 0.0, 16.0, {}),   # vela negra con pan de oro
 '388256': ('7417360935666388256', 0.0, 10.5, {}),   # globo rosa y calabaza de yeso
 '708807': ('7438892499625708807', 0.0, 19.0, {}),   # vaso de vela con pan de oro
 '609878': ('7502372432867609878', 0.0, 26.0, {}),   # agregado granulado y bandeja texturada
 '085134': ('7522631263858085134', 0.0, 16.5, {}),   # mezcla, lijado y huevo de yeso
 '234517': ('7613561127108234517', 0.0, 6.5, {}),    # molde con figuras y piezas secandose
 '934542': ('7642551377754934542', 0.0, 26.0, {}),   # colado en molde de silicona: tanda entera
 '934674': ('7671328069096934674', 0.0, 15.0, {}),   # portavela esferico con la vela encendida
 '848658': ('7672812203048848658', 0.0, 14.0, {}),   # vasitos de papel y piezas con encaje
 '711506': ('7677101576015711506', 0.0, 26.0, {}),   # molde de osito y mini figura
 '704007': ('7685421326684704007', 0.0, 26.0, {}),   # los chips rotos a mano y mezclados
 '483488': ('7701615653794483488', 0.0, 25.0, {}),   # velas en vaso de piedra con musgo
 '463456': ('7702258669907463456', 0.0, 26.0, {}),   # velas cilindricas con corteza
 '735623': ('7704548121182735623', 0.0, 18.5, {}),   # molde rosa y figura desmoldada
 '684365': ('7706868232631684365', 0.0, 26.0, {}),   # tags redondos de yeso
 '841813': ('7707017187323841813', 8.0, 26.0, {}),   # mezcla de cemento gris (antes hay cara a camara)
 '661782': ('7707377880912661782', 0.0, 26.0, {}),   # globo azul con vendas de yeso
}
