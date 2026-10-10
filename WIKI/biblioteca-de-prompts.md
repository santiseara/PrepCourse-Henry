# Biblioteca de prompts

> Mapa de los 23 prompts de producción de Santiago, por área (guiones, copy, oferta, visual, web, meta). El texto completo de cada prompt se va sumando a `RAW/prompts/` (ver "Estado de la carpeta" abajo). (fuente: RAW/2026-10-10-wiki-previa/biblioteca-de-prompts.md, RAW/prompts/_indice.md)

23 prompts que Santiago usa en producción, volcados en `RAW/prompts/`. No son experimentos: cubren el flujo entero del negocio y varios exigen como entrada los documentos de [[investigacion-de-mercado]] (Avatar Sheet, Offer Brief, deep research, documento de creencias).

Casi todos comparten estructura: **asignación de rol → contexto y misión → reglas duras → formato de salida obligatorio**. Es el patrón que sistematiza `prompt-generador-de-prompts-maestros`, un meta-prompt que convierte ideas vagas en prompts de alto rendimiento.

## Guiones y video

| Prompt | Qué hace |
|---|---|
| `prompt-guiones-por-nivel-de-conciencia` | **5 prompts en uno**, uno por nivel de conciencia de Schwartz. Fórmula de 7 pasos |
| `prompt-guiones-7-pasos` | Guiones de video ad con la estructura base |
| `prompt-guiones-30-segundos` | «Narrativa de compresión»: historia emocional completa + venta en 30s exactos |
| `prompt-ads-storytelling-largos-publico-frio` | Anuncio-historia de 1:30+, el producto aparece pasado el primer minuto, 70% narración |
| `prompt-variacion-de-guiones-winners` | Guion ganador + sales page → variantes masivas sobre la estructura que funciona |
| `prompt-vsl-oto-post-purchase` | Guion de VSL para el upsell post-compra, estructura obligatoria de 8 puntos |
| `prompt-testimonios-sora-2` | Pack de producción UGC: guion para ElevenLabs + prompt visual para Sora 2. Regla de 14s / 35–40 palabras, 3 estilos (escéptico convertido, profesional, resultado tangible) |

Ver [[guiones-de-video-ads]].

## Copy y ángulos

| Prompt | Qué hace |
|---|---|
| `prompt-angulos` | Investigación online para encontrar ángulos nuevos |
| `prompt-angulos-manuales-launch-expert` | Ángulos de alto CTR combinando psicología visual y copy, formateados para Launch Expert AI Creative Suite |
| `prompt-meta-ads-primary-text` | Primary text de Meta Ads. Registro polarizante y crudo, orientado a ROAS |
| `prompt-escribir-sales-page` | Style transfer desde una carta de ventas fuente al producto nuevo. **Son dos prompts**: uno escribe el sales letter y otro lo **acorta**. Se ejecuta en Claude |
| `prompt-comentarios-positivos-ig` | Imágenes de secciones de comentarios de Instagram ultra realistas, como prueba social |

Ver [[angulos-publicitarios]] · [[pagina-de-ventas]].

**Inputs que exige el prompt de sales page** (útil tenerlos listos antes de ejecutarlo): nombre y producto · nicho · avatar · **el gran número** · promesa principal · dolores · **el enemigo** (lo que ya probaron y les falló) · características clave · bonus · precio real y precio de oferta.

El «enemigo» es el que más se olvida y el que más trabaja: nombrar lo que la persona ya intentó sin éxito valida su frustración antes de proponer nada.

## Oferta

| Prompt | Qué hace |
|---|---|
| `prompt-modelar-ofertas` | Offer hacking estilo Hormozi: toma una oferta validada y la reconstruye |
| `prompt-crear-upsells` | Ecosistemas de productos digitales encadenados para maximizar AOV |

Ver [[seleccion-y-modelado-de-oferta]] · [[aumento-de-aov]].

## Visual y producto

| Prompt | Qué hace |
|---|---|
| `prompt-imagenes-ads` | Prompts de texto-a-imagen para anuncios estáticos |
| `prompt-crear-mockups` | Packaging high-end y psicología del color |
| `prompt-one-shot-mockups` | Convierte productos digitales intangibles en objetos fotorrealistas de alto valor percibido |
| `prompt-ebook-con-claude` | Escribe y maqueta un ebook completo en HTML/CSS para impresión (paged media) |

Ver [[imagenes-y-mockups]] · [[creacion-de-productos-digitales]].

## Web

