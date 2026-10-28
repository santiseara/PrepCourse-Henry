# Energía Vital — Guía de Autocuración Energética

> Oferta propia que ya corre en **Argentina** desde el 6 de octubre con la página **Digital World** (54 anuncios activos al 28/10) y que ahora se lanza a **LATAM en español neutro** a **US$ 9,99**. Producto: la **Guía de Autocuración Energética**, 80 fichas que conectan cada dolencia con su raíz emocional y la acompañan con cristales, hierbas y afirmaciones. (fuente: pedido de Santiago del 2026-10-28 + biblioteca de anuncios de Digital World)

## La oferta
- Landing AR: `https://energiavital.impultienda.ar/` — *"Guía de Autocuración Energética. 80 fichas para descubrir la raíz espiritual de tus dolores y acompañarlos con cristales y hierbas."*
- Precio AR$ 14.990 (tachado 62.400). **Para LATAM: US$ 9,99.**
- Frases fuertes del hero, que los ads repiten tal cual: **"Vas directo a la raíz espiritual, no al síntoma"**, **"Recetas de 3.000 años, las mismas que usaban nuestras abuelas"**, **"Lo aplicás en minutos, sin experiencia previa"**, *"La mayoría de las terapias tratan el síntoma, no la causa"*, *"Te cansaste de aliviar por ratos y volver a lo mismo"*, *"No prometemos magia"*, "acceso de por vida", **garantía de 30 días**.
- Contenido de cada ficha (se ve en el mockup de la tapa): Síntomas Físicos · Significado Espiritual · Chakra Relacionado · **Receta del Elixir de Curación** (un cristal + una hierba + los pasos).
- **8 bonos:** Planificador de autocuidado · Calendario Lunar · Limpieza Energética del Hogar · Diccionario de Cristales y Piedras · Ritual de Protección Energética · 50 Afirmaciones Poderosas · Mini Guía "Respira en 5 Minutos" · Diario de Bienestar de 30 Días.
- Tapa: violeta con mandalas dorados. De ahí sale la paleta de los videos (#5A348C violeta y #D6B25E dorado).

## Lo que corre en Argentina (Digital World, page id 1259902353883039)
- **54 anuncios activos**, arrancados el 6/10 y con tandas nuevas el 17, 18, 21, 23, 26 y 28. Está escalando.
- **Un solo texto principal para todos** (el de psicosomatización), y lo que rota es el video. Mismo patrón que Hora de Papel en [[100-paper-squishies]].
- **Videos de 57 a 74 segundos**, 9:16, voz en off sobre montaje de clips reales, **subtítulo karaoke** de 2–3 palabras abajo y una **placa de titular quemada arriba** con el hook.

### Las 3 familias de hook, con su placa
1. ⭐ **"SI TE HICIERON ALGÚN TRABAJO PARA AFECTAR TU SALUD, PRESTÁ ATENCIÓN"** — la de más impresiones. Brujería / energía ajena.
2. **"ATENCIÓN TERAPEUTAS DE REIKI"** — llamada a un nicho profesional, tono suave y entre colegas.
3. **"(ESTE) NO ES EL TÍPICO LIBRO ESPIRITUAL"** — anti-hype.

### Las 2 DNA de cuerpo (transcriptas el 28/10)
**A · Esotérica dura** (la del ganador #1, 69 s): síntoma concreto en la primera línea ("te va a doler mucho la columna y la cadera") → lista de síntomas → **negación** ("no es estrés, no es la postura") → mecanismo ("alguien te está chupando la energía y el cuerpo te está avisando") → reencuadre ("las enfermedades no son un castigo, son alertas del alma") → puente ("necesitás leer este libro") → entregables (significado espiritual, qué chakra está bloqueado, cristales y hierbas, afirmaciones) → CTA con escasez ("el acceso puede desaparecer") → prueba social ("más de 8.000 personas") → **filtro final** ("leelo solo si sentís que tus caminos están cerrados").

**B · Terapeuta a terapeuta** (54 s, se usa con los hooks 2 y 3): "esto es lo primero que reviso antes de que llegue mi próximo cliente" → la escena de la sesión → *"quizás querés tener más herramientas para saber desde dónde abordarlo"* → "por eso esta guía me pareció tan útil" → +100 prácticas en un solo lugar → **"no tenés que estudiarla de principio a fin, es una guía de consulta"** → quién la usa (Reiki o en formación) → CTA suave ("te dejo el acceso acá abajo").

## Tanda 1 de LATAM (2026-10-28): 6 videos
- Guiones en **español neutro, sin voseo**: `OUTPUTS/2026-10-28-guiones-energia-vital-latam.md` (copia en `anuncios/guiones-tanda1.md`). Uno por ángulo, con cuerpo y CTA propios:
  1. energía pesada en la espalda (familia 1) · 2. atención terapeutas de reiki (familia 2) · 3. este no es el típico libro espiritual (familia 3) · 4. dónde guarda tu cuerpo cada emoción (ángulo nuevo, el mapa cuerpo-emoción) · 5. lo que tu abuela sabía y nadie anotó (las recetas de 3.000 años de la landing) · 6. te alivias y a los tres días vuelve (el ángulo de la rueda, también de la landing).
- **Videos de 39 a 44 s**, 9:16, en `~/Desktop/energia-vital/anuncios/EV-V1…EV-V6`.
- **Voz:** AI Studio, Gemini 3.1 Flash TTS Preview, voz **Achernar** (Soft), Pace Natural, acento dirigido desde el Scene y el Audio Profile ("mujer latinoamericana de 42, mezcla colombiano-mexicana, nunca castellano ni rioplatense"). Las 3 opciones que se le pasaron están en `anuncios/voces/`. Plan a `speed 1.30` con `silence [0.26, 0.12]`.
- **Edición:** `OUTPUTS/scripts-vsl/edit_energia.py` (copia de `edit_squishies.py`) con la paleta de la tapa: caja violeta del hook, chips violetas, palabra activa del subtítulo en dorado y placa final "GUÍA DE AUTOCURACIÓN ENERGÉTICA · 80 FICHAS · 8 BONOS DE REGALO". Planes: `gen_energia_plans.py`.
- **B-roll de TikTok:** 110 clips bajados con tikwm de los tags `limpiezaenergetica`, `cristalesypiedras`, `sahumerio` y `reiki`; **21 quedaron limpios y 19 se usaron** (se descartaron dos en la segunda pasada, ver abajo). Cero stock, cero créditos.
- **Texto principal:** uno solo para los seis, en `anuncios/texto-principal.md`.

## Lo que se aprendió acá
- **El rendimiento de TikTok en este nicho es bajísimo:** de 110 clips, apenas 21 servían. Casi todo lo que se publica de cristales y sahumerios lleva **subtítulo quemado, un @usuario de repost o la cara del creador hablando**. Conviene bajar el triple de lo que se necesita.
- **Un `zoom` alto no salva una marca de repost.** Los clips F (conos backflow) y K (puestos de cristales) tenían un cartel de `@usuario` que **cambia de lugar** a lo largo del video: con `zoom 1.30` + `ybias 1.0` se fue en unos planos y en otros no. Cuando la marca se mueve, el clip se descarta; no se intenta recortarla.
- **La hoja de contactos del render es la que manda.** Las dos marcas aparecieron recién al mirar los seis videos terminados, no al revisar los clips sueltos.

## Preguntas abiertas
- ¿Se corre también el formato de **imagen/native** que usa Digital World, o solo video?
- ¿La landing de LATAM va a ser la misma en neutro y en dólares, o se arma una nueva?
- ¿Hay OTO después del pago? Los 8 bonos ya están adentro del producto.

## Relacionado
[[guiones-y-anuncios]] · [[100-paper-squishies]] · [[funnel-hacking]] · [[ugc-y-video-generativo]] · [[internacionalizacion]] · [[vsl-reglas-de-armado]]

## Fuentes
- Biblioteca de anuncios de Digital World y landing `energiavital.impultienda.ar` (relevadas el 2026-10-28)
