# Método V3 — estructura de campañas

> La estructura base de hoy: una CBO por oferta y por cuenta, un conjunto por tanda con 5 a 10 anuncios distintos, renovaciones dentro de la misma campaña, campaña de winners y lanzamiento con un solo interruptor. (fuente: RAW/2026-10-10-wiki-previa/metodo-v3.md)

**Una campaña CBO por oferta y por cuenta. Adentro, un conjunto por tanda de creativos. En cada conjunto, de 5 a 10 anuncios distintos.** Las renovaciones no abren campañas nuevas: entran como un conjunto nuevo dentro de la campaña que ya está corriendo.

Es la estructura con la que se montan hoy todas las ofertas. Las demás estructuras de [[escalado-en-meta-ads]] siguen existiendo, pero se usan sobre esta base, no en lugar de ella.

## Por qué existe: la cola de duplicados

El patrón anterior era duplicar campañas y conjuntos con el mismo creativo y matarlos a los ~20 USD de gasto. Medido en cuatro ofertas reales durante una semana:

| | Cola (anuncios duplicados con poco gasto) | Núcleo (anuncios con gasto real) |
|---|---|---|
| Parte del gasto | **25% a 75%** según la oferta | el resto |
| ROAS | **0,23 a 0,99** | **1,10 a 1,69** |

En total, la cola se comió más de la mitad de lo que ganaba el núcleo. En una de las ofertas, **42 de 46 campañas duplicadas no hicieron ni una venta** y quemaron el 16% del presupuesto semanal. Un mismo creativo llegó a aparecer **7 veces** en conjuntos distintos.

Después de pasar a V3, la cola bajó al **5–10% del gasto** en las mismas ofertas. V3 corta el problema de raíz: una campaña, un conjunto por tanda, anuncios distintos adentro. No hay duplicados que repartan el presupuesto.

## La estructura

```
Campaña   V3 · <Producto> · <Cuenta>       CBO · Ventas · Compra · Volumen más alto
 ├─ Conjunto  18-9     → 5 a 10 anuncios (18/9 - 1 … 18/9 - 10)
 ├─ Conjunto  20-9     → la tanda siguiente
 └─ Conjunto  22-9     → y así, una por tanda
```

La notación es **Campañas-Conjuntos-Anuncios**: V3 es una **CBO 1-1-5** o **1-1-10** que va sumando conjuntos. Ver [[estructuras-cbo]] y [[nomenclatura-del-metodo]].

### Campaña

- Objetivo **Ventas**, conversión en el **sitio web**, evento **Compra**.
- **CBO**: el presupuesto va a nivel de campaña.
- Estrategia de puja: **Volumen más alto**, sin tope de costo.
- Presupuesto de referencia en las ofertas actuales: de **90 a 500 USD por día**, según la cuenta y el mercado.

### Conjunto

- País o países del mercado (Tier 1, LatAm o un país solo; ver [[internacionalizacion]]).
- Edad **18–65**.
- **Advantage+ Audience activado**, salvo cuando el producto exige un filtro duro de género. Con Advantage+ activado, el género es solo una sugerencia y Meta lo entrega igual al otro. Si el producto es solo para mujeres o solo para hombres, **hay que apagarlo**.
- Ubicaciones automáticas. Si aparecen errores de "entrega inestable" o problemas de tracking, probá sacar **Threads**.
- Atribución de **7 días clic + 1 día visualización**.
- **DSA obligatorio** si algún país del conjunto es de la Unión Europea (España, Irlanda, Francia…). Se completa con el nombre de la Página que anuncia.
- Hora de inicio: **00:00 del mercado objetivo**.

### Anuncio

- Video o imagen **único**. En video, **9:16**.
- Título con prueba social, por ejemplo `⭐️⭐️⭐️⭐️⭐️ 4.9/5`.
- Botón de llamada a la acción: **Más información**.
- Link con los UTMs dentro de la URL (ver [[nomenclatura-del-metodo]]).
- Si la tanda se sube por catálogo, ver [[subir-ads-con-metodo-catalogo]].

## Renovaciones: siempre en la misma campaña

**Cada tanda nueva de creativos es un conjunto nuevo dentro de la campaña que ya corre**, con el nombre de la tanda. Nunca va en una campaña paralela.

