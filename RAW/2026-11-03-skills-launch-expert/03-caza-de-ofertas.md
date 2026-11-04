# Manual de Caza de Ofertas · Launch Expert Academia

> Pegá este archivo entero en tu segundo cerebro (proyecto de Claude, Obsidian, Notion o el CLAUDE.md de tu carpeta).
> Después escribile a tu IA: **"Cazá ofertas de [nicho] siguiendo el Manual de Caza de Ofertas."**
> Ejemplos: "Cazá ofertas de bajar de peso", "Cazá ofertas de reconquista", "Cazá ofertas de ingresos extra con IA".
> Los nichos y palabras de este manual son ejemplos de búsqueda, no recomendaciones de ofertas puntuales.

---

## 0. Instrucción para la IA que lee este archivo

Sos mi cazador de ofertas. Cuando te diga "cazá [nicho]":
1. Usá la herramienta **`ads_library_search` del conector oficial de Meta** (Facebook). Si está diferida, cargala. Es solo lectura: no toca ninguna cuenta. Si no está instalada, hacé la búsqueda en `facebook.com/ads/library` con el navegador, con los mismos filtros.
2. Seguí los pasos de las secciones 3 a 9 **en orden**, sin saltear filtros.
   **La base para seleccionar una oferta es siempre: más de 40 anuncios activos durante más de una semana.** Lo que no llega, no se recomienda.
3. Buscá primero en los **mercados fuente** (los más sofisticados) y verificá el hueco en los **mercados destino** (los menos sofisticados). Sección 1.
4. **Abrí siempre la landing y el checkout** antes de recomendar algo: el volumen de anuncios solo no alcanza (sección 7).
5. Entregame el reporte con el formato de la sección 11 y cerrá con un veredicto. Si un dato no lo pudiste confirmar, marcalo como "no confirmado".
6. Nunca hagas una compra de prueba sin mi OK explícito.

---

## 1. La estrategia: grandes nichos, grandes mercados, arbitraje de sofisticación

**Qué buscamos:** ofertas de calidad (low ticket, digital, con embudo maduro) en los **grandes nichos**, para lanzarlas en **grandes mercados**.

| Gran nicho | Subnichos típicos |
|---|---|
| **Dinero** | ingresos extra, negocios desde casa, IA para ganar plata, oficios, emprendimientos manuales |
| **Salud y cuerpo** | bajar de peso, energía, movilidad, belleza, rutinas para +40/+50/+60 |
| **Relaciones** | reconquista, pareja, seducción, autoestima, vínculos familiares |

Estos nichos tienen demanda enorme y permanente en todos los países. El dolor es el mismo en todos lados; lo que cambia es **cuántas promesas ya escuchó el público**.

**El arbitraje:** espiamos en **mercados muy sofisticados** (donde los anunciantes tuvieron que inventar mecanismos únicos cada vez más avanzados para seguir vendiendo) y lanzamos en **mercados menos sofisticados** (donde ese nivel de mecanismo todavía no llegó y una oferta así se ve nueva).

| Rol | Mercados | Por qué |
|---|---|---|
| **Fuente** (dónde espiar) | Brasil, Estados Unidos y el mundo anglo; en algunas verticales Corea y Japón | Mucha competencia, embudos maduros, mecanismos únicos muy trabajados. Las olas low ticket suelen nacer acá |
| **Destino** (dónde lanzar) | Latinoamérica hispana, España, Europa no anglo (Italia, Francia, Alemania, Portugal, Polonia…), y el mundo anglo cuando la fuente es Brasil | Menos competencia directa y público que todavía no vio ese mecanismo |

> **La regla:** no inventes ofertas. Encontrá la que ya está ganando en un mercado más sofisticado, entendé su mecanismo y llevala a un mercado donde todavía nadie la hace bien.

---

## 2. Los niveles de sofisticación de un mercado

