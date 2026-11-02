# Vence al Parkinson

> Infoproducto de 5 tomos + 4 bonos (1.395 páginas de actividades ilustradas) para personas con Parkinson, familias y cuidadores. Corre en **Argentina**, en español con voseo, $16.999 ARS en ImpulTienda. Landing: `vence-al-parkinson.impultienda.ar`. (fuente: landing propia + Biblioteca de Anuncios, 1/11/2026)

## Ideas clave
- **La oferta.** 5 tomos: Vencé el freezing y los temblores (325 págs), Recuperá el movimiento (371), Bienestar físico y emocional (126), Respirá mejor (100), No lo enfrentes solo — familia y cuidadores (293). 4 bonos: fuerza de la voz, movete mejor en casa, guía del acompañante, alimentación. Acceso inmediato, pago único, garantía de 7 días.
- **Frases fuertes de la landing** (las repite el ad, regla del 27/10 de [[guiones-y-anuncios]]): "Volvé a tomar el control frente al Parkinson en semanas" · "No es el temblor lo que más cuesta. Es ir dejando de hacer solo cosas que antes hacías sin pensarlas" · "recuperar ese terreno, paso a paso, en tu casa" · "las abrís, elegís una y la aplicás" · "Vas caminando y de golpe los pies no responden" · "Empezaste a inventar excusas para no salir" · "seguís sin saber qué hacer el lunes a la mañana" · "Lo ves pelear con su propio cuerpo y no sabés si ayudarlo o esperar" · "Cada semana que pasa sin trabajarlo, el Parkinson te saca un poco más" · "lo que sale UNA sesión de kinesiología".
- **Mercado: Argentina.** Confirmado por Santiago el 1/11/2026. Voseo en guiones y en la voz.

## El competidor (el que modelamos)
- Página **Tom Miller**, landing `volve-a-tener-el-control-frente-al-parkinson-en-semanas.impultienda.ar`, también en ImpulTienda. **30 ads activos** el 1/11/2026, el más viejo del **5/10** (27 días corriendo) → whale.
- **Todos los ads son el mismo video**: voz en off masculina neutra, 31 a 38 segundos, clips reales + hojeada del libro impreso + placas de texto blancas con esquinas redondeadas y la palabra clave en dorado.
- **Un solo cuerpo validado, 21 hooks rotando.** El cuerpo es idéntico palabra por palabra en los 30: *"Este material fue hecho para ti. Son más de 800 actividades para personas con Parkinson. Más libros guías sobre movilidad, equilibrio, respiración, descanso, confianza. Todo explicado de forma simple y paso a paso. Recupera confianza, movimiento y parte de esa libertad que sentías antes. No dejes que el Parkinson te quite más terreno. Toca el botón de abajo y accede a este material."*
- **Hooks por repetición (= los que escalan):**
  1. **7 copias** — "Te preocupa que el Parkinson siga avanzando y tu familia tenga que hacer por ti lo que antes hacías solo." (miedo a la dependencia)
  2. **4 copias** — stack de síntomas: "se te complica caminar, sientes temblores, te falta el aire, tienes rigidez, miedo de caerte o duermes mal". Es además **el hook más viejo** (5/10).
  3. "Sientes que el Parkinson te está quitando poco a poco la libertad que tenías antes."
  4. "Te quita el sueño pensar que… un día necesites ayuda hasta para vestirte o comer."
  5. **Micro-escena familiar con diálogo** (hija/papá): "Dejá, pa, no importa, yo limpio. Sentate." · "Tranquilo, papá, respirá. Un pasito." · "Todavía puedo yo, hija." · "Solo quiero agarrar tu mano sin miedo a tropezar."
  6. **Testimonio en primera persona**: "A veces me quedaba bloqueada al caminar y solo quería recuperar un poco de dignidad al moverme."
  7. **Cuidador como avatar**: "Alguien de tu familia tiene Parkinson y cada vez le cuesta más caminar, moverse o sentirse seguro."
- **La edición del ganador:** hook de 5–6 s sobre un clip real de la persona trabada o de la familia → corte a la hojeada del libro con la placa "este material fue hecho para ti" → lista de contenidos en placas ("+800 actividades y guías", "equilibrio, respiración", "descanso y confianza", "todo explicado de forma simple **y paso a paso**") → beneficio ("recuperá **confianza, movimiento** y parte de **esa libertad que sentías antes**") → urgencia ("no dejes que el Parkinson te quite más terreno") → CTA con todos los tomos y bonos en fila.
- **Descuidos suyos que conviene no copiar:** varios clips traen subtítulos quemados en portugués ("O PARKINSON TRAVA O PASSO!") y marcas de TikTok ajenas ("¿Notaste el Cambio? ADIÓS PÁRKINSON"), porque reciclan la edición brasilera. El primary text es el mismo en los 30.

