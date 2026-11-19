# The Aromatic Plaster Atelier

> Oferta nueva para **mercado inglés** (19/11/2026), clonada de *Manualidades con Propósito*
> (emprendecontusmanos.com, Argentina) y apalancada en la DNA de [[scented-stones]].
> El nombre lo puso Santiago: **The Aromatic Plaster Atelier**.
> (fuente: Biblioteca de Anuncios de Meta, page id 1135159816352814, leída el 19/11/2026)

## Ficha
| Campo | Valor |
|---|---|
| Mercado | 🇬🇧 Inglés |
| Producto | Ebook + videos paso a paso: **piedras aromáticas, tags perfumados, flores difusoras y portavelas** de yeso cerámico |
| Mecanismo | Yeso cerámico + fragancia + molde de silicona. Sin horno, sin llama, sin enchufe. Se recarga con gotas de esencia |
| Avatar | Mujer que quiere un ingreso extra desde su cocina, sin querer "tener un negocio" |
| Tanda 1 | 6 guiones, `OUTPUTS/2026-11-19-guiones-aromatizadores-EN-tanda1.md` |
| Carpeta | `~/Desktop/aromatizadores/` |

## Qué la separa de [[scented-stones]]
Piedras vende **una** pieza. Esta vende **cuatro**: tags para el placard y el auto, piedras para
el cajón, **flores difusoras** (la flor se apoya sobre un frasquito con líquido aromático, una
soga de algodón lo sube, el yeso lo absorbe y perfuma un ambiente entero) y portavelas.
Esa variedad es el hook del ad ganador de ellos: *"todos estos productos están hechos con el
mismo material"*.

## 🕵️ El ganador que se clona
**Manualidades con Propósito** — 7 ads activos al 19/11, el más viejo del **22/10**.
Landing: tienda Shopify con 7 infoproductos; el principal a **$17.999 ARS** (~US$ 12), ancla
$719.999, **75 % OFF**, 6 bonos, 2 masterclass, garantía de 7 días, acceso inmediato.
Entregables con nombre propio: *Emprende con Aromatizadores Decorativos*, *Guía Premium de
Materiales y Proveedores*, *Calculadora de Costos y Precios*, *Colecciones y Kits que Venden*,
*20 Colecciones Listas para Vender*, *Sistema Profesional de Control de Calidad*.

### Las 6 estructuras de guion que corren (transcritas las 7)
1. **Un solo material** (22/10 y 18/11, el de más impresiones y el más nuevo). *"Aunque no lo
   parezca, todos estos productos están hechos con el mismo material"* → lista de piezas →
   qué son (absorben y liberan aroma) → menos de 24 h y materiales accesibles → dónde van
   (baño, placard, cajón, escritorio, auto) → el libro desde cero → CTA + 75 % off.
2. **Una es una cosa, cien es otra.** *"Hacer una piedra aromática es una cosa, pero que te
   encarguen 100 iguales para un evento es otra historia"* → souvenir de casamientos,
   cumpleaños, bautismos, baby showers → una técnica, muchas piezas → libro → CTA.
3. **Las tres formas de aromatizar** (59 s, educativo). Tags vs piedras vs flores difusoras,
   con el mecanismo de la flor explicado → entregables con nombre → CTA.
4. **La mesada de mi cocina** (fundadora). Probó un emprendimiento tras otro, miedo, la primera
   pieza que sale entera del molde, armó el método, *"casi 3.000 mujeres"* → CTA suave.
   Es el guion 2 de [[scented-stones]] ("nunca quise un negocio") con otra ropa.
5. **La chica de los souvenirs** (tercera persona). *"Esta chica tuvo una idea de negocio
   brillante"* → souvenirs que no terminan en la basura → virales → libro → CTA.
6. **¿Dónde los compraste?** (23 s, el más corto). La pregunta cuando regala uno, no le creen
   que los hizo ella → parecen premium → libro → CTA. Es el guion 3 de piedras (reacción de un
   tercero).

