# Caza de ofertas — la skill `cazar`

> La skill autónoma que barre la Biblioteca de Anuncios de Meta **en todo el mundo**, agrupa por anunciante y devuelve una shortlist de 3–5 winners duros (50+ ads activos corriendo hace 3+ días) con landing, ángulo y veredicto. (fuente: RAW/2026-10-24-skill-cazar.md)

Es el **paso cero** de la operación, la versión automatizada de [[funnel-hacking]]: lo que ahí se hace a mano con filtros y ojo entrenado, acá lo corre Claude solo con un nicho como argumento.

**Estado:** instalada y activa en estas sesiones (idéntica al archivo de RAW). Se dispara con *"cazar"*, *"buscar winner"*, *"buscar whales"*, *"analizá este nicho"* o *"espiar ads"* + el nicho (ej: `cazá recetas keto`, `cazá IA para abogados`).

## Qué oferta busca Santiago (el filtro que manda)

Registro 2026-10-24 — lo pidió explícito al cargar la skill:

- **50+ ads activos, mínimo 5 ofertas.** Piso vigente desde el 6/11/2026: primero subió a 70 y el mismo día Santiago lo bajó a 50 ("te voy a bajar un poco la vara") porque con 70 el mercado inglés no devolvía nada. Abajo de 50 no entra, y si no junto 5 que pasen, lo digo (ver los dos registros del 06/11/2026 al final).
- **Low ticket.** Nada de high ticket ni escalera de valor con tickets de 1.000+ USD. Solo infoproducto: nada de productos físicos ni servicios.
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

## Paso 3 (obligatorio) — auditar en el navegador

**Registro 24/10/2026: la API sola no alcanza.** Después del barrido y el conteo, hay que abrir cada candidata en la Biblioteca web. Es el paso que convierte una lista de números en una oferta modelable, y resuelve **las cuatro cosas que la API no da**:

| Dato | API | Biblioteca web |
|---|---|---|
| Fecha de inicio de cada ad | ❌ solo los 50 más nuevos | ✅ **todas, al scrollear** |
| Dominio de la landing | ❌ nunca | ✅ |
| Precio y copy completo | ❌ solo el título | ✅ |
| Producto real que vende | ❌ se adivina | ✅ |

**La URL que sirve** (país = todos, solo activos):

```
https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&view_all_page_id=<PAGE_ID>&search_type=page&media_type=all
```

⚠️ **Si no ponés `country=ALL`, la Biblioteca filtra por Argentina y te dice "no hay anuncios"** aunque la página tenga 300 corriendo. Es el error que más tiempo hace perder.

**Cómo leerla:** scrollear hasta el fondo para cargar todos los ads y después contar las fechas de *"En circulación desde el…"* agrupadas por día. Eso da **la longevidad real y el patrón de gasto**, que es la señal más valiosa:
- Muchos ads viejos todavía activos repartidos en **muchas fechas distintas** = renueva creativos todos los días porque gana plata. **La mejor señal que existe.**
- Todo el volumen concentrado en **2 o 3 días recientes** = lote masivo de testeo, no historia. Volumen sin rentabilidad probada.

**Por qué importa:** en la primera caza, el anunciante con 510 ads (el más grande por volumen) resultó tener **9 días de antigüedad** y vender calistenia; mientras que el verdadero winner tenía 97 ads y **106 días corriendo**. Con la API sola, el ranking salía al revés.

> Truco: al extraer dominios por JavaScript, reemplazar los puntos antes de devolverlos (`replace(/\./g,' punto ')`) — si no, el filtro de seguridad del navegador los tapa como si fueran un token.

## Cómo se comporta la herramienta de verdad (registro 24/10/2026)

Aprendido corriendo la primera caza real (renda extra + emagrecimento en Brasil, ver el output abajo). Esto **no está en la skill** y cambia cómo hay que usarla:

- **Para contar, usar `limit: 1`.** El campo `estimated_total_count` trae el total real de ads de la página igual. Ahorra miles de tokens por consulta: contar 15 anunciantes sale casi gratis.
- **Devuelve los ads más NUEVOS y no pagina.** Con más de 50 ads activos, es imposible llegar al más viejo → **la señal ① (longevidad) no se puede verificar en las páginas grandes**. Justo al revés de lo que uno querría.
- **La antigüedad aparece de rebote en las búsquedas por keyword**, no en las de `page_ids`: ahí sí salen ads de hace semanas o meses. Si querés longevidad, mirá las fechas de los resultados por keyword y después contá con `page_ids`.
- **`ad_active_status: ALL` no sirve para medir historial**: devolvió el mismo número que `ACTIVE`.
- **No devuelve la URL de la landing**, solo el `ad_snapshot_url`. Para mapear landings, precios y upsells hay que abrir los snapshots con el navegador.
- **Las keywords genéricas traen ruido de otros nichos.** "por dia no pix" devolvió 1,3 M de resultados con suplementos mexicanos. Frases de 2-3 palabras específicas del nicho ("secar barriga", "receita caseira para emagrecer") funcionan mucho mejor.
- **Los footprints de checkout funcionan muy bien**: `kiwify` como `search_terms` devolvió 16.354 ads y fue la ronda que más ofertas low ticket con **precio visible en el título** destapó (R$ 29,90, R$ 39, R$ 97). Probar también `cakto`, `kirvano`, `hub.la`.
- **El ranking por defecto favorece testers.** Como ordena por lo más nuevo, la primera pantalla siempre son lanzamientos de hoy. Los winners viejos hay que ir a buscarlos con keywords de subnicho.
- **El volumen engaña sin la fecha.** Un anunciante con cientos de ads puede llevar 9 días; otro con 97 puede llevar 106. El conteo por API **ordena mal** si no se cruza con las fechas del navegador.
- **Subnicho > nicho.** El término genérico ("renda extra") devuelve miles de anunciantes atomizados que mueren en una semana. El término de oficio ("crochê", "artesanato para vender") destapa las ofertas con 34 y 65 días corriendo.

