# Skills de Launch Expert

> Las 7 skills de la Biblioteca de Launch Expert Academia (`lp.santiagobilbao.com/sk`), bajadas e instaladas el 3/11/2026 en `~/.claude/skills/`. Son manuales operativos: no hay que pegarlos en el chat, Claude los carga solo cuando la tarea las toca. (fuente: RAW/2026-11-03-skills-launch-expert/)

Cada una es el método de Bilbao escrito para que una IA lo siga sin dudar. **Donde una regla de estas choca con una corrección de Santiago, manda la corrección de Santiago** — está marcado abajo caso por caso.

## Las 7, qué son y con qué se disparan

| # | Skill | Qué hace | Frase que la activa | Tema de la wiki |
|---|---|---|---|---|
| 01 | `edicion-ia` | Anuncios y VSL con avatar IA: qué modelo usar, voz fija, cortes, control de calidad | "seguí el Manual de Edición IA" | [[ugc-y-video-generativo]] · [[vsl-reglas-de-armado]] |
| 02 | `embudo-post-compra` | Backend entero: espiar la competencia, 4 OTOs, downsells con ruleta, montaje en Impultienda | "seguí el Manual del Embudo Post-Compra" | [[embudo-vsl-post-pago]] · [[aumento-de-aov]] |
| 03 | `caza-de-ofertas` | El método largo de caza: arbitraje de sofisticación, puntaje, veredicto | "cazá ofertas de [nicho] siguiendo el Manual de Caza de Ofertas" | [[caza-de-ofertas]] · [[funnel-hacking]] |
| 04 | `manejo-cbo` | Armar, leer, escalar y cortar la CBO con el método V3 | "seguí el Manual de Manejo de la CBO" | [[metodo-v3]] · [[estructuras-cbo]] |
| 05 | `pujas-search-scale` | **Bot**: Cost Cap y Bid Cap con los winners en cuentas aisladas, pujas cada 30 min | "instalá Pujas Search Scale para mi oferta X" | [[escalado-en-meta-ads]] |
| 06 | `surfing-scale` | **Bot**: surfea el presupuesto de las CBO ±30 % y pide el OK por WhatsApp | "instalá Surfing Scale para mis CBO de X" | [[metodo-v3]] |
| 07 | `disputas` | Contesta reclamos y contracargos de Whop/Impul Pay y Mercado Pago con la evidencia del panel | "resolvé mis reclamos de Whop y Mercado Pago" | [[disputas-y-reembolsos]] |

Las 05 y 06 vienen con el código completo de los bots (Python + instalador de servidor). **Instaladas no significa corriendo:** los bots son un paso aparte que pide token de Meta, servidor y OK explícito (ver abajo).

## Lo que estas skills agregan a la wiki

### 01 · Edición IA — lo nuevo
- **Tabla de rutas por tipo de video con costo.** wan2.7-r2v (~US$0,06/s) para avatar con voz fija; Omni Flash 1.1 (~US$0,036/s) si se acepta que la voz varíe; Grok Imagine (US$0,05-0,11 por toma de 6 s) para B-roll; Veo 3.1 Lite para diálogo corto.
- **Lo que no funciona y ya costó plata:** Kling con audio, Seedance con audio (~US$1 por 8 s), Veo 3.1 completo, Omni completo.
- **Los bordes de cada clip salen de alineación forzada contra el guion, nunca de Whisper** — Whisper arrastra sílabas sueltas. Las pausas internas se cortan por energía del audio.
- **Parámetros de montaje medidos:** VSL → SP 1,12-1,15 · GAP 0,30 s · KEEP 0,14 s. Ads → SP 1,0-1,15 · GAP 0,60 s · KEEP 0,20 s. Audio final a −14 LUFS.
- **Filtro de seguridad de los modelos:** tabla de frases de venta que bloquean y su reemplazo ("a un precio que no vas a volver a ver" → "solo en esta página"). Los bloqueos no se cobran.
- **Ritmos medidos:** wan2.7 español = palabras/4,1 + 0,6 s · ElevenLabs ~161 ppm · HeyGen a 1,05 ~175 ppm.
- **Defectos que hay que buscar siempre**, con el método de detección de cada uno (ignora la foto hasta ~45 % en Omni, corte interno, subtítulos quemados, sílabas sueltas, tartamudeos con Whisper *medium*).
- ⚠️ **Choca con lo tuyo:** el manual dice cero SFX y una voz fija por país. Vos ya tenés [[velocidad-de-la-voz]] (speed 1.30) y voces fijas Sulafat/Orus por género, no por país, y el visual 100 % clip de TikTok. **Manda lo tuyo.**

