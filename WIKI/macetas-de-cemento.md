# Macetas de cemento (Argentina)

> Oferta argentina de macetas de cemento que se clona de **Aula Digital 360** (`auladigital360.shop`),
> una ballena con **58 ads activos** corriendo desde el 12/10/2026. Manual para fabricar y vender
> macetas de cemento desde casa, AR$ 16.990, 3 bonos y garantía de 7 días.
> (fuente: Biblioteca de anuncios de Meta y la landing del competidor, consultadas el 2026-11-17)

## El competidor que se clona
- **58 ads activos**, todos video, todos al mismo dominio. La oferta viene escalando desde el 12 de
  octubre y sigue sumando creativos (los últimos arrancaron el 14/11).
- **Un solo texto principal para los 58**: *"Emprende fabricando macetas de cemento desde tu casa…"*,
  título `80% off + 3 libros gratis de regalo`, chip de prueba social `+1000 alumnos activos`.
  Confirma otra vez la regla: lo único que rota es el video.
- **Cuatro formatos**: el de **31 s** (18 ads, el ganador), uno de **26 s**, uno de **20 s** y el
  **audio de WhatsApp** de 51 s a 1:15 (9 ads).
- La Biblioteca sirve los previews a 360×640; no es la resolución que suben.

## Su oferta (landing)
- **Jorge Ramos**, "8 años fabricando, +3.000 macetas por año". Precio de anclaje: **una maceta de
  cemento sale $48.000 en el vivero** (en los ads lo suben a $59.000–$60.000).
- **AR$ 84.950 → AR$ 16.990**, pago único por Mercado Pago, garantía de 7 días, "+1.000 alumnos".
- **3 bonos gratis**: pack de planos ($49.990), pinturas y texturas premium ($39.900), plantas para
  cada maceta ($29.990). Valor total declarado: $204.830.
- Mecanismo: *solo arena y cemento*, una mesa alcanza, moldes caseros, los errores que hacen tirar
  plata, todo por escrito para leer en el celular.
- Escasez: "lanzamiento de un solo día, mañana vuelve a AR$ 84.950".

## Su guion ganador (31 s, reconstruido del subtitulado quemado)
> Empecé haciendo una maceta para mi casa, hoy vendo más de 40 por mes. Pedí una linda para mi ficus,
> vi el precio y estaban más de 60.000 pesos. Dije: esto es arena y cemento, la hago yo. La puse en el
> patio de adelante y mi vecina me preguntó dónde la había comprado. Le dije que la hice yo y enseguida
> me dijo: haceme una que te la pago. Lo que me ordenó todo fue este manual paso a paso: solo arena y
> cemento, qué molde usar, cómo publicarlas, venderlas y qué errores evitar. Solo por hoy tenés 80 % de
> descuento y te llevás tres libros adicionales totalmente gratis. Clic en descargar y aprovechá la
> oferta antes de que suba el precio.

Los otros tres formatos son **el mismo cuerpo con otro hook**: *"No quise pagar 60.000 pesos por una
maceta, hoy soy yo la que las vende"* (20 s) y *"Si sabés mezclar arena con agua, ya sabés hacer algo
que la gente paga"* (35 s). El de 1:15 es un **audio de WhatsApp a Jorge** de una alumna.

## Su edición (lo que se copió tal cual)
- **Chips fijos arriba a la izquierda** durante todo el video, en tres juegos que rotan por creativo:
  1. azul `fabrica y emprende con macetas de cemento`
  2. azul `1 maceta de cemento = $60.000` + rojo `aprendé a fabricarlas y a venderlas desde 0.` + rojo `Descargá nuestra guía 👇`
  3. rojo `APRENDÉ A FABRICAR MACETAS DE CEMENTO DESDE CERO` + azul `1 maceta de cemento: $60.000` + azul `inversión = $4.500`
- **Subtítulos** de 3 palabras, mayúscula, blancos con borde negro grueso y la palabra que suena
  adentro de una **caja roja o verde**, alternando los dos colores dentro del mismo video.
- **100 % b-roll de macetas**, voz en off de mujer y una cama musical por debajo (no tienen un solo
  silencio bajo -45 dB). Sin placa final, sin insertos, sin caja de hook.
- Usan clips de TikTok **con la marca de agua puesta** (se les cuela `MAKE & REBORN` en varios ads).
  Nosotros no.

## Nuestra tanda 1 (6 ads + 2 fotos, 17/11)
`OUTPUTS/2026-11-17-guiones-macetas-cemento-tanda1.md`. Un hook por familia, cuerpo casi calcado,
porque Santiago pidió *"los guiones cambialos un poco pero tampoco tanto"*.
1. La vecina (clon del ganador) · 2. No quise pagar · 3. Si sabés mezclar · 4. Audio de WhatsApp ·
5. La de los Estados · 6. Lo que cuesta hacerla.
- **Voz:** Sulafat por API, estilo rioplatense, `speed 1.20`. La V4 salió con `gemini-3.1-flash-tts-preview`
  porque el 2.5 se quedó sin cuota a mitad de la tanda.
- **Scripts:** `gfx_macetas.py` (chips), `vent_macetas.py` (pool), `gen_macetas_plans.py`, `edit_macetas.py`.
- **Las 2 fotos** salen de los dos planos que más se repiten en sus videos, con sus chips y su titular:
  `gfx_fotos_macetas.py`.

## El pool de TikTok
201 clips de `#macetasdecemento`, `#concreteplanter` y del perfil `@ali.diyideas`. **Entraron 28.**
El plano insignia de Aula Digital es el clip `7678821416162184478` de **@ali.diyideas** (la mujer de
remera negra, el globo azul y la maceta de tela blanca con moño amarillo): es el mismo que corre en
sus ads, limpio y en 1080×1920. Detalle de por qué se cayó cada uno: `OUTPUTS/scripts-vsl/vent_macetas.py`.

## Entrega
- **Videos:** `~/Desktop/macetas-cemento/anuncios/17-11 - N · <hook>.mp4` (6, de 30 a 44 s, 6,6 a 9,4 MB).
  No subieron al Drive: `file_upload` corta arriba de ~800 KB ([[organizacion-y-registro]], 17/11).
- **Fotos:** las 2 sí están en `Mi unidad / Ebook Dami / Ebook Macetas de Cemento (AR) / Videos terminados`.
- Los masters en alta y el pool quedan en `anuncios/work/`.

## Preguntas abiertas
- ¿Santiago ya tiene landing propia para esta oferta en AR? Los guiones salieron del vocabulario del
  competidor; si la landing propia dice otra cosa, hay que alinear los entregables que nombra la voz.
- El backend (OTOs) todavía no se armó: se clona del molde de [[scented-stones]].

## Relacionado
[[from-concrete-to-cash]] · [[bachas-de-concreto]] · [[guiones-y-anuncios]] · [[funnel-hacking]] · [[modelo-low-ticket]]

## Fuentes
- Biblioteca de anuncios de Meta, búsqueda por `www.auladigital360.shop`, Argentina (2026-11-17)
- Landing `auladigital360.shop` (2026-11-17)
