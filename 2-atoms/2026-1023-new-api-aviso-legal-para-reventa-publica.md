---
id: 2026-1023-new-api-aviso-legal-para-reventa-publica
type: atom
certainty: solid
sources: [sources/2026-10-22-new-api-github.md]
links: ["[[2026-1023-priceai-transit-canal-tipo-sub2api-vs-new-api]]", "[[2026-1023-priceai-descargo-de-responsabilidad-sin-sla]]", "[[2026-1023-lzt-categoria-llm-accounts-para-reventa]]"]
---

## Claim
El README abre con dos bloques normativos que no son boilerplate:

**"Important"**: el proyecto se declara *"intended solely for lawful and authorized AI API gateway, organization-level authentication, multi-model management, usage analytics, cost accounting, and private deployment scenarios"*; los usuarios **deben obtener legítimamente** las claves, cuentas, servicios y permisos de interfaz upstream y **cumplir los términos de servicio upstream**; y quienes ofrezcan servicios de IA generativa al público deben cumplir los requisitos regulatorios de su jurisdicción: **registro, licencias, seguridad de contenido, verificación de identidad real, retención de logs, impuestos** y **autorización upstream**.

**"Warning"**: al operar el proyecto como **servicio público de IA generativa o servicio de reventa de API**, el usuario debe completar *primero* todas las obligaciones de *filing, licensing, content safety, real-name verification, log retention, tax, payment, and upstream authorization*.

## Why It Matters
El vault tiene muchos datos sobre un sector —el relay de reventa— que opera al otro lado de esta advertencia. Los 8 canales "New API" del ranking de PriceAI ([[2026-1023-priceai-transit-canal-tipo-sub2api-vs-new-api]]) son exactamente los despliegues que este README condiciona, y ninguno de esos canales publica SLA ni asume responsabilidad ([[2026-1023-priceai-descargo-de-responsabilidad-sin-sla]]).
El dato estructural que este README añade es que **la verificación de identidad real y la retención de logs son obligaciones explícitas**, no buenas prácticas: es un recordatorio de que la reventa de API está parcialmente regulada, y que la documentación del vault debe tratar estos relays como **infraestructura sin SLA y con exposición regulatoria**, no como simple proveedor barato.
Y conecta con el tema de reventa de cuentas de IA ([[2026-1023-lzt-categoria-llm-accounts-para-reventa]]): la diferencia entre "reventa de acceso a un modelo" y "reventa de cuentas" es precisamente si la cuenta upstream es tuya y está autorizada — que es lo que este README exige.

## [FRICTION]
> [[2026-1023-priceai-transit-canal-tipo-sub2api-vs-new-api]] afirma que los canales etiquetados "New API" son **despliegues del mismo stack open source con distinta marca, distinto 号池 y distinto multiplicador**, y que "comparar 30 relays es comparar, en su mayor parte, 30 despliegues del mismo stack".
> Este átomo presiona esa creencia en un punto: el stack open source **no es una implementación neutra**, declara una postura de cumplimiento explícita (claves upstream legítimas, registro, identidad real, retención de logs, impuestos) que un despliegue real de reventa a precio 0.04x–7.00x difícilmente puede exhibir. Si la etiqueta describe el software y no su cumplimiento, entonces "mismo stack" no significa "misma operación": hay una distancia entre el software que se despliega y las obligaciones que ese software asume.
> Ambas no pueden ser completamente correctas en su lectura general: o la etiqueta "New API" de la tabla describe solo el software (y las obligaciones se incumplen o se cumplen en un ámbito que PriceAI no tabula), o esos canales no son despliegues New API equivalentes sino implementaciones derivadas. Marcado para juicio humano, no auto-resuelto: la fuente no contiene ningún dato de cumplimiento de los canales concretos.