Cuantas más ofertas vio un público, más escéptico es y más elaborado tiene que ser el mensaje. Así se reconoce cada nivel mirando los anuncios:

| Nivel | Qué ves en los anuncios | Qué funciona |
|---|---|---|
| **1. Virgen** | Casi nadie vende eso; anuncios simples | La promesa directa ("bajá de peso en casa") |
| **2. Promesa ampliada** | Varios anunciantes con la misma promesa, cada uno más grande | Promesa más fuerte, más rápida o más específica |
| **3. Mecanismo** | Ya no alcanza la promesa: aparecen el "cómo" y el "por qué" | Un mecanismo con nombre ("el método X", "el protocolo de 4 pasos") |
| **4. Mecanismo ampliado** | Muchos mecanismos compitiendo | Mecanismo más nuevo, más simple o más completo |
| **5. Identificación** | El público está saturado y desconfía de todo | Historias, identidad, avatar muy específico, quizzes personalizados |

**Cómo usarlo:**
- En el mercado **fuente**, buscá ofertas de nivel 3-5: ahí están los mecanismos únicos más avanzados.
- En el mercado **destino**, medí en qué nivel está ese nicho mirando a los competidores locales. Si están en nivel 1-2, un mecanismo de nivel 3-4 traído de afuera se ve nuevo y gana.
- **No subas de más el nivel**: en un mercado de nivel 2, un mensaje de nivel 5 confunde. Simplificá el mecanismo lo justo para que se entienda.

---

## 3. Elegir nicho y armar las palabras de búsqueda

`ads_library_search` busca en el **texto del anuncio**. Hacé **una palabra o frase por búsqueda** y corré entre 5 y 10 variaciones, en el idioma de cada mercado fuente.

**Armá las palabras por 4 ejes:**
1. **Formato del producto**: guía, ebook, método, protocolo, desafío, kit, plantillas, curso, programa.
2. **Disparadores de compra impulsiva**: secreto, paso a paso, en 7 días, sin gimnasio, desde casa, para principiantes.
3. **Huellas técnicas**: dominios de plataformas de pago o de quiz que aparecen en el texto (Hotmart, Kiwify, ClickBank, Gumroad, Payhip…).
4. **El nicho traducido**: la misma idea en portugués, inglés y el idioma del destino.

**Ejemplos de palabras por idioma (para arrancar):**
| Idioma | Dinero | Salud | Relaciones |
|---|---|---|---|
| Portugués | renda extra, trabalhar em casa, método, passo a passo | secar barriga, desafio, protocolo, emagrecer | reconquista, conquistar, relacionamento |
| Inglés | side hustle, make money, step by step, blueprint | lose weight, challenge, protocol, over 50 | get your ex back, attraction, relationship |
| Español | ingresos extra, trabajar desde casa, método | bajar de peso, desafío, protocolo, después de los 50 | recuperar a tu ex, pareja, conquistar |

---

## 4. Paso 1: barrido mundial

Llamá a `ads_library_search` con:
- `search_terms`: una palabra o frase por llamada.
- `countries`: **omitilo** para buscar en todo el mundo (así aparece el anunciante grande que se esconde detrás de un solo país). Después repetí en cada mercado fuente con su código (`["BR"]`, `["US"]`…).
- `ad_active_status`: `ACTIVE`.
- `limit`: hasta 50.

De cada anuncio anotá: texto, página, fecha de inicio y el link de vista previa (`ad_snapshot_url`).
**Agrupá por anunciante** y quedate con las páginas que repiten muchos anuncios sobre la misma oferta.

---

## 5. Paso 2: contar el arsenal de cada anunciante

Para cada página candidata, llamá de nuevo con `page_ids: ["<id de la página>"]`: trae **todos** sus anuncios. Contá:
- Cuántos anuncios activos tiene **sobre la misma oferta**.
- Desde cuándo corre el anuncio activo más viejo.
- A cuántas landings distintas apuntan.

