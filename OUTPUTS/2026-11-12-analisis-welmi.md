# Radiografía completa de Welmi (app de conteo de calorías con IA)

Fecha: 2026-11-12
Fuente: Biblioteca de Anuncios (página Welmi App - Calorie Counter & Nutrition), welmi.ai, onboarding.welmi.ai, App Store, iTunes API, apppricinglab.

---

## 1. Quién es

| Dato | Valor |
|---|---|
| Producto | Welmi — contador de calorías con IA (foto del plato / voz / código de barras) |
| Empresa | **T-SHAPED APPS LTD**, Griva Digeni 51, Athineon Court, Of. 202, 8047 Paphos, **Chipre** |
| Bundle iOS | `com.fitme.companion.app` (la app nació como otra cosa y se rebrandeó a Welmi) |
| Android | `welmi.ai.android` |
| Lanzamiento | 28/02/2025 · última versión 01/11/2026 |
| Ratings | 4.77 · 20.594 ratings US · **250.000+ ratings globales** (la web dice 226.000+) |
| Instalaciones Android | ~435.000–555.000 (estimaciones de terceros) |
| Ranking | **#193 en Health & Fitness (US)** |
| Idiomas de la app | **35** |
| Otras apps del mismo estudio | Gymtone (gym planner), Vea (period tracker) |
| Atribución / paywall | **Adapty** (`api-ua.adapty.io` + dominio propio `attribution.welmi.ai`) |
| Cobro web | **Stripe + PayPal + tarjeta** |

Es **faceless**: no hay gurú, ni cara, ni marca personal. Pasa el filtro de funnel hacking.

---

## 2. El tamaño real de la operación

- **637 anuncios activos** en la fanpage principal (volcado completo del 12/11/2026).
- **~10.000 resultados** históricos con la palabra "welmi" en la Biblioteca (activos + apagados, todos los países).
- Al menos **4 fanpages distintas**: "Welmi App - Calorie Counter & Nutrition", "Welmi App", "Welmi - Calorie Counter", "Welmi App - Calorie Counter & Nutrition Assistant". Reparten anuncios entre páginas (la defensa anti-espía del manual).
- Anuncios más viejos encontrados (incluyendo apagados): **abril–mayo 2026**. O sea: llevan **7 meses mínimo** comprando tráfico sin parar.

### Línea de tiempo de la tanda activa

| Fecha de alta | Ads activos |
|---|---|
| 5–15 oct | 25 |
| **20 oct** | **182** |
| **23 oct** | **118** |
| 26–30 oct | 44 |
| **2 nov** | **64** |
| 3 nov | 35 |
| **6 nov** | **44** |
| 7–10 nov | 61 |
| 11 nov | 23 |
| 12 nov (hoy) | 8 |

Patrón: **tandas gigantes cada 3–4 días** (182, 118, 64, 44) más un goteo diario de 5–25 ads. No es "subo un creativo a ver". Es una fábrica.

### Mercados (por idioma del copy)

| Idioma | Ads activos |
|---|---|
| 🇪🇸 Español | **163** |
| 🇬🇧 Inglés | 84 |
| 🇧🇷 Portugués | 76 |
| 🇫🇷 Francés | 71 |
| 🇹🇷 Turco | 70 |
| 🇺🇦 Ucraniano | 39 |
| 🇷🇺 Ruso | 39 |
| 🇮🇹 Italiano | 29 |
| 🇩🇪 Alemán | 2 |

El mercado más fuerte es el de habla hispana, no el inglés. Turquía y Ucrania/Rusia con 70+ y 78 ads: mercados baratos que casi nadie mira.

---

## 3. La oferta y la plata

### Precios reales (App Store US, 10 productos vivos)

| Plan | Precio |
|---|---|
| Semanal | **$4.99** |
| Mensual | **$9.99 / $11.99 / $19.99** (tres precios en test simultáneo) |
| Anual | **$23.99 / $35.99 / $39.99 / $47.99 / $59.99** (cinco precios) |
| **Welmi AI Bundle** (add-on) | **$24.99** |

Tener 3 precios mensuales y 5 anuales corriendo a la vez = **están testeando precio todo el tiempo**, no eligieron uno.

### Las dos vías de cobro

1. **App → IAP** (lo que vende el 90% de los ads: "Descargá gratis en App Store/Google Play").
2. **Web → checkout propio** (quiz en `onboarding.welmi.ai` → paywall → Stripe/PayPal). Acá se quedan el 100% de la plata, sin el 30% de Apple. Y acá está el embudo que nos interesa.

