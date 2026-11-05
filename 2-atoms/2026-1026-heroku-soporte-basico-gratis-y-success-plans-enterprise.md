---
id: 2026-1026-heroku-soporte-basico-gratis-y-success-plans-enterprise
type: atom
certainty: solid
sources: [sources/2026-10-25-heroku-pricing.md]
links: ["[[2026-1023-hetzner-sla-99-9-gdpr-e-iso-27001]]", "[[2026-1026-heroku-private-y-shield-desde-125-y-150-dolares]]", "[[2026-1026-heroku-elements-1-credito-igual-a-1-dolar-solo-enterprise]]"]
---

## Claim
La sección **Heroku Success** declara: *"**Basic Support is free for all Heroku customers** and includes access to documentation, Trailhead, Trailblazer communities, and our Help Portal. Go further with **Enterprise Success Plans—Standard, Premier, and Signature—offering faster response times and expert guidance** for your mission-critical applications"*. La página **no publica precios** ni tiempos de respuesta concretos para ninguno de los tres planes de pago; los precios se obtienen vía "Contact sales".

## Why It Matters
Es el **eslabón que falta** en la comparación de coste de riesgo que el vault viene construyendo: hasta ahora el patrón era "**el precio barato viene con SLA y cumplimiento sin publicar**" ([[2026-1023-hetzner-sla-99-9-gdpr-e-iso-27001]]). En Heroku, el soporte de base es **gratuito para todos los clientes**, sin SLA ni créditos, y el soporte con tiempos de respuesta garantizados **existe pero no tiene precio público** — hay que contactar con ventas. Es decir, la misma forma de "**lo que cuesta dinero no está en la página**" que el vault ya vio con el Private Space y con las ediciones de Connect.
La diferencia con los proveedores de VPS del vault es que aquí **el soporte no es un extra sobre el precio del servidor**: es una capa separada, con su propio gate (Enterprise) y su propio circuito comercial. Un producto que vende a clientes finales necesita saber **qué respaldo da su proveedor cuando hay una caída**, y la respuesta estructural es: soporte de comunidad gratis, y soporte con SLA solo en un tramo que no se puede presupuestar desde la página.
Para el producto del vault esto importa en un punto concreto: el tier **Shield** ($150/mes el dyno más pequeño) promete HIPAA/PCI, BAAs, keystroke logging y strict TLS ([[2026-1026-heroku-private-y-shield-desde-125-y-150-dolares]]), es decir, **el aislamiento de red cuesta una cifra y la atención por incidente cuesta otra, y esa segunda no está cuantificada**.

## Nota de verificación
La página no publica **ni un solo número** de esta sección: sin precios, sin tiempos de respuesta, sin créditos, sin SLA. Los tres nombres de plan (Standard, Premier, Signature) y la gratuidad del Basic Support son lo único verificable.


## Nota de extensión 2026-10-26
La captura de `https://support.heroku.com/` (2026-10-25) confirma y precisa esta afirmación del pricing desde el otro lado del producto, es decir, desde donde vive la promesa.

**El "Trailblazer communities" del Basic Support tiene destino concreto y es público.** La home de soporte ofrece, junto al ticket, **"Ask the community"** → **Stack Overflow con la etiqueta `heroku`** (`stackoverflow.com/questions/tagged/heroku`), y lo describe como *"Engage with a community of passionate experts to get the answers you need"*. Es decir, el Basic Support gratuito no es solo "documentación + portal": incluye explícitamente un **corpus público indexable** de respuestas de terceros. El detalle literal de la captura es que ese canal aparece **antes** que la vía de ticket: *"Looking for more help? Ask the community or create a ticket to get it routed to the best person to answer it."* ([[2026-1026-heroku-soporte-canales-externos-stackoverflow-y-pagina-de-estado]]).

**El Help Portal del Basic Support tiene una taxonomía de 14 categorías con identificadores numéricos estables**, y una de ellas es "Billing, Verification & Payments" (`n/2`) ([[2026-1026-heroku-soporte-catorce-categorias-con-identificadores-numericos]], [[2026-1026-heroku-soporte-categoria-billing-verification-y-payments]]).

**La promesa "faster response times" sigue sin ninguna cifra, y la propia home añade un elemento que la contradice en el plano operativo**: el artículo más leído del portal es **"Before opening a support ticket"**, es decir, el contenido más consultado del soporte de Heroku es la instrucción de *no* abrir ticket ([[2026-1026-heroku-soporte-articulo-mas-tendido-es-instruccion-para-no-abrir-ticket]]). Un ticket que no se abre no tiene tiempo de respuesta.

**Y hay una cuarta puerta, sin precio ni contenido publicado en la captura**: **"Enterprise Resources"** (`help.heroku.com/enterprise`), un directorio de soporte propio del estado Enterprise, distinto de "My tickets" y de "Create a ticket" ([[2026-1026-heroku-enterprise-resources-como-seccion-propia-del-soporte]]).

Nota: la captura del soporte **no** reproduce precios, ni tiempos de respuesta, ni SLA, ni el contenido de `help.heroku.com/enterprise`. La extensión no cierra ninguno de esos huecos; los confirma.