## Detalles / notas
- **Riesgo de cuenta.** El original interpela directo ("¿Tenés Parkinson?"), que es justo lo que la política de **atributos personales** de Meta castiga. En nuestros guiones el mismo ángulo se dice sin señalar al espectador: el Parkinson como sujeto ("lo que el Parkinson te va sacando"), la escena, o la primera persona. Nada de prometer frenar, revertir o curar ([[problemas-de-cuentas-meta]], [[profesional-digital]]).
- Material del competidor descargado en `~/Desktop/vence-al-parkinson/anuncios/work/ganadores/` (30 MP4 + `transcripciones.md` + hojas de contacto).

## Producción de la tanda 1 (1/11/2026)
- **Guiones:** 6, uno por familia ganadora del competidor, en voseo. `OUTPUTS/2026-11-01-guiones-vence-al-parkinson-v1-v6.md`.
- **Voces:** Google AI Studio, Gemini 3.1 Flash TTS Preview, Pace Natural, acento dirigido desde el Audio Profile ("Argentine woman from Buenos Aires, rioplatense, sh en ll/y, voseo, nunca locutora"). Se le pasaron 3 opciones y eligió **dos**: **Sulafat** (mujer cálida de ~52) y **Gacrux** (mujer de ~60, serena). Van alternadas: V1, V3 y V5 con Sulafat; V2, V4 y V6 con Gacrux. Plan a `speed 1.30` con `silence [0.26, 0.12]`.
- **Edición:** `OUTPUTS/scripts-vsl/edit_parkinson.py` (copia de `edit_energia.py`) con la paleta de la landing (terracota #B0563A, dorado #D9A441, verde #3E8E5A) y un tipo de overlay nuevo, **`card`**: placa blanca con esquinas redondeadas, texto negro en mayúscula y la palabra clave en dorado, que es exactamente el look del ganador. Las placas van a `y=900` para no chocar con el subtítulo (`capy 1420`).
- **Planes:** `OUTPUTS/scripts-vsl/gen_parkinson_plans.py`. Corte de plano 1,9–2,9 s, sin destellos (`flash: 0`), una sola cama musical a `-8`.
- **Parche al editor:** el reparto del pool usaba *la primera letra del nombre del clip* como "fuente", así que `fisio_*` contaba como una sola. Ahora usa el campo **`fam`** del plan (creador), que es lo que pide la regla del 30/10 de [[guiones-y-anuncios]].

## B-roll de TikTok
- Tags barridos: `#parkinsons`, `#fisioterapianeurologica`, `#adultomayor`, `#cuidadordeadultomayor` → 145 clips bajados con tikwm. **Rendimiento bajísimo: el nicho es contenido educativo, casi todo viene con subtítulo quemado o con el creador hablando a cámara.** De los 145 quedaron 12 limpios.
- Lo que sí rinde: entrar por el **perfil de los creadores** cuyos clips pasaron el filtro (`@temblandosinmiedo`, `@grandmas.caregiver`, `@plataformavedius`, `@fysiokriss`, `@neuroevolutiongdl`), que publican el mismo tipo de material sin carteles.
- **De los 221 clips bajados quedaron 16.** Los que se cayeron en la revisión del render (no en la hoja de contactos): `fisio_359173` y `fisio_181078` traen subtítulo quemado de punta a punta, y `fisio_990533` tiene un logo redondo arriba a la derecha que solo se saca con `zoom 1.30` + `ybias 1.0`.
- **Ojo con el portugués:** `@plataformavedius` es brasilero y mete una placa en portugués al final de cada clip ("4 EXERCÍCIOS PARA pacientes com AVE"). La ventana se corta antes.

## Preguntas abiertas
- ¿Se testea también el formato UGC con la presentadora sosteniendo el libro impreso (el ad 10 del competidor), o solo voz en off?
- ¿Hay versión en inglés de la landing para salir después a US/CA/AU/UK?

## Relacionado
[[guiones-y-anuncios]] · [[renovacion-de-creativos]] · [[problemas-de-cuentas-meta]] · [[funnel-hacking]]

## Fuentes
- Landing propia: vence-al-parkinson.impultienda.ar
- Biblioteca de Anuncios, 1/11/2026 (30 ads activos de la página Tom Miller)
- OUTPUTS/2026-11-01-guiones-vence-al-parkinson-v1-v6.md
