# Herrero de Finde — diagnóstico del embudo (2026-10-26)

Datos del día que pasó Santiago: **Landing 695 → Checkout 64 (9,21%) → Compra 33 (51,56%)**. Conversión total desde landing **4,75%**. Order bumps **0%**.

## La lectura

| Ratio | Hoy | KPI de la casa | Veredicto |
|---|---|---|---|
| Conversión total desde landing | **4,75%** | ≥ 2,5–3% ([[pagina-de-ventas]]) | muy por encima |
| Checkout → compra | **51,56%** | 25–30% ([[metricas-y-kpis]]) | el doble del objetivo |
| Landing → checkout | **9,21%** | ganadores ~15 · neutros ~12,5 · perdedores ~10 ([[lectura-de-resultados]]) | **zona de perdedor** |

El embudo no está roto: está **mal repartido**. Un 51,56% de cierre en el checkout no es buena suerte, es un síntoma: a la pasarela solo llega el que ya decidió comprar del todo. **La landing está pidiendo la decisión de compra completa antes del clic.** Sobre-filtra: deja afuera al que hubiera comprado en el checkout, donde cierran la garantía, el precio y el stack.

## Cuánto vale arreglarlo

Con el mismo gasto y el mismo 51,56% de cierre:

| Landing → checkout | Checkouts | Compras | Diferencia |
|---|---|---|---|
| 9,21% (hoy) | 64 | 33 | — |
| 12% | 83 | 43 | **+10 ventas/día (+30%)** |
| 15% | 104 | 54 | **+21 ventas/día (+64%)** |

Cada punto porcentual = **3,6 ventas más por día** = ~$54.000 ARS diarios al ticket de $14.990.

## Paso 0 antes de tocar nada: ¿es la landing o son los creativos?

Hoy subió tanda nueva (V22–V33). La causa 6 de [[diagnostico-de-checkout]]: *"tenés una oferta en profit, tirás una renovación de anuncios y el ratio se cae. No es la landing: son los creativos."*

**Abrir el landing → checkout por anuncio en Meta.** Si el V7 va al 14% y los nuevos al 5%, el problema es el nivel de conciencia de los creativos nuevos y la landing no se toca. Si todos están entre 8 y 10%, es la landing. Es gratis y evita rehacer lo que funciona.

El otro número que falta: **clics en el enlace vs. 695 visitas a la landing** (la carga, KPI 60–90%). Si se separan mucho hay gente pagada que nunca vio la página.

## Las fugas medidas en la landing publicada hoy

Todo medido sobre `txg7mz-en.myshopify.com/pages/herrero-de-finde` el 2026-10-26.

### 1. 🔴 El desierto de CTA (lo más caro y lo más barato de arreglar)
La página mide **21.706 px: 29 pantallas de celular**. Los 8 botones caen así:

| Botón | % de la página |
|---|---|
| 1 | 8% |
| 2 | **32%** |
| 3 | 38% · 4 | 57% · 5 | 78% · 6 | 81% · 7 | 91% · 8 | 98% |

Entre el botón del hero y el siguiente hay **5.100 px: siete pantallas sin ninguna salida a comprar**, y justo ahí están las secciones que más persuaden (*"Esto es para vos si…"*, el visor de un plano real, el mosaico de la biblioteca). El que se convence en el visor de planos tiene que seguir scrolleando cuatro pantallas para poder comprar.

**Fix:** barra sticky abajo (*"Quiero los planos · $14.990 · 60 días de garantía"*) desde que se pasa el hero, más dos botones intercalados en el tramo 8%–32%: uno debajo de *"Esto es para vos si…"* y otro debajo del visor de planos. **No hay ninguna barra fija hoy.**

### 2. 🔴 Message match: el ad ganador y el hero venden cosas distintas
El V7 (CPA de 1 USD, el que trae el grueso del tráfico) vende **una herramienta de taller barata**: *"un rollo de alambre tubular te sale más caro que esto… el alambre se te termina en dos trabajos, esto te queda para siempre"*. No promete un peso de ingresos.

La landing abre con **"Hacé tu primer $1.000.000 con la soldadora que ya tenés"** y dos tablas de proyección ($1.125.000 / $2.540.000 el primer mes). Eso es bizop, otro nivel de conciencia y otro grado de credibilidad. El herrero que venía pensando *"qué barato para una biblioteca de planos"* aterriza en una promesa de ingresos que puede sonarle a humo.

**Fix:** una versión B del hero con la promesa del V7 (*"Dejá de dibujar el sábado"* / lo que te cuesta un rollo de alambre), y mandar ahí los ads de la familia V7. Es la única landing que la gente del V7 vería.

### 3. 🟠 Largo
29 pantallas es mucho para tráfico de video de 50 segundos. Candidatos a recortar sin perder persuasión ([[pagina-de-ventas]]: *"quitar dolores y beneficios puede subir la conversión"*): las **dos** tablas comparativas seguidas (contra YouTube y contra otros packs), los 12 bonus desplegados uno por uno (van en grilla, con dos o tres abiertos) y el muro de fotos después de las reseñas.

### 4. 🟠 Urgencia muerta
"Los primeros 100 herreros" es texto plano. No hay contador, ni fecha dinámica, ni lugares restantes, ni "X personas viendo esto". De lo más fácil que queda por poner ([[pagina-de-ventas]]).

### 5. 🟡 Carga
LCP medido: **7,4 s**, y el elemento más lento es **el H1**, que espera la fuente de Google. La medición se hizo con sesión de admin (hot-reload y preview bar de Shopify encima), así que el número real del visitante es menor — **hay que medirlo limpio con PageSpeed Insights en mobile**. Lo que sí es real: el titular depende de una webfont externa. Un `font-display: swap` y precargar la woff2 lo arregla en diez minutos. El resto está bien hecho (WebP, lazy en 70 de 71 imágenes, dimensiones declaradas, 1,6 MB).

## Aparte del embudo: order bumps en 0%

Con 33 compras al día y un cierre del 51%, un bump de $9.990 (la Planilla de Cortes aparte, un pack de planos extra, la revisión de presupuesto) al 20% de aceptación son **+$66.000 ARS por día** sin tocar ni un ad ni la conversión del front ([[aumento-de-aov]]). Hoy no se está cobrando nada de eso.

## Lo que NO hay que tocar

- **El checkout.** 51,56% es el doble del KPI.
- **El precio y la oferta.** Con 4,75% de conversión total, el valor percibido está por encima del precio. Si algo, el test es **subirlo**, no bajarlo ([[optimizacion-de-roas]]).
- **Los ads que ya funcionan.**

## Dos advertencias de método

- Son los números **de un día**. 33 ventas no cierran nada. La regla propia: **mínimo 3 días de tráfico** para juzgar un cambio de landing ([[pagina-de-ventas]]).
- **Un cambio por vez.** Si entran juntos el sticky, el hero nuevo y el recorte, después no se sabe cuál movió la aguja.

## Orden sugerido

1. Abrir el landing → checkout por anuncio (gratis, 10 minutos, puede cancelar todo lo demás).
2. Sticky CTA + dos botones en el tramo muerto. Es el cambio más barato y el de mayor impacto esperado.
3. Hero B con la promesa del V7, con los ads de esa familia apuntando ahí.
4. Recorte de largo y urgencia real.
5. Order bump en el checkout.

## Relacionado
[[herrero-de-finde]] · [[diagnostico-de-checkout]] · [[pagina-de-ventas]] · [[lectura-de-resultados]] · [[metricas-y-kpis]] · [[aumento-de-aov]]
