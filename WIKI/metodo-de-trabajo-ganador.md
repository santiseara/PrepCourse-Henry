# Método de trabajo ganador (propuesta del 27/11/2026)

> Diagnóstico de por qué ninguna de las ofertas de octubre-noviembre vendió, y el método nuevo que
> lo corrige. Nace del pedido de Santiago del 27/11: *"no nos está funcionando ninguna oferta…
> estamos haciendo claramente algo mal… hagamos las cosas distintas… que todo lo que tiremos al
> menos venda"*. Contrastado contra [[atelie-3d]].

## El diagnóstico, con los hechos del propio repositorio

**1. Tiramos 30 ofertas nuevas en 42 días.** Del 16/10 al 26/11, el changelog registra **30 altas
de oferta nueva**: una cada 1,4 días. El método que ya está escrito en [[validacion-de-oferta]] dice
*100 USD y una semana por oferta* y *una sola oferta hasta que genere 1.000-2.000 USD/día*. No es
que falte método: es que no lo estamos corriendo.

**2. No estamos lanzando ofertas: estamos lanzando creativos.** Las 6 carpetas de oferta que viven
hoy en el Escritorio (Fuga Perfecta, Laser Profit Vault, Mini Plaster, Puertas de ACM, The 3D
Method, The Artist Method) tienen **`landing/` vacía y `imagenes/` vacía en las 6**. Todo el trabajo
está en `anuncios/`. La última landing armada es del **20/11**; después hubo 10 ofertas nuevas sin
una sola página. Una oferta es promesa + landing + checkout + producto + backend; estamos entregando
el pedazo que menos decide la venta.

**3. Nuestra propia wiki ya decía dónde está el problema.** [[lectura-de-resultados]]: *"casi nunca
es el anuncio: era la landing"*, y la métrica que separa ganadores de perdedores es **cuántos pasan
de ver la landing a iniciar el pago** (15 de cada 100 en los ganadores, 10 en los perdedores).
Es exactamente el tramo que no estamos construyendo.

**4. Vendemos archivos; los que venden, venden la cuenta.** Los 12 ads de [[atelie-3d]] no prometen
400 archivos: prometen *gastás pocos reales de filamento, te pagan feliz, multiplicalo por las
encomiendas hasta Navidad*. Lo mismo decía [[ofertas]] hace un mes y medio: *"Scented Stones se
vende como 'ganá plata con un oficio'… las craft que no funcionaron se parecen más a hobby, que no
tiene urgencia de compra"*. Varias de las ofertas de noviembre son hobby.

**5. Matamos los creativos antes de que lleguen a trabajar.** Ateliê 3D corre los mismos videos
**desde el 20/10** y lo que hace es *sumar* ads, no reemplazarlos: ~120 activos. Nosotros tiramos 6,
y a los dos días estamos en otro nicho. Nunca llegamos al punto donde se aprende algo.

**6. La única que vendió, la soltamos.** Mini Plaster Studio dio ventas con buena conversión y poco
volumen (26/11). La respuesta correcta a eso es volumen y backend sobre esa oferta, no una oferta
nueva al día siguiente.

**7. Entramos caros y planos.** US$ 17-27 a público frío, sin nada arriba ni abajo. Ellos entran a
US$ 1,85 y cobran US$ 7 (R$ 37,90) o US$ 5 (R$ 27) en la misma página, antes del checkout.

## El método nuevo (las 10 reglas)

### Las que cambian qué lanzamos
1. **Una oferta a la vez.** No se empieza otra hasta que la anterior esté muerta (gastó su
   presupuesto de validación sin venta) o viva (vendió, y entonces se la trabaja). Cero excepciones.
2. **La promesa se escribe como una cuenta, en una línea**, antes de escribir un solo guion:
   *"gastás X, te pagan Y, N veces por mes"*. Si no se puede escribir, la oferta no se lanza.
   Hobby sin plata adentro = no se lanza.
3. **Deadline real o no hay oferta.** Estacional, de calendario operativo (como el calendario de
   producción de Ateliê), o de cupo verificable. Nunca un descuento inventado.

### Las que cambian cómo lo lanzamos
4. **Checklist de salida, de 5 piezas.** No sale a correr nada sin: (a) promesa y avatar escritos,
   (b) landing completa, (c) checkout probado con order bump, (d) producto entregable real aunque
   sea MVP, (e) 6 creativos. Falta una → no se sube a Meta.
5. **Escalera de precio en la misma landing**, copiada de [[atelie-3d]]: front barato de entrada
   (US$ 5-9) · plan premium como opción destacada (US$ 27-37) · modal de rescate si eligen el barato
   · order bump en el checkout · OTOs después ([[embudo-vsl-post-pago]]).
6. **La semana tiene forma fija:** día 1 oferta y promesa · día 2 producto MVP · día 3 landing y
   checkout · día 4 creativos · día 5 sale · días 6-7 se lee y se decide. Hoy el día 1 son 6 videos
   y el día 2 es otra oferta.

### Las que cambian cómo lo leemos
7. **Corte explícito antes de lanzar.** US$ 100-150 sin una venta = muerta, se cierra y se escribe
   por qué. Con ventas = **prohibido tocar el nicho**; se trabaja el embudo en el orden de
   [[lectura-de-resultados]] (landing → pago, aprobación de tarjetas, AOV).
8. **Ningún creativo nuevo sin el número delante.** Todo pedido de renovaciones o variables viene
   con la captura de Meta. Si no hay número, lo que falta no es creativo.
9. **Sobre la que vende, volumen, no novedad.** De 6 ads a 20-30 del mismo cuerpo con hooks nuevos,
   como hacen ellos. Renovar la estética recién cuando la frecuencia lo pida
   ([[renovacion-de-creativos]]).
10. **Un registro por oferta con plata adentro:** gasto, ventas, CPA, landing → pago. Hoy el
    registro dice qué entregamos, no qué pasó.

## Preguntas abiertas

- Faltan los números reales de las últimas 10 ofertas (gasto y ventas por oferta). Sin eso, los
  puntos 1 y 7 son el diagnóstico más probable, no uno medido.
- ¿Quién arma hoy la landing y el checkout, y por qué las 6 carpetas `landing/` están vacías?
  Es el punto que más vale resolver de todo este documento.

## Relacionado

[[atelie-3d]] · [[validacion-de-oferta]] · [[lectura-de-resultados]] · [[seleccion-y-modelado-de-oferta]] ·
[[ofertas]] · [[aumento-de-aov]] · [[the-3d-method]] · [[mini-plaster-studio]]

## Fuentes

- `changelog.md` (30 altas de oferta nueva entre el 16/10 y el 26/11/2026)
- `~/Desktop/<oferta>/landing/` de las 6 ofertas vivas (vacías las 6, 27/11/2026)
- Biblioteca de Anuncios y landing de [[atelie-3d]], 27/11/2026