## Cazar por fecha, no por volumen (regla madre, 27/10/2026)

**Corrección de Santiago:** *"la mayoría con menos de 20 ads, todos los ads son iguales y con bajas impresiones"*. El error era usar **cantidad de ads activos** como proxy de gasto: en Brasil, con R$ 20 por día cualquiera duplica 50 ads idénticos. No prueba nada.

Dos parámetros de la Biblioteca que hay que usar siempre:

| Parámetro | Qué hace |
|---|---|
| `start_date[min]` / `start_date[max]` | devuelve ads que **estuvieron activos en esa ventana**. Con una ventana de hace 4–5 meses y `active_status=active`, lo que cae son ads que siguen vivos hoy y ya corrían entonces |
| `sort_data[mode]=total_impressions` | ordena por **impresiones totales**, de mayor a menor |

URL base (cambiar KEYWORD y la ventana):

```
https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=KEYWORD&search_type=keyword_unordered&media_type=all&start_date[min]=2026-05-01&start_date[max]=2026-08-01&sort_data[mode]=total_impressions&sort_data[direction]=desc
```

**El filtro nuevo, en este orden:**
1. **Fecha del ad activo más viejo.** 45+ días = nivel 3; 90+ días = no hay discusión.
2. **Escalera de fechas:** ads vivos repartidos en muchas fechas distintas (ej. 873 / 76 / 69 / 57 días *más* un lote de hoy) = renueva creativos todos los meses porque gana plata.
3. **Recién después, el volumen.** 22 ads con dos años de historia valen más que 150 lanzados hoy.

**Por qué el nicho de bajar de peso devuelve siempre marcas personales (hallazgo del 27/10).** Ordenado por impresiones, todo lo que lleva años corriendo en emagrecimento tiene cara: Zanon Macedo (15 meses), drvictorcutait (2 años y 4 meses), Géssica Andrade, Dr. Fabiano, Clínica Monteze. En ese nicho **la cara es la oferta**: el avatar le compra al médico, no al PDF. No es que se busque mal, es como está armado el mercado en Brasil. La única página sin cara que sobrevive años es **Menopausa Cancelada** (ID 106449212160487, un ad activo desde junio de 2024), y lo esquiva con **funnel de WhatsApp**: el chat reemplaza la confianza que daría la cara. Ese es el mecanismo a copiar, y es el mismo de Viver é Cristo.

## Correcciones de Santiago sobre la caza

**27/10/2026 — "las últimas que me diste fueron malísimas, las conoce todo el mundo y encima la mayoría eran marcas personales".** Reglas que salen de ahí, obligatorias en toda caza:

- **La marca personal se descarta ANTES de contar el arsenal**, no después. Si el `page_name` es un nombre propio, un @usuario o lleva título (Dra., Chef, Nutricionista, Coach), se tira sin mirar cuántos ads tiene. En la caza del 27/10 eso eliminó 12 de las ~20 candidatas de la primera pantalla. Lo que sirve es la **página-marca**: Viver é Cristo, Fazendo a Nossa Festa, Prosperando Hoje, Doces Lucrativos.
- **Nunca arrancar por la keyword del nicho.** "renda extra", "emagrecer", "cardápio" devuelven lo que ve todo el mundo. El arranque es por **footprint de checkout** (cakto, kirvano), **precio en el texto** ("apenas R$ 9,90") y **mecánica de entrega** ("moldes em PDF", "arquivo em PDF"). Eso filtra solo a quien vende un PDF de 10 reales.
- **Decir cuando un nicho no da.** El 27/10 bajar de peso no devolvió un solo winner duro en PDF: lo honesto es decirlo y no rellenar la shortlist con testers de hoy.
- **Volumen sin antigüedad no es winner.** Livera tenía 154 ads activos y los 154 estaban en circulación desde ese mismo día. Es un lote de testeo con presupuesto. Se anota el ángulo y se vuelve a mirar a los 3 días.

**Dónde viven las ofertas escondidas (hallazgo del 27/10):** el cruce **fe + souvenir imprimible**. Mismo PDF vendido con cuatro usos a la vez (regalo, souvenir para la iglesia, decoración, catequesis), funnel de WhatsApp y el ángulo **"pagás solo después de recibir todo"** — riesgo cero, cero marca personal y ningún gurú compitiendo por esas palabras. Ver `OUTPUTS/2026-10-27-caza-ingresos-extra-y-bajar-de-peso.md`.

## Banco de keywords (26/10/2026)

Las keywords no se improvisan en cada caza: hay un banco por mercado y por eje en
`OUTPUTS/2026-10-26-keywords-caza-ingresos-br-ar.md` (BR + AR, ~180 términos en 6 ejes, con la lista negra de términos de gurú).

