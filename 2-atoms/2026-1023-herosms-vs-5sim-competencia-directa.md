---
id: 2026-1023-herosms-vs-5sim-competencia-directa
type: atom
certainty: solid
sources: [sources/2026-10-22-hero-sms-home.md, sources/2026-10-22-5sim-home.md]
links: ["[[2026-1023-herosms-catalogo-cinco-servicios-visibles]]", "[[2026-1023-herosms-precios-escapate-entre-0059-y-08551]]", "[[2026-1023-5sim-catalogo-servicios-precios-y-stock]]"]
---

## Claim
HeroSMS y 5sim se pueden comparar en seis ejes observables desde sus homes (ambas capturas del 2026-10-22):

| Eje | 5sim | HeroSMS |
|---|---|---|
| Servicios en la lista visible de la home | 8 en el selector | 5 en el selector + 45 enumerados en el pie |
| Contador de exhaustividad | `Show all 1329` (servicios) / `Show all 153` (países) | `Show more` sin contador; claim de 700+ servicios y 180+ países |
| Precio "from" más bajo visible | $0.01 (Amazon, Facebook, Microsoft, OpenAI/ChatGPT, Instagram/Threads) | **$0.0059** (TikTok/Douyin) |
| Precio "from" más alto visible | $0.1 (Telegram) | **$0.8551** (Full rent) |
| Desglose de stock | un contador único por servicio | **físico y virtual separados** por servicio |
| Identidad de proveedor | operador autónomo | **fachada sobre SMS-Activate** (declarado) |

Los dos comparten el modelo base: prepago sobre saldo, sin suscripción, número suelto, flujo de compra por pasos, "Any other"/"Any Other" como fallback, y reembolso automático si el SMS no llega. Difieren en que 5sim publica **más nombres, más cifras y un desglose de precio por país y operador**, y en que HeroSMS publica **un desglose físico/virtual que 5sim no da** y un precio "from" más barato.

## Why It Matters
Es la lectura de decisión que el vault no tenía: los dos proveedores no son equivalentes en auditabilidad. Para un plan que quiera calcular margen sobre identidades verificadas, **5sim es el proveedor auditable** (CSV de precios por país-operador, 175 filas para un solo servicio) y HeroSMS es el proveedor **opaco pero potencialmente más barato** en escaparate. La cifra que separa las dos estrategias de aprovisionamiento es el suelo: $0.1026 medido (5sim, `telegram`) frente a $0.0059 anunciado (HeroSMS, TikTok/Douyin) — 17,4× de diferencia que ningún dato del vault permite todavía resolver, porque son magnitudes distintas (mínimo medido vs. "from" publicitario).
Y hay que tener en cuenta que **no son dos proveedores independientes**: HeroSMS declara ser un producto nuevo construido sobre la infraestructura de SMS-Activate ([[2026-1023-herosms-sobre-la-infraestructura-de-sms-activate]]), lo que puede explicar que su catálogo y sus cifras de marketing hereden los de un tercero.

## Nota de verificación
La tabla resume datos ya verificados en los átomos hermanos: [[2026-1023-herosms-catalogo-cinco-servicios-visibles]], [[2026-1023-herosms-precios-escapate-entre-0059-y-08551]], [[2026-1023-hero-sms-stock-fisico-y-virtual-por-servicio]] y [[2026-1023-5sim-catalogo-servicios-precios-y-stock]]. Las fuentes de 5sim citadas en esta tabla proceden de átomos ya existentes del vault, no de una captura nueva en esta corrida.


## Nota de extensión 2026-10-27
A partir de `sources/2026-10-26-hero-sms-api-docs.md`.

Este átomo compara HeroSMS y 5sim como competencia directa. La página de API añade **un eje de comparación que antes no era medible**: quién **publica su contrato técnico**. HeroSMS publica OpenAPI 3.2.0 en JSON y YAML, servidor `https://hero-sms.com/api/v1`, `apiKeyAuth` con cabecera `Authorization` y **clientes de ejemplo en Shell, Ruby, Node.js, PHP y Python** ([[2026-1027-hero-sms-openapi-3-2-0-con-api-key-en-la-cabecera-authorization]]); 5sim integra la compra dentro del chat y no expone una especificación equivalente ([[2026-1023-5sim-asistente-ia-integrado]]).

Consecuencia para el Editor: la comparación puede añadir una **columna de documentabilidad** a la tabla de proveedores de SMS, y conviene encuadrarla bien: **publicar la especificación no es publicar el precio**. HeroSMS sigue sin precios públicos ([[2026-1024-herosms-url-de-precios-devuelve-404-y-no-publica-precios-propio]]), de modo que el resultado del cruce es que **el proveedor con el contrato técnico más abierto es también el más opaco en precio** —lo que refuerza, en vez de debilitar, la tesis del thread de que **en SMS el precio solo se obtiene entrando al panel con saldo**.