---

## 4. El quiz funnel web, pantalla por pantalla

`welmi.ai` → botón → `onboarding.welmi.ai/survey/es/` → **~35 pantallas**.

**Bloque 1 — compromiso barato**
1. Género (hombre / mujer) — primera pregunta, un clic, cero fricción.
2. Prueba social inmediata: "1 millón de personas eligieron Welmi · 4.8/5 · 15.308+ App Store · 4.7/5 · 14.900+ Google Play".
3. Edad (18–24 / 25–34 / 35–44 / 45+).

**Bloque 2 — objetivo y dolor**
4. Objetivo: perder peso / estar más sano / verte mejor / más energía (**4 ramas distintas de copy en todo el resto del funnel**).
5. Placa de promesa: "Hombres de 45+ suelen alcanzar este objetivo en unos 2 meses" + gráfico 3/7/30 días.
6. "¿Intentaste bajar antes?" (recién empiezo / lo dejé / estoy en eso).
7. "¿Cuál fue tu mayor reto?" (era complicado / sin tiempo / no veía resultados / estresante / perdí la motivación) ← **recolecta la objeción para devolvérsela después**.

**Bloque 3 — educación + microcompromisos**
8. Placa "Welmi lo hace fácil: solo hacé una foto de tu comida".
9. Nivel de conocimiento en nutrición.
10. "¿Te derivó un profesional?" (hace parecer serio y médico).
11. Comidas por día · hábitos a cambiar · intolerancias (lactosa, gluten, etc.) · tipo de dieta (keto, paleo, vegana, alta en proteína…).
12. Placa científica: "Nuestro plan se basa en estudios de las principales organizaciones de salud" + mención a **Harvard** y **UNICEF**.

**Bloque 4 — datos del cuerpo (los que duelen)**
13. Caminata diaria · "¿te quedás sin aire subiendo escaleras?" · estatura · **peso actual** · objetivo de pasos · **peso objetivo** · ritmo (relajada / equilibrada / ambiciosa) con alerta "este ritmo es difícil de sostener".
14. Fecha del primer control de progreso.
15. Condiciones de salud (diabetes, menopausia, embarazo, problemas de estómago…).

**Bloque 5 — el cierre emocional**
16. "No estás solo en esto. Estaremos con vos en cada paso."
17. **Pantalla de cálculo en vivo**: "Analizando perfil: 5'10", 207 lb ✓ · Metabolismo: 1772 calorías ✓ · Preparando tu plan de comidas ✓ · Evaluación de salud ✓". Fabrica la sensación de que algo se computó para vos.
18. Proyección con fechas reales: "Hoy · 12 nov · 94 kg → En 2 semanas · … → En 2 meses · …".

**Bloque 6 — la puerta**
19. **Email gate**: "Tu plan de acción ya está listo. Introducí tu email para recibir tu plan personalizado." + candado "🔒 Tu correo solo se usa para crear tu cuenta". Botón: **"Descubrir mi plan"**.

Nada de precio hasta acá. Se paga con 35 respuestas y un email antes de ver un número.

---

## 5. El paywall y lo que viene después (todo verificado en el código del funnel)

Las rutas del embudo son literalmente: `email → results → paywall → checkout → discount-ticket → discount → upsell → payment-success / payment-failed`.

**a) Paywall ("PaywallSales")**
- 4 planes: **1 semana (prueba) / 4 semanas / 12 semanas / 52 semanas**, cada uno con precio viejo tachado y precio nuevo (`oldCents` vs `cents`).
- Plan recomendado: 12 semanas — *"Los usuarios de Welmi con objetivos parecidos a los tuyos llegan más rápido con un **plan de 12 semanas**"* + *"hasta 2× mejores resultados"* (*según investigación propia, 2025*).
- Banner de descuento con **contador regresivo**: "50% de descuento reservado para: 09:58".
- Ancla de precio: **€19.99** como referencia de lo que costaría "normal".
- **Garantía de devolución de 30 días** (sello) + garantía condicionada: *"verás progreso visible en 4 semanas; si seguiste el plan y no hubo resultados, te devolvemos la compra"*.
- Testimonios con foto y nombre (Hannah, Paul, "Dan, 29") + sello "Verified review" + laureles.
- Métodos: Visa/Mastercard, **PayPal**, **pago con un clic**. Aviso: "las tarjetas prepagas o virtuales no siempre se aceptan".
- Letra chica: el precio con descuento es **introductorio**; después renueva automáticamente al precio completo cada período hasta que canceles.