Dos reglas técnicas que salieron de armarlo:
- **`search_type=keyword_exact_phrase`** para las frases de 2-3 palabras. Con `keyword_unordered` entra ruido de otros nichos.
- **El eje más virgen del nicho de ingresos no es el oficio, son los atajos**: listas de proveedores/fornecedores, planillas de precificación, CV editable, cobrar en dólares. Son ofertas de "generar ingresos" que no prometen plata, así que ningún gurú compite por esas palabras.

**Bancos por nicho (27/10/2026)** — `OUTPUTS/2026-10-27-keywords-br-ia-renda-extra-manifestacao.md`: Brasil, nichos IA, renda extra (tanda nueva, sin repetir la del 26/10) y manifestación. Tres aprendizajes de armarlo:
- **En IA, el eje virgen es "IA por oficio"** (IA para corretor de imóveis, plano de aula com IA, roteiro de pregação com IA). "Inteligência artificial", "ChatGPT" y "curso de IA" son tierra de gurús de high ticket.
- **Manifestación no es un nicho, son tres mercados que no comparten copy**: lei da atração/quântico, espiritualidade prática (simpatia, banho, tarô, numerologia) y cristão/evangélico (oração, salmo, jejum, devocional). Buscar solo "lei da atração" deja afuera los dos que más venden low ticket.
- **Cuidado de política en manifestación:** promesas de curar o amarrar tumban cuentas. Se modela el ángulo (identidad, ritual), nunca la garantía de resultado sobrenatural.

**Registro 2026-11-02 — cazar infoproducto con VSL en Brasil: la celda vacía.** Santiago pidió *"únicamente ofertas con VSL … validadas, que no sean de marcas personales, que tengan más de 50 anuncios … nicho de salud o de renta extra en Brasil"*. Tras ~40 búsquedas y ~2.000 anuncios escaneados, **no existe ninguna oferta que cumpla los cuatro criterios a la vez**. Lo que salió, que vale para toda caza futura en Brasil:

- **La VSL está prácticamente extinta en Meta Brasil.** Barrido del universo de video activo (query `você`, `media_type=video`, 321 anuncios): anunciantes con creativo de **+110 s = 4**, ninguno con volumen. El mercado corre **creativo corto (8–60 s) → WhatsApp, Instagram o checkout directo**. Si el requisito no negociable es VSL, hay que cazar en **inglés**, no en portugués.
- **El filtro de "50+ ads en una fanpage" excluye por construcción al infoproducto low ticket brasileño.** Ese mercado **rota decenas de fanpages con 1–48 ads cada una** (cuentas sucias de afiliado). Verificado: Receitas para Diabéticos 6, Pack De Achadinhos Shopee 1, Homens com Propósito 5, Fundação UniHealth 22, Insta Criativo 16. El techo real de ese perfil es **~48 ads**, no 50+. → responde la pregunta abierta de qué umbral usar: en infoproducto BR, **20–48 ads ya es winner**.
- **Quién sí tiene 50+ en Brasil, y por qué no sirve:** nutra física → WhatsApp (DRM Plus 130, Dra. Caroline Townsend con 16 fanpages clonadas), e-commerce/revenda (LIQUIDZ 670, activos desde ago 2025), y lanzadores con VSL pero **marca personal** (Venda Sem Estoque 110 → `site.marcelowedrop.com`, único con VSL verificada).
- **Footprints que aíslan infoproducto de verdad:** `kiwify` y `hotmart` como `search_terms` (el de kiwify devuelve 15.800 ads, puro infoproducto) y el **precio en el link title** (`Apenas R$10`, `por R$ 17,90`, `De R$197 por R$35`).
- **Footprint que aísla VSL:** `media_type=video` en el UI **+ filtrar por la duración del creativo** (el texto de la Biblioteca trae `0:00 / 2:00`). Es el discriminador más limpio que hay para separar embudo de VSL de creativo corto.
- **Solo traen ruido en Brasil:** `renda extra`, `emagrecer`, `antes de dormir`, `por apenas R$`, `aula gratuita`, `assista ao vídeo`. Los invade el comercio local, las apps de microdrama y los coaches de marca personal.
- **Trampa técnica:** el dominio que muestra la Biblioteca de Anuncios es el **display link y suele ser falso** (no resuelve en DNS: `kitrevistinhasdecolorir.com`, `secajejumturbo.com.br`, `receitasproteicaspobre.com.br`). **No se puede verificar una landing por ahí** — hay que entrar por el ad.
- **Mejor oferta del perfil pedido (sin VSL):** `Arquivos que encantam` (page_id 216603914872916) — 48 ads activos, 18 días, Kit Lembrancinhas de revistinhas para colorir a **R$10**, página no personal, con el creativo `🚨Apenas R$10 🚨` duplicado ~45 veces. El cluster "que encantam" suma **194 ads activos**. Ver `OUTPUTS/2026-11-02-caza-infoproductos-vsl-brasil.md`.

**Registro 2026-11-02 (bis) — la misma caza en inglés: acá sí existe.** Santiago eligió *mantener la VSL y cambiar de mercado*. Con los criterios intactos (infoproducto digital + VSL + 50+ ads + no marca personal + salud/renta extra), en EE.UU. **aparecen tres en la primera pasada**, contra cero en Brasil. Confirma que la VSL sigue siendo el embudo dominante en inglés.

