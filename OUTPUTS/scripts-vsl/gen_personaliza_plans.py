import json
T = '../tiktoks/'
clips = {'A': T + '7515357859094498590.mp4',   # xtool: camiseta negra, film, impresora, prensa, despegue, empaque (sin 9.3-11.6 ni 16+: marca)
         'B': T + '7497737253460938015.mp4',   # hellcat: transfer rojo, prensa, camiseta terminada
         'C': T + '7489234063988051255.mp4',   # legionmenace: buzo, prensa, doblado
         'D': T + '7301003737177345286.mp4',   # estampadoscolombia: prensa + brilla en la oscuridad (sin 0-10: caras y logo)
         'E': T + '7595239375164804360.mp4',   # transfera: despegue del transfer del perro
         'F': T + '7654028825654840584.mp4'}   # mastevale: buzo crema, plancha chica, empaque (negro desde 38 s)
R = {'A': [[0, 2.3], [2.3, 5.0], [5.0, 7.8], [7.6, 9.3], [11.6, 14.0], [13.9, 16.0]],
     'B': [[0, 3], [3.3, 6.3], [6.9, 9.9], [12.9, 15.9]],
     'C': [[0, 2.8], [5.5, 8.5], [8.7, 11.7], [11.7, 15.4]],
     'D': [[13.5, 16.5], [16.8, 19.8], [23.6, 26.9]],
     'E': [[0, 2.6], [2.5, 5.5], [5.5, 9.8]],
     'F': [[0, 3], [3, 6], [6, 9], [9, 12], [12, 15], [15, 18], [18, 21], [21, 24], [24, 27], [27, 30], [30, 33], [33, 36.5]]}
C = {k: {'src': v} for k, v in clips.items()}
POOL = [[k, a, b] for k in R for a, b in R[k]]
for i in range(22):
    k = f'L{i:02d}'
    C[k] = {'src': f'../landing/img{i:02d}.webp', 'still': True, 'fit': i < 17}
GEN_STILLS = ['L00', 'L02', 'L06', 'L07', 'L09', 'L10']
POOL += [[k, 0, 3] for k in C if k.startswith('L')]
def plan(n, hook, anchors, overlays, seed, sfx=()):
    keys = set(GEN_STILLS) | {a[2] for a in anchors if a[2].startswith('L')}
    pool = [p for p in POOL if not p[0].startswith('L') or p[0] in keys]
    P = {'vo': f'../vo/V{n}.wav', 'script': f'../vo/V{n}.txt', 'speed': 1.15, 'lang': 'es', 'clips': C, 'pool': pool,
         'usage': 'usage.json', 'seed': seed, 'hook': hook, 'anchors': anchors, 'overlays': overlays, 'whoosh': [1],
         'cut': [1.8, 2.4, 3.0], 'sfx': list(sfx), 'accent': [236, 72, 120], 'brand': ['PERSONALIZA ', 'Y VENDE'],
         'end_sub': 'Guía + 500.000 diseños + 5 bonos'}
    json.dump(P, open(f'V{n}.json', 'w'), indent=1, ensure_ascii=False)
END = lambda word, cta='Toca Más información 👇', occ=0: {'type': 'end', 'word': word, 'occ': occ, 'cta': cta}

plan(1, 'Mi esposo se rió de esto 😅',
     [['Mi', 0, 'E', 5.5], ['camisetas', 0, 'A', 0], ['doblar', 0, 'C', 11.7], ['casa.', 0, 'L07', 0], ['transfer', 0, 'E', 0],
      ['imprimes,', 0, 'A', 2.3], ['despegas.', 0, 'E', 2.5], ['tienda.', 0, 'L06', 0], ['sobrina', 0, 'L10', 0], ['mamás', 0, 'L18', 0],
      ['quinientos', 0, 'L12', 0], ['primer', 0, 'F', 33], ['Toca', 0, 'B', 12.9]],
     [{'type': 'chip', 'text': '$300 extra este mes', 'icon': '💵', 'word': 'trescientos', 'dur': 2.2},
      {'type': 'chip', 'text': 'La plancha de la ropa', 'icon': '✓', 'word': 'plancha', 'dur': 2.0},
      {'type': 'chip', 'text': '+500.000 diseños listos', 'icon': '🎨', 'word': 'quinientos', 'dur': 2.2},
      END('Toca', 'Toca Más información 👇')], 11, sfx=[['chaching', 'dólares', 0]])

plan(2, 'Del sábado al lunes: mi primer pedido 📦',
     [['El', 0, 'E', 5.5], ['guía,', 0, 'L13', 0], ['diseño', 0, 'L09', 0], ['papelería', 0, 'A', 2.3], ['camiseta', 0, 'A', 0],
      ['calor,', 0, 'B', 6.9], ['despegué...', 0, 'E', 2.5], ['WhatsApp.', 0, 'L19', 0], ['cuatro', 0, 'L10', 0],
      ['máquina,', 0, 'F', 18], ['semana,', 0, 'C', 11.7], ['Toca', 0, 'F', 33]],
     [{'type': 'chip', 'text': 'Sábado: aprendí', 'icon': '📖', 'word': 'sábado', 'occ': 1, 'dur': 2.0},
      {'type': 'chip', 'text': 'Domingo: la foto', 'icon': '📸', 'word': 'domingo', 'dur': 2.0},
      {'type': 'chip', 'text': 'Lunes: primer pedido', 'icon': '📦', 'word': 'lunes', 'occ': 1, 'dur': 2.0},
      {'type': 'chip', 'text': '$12 cada una', 'icon': '💵', 'word': 'doce', 'dur': 1.8},
      END('Toca', 'Toca el botón de abajo 👇')], 22, sfx=[['chaching', 'doce', 0]])

