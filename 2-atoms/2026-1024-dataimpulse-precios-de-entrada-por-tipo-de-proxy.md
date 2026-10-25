---
id: 2026-1024-dataimpulse-precios-de-entrada-por-tipo-de-proxy
type: atom
certainty: solid
sources: [sources/2026-10-23-dataimpulse-proxies.md]
links: ["[[2026-1023-5sim-sms-verificacion-como-coste-marginal-de-alta]]", "[[2026-1023-lzt-topup-mastercard-comision-10]]", "[[2026-1022-costes-por-categoria-tenant]]", "[[2026-1024-dataimpulse-escalera-de-volumen-por-tipo]]"]
---

## Claim
La home de DataImpulse fija el precio de entrada por gigabyte de cada uno de sus cuatro pools: **residencial $1/GB, datacenter $0.50/GB, móvil $2/GB y premium residencial $5/GB**, con un plan "Intro" de **$5** ("For New Users") en los cuatro tipos de proxy. El FAQ lo repite en su forma más directa: *"Residential starts from $1 per GB without a subscription. You pay only for the traffic you use. Mobile proxies start from $2/GB, and datacenter ones are the cheapest – just $0.50 per GB."*

## Why It Matters
El precio es el eje de posicionamiento del proveedor, no un detalle: dentro del mismo catálogo, el datacenter cuesta **la mitad** que el residencial, el móvil cuesta **el doble** y el premium residencial **cinco veces más**. Es una escala explícita de riesgo de bloqueo — datacenter = rápido y barato pero "best for sites that don't aggressively block server IPs"; móvil = "not the cheapest but still the strongest option" para verificación publicitaria y plataformas sociales.
Para el modelo de coste del vault esto cambia la jerarquía de insumos: el proxy **no** es un coste marginal pequeño al lado del SMS (que va de $0.1026 a $8.8897 por número en [[2026-1023-5sim-sms-verificacion-como-coste-marginal-de-alta]]). A $1/GB, el tráfico de proxy puede dominar el coste de un alta si el flujo consume MB por sesión, y además es el único insumo cuyo coste depende de un volumen que el proveedor controla (tráfico no consumido = no facturado, ver [[2026-1024-dataimpulse-payg-sin-suscripcion-ni-caducidad]]).
El matiz de la comisión sigue vigente: si se recarga con Mastercard hay un 10 % de comisión sobre el saldo ([[2026-1023-lzt-topup-mastercard-comision-10]]), aunque DataImpulse no publica comisiones: su lista de métodos de pago es solo una fila de iconos, sin cifras.

## [FRICTION]
> [[2026-1022-costes-por-categoria-tenant]] afirma que el coste del producto se reparte en tres categorías — `categoryCloneResponses` y `categoryIngestion` (facturables al tenant) frente a `categoryPlatformOps` (memoria, embeddings, clasificadores internos, absorbidos por la plataforma) — y que "el consumo del tenant escala linealmente pero la operación interna no se traslada".
> Este átomo presiona ese corte porque el tráfico de proxy es un **tercer insumo variable con coste marginal explícito** (hasta $5/GB en premium residencial) que no encaja en ninguna de las tres categorías: no es respuesta de clon, ni ingesta, ni operación interna. En un pipeline de altas automatizadas con IP por cuenta, ese tráfico escala linealmente con el tenant, exactamente como las categorías facturables.
> Ambas no pueden ser completamente correctas: o el proxy entra como coste variable por tenant facturable (rompiendo la asunción de que las operativas internas no se trasladan), o se asume absorbido por la plataforma, con lo que su crecimiento lineal erosiona el margen de forma invisible en el panel de [[2026-1022-platform-admin-tenants-costes-mrr]]. Marcado para juicio humano, no auto-resuelto.

## Nota de verificación
Números transcritos literalmente de la home y del FAQ. La captura **no** publica: número máximo de conexiones simultáneas, ancho de banda por conexión, ni comisiones o cambio de divisa.

## Nota fechada — 2026-10-24 (captura IPRoyal, no modifica lo anterior)
Un segundo proveedor confirma que **el $/GB no es la unidad del sector**, solo la de DataImpulse. IPRoyal publica cinco líneas con **cinco unidades distintas**: residencial $1.75/GB (pool 64M+), ISP $1.80/proxy (500K+ IPs), datacenter $1.39/proxy (60+ ubicaciones, "unlimited bandwidth"), móvil $117/mes (4.5M+ IPs) y Web Unblocker $1.00/1000 requests. Es decir: el residencial de IPRoyal es **×1,75** del de DataImpulse, y el móvil pasa de coste marginal por GB a **coste fijo recurrente** ([[2026-1024-iproyal-cinco-lineas-y-cinco-unidades-de-precio]], [[2026-1024-iproyal-movil-117-al-mes-y-45m-de-ips]], [[2026-1024-iproyal-datacenter-139-por-proxy-y-60-ubicaciones]]). La escala de precios de este átomo sigue siendo válida **para el catálogo de DataImpulse**, pero no puede generalizarse al sector.