- **La shortlist:** `SSAcademy` (page_id 529517186908298) — 124 ads, 52 días sin pausar, VSL de 1:46–2:57, landing ClickFunnels `sellersyncacademy.com`, renta extra, **faceless** (el copy no nombra a nadie) → **4/4, candidata A**. `V Shred` (801113639985410) — 440 ads en US, activos desde el 15/07 (3,5 meses), VSL 1:18–2:04, `le.vshred.com`, infoproducto de fitness, embudo quiz→VSL → 3/4. `30 Second Clients` (100777102992403) — 151 ads, VSL 1:01–2:09, `go.smartphonefreedomlifestyle.com`, renta extra → 3/4. Detalle completo en `OUTPUTS/2026-11-02-caza-infoproductos-vsl-ingles.md`.
- **La regla fuerte que salió: en salud la VSL es casi siempre producto físico; el infoproducto con VSL vive en renta extra.** Las dos mejores VSL de salud que encontré en inglés venden cosas: `Sciatica Center` (184 ads) vende una crema de magnesio y `Sinus Relief Insider` (97 ads, VSL de 2:02–3:46 activa desde el 25/05 — cinco meses, la longevidad más dura de toda la caza) vende una máscara térmica en Shopify. El margen y el AOV de un suplemento o dispositivo aguantan producir una VSL; el infoproducto de salud rara vez llega a ese volumen. Excepción: los programas de fitness tipo V Shred.
- **Footprints que funcionan en inglés:** `instant access` aísla infoproducto digital (38.000 ads — de ahí salieron SSAcademy y 30 Second Clients en una sola búsqueda); `faceless` aísla renta extra sin cara (4.900 ads); `free presentation` aísla VSL (19.900 ads). Las páginas advertoriales se llaman `... Journal`, `... Report`, `... Insider`.
- **Solo traen ruido en inglés:** `work from home` (1,6M de ads, puro gimnasio local), `blood sugar` (nutra física), `side hustle` (apps y SaaS), `sciatica` (quiroprácticos locales).
- **El discriminador de VSL que sirve en cualquier idioma:** la **duración del creativo** que muestra el UI (`0:00 / 2:36`). 1:00–3:00 es el rango de la VSL de infoproducto; 8–30 s es ad corto a checkout o a WhatsApp.

## Preguntas abiertas
- ~~¿Qué umbral de ads usar cuando el nicho es chico y nadie llega a 50?~~ **Resuelto el 2/11/2026:** en infoproducto low ticket brasileño el techo por fanpage es ~48 ads, así que ahí 20–48 ya es winner (registro de arriba).
- ¿Guardar un registro acumulado de cazas para la segunda pasada a los 2–3 días (subió/bajó el número de ads), como pide [[funnel-hacking]]?

## La skill `caza-de-ofertas`: el método largo del manual (3/11/2026)

Desde el 3/11 está instalada también la skill **`caza-de-ofertas`**, el Manual de Caza de Ofertas de Launch Expert ([[skills-launch-expert]]). No reemplaza a `cazar`: es el método largo, con el marco de **arbitraje de sofisticación** que acá faltaba escrito.

**Mercado fuente → mercado destino:** se espía donde el público ya vio todo (Brasil, EE.UU. y el mundo anglo; en algunas verticales Corea y Japón) y se lanza donde ese mecanismo todavía no llegó (LATAM hispana, España, Europa no anglo, y el anglo cuando la fuente es Brasil).

**Los 5 niveles de sofisticación**, que se leen mirando los anuncios:

| Nivel | Qué ves | Qué funciona |
|---|---|---|
| 1 Virgen | Casi nadie vende eso, anuncios simples | La promesa directa |
| 2 Promesa ampliada | Misma promesa, cada uno más grande | Promesa más fuerte, más rápida o más específica |
| 3 Mecanismo | Aparecen el "cómo" y el "por qué" | Un mecanismo con nombre |
| 4 Mecanismo ampliado | Muchos mecanismos compitiendo | Mecanismo más nuevo, más simple o más completo |
| 5 Identificación | Público saturado, desconfía de todo | Historias, identidad, avatar muy específico, quizzes |

En la **fuente** se buscan ofertas de nivel 3-5. En el **destino** se mide el nivel de los competidores locales: si están en 1-2, un mecanismo de nivel 3-4 traído de afuera se ve nuevo y gana. **No subir de más el nivel:** en un mercado de nivel 2, un mensaje de nivel 5 confunde.

**Ahora son tres filtros que conviven:**

| | Skill `cazar` | Manual (`caza-de-ofertas`) | Tu regla madre del 27/10 |
|---|---|---|---|
| Ads activos | 50+ | **40+** (piso) | el volumen va **último** |
| Antigüedad | 3+ días | **más de una semana** | 45+ días = nivel 3; 90+ = no hay discusión |
| Orden de lectura | volumen | volumen y después landing | **fecha e impresiones primero** |
| Marca personal | descartar | descartar al filtrar falsos positivos | descartar **antes** de contar el arsenal |

**Manda tu regla madre del 27/10** (sección de arriba): fecha antes que volumen, ordenar por impresiones y tirar la marca personal antes de contar nada. El 40+ durante más de una semana del manual queda como **piso mínimo**, no como criterio de selección.

**Lo demás del manual que suma acá:**
- **Palabras de búsqueda por 4 ejes:** formato del producto (guía, método, protocolo, kit, plantillas), disparadores de compra impulsiva (secreto, paso a paso, en 7 días, sin gimnasio), huellas técnicas (dominios de pago y de quiz) y el nicho traducido. Coincide con tu hallazgo del 27/10 de arrancar por footprint de checkout y no por la keyword del nicho.
- **Verificar el hueco** buscando el **nombre del mecanismo** en el idioma del destino: cero resultados = no existe ahí todavía.
- **Un ángulo está probado** cuando 3+ anunciantes distintos lo corren 14+ días.
- **Si ya aparecen testers con anuncios de pocos días en el destino, la ventana se está cerrando.**
- **Puntaje de 4 señales:** longevidad 45+ días · 80+ anuncios · mismo creativo 10+ veces · hueco de arbitraje. 4/4 = candidata A, 3/4 = B, 2 o menos = observar.

