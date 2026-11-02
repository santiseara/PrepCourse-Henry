# Módulo 1 — Búsqueda de ofertas ganadoras (guía de clase)

> Versión guía del Módulo 1: solo los puntos que hay que decir sí o sí, en orden, para dar la clase hablando y no leyendo. La teoría completa quedó en `OUTPUTS/2026-11-01-modulo-1-busqueda-de-ofertas-ganadoras.md`.

Guía para dar la clase: los puntos que hay que decir sí o sí, en orden. Los ejemplos se muestran en vivo en la Biblioteca.

## El punto del módulo

**No inventamos demanda: la detectamos.** Nadie adivina qué quiere comprar la gente. Se mira qué ya se está vendiendo con plata adentro y se modela.

**El orden en que se decide** (y el 80% del resultado está en los dos primeros):

1. **Mercado** — el nicho y el país
2. **Anuncios** — el ángulo y el formato
3. **Funnel** — landing, checkout, upsells
4. **Producto** — lo último, y es lo que casi todos hacen primero

**El error que cuesta años:** correr una oferta que *a mí me parece* perfecta. Dos años de testeos, mucho tráfico a la landing, cero conversión. La landing no era el problema: el mercado no existía.

**Lo que se llevan de este módulo:** saber mirar la Biblioteca de Anuncios y salir con 3 a 5 ofertas candidatas, puntuadas, con el funnel del competidor desarmado.

## Qué es una oferta ganadora

Una oferta ganadora es **una oferta que ya está gastando plata todos los días desde hace semanas**. No es una idea linda ni un producto que "debería" vender.

La lógica: nadie quema presupuesto varias semanas a pérdida. Si sigue al aire, es porque cierra números.

### Las cinco señales, en una línea

| Señal | Qué quiere decir |
| --- | --- |
| **Longevidad** | Anuncios corriendo hace 20+ días |
| **Volumen** | Muchos anuncios activos al mismo tiempo |
| **Duplicación** | El mismo creativo repetido — están escalando el ganador |
| **Mismo URL** | Todo apunta al mismo destino (si no, no es una oferta) |
| **Funnel armado** | Hay checkout, order bump, upsell: hay negocio detrás |

### Qué NO cuenta

- Que a vos te guste el nicho
- Muchos anuncios subidos **hoy** (eso es un test, no un winner)
- Un experto o marca personal detrás — lo que vende es la cara, no la oferta
- Un número de anuncios sin mirar la **fecha**

**Lo que buscamos:** páginas-máquina. Oferta repetible, sin cara, con funnel. Eso se puede modelar.

## La Biblioteca de Anuncios de Meta

Gratis, sin login, y están **todos los anuncios activos del mundo**: `facebook.com/ads/library`

### El error que hace perder horas

La Biblioteca **filtra por país por defecto**. Si no cambiás eso a *Todos*, estás mirando una rendija.

- En la URL: `country=ALL`
- Si una oferta corre en 6 países y vos mirás uno, ves 12 anuncios en lugar de 80

### Los dos paneles que importan

| Panel | Para qué sirve |
| --- | --- |
| **Palabra clave** | Descubrir ofertas que no sabés que existen |
| **Anunciante / página** | Ver TODO lo que corre una página: el inventario completo |

**URL de búsqueda** — cambiá `KEYWORD` y la ventana de fechas:

```
https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=KEYWORD&search_type=keyword_unordered&media_type=all&start_date[min]=2026-05-01&start_date[max]=2026-08-01&sort_data[mode]=total_impressions&sort_data[direction]=desc
```

**URL para espiar una página** — cambiá `PAGE_ID`:

```
https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&view_all_page_id=PAGE_ID&search_type=page&media_type=all
```

### Los cuatro caminos para buscar

1. **Footprint de checkout** — nombres de pasarelas y plataformas de pago. El mejor: te deja solo gente que vende
2. **Frases de copy** — lo que dice el anuncio, no el nombre del nicho
3. **Dominio** — si encontrás una landing buena, buscá el dominio y aparecen los que la copian
4. **Desde el anunciante** — un winner te lleva a sus vecinos

### Nunca arranques por la keyword obvia

- "renda extra", "ganar dinero online": ahí está todo el ruido del mundo
- Arrancá por el **footprint de pago** o por una **frase de copy**
- Un subnicho raro vale más que el nicho grande

### Dos trucos

- Ordená por impresiones (`sort_data[mode]=total_impressions`) para que lo grande suba primero
- `search_type=keyword_exact_phrase` para frases; `keyword_unordered` deja entrar ruido

## Cómo se lee si una oferta vende

### La señal no es el volumen: es la fecha

**Caso real:** una oferta con **510 anuncios activos** pero todos subidos hace 9 días. Otra con **97 anuncios** corriendo hace 106 días. La ganadora es la segunda. La primera está testeando.

El orden en que se mira:

1. **Fecha** de inicio de los anuncios
2. **Volumen** de anuncios activos
3. **Duplicación** del mismo creativo

### La regla de los 3 días