### 02 · Embudo Post-Compra — lo nuevo
- **Primero se espía el backend del competidor, después se diseña.** Comprar el front con mail y tarjeta aparte, grabar la pantalla rechazando cada OTO (así se ven los downsells), tabla con nombre / precio / promesa / largo de VSL / segundo del botón / tipo de downsell / qué entrega.
- **Regla de oro del recorrido:** cada DS salta al OTO siguiente **en las dos ramas** (acepte o rechace). Si no, quien rechaza el OTO1 nunca ve el 2, el 3 ni el 4.
- **Ruletas con descuentos distintos: 50 / 53 / 47 / 55 %.** Cuatro pantallas al 50 % delatan que está arreglado. Nunca resaltar el número ganador. Precio del DS redondeado hacia abajo.
- **Las 8 páginas se generan desde una tabla única** (`config.py` + `build.py`): precio, delay, id del video y textos en un solo lugar, así el tachado del DS nunca se desincroniza.
- **El script del botón, completo**, con lo que importa: la plataforma re-pinta el HTML, así que los elementos se buscan en cada tick y el estado vive en `window`; `localStorage` para no hacer esperar en la recarga; probar siempre en incógnito.
- **Mapeo de ejes:** los order bumps son el mapa, los OTOs el vehículo. Si el bump es "más diseños", ningún OTO puede ser "más diseños".
- **Escalera de precios:** hispano 19 → 69 → 29-37 → 19-27 → 9-17; inglés 27 → 97 → 37 → 27 → 17-20. Tasas de toma realistas: 10-15 % en OTO1 y OTO2.
- Coincide con lo que ya tenías en [[embudo-vsl-post-pago]]: OTO1 el más caro, delay del botón = segundo exacto del precio **en el video ya editado**.

### 03 · Caza de Ofertas — lo nuevo
- **Arbitraje de sofisticación**, que es el marco que te faltaba escrito: espiar en mercado **fuente** (Brasil, EE.UU./anglo, a veces Corea y Japón) y lanzar en mercado **destino** (LATAM hispana, España, Europa no anglo, y el anglo cuando la fuente es Brasil).
- **Los 5 niveles de sofisticación** y cómo reconocerlos mirando los anuncios (1 virgen → 5 identificación). En la fuente se buscan ofertas de nivel 3-5; en el destino se mide el nivel de los competidores locales. **No subir de más el nivel:** en un mercado de nivel 2, un mensaje de nivel 5 confunde.
- **Palabras de búsqueda por 4 ejes:** formato del producto, disparadores de compra impulsiva, huellas técnicas (dominios de pago/quiz) y el nicho traducido.
- **Verificar el hueco en el destino** buscando el nombre del mecanismo en el idioma local: cero resultados = el mecanismo no existe ahí todavía.
- **Un ángulo está probado** cuando 3+ anunciantes distintos lo corren 14+ días.
- ⚠️ **Choca con lo tuyo:** el filtro madre del manual es **40+ ads activos durante más de una semana**. Tu regla madre del 27/10 es más fina: **fecha antes que volumen**, ordenar por impresiones y descartar marca personal **antes** de contar el arsenal ([[caza-de-ofertas]]). **Manda la tuya**; el 40+/semana queda como piso.

