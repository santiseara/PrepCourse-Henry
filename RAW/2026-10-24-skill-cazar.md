---
name: cazar
description: Busca productos winner en Facebook Ads Library en todo el mundo y te trae los mejores anunciantes (50+ ads activos corriendo hace 3+ días). Usar cuando el usuario dice "cazar", "buscar winner", "buscar whales", "analizar nicho" o "espiar ads".
---

# Cazar winners en Ads Library

Skill autónoma. El argumento es el **nicho o keyword** a investigar (ej: "recetas keto", "IA para abogados"). No depende de ninguna otra skill ni de carpetas previas: corre sola y devuelve la shortlist en el chat (y guarda un `.md` si el usuario quiere).

## Qué hace por defecto

1. **Busca en TODO EL MUNDO** (sin filtro de país).
2. Agrupa los resultados por anunciante y cuenta cuántos ads activos tiene cada uno.
3. Se queda con los **winners duros**: anunciantes con **50+ ads activos** sobre la misma oferta, corriendo hace **3+ días**.
4. Los rankea por señales de escala y te devuelve la shortlist con link a la landing, cantidad de ads, antigüedad y el ángulo que están usando.

## Requisito ⚠️

Usa la herramienta **`ads_library_search` del conector oficial de Meta** (el de Facebook — NO un MCP de terceros). Tenés que tenerlo **instalado** y con al menos una cuenta de ads activa en la sesión. Si está diferida, cargarla con ToolSearch.
- Es **solo lectura**: no toca tu cuenta ni crea nada → cero riesgo de baneo.
- **Fallback sin conector**: si no lo tenés instalado, hacé la caza a mano en `facebook.com/ads/library` (Chrome MCP o captura de pantalla) con los mismos filtros y la misma lectura de señales. Más lento, pero funciona.

## Paso 1 — Barrido mundial

Llamar a `ads_library_search` con:
- `search_terms`: **una** keyword o frase por llamada (es el texto del creativo). Para probar N variaciones → N llamadas. Correr 3-5 variaciones del nicho (español + portugués + inglés si aplica).
- `countries`: **omitirlo** → busca en todos los países. Así cae el whale que se esconde detrás del snapshot de un solo país.
- `ad_active_status`: `ACTIVE` (default de caza; usar `ALL` si querés ver también los que pausaron).
- `limit`: hasta 50.
- `advertiser_request`: el pedido del usuario con sus palabras (ej: "cazá recetas keto").

Generar keywords por 4 ejes: **formato** (ebook, guia, plantilla, kit, método, protocolo...), **disparadores de compra impulsiva**, **footprints técnicos** (dominios de Hotmart/Gumroad/Payhip como `search_terms` — si el dominio aparece en el texto del creativo, cae) y **keywords del nicho traducidas**. Para Brasil funcionan: método, segredo, desafio, renda extra, secar barriga, reconquista, passo a passo.

De cada ad la tool devuelve: texto del creativo, página, **fecha de creación** y `ad_snapshot_url` (vista visual del ad).

## Paso 2 — Contar el arsenal de cada anunciante

Del barrido salen páginas candidatas. Para cada anunciante prometedor, llamar de nuevo a `ads_library_search` con `page_ids: ["<id de la página>"]` → devuelve **TODOS** los ads de esa página. Con eso se cuenta el arsenal real y se ve la antigüedad del más viejo.

**El filtro madre (winner duro):**
- **50+ ads activos** sobre la MISMA oferta, y
- el ad más viejo activo arrancó hace **3+ días** (lo que arrancó hoy es un tester validando; lo que lleva 3+ días corriendo ya está vendiendo).

> La tool no filtra por fecha: trae la fecha de creación de cada ad → filtrar en el análisis, quedándose con los que llevan 3+ días. Descartar los que arrancaron hoy.

## Señales de winner — escalera de certeza