**b) Downsell: el boleto raspable ("DiscountTicket")**
Si te vas del paywall: *"**Rascá el boleto para descubrir tu oferta**"* → "✨ OFERTA EXCLUSIVA ✨" → **50%, 75% o 90% DE DESCUENTO** → "Tu precio inicial está desbloqueado" + nuevo contador. Es la ruleta de descuento, con mecánica de scratch card.
Además hay una capa estacional: **"🎁 Oferta navideña — termina en: 00:00"**.

**c) Upsell post-pago ("UpsellScan")**
Inmediatamente después de cobrar:
- *"Desbloqueá el **AI body scan** y el informe de bienestar"* — **acceso de por vida a los escaneos con IA**.
- *"Es un pago único de acceso de por vida. No se renueva."* (el **Welmi AI Bundle de $24.99** del App Store).
- *"Al tocar el botón se cobrarán $X **de inmediato a la tarjeta guardada**"* → **1-click, sin volver a pedir datos**.
- Reductor de riesgo: *"Este complemento es opcional. Tu suscripción no depende de esta compra."*
- Salida: *"Continuar sin AI body scan"* (link chiquito, no botón).
- Cláusula legal: al tocar el botón renunciás al derecho de desistimiento porque el servicio empieza ya.

**d) Entrega ("PaymentSuccessV2")**
"¡Tu membresía Premium está activa!" → **QR + "Descargá la app y entrá con tu email y contraseña"**. El producto se entrega dentro de la app, no por mail.

**e) Recupero**
`payment-failed` con diagnóstico ("no se pudo procesar, posibles motivos…", "actualizá tu método de pago") y reintento.

---

## 6. Los anuncios

### Los números del copy (233 copies únicos medidos)

- **5 a 6 líneas** el 80% de las veces (media 5,5).
- **77 palabras** de promedio.
- **229 de 233 arrancan con emoji** y cada línea lleva el suyo.
- 126 de 233 mencionan **la foto del plato**. 78 mencionan **déficit calórico**. 77 mencionan **proteína**.
- CTA final siempre igual: **"Probá Welmi gratis — App Store y Google Play"** / "Descargá Welmi y empezá hoy".
- **Nunca aparece un precio en el anuncio.** La palabra que usan es "gratis".
- Un mismo contenido se duplica en **2 a 5 anuncios** (duplicación de escala, el 100% de los ads está duplicado al menos una vez).

### La plantilla exacta que repiten 233 veces

```
Línea 1 · Creencia falsa + dolor concreto (emoji)
Línea 2 · El verdadero problema: no sabés TU número
Línea 3 · El mecanismo: le sacás una foto al plato y la app cuenta
Línea 4 · El beneficio: sabés cuánto te queda hoy, sin pesar nada
Línea 5 · Permiso: podés seguir comiendo lo que te gusta
Línea 6 · CTA: Descargá / Probá gratis — App Store y Google Play
```

### Duración de los videos
Mediana ~0:30. Rango 0:14 a 1:13. El 90% está entre 20 y 45 segundos.

### Los 5 formatos de creativo (muestra transcrita)

1. **Transformación + demo de app (0:38)** — hombre común se transforma, voz en off en primera persona, pantallas de la app intercaladas, cierre con las dos tiendas.
2. **Hook de remera levantada + VO explicativa (0:28)** — "para bajar de peso no necesitás dietas… solo importa el déficit" + balanza + foto del plato + "Get started for free".
3. **Animación 3D científica día a día (0:47)** — "Qué dirán tus análisis si comés 500 calorías menos durante dos meses": Día 1 / Día 5 (−1 kg, "no es músculo, es agua") / Día 10 (bajón de energía) / Día 20 (los jeans flojos) / Día 30 (−3-4%) / −5% (presión, azúcar, grasa en sangre). Cuerpo de vidrio, órganos, gráficos. **Es un VSL de 47 segundos.**
4. **Fisicoculturista real + demo (0:22)** — "el gimnasio es la mitad del resultado, la otra mitad está en tu plato".
5. **Avatar 3D en testimonio en primera persona (0:30)** — "Yo hacía todo bien: press de banca, fondos… y el pecho seguía aguado. Resultó que comía 600 calorías de más al día".

Todos: 9:16, **subtítulos palabra por palabra**, música de fondo, cortes cada 1–2 segundos, la app en pantalla en el medio, cierre con los dos botones de tienda y "4.7 ★ / Apps esenciales de salud".