plan(3, '¿Cuánto ganas con una camiseta? 👀',
     [['Haz', 0, 'A', 0], ['transfer,', 0, 'E', 0], ['mascota,', 0, 'E', 5.5], ['minutos.', 0, 'B', 6.9], ['equipo', 0, 'L10', 0],
      ['bolsas', 0, 'L00', 0], ['cojines,', 0, 'L06', 0], ['plancha', 0, 'F', 15], ['guía', 0, 'L12', 0], ['baratísima,', 0, 'L16', 0],
      ['link', 0, 'C', 11.7]],
     [{'type': 'chip', 'text': 'Camiseta lisa: $4', 'icon': '✓', 'word': 'cuatro', 'dur': 1.8},
      {'type': 'chip', 'text': 'Transfer: menos de $1', 'icon': '✓', 'word': 'transfer,', 'dur': 1.8},
      {'type': 'price', 'label': 'CAMISETA PERSONALIZADA', 'title': 'Se vende entre', 'price': '$12 – $15', 'foot': 'Con nombre, foto o diseño', 'word': 'doce', 'dur': 2.6},
      {'type': 'chip', 'text': '+$150 en una tarde', 'icon': '💵', 'word': 'ciento', 'dur': 2.2},
      END('link', 'El link está abajo 👇')], 33, sfx=[['chaching', 'ciento', 0]])

plan(4, '3 errores que arruinan tu estampado ⚠️',
     [['Tres', 0, 'B', 12.9], ['vapor', 1, 'F', 12], ['seco', 0, 'F', 15], ['mesa', 0, 'F', 9], ['despegar', 0, 'E', 0],
      ['frío,', 0, 'E', 2.5], ['principio.', 0, 'C', 5.5], ['guía', 0, 'L13', 0], ['bono', 0, 'L15', 0], ['lavada', 0, 'L10', 0],
      ['quinientos', 0, 'L12', 0], ['Toca', 1, 'E', 5.5]],
     [{'type': 'chip', 'text': 'Error 1: plancha con vapor', 'icon': '✕', 'word': 'Uno:', 'dur': 2.2},
      {'type': 'chip', 'text': 'Error 2: la tabla de planchar', 'icon': '✕', 'word': 'Dos:', 'dur': 2.2},
      {'type': 'chip', 'text': 'Error 3: despegar a destiempo', 'icon': '✕', 'word': 'Tres:', 'occ': 1, 'dur': 2.2},
      {'type': 'chip', 'text': 'Bono: soluciones', 'icon': '🎁', 'word': 'bono', 'dur': 2.0},
      END('Toca', 'Toca Más información 👇', occ=1)], 44)

plan(5, 'Empaca conmigo este pedido 🛍️',
     [['Empaca', 0, 'F', 33], ['bolsas', 0, 'L04', 0], ['WhatsApp.', 0, 'L20', 0], ['bolsa', 0, 'L03', 0], ['bebé.', 0, 'L05', 0],
      ['comedor,', 0, 'F', 21], ['plancha', 0, 'F', 15], ['bautizo', 0, 'L11', 0], ['Navidad', 0, 'L09', 0], ['guía', 0, 'L12', 0],
      ['precios.', 0, 'L16', 0], ['toca', 0, 'A', 13.9]],
     [{'type': 'chip', 'text': '24 bolsas · baby shower', 'icon': '🛍️', 'word': 'veinticuatro', 'dur': 2.2},
      {'type': 'price', 'label': 'PEDIDO BABY SHOWER', 'title': 'Ganancia de una tarde', 'price': '$120', 'foot': '24 bolsas · costo $2 · venta $7', 'word': 'ciento', 'dur': 2.8},
      {'type': 'chip', 'text': 'Próximo pedido: bautizo', 'icon': '📦', 'word': 'bautizo', 'dur': 2.0},
      {'type': 'chip', 'text': 'Se viene diciembre', 'icon': '🎄', 'word': 'Navidad', 'dur': 2.0},
      END('toca', 'Toca Más información 👇')], 55)

plan(6, 'Empecé haciendo un regalo 🎁',
     [['Empecé', 0, 'L01', 0], ['camiseta', 0, 'L10', 0], ['amigos...', 0, 'B', 12.9], ['pedidos', 0, 'F', 33], ['máquina', 0, 'B', 6.9],
      ['plancha', 0, 'F', 15], ['diseñar.', 0, 'L09', 0], ['quinientos', 0, 'L12', 0], ['impresora?', 0, 'A', 2.3],
      ['noches,', 0, 'D', 13.5], ['garantía.', 0, 'L14', 0], ['camiseta.', 1, 'E', 5.5], ['Toca', 0, 'A', 13.9]],
     [{'type': 'chip', 'text': 'Sin máquina cara', 'icon': '✓', 'word': 'No.', 'dur': 2.0},
      {'type': 'chip', 'text': 'Sin saber diseñar', 'icon': '✓', 'word': 'Tampoco:', 'dur': 2.0},
      {'type': 'chip', 'text': '¿Sin impresora? A la papelería', 'icon': '✓', 'word': 'mandas', 'dur': 2.2},
      {'type': 'chip', 'text': '14 días de garantía', 'icon': '🛡️', 'word': 'garantía.', 'dur': 2.0},
      END('Toca', 'Toca el botón de abajo 👇')], 66)
print('ok')