Cuanto más arriba, menos apuesta:
- **Nivel 1 — convierte**: 8+ ads activos con antigüedad de 4-20 días.
- **Nivel 2 — escalando**: ~30 ads sostenidos 3+ días.
- **Nivel 3 — WHALE (la casi-segura)**: **50-100+ ads activos** sobre una misma oferta, y/o los mismos ads corriendo **45-90+ días** sin pausa. Nadie banca gasto perdedor 2-3 meses: la longevidad sostenida es la prueba de rentabilidad más dura que da la Library. Al detectar un whale, ir a profundidad: enumerar todo su arsenal con `page_ids`, mapear landings, precios y ángulos.
- **Duplicación de creativos**: el mismo creativo repetido 10-20 veces = ese ya ganó el test interno del anunciante. Anotar esos `ad_snapshot_url` aparte — son los ángulos a modelar primero.
- Todos los creativos apuntando a la MISMA landing (si apuntan a landings distintas, todavía está testeando).
- Sin "follow me ads" (perfiles que solo juntan seguidores no venden).
- Misma oferta corriendo en 5-10 fanpages distintas = se esconde de los cloners → convierte seguro.
- Descartar marcas personales (no modelables) y fanpages con "fronts" duplicados que no gastan.

## Veredicto de competencia

Contar cuántos anunciantes distintos atacan la misma promesa:
- **ENTRAR**: 2-6 anunciantes activos con gasto sostenido y ninguno domina → demanda validada y espacio.
- **SUBNICHO**: 7+ anunciantes con creativos muy parecidos → validado pero saturado. Proponer 3 subnichos concretos (mismo dolor, avatar más específico).
- **DESCARTAR**: 0-1 anunciantes o ads que mueren a los pocos días → demanda no validada.
- **WHALE DOMINANTE**: un jugador domina con señales de Nivel 3 → no competirle de frente en su mercado. Modelar su oferta y lanzarla traducida en otro mercado con hueco (ver abajo).

## (Opcional) Arbitraje multi-mercado

Si encontrás un winner fuerte, chequeá si el mismo ángulo está libre en otro mercado. Repetir la búsqueda con `countries: ["<ISO-2>"]` traduciendo el término:
- 🇧🇷 Brasil (`["BR"]`) — suele ser la cuna de las olas low-ticket → mercado FUENTE
- 🇺🇸 EE.UU. (`["US"]`), 🇮🇹 Italia (`["IT"]`), 🇫🇷 Francia (`["FR"]`), 🇲🇽/🇪🇸 español

**Orden de prioridad de destino**: 1) inglés, 2) Europa (IT/FR/DE), 3) LATAM, 4) Brasil. Se **modela** desde el mercado fuente (saturado, funnels maduros) y se **lanza** en un destino con 0-3 players débiles. Si en el destino ya aparecen testers con ads de pocos días, la ventana se está cerrando.

## Output

Devolver en el chat la **shortlist rankeada de 3-5 anunciantes** que pasaron el filtro (50+ ads, 3+ días), cada uno con:
- Nombre de la página + link a su Ads Library y a la landing
- Cantidad de ads activos y antigüedad del más viejo
- Tipo de producto y precio si es visible
- Hook/ángulo principal (el dolor que atacan = lo validado)
- Los `ad_snapshot_url` de los creativos más duplicados (esos son los ángulos a modelar primero)

Cerrar con el veredicto (ENTRAR / SUBNICHO / DESCARTAR / WHALE) y, si aplica, el par mercado fuente→destino. Si el usuario quiere, guardar todo en un `01-caza.md`.

**Score de 4 señales** para rankear (1 punto c/u): ① longevidad — mismos ads 45+ días; ② volumen — 50+ ads de un solo jugador sobre la misma oferta; ③ duplicación — mismo creativo repetido 10+ veces; ④ hueco de arbitraje — sin equivalente fuerte en un mercado destino prioritario. **4/4 = candidata A** (examen aprobado, copiala); 3 = candidata B; ≤2 = observar, no entrar todavía.

Recordatorio: el whale valida la **OFERTA**, no te salva de un test sucio. Landing degradada, pixel ciego o un solo conjunto queman igual — cuando lances, armá el test en serio.
