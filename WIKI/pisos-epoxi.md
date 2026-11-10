# Pisos Epoxi (El Manual del Piso Epoxi)

> Oferta nueva para **LATAM** a **$17**, modelada sobre la ballena en inglés **Hands & Home / The Epoxy Floor Playbook** (`handshome.impultienda.ar`, US$26.99). Enseña a hacer pisos epoxi para la casa propia o como oficio que se cobra por metro cuadrado. (fuente: Biblioteca de Anuncios, 2026-11-10 + landing del competidor)

## Ficha
| Campo | Valor |
|---|---|
| Mercado | 🇪🇸 LATAM multipaís, español **neutro** (sin voseo) |
| Precio | $17 |
| Producto | **El Manual del Piso Epoxi**: 6 sistemas de piso, 60+ proyectos, 48 diseños metálicos, Prep es el 80%, La Tabla de Soluciones (12 problemas), Calcula y Cobra |
| Bonos | Tu Primer Trabajo Pago · Dónde Comprar y Qué Alquilar · Antes y Después que Vende |
| Avatar | El que pidió presupuesto y se asustó · el que quiere un ingreso de fin de semana · el pintor, albañil o gasista que ya está adentro de esas casas |
| Voz | **Orus** (hombre), español neutro, Style de oficio |

## 🐋 El ganador: Hands & Home (leído el 2026-11-10)
- **61 ads activos**, el más viejo del **6 de octubre** → 35 días corriendo. Corre en **ImpulTienda**, igual que nosotros.
- **Una sola descripción para todos los ads** (la de "$800 in material / $3,600 invoice") y **un bloque de producto idéntico palabra por palabra** en los 10 videos que bajé. Lo único que rota es el **hook**.
- Precio US$26.99 con ancla US$54, garantía de 7 días, contador de oferta.

### Las 6 familias de hook (lo que clonamos)
| # | Familia | Primera línea del original |
|---|---|---|
| 1 | **El 80% antes de abrir el tarro** (3 de 10 ads = la principal) | "I do 80% of this epoxy floor before I open this can" |
| 2 | **El vecino** | "I did my epoxy floor the same day as my neighbor. Six months later, his peeled" |
| 3 | **El que vive de arreglar pisos ajenos** | "Every week I get paid to fix epoxy floors that peeled" |
| 4 | **El pintor que pierde el trabajo** (diálogo) | "How much to paint the garage? And the floor? I don't do floors." |
| 5 | **Un garage, un fin de semana** / el primer piso paga todo | "One garage, one weekend… and $2,700 in your pocket" |
| 6 | **La ventana que se cierra** | "It's a golden opportunity, but it has an expiration date" |

### El cuerpo que no cambia
Mecanismo en 4 pasos (**preparar → mezclar → verter → terminar**) → la cuenta material contra precio terminado → "That's why we created the Epoxy Floor Playbook" → 60+ proyectos paso a paso → **"If you can paint a wall, you can follow it"** → el celular en el garage → la Fix-It Chart → 3 bonos gratis → "Click below and pour your first mirror-gloss floor this weekend".

### La edición (clonada, [[guiones-y-anuncios]] registro del 5/11)
- **100% b-roll** de pisos epoxi reales; en algunos ads arranca con un avatar a cámara, en otros no (el nuestro no lo usa).
- **Subtítulos de 3 palabras**, blancos con borde negro y la **palabra activa en cobre** (#C06A2C), sin caja.
- **Chips oscuros redondeados** arriba (`MIX → POUR`, `60+ PROJECTS · STEP BY STEP`).
- **Pastillas blancas con cruz roja** para los defectos (`Bubbles?`, `Peeling?`).
- **Panel claro "THE SYSTEM / what nobody teaches you"** con los ítems que se van sumando.
- **Insertos del producto dibujados**: la página "Metallic Marble · Step by Step" con grilla de fotos numeradas, la Fix-It Chart, la tabla de precios por metro, las 3 tapas de bonos y el **celular con las páginas** en el cierre.
- Cierre: `CLICK BELOW` + bajada + botón.

## 🔎 Competencia en español (leída el 2026-11-10)
Búsqueda `piso epoxi` en la Biblioteca de Anuncios, todo el mundo: ~910 ads activos, pero los de arriba son **aplicadores locales, mayoristas de resina y capacitaciones presenciales que cierran por WhatsApp** (Megapisos BR, Epodex, Wwave, JDT Capacitaciones, EpoxyArt Master). **No aparece un infoproducto low ticket con checkout** en español. El nicho está tomado por el servicio, no por el curso: es el mismo arbitraje de [[caza-de-ofertas]] (ballena en inglés, mercado destino vacío).

## 🇱🇦 Lo que cambia para LATAM
- **Español neutro, sin voseo** (regla del 28/10 de [[energia-vital]]).
- **Cero cifras en moneda**: sale a varios países a la vez, así que el margen va como **múltiplo** ("el material es una fracción de lo que se cobra", "x4 sobre el material") — regla del 8/11 de [[quesos-latam]].
- Sin promesas de ingreso ni plazos de resultado, para no comer bloqueos como en [[profesional-digital]].
- El precio de $17 queda para la landing; los guiones no lo nombran.

## Tanda 1 (2026-11-10, 6 videos)
`OUTPUTS/2026-11-10-guiones-pisos-epoxi-tanda1.md` · descripción en `OUTPUTS/2026-11-10-descripcion-pisos-epoxi.md` · videos en `~/Desktop/pisos-epoxi/anuncios/`.
Nombres: `10/11 - 1` a `10/11 - 6`, uno por familia de hook.

### Producción
- **B-roll:** 33 clips limpios de TikTok de 61 bajados (`#pisoepoxi`, `#epoxyfloor`). Se cayeron los de subtítulo quemado, los de marca de agua centrada y **una cuenta entera de renders de IA** (pisos con nubes, árboles sumergidos): no son trabajo real y se notan.
- **Gráficos:** `OUTPUTS/scripts-vsl/gfx_epoxi.py` (HTML + Chrome headless) dibuja las 5 piezas del producto. Las fotos de los pasos son **cuadros de los propios clips**, igual que el ganador.
- **Editor:** `OUTPUTS/scripts-vsl/edit_epoxi.py` + `gen_epoxi_plans.py` + `vent_epoxi.py`. Voz Orus a `speed 1.30`, cama `bed_activo`.

## Preguntas abiertas
- ¿La landing en español ya existe? El inserto y los guiones se escribieron contra la del competidor traducida (regla del 5/11: el inserto se dibuja con la landing real en la mano).
- Backend: el competidor no muestra OTOs desde el ad; falta espiar el post-compra ([[embudo-post-compra]]).

## Relacionado
[[guiones-y-anuncios]] · [[quesos-latam]] · [[herrero-de-finde]] · [[profesional-digital]] · [[internacionalizacion]]

## Fuentes
- Biblioteca de Anuncios, búsqueda `handshome.impultienda.ar` (2026-11-10)
- `handshome.impultienda.ar` (landing completa)
- 10 videos del competidor transcriptos con faster-whisper