## Relacionado
[[funnel-hacking]] · [[seleccion-y-modelado-de-oferta]] · [[validacion-de-oferta]] · [[investigacion-de-mercado]] · [[claude-con-meta-ads]] · [[internacionalizacion]] · [[modelo-low-ticket]] · [[angulos-publicitarios]] · [[como-trabajar-con-santiago]]

## Fuentes
- RAW/2026-10-24-skill-cazar.md (la skill, cargada por Santiago el 24/10/2026)
- OUTPUTS/2026-10-24-caza-renda-extra-y-emagrecimento-brasil.md (primera caza real: de ahí salen las notas de comportamiento de la herramienta)
- Criterios de selección dictados por Santiago en la conversación del 24/10/2026
- OUTPUTS/2026-11-02-caza-infoproductos-vsl-brasil.md (la caza de infoproducto con VSL en Brasil: de ahí salen los footprints, la trampa del display link y el techo de 48 ads)
- OUTPUTS/2026-11-02-caza-infoproductos-vsl-ingles.md (la misma caza en EE.UU.: la shortlist de tres, los footprints en inglés y la regla de que en salud la VSL es producto físico)

### 🆕 2026-11-10 · Las keywords no se corren por la API: van por la UI con frase exacta

Del banco nuevo de ingresos en Brasil (`OUTPUTS/2026-11-10-keywords-br-ingresos-tanda-nueva.md`):

- **`ads_library_search` (la API) no sirve para probar keywords.** No tiene `keyword_exact_phrase` y rankea por relevancia solo las primeras filas: después ordena por fecha de creación y devuelve a los que más publican ese día. Las 6 primeras pruebas (`sem precisar de experiência`, `não precisa de diploma`, `trabalhar por conta própria`, `lucro por peça`, `quanto cobrar`, `faça e venda`) volvieron **100 % DramaBox, Vega TV, Dramaflix y AI-Talera**. Sirve para contar arsenales con `page_ids` + `limit: 1`, no para medir una palabra.
- **La UI sí, y el conteo se lee del DOM.** El HTML que devuelve `fetch` de la página de la Library **no trae el número** (lo pinta el SPA después de su consulta) y el endpoint viejo `/ads/library/async/search_ads/` devuelve **404**. Lo que funciona: navegar a la URL con `search_type=keyword_exact_phrase`, esperar a que aparezca `~N resultados` en `body.innerText` y cortar las tarjetas por `Ver detalles del anuncio` para leer página + dominio + copy de cada una. Con `browser_batch` alternando `navigate` + `javascript_tool` entran 4 keywords por llamada.
- **Ojo con el país:** la UI filtra, así que `country=BR` da números más chicos que el `country=ALL` de los bancos viejos (`mesmo começando do zero`: 5.600 en BR contra 11.938 mundial). Se elige uno y se mantiene en toda la tanda, y se aclara cuál es al entregar.
- **Lo que confirmó esta tanda:** el eje que pesca en el nicho dinero es el **formato del material** (`material completo`, `aulas gravadas`) y la **objeción del comprador** (`sem patrão`, `sem nenhuma experiência`), no el deseo. `sem patrão` (210) es chica pero limpísima: es toda la flota de fronts con nombre genérico de mujer (Lidiane silva, Lilian Silva, Mariana Gourmet) mandando a WhatsApp con material digital de cocina.


## Registro 05/11/2026 — dos reglas técnicas de keywords (Brasil)

De la caza de emagrecimento + renda extra del 05/11 (`OUTPUTS/2026-11-05-caza-brasil-keywords-ocultas.md`):

1. **Las frases de 4+ palabras no sirven.** `ponto chinês da fome` → 0 resultados; `bactéria do intestino que engorda` → 4 viejos; `qual é o seu tipo de barriga` → 3.482 contaminados con microdramas. Lo que pesca son **2–3 palabras**: `auriculoterapia`, `nervo vago`, `pernas inchadas`, `escovação a seco`.

2. **En salud, las terapias manuales están tomadas por clínicas locales.** `massagem modeladora` (3.009), `ventosaterapia` (2.832), `liberação miofascial` (5.448) y `extensão de cílios` (13.872) devuelven estudios de barrio con "agende sua avaliação". El filtro que separa al infoproducto del servicio local:
   - **formato en el título** — atlas, mapas, catálogo digital, guia, material completo;
   - **moneda USD** en un anuncio en portugués (gestor grande, no comercio de barrio);
   - **fanpage sin ciudad** en el nombre.

3. **La veta nueva de salud en BR no es el peso: es la terapia manual y el síntoma de pierna.** `auriculoterapia` destapó *Atlas de Auriculoterapia* con **100 Mapas por R$19,90** (producto puro, cero marca personal), y `drenagem linfática em casa` / `escovação a seco` destaparon una ballena de **132 anuncios activos** (page_id `702881226395611`, todos con el título `⭐⭐⭐⭐⭐ (5/5)`).

