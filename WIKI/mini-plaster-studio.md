# Mini Plaster Studio (yesitos para pintar, mercado inglés)

> Oferta de **figuritas de yeso para pintar armadas en kits** (party favors, souvenirs, cumpleaños),
> modelada de **Mini Yesitos para Pintar** (`miniyesitos.brujulanegocios.com`, fanpage *Creaciones con
> Alma*, Argentina) para correr en inglés en US/CA/AU/UK/NZ. Pedido de Santiago del 25/11/2026.
> Análisis completo del competidor y del mercado inglés en
> `OUTPUTS/2026-11-25-analisis-mini-yesitos-y-mercado-ingles.md`.

## Ideas clave
- **El original está vivo y escalando.** ~61 ads activos, el más viejo del 28/10/2026, con tandas
  nuevas el 2, 10, 14, 15, 16, 18 y **24/11**. Una sola fanpage, una sola landing, un solo producto.
- **No vende "hacer yeso", vende convertir la figura en un producto que se vende de a 30.** Su ángulo
  nº1 (los tres ads de más impresiones) es **packaging y valor percibido**: *"mismas figuras, distinto
  packaging, ¿cuál comprarías?"*. Y los dos primeros son **estáticos**, no videos.
- **El mercado inglés está un nivel entero atrás.** El producto físico se vende muy bien (PYO plaster
  kits: US$ 4-6 el kit en Etsy, US$ 29 el starter de 20, mayorista en Faire, góndola en Hobby Lobby),
  pero **el infoproducto no existe**: solo dos PDF sueltos de Etsy (US$ 9,15 y US$ 12,20) **sin un solo
  anuncio corriendo**. Nadie enseña el negocio con Meta Ads.
- **Lo que ya funciona en inglés y conviene robar:** *"the party bag filler parents are switching to"*,
  *"the perfect alternative to plastic throwaway toys"*, *"party favors kids actually use"*,
  *"non-toxic, washable paints"*, *"orders need 2-3 weeks lead time"*.
- **Ocasiones que el argentino no nombra y en inglés pagan:** class parties, teacher gifts, VBS y
  summer camps, school fundraisers, Easter, Halloween, Valentine's class gifts, holiday craft fairs.

## Nuestra oferta
- **Mini Plaster Studio** (nombre propuesto por Claude el 25/11; **pendiente de que Santiago lo
  confirme o lo cambie** — si lo cambia solo hay que rehacer la placa final).
- 30 colecciones · 50 ideas de kits · 5 bonos · **garantía de 30 días** contra los 7 del original.
- ⚠️ **Pendiente: no tiene landing todavía.** Los videos cierran con placa MINI PLASTER STUDIO y
  "Tap Learn more". Falta precio (sugerido US$ 19,99 de US$ 97), checkout, dominio y backend.

## El formato de video (copiado del ganador, medido cuadro a cuadro)
9:16 · 37-51 s · b-roll real de manos colando yeso, desmoldando y armando kits, **ni una foto fija**
([[estilo-de-video-ia]]) · voz en off femenina · cama musical activa por debajo · **subtítulos de 2
palabras**: la que no suena en **amarillo pálido #FFFFA8** con borde negro y la que **suena en pastilla
FUCSIA #EE57B8** con letra blanca · **tarjetas crema #FEFDF8** con el número grande · placa final
MINI PLASTER STUDIO con botón fucsia.

⛔ **Su b-roll no se puede reusar:** lleva la marca de agua *"CA · Creaciones con Alma"* **centrada y
semitransparente en todo el cuadro**. No se recorta como el watermark de pie de
[[ingles-mapas-mentales]]: está en el medio. Por eso el visual sale **entero de TikTok**.

## Tanda 1 (2026-11-25): 6 guiones y 6 videos
Guiones en `OUTPUTS/2026-11-25-guiones-mini-plaster-studio-tanda1.md` (EN + ES voseo completos, más
el texto principal único en inglés). Cinco modelados sobre sus ángulos ganadores y uno que ataca el
hueco inglés:

1. Packaging y valor percibido ($4 contra $12, las mismas figuras) — *su ángulo nº1*
2. Se venden en packs de 30, no de a uno + la cuenta de los materiales — *su nº2*
3. El souvenir que no termina en la basura / un cumple por fin de semana — *su nº6 + el inglés*
4. Navidad: 29 días, un pedido son 30 kits — *su nº4, la mejor ventana del año*
5. "Necesito 25 kits para el sábado, ¿cuánto?" — *su nº7*
6. Los tres pasos del acabado — *su nº9, y el hueco inglés: nadie explica el mecanismo*

**Banco:** "si empezara de cero", "no le vendas solo a las mamás", "cada año piden otra figura",
"menos pantallas más arte".

