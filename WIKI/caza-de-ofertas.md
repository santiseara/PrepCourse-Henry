# Caza de ofertas — la skill `cazar`

> La skill autónoma que barre la Biblioteca de Anuncios de Meta **en todo el mundo**, agrupa por anunciante y devuelve una shortlist de 3–5 winners duros (50+ ads activos corriendo hace 3+ días) con landing, ángulo y veredicto. (fuente: RAW/2026-10-24-skill-cazar.md)

Es el **paso cero** de la operación, la versión automatizada de [[funnel-hacking]]: lo que ahí se hace a mano con filtros y ojo entrenado, acá lo corre Claude solo con un nicho como argumento.

**Estado:** instalada y activa en estas sesiones (idéntica al archivo de RAW). Se dispara con *"cazar"*, *"buscar winner"*, *"buscar whales"*, *"analizá este nicho"* o *"espiar ads"* + el nicho (ej: `cazá recetas keto`, `cazá IA para abogados`).

## Qué oferta busca Santiago (el filtro que manda)

Registro 2026-10-24 — lo pidió explícito al cargar la skill:

- **Low ticket.** Nada de high ticket ni escalera de valor con tickets de 1.000+ USD.
- **Que no la vea nadie.** No las comunes, no las obvias, no las básicas que ya están en todos los swipe files. Si la encuentra cualquiera, está quemada.
- **Sin marca personal.** El activo no puede ser la persona: no es modelable y además pujan por CPAs de 100–200 USD que te revientan los CPM ([[funnel-hacking]]).
- **Ya escalada o empezando a escalar.** Los dos extremos sirven: el whale probado y el que recién prendió el motor. Lo que no sirve es el tester de hoy.
- **Que venda.** La prueba es el gasto sostenido, no el creativo lindo.

> Traducción operativa: priorizar **whales faceless escondidos** (misma oferta en varias fanpages, pocos competidores locales) sobre el top de resultados que devuelve cualquier búsqueda genérica.

## Requisito técnico

Usa `ads_library_search` del **conector oficial de Meta** (no un MCP de terceros). Es **solo lectura**: no toca la cuenta ni crea nada → cero riesgo de baneo ([[claude-con-meta-ads]]).

**Fallback sin conector:** caza a mano en `facebook.com/ads/library` con Chrome MCP o captura de pantalla, mismos filtros y misma lectura de señales. Más lento, funciona igual.

## Paso 1 — Barrido mundial

`ads_library_search` con:

| Parámetro | Valor |
|---|---|
| `search_terms` | **una** keyword o frase por llamada (es el texto del creativo). N variaciones = N llamadas; correr 3–5 del nicho |
| `countries` | **omitirlo** → todos los países. Así cae el whale que se esconde detrás del snapshot de un solo país |
| `ad_active_status` | `ACTIVE` por defecto; `ALL` para ver también los que pausaron |
| `limit` | hasta 50 |
| `advertiser_request` | el pedido del usuario con sus palabras |

**Los 4 ejes para generar keywords:**
1. **Formato** — ebook, guía, plantilla, kit, método, protocolo…
2. **Disparadores de compra impulsiva**
3. **Footprints técnicos** — dominios de Hotmart / Gumroad / Payhip como `search_terms`: si el dominio aparece en el texto del creativo, cae
4. **Keywords del nicho traducidas**

Para Brasil funcionan: *método, segredo, desafio, renda extra, secar barriga, reconquista, passo a passo*.

De cada ad la tool devuelve: texto del creativo, página, **fecha de creación** y `ad_snapshot_url`.

## Paso 2 — Contar el arsenal

Para cada anunciante prometedor, volver a llamar con `page_ids: ["<id>"]` → devuelve **todos** los ads de esa página. Con eso se cuenta el arsenal real y se ve la antigüedad del más viejo.

**El filtro madre (winner duro):** 50+ ads activos sobre la **misma** oferta **y** el ad activo más viejo arrancó hace **3+ días**.

> La tool no filtra por fecha: trae la fecha de creación de cada ad → el filtro se hace en el análisis. Lo que arrancó hoy es un tester validando; lo que lleva 3+ días ya está vendiendo.

## Señales de winner — escalera de certeza

| Nivel | Señal | Lectura |
|---|---|---|
| 1 — convierte | 8+ ads activos, 4–20 días | Sirve para modelar |
| 2 — escalando | ~30 ads sostenidos 3+ días | Está metiendo plata |
| 3 — **WHALE** | **50–100+ ads** sobre una misma oferta, y/o los mismos ads **45–90+ días** sin pausa | La casi-segura. Nadie banca gasto perdedor 2–3 meses |

Al detectar un whale: ir a profundidad — enumerar todo el arsenal con `page_ids`, mapear landings, precios y ángulos.

Señales que confirman:
- **Duplicación de creativos:** el mismo creativo repetido 10–20 veces = ya ganó el test interno del anunciante. Anotar esos `ad_snapshot_url` aparte: **son los ángulos a modelar primero** ([[angulos-publicitarios]]).
- **Todos los creativos a la MISMA landing.** Si apuntan a landings distintas, todavía está testeando.
- **Sin "follow me ads"** (perfiles que solo juntan seguidores no venden).
- **Misma oferta en 5–10 fanpages distintas** = se esconde de los cloners → convierte seguro.
- Descartar marcas personales y fanpages con "fronts" duplicados que no gastan.

