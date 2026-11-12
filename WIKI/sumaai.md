# SumaAI (contador de calorías con IA)

> Oferta propia modelada sobre [[welmi]]: contar calorías sacándole una foto al plato. Marca elegida por Santiago el 2026-11-12 entre las opciones de nombre chequeadas en el App Store. El quiz ya está armado: **19 pasos** (el original tiene ~35), paleta azul y pago único en ImpulTienda. (fuente: pedido de Santiago del 2026-11-12, OUTPUTS/2026-11-12-analisis-welmi.md)

## Ideas clave

- **Nombre:** **SumaAI**. Claim: *Sacale una foto. SumaAI la suma.* Logo de texto solo (`Suma` + `AI` en el azul de marca), sin ícono.
- **Mecanismo:** una foto del plato → el número del día. La promesa nunca es "comé menos", es **"no sabés cuántas calorías comés"** y el permiso *seguí comiendo lo que te gusta* (el eje de los 233 copies de [[welmi]]).
- **Por qué este nombre:** `cal / kal / nutri / fit / slim` están quemados en el App Store (Cal AI, Kalo, Calo, Calz, Numi, Nutri AI, Satia ×3, Platia ×2). *Suma* no colisiona en Health & Fitness y `suma.app` estaba libre. Ver OUTPUTS/2026-11-12-nombres-de-marca-contador-de-calorias.md.
- **Diferencia de fondo con el original:** Welmi vende **suscripción** (4 planes de 1/4/12/52 semanas que renuevan). Nosotros vendemos **pago único con acceso de por vida** en ImpulTienda, con cuotas de Mercado Pago. El paywall de 4 planes no se clona: no entra en el checkout.

## El quiz (19 pasos, armado el 2026-11-12)

Orden: género → edad → objetivo (4 ramas) → placa de promesa con gráfico 3/7/30 → ¿ya intentaste contar? → **cuál fue tu mayor reto** → placa del mecanismo con la maqueta del celular → comidas por día → intolerancias y dieta (unificadas) → cuánto te movés → altura → peso → peso objetivo → ritmo → condiciones de salud → placa de apoyo que **repite el reto que eligió** → cálculo en vivo (8,5 s) → resultado → oferta.

- **Las 16 pantallas que se sacaron** del original: prueba social con ratings (no son nuestros), "¿te derivó un profesional?", nivel de conocimiento en nutrición, hábitos a cambiar, placa científica con Harvard y UNICEF, objetivo de pasos diarios, fecha del primer control, escaleras y caminata por separado, intolerancias y tipo de dieta por separado, edad exacta, placas de relleno y **el email gate** (el mail se pide en el checkout, regla de [[quizzes-reglas-de-armado]]).
- **Lo que se conservó del original porque es lo que vende:** la pregunta del **mayor reto** (recoge la objeción y se la devuelve dos pasos después), la **pantalla de cálculo en vivo**, la **proyección con fechas reales** y el gráfico día 3 / 7 / 30.
- **Los números se calculan de verdad** (Mifflin-St Jeor + factor de actividad + déficit por ritmo). El objetivo diario tiene **piso de 1.200 calorías** y, cuando pega el piso, la fecha se recalcula con el déficit real y aparece un aviso: *"estiramos la fecha en vez de recortar la comida"*.
- **Paleta azul** (pedido de Santiago): acento `#1B4CD9`, tinta `#0E2452`, lavado `#E8EFFD`, fondo `#F2F6FD`. El verde `#1F6B47` queda solo para "bien" y el rojo `#C0392B` solo para riesgo.
- Token `{{o}}` para la concordancia de género y la opción de menopausia solo en la rama mujer.

## Pendientes (lo que falta para poder subirlo)

- **Qué se entrega exactamente.** La slide de oferta lista "todo lo que te llevás" (número diario, contador por foto, plan por etapas, equivalencias argentinas, qué pedir afuera). Falta confirmar si es app propia, acceso web o guía.
- **Precio real.** Hoy el CONFIG trae `$14.990` tachando `$49.990` y 3 cuotas de `$4.997` como placeholder.
- **Checkout.** Va relativo (`/checkout`) hasta que exista el subdominio; se verifica con `curl -sIL` que devuelva 200 ([[quizzes-reglas-de-armado]], corrección de Tai Chi Fit).
- **Las 3 reseñas del CONFIG son de ejemplo** y hay que reemplazarlas por reales.
- Sin imágenes: la maqueta del celular y el sello de garantía están dibujados en CSS/SVG. Si más adelante van fotos, entran por el CONFIG.

## Preguntas abiertas

- ¿El downsell del boleto raspable de [[welmi]] va en la salida del quiz o recién en el post-pago?
- ¿Se corre primero en Argentina o directo en español neutro para LATAM? ([[internacionalizacion]])

## Relacionado

[[welmi]] · [[quizzes-reglas-de-armado]] · [[quiz-funnel]] · [[embudo-vsl-post-pago]] · [[aumento-de-aov]] · [[guiones-y-anuncios]]

## Fuentes

- OUTPUTS/2026-11-12-analisis-welmi.md y OUTPUTS/2026-11-12-nombres-de-marca-contador-de-calorias.md
- OUTPUTS/2026-11-12-quiz-sumaai.html (copia del entregable)
- `~/Desktop/sumaai/landing/` (quiz.html, sumaai-quiz.txt, PRUEBA.html)
