# The Group Work Playbook

> Oferta low ticket en inglés (USD 27) para psicólogas y counsellors que coordinan grupos: +150 dinámicas listas para aplicar en PDF. Modelada sobre el ganador en español **Talleres Listos**. (fuente: landing propia y Facebook Ads Library, page 1423115024221032)

## Ideas clave
- **Avatar:** psicóloga, psicopedagoga o counsellor que hace consulta individual y quiere (o le piden) coordinar grupos. Mercado de habla inglesa ([[internacionalizacion]]).
- **Promesa de la landing:** *"Build a group workshop in 10 minutes: +150 activities ready to run in schools, workplaces, families and therapeutic groups."*
- **Precio:** USD 27, tachado de 71. Pago único, acceso instantáneo, garantía de 30 días.
- **Landing propia:** `the-group-work-playbook.impultienda.ar`. CTA: *"I want The Group Work Playbook"*.
- El competidor corre **105 ads activos** sobre el mismo producto en español (eran ~160 el 22/10 a la mañana), con dos landings (voseo AR y neutro LATAM) y un segundo producto, el Kit de evaluación psicopedagógica.

## Qué incluye (términos exactos de la landing, para los guiones)
**6 módulos de 25 dinámicas cada uno (150):** Icebreakers and group building · Emotions and self-awareness · Teens and school life · Families and parent workshops · Workplaces and teams · Wellbeing and therapeutic groups.

**Cada dinámica, en una ficha:** Goal · Who it's for and group size · Time · Materials · Step by step · Closing questions · Variations (and online) · **Care notes**.
Más: índice con links, índice por tipo de grupo y la lista de dinámicas de **15 minutos o menos**.

**5 bonos:**
1. 12 workshops built end to end (60–90 min, minuto a minuto): classroom life, bullying, self-esteem, boundaries, work stress, grief.
2. How to pitch your workshop to a school or a company (propuesta, mails, guion de reunión, cómo armar honorarios, plantillas Word).
3. Printable worksheets and materials.
4. Planning and evaluating the workshop (planilla, asistencia, encuesta, informe final en Word).
5. How to handle a difficult group.

**Nombres de dinámicas usables en ads:** Living map · The object I brought · Our agreement · The tallest tower · Ten minutes of my full attention · The screens agreement · Where my anxiety lives · The letter I'm not sending · Three chairs.

## DNA ganadora del competidor
Detalle completo, con las 9 transcripciones y los frames, en `OUTPUTS/2026-10-22-analisis-ads-talleres-listos-v2-transcripciones.md`. Resumen:
- **Un body fijo + muchos hooks.** El primary text es idéntico en todos los ads; cambia solo la primera línea con emoji ([[renovacion-de-creativos]]).
- **Cuatro mercados de deseo:** el encargo que ya llegó (te llamó el colegio) · más gente por hora (una sesión vs. diez personas) · el tema (bullying, bienestar de mujeres, empresas, padres) · el dolor operativo (empezar de cero, repetir el rompehielos).
- **Sin precio en el ad.** CTA de curiosidad: "mirá todo lo que incluye".
- **Videos de 20 a 35 s**, verticales, 70 a 85 palabras de voz en off.
- **La receta del guion, idéntica en los 9 ganadores transcriptos (22/10/2026):**
  1. hook = la primera línea del primary text, leída tal cual;
  2. el problema en una o dos frases;
  3. mecanismo con el nombre del producto en 3 pasos (elegís el objetivo → buscás en el índice → tenés la dinámica con paso a paso, duración y materiales);
  4. el plus ("Además, el modelo de propuesta para presentarlo en un colegio o en una empresa");
  5. frase de estado nuevo, corta ("Pasás de la idea a la fecha confirmada");
  6. CTA fijo con final variable ("Tocá el botón y mirá cómo es por dentro / las 150 dinámicas").
  Sin precio, sin testimonio, sin primera persona, sin storytelling.