**Filtro madre (la base para seleccionar una oferta):** **más de 40 anuncios activos** sobre la misma oferta, corriendo **hace más de una semana** (7+ días). Si no cumple las dos cosas, no se selecciona, por buena que parezca. Lo que arrancó hace pocos días todavía está en test; lo que sostiene 40+ anuncios más de una semana está vendiendo.

---

## 6. Señales de que la oferta gana

**Escalera de certeza** (todo arranca desde la base: menos de eso, se descarta):
| Nivel | Señal | Lectura |
|---|---|---|
| Debajo de la base | Menos de 40 anuncios, o menos de una semana corriendo | **No se selecciona.** Como mucho, se anota para volver a mirar |
| 1. **Base: oferta seleccionable** | **Más de 40 anuncios activos durante más de una semana** | Vende. Es el mínimo para considerarla |
| 2. Escalando | 40+ anuncios sostenidos **2-4 semanas**, sumando creativos nuevos | Vende y está invirtiendo más |
| 3. **Ballena** | 80-100+ anuncios sobre una misma oferta, y/o los mismos anuncios corriendo **45-90+ días** | Casi seguro rentable: nadie paga pérdidas 2-3 meses |

**Señales extra:**
- **El mismo creativo duplicado 10-20 veces**: ese ganó el test interno del anunciante. Guardá esos links aparte: son los ángulos a modelar primero.
- **Todos los anuncios van a la misma landing** (si van a varias, todavía está testeando).
- **La misma oferta en 5-10 páginas distintas**: se esconde de los que copian. Convierte seguro.

**Puntaje de 4 señales** (1 punto cada una):
1. **Longevidad**: los mismos anuncios 45+ días.
2. **Volumen**: 80+ anuncios de un solo anunciante sobre la misma oferta (la base de 40+ ya es obligatoria para entrar al puntaje).
3. **Duplicación**: el mismo creativo 10+ veces.
4. **Hueco de arbitraje**: no hay un equivalente fuerte en un mercado destino.

**4/4 = candidata A** (entrar) · **3/4 = candidata B** · **2 o menos = observar**.

---

## 7. Filtrar falsos positivos (no saltear)

Muchas "ballenas" no son lo que buscamos. **Abrí la landing y llegá hasta el precio** antes de recomendar:
- **Precio alto** (cursos de cientos de dólares) → no es low ticket.
- **Influencer o marca personal real** → no se puede modelar (vende la persona, no la oferta).
- **Producto físico o contra entrega** → otro negocio.
- **Páginas que solo juntan seguidores** ("seguime para más") → no venden.
- **Apps y juegos** que usan palabras parecidas → ruido.
- Si la landing es un quiz y no querés completarlo, buscá en el código de la página los links de checkout y los precios.
- La fecha de "activo desde" que muestra la biblioteca es la del anuncio más viejo **visible**, no necesariamente el inicio real.

---

## 8. Veredicto de competencia

Contá cuántos anunciantes distintos atacan la misma promesa en el mercado **destino**:
| Situación | Veredicto |
|---|---|
| 0-1 anunciantes en la fuente, o anuncios que mueren a los pocos días | **DESCARTAR**: demanda no validada |
| 2-6 anunciantes con gasto sostenido y ninguno domina | **ENTRAR**: demanda validada y espacio |
| 7+ anunciantes con creativos muy parecidos | **SUBNICHO**: validado pero saturado. Proponé 3 subnichos (mismo dolor, avatar más específico: edad, situación, profesión) |
| Un anunciante domina con señales de ballena | **MODELAR Y MUDAR**: no le compitas en su mercado; modelá la oferta y lanzala en un destino con hueco |

---

## 9. Paso 3: verificar el hueco en el mercado destino

