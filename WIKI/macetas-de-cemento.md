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
- **Las 2 fotos** (`gfx_fotos_macetas.py`): ver abajo cómo se midió cuáles son.

## El pool de TikTok
201 clips de `#macetasdecemento`, `#concreteplanter` y del perfil `@ali.diyideas`. **Entraron 28.**
El plano insignia de Aula Digital es el clip `7678821416162184478` de **@ali.diyideas** (la mujer de
remera negra, el globo azul y la maceta de tela blanca con moño amarillo): es el mismo que corre en
sus ads, limpio y en 1080×1920. Detalle de por qué se cayó cada uno: `OUTPUTS/scripts-vsl/vent_macetas.py`.

## Las 2 fotos: cómo se eligieron
Santiago pidió *"las 2 que más repetidas tenga la página original"*. Con el filtro **Imágenes** la
Biblioteca devuelve **cero** ads de Aula Digital: los 58 son video. Así que "las 2 imágenes" se midieron
sobre los **58 posters** (el cuadro de portada de cada ad): se bajaron los 58, se les sacó hash
perceptual de 12×12 y se agruparon por distancia de Hamming ≤ 12. Los dos grupos más grandes tienen
**seis ads cada uno**:

1. la mujer del vivero levantando una **matera negra grande**, con las macetas blancas al costado;
2. la misma mujer poniendo un **ficus en una maceta blanca grande**, en el mismo vivero.

Las dos son del mismo creador de TikTok, **@materos_pertuz** (vivero de Bucaramanga), y las dos se
consiguieron **limpias y sin su texto** de los clips originales: `7600598138956696840` @20,6 s y
`7467949774021414149` @1,2 s. Vienen en 576×1024, así que se escalan con Lanczos y un unsharp suave,
y salen en **1080×1920** (recortarlas a 4:5 le cortaba la cabeza a la del vivero).

🐞 **Primero las hice mal:** las armé con cuadros del clip de @ali.diyideas que usa el *video*, no con
las imágenes que más repite la *página*. Regla: "las más repetidas" se **cuenta**, no se estima a ojo.

## Entrega
Todo en `Mi unidad / Ebook Dami / Ebook Macetas de Cemento (AR) / Videos terminados`: los 6 videos y las
2 fotos. Los MP4 se subieron **troceados en partes de 700 KB** y recompuestos en el navegador, porque
`file_upload` corta arriba de ~800 KB; los seis SHA-256 quedaron idénticos a los del disco
([[organizacion-y-registro]], 17/11). Copia local en `~/Desktop/macetas-cemento/anuncios/`; los masters
en alta y el pool, en `anuncios/work/`.

## Preguntas abiertas
- ¿Santiago ya tiene landing propia para esta oferta en AR? Los guiones salieron del vocabulario del
  competidor; si la landing propia dice otra cosa, hay que alinear los entregables que nombra la voz.
- El backend (OTOs) todavía no se armó: se clona del molde de [[scented-stones]].

## Relacionado
[[from-concrete-to-cash]] · [[bachas-de-concreto]] · [[guiones-y-anuncios]] · [[funnel-hacking]] · [[modelo-low-ticket]]

## Fuentes
- Biblioteca de anuncios de Meta, búsqueda por `www.auladigital360.shop`, Argentina (2026-11-17)
- Landing `auladigital360.shop` (2026-11-17)