- El conjunto nuevo **clona la configuración del que ya entrega**: segmentación, pixel, evento de optimización y atribución.
- Es una decisión de método. No se reevalúa en cada tanda, aunque la CBO tenga que repartir el presupuesto con el conjunto nuevo.
- Una tanda = un conjunto. Si llegan 10 anuncios de dos tandas distintas, van en **dos conjuntos de 5**. Un conjunto no puede llevar dos fechas.

## La campaña de winners

Cuando una oferta ya tiene ganadores claros, se abre en otra cuenta una campaña que **solo tiene los winners**:

- Campaña `V3 · <Producto> · <Cuenta> — Winners`, CBO, Volumen más alto, **250 USD por día** como referencia.
- **Un solo conjunto**, `Winners · Broad 18-65`, con la misma configuración estándar de la oferta.
- Adentro, los **6 a 10 mejores anuncios** por ROAS de 7 días, **clonados por post ID** desde la cuenta donde nacieron. Así conservan los likes y comentarios.
- **Cuidado con los ROAS altos de muestra chica.** Un anuncio con ROAS 5 y 24 USD de gasto no es un winner, es ruido.

## Escalar la V3: surfeo cada 2 horas

La campaña V3 se puede **surfear cada 2 horas, siempre que mantenga un ROAS mayor a 2–2,5**:

- Si sostiene ese ROAS, **duplicá el presupuesto** (o subilo 50%) y esperá 2 horas para la próxima decisión.
- Nunca con 1 venta: esperá **3 a 5 ventas** con ese ROAS antes de subir.
- Si el ROAS baja de 2, dejá de subir. Al final del día, volvé al presupuesto base o dejalo un escalón arriba si el día cerró muy bien.
- Detalle del surfeo en [[escalado-en-meta-ads]].

## Cuándo juzgar

- **Un anuncio suelto en testeo** se corta con la regla de [[testeo-de-creativos]] (al CPA medio o al break-even sin ventas).
- **Una campaña o un conjunto V3 entero no se juzga antes de gastar 2 o 3 veces el CPA objetivo.** Con un CPA de 42 USD, cualquier veredicto antes de 90–135 USD de gasto es ruido.
- **El creativo y la concentración del presupuesto pesan mucho más que el tipo de campaña.** Entre CBO 1-1-1, CBO 1-3-1 y ABO 1-1-1, los anuncios con gasto real rinden parecido. La diferencia la hace la cola.
- Las CBO se leen **a nivel campaña**, nunca conjunto por conjunto ([[escalado-en-meta-ads]]).
- Los ROAS del pixel de Meta vienen inflados frente a UTMify. Sirven para ordenar de mejor a peor, no como valor real ([[tracking-y-atribucion]]).

## Operativa multi-cuenta

- **Una cuenta master por producto.** Los videos se suben una sola vez y los anuncios se arman en esa cuenta. El resto de las cuentas los **clonan por post ID**, sin volver a subirlos. Solo hace falta que la cuenta destino y la Página estén en el **mismo Business**. La prueba social se concentra en un solo post.
- **No todos los winners tienen post ID.** Un anuncio armado directo sobre el video, sin publicación de Página detrás, no se puede clonar. Antes de perder acceso a una cuenta, separá los creativos que tienen post ID de los que no, y **bajá el MP4 de los que no**. Una cuenta deshabilitada todavía deja leer y descargar. Si salís del Business, ya no.
- Si la Página original se pierde, los videos siguen en la cuenta. Se pueden crear anuncios nuevos con la Página actual y clonar esos, pero la prueba social arranca de cero.
- Ver [[contingencia-de-cuentas]].

## Lanzamiento: un solo interruptor

Dejá los **conjuntos y los anuncios en ACTIVO** y **solo la campaña en PAUSA**. Así, lanzar es prender una sola cosa. Después de crear o editar algo, **verificá siempre el estado real** en el administrador. Meta a veces deja activo algo que figuraba en pausa.

Relacionado: [[estructuras-cbo]] · [[nomenclatura-del-metodo]] · [[testeo-de-creativos]] · [[escalado-en-meta-ads]] · [[renovacion-de-creativos]] · [[subir-ads-con-metodo-catalogo]]

