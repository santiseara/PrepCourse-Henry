# Color Exacto (CrobaVault) — coloración capilar

> Curso digital de **colorimetría** de la página **Nube Educativa** (checkout `crobavault-t8.impultienda.ar`), con **~200 anuncios activos** el 15/11/2026. Lo clonamos para **Argentina**, que es el único mercado grande que ellos no están tocando. (fuente: Facebook Ads Library + su landing)

## La oferta de ellos
- **Nombre:** Color Exacto · **mecanismo:** el *Método de las 3 Lecturas* (altura → fondo de aclaración → reflejo).
- **Promesa:** dejar de teñir a ojo. *"No te falta mano: te falta la fórmula correcta."*
- **Entregables:** 100 fórmulas por caso (tinte, oxidante y tiempo), 15 módulos y 40 lecciones, 6 herramientas para imprimir (carta de alturas, estrella de neutralización, ficha de diagnóstico), certificado.
- **5 bonos:** Tu primer color en una tarde · Tabla de gramos · Rescate de color (20 errores) · Foto imposible (12 pedidos difíciles) · Rubios, grises y platinados (15 fórmulas de matiz).
- **Precio:** US$ 24 (tachado US$ 59), pago único, acceso por mail en 24 h.
- **Avatar:** la que quiere trabajar de colorista o ya atiende clientas y le tiene miedo al color. Trabaja en su casa, a domicilio o en un salón.

## Dónde corren (y dónde no)
Los 30 anuncios más vistos son **el mismo set de 6 ángulos traducido** a italiano, francés, inglés, alemán, japonés y hebreo. **Ni uno en español.** Es arbitraje de mercado puro: la oferta está validada y el castellano rioplatense está libre.

## Los 6 ángulos de su arsenal
| # | Ángulo | Hook |
|---|---|---|
| 1 | Oferta directa | "Mechas, babylights, balayage y 100 fórmulas, paso a paso" |
| 2 | Mecanismo visual | "Esta carta tiene 10 alturas de tono: con ella dejás de teñir a ojo" |
| 3 | Miedo al color | "¿Querés trabajar de peluquera pero el color te da miedo?" |
| 4 | Dolor técnico | "¿Te cuesta identificar alturas, fondos o qué poner para neutralizar?" |
| 5 | Demanda del mercado | "Rubios sin amarillo, cobres que brillan y canas tapadas: eso es lo que más te piden" |
| 6 | **El error concreto** ⭐ | "¿Por qué le quedó naranja?" / "Quería rubio frío y se fue amarilla" |

El 6 es el más repetido de todos: es el que lleva la **reatribución de culpa**, que es el corazón de la oferta.

## DNA de sus guiones (29 s, ~80 palabras)
1. **Hook:** el error concreto que la colorista ya vivió, en forma de pregunta.
2. **Reatribución:** *"no fue tu mano"* / *"no es mala suerte"* / *"no fue el matizador"* → la culpa es del fondo de aclaración o de la fórmula, nunca de ella.
3. **Mecanismo:** las 3 lecturas antes de abrir el pomo → la fórmula sale escrita.
4. **Entregables con número:** 100 fórmulas, 40 clases, carta de alturas, 5 bonos.
5. **Capacidad:** desde cero, a tu ritmo, en tu casa / a domicilio / en tu salón, con la primera clienta.
6. **CTA:** "Tocá Más información" (+ "y dejá de adivinar" / "y prepárate").

**Nunca dicen el precio en el video.** El primary text tampoco: el precio aparece recién en la landing.

## Su montaje (hoja de contactos de 2 creativos)
- B-roll real de coloración: papel aluminio, pincel y bowl, guantes, mechas, el resultado peinado.
- **Pastilla amarilla arriba** con el hook los primeros segundos ("YELLOW BLONDE?").
- Subtítulo en **cursiva blanca**, dos o tres palabras, centrado abajo.
- Mockups del producto flotando (tapa, rueda de neutralización, bono de rubios). **Eso no lo copiamos**: la regla de [[guiones-y-anuncios]] prohíbe la foto fija, y los entregables se cuentan con placas de texto sobre el b-roll.
- Cierre: botón naranja "TAP LEARN MORE".

## Lo nuestro (tanda 1, 2026-11-15)
- 6 guiones en **voseo**, uno por ángulo, 75-82 palabras → 25-28 s. `OUTPUTS/2026-11-15-guiones-color-exacto-tanda1.md`.
- Voz **Sulafat** con style rioplatense de colorista, `speed 1.30`.
- Pool de **20 clips limpios de 36** revisados, de `#balayage`, `#coloracioncapilar`, `#mechascabello` y `#babylights`. El nicho del color es de los más limpios que vimos: casi todo es espalda, manos y pelo, sin cara y sin subtítulo quemado.
- Editor `OUTPUTS/scripts-vsl/edit_color.py` (clon de `edit_macrame.py`) con la pastilla del hook en **amarillo #F5C518** y el botón en **terracota #C1622F**, como ellos.
- **El texto de objeto se deja:** el clip con los tubos `8.46 + 8.60` es exactamente la fórmula de la que habla el guion.

## Dos cosas que costaron un re-render (2026-11-15)
- 🐞 **`edit_macrame.py` no traía `noflip`.** Al clonarlo salieron los tubos **8.46 + 8.60 espejados**: los números
  del tinte se leían al revés, justo en el ad que vende fórmulas. El editor espeja un clip cuando su `usage` es impar;
  keymaster ya tenía la excepción y macramé no. **Al clonar un editor, revisar que soporte `noflip` antes de armar un
  pool con texto de objeto** (tubos, cajas, etiquetas, códigos).
- **El chip lleva una cruz roja**, así que su texto tiene que ser **el costo, no el beneficio**. En V5 decía *"es lo que
  mejor se paga"* con una cruz al lado: quedó como un error. Pasó a *"y se va a otro salón"*.

## Preguntas abiertas
- Nombre para Argentina: ¿se queda **Color Exacto** o se renombra el método?
- Checkout y precio en pesos (todavía no hay landing AR).

## Relacionado
[[guiones-y-anuncios]] · [[caza-de-ofertas]] · [[atlas-de-cortes]] · [[nail-designer]] · [[funnel-hacking]]

## Fuentes
- Facebook Ads Library, búsqueda `crobavault-t8.impultienda.ar` (15/11/2026): ~200 anuncios activos, página Nube Educativa.
- `https://crobavault-t8.impultienda.ar` (landing completa).
- 10 creativos bajados y transcriptos con faster-whisper.