### 04 · Manejo de la CBO — lo nuevo
- **Con cuánto arrancar, en tickets:** oferta nueva lento 2-3 tickets · oferta nueva rápido 10-15 · oferta validada en cuentas nuevas 2-3 (5-10 con confianza). Una oferta validada se lanza directo en **3 cuentas**.
- **Los primeros 3 días, tabla de decisión:** día 1 con ROAS negativo → bajar 30 % y seguir bajando hasta el equilibrio de la cuenta; día 2 flojo → sumar renovaciones; **con ROAS positivo no se apagan anuncios** (saca al conjunto del aprendizaje); con ROAS negativo sí se puede.
- **El gasto mínimo de la renovación, con número:** 1 ticket por día o 5-10 % de la CBO, **durante 3 días y después se saca**. Los mínimos activos no deben pasar el ~20 % de la CBO. Sin mínimo, Meta le da todo al conjunto viejo y los creativos nuevos no se prueban.
- **Ritmo del surfeo según presupuesto:** debajo de 500 USD/día → +30 % cada 3-4 h · arriba de 500 → +30 % una vez por día.
- **La tabla ayer/hoy:** ayer bueno + hoy bien → +30 % · ayer bajo + hoy mejor → **quieta** · ayer bajo + hoy mal → −30 % · los dos muy buenos → surfeo agresivo.
- **El techo de la cuenta:** si a 2.000 rinde y a 2.600 se cae, el techo está cerca de 2.000 — no se fuerza, se abren cuentas.
- **Pujas manuales (oferta súper validada):** presupuesto 20-30 tickets · Cost Cap inicial = front ÷ 2 + 30 % · Bid Cap inicial = front × 1,3 · si quema sin ventas, −1 USD y esperar 2 h; si no gasta, +1 USD y esperar 2 h.
- **Objetivo de la V3 dicho con número:** la mayor cantidad de conjuntos con **más de 50 ventas en menos de 7 días**.
- ⚠️ **Diferencia con tu wiki:** [[metodo-v3]] dice surfeo cada ~2 horas; el manual dice cada 3-4 h debajo de 500 USD y una vez por día arriba. Es la misma idea con el ritmo atado al presupuesto.

### 05 · Pujas Search Scale (bot)
Escala ofertas **ya validadas** con puja manual, en **cuentas aisladas** donde la oferta no corre: una para Cost Cap y una para Bid Cap.
- `analizar.py` cruza gasto por hora de Meta con ventas por hora de Utmify → picos y horas que queman.
- `winners.py` saca los 8 ganadores (no entra el que tiene menos de 2 CPA de gasto).
- `crear.py` crea todo **en pausa**; `--prender` solo con OK explícito.
- `pujas.py` mueve la puja en escalera cada 30 min (`:00` y `:30`), con avisos por Telegram o WhatsApp.
- Cost Cap inicial = **CPA real de los winners** · Bid Cap = front × 1,3.
- Servidor Ubuntu 24.04 (DigitalOcean US$6/mes) o la Mac prendida.
- **Reglas que la skill se impone:** los tokens solo en `.env`, nunca en el chat ni en carpetas sincronizadas; un solo bot por operación; simulacro antes de cada cambio.

### 06 · Surfing Scale Automatic Bid (bot)
Las reglas de la CBO V3 escritas para una máquina: ±30 %, nunca más, en los horarios en que la oferta vende.
- **El ROAS sale solo de Impultienda** (webhook propio). Utmify queda afuera a propósito: llega 20 minutos tarde.
- Modo **agresivo** (CBO chicas que ya venden) y **tranquilo** (todo lo demás).
- Corre cada 10 minutos, propone numerado y **no mueve nada hasta que respondés SI n / NO n** por WhatsApp o Telegram. Después relee la campaña en Meta y confirma "✅ aplicado".
- `"permitir_auto": false` deja el modo automático bloqueado para siempre.
- Solo CBO en cuentas en dólares. Las Cost Cap / Bid Cap se manejan con la 05.

