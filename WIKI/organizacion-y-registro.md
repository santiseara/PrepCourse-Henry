# Organización y registro de la operación

> Registro diario por oferta, tres cuentas con tres trabajos, el recorrido de herramientas y las reglas para que el método siga vivo. (fuente: RAW/2026-10-10-wiki-previa/organizacion-y-registro.md)

**Sin un registro, cada decisión se olvida y se repiten los mismos tests.** Todo cambio de presupuesto o de puja se anota con la hora y con la captura de los números.

## Registro diario

- **Una página por oferta y por día** (en Notion, o en `OUTPUTS/` de este segundo cerebro).
- Cada cambio de presupuesto o de puja se anota **con la hora** y con una **captura del dashboard de UTMify**.
- Así no se pierde el historial de qué se tocó y qué pasó con las ventas después.
- Para los creativos, el registro de qué ángulo ganó lo lleva la skill `ad-builder`.

## Tres cuentas, tres trabajos

| Cuenta | Qué corre |
|---|---|
| **Testeo** | ABO 1-1-1 (o 5 conjuntos), con 3× el CPA medio (testeo acelerado) o 1× el CPA medio. O la CBO de testeo ([[testeo-de-creativos]]) |
| **Escala automática** | V3, aisladas, Pockets, Launch Pocket, CBO mixta y power ([[metodo-v3]], [[estructuras-cbo]]) |
| **Pujas manuales** | CostCap, BidCap y ROAS cap con intrapujas ([[escalado-en-meta-ads]]) |

Una cuarta cuenta, o más, sirve para **replicar horizontalmente** lo que gana. Probá entre 5 y 7 cuentas y quedate con las de **menor CPM**. El CPM puede variar mucho entre cuentas (4, 6 u 8 USD) solo por su historial.

## El recorrido de herramientas

1. **Espiar:** Biblioteca de Anuncios, AdSpy, Minea o GetHook ([[funnel-hacking]]).
2. **Modelar la oferta** y escribir la landing y el copy: Claude.
3. **Producto:** Gamma para el MVP y Claude + Higgsfield para la versión de calidad, después de validar ([[creacion-de-productos-digitales]]).
4. **Testear y escalar:** Meta Ads, a mano o por el conector de Claude.
5. **Trackear:** UTMify ([[tracking-y-atribucion]]).

## Reglas de organización

- **La Biblioteca de Anuncios es la mejor mentoría gratis que existe.** Dedicarle horas no es negociable, en cualquier nivel.
- **No dependas de swipe files compartidos.** Si mucha gente modela lo mismo al mismo tiempo, se satura.
- **No te despegues de la comunicación validada.** Traducí y adaptá el copy y el formato exacto del competidor que modelás. Solo se mejora el mecanismo único. No se cambia la comunicación a la primera, sin datos.
- **El método es un documento vivo.** Las estructuras de campaña y las herramientas cambian cada pocas semanas. Cuando llegue material nuevo, cargalo en `RAW/` y pedile a Claude «procesá RAW».
- **Tené funnels listos antes de necesitarlos.** Con varias ofertas armadas es más probable encontrar una cuya matemática cierre (costo por visita menor que ingreso por visita).

Relacionado: [[testeo-de-creativos]] · [[escalado-en-meta-ads]] · [[metodo-v3]] · [[ia-en-el-flujo-de-trabajo]]

## 📁 Entrega en Google Drive — las ofertas con el socio (REGLA FIJA, 2026-11-13)

Santiago: *"vos entrás a esa carpeta y vas a crear una nueva carpeta con el nombre de la oferta que el nombre de la oferta siempre por delante va a tener la palabra eBook… y dentro de la carpeta que crees vas a crear una carpeta que se llame Videos terminados y ahí vas a subir los anuncios terminados siempre siempre"*.

**Toda oferta que se hace con el socio (Damián) se entrega en el Drive de Santiago, en este camino exacto:**

```
Mi unidad / Ebook Dami / Ebook <Oferta> (<MERCADO>) / Videos terminados /
```

- La carpeta madre **`Ebook Dami`** ya existe y no se toca. Dentro va **una carpeta por oferta**.
- El nombre de la carpeta de la oferta **siempre arranca con `Ebook`** y después el nombre de la oferta (ej.: oferta "Campo" → `Ebook Campo`). Las carpetas que ya están ahí cierran con el mercado entre paréntesis — `Ebook Tapizado (LATAM)`, `Ebook Juegos en Pareja (ARG)`, `Ebook Box (INGLES)` —, así que se respeta esa forma: **`Ebook <Oferta> (LATAM | ARG | INGLES | …)`**.
- Dentro de la carpeta de la oferta va **siempre** una subcarpeta **`Videos terminados`**, y ahí van **los anuncios terminados** (los MP4 finales, no los crudos ni las voces ni los guiones).
- **El nombre de cada video es el arranque del hook**, tal cual se escucha. Si el video empieza diciendo *"Las vacas que…"*, el archivo se llama **`Las vacas.mp4`**. Nada de `V1.mp4` ni de la nomenclatura `DD-M - N` acá: esa sigue valiendo para la carpeta del Escritorio.
- **Es el mismo proceso siempre, sin que lo pida.** Apenas una tanda está terminada, se sube.

**La única excepción:** cuando la oferta es **de Santiago solo** (sus cosas, no las del socio). Ahí no va a `Ebook Dami`; se le pregunta o se usa el circuito de siempre de `~/Desktop/<oferta>/anuncios/`.

> Esto **no reemplaza** la carpeta local: los videos igual se arman y quedan en `~/Desktop/<oferta>/anuncios/` con el nombre de tanda `DD-M - N` (regla de [[como-trabajar-con-santiago]]). El Drive es la **entrega**, el Escritorio es el **taller**.

## Conexiones con tu operación actual
- **El registro diario va en `OUTPUTS/` de este cerebro.** Cuando me pases cambios de presupuesto o de puja con la captura de UTMify, los anoto en `OUTPUTS/AAAA-MM-DD-registro-<oferta>.md` y los enlazo desde el índice.
- **"El método es un documento vivo: cargá en RAW y pedí procesá RAW"** es exactamente cómo funciona este segundo cerebro.
- **"No te despegues de la comunicación validada"** coincide con tus variables: se mantiene la DNA y se mejora el mecanismo, no se reinventa ([[scented-stones]]).

## Fuentes
- RAW/2026-10-10-wiki-previa/organizacion-y-registro.md (página de la wiki previa, actualizada el 2026-09-24)
- Fuentes originales citadas (todavía no están en este cerebro): clases de la formación y experiencias de la comunidad, agosto–septiembre 2026
