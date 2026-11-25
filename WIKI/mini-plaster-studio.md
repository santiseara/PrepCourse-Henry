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
- **Efectos de sonido:** de `~/SFX/alias` ([[efectos-de-sonido]]), pocos y en puntos clave.
- Scripts: `OUTPUTS/scripts-vsl/gen_my_plans.py`, `edit_my.py`, `ventanas_yesitos.py`.
- Carpeta: `~/Desktop/mini-yesitos/` con `anuncios/`, `imagenes/` y `landing/`.

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