### Los ángulos (uno por ad, mismo mecanismo)

Panza cervecera · abdominales que no aparecen · "tu amigo come lo que quiere y no engorda" · el desayuno "sano" de 800 calorías · a ojo calculás la mitad · "no es genética, es aritmética" (proteína) · el déficit de 500 kcal · la cerveza/puñado de nueces de 200 calorías al año · "comé tacos/pizza/hamburguesa y bajá igual" · "2 días a café y ensalada y al tercero vaciás la heladera" · definición/cutting sin pesar comida · Harvard dice que el diario de comidas duplica los resultados.

**Un mecanismo, doce dolores.** Eso es lo que les permite tener 233 copies sin repetir nada.

---

## 7. Qué se roba de acá (accionable)

1. **La plantilla de copy de 6 líneas con emoji por línea.** Está validada 233 veces en 9 idiomas. Se puede calcar tal cual para cualquier oferta tuya cambiando el mecanismo.
2. **El VSL de 47 segundos "día por día"** (formato 3). Es el mejor creativo del lote: promesa temporal, ciencia simple, objeción resuelta en el medio ("a ojo calculás la mitad"), producto como solución a UNA cosa. Se replica con animación o con B-roll.
3. **El boleto raspable como downsell.** En vez de la ruleta de siempre: "rascá el boleto" con 50/75/90%. Es más limpio y tiene mejor mecánica de juego.
4. **El upsell de "pago único, acceso de por vida" sobre tarjeta guardada**, con el calmante *"esto es opcional, tu compra no depende de esto"* y la salida como link chiquito. Encaja directo con los OTOs del molde de piedras.
5. **La pantalla de cálculo en vivo** antes del email gate (analizando perfil ✓ / metabolismo ✓ / plan ✓). Es el momento que convierte un quiz en un "plan personalizado". Falta en nuestros quizzes.
6. **El email gate antes del precio.** 35 preguntas y un mail antes de ver un número: el que llegó ya invirtió demasiado para irse.
7. **La pregunta de objeción** ("¿cuál fue tu mayor reto?") para devolver la objeción en el paywall.
8. **Los mercados huérfanos**: turco, ucraniano y ruso con 70+ anuncios cada uno. Si ellos ponen plata ahí, hay tráfico barato que nadie de nuestro círculo está tocando.
9. **Precio múltiple en paralelo**: 3 precios mensuales y 5 anuales a la vez. Nosotros fijamos un precio y no lo movemos más.

## 8. Qué NO sirve copiar

- **No es un infoproducto low ticket.** Es una app de suscripción con 250.000 reseñas, 500.000 instalaciones y ~7 meses de gasto continuo. No se compite de frente: ellos pagan instalaciones con LTV de suscripción anual de hasta $59.99 + upsell de $24.99. En el nicho de calorías con IA el CPM ya está carísimo (Cal AI tiene 375.000 reseñas en el mismo nicho).
- **La entrega es una app.** Vos entregás PDFs. Toda la promesa de "sacale una foto al plato" no se puede sostener con un PDF — si querés usar el ángulo, el mecanismo tiene que ser otro (una tabla, una calculadora, un sistema de 2 números).
- **El tráfico va a la tienda de apps**, no a una landing. Ese modelo de campaña (instalaciones de app) no es el tuyo.

## 9. Veredicto

| Criterio | Resultado |
|---|---|
| Marca personal | ❌ No hay — **pasa** |
| Mismo destino | ✅ Todos a la app (316 por dominio propio, 284 por Adapty) — **pasa** |
| Antigüedad | ✅ 7 meses, 637 activos — **pasa con honores** |
| Low ticket | ❌ Suscripción, no producto digital de $14–27 |
| Modelable 1:1 | ❌ No (app + capital + 250k reseñas) |
| **Modelable como embudo y como copy** | ✅ **Sí, y es de lo mejor que vi** |

**Welmi no es una oferta para cazar. Es un manual para estudiar.** El valor está en el quiz de 35 pasos, el paywall con boleto raspable, el upsell de 1 clic y, sobre todo, en la plantilla de copy de 6 líneas replicada 233 veces en 9 idiomas sin repetir un ángulo.

---

## Pendiente

Los precios exactos del **paywall web** (no los del App Store) están detrás del email gate. Para verlos hay que dejar un correo en el formulario del quiz: no lo hice sin tu OK.