### 07 · Disputas Whop + Mercado Pago
La única que viene como paquete con scripts (`estado.py`, `whop_responder.py`, `whop_contracargos.py`, JS para el panel, tools en Swift para PDF).
- **El panel de Impultienda como fuente de evidencia:** consulta Supabase (`sb.impultienda.ar/rest/v1/`) desde la pestaña con sesión iniciada. Tablas `orders`, `email_events`, `download_logs`, `order_items`.
- **Reglas duras:** solo hechos verificables; si el mail de entrega falló (casilla llena, rebote) **no se declara la entrega**, se reenvía primero; las descargas con user-agent `node`/`bot`/`python`/`curl` son de servidor y no se le atribuyen al comprador; el `recommended_action` de Whop es publicidad y se ignora; **nunca** se toca reembolsar sin orden explícita.
- Los upsells son órdenes hijas (`parent_order_id`): es el argumento contra "no autoricé" y "me cobran de más".
- La base guarda en UTC; al comprador se le escribe en su hora local.
- **El chat de MP rechaza el PDF**: el informe de actividad se sube como JPG.
- Antes de usarla hay que completar su **sección 8** con las carpetas de entrega y la política de reembolsos reales, y cargar `.env` con las claves de Whop y MP.

## Qué falta para que las 7 estén operativas

| Skill | Estado | Qué falta |
|---|---|---|
| 01, 02, 03, 04 | ✅ listas | Nada. Se usan ya |
| 05 `pujas-search-scale` | ⏳ instalada, no desplegada | Carpeta `~/pujas-search-scale/`, token de Meta en `.env`, cuentas aisladas, servidor y OK para prender |
| 06 `surfing-scale` | ⏳ instalada, no desplegada | Carpeta `~/surfing-scale/`, token de Meta, **webhook de Impultienda**, servidor y OK para prender |
| 07 `disputas` | ⏳ instalada, falta configurar | `.env` con claves de Whop y Mercado Pago + completar la sección 8 (carpetas y política) |

## Preguntas abiertas

- **Caza:** ¿la skill `cazar` (barrido rápido, 50+ ads / 3+ días) y `caza-de-ofertas` (método largo, 40+ / semana + arbitraje) conviven, o `cazar` se reescribe con el marco de sofisticación del manual?
- **Edición:** ¿las rutas de modelo del manual (wan2.7-r2v, Omni Flash por ApiMart) entran a tu flujo, o seguís con HeyGen Avatar IV + voz de Google AI Studio + clips de TikTok?
- **Bots:** ¿se despliegan en un DigitalOcean de US$6 o quedan como referencia?

## Relacionado

[[caza-de-ofertas]] · [[metodo-v3]] · [[estructuras-cbo]] · [[escalado-en-meta-ads]] · [[embudo-vsl-post-pago]] · [[aumento-de-aov]] · [[ugc-y-video-generativo]] · [[vsl-reglas-de-armado]] · [[disputas-y-reembolsos]] · [[funnel-hacking]] · [[mentoria]] · [[ia-en-el-flujo-de-trabajo]]

## Fuentes

- RAW/2026-11-03-skills-launch-expert/01-edicion-ia.md
- RAW/2026-11-03-skills-launch-expert/02-embudo-post-compra.md
- RAW/2026-11-03-skills-launch-expert/03-caza-de-ofertas.md
- RAW/2026-11-03-skills-launch-expert/04-manejo-de-la-cbo.md
- RAW/2026-11-03-skills-launch-expert/05-pujas-search-scale.md
- RAW/2026-11-03-skills-launch-expert/06-surfing-scale.md
- RAW/2026-11-03-skills-launch-expert/07-disputas-whop-mercadopago.zip
- Instaladas en `~/.claude/skills/{edicion-ia,embudo-post-compra,caza-de-ofertas,manejo-cbo,pujas-search-scale,surfing-scale,disputas}/`