### Su edición, medida (se copia tal cual)
- 9:16, **23 a 59 s**, voz en off de mujer cálida, cama musical por debajo. Sin SFX.
- **Sin caja de hook, sin fichas, sin placa oscura, sin botón.** El peso está en el b-roll.
- **Subtítulos**: mayúscula, sans **bold itálica** (Montserrat ExtraBold itálica sirve), blancos
  con borde negro grueso, **2-3 palabras por renglón y hasta 3 renglones**, centrados en el
  tercio inferior (~73 % de alto), y **la palabra que suena en ROSA FUCSIA** — texto de color,
  sin caja. Los ads viejos (22/10 al 15/11) los tenían todos blancos: el fucsia es la evolución.
- **La tapa del ebook** aparece sostenida en mano sobre el b-roll, anclada a la palabra que la
  nombra. Su tapa: fondo crema, serif italiano chico arriba, título grande en serif de dos
  renglones, ornamento de ramita, 3-4 renglones de cuerpo chico y una foto de producto sobre
  lino ocupando la mitad inferior, con un sello redondo abajo a la izquierda.
- Flecha roja ↓ en el subtítulo del CTA.

## 🧱 Herramientas de esta oferta
- `OUTPUTS/scripts-vsl/edit_aroma.py` — el editor (copia de `edit_capillas.py` con **itálica** y
  **ancho de renglón** configurables: `italic`, `margin`).
- `OUTPUTS/scripts-vsl/gen_aroma_plans.py` — los 6 planes.
- `OUTPUTS/scripts-vsl/gfx_aroma.py` — la tapa del ebook en inglés, calcada de la de ellos.
- Voz: **Sulafat** (mujer), `gemini-3.1-flash-tts-preview` / `gemini-2.5-flash-preview-tts`,
  estilo de mujer estadounidense cálida. Velocidad 1.20.
- Cama musical: la activa validada (28 % de graves, pulso 1,48), la misma de [[slime-shop-kit]].

## ⚠️ El b-roll: los tags en inglés están podridos
Medido el 19/11 con OCR de Vision sobre **150 clips** de `#aromastone`, `#aromastones`,
`#scentedstone`, `#gypsumflower`, `#plasterflower` y `#cardiffuser`: **11 sin una letra** y
6 con texto marginal. El nicho en inglés está tomado por **packaging comercial** (Sure Scents,
AIRBRC, Salt & Stone, Aromeo), tiendas de Etsy con marca de agua, reseñas de perfumería y
tutoriales japoneses con texto quemado de punta a punta. De esos 11 "limpios", mirándolos,
sirven 4. Lo que rinde es el **tag del oficio**, que no tiene idioma porque no tiene texto:
`#jesmonite`, `#yesoceramico`, `#aromatizadordegesso`, `#gessoperfumado`, `#tagsaromaticos`,
`#piedrasaromaticas`, `#moldesdesilicona`. Misma lección que [[quesos-latam]] y
[[noche-de-citas-cristiana]].

## Preguntas abiertas
- ¿Landing propia? Los guiones nombran el ebook y los 6 bonos de ellos; si la nuestra trae otros
  entregables hay que rehacer esa línea (regla del 5/11 de [[arreglos-de-ropa]]).
- ¿Precio y checkout? Hoy el ad cierra con "75 % off today", sin cifra.
- ¿Backend? El molde son los 4 OTOs de [[scented-stones]] ([[embudo-vsl-post-pago]]).

## Relacionado
[[scented-stones]] · [[guiones-y-anuncios]] · [[como-trabajar-con-santiago]] · [[internacionalizacion]] · [[caza-de-ofertas]]

## Fuentes
- Biblioteca de Anuncios de Meta, page id 1135159816352814 (19/11/2026)
- emprendecontusmanos.com y su página de producto (19/11/2026)
- OUTPUTS/2026-11-19-guiones-aromatizadores-EN-tanda1.md
