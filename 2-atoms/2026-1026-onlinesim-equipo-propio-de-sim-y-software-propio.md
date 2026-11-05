---
id: 2026-1026-onlinesim-equipo-propio-de-sim-y-software-propio
type: atom
certainty: tentative
sources: [sources/2026-10-25-onlinesim-virtual-sms.md]
links: ["[[2026-1023-herosms-sobre-la-infraestructura-de-sms-activate]]", "[[2026-1023-sms-activate-cierra-total-el-22-de-diciembre]]", "[[2026-1023-hero-sms-stock-fisico-y-virtual-por-servicio]]"]
---

## Claim
El FAQ de OnlineSim declara **infraestructura de primer nivel**: "We have our own **equipment that holds the SIM cards** and our own **software** that we use to provide mobile numbers to customers to receive messages. When a customer sends a message to an acquired mobile number, it comes to the SIM card. Our software transmits it in the interface of our service." Es decir: hardware propio con tarjetas SIM físicas, software propio de desvío, y una descripción del pipeline que va del SMS entrante a la interfaz.

## Why It Matters
Es una afirmación que **cambia el mapa de operadores del vault**. El corpus actual tenía a 5sim como operador autónomo y a HeroSMS como **fachada white-label sobre la infraestructura de SMS-Activate** ([[2026-1023-herosms-sobre-la-infraestructura-de-sms-activate]]), con SMS-Activate ya cesado por completo ([[2026-1023-sms-activate-cierra-total-el-22-de-diciembre]]). Si OnlineSim tiene equipo y software propios, entonces el **pool de números** no es un recurso único heredado del operador saliente, sino un recurso que al menos dos proveedores pueden tener por separado — lo que significa que la hipótesis de "stock compartido" que el vault explora para explicar las cifras anómalas de 5sim ([[2026-1023-5sim-catalogo-servicios-precios-y-stock]]) necesita más de un candidato.
La existencia de stock **físico** como base (tarjetas SIM en un equipo propio) también matiza el dato de HeroSMS, donde el físico era un residuo del 0,4 % al 1,2 % del inventario ([[2026-1023-hero-sms-stock-fisico-y-virtual-por-servicio]]): aquí el físico no es residuo, es el **sustrato**.
Advertencia: es una declaración del propio proveedor, no una verificación, y no aporta ni número de SIM, ni países, ni stock.

## [FRICTION]
> [[2026-1023-herosms-sobre-la-infraestructura-de-sms-activate]] (escrita hace tres días) afirma que HeroSMS es una fachada sobre SMS-Activate y que "el pool de números y la cobertura de país **heredan** del operador de origen", dejando la herencia como inferencia.
> Este átomo presiona esa creencia en un punto: si OnlineSim declara equipo y software propios, **existe un segundo operador con SIM cards propias**, de modo que o HeroSMS hereda el pool de SMS-Activate y OnlineSim tiene el suyo (dos pools distintos, dos políticas de cobertura distintas — coherente con que uno sirva Rusia/Bielorrusia y el otro no), o el "own equipment" de OnlineSim es marketing en la misma línea que el resto de sus contadores y entonces el pool heredado sigue siendo el único explicable.
> Ambas no pueden ser completamente correctas como descripción de la estructura del sector: o hay un único linaje de infraestructura con varios escaparates, o hay varios operadores de hardware y la "herencia" de HeroSMS no explica el stock. Marcado para juicio humano, no auto-resuelto.
