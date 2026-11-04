# Manual de Manejo de la CBO · Launch Expert Academia

> Pegá este archivo entero en tu segundo cerebro (proyecto de Claude, Obsidian, Notion o el CLAUDE.md de tu carpeta).
> Cuando le pidas a tu IA que arme, lea, escale o corte una campaña, decile:
> **"Seguí el Manual de Manejo de la CBO al pie de la letra."**
> "Ticket" = el precio del front de tu oferta. Todos los presupuestos se calculan en tickets.

---

## 0. Instrucción para la IA que lee este archivo

Sos mi media buyer y trabajás con el **método V3**: una sola campaña para testear, preescalar y escalar cada oferta.
1. **Leé la CBO a nivel campaña**, nunca conjunto por conjunto.
2. **Usá números reales**: ROAS de ventas **aprobadas**, sin sumar pendientes, con comisiones cargadas (sección 9).
3. **Una oferta nueva corre mínimo 3 días** antes de decidir si sirve (sección 4).
4. **Nunca subas más de 30 % de una vez.** Cada 3-4 horas si la CBO está debajo de 500 USD; una vez por día si está arriba (sección 6).
5. Para cada decisión, decime **qué regla de este manual aplicás** y con qué números (ROAS de ayer, ROAS de hoy, presupuesto actual, nuevo presupuesto).
6. **No cambies presupuestos, pujas ni estados sin mi OK.**

---

## 1. El método V3 en una frase

**Una campaña por cuenta publicitaria. Un conjunto. De 5 a 10 anuncios (mejor 10).** Con esa misma campaña se testea la oferta, se preescala y se escala surfeando el presupuesto. Las renovaciones entran como conjuntos nuevos dentro de la misma campaña.

```
Campaña   V3 · <Producto> · <Cuenta>      CBO · Ventas · Compra · Volumen más alto
 ├─ Conjunto  tanda 1   → 10 anuncios
 ├─ Conjunto  tanda 2   → renovación: 5 a 10 anuncios nuevos (con gasto mínimo)
 └─ Conjunto  tanda 3   → y así, una por renovación
```

**El objetivo:** encontrar la mayor cantidad de conjuntos con **más de 50 ventas en menos de 7 días**. Por eso no se tocan los conjuntos que vienen bien: cualquier cambio fuerte los saca de la fase de aprendizaje.

**Reglas fijas:**
- **Una campaña por cuenta publicitaria.** Nunca dos campañas iguales (mismo producto y mercado) en la misma cuenta. Para crecer a lo ancho, se abren **otras cuentas** (sección 7).
- La CBO se lee a nivel campaña. Que un conjunto no gaste no es un problema: Meta eligió.
- Ninguna estructura salva un embudo malo. Si los números no dan, el problema está en la oferta, la landing o el checkout.

---

## 2. Configuración de la campaña

| Nivel | Configuración |
|---|---|
| Campaña | Objetivo Ventas, sitio web, evento Compra. CBO. Puja **Volumen más alto**, sin tope |
| Conjunto | País o países del mercado. Edad 18-65. **Advantage+ Audience activado** (apagalo solo si el producto exige un género: con Advantage+ el género es una sugerencia). Ubicaciones automáticas. Atribución **7 días clic + 1 día visualización**. **DSA obligatorio** si hay un país de la UE. Inicio a las **00:00 del mercado** |
| Anuncio | Video o imagen único, 9:16. Título con prueba social (`⭐️⭐️⭐️⭐️⭐️ 4.9/5`). Botón **Más información**. Link con UTMs |

- **Lanzamiento con un solo interruptor:** conjuntos y anuncios en ACTIVO, solo la campaña en PAUSA. Lanzar = prender la campaña. Verificá el estado real de los tres niveles.
- **Programá a las 00:00**: le das a Meta el día entero para gastar en el mejor momento.

---

## 3. Con cuánto arrancar

| Caso | Estructura | Presupuesto de la CBO |
|---|---|---|
| **Oferta nueva, ir lento** | 1-1-10 en una cuenta | **2-3 tickets** (front de 27 USD → 50-75 USD/día) |
| **Oferta nueva, ir rápido** | 1-1-10 en una cuenta | **10-15 tickets** (front de 27 USD → ~270-400 USD/día) |
| **Oferta validada** (ya venía corriendo y dando ganancia) | 1-1-X en **cuentas nuevas**, X = los anuncios winners | **2-3 tickets**. Si tenés confianza, más arriesgado: **5-10 tickets** |
| **Expansión horizontal de un winner** | 1-1-X en cada cuenta nueva (sección 7) | **2-3 tickets**. Con confianza, **5-10 tickets** |

Una oferta validada conviene lanzarla directamente en **3 cuentas** a la vez.

---

## 4. Los primeros 3 días de una oferta nueva

**La campaña corre mínimo 3 días.** Por eso conviene arrancar con 10 anuncios. Se puede tocar antes de los 3 días, pero solo con estas reglas:

| Situación | Qué hacer |
|---|---|
| **Día 1 cierra con ROAS negativo** | **Bajá el presupuesto 30 %.** Si sigue mal, seguí bajando de a 30 % hasta encontrar el punto de equilibrio de la cuenta |
| **Día 2 sigue con ROAS malo** | **Sumá renovaciones**: un conjunto nuevo con 5-10 anuncios nuevos y gasto mínimo (sección 5) |
| **La campaña va con ROAS negativo o bajo** | Podés **apagar anuncios** que no venden |
| **La campaña va con ROAS positivo** | **No apagues anuncios.** Es un cambio significativo y saca al conjunto del aprendizaje |
| **Día 1 ya va bien** | Empezá a surfear (sección 6) |

**Validada** = pasaron 3 días, venís en ganancia, ya tiene el backend puesto, empezaste a surfear para arriba y responde bien. Recién ahí se expande a otras cuentas.

---

## 5. Renovaciones

1. **El conjunto que ya corre no se toca.** Se deja todo igual.
2. Agregás un **conjunto nuevo** dentro de la misma campaña con **5 a 10 anuncios nuevos**. Clona la configuración del conjunto que ya entrega (segmentación, pixel, evento, atribución).
3. Le ponés un **gasto mínimo** en el conjunto ("porcentaje mínimo de presupuesto" o mínimo diario), para que gaste sí o sí y testee los creativos nuevos.
   - **Por qué:** si la campaña tiene un conjunto con 100 ventas y le agregás uno nuevo, Meta le va a seguir dando casi todo el presupuesto al de 100 ventas. Sin mínimo, la renovación no se prueba.
   - **Cuánto:** **1 ticket por día** (o entre el 5 % y el 10 % de la CBO), durante **3 días**. Después se saca, venda o no.
   - Los mínimos activos no deberían sumar más del ~20 % de la CBO. Si bajás la CBO, revisá que no queden mínimos viejos trabando el presupuesto.
4. **Una tanda = un conjunto**, nombrado con la fecha del archivo del editor.
5. Se pueden agregar renovaciones antes de que la campaña cumpla 5 días si viene floja.
6. Cuando expandiste a otras cuentas, **renová en todas**: la de origen y las nuevas.

Con el mínimo bien puesto, es normal ver un conjunto de renovación metiendo sus propias ventas en las primeras 9-10 horas.

---

## 6. Escalar verticalmente: surfear el presupuesto

**Nunca más de 30 % por vez.**

| Presupuesto de la CBO | Ritmo |
|---|---|
| **Menos de 500 USD/día** | **+30 % cada 3-4 horas** mientras siga imprimiendo bien (agresivo) |
| **Más de 500 USD/día** | **+30 % una vez por día** (a partir de ahí cada subida pesa mucho: 30 % ya son más de 100 USD) |
| Opción tranquila, cualquier presupuesto | +30 % una vez por día |

**Cuándo subir:** la campaña viene estable con **ROAS mayor a 2**. Lo más claro es mirar **ayer y hoy**:

| Ayer | Hoy (a la mañana) | Acción |
|---|---|---|
| ROAS bueno (2+) | Viene bien | **+30 %** (ej. 439 × 1,3 = 570) |
| ROAS bajo (ej. 1,42) | Viene mejor (ej. 1,85) | **Dejala quieta.** Ni subir ni bajar |
| ROAS bajo | Viene mal | **Tirale la oreja: bajá 30 %** |
| Muy bueno (ej. 2,5-4) | Muy bueno | **Surfeo agresivo**: +30 % y volvé a mirar en 3-4 horas |

**Después de cada subida:**
- Mirá de nuevo en 3-4 horas. **Si sigue imprimiendo, subí otro 30 %.** Si el ROAS empieza a bajar, **dejala quieta**.
- Si baja un par de puntos, está bien: dejala correr igual.
- Si se cae, **bajá 30 %** (tirarle la oreja).

**El techo de la cuenta:** cada cuenta aguanta hasta cierto presupuesto. Si en 2.000 USD/día rinde y al subir a 2.600 el ROAS se cae, el techo de esa cuenta está cerca de 2.000: volvé a bajar 30 %. Para seguir creciendo no se fuerza esa cuenta, se abren otras (sección 7).

**No hace falta estar pegado a las campañas.** Un vistazo a la mañana, otro cada 3-4 horas si estás surfeando, y listo.

---

## 7. Escalar horizontalmente: otras cuentas publicitarias

**No dupliques la campaña en la misma cuenta.** La misma campaña va en cuentas distintas: cuenta 1, cuenta 2, cuenta 3, cuenta 4…

**Cómo se arma:**
1. **No copies la campaña entera** con todos sus conjuntos. Analizá los **winners** de todos los conjuntos de la campaña de origen.
2. En cada cuenta nueva lanzá una **1-1-X** con esos winners (ej. 5 winners → 1-1-5), clonados por ID de publicación para conservar la prueba social.
3. Presupuesto: **2-3 tickets**. Si tenés confianza en la oferta, **5-10 tickets**.
4. Cada cuenta nueva se maneja igual: surfeo vertical (sección 6) y renovaciones (sección 5).
5. Cuando renovás creativos, **renová en todas las cuentas** (la de origen y las nuevas).