1. Traducí las palabras clave de la oferta ganadora al idioma del destino y buscá con `countries: ["<código>"]`.
2. Mirá si existe la misma promesa o el mismo mecanismo. Contá anunciantes y antigüedad.
3. Medí el **nivel de sofisticación** del destino (sección 2).
4. Si ya aparecen testers con anuncios de pocos días, **la ventana se está cerrando**: hay que moverse rápido o elegir otro destino.
5. Buscá también el nombre del mecanismo en el idioma destino: si da cero resultados, el mecanismo no existe ahí todavía.

---

## 10. Radiografía de la oferta elegida

Cuando tengas la candidata A, desarmala entera:
- **Anuncios**: los 5-10 más duplicados y más longevos. Gancho literal de cada uno y qué dolor o deseo ataca. Un ángulo está **probado** cuando 3+ anunciantes distintos lo corren 14+ días.
- **Landing**: estructura, promesa, mecanismo (con nombre), prueba, oferta, garantía. Si hay quiz, cada pantalla.
- **VSL**: bajala y transcribila.
- **Precio**: precio tachado, precio real, cuotas, order bumps.
- **Post-compra**: OTOs y downsells (para recorrerlo, ver el Manual del Embudo Post-Compra, sección 2). Compra de prueba solo con OK.
- **Cómo pasa las políticas de Meta**: qué palabras evita, qué muestra y qué no.

---

## 11. Formato del reporte

Para cada anunciante de la shortlist (3-5 que pasaron los filtros):

| Campo | Qué poner |
|---|---|
| Página | Nombre + link a su biblioteca de anuncios |
| Mercado fuente | País e idioma |
| Arsenal | Anuncios activos sobre la oferta + antigüedad del más viejo |
| Producto y precio | Tipo de producto, precio real (o "no confirmado") |
| Mecanismo | El "cómo" que vende, con su nombre |
| Nivel de sofisticación | Del mercado fuente (1-5) |
| Ángulo principal | El dolor o deseo que ataca el creativo más duplicado |
| Creativos a modelar | Links de vista previa de los más duplicados |
| Puntaje | x/4 y por qué |

Cerrá con:
- **Veredicto**: ENTRAR / SUBNICHO / DESCARTAR / MODELAR Y MUDAR.
- **Par de arbitraje**: mercado fuente → mercado destino, con el nivel de sofisticación de cada uno.
- **Próximo paso**: qué radiografiar primero.

---

## 12. Modelar sin copiar

- **Se toma**: la promesa, el mecanismo (reescrito), la estructura del embudo, los ángulos probados y el rango de precio.
- **Es propio**: marca, nombre del producto, logo, dominio, página de Facebook, caras, voz, testimonios, el producto entregado y el guion.
- **El guion se reescribe** como habla el público del destino, no se traduce palabra por palabra.
- **Adaptá el mecanismo al nivel del destino**: más simple si el mercado está menos sofisticado.
- El precio lo fija el mercado destino, no la conversión del original.

---

## 13. Límites

- No uses marcas registradas ajenas (medicamentos, marcas famosas) en el nombre ni en los anuncios.
- En salud: nada de promesas médicas, curas ni cifras de resultado garantizadas.
- No copies archivos, textos literales, fotos ni testimonios de otros.
- La ballena valida **la oferta**, no te salva de un mal lanzamiento: landing rota, pixel mal puesto o un solo conjunto queman igual.

---

## 14. Checklist de caza

1. Nicho elegido dentro de un gran nicho (dinero, salud o relaciones).
2. 5-10 palabras de búsqueda armadas por los 4 ejes, en los idiomas de los mercados fuente.
3. Barrido mundial hecho y agrupado por anunciante.
4. Arsenal contado por página (anuncios activos, antigüedad, landings).
5. Filtro madre aplicado: más de 40 anuncios activos durante más de una semana.
6. Falsos positivos descartados abriendo landing y precio.
7. Puntaje de 4 señales calculado.
8. Hueco verificado en el mercado destino y nivel de sofisticación medido.
9. Reporte entregado con veredicto y par fuente → destino.
10. Radiografía de la candidata A hecha.