Un anuncio con menos de 3 días al aire **no prueba nada**. La mayoría de los tests se matan antes de las 72 horas. Si lleva 20 días, ya pasó el filtro.

### Escalera de certeza

| Anuncios activos + antigüedad | Qué significa |
| --- | --- |
| **8–15**, 20+ días | Oferta que funciona. No la descartes por chica |
| **20–40**, 20+ días | Validada y escalando |
| **50–100+**, 30+ días | Whale. Modelala, no compitas |
| Cualquier cantidad, < 3 días | Test. Anotala y volvé en dos semanas |

8 anuncios corriendo hace dos meses es mejor negocio que 300 de ayer.

### Lo que se descarta ANTES de contar

- **Marca personal / experto con cara** — vende la persona (de 20 ofertas, 12 se cayeron por esto)
- **Anuncios sin URL o con URLs distintas** — no es una oferta, es tráfico
- **E-commerce físico** — otro juego, otros márgenes
- **Infoproducto de un gurú conocido** — no podés replicar su autoridad
- **Lead magnets puros sin checkout** — no sabés si monetizan

**La excepción:** si la cara es un actor genérico o una voz en off, se puede modelar. Lo que no se modela es la autoridad de una persona real.

## Las otras plataformas

La Biblioteca alcanza para trabajar. El resto sirve para **ver cosas que Meta no muestra** o para ir más rápido.

| Plataforma | Qué aporta | Costo |
| --- | --- | --- |
| **Biblioteca de Meta** | La fuente. Todo lo activo, con fechas | Gratis |
| **TikTok Creative Center** | Qué formato y qué hook funciona por país | Gratis |
| **AdSpy / BigSpy / Minea** | Filtros finos: antigüedad, país, engagement, ordenar por lo que escala | Pago |
| **SimilarWeb** | De dónde viene el tráfico de una landing y cuánto mueve | Freemium |
| **Hotmart / Kiwify / Braip** | Qué se vende más en Brasil y LatAm (ranking de afiliados) | Gratis |
| **Foros y Reddit** | Las palabras con las que la gente describe su problema | Gratis |

**Si estás empezando, no pagues nada.** Los filtros de pago aceleran, no deciden. La decisión sale siempre de la Biblioteca.

### Los marketplaces: cuidado

Ahí se ve **qué se vende**, pero no **cómo lo venden**. Te dan la idea; el funnel lo tenemos que ir a buscar a la Biblioteca.

### Los swipe files

Tentadores y casi siempre viejos. Una oferta de un swipe file de hace seis meses probablemente ya esté quemada.

## Dónde buscar: nichos y mercados

### Los tres big niches

**Salud · Dinero · Relaciones.** El criterio no es el tamaño: es la **urgencia de compra**. Nadie posterga un dolor de espalda. Son evergreen y están conectados entre sí.

### Bajar a subnicho

| Big niche | El patrón | Ejemplos de subnicho |
| --- | --- | --- |
| **Dinero** | "ganá plata con X" | herrería, costura, barbería, uñas, Canva, reparar celulares |
| **Salud** | dolor o condición concreta | menús para diabéticos, Parkinson, menopausia, dolor de rodilla, yoga para mayores |
| **Relaciones** | conflicto concreto | crianza de hijos adolescentes, recuperar la pareja, ansiedad social |

**El patrón que se repite:** el oficio es el disfraz; lo que se vende es **hacer plata con el oficio**. Y el subnicho con nombre y apellido gana al nicho grande: más urgencia, menos competencia, CPM más barato.

### Mercado fuente → mercado destino

Se **espía** en mercados maduros y se **lanza** en mercados vírgenes.

| Fuente (espiar) | Destino (lanzar) | Por qué |
| --- | --- | --- |
| Brasil | Habla inglesa | Brasil va 1–2 años adelantado |
| Estados Unidos | Europa, LatAm | Volumen y madurez de funnels |
| Europa | LatAm | Menos saturado abajo |

**Orden de preferencia para lanzar:** 1) inglés, 2) Europa, 3) LatAm, 4) Brasil (el más competitivo).

**La regla dura:** nunca modeles en el mismo mercado. Si lo traés de afuera, llegaste primero y la puja juega a tu favor. Si lo corrés al lado del original, arrancas con CPM más caro, sin data y contra un backend que no ves.

### Dos advertencias

- **Manifestación, ley de atracción, tarot:** venden muchísimo pero Meta te baja la cuenta. No para empezar
- **Salud:** cuidado con promesas de curar. El ángulo va por alívio, hábito o menú, nunca por cura

## Auditar al competidor

Encontrar la oferta es la mitad. La otra mitad es **desarmarle el funnel completo**, y es el paso que casi nadie hace.

### Paso 1 — Abrir todo el inventario de la página

- URL con `view_all_page_id` y `country=ALL`
- Scrolleá hasta el fondo para que cargue todo
- Contá los anuncios y mirá la fecha del más viejo: esa es la longevidad real

### Paso 2 — Guardar los creativos repetidos

El creativo que aparece 10 veces es **el que les está dando plata**. Guardá hook, formato, duración y ángulo.

### Paso 3 — Entrar a la landing y comprar

