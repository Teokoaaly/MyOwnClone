---
id: 2026-1026-new-api-reintento-de-tarea-reserva-el-sobrante-y-no-sale-si-no-alcanza
type: atom
certainty: solid
sources: [sources/2026-10-25-new-api-releases.md]
links: ["[[2026-1023-new-api-routing-por-grupo-prioridad-y-afinidad]]", "[[2026-1023-new-api-grupos-como-eje-de-precio-del-relay]]", "[[2026-1026-new-api-canales-y-plugins-competen-por-prioridad-y-peso]]"]
---

## Claim
**v1.0.0-rc.46** corrige el **precio usado en el reintento de una tarea**: antes, al reintentar en otro canal, se **cobraba con el precio del intento anterior**. Ahora, si el canal de reintento es **más caro**, el gateway **reserva primero la diferencia**; y **no llama al canal si el saldo no cubre** esa diferencia.

La misma versión corrige que el envío y el sondeo de tareas **ignoraban el "Request Header Override"**.

## Why It Matters
Es un fallo de ingreso con nombre: **cobrar al precio del intento anterior** es exactamente el tipo de fuga que un gateway de reventa no puede permitirse, porque el reintento es precisamente el camino caro (el primer canal falló). El arreglo no es solo contable: introduce una **pre-autorización de la diferencia** y una **condición de saldo antes de despachar**, o sea, el mismo patrón **fail-closed** que ya se había documentado en el motor de precios del gateway.
El efecto estructural es que el **precio deja de ser una propiedad del modelo** y pasa a ser **una propiedad del par (modelo, canal)** — lo cual conecta directamente con el routing por prioridad y peso ([[2026-1023-new-api-routing-por-grupo-prioridad-y-afinidad]]) y con la lectura de que el grupo es el eje de precio ([[2026-1023-new-api-grupos-como-eje-de-precio-del-relay]]): en la práctica, **el mismo modelo puede tener tres precios según qué canal lo haya servido**, y la tabla de precios pública de un relay no lo refleja.
El arreglo del **Request Header Override** es la otra cara: si el override no se aplicaba al envío ni al sondeo, la petición de tarea **no era la que el operador configuró**, y con ella la cabecera que a veces transporta la identidad del upstream.

## [FRICTION]
> [[2026-1023-new-api-grupos-como-eje-de-precio-del-relay]] sostiene (marcado `tentative`) que **el grupo es el eje sobre el que el operador aplica su decisión comercial de precio**, y que el precio se define **por modelo y por nivel de uso**, con el grupo como palanca de asignación.
> Este átomo presiona esa creencia en un punto concreto: con el arreglo de rc.46, **el precio cobrado pasa a depender del par (modelo, canal)**, porque un reintento a un canal más caro **cobra la diferencia**, y un canal que no puede cubrirla **no se llama**. Es decir, el precio efectivo de una misma llamada **varía según qué canal la sirvió**, y esa variación es invisible en la tabla de precios de un relay.
> Ambas no pueden ser completamente correctas en su lectura general: o el grupo sigue siendo el único eje de precio (y entonces el sobreprecio del canal caro es un error residual del motor), o el precio es **multidimensional** —grupo, modelo, canal y momento del reintento— y el "precio del modelo" que se publica es solo uno de sus componentes. Marcado para juicio humano, no auto-resuelto: el release note describe el comportamiento del reintento de **tareas**, no el de las peticiones de texto ordinarias, y no dice si el mismo mecanismo de precio-por-canal se aplica ahí.