## Producción
- **Voz: Sulafat**, estilo de mujer norteamericana hablando rápido y vivo a volumen normal (el de
  [[fuga-perfecta]] traducido, con los negativos explícitos). V1, V2, V3 y V6 por API
  (`gemini-3.1-flash-tts-preview` y `gemini-2.5-flash-preview-tts`); **V4 y V5 por AI Studio desde su
  Chrome**, porque la cuota de API del día ya se había ido en [[the-artist-method]].
  Los seis a 194-214 ppm en crudo y -15 a -19 dB: ninguno susurra. Normalizados a -16 LUFS.
- **Pool:** clips de TikTok de `#yesitosparapintar`, `#yesitos`, `#gessinhosparapintar`,
  `#moldesdesilicona` y `#plastercraft`.
- **Efectos de sonido:** de `~/SFX/alias` ([[efectos-de-sonido]]), uno por video.
- **Cama musical: la pista que mandó Santiago**, `nastelbom-advertising-424209` (Pixabay, 256 kbps),
  guardada en `~/Desktop/mini-yesitos/anuncios/work/music/`. Se toma **desde el segundo 20**, que es
  donde el arreglo está en pleno, 55 s con fundidos, pasa-altos a 70 Hz y dos huecos suaves
  (−3 dB en 450 Hz y −2,5 dB en 2,6 kHz) para que no pelee con la voz.
- Scripts: `OUTPUTS/scripts-vsl/gen_my_plans.py`, `edit_my.py`, `ventanas_yesitos.py`.
- Carpeta: `~/Desktop/mini-yesitos/` con `anuncios/`, `imagenes/` y `landing/`.
- **Entregados en el Drive** ([[organizacion-y-registro]]): `Mi unidad / Ebook Dami / Ebook Mini Plaster
  Studio (INGLES) / Videos terminados`, los seis con el nombre del arranque de su hook — *Same five
  figures* · *They dont sell one at a time* · *The party favor that doesnt end up in the bin* ·
  *29 days to Christmas* · *I need 25 kits by Saturday* · *Its not the mold its the finish*.
  https://drive.google.com/drive/folders/1rrJRA3rXtODPIBbT8f8Sy7NSwQf3RnkW
  Masteres en `~/Desktop/mini-yesitos/anuncios/` como `25-11 - 1` a `25-11 - 6` (42 a 49 s).

## ⚠️ El `music_db` del editor NO es la distancia a la voz que uno escucha (registro 2026-11-25)
Santiago pidió *"que se escuche pero que no tape la voz"*. El editor escala la música contra el **RMS
de toda la pista de voz**, que incluye las pausas y las colas bajas, así que el número del plan queda
**4 dB corto** respecto de lo que se oye sobre el habla.
- Medido en esta tanda: con `music_db -11` la música quedaba **15,2 dB por debajo del habla real**
  (inaudible); con `-7` quedaba en −11,2 dB y Santiago pidió *"bajale un poco, un poco nada más"*.
  **Quedó en `-9`, que da −13 dB sobre el habla**: esa es la referencia para la próxima tanda.
- **Cómo se verifica, sin oír nada:** se leen `vo.wav` y `music.wav` de la carpeta `_tmp` del render,
  se toman solo las muestras donde `|voz| > 0,02` (el habla de verdad) y se compara el RMS de las dos.
  **Objetivo −13 dB** (lo que aprobó Santiago). Los seis de esta tanda dieron entre −12,8 y −13,8.
  Un escalón de 2 dB en el plan es lo que él llama *"un poco"*.
- Es la hermana de la regla de [[laser-profit-vault]] del mismo día, donde a −11 Santiago tampoco la
  escuchaba y hubo que subir a −9.

## Preguntas abiertas
- **¿El nombre queda en Mini Plaster Studio?**
- ¿Se arma la landing? Hoy los ads no tienen dónde caer.
- ¿Se corre también una tanda de **estáticos de comparación**? Es su ángulo nº1 y lo corre como foto.
- ¿El backend sale del molde de los 4 OTOs de [[scented-stones]]?

## Relacionado
[[arte-en-yeso-y-cemento]] · [[aromatic-plaster-atelier]] · [[scented-stones]] · [[party-box-vault]] ·
[[funnel-hacking]] · [[internacionalizacion]] · [[guiones-y-anuncios]] · [[efectos-de-sonido]] ·
[[testeo-de-creativos]]

## Fuentes
- Biblioteca de Anuncios de Meta, fanpage Creaciones con Alma (61 ads, 13 videos transcriptos el 2026-11-25)
- miniyesitos.brujulanegocios.com (landing completa, 2026-11-25)
- Etsy, Faire, notonthehighstreet y Hobby Lobby (precios del producto físico en inglés, 2026-11-25)
- OUTPUTS/2026-11-25-analisis-mini-yesitos-y-mercado-ingles.md