## Conexiones con tu operación actual
- **La tanda pasa a ser de 5 a 10 anuncios.** La regla de "3 guiones por tanda" ([[guiones-y-anuncios]]) es la base creativa. Para llenar un conjunto V3 hacen falta 5 a 10 anuncios: 3 guiones × hooks o B-rolls distintos, o una tanda aparte de natives. **Sin mezclar imagen y video** en la misma tanda ([[estructuras-cbo]]).
- **"Más información" es tu CTA.** El guión 3 de [[scented-stones]] cierra con "Tap Learn more": coincide con el botón estándar de V3.
- **Advantage+ y género:** piedras le habla a mujeres, pero no es un producto exclusivo. Por defecto Advantage+ queda activado. Solo se apaga si decidís un filtro duro.
- **Un solo interruptor + verificar el estado real** coincide con la regla de [[claude-con-meta-ads]].

## Los números exactos del manual (3/11/2026)

Desde el 3/11 está instalada la skill **`manejo-cbo`**, el Manual de Manejo de la CBO de Launch Expert ([[skills-launch-expert]]). Confirma toda esta página y le pone números a lo que acá estaba en palabras:

- **Objetivo de la V3, con número:** la mayor cantidad de conjuntos con **más de 50 ventas en menos de 7 días**. Por eso no se toca el conjunto que viene bien.
- **Con cuánto arrancar, en tickets:** oferta nueva lento **2-3 tickets** · oferta nueva rápido **10-15** · oferta validada en cuentas nuevas **2-3** (5-10 con confianza). Una oferta ya validada se lanza directo en **3 cuentas**.
- **Los primeros 3 días:** día 1 con ROAS negativo → **bajar 30 %** y seguir bajando de a 30 % hasta encontrar el equilibrio de la cuenta · día 2 flojo → **sumar renovaciones** · con ROAS **positivo no se apagan anuncios** (saca al conjunto del aprendizaje); con ROAS negativo sí se puede.
- **El gasto mínimo de la renovación:** **1 ticket por día** (o 5-10 % de la CBO), **durante 3 días, y después se saca**, venda o no. Los mínimos activos no deberían pasar el **~20 % de la CBO**, y si bajás la CBO hay que revisar que no queden mínimos viejos trabando el presupuesto.
- **Ritmo del surfeo atado al presupuesto** (acá decía "cada ~2 horas"): CBO **debajo de 500 USD/día → +30 % cada 3-4 h** · **arriba de 500 USD/día → +30 % una vez por día**, porque a partir de ahí cada 30 % ya son más de 100 USD.
- **La tabla ayer/hoy:** ayer bueno (2+) y hoy bien → **+30 %** · ayer bajo y hoy mejor → **quieta, ni subir ni bajar** · ayer bajo y hoy mal → **−30 %** (tirarle la oreja) · los dos muy buenos (2,5-4) → surfeo agresivo y volver a mirar en 3-4 h.
- **El techo de la cuenta:** si a 2.000 USD/día rinde y a 2.600 el ROAS se cae, el techo está cerca de 2.000. No se fuerza esa cuenta, se abren otras.
- **Pujas manuales con oferta súper validada:** presupuesto **20-30 tickets** · Cost Cap inicial = **front ÷ 2 + 30 %** · Bid Cap inicial (ABO, 7 conjuntos) = **front × 1,3** en Argentina, **de 17 a 24 USD** en el mercado inglés · si quema sin ventas, **−1 USD y esperar 2 h**; si no gasta, **+1 USD y esperar 2 h**. Siempre en cuentas nuevas.
- **Leer los números:** ROAS de ventas **aprobadas** (las pendientes de tarjeta que siguen pendientes son checkouts abandonados), con comisiones cargadas (~8-10 % → el equilibrio real queda en ROAS ~1,10). El ROAS del pixel viene inflado: sirve para ordenar, no como valor.
- **Cuenta master por producto:** subir los videos y armar los anuncios en una sola cuenta y clonarlos en las demás por ID de publicación, para conservar la prueba social.

El bot que automatiza este surfeo es la skill **`surfing-scale`** (±30 %, horarios por oferta, confirmación SI/NO por WhatsApp, ROAS solo de Impultienda) — ver [[skills-launch-expert]].

## Fuentes
- RAW/2026-10-10-wiki-previa/metodo-v3.md (página de la wiki previa, actualizada el 2026-09-24)
- Fuentes originales citadas (todavía no están en este cerebro): operación real en Meta Ads, septiembre 2026; estructura V3 de Grupo Firgon
