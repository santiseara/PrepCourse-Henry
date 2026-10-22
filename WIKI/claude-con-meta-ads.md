# Claude conectado a Meta Ads

> Qué hace bien Claude con el conector oficial de Meta Ads, qué no puede hacer y las trampas que ya costaron plata (estados que se activan solos, anuncios rechazados que no aparecen como error). (fuente: RAW/2026-10-10-wiki-previa/claude-con-meta-ads.md)

**Con el conector oficial de Meta, Claude crea campañas, conjuntos y anuncios, lee métricas y busca en la Biblioteca de Anuncios.** Ahorra horas, pero tiene límites y trampas que conviene conocer antes de dejarlo trabajar solo.

## Qué hace bien

- Crear campañas, conjuntos y anuncios con la estructura del [[metodo-v3]].
- **Clonar anuncios entre cuentas por post ID**, sin volver a subir los videos.
- Leer resultados por campaña, conjunto o anuncio, y cruzarlos con UTMify.
- Buscar competidores en la Biblioteca de Anuncios (la skill `cazar` lo hace sola).
- Armar catálogos, conjuntos de productos y feeds ([[subir-ads-con-metodo-catalogo]]).

## Lo que no puede hacer (y se hace a mano)

- **No tiene el campo "Parámetros de URL".** Los UTMs tienen que ir **dentro del link**, o se pegan después con una edición masiva en el Administrador ([[nomenclatura-del-metodo]]).
- **Los creativos no se editan.** Para cambiar el video, el copy, el link o el botón, se crea un creativo nuevo.
- **El anuncio de catálogo en video único** se termina a mano en el Administrador.

## Trampas que ya costaron

1. **No confíes en el "PAUSED" que devuelve al crear.** En un caso real, las 6 campañas creadas "en pausa" estaban **activas**. Después de crear, pedile siempre que **verifique el estado real** y que pause lo que haga falta.
2. **Editar puede activar.** Cambiar solo el nombre o la puja de un conjunto lo dejó activo. Editar no es lo mismo que conservar el estado: volvé a verificar.
3. **Los estados quedan desparejos** entre campaña, conjunto y anuncio. Para lanzar con un solo interruptor: conjuntos y anuncios activos, **solo la campaña en pausa**.
4. **Los videos necesitan miniatura.** Al crear un creativo de video, el conector exige una imagen, aunque Meta diga que la genera sola. La solución es usar la miniatura que ya tiene el video subido.
5. **"No hay errores" no significa aprobado.** La consulta de errores no muestra los anuncios rechazados. Pedile que revise el estado de cada anuncio.
6. **El conector entra con el perfil de Facebook con el que lo autorizaste.** Si al conectarlo el navegador tenía abierta otra cuenta, no va a ver tus cuentas publicitarias. Autorizalo con el perfil correcto.
7. **Algunas cuentas no dejan subir videos por URL.** Subí los videos en una cuenta que sí deje (la cuenta master) y cloná desde ahí ([[metodo-v3]]).

## Reglas de armado del anuncio (correcciones de Santiago)

- **2026-10-21 — Anuncios multianunciante: siempre desactivado.** En "Configuración del anuncio" viene tildado por defecto. Hay que destildarlo en cada anuncio.
- **2026-10-21 — Cada parte del texto va en su campo:**
  - **Texto principal** → la descripción larga (el copy).
  - **Título** → "Tap the button below 👇".
  - **Descripción** → las 5 estrellas ⭐⭐⭐⭐⭐.
  - Nunca va todo junto en el texto principal.
- **Apagar la IA de Meta:** destildar los textos y títulos generados con IA, no elegir imágenes generadas con IA y dejar la traducción en 0 idiomas (por defecto viene activada en todos).
- **Error de Threads #4588023:** la cuenta publicitaria necesita tener asignada la cuenta de Instagram/Threads de la página, en Configuración del negocio. Sin eso no deja publicar.
- **Cuenta Reset FIT (2026-10-21):** el conector de Meta todavía no está habilitado en esa cuenta ("se está liberando de a poco"). Ahí se arma desde el navegador, y Santiago sube los videos a la biblioteca.

## Cómo pedirle las cosas

- Dale **todos los datos juntos**: cuenta, pixel, Página, link con UTMs, presupuesto, países, género y nombres. Si falta algo, que pregunte antes de crear.
- Pedile que **cree todo en pausa y te muestre el resumen** antes de activar.
- Al final, que **verifique el estado real** de cada campaña, conjunto y anuncio.

Relacionado: [[metodo-v3]] · [[nomenclatura-del-metodo]] · [[ia-en-el-flujo-de-trabajo]] · [[problemas-de-cuentas-meta]]

## Conexiones con tu operación actual
- La skill **`cazar`** está disponible en estas sesiones: puedo buscar winners en la Biblioteca de Anuncios cuando me lo pidas.
- El conector de Meta Ads **no está conectado en este entorno** (sesión en la nube). Para crear campañas desde Claude hay que conectarlo en esta sesión o trabajar desde la tuya.
- La regla "crear todo en pausa → mostrar resumen → verificar el estado real" pasa a ser obligatoria para mí cada vez que toque campañas.

## Fuentes
- RAW/2026-10-10-wiki-previa/claude-con-meta-ads.md (página de la wiki previa, actualizada el 2026-09-24)
- Fuentes originales citadas (todavía no están en este cerebro): operación real con el conector de Meta Ads en Claude Code, septiembre 2026