Se recorre el funnel entero como cliente:

- [ ] Headline y promesa principal
- [ ] Mecanismo único (el "por qué esto funciona")
- [ ] Precio del front y qué incluye
- [ ] Bonus (cuántos y de qué)
- [ ] Garantía
- [ ] Order bump en el checkout
- [ ] Upsells después de pagar
- [ ] A dónde te manda después (WhatsApp, email, comunidad)

### Paso 4 — Calcular el backend

Es el paso que separa al que gana del que mira. El front es lo que ves; el backend es lo que les permite pagar más caro el clic que vos.

- Front + order bump + upsells = el AOV real
- Si venden a 17 USD y tienen 3 upsells, no compiten con 17: compiten con 40
- **No se puede clonar lo que no se ve**, por eso hay que comprar

### Paso 5 — Buscar el hueco de arbitraje

Casi todas las ofertas tienen algo flojo. Ese hueco es tu entrada:

- Copy genérico → un ángulo más específico
- Un solo formato de creativo → otro formato
- Landing pobre → landing mejor
- Sin upsells → el mismo producto con backend

### La segunda pasada

**Volvé a mirar la misma oferta 7–14 días después.** Si sigue ahí y con más anuncios, está escalando. Si desapareció, te ahorraste el dinero.

## El scorecard y el veredicto

### Las 4 señales — un punto cada una

| Señal | Pasa si… |
| --- | --- |
| **Longevidad** | El anuncio más viejo tiene 20+ días |
| **Volumen** | 8 o más anuncios activos |
| **Duplicación** | El mismo creativo repetido varias veces |
| **Hueco de arbitraje** | Encontraste algo concreto para mejorar |

**4 de 4** = candidata fuerte · **3 de 4** = sirve · **2 o menos** = anotala y seguí buscando.

### El veredicto

| Veredicto | Cuándo | Qué hacés |
| --- | --- | --- |
| **ENTRAR** | 3–4 puntos, mercado destino libre | Modelar y lanzar |
| **SUBNICHO** | Nicho saturado pero con un ángulo lateral libre | Entrar por el costado |
| **WHALE** | 50–100+ anuncios, meses corriendo | Modelar en otro mercado, nunca competir |
| **DESCARTAR** | Marca personal, sin URL, e-commerce físico | Siguiente |

### La ficha de oferta

Una por cada candidata, siempre igual:

```
OFERTA: ________________________  PAÍS: ______
PÁGINA / PAGE ID: ______________________________
ANUNCIOS ACTIVOS: ____   MÁS VIEJO: ____ días
FORMATO DOMINANTE: _____________________________
PROMESA / ÁNGULO: ______________________________
PRECIO FRONT: ____   BUMP: ____   UPSELLS: ____
AOV ESTIMADO: ____
HUECO DE ARBITRAJE: ____________________________

SCORE:  longevidad [ ]  volumen [ ]  duplicación [ ]  hueco [ ]
VEREDICTO:  ENTRAR / SUBNICHO / WHALE / DESCARTAR
SEGUNDA PASADA (fecha): ______  ¿Sigue? Sí / No
```

**Y después, cuál elegís:** entre las candidatas con score alto, la que **más ganas te dé de correr**. No hay criterio más sofisticado y es a propósito: lo que importa es no demorarse.

## Errores, rutina y tarea

### Los errores que matan la cacería

1. **No poner `country=ALL`** — el que hace perder más horas
2. **Contar anuncios sin mirar la fecha**
3. **Elegir por afinidad al nicho** — te gusta el fitness, vendés fitness
4. **Elegir una oferta demasiado fácil de replicar** — si cualquiera la copia en una tarde, no tenés diferenciación
5. **Modelar en el mismo mercado**
6. **No comprar el funnel** — te quedaste con el front
7. **Mirar swipe files viejos en lugar de la Biblioteca**
8. **Enamorarse de la primera** — el objetivo es un banco de ofertas, no una
9. **Buscar y no anotar** — sin ficha, en una semana no te acordás de nada
10. **Cambiarle el formato de creativo** al que estamos modelando

### La rutina de cacería

| Cuándo | Qué |
| --- | --- |
| Todos los días, 30 min | Una keyword nueva o un anunciante nuevo, ficha de lo que aparezca |
| Una vez por semana | Segunda pasada sobre las candidatas de la semana anterior |
| Siempre | El banco de ofertas crece; nunca se arranca de cero |

Una oferta caduca a los **3–4 meses**. Por eso la cacería no se termina nunca: es rutina, no un evento.

### La tarea del módulo

- [ ] Elegir un big niche y bajar a un subnicho concreto
- [ ] Armar un banco de 10 keywords (footprints de pago + frases de copy)
- [ ] Barrer la Biblioteca con `country=ALL` y ventana de fechas
- [ ] Completar 5 fichas de oferta con score y veredicto
- [ ] Comprar el front de la mejor candidata y mapearle el backend
- [ ] Agendar la segunda pasada a 7 días

**Con 100 USD y una semana se valida.** Pero primero hay que tener qué validar: eso es este módulo.
