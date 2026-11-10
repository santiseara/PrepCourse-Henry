# Carteras Maison (el Método Riviera)

> Oferta nueva para **Argentina**, clonada de la ballena inglesa **Maison Luxe Bags / The Riviera Method** (`maisonluxebags.impultienda.ar`, US$27). Enseña a hacer carteras que parecen de boutique con **cañamazo plástico y cordón náutico**, para uso propio o para vender. (fuente: Biblioteca de Anuncios + landing del competidor, 2026-11-10)

## Ficha
| Campo | Valor |
|---|---|
| Mercado | 🇦🇷 Argentina, **voseo** |
| Producto | **Carteras Maison**, el Método Riviera: 250+ moldes en 5 capítulos, 25 clases en video, 5 bonos |
| Mecanismo | Cañamazo plástico + cordón náutico + aguja de plástico + cierre y cadena. Sin máquina de coser, sin cuero |
| Bonos | Mensajes para copiar y pegar · Tu primera cartera rápida · Dónde comprar · La fórmula de precio · El planificador del mes |
| Avatar | Mujer que quiere plata propia desde casa, sin jefe ni horario; la que probó crochet y no le cerraban los números |
| Voz | **Sulafat** (mujer), acento rioplatense |

## 🐋 El ganador: Maison Luxe Bags (leído el 2026-11-10)
- **55 ads activos**, el más viejo del **28/10** → 13 días. **490 ads en total** con los muertos: testea fuerte y mata rápido. Corre en **ImpulTienda**, igual que nosotros.
- Precio **US$27** con ancla US$54, contador, 7 días de garantía, "5 bonos gratis solo hoy", +1.200 alumnas.
- Autora: **Sophie Hart**, mamá de dos, historia de viaje por la Riviera europea. Testimonios en formato **chat de WhatsApp** (Brisbane, Columbus, Leeds, San Diego).
- **Arbitraje confirmado:** corre el mismo producto en `maisonluxebags-italy` y `-japan`. **En español no está.** La búsqueda `cañamazo` en todo el mundo devuelve 37 ads y son escuelas de bordado y capacitaciones por WhatsApp: ningún infoproducto low ticket con checkout.

### Los cuerpos y las familias de hook (lo que clonamos)
Corre **dos cuerpos fijos** y les rota el hook:
| Cuerpo | De qué va | Hooks que le cuelga |
|---|---|---|
| **A · "una cartera por noche"** | Salió del laburo en un local: una cartera por noche, fotos, amigas, la cuenta con el planificador, renuncia | "Tres meses haciendo carteras a escondidas" · "Mi suegra no podía creer que la hice yo" · "Story time: cómo una cartera por noche me sacó del local" |
| **B · "el secreto no es el material, son los detalles"** | Cañamazo firme, cada agujerito tapado, forro adentro, herrajes dorados → por eso preguntan de qué local es | "Las carteras de diseñador salen más de mil dólares" · "Me preguntó de qué boutique la saqué" · "Por qué tu cartera queda floja" |
| Materiales / objeción | Todo lo que necesitás y dónde se compra | "¿De dónde sacás el cañamazo y el cordón? ¿Eso sale aparte?" |
| Un día en mi vida | La rutina hora por hora desde que hace carteras | "Hace un año a esta hora yo seguía contando las horas" |
| La apuesta de 3 días | Diario día 1 / día 2 / día 3 con la hija | "Mi hija me apostó que largaba el segundo día" |
| Variedad | Seis modelos, mismo material, otro molde | "Un método, todas estas carteras" |

### La edición (clonada)
- **100 % b-roll** de carteras de cañamazo reales, sin cara hablando a cámara.
- **Subtítulos de 2-3 palabras en mayúscula**, blancos con borde negro y la **palabra activa en magenta**, sin caja.
- En los cortos, **placa de texto arriba** ("WATCH A PLASTIC SHEET BECOME A LUXURY BAG", "NO SEWING MACHINE · NO LEATHER").
- **El producto en pantalla**: la tapa del libro apoyada sobre carteras reales y la página de moldes. Se dibuja por código (`gfx_carteras.py`).

## 🇦🇷 Lo que cambia para Argentina
- **Voseo** y situaciones locales (la mercería, la plaza, el colegio, la mesada).
- **Etsy afuera** (regla fija): el original manda a Amazon y Etsy, nosotros a la mercería, internet y WhatsApp.
- Sin nombrar a la autora: el guion no nombra al experto.
- La cifra va en pesos porque es **un solo país** (regla del 7/11): la cartera a **cincuenta mil pesos**. ⚠️ A validar con Santiago.

## Tanda 1 (2026-11-10, 6 videos)
`OUTPUTS/2026-11-10-guiones-carteras-maison-tanda1.md` · descripción en `OUTPUTS/2026-11-10-descripcion-carteras-maison.md` · videos en `~/Desktop/carteras-maison/anuncios/`.
Nombres: `10/11 - 1` a `10/11 - 6`, uno por familia de hook.

### Producción
- **B-roll:** 22 clips limpios de 60 bajados (`#plasticcanvasbag`, `#plasticcanvas`). Se cayeron los de cara a cámara, los de subtítulo quemado y **seis creadores que promocionan su propio curso o kit** (uno de ellos, argentino, con un *"SEMINARIO PRESENCIAL de Plastic Canvas"*): en este nicho el b-roll también vende cursos.
- **Gráficos:** `OUTPUTS/scripts-vsl/gfx_carteras.py` (HTML + Chrome headless) dibuja las 5 piezas del producto: la tapa, la página de 250+ moldes en 5 capítulos, la lista de materiales, los 5 bonos y el celular. Las fotos de carteras son **cuadros de los propios clips**.
- **Editor:** `OUTPUTS/scripts-vsl/edit_carteras.py` + `gen_carteras_plans.py` + `vent_carteras.py`. Voz Sulafat a `speed 1.30`, cama `bed_activo`, subtítulos de 2 palabras con resalte magenta.
- Videos de **29 a 59 s**.

## Preguntas abiertas
- ¿La landing en español ya existe? Santiago pidió **usar el original**, bautizado **Carteras Maison**; el inserto se dibujó contra la landing del competidor.
- Precio de venta de la oferta y backend post-compra ([[embudo-post-compra]]): el competidor no muestra OTOs desde el ad.

## Relacionado
[[guiones-y-anuncios]] · [[pisos-epoxi]] · [[arreglos-de-ropa]] · [[caza-de-ofertas]] · [[internacionalizacion]]

## Fuentes
- Biblioteca de Anuncios, búsqueda `maisonluxebags.impultienda.ar` y `maisonluxebags` (2026-11-10)
- `maisonluxebags.impultienda.ar` (landing completa)
- 14 videos del competidor transcriptos con faster-whisper
