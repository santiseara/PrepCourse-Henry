# Displays de papel - renovaciones del 12/11 (R1, R2, R3)

Renovacion, no tanda nueva: el CUERPO del guion 1 del 11/11 (la imprenta escondida) va copiado
textual y solo cambia el hook, con tres formatos distintos. Es el angulo que Decorarina mas
replica en portugues y en espanol: la comunicacion que el mercado ya valido.

| # | Hook | Formato | Archivo | Duracion |
|---|---|---|---|---|
| R1 | La hoja tamano carta contra el dinosaurio de dos metros | Demo con el objeto en la mano | 12-11 - 1.mp4 | 37,9 s |
| R2 | Cuatro anos decorando fiestas sin pisar una imprenta | Declaracion de autoridad | 12-11 - 2.mp4 | 41,1 s |
| R3 | De que esta hecho el leon de tamano real que tengo detras | Pregunta-acertijo | 12-11 - 3.mp4 | 33,6 s |

---

Guion 1

Esto es una hoja tamaño carta. Y esto que está detrás de mí es un dinosaurio de dos metros.
Salió del mismo paquete de hojas, de una impresora de escritorio y de una tarde en la mesa del comedor. Nadie que lo ve de frente se da cuenta: todos creen que lo mandé a hacer afuera.
Lo único que cambia es la técnica: cómo se parte la imagen, cómo se configura la impresora una sola vez, dónde caen las uniones para que no se vean y cómo se le pone la base para que quede parado solo.
Son hojas, cinta y una impresora común. Nada de plotter, nada de sublimación, nada de esperar tres días a que la imprenta te entregue.
El paso a paso completo está en video, con el banco de casi dos mil imágenes listas para usar.
Haz clic en el botón de abajo y arma el primero esta semana.

Guion 2

Hace cuatro años que vivo de decorar fiestas y nunca mandé una sola pieza a la imprenta.
Ni el oso de dos metros, ni las letras del fondo de fotos, ni los personajes de tamaño real. Todo salió de una impresora de escritorio, en mi casa, y ningún cliente me preguntó nunca de dónde venía.
Lo único que cambia es la técnica: cómo se parte la imagen, cómo se configura la impresora una sola vez, dónde caen las uniones para que no se vean y cómo se le pone la base para que quede parado solo.
Son hojas, cinta y una impresora común. Nada de plotter, nada de sublimación, nada de esperar tres días a que la imprenta te entregue.
El paso a paso completo está en video, con el banco de casi dos mil imágenes listas para usar.
Haz clic en el botón de abajo y arma el primero esta semana.

Guion 3

¿De qué crees que está hecho el león de tamaño real que tengo detrás?
No es cartón, no es madera y no vino de ninguna imprenta. Son hojas de impresora, pegadas una al lado de la otra y cortadas en la mesa de mi casa.
Lo único que cambia es la técnica: cómo se parte la imagen, cómo se configura la impresora una sola vez, dónde caen las uniones para que no se vean y cómo se le pone la base para que quede parado solo.
Son hojas, cinta y una impresora común. Nada de plotter, nada de sublimación, nada de esperar tres días a que la imprenta te entregue.
El paso a paso completo está en video, con el banco de casi dos mil imágenes listas para usar.
Haz clic en el botón de abajo y arma el primero esta semana.

---

## Nombres de la tanda

12/11 - 1   La hoja contra el dinosaurio
12/11 - 2   Cuatro anos sin pisar una imprenta
12/11 - 3   De que esta hecho el leon

## Donde termina el hook y empieza el cuerpo

El hook del guion 1 eran las dos primeras frases (la mama que pregunta en que imprenta + "nadie se
da cuenta"). El cuerpo arranca donde arranca el producto: "Lo unico que cambia es la tecnica".
Los tres hooks nuevos cierran preparando esa bisagra, asi que el cuerpo entra textual y no queda
hablando de algo que nadie dijo.

## Por que estos tres formatos

El checklist del 27/10 pide formatos distintos, no el mismo hook con otro objeto. La tanda del
11/11 ya uso: pregunta de clienta, la cuenta, la escalera de tamanos, la temporada, la objecion
("no se disenar") y el pedido rechazado.

- **R1 - demo con el objeto en la mano.** La hoja y la pieza de dos metros en el mismo plano. Es
  el unico formato que prueba la promesa antes de explicarla.
- **R2 - declaracion de autoridad.** Cuatro anos de oficio y cero imprenta. Ataca la credibilidad,
  no el precio ni la tecnica.
- **R3 - pregunta-acertijo.** Abre con una pregunta al espectador y la respuesta descarta carton y
  madera, que es lo primero que piensa cualquiera que ve un display de dos metros (y es, ademas,
  lo que de verdad venden la mitad de los competidores de TikTok).

## Que cambio en la estetica

Una renovacion que se ve igual la recibe igual el segmento saturado:

- La caja de la palabra activa pasa de **tinta azul noche** a **naranja quemado**.
- Cortes mas rapidos: **1,6 / 2,0 / 2,5 s** en vez de 1,9 / 2,4 / 2,9 (promedio 2,0 s por plano).
- **Ni un clip nuevo bajado.** La ventana de muestreo se corrio **+1,45 s** con tramos de 2,4 s y
  tope de 10 por clip: 145 recortes nuevos, **ninguno** coincide con los 6 videos del 11/11.
- Insertos repartidos distinto: R1 lleva tamanos + celular + biblioteca, R2 abre con el de costos
  y suma el panel "lo que hay en la mesa", R3 solo tamanos + biblioteca.

## Lo que saco la revision del render (y queda vetado para siempre)

La hoja de contactos de los tres videos terminados, a un cuadro cada 1,1 s:

- **Clip s, 59-71 s:** una bolsa naranja **"SUPORTE PARA BALAO - MEDIO"**, en portugues, grande y
  legible en el borde de la mesa. Habia caido justo en el hook de R1. El OCR de la tanda 1 no la
  marco porque no es un cartel: es un envase.
- **Clip r, 27-30 s:** la **silueta de MDF pelada** que el tipo levanta con la mano. Es exactamente
  lo que decimos que no es. En R3, que abre con "no es carton, no es madera", estaba a los 5 s.
- **Clip b, 133-153 s:** el **carton de "maizena"** con la marca impresa, usado de base.

Los tres quedaron en el `VETO` de `gen_displays_ren_plans.py` y los videos se rehicieron.

## Scripts

`OUTPUTS/scripts-vsl/gen_displays_ren_plans.py` + `edit_displays.py`. Voz Sulafat por API
(`gemini-2.5-flash-preview-tts`) con el mismo Style de la tanda 1, a speed 1,30.

## Relacionado
[[displays-de-papel]] · [[renovacion-de-creativos]] · [[guiones-y-anuncios]]

## Fuentes
- OUTPUTS/2026-11-11-guiones-displays-de-papel-tanda1.md
- OUTPUTS/2026-11-11-visuales-tiktok-displays-de-papel.md