**Cuándo expandir:** cuando la oferta está validada en la primera cuenta (sección 4). No hace falta esperar a llegar a 2.000 USD en una sola campaña. Una oferta que ya venía validada se puede lanzar directo en 3 cuentas.

**Cuenta master por producto:** subí los videos y armá los anuncios en una sola cuenta, y en las demás clonalos por ID de publicación. Antes de perder una cuenta, separá los anuncios que se pueden clonar de los que no (los armados directo sobre el video) y bajá esos videos.

---

## 8. Pujas manuales: Cost Cap y Bid Cap (oferta súper validada)

Cuando la oferta ya está súper validada y viene muy bien, además de las CBO de volumen más alto abrí **cuentas nuevas** con la misma estructura en puja manual. Siempre en cuentas nuevas.

| | **Cost Cap** | **Bid Cap** |
|---|---|---|
| Estructura | CBO 1-1-winners | CBO 1-1-winners |
| Presupuesto | **20-30 tickets** | **20-30 tickets** |
| Puja inicial | **front ÷ 2 + 30 %** (front 27 → ~17,5) | **front × 1,3** (front 27 → ~35) |

**Cómo se manejan (las dos igual):**
| Situación | Acción |
|---|---|
| Gasta y **quema sin ventas** | **Bajá la puja 1 USD** y esperá 2 horas. Si sigue quemando, bajá otro dólar y esperá 2 horas |
| **No gasta** | **Subí la puja 1 USD** y esperá 2 horas |
| **Gasta y vende** | **Surfeala** (sección 6) |

---

## 9. Leer los números de verdad

- **ROAS de ventas aprobadas.** Las pendientes de tarjeta que siguen pendientes días después son **checkouts abandonados**: nunca las sumes.
- **Cargá comisiones e impuestos** en tu tracker. Si están en 0, la ganancia que ves es bruta (con ~8-10 % de comisión, el equilibrio real queda en ROAS ~1,10).
- **Mirá el día de ayer cerrado y el de hoy**, filtrando por fecha. Las decisiones de surfeo salen de esa comparación.
- **El ROAS del pixel de Meta viene inflado** frente al tracker: sirve para ordenar, no como valor real.
- **Compará el CPM entre cuentas** antes de culpar al anuncio: con los mismos anuncios, una cuenta puede tener el CPM mucho más caro.
- **Un solo creativo sosteniendo casi todo el gasto** es una alarma: tené las renovaciones listas antes de que se fatigue.
- **Cuidado con los ROAS altos de muestra chica**: ROAS 5 con 24 USD de gasto no es un winner.

---

## 10. Rutina diaria

| Momento | Qué hacer |
|---|---|
| 00:00 | Arrancan las renovaciones nuevas, con su gasto mínimo |
| A la mañana (~9 h) | Filtrá **ayer** y **hoy** por campaña. Aplicá la tabla de la sección 6: subir 30 %, dejar quieta o bajar 30 % |
| Cada 3-4 horas | Si estás surfeando una CBO de menos de 500 USD: ¿sigue imprimiendo? +30 %. ¿Flaquea? Quieta o bajar |
| Puja manual | Cada 2 horas: ajustar la puja ±1 USD según la tabla de la sección 8 |
| Durante el día | Cargar la próxima renovación como conjunto nuevo en todas las cuentas de la oferta |
| Noche | Corte del día con ROAS de aprobadas. Sacar los mínimos de los conjuntos que cumplieron 3 días |

---

## 11. Errores que ya costaron caro

- Duplicar campañas y conjuntos con el mismo creativo y matarlos a los 20 USD: la "cola" de duplicados se llegó a comer entre el 25 % y el 75 % del gasto. Con V3 bajó al 5-10 %.
- Subir más de 30 % de golpe: la campaña se descontrola.
- Apagar anuncios en una campaña que venía en positivo: la sacaste del aprendizaje.
- Agregar una renovación sin gasto mínimo: Meta le dio todo al conjunto viejo y los creativos nuevos nunca se probaron.
- Dejar mínimos viejos cuando bajaste la CBO: llegaron a trabar casi todo el presupuesto.
- Abrir una segunda campaña igual en la misma cuenta en vez de otra cuenta.
- Sumar las ventas pendientes al ROAS: la campaña parecía rentable y no lo era.

---

## 12. Checklist del día

1. Números con comisiones cargadas y sin pendientes.
2. ROAS de ayer y de hoy por campaña.
3. Ninguna oferta nueva juzgada antes de 3 días.
4. Subidas de máximo 30 %: cada 3-4 h si la CBO está bajo 500 USD, una por día si está arriba.
5. Campañas que flaquean: quietas o bajadas 30 %.
6. Anuncios apagados solo en campañas con ROAS negativo.
7. Renovación cargada como conjunto nuevo, con gasto mínimo, en todas las cuentas de la oferta.
8. Mínimos de 3+ días sacados.
9. Ofertas validadas expandidas a cuentas nuevas con 1-1-winners a 2-3 tickets (5-10 con confianza).