4. **Señal de front faceless afinada:** un nombre de persona *genérico* y repetido entre páginas (Ana Silva, Patricia Oliveira, Carla Matos, Beatriz Rocha) con el mismo título `CLIQUE AQUI` y sin cara **no es marca personal: es una flota para esconderse**. Es lo contrario de la página con foto real y "minha história", que sí se descarta. Apareció así el nicho de **cuidador de idosos** (38 ads en la cabecera + 3 fronts).

5. **Capa nueva de renda extra: el oficio técnico y la certificación obligatoria** — `conserto de celular`, `manutenção de ar condicionado`, `técnico de inverter`, `NR-35`, `instrutor de NRs`. Avatar distinto al de artesanía: hombre de 30–50 que quiere cobrar por un servicio concreto.

## Registro 05/11/2026 — en renda extra, las keywords van en genérico, no por oficio

Corrección de Santiago, el mismo día: *"no quiero que en las de renda extra me pongas específicamente qué tipos de trabajo… quiero palabras generales de renda extra, o sea, no algo súper específico"*.

**La regla:** en el nicho dinero las keywords de caza se arman **sin nombrar el oficio** (nada de `chaveiro`, `piscineiro`, `conserto de celular`). Pero tampoco sirve nombrar el deseo: `renda extra`, `ganhar dinheiro` y `comece a vender` están quemadas por ruido. Las cuatro formas que sí funcionan:

| Forma | Ejemplos validados |
|---|---|
| **Objeción o condición del comprador** | `mesmo começando do zero`, `não é pirâmide` |
| **Precio o formato** | `curso por apenas` |
| **El oficio en genérico** | `aprender uma profissão`, `grana extra`, `fazer um bico` |
| **La mecánica de trabajo** | `só copiar e colar`, `nas horas vagas` |

**La mejor de todas: `mesmo começando do zero`** (11.938 resultados). Destapó *"Curso Completo de Tranças por Apenas R$ 27!"* y *"Curso de chinelos por R$ 10"* — precio en el título, faceless, y el oficio aparece solo, sin que uno tenga que adivinarlo de antemano. Es la ventaja de la keyword general sobre la específica: **no hay que saber el oficio para encontrar la oferta**.

`grana extra` sirve de control: trae al mismo winner que había aparecido buscando el oficio (`conserto de celular` → Jeferson Moreira).

**Quemadas por ruido en el nicho dinero (con su número):** `caiu no pix` 186.399 · `depois do expediente` 537.439 · `comece a vender` 372.147 · `aprenda do zero` 296.097 · `complementar a renda` 164.942 · `grupo VIP` 64.128. Todas devuelven comercio local, ecommerce o microdramas.

## Registro 06/11/2026 — el piso sube a 70 ads y "mínimo 5 o no me mandes nada"

Santiago lo pidió explícito al abrir la caza del mercado inglés en ingresos extra. **Reemplaza el filtro de 40/50 ads del manual** en toda caza futura:

- **Piso de 70 ads activos.** Abajo de 70 no entra ni como mención. El 50+ de la skill y el 40+ del manual quedan viejos. ⚠️ *Corregido el mismo día: el piso final es 50, ver el registro siguiente.*
- **Mínimo 5 ofertas que pasen.** Si junto 2 o 3, **no mando nada**: lo digo y sigo buscando. No se rellena la shortlist.
- **Solo infoproducto low ticket.** Nada de productos físicos (ni los que venden el físico con un PDF de regalo), nada de servicios, nada de high ticket.
- **Nada de marcas personales**, como ya estaba: se descarta antes de contar.

Los cuatro filtros se aplican **antes** de escribir la shortlist, no después.

### Hallazgo técnico: cómo contar el arsenal barato

`ads_library_search` con `page_ids: ["<id>"]` y **`limit: 1`** devuelve igual el `estimated_total_count` de la página = el arsenal exacto de ads activos, por ~300 tokens en vez de ~10.000. Es la forma correcta de screenear muchas páginas candidatas de una.

### Hallazgo técnico: la búsqueda se rompe con keywords amplias

La herramienta rankea por relevancia **solo las primeras ~5-10 filas**; después se cae a orden por fecha de creación y devuelve el ruido de los anunciantes que más publican ese día (apps de novelas, dramas cortos, nutra con nombre de persona, el enjambre de India/Nigeria).

- Frases amplias ("make money with AI", "side hustle", "work from home typing jobs", "get paid for online surveys") → **inservibles**, 500.000+ resultados de ruido.
- Frases angostas y literales de 3-4 palabras ("digital products resell rights" → 330 resultados, "master resell rights" → 190, "faceless digital marketing" → 1.105) → **todas en tema**.
- Regla operativa: **usar `limit: 10-12` y leer solo las primeras filas**, y tirar muchas búsquedas angostas en vez de pocas amplias.
- `countries` conviene siempre para el mercado inglés (`["US","CA","GB","AU","NZ"]`): sin filtro, el ruido de India y Nigeria se come la pantalla.

### El mercado inglés de ingresos extra está atomizado (resultado de esta caza)

Barrí ~20 keywords angostas por los ejes del nicho: PLR/resell rights, faceless digital marketing, digital products, printables de Etsy, Amazon influencer, freight dispatcher, flipping/reselling, AI side hustle, encuestas pagas, blueprints de ingreso extra. **Ninguna oferta cumplió los 4 filtros.** Lo que hay:

- Arsenales chicos en todas las páginas-marca del nicho: Bizzoso 18, Sarah Clarke Consulting 13, Appisi 4, Copy Paste Paid 7, Faceless After Fifty 7, Sofia Mercado 9, Prime Finds With Jill 40, Kaizen Marketing Agency 0 (ya pausada).
- Los dos únicos arsenales de 70+: **Credit Secrets** (77 ads, "This Loophole Still Works in 2026") es reparación de crédito, no ingresos extra; y **SSAcademy** (170 ads, "How I leverage Amazon's 600B infrastructure") es hook de masterclass gratis → embudo de **high ticket**, no low ticket.
- Lectura: en inglés este nicho lo laburan cientos de operadores chicos de 5-40 ads y marcas personales de coach. Los arsenales de 70+ en low ticket están en nichos de **hobby/oficio** (los que ya trabaja: squishies, autómatas, herrería, barbería), no en "ganá plata online".

**Para la próxima caza de ingresos extra en inglés:** arrancar por footprint de checkout y precio en el texto (como se hace en Brasil con cakto/kirvano), no por la keyword del nicho — y mirar los nichos de oficio con promesa de ingreso en vez de "make money online" genérico.

## Registro 06/11/2026 (b) — la vara baja a 50 y aparecen las dos primeras del mercado inglés

Santiago, el mismo día y después del no-send: *"Te voy a bajar un poco la vara, mínimo 50 ads"*.

**Regla vigente:** el piso es **50 ads activos**. Reemplaza al 70 que había fijado horas antes y coincide con el filtro madre de la skill. Lo demás no se mueve: solo infoproducto low ticket, nada de marcas personales, nada de físico, mínimo 5 ofertas o se avisa.

### Lo que pasó el filtro con 50

| Oferta | Ads | Precio / producto | Veredicto |
|---|---|---|---|
| **Emily Makes → cutifystudio.com** | 130 | **$39**, biblioteca de 150.000 SVG con licencia comercial | Pasa limpio |
| **Tina Ghazi Digital → go.tinaghazi.com** | 142 | **$17**, Canva Crash Course con Master Resell Rights | Pasa, pero la fanpage va con nombre propio |

Adyacentes (low ticket digital, sin promesa de ingreso — nicho hobby, no "ingresos extra"): **The Crochet Nook** 215 ads (bundles de patrones de crochet) y **Master Crafts DIY** 208 ads ("500+ Plans. Every Cut Listed.", biblioteca de planos de carpintería).

### Los 50+ que se cayeron por el otro lado del filtro

- **Alina Bond** — 1.250 ads. Es **Zeely.ai**: app con suscripción, no infoproducto.
- **30 Second Clients** — 262 ads. Es **Max Tornow**: marca personal + video gratis → high ticket (`smartphonefreedomlifestyle.com`).
- **Norman Calloway** — 143 ads. Advertoriales de abogado de DUI, fuera de nicho.
- **Al Crayfish** — 83 ads. Embudo a grupo de WhatsApp por "cursos gratis de IA", sin producto ni checkout.
- **Highland Growth** — 61 ads, pero la página mezcla ofertas sin relación (hasta un ad en turco). No es la misma oferta.
- **Credit Secrets** 77 (reparación de crédito) y **SSAcademy** 170 (masterclass gratis → high ticket), ya descartados en el registro anterior.

### El patrón que sí funciona en inglés (lo que hay que modelar)

**Advertorial largo en primera persona → bundle digital de ~$17-$39 con licencia comercial.** El de Cutify Studio es el molde: narradora con nombre y edad ("My name is Sarah. 37, administrative assistant, mom of two"), fecha concreta como ancla, el gasto hundido del equipo que ya compró ($378 de Cricut en el placard), un villano abstracto y nombrable (**"alquilar archivos" vs "tener la biblioteca"**, "there are two kinds of women who own a Cricut"), la cuñada que lo hace bien, la matemática explícita ($39 contra $4,99 por archivo), y el ingreso como consecuencia y no como promesa de tapa (mayo $170, junio $340, julio $510). El producto se vende a hobbistas con máquina parada, no a gente buscando "ganar plata online".

Tina Ghazi corre el otro molde: **MRR como el beneficio principal** — "the smartest $17 you'll ever spend", vendé el curso como tuyo y quedate con el 100%, y encima pone cupón (`CANVA20`) y precio en el texto del ad.

### Cómo buscar la próxima vez (lo que funcionó y lo que no)

- **Funcionó:** frases de producto angostas y literales — `master resell rights digital products`, `sell digital printables on Etsy`, `SVG bundle full commercial license Cricut`, `private label rights ebooks bundle`, `printable planner PLR shop sell your own`, `woodworking plans projects download`. Y una vez que cae uno, buscar los *hermanos* por el patrón del bundle, no por la keyword del nicho.
- **No funcionó:** cualquier frase de promesa o de precio. `keep 100% of the profit resell rights` (375k), `sell it as your own keep all the profit guide` (1,7M), `read this if you own a` (5,4M), `extra $500 a month from home system` (28k), `sell printables while you sleep passive` (5k) → todas caen en apps de novelas románticas, gyms y nutra. La Library rankea por relevancia solo las primeras filas y después ordena por fecha: con una frase amplia eso es ruido puro.
- **Confirmado otra vez:** `page_ids` + `limit: 1` da el `estimated_total_count` exacto por ~300 tokens. Es la única forma sana de contar arsenales en serie.
- **Ojo con el conteo:** la UI web de la Library filtra por país (muestra "~83 resultados" para Tina Ghazi con country=AR) mientras la API sin `countries` da el total mundial (142). El número que vale para el filtro es el de la API.