| Prompt | Qué hace |
|---|---|
| `prompt-html-google-ai-studio` | Adapta una página de ventas HTML existente a un producto nuevo manteniendo la estructura |
| `prompt-magic-patterns` | Detecta nicho y avatar leyendo el sales copy y genera la landing con paleta y UI acordes |
| `prompt-optimizar-carga-web-html` | Core Web Vitals para landings de tráfico pago, sin alterar el diseño |

Ver [[pagina-de-ventas]].

## Meta

| Prompt | Qué hace |
|---|---|
| `prompt-generador-de-prompts-maestros` | Convierte ideas vagas en prompts estructurados |
| `prompt-educar-chatgpt` | Instrucción de sistema para respuestas sin filtro. **Se pega en las instrucciones del proyecto**, no como mensaje suelto — ver [[ia-en-el-flujo-de-trabajo]] |

## Observaciones

**Dos pares casi duplicados** que conviene resolver: `prompt-crear-mockups` vs `prompt-one-shot-mockups`, y `prompt-guiones-7-pasos` vs `prompt-guiones-30-segundos` (ambos titulados «Script Ad Prompt Doc – Productos Digitales» en origen, pero con contenido distinto).

**El nivel de conciencia como eje.** El prompt de guiones por nivel de conciencia es el más elaborado del conjunto y refleja algo que aparece también en las preferencias de variación creativa: el nivel de conciencia del público es una de las dimensiones que hay que variar deliberadamente al testear. Ver [[angulos-publicitarios]].

Relacionado: [[ia-en-el-flujo-de-trabajo]] · [[investigacion-de-mercado]]

## Conexiones con tu operación actual
- Los más útiles para [[scented-stones]] ahora mismo:
  - `prompt-variacion-de-guiones-winners`: tus 3 ganadores + la sales page → variables.
  - `prompt-crear-upsells`: para armar el backend de [[aumento-de-aov]].
  - `prompt-testimonios-sora-2`: encaja con tu stack de Sora y HeyGen.
- `prompt-guiones-30-segundos` es la versión en prompt de tu regla de 30 segundos ([[guiones-y-anuncios]]).
- **Prompts con texto disponible: 4 de 23** (tabla de abajo). Para el resto tengo solo la descripción.

## 📂 Estado de la carpeta `RAW/prompts/`
| Prompt | Texto | Qué pide / notas para usarlo |
|---|---|---|
| `prompt-ads-storytelling-largos-publico-frio` | ✅ | Pide 7 variables (producto, buyer persona, dolor emocional, ángulo, transformación, ancla de precio, CTA). Devuelve 3 guiones de 1:30 a 2:30 (250–380 palabras), cada uno con una voz distinta: afectada, juez que se redime, autoridad que ayuda. Incluye 7 beats, timestamps, shots, overlays y nota de casting. **Para [[scented-stones]], la voz "juez que se redime" es la contadora del guión 3.** |
| `prompt-angulos-manuales-launch-expert` | ✅ | **No genera nada sin los 4 documentos** (página de ventas, Offer Brief, Avatar Sheet, creencias; ver [[investigacion-de-mercado]]). Devuelve 5 ángulos de imagen estática: dolor agudo, sueño cumplido, mecanismo único, contrarian y UGC nativo. Cada uno con nombre, emoción, gancho de 7–10 palabras y escena. Sirve para natives ([[imagenes-y-mockups]]). |
| `prompt-angulos` | ✅ | Investigación online de reseñas y comunidades (G2, Trustpilot, Hotmart, TikTok, Reddit…) para encontrar **al menos 3 ángulos alternativos con evidencia real**. Para piedras: comentarios de TikTok y reseñas de guías de scented stones o salt dough. |
| `prompt-comentarios-positivos-ig` | ✅ | Genera la imagen de una sección de comentarios de Instagram "ultra realista" con nombres y fotos inventados. ⚠️ **Es prueba social fabricada.** Presentar comentarios inventados como reales en una landing o un ad expone a reclamos de defensa del consumidor (en EE.UU., la FTC prohíbe las reseñas falsas) y a rechazos de Meta ([[problemas-de-cuentas-meta]]). No lo voy a usar para generar testimonios falsos presentados como reales. Sí te ayudo a juntar y diseñar **comentarios reales** de compradores. |
| Los otros 19 | ⏳ | Solo la descripción de arriba. Prioridad: `prompt-variacion-de-guiones-winners`, `prompt-crear-upsells`, `prompt-vsl-oto-post-purchase` y `prompt-meta-ads-primary-text`. |

## Fuentes
- RAW/2026-10-10-wiki-previa/biblioteca-de-prompts.md (página de la wiki previa, actualizada el 2026-08-10)
- Fuentes originales citadas (todavía no están en este cerebro): RAW/prompts/_indice.md, RAW/prompts/