## Edición de los videos (relevada de los frames del #1 y el #9, 22/10/2026)
- **Apertura 0 a 3 s:** b-roll real de stock a pantalla completa (ronda de gente en círculo, sala luminosa), con tres capas desde el frame 0: chip **blanco** arriba con el calificador del público ("👆 PARA PSICÓLOGOS Y PSICOPEDAGOGOS", texto oscuro), hook al centro en **cajas violetas separadas, una por línea** (#6D28D9, Montserrat ExtraBold mayúscula blanca) y chip blanco debajo con el claim ("+150 dinámicas listas para aplicar 👇"). **Mientras está el hook no hay subtítulos.**
- **Medio:** pesa más el producto que el b-roll. Mockup del PDF en abanico con badge naranja "+150" y chip violeta "+5 bonos incluidos", y fichas reales del PDF a pantalla completa.
- **Subtítulos:** blancos con sombra, **sin caja**, en minúscula, 3 o 4 palabras, a ~75% de alto. Sin palabra resaltada en otro color.
- **Cierre:** sin placa de CTA, termina en el mockup.

⚠️ Corrige lo que figuraba antes acá: el chip calificador **no es amarillo, es blanco**, y los subtítulos **no van en caja violeta**.

**Nuestra edición (`edit_gwp.py`), ya alineada a eso y validada con un render de prueba:** chip blanco calificador desde el frame 0 (`'at': 0.0`), hook en cajas violetas una por línea, chip de claim blanco debajo del hook (y=1020) y repetido mid-roll (y=1600), subtítulos blancos sin caja a y=1440 que arrancan recién cuando se va el hook, pool con más stills de producto que b-roll, música a −26 dB y whooshes en los cortes. Se conserva la placa final con CTA, que el competidor no tiene: es decisión nuestra.

⚠️ **B-roll:** usar solo el tramo 0 a 4,5 s de cada clip; varios cambian de escena después (mk135 pasa a un loft de oficina a los 5 s). Descartados por no pegar con el nicho: mk08, mk103, mk105, mk106, mk110, mk113, mk129 (artesanía), mk135. El resto está verificado a 4,3 s.

⚠️ Tres cosas que costaron y conviene no repetir: las rutas del plan.json se resuelven **contra la carpeta `plans/`**, no contra `work/` (van con `../`); el campo `hook` usaba por defecto el mismo renderer que el chip (`png_tag`) y se pisaban, ahora usa `png_hook`; y `edit_gwp.py` necesita `sfx.py`, `music.py` y las camas `music/bed_*.wav` en su misma carpeta.

**Pipeline nuestro:** `OUTPUTS/scripts-vsl/edit_gwp.py` y `gen_gwp_plans.py` (copiados también en `~/Desktop/the-group-work-playbook/anuncios/work/`), que arma los 6 plan.json. Los stills de la landing están en `~/Desktop/the-group-work-playbook/landing/`.

## Cómo relevar la Ads Library sin la extensión de Chrome (22/10/2026)
La extensión se cae seguido. Alternativa que funcionó y no depende de ella:
- `"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=old --disable-gpu --no-sandbox --user-data-dir=<temp> --virtual-time-budget=40000 --dump-dom "<url de la ads library>"` devuelve el DOM renderizado con las tarjetas y las URLs de los .mp4. `--headless=new` devuelve vacío en esta Mac.
- Los videos se bajan con `curl` y se transcriben con `faster_whisper` (modelo small, es) usando `~/bin/ffmpeg` para pasar a wav. Los frames salen con `ffmpeg -ss`.
- `curl` directo a facebook.com da 403: hay que pasar por el navegador.

## Huecos que ellos no tocan (nuestros ángulos propios)
Testimonio en primera persona · regalar una dinámica completa en el ad · cuentas de honorarios (taller de empresa vs. sesión) · los *care notes* y el riesgo profesional (duelo, angustia) · las variantes online.

## Detalles / notas
- Los guiones van en 🇬🇧 inglés y 🇪🇸 español con voseo, las dos versiones completas ([[como-trabajar-con-santiago]]). Las natives, solo en inglés.
- Estética de natives distinta a la de craft: no es boho ni golden hour. Consultorio y aula, luz natural, fichas impresas, sillas en ronda, rotafolio. Sin caras reconocibles (hay menores y pacientes en escena).
- **Cuidado de compliance:** es material psicoeducativo, no tratamiento ni diagnóstico. No prometer resultados clínicos en los ads.

## Preguntas abiertas
- ¿Qué países del habla inglesa se testean primero? Por defecto US/CA/AU/UK/NZ, ABO $10 por conjunto ([[testeo-de-creativos]]).
- ¿Hay upsell/OTO armado? El competidor tiene un segundo producto (Kit de evaluación psicopedagógica) que podría modelarse como OTO.
- Falta decidir el formato de video: avatar UGC, voz en off con b-roll, o slideshow de fichas.

## Relacionado
[[funnel-hacking]] · [[renovacion-de-creativos]] · [[guiones-y-anuncios]] · [[internacionalizacion]] · [[modelo-low-ticket]]

## Fuentes
- Landing propia: the-group-work-playbook.impultienda.ar
- Facebook Ads Library, page 1423115024221032 (Talleres Listos), relevado 22/10/2026
- OUTPUTS/2026-10-22-analisis-ads-talleres-listos.md (v1)
- OUTPUTS/2026-10-22-analisis-ads-talleres-listos-v2-transcripciones.md (v2: audio transcripto y frames)
- OUTPUTS/2026-10-22-guiones-group-work-playbook-v3-voz-en-off.md (la tanda vigente)