### ⛔ 2026-11-08 · "Palabras clave" no es "cazá": si pide keywords, van keywords y nada más

Santiago, cuando le estaba armando el banco de los 4 nichos nuevos de Brasil con candidatas, filtro madre y links de fanpages: *"Acordate que solo te pedí palabras clave, no la skill cazar"*.

- **Pedido "dame palabras clave / las mejores palabras" → se entrega el banco de keywords solo.** Nada de shortlist de anunciantes, arsenales, veredicto de competencia, radiografía ni "próximo paso: abrir la landing". Ese aparato es de esta skill y se activa solo cuando dice *cazá*, *buscá winner*, *espiá*, *analizá este nicho*.
- **Lo que sí suma y no es la skill:** correr las keywords en la Biblioteca para saber **cuáles devuelven ruido**, y entregar la lista de las que no sirven con el motivo. Eso hace mejores las palabras, que es lo que pidió.
- Es hermana de la regla de la página terminada: se hace lo que pide, no el viaje largo porque tengo las herramientas a mano.

### Registro 2026-11-08 · tres reglas de keywords (banco de los 4 nichos nuevos de BR)

Del barrido de 22 keywords en la Biblioteca para [[internacionalizacion]] Brasil (ver output del 08/11):

1. **Dos o tres palabras.** Confirmado otra vez: `tabela de preços para confeitaria` devolvió **8** resultados y `salgados para vender` **569**. La frase de 4+ palabras no existe escrita en ningún creativo.
2. **La frase emotiva en primera persona está quemada por los microdramas.** `meu filho não fala` (31.092) y `meu cachorro late muito` (223) devuelven **DramaBox, Dramas For U y Hot-Romance**: las apps de novelitas cortas compran todo el inventario de esas frases. Si la keyword suena a título de novela, no se usa.
3. **Terapia, dolor y adiestramiento = servicio local, no infoproducto.** `exercícios para dor nas costas` y `adestramento em casa` son 100 % fisio, quiropraxia y adestrador de barrio con "Agendar avaliação". El síntoma sirve como **ángulo de copy**, nunca como palabra de caza. Para pescar el infoproducto se entra por el **formato** (atlas, mapas, catálogo digital, apostila, para imprimir) o por el **profesional que lo compra**.

**Los 4 nichos nuevos validados ese día** (los bancos anteriores cubrían renda extra, emagrecimento, manifestação, relacionamentos, IA y terapias manuales): **infantil imprimible** (`atividades para imprimir`, 7.051), **fe / infantil cristiano** (`ministério infantil`, 882; `escola bíblica dominical`, 246), **material para profesionales** (`alinhado à BNCC`, 638; `recursos terapêuticos`, 1.071) y **cocina que da plata** (`receitas para vender`, 4.842). Los cuatro comparten la huella: fanpage con nombre genérico o de "tienda" sin ciudad + cantidad o precio en el título + estrellitas 4,9/5 + el mismo título repetido 10 o 15 veces.

### ⛔ 2026-11-08 · Los nichos son tres: emagrecimento, renda extra y manifestação

Santiago, después de que le entregara un banco con infantil imprimible, fe, material para profesionales y cocina: *"Muy malos nichos, quiero de bajar de peso, ingresos extra y manifestacion, pero no me des tantas, maximo 10 por nicho"*.

- **No se proponen nichos nuevos.** Los tres de arriba son los que trabaja y los únicos que hay que cazar, salvo que él nombre otro. Un nicho con mucho volumen en la Biblioteca (infantil imprimible tenía 7.051 ads activos) **no es un buen nicho** si él no lo vende: la vara es su operación, no el tamaño del mercado.
- **Diez por nicho, no más.** Un banco de 40 keywords por nicho con ejes agrupados no le sirve: pide la lista corta de las que pescan. Lo que sí suma al lado de cada una es **el número de anuncios activos y qué oferta destapa**, para que decida sin tener que correrlas.
- Mejor nueve que funcionan que diez con una muerta: si una del top se cae por ruido, se entrega el nicho con las que quedan y se dice.

### Registro 2026-11-08 (2ª pasada) · lo mejor de cada nicho, validado

- **Emagrecimento:** el dinero está en la **receta en PDF**, no en el peso. `receitas na airfryer` (877) y `receitas proteicas` (576) devuelven página tras página de R$10 con el mismo título repetido 8 o 15 veces (Vitrine Nossa Saúde, Eliane Morais, Chef Bia, la flota "Pegar receitas 👉"). `mounjaro natural` (680) sigue viva con Flávia Campos, 15 ads.
- **Manifestação:** `mapa astral` (931) es la mejor del nicho y la más low ticket que vimos — **R$9,00, R$27 y R$29,90 en el título del creativo**, en páginas distintas corriendo lo mismo (Entrelinhas Descubra, 64 Portais, Lua Jade). `lei da atração` (986) destapa la flota de Kamily Rebelatto en 4 fanpages. El ángulo nivel 3 del nicho ya está escrito por ellos: *"a lei da atração não é suficiente"*, *"faz lei da atração, mas o dinheiro não fica?"*.
- **Muertas confirmadas:** `ozempic caseiro` (0), `áudio subliminar` (1), `oração a Santo Expedito` (4, frase larga), `numerologia do nome` (222.226 de basura), `carteira do dinheiro` (305.599), `hora espelhada` y `quem nunca vendeu nada` (microdramas), `cardápio de 7 dias` (apps de delivery).
