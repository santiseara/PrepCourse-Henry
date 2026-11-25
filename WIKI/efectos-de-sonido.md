# Efectos de sonido

> La biblioteca de SFX de Santiago (carpeta de Drive "efectos de sonido", 31 archivos) es **la única fuente de efectos de sonido**. Nada sintetizado, nada descargado de otro lado, nada de los bancos de Higgsfield o ElevenLabs.

## La regla (2026-11-25)

**Cada vez que un video lleve un efecto de sonido, el archivo sale de esta carpeta.** Pedido textual de Santiago: *"Te voy a mandar una carpeta con muchos sonidos, subila al cerebro y usa siempre los sonidos de la carpeta esta"*.

- Fuente en Drive: [efectos de sonido](https://drive.google.com/drive/folders/143Fjg-7aGyRGGPl4aSBB1d8PQ6wE9Uzq) (la comparte Federico Martínez Stupfler, Santiago tiene acceso de lectura).
- **Copia local en la Mac: `/Users/santiagoseara/SFX/`** — los 31 originales tal cual (mp3/wav/flac), bajados el 25/11/2026.
  - `/Users/santiagoseara/SFX/alias/` — 25 versiones **listas para el montaje**: `.wav` 44,1 kHz estéreo, sin el silencio del arranque, recortadas a 0,2–4 s, normalizadas a −16 LUFS con pico −1,5 dB y con fundido de salida de 0,08 s.
- **`OUTPUTS/scripts-vsl/sfx.py` queda retirado.** Los sonidos sintetizados ya no se usan: lo único que ese script tenía y la carpeta no es el **redoble** (`drumroll`), así que si hace falta un redoble se sintetiza y se avisa.
- Esto **no** quiere decir meterle efectos a todo. Siguen valiendo los límites que ya estaban: pocos y en momentos clave (unos 10 por VSL, 3–4 headlines con sonido por ad, ver [[vsl-reglas-de-armado]]) y **cero SFX** en los formatos donde ya estaba prohibido ([[estilo-de-video-ia]] punto 7, [[laboratorio-wow]], [[kit-de-radiestesia]], [[slime-shop-kit]], [[crochet-painting]], [[aromatic-plaster-atelier]]). La regla cambia **de dónde sale el archivo**, no cuántos van.
- Si Santiago suma sonidos nuevos a la carpeta de Drive, se vuelven a bajar a `/Users/santiagoseara/SFX/` antes de la tanda siguiente.

### Registro 2026-11-25 (tarde) — reconfirmada y cableada en el editor
Santiago, al pedir la tanda de [[the-artist-method]]: *"si vas a usar efectos de sonido, tenés la carpeta
subida que te mandé hace poco. Eso marcalo como regla. Siempre que uses efectos de sonido, que sean de la
carpeta de Drive."*
- **La regla ya no depende de que yo me acuerde.** `edit_tam.py` copia `~/SFX/alias/*.wav` a `sfx/` de la
  carpeta temporal y **corta con error** si la biblioteca no está. La llamada a `sfx.py` quedó borrada del
  editor, no solo retirada del papel. Los `edit_*.py` viejos siguen llamando a `sfx.py`: **hay que
  parchearlos igual cuando se usen**.
- La tabla de volúmenes del editor tenía solo 5 sonidos (`chaching`, `ding`, `pop`, `whoosh`, `sello`) y
  reventaba con un `KeyError` al pedir cualquier otro. Ahora cubre 15 y cae a `0.26` por default.
- En esa tanda se usaron **dos**: `papel` cuando entra la lista de proyectos y `ding` en la placa final.
  Nada más, porque el formato es calmo: la regla dice de dónde sale el archivo, no que haya que meter más.

### Registro 2026-11-25 (tarde II) — tercera vez que la pide en el mismo día
Santiago, al pedir la tanda de [[mini-plaster-studio]]: *"si vas a usar efectos de sonido, tenés la
carpeta subida que te mandé hace poco. Eso marcalo como regla. Siempre que uses efectos de sonido, que
sean de la carpeta de Drive."*
- `edit_my.py` nace ya con la biblioteca cableada (hereda de `edit_tam.py`): copia `~/SFX/alias/*.wav`
  y **corta con error** si la carpeta no está. Ningún `edit_*.py` nuevo vuelve a llamar a `sfx.py`.
- En esa tanda se usaron **cinco, uno por video**: `chaching` cuando aparece el precio de venta (V1 y
  V2), `pop` en la tarjeta de los 30 souvenirs (V3), `ding` en la colección de Navidad (V4),
  `llamada` cuando entra el mensaje del cliente (V5) y `tick` en el primer paso del acabado (V6).
  Uno por pieza, en el punto donde el ad cambia de idea.

## Cómo se usa en el montaje

Los editores (`edit_ugc_split.py` y los `edit_*.py` de `OUTPUTS/scripts-vsl/`) leen los efectos de la subcarpeta `sfx/` de la carpeta de trabajo y los buscan **por nombre `.wav`**. Entonces:

```bash
mkdir -p <carpeta-de-trabajo>/sfx
cp /Users/santiagoseara/SFX/alias/*.wav <carpeta-de-trabajo>/sfx/
```

Los nombres de `alias/` son **los mismos que esperaban los scripts** (`ding.wav`, `pop.wav`, `whoosh.wav`, `chaching.wav`, `buzzer.wav`, `sello.wav`, `tick.wav`, `scribble.wav`), así que no hay que tocar ni un script: cambia el contenido, no el nombre.

| alias (lo que pide el script) | sale de | dura | para qué |
|---|---|---|---|
| `chaching.wav` | cash.mp3 | 2,20 s | el precio, la ganancia, el cobro |
| `ding.wav` | ding.mp3 | 1,60 s | tilde, dato que cierra |
| `pop.wav` | efecto de sonido POP.mp3 | 0,76 s | bonos, aparición de un chip |
| `whoosh.wav` | Whoosh Sound Effect.mp3 | 0,64 s | entrada de B-roll |
| `swoosh.wav` | SWOOSH_3.mp3 | 0,64 s | cambio de bloque |
| `buzzer.wav` | error.mp3 | 1,20 s | cada error de una lista |
| `sello.wav` | BOOM SWOOSH.mp3 | 1,60 s | garantía, sello |
| `tick.wav` | click.mp3 | 0,29 s | pregunta de "adiviná", clic |
| `scribble.wav` | teclado.mp3 (desde 6,5 s) | 1,20 s | cuentas, tecleo |
| `impacto.wav` | bullet_hit2.mp3 | 0,48 s | golpe seco |
| `subdrop.wav` | Subdrop Low.MP3 | 2,00 s | caída, revelación grave |
| `boom.wav` | boom.mp3 | 2,50 s | impacto grande |
| `bwong.wav` | Bwongwong.mp3 | 2,00 s | error cómico, "no" |
| `glitch.wav` | GLICH2.mp3 | 1,20 s | corte raro, transición digital |
| `flare.wav` | Lens flare transition.mp3 | 0,71 s | transición con destello |
| `fuego.wav` | Fireball Whoosh.MP3 | 1,74 s | transición fuerte |
| `texto.wav` | Aparición de Texto.MP3 | 1,25 s | headline que entra |
| `papel.wav` | Paper Flip.MP3 | 0,87 s | hoja, PDF, lista |
| `camara.wav` | Camera Shutter.MP3 | 0,61 s | foto, antes/después |
| `camara_fotos.wav` | camara de fotos.mp3 | 2,00 s | ráfaga de fotos |
| `sorpresa.wav` | sorpresa.mp3 | 0,65 s | revelación |
| `burbuja.wav` | burbuja estrella.mp3 | 0,18 s | sticker, burbuja |
| `llamada.wav` | LLAMADA.mp3 | 0,89 s | teléfono, notificación |
| `alarma.wav` | ALARMA CLOCK.mp3 | 2,50 s | despertador, urgencia |
| `grillo.wav` | grillo.mp3 | 4,00 s | silencio incómodo |

Los originales que no tienen alias porque están duplicados: `Swoosh.mp3`, `SWOOSH_1.wav`, `SWOOSH_2.mp3`, `SWOOSH_2.flac`, `SWOOSH_3.mp3`, `Swooshes.wav`, `Woosh (Sound Effect).mp3`. Si hace falta otro swoosh, se saca de ahí.

## Detalles / notas

- **Volumen en la mezcla:** los alias ya están parejos (−16 LUFS), así que las ganancias que usan los editores siguen sirviendo tal cual: `0,9` para el efecto que acompaña un headline, `0,55` para el pop, `0,35` para el whoosh de entrada de B-roll. Nunca por encima de la voz, y la regla de Santiago del 2026-10-14 sigue en pie: *"se hace muy cansador el efecto de sonido, solo los puntos importantes"*.
- **13 de los 31 originales arrancan con silencio** (hasta 6,4 s en el caso de `teclado.mp3`). Por eso existe `alias/`: si se usa el mp3 crudo en un timestamp, el efecto suena tarde o no suena.
- **Nada de esto va al repo.** Son 9,1 MB de binarios: viven en `/Users/santiagoseara/SFX/`, igual que los renders y el b-roll viven en `~/Desktop/<oferta>/` ([[organizacion-y-registro]]).
- Para regenerar los alias desde los originales está el procedimiento arriba (silenceremove + atrim + loudnorm + fade), ejecutado el 25/11.

## Preguntas abiertas

- Falta un **redoble** (`drumroll`) en la carpeta, que `sfx.py` sí tenía y los ads entretenidos de Scented Stones usaban antes de revelar un número.
- Faltan los que pide [[fuga-perfecta]]: **high-five** y **risas**.
- ¿Las camas musicales también pasan a salir de una carpeta fija? Hoy la música sigue siendo `bed_herrero` / `music.py` ([[vsl-reglas-de-armado]] §4b). Santiago habló de *sonidos*, no de música.

## Relacionado

[[vsl-reglas-de-armado]] · [[estilo-de-video-ia]] · [[guiones-y-anuncios]] · [[organizacion-y-registro]] · [[skills-de-video-ia]]

## Fuentes

- Drive: carpeta "efectos de sonido" (143Fjg-7aGyRGGPl4aSBB1d8PQ6wE9Uzq), 31 archivos, bajada el 2026-11-25
- Pedido de Santiago en el chat del 2026-11-25
- `OUTPUTS/scripts-vsl/sfx.py`, `OUTPUTS/scripts-vsl/edit_ugc_split.py`