## Veredicto de competencia

Cuántos anunciantes distintos atacan la misma promesa:

- **ENTRAR** — 2–6 activos con gasto sostenido y ninguno domina → demanda validada y espacio.
- **SUBNICHO** — 7+ con creativos muy parecidos → validado pero saturado. Proponer 3 subnichos concretos (mismo dolor, avatar más específico) ([[segmentos-de-mercado]]).
- **DESCARTAR** — 0–1 anunciantes, o ads que mueren a los pocos días → demanda no validada.
- **WHALE DOMINANTE** — un jugador con señales de Nivel 3 → no competirle de frente. Modelar su oferta y lanzarla traducida en otro mercado con hueco.

## Arbitraje multi-mercado (opcional)

Si hay un winner fuerte, chequear si el ángulo está libre en otro mercado: repetir con `countries: ["<ISO-2>"]` y el término traducido.

- 🇧🇷 Brasil (`["BR"]`) — cuna de las olas low-ticket → **mercado FUENTE**
- Destinos: 🇺🇸 `["US"]`, 🇮🇹 `["IT"]`, 🇫🇷 `["FR"]`, 🇲🇽/🇪🇸 español

**Orden de prioridad de destino:** 1) inglés, 2) Europa (IT/FR/DE), 3) LATAM, 4) Brasil. Se **modela** desde el mercado fuente (saturado, funnels maduros) y se **lanza** en un destino con 0–3 players débiles. Si en el destino ya hay testers con ads de pocos días, **la ventana se está cerrando** ([[internacionalizacion]] · [[seleccion-y-modelado-de-oferta]]).

## Score de 4 señales

1 punto cada una:

① **Longevidad** — mismos ads 45+ días
② **Volumen** — 50+ ads de un solo jugador sobre la misma oferta
③ **Duplicación** — mismo creativo repetido 10+ veces
④ **Hueco de arbitraje** — sin equivalente fuerte en un mercado destino prioritario

**4/4 = candidata A** (examen aprobado, copiala) · **3 = candidata B** · **≤2 = observar, no entrar todavía**.

## Output esperado

Shortlist rankeada de **3–5 anunciantes** que pasaron el filtro, cada uno con:

- Nombre de la página + link a su Ads Library y a la landing
- Cantidad de ads activos y antigüedad del más viejo
- Tipo de producto y precio si es visible
- Hook / ángulo principal (el dolor que atacan = lo validado)
- Los `ad_snapshot_url` de los creativos más duplicados

Cierra con el veredicto (ENTRAR / SUBNICHO / DESCARTAR / WHALE) y, si aplica, el par mercado fuente→destino. Si Santiago quiere, se guarda todo en un `01-caza.md` (o en `OUTPUTS/AAAA-MM-DD-caza-<nicho>.md`, ver [[organizacion-y-registro]]).

## Dos filtros que conviven

| | Skill `cazar` | [[funnel-hacking]] (la formación) |
|---|---|---|
| Ads activos | **50+** (whale duro) | 10–15 mínimo, 20–30 estricto |
| Antigüedad | 3+ días | 1 semana a 10–15 días |
| Mismo URL | señal, no filtro | **filtro imprescindible** |
| Marca personal | descartar | descartar |
| País | todo el mundo | por mercado |

La skill es más exigente en volumen y más laxa en tiempo. **Lo mejor es combinarlos:** correr la skill para el barrido mundial y aplicarle encima el *mismo URL* y *sin marca personal* de la formación, que son los dos filtros que separan al que escala del que testea.

## Después de la caza

1. Modelar, no copiar el mercado propio → [[seleccion-y-modelado-de-oferta]]
2. Los 4 documentos base (deep research, Avatar Sheet, Offer Brief, creencias) → [[investigacion-de-mercado]]
3. Test sucio con 100 USD y una semana → [[validacion-de-oferta]]

> **Recordatorio de la skill:** el whale valida la **OFERTA**, no te salva de un test sucio. Landing degradada, pixel ciego o un solo conjunto queman igual — cuando lances, armá el test en serio ([[setup-de-campanas]] · [[testeo-de-creativos]]).

## Preguntas abiertas
- ¿Qué umbral de ads usar cuando el nicho es chico y nadie llega a 50? (la formación diría 10–15; la skill no contempla el caso)
- ¿Guardar un registro acumulado de cazas para la segunda pasada a los 2–3 días (subió/bajó el número de ads), como pide [[funnel-hacking]]?

## Relacionado
[[funnel-hacking]] · [[seleccion-y-modelado-de-oferta]] · [[validacion-de-oferta]] · [[investigacion-de-mercado]] · [[claude-con-meta-ads]] · [[internacionalizacion]] · [[modelo-low-ticket]] · [[angulos-publicitarios]] · [[como-trabajar-con-santiago]]

## Fuentes
- RAW/2026-10-24-skill-cazar.md (la skill, cargada por Santiago el 24/10/2026)
- Criterios de selección dictados por Santiago en la conversación del 24/10/2026
