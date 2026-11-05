---
id: 2026-1027-dataimpulse-movil-detection-not-latency
type: atom
certainty: solid
sources: [sources/2026-10-26-dataimpulse-mobile-proxies.md]
links: ["[[2026-1024-dataimpulse-cuatro-tipos-y-que-cada-uno-resuelve]]", "[[2026-1024-2captcha-velocidad-de-resolucion-1-a-2-segundos-en-los-tipos-estandar]]", "[[2026-1024-dataimpulse-precios-de-entrada-por-tipo-de-proxy]]", "[[2026-1027-dataimpulse-sesion-sticky-movil-hasta-120-minutos]]"]
---

## Claim
El FAQ "Are DataImpulse mobile proxies fast?" da el criterio de elección del pool en función del cuello de botella, no de la cifra de latencia: **"Speed depends on two things: the carrier network in the target country and how far the request travels. On 4G/5G connections, DataImpulse mobile proxies typically deliver response times comparable to a regular mobile internet user in that location. For most part of scraping and verification tasks, latency isn't the bottleneck – detection is. Mobile proxy IPs have higher trust scores with target sites, so you get fewer blocks, which in practice means faster completion of the actual job. If speed is critical and detection isn't a concern, datacenter proxies will always be faster per-request."**

## Why It Matters
Es la **doctrina de selección de pool que el vault necesitaba y no tenía escrita**: el criterio no es "más rápido" sino "menos detectable", y el propio proveedor dice explícitamente que **el datacenter gana en velocidad por request** —a $0,50/GB, un 25 % del precio del móvil a $2/GB ([[2026-1024-dataimpulse-precios-de-entrada-por-tipo-de-proxy]])— siempre que la detección no sea el problema. Es una inversión de la intuición habitual (el móvil es "el premium") y encaja con la jerarquía de coste del thread: **correo ≪ captcha ≪ proxy ≪ SMS**, donde lo que se paga en el móvil no es ancho de banda sino **probabilidad de que el request llegue a su destino**.
Y hay una lectura de sistema que conecta con la §8.6: el captcha se resuelve en 1–2 segundos ([[2026-1024-2captcha-velocidad-de-resolucion-1-a-2-segundos-en-los-tipos-estandar]]), o sea que la latencia del captcha es **despreciable frente a la latencia del proxy**. Si además la detección —no la latencia— es el cuello de botella, entonces **el proxy es la partida donde se pierde el tiempo y el dinero del flujo**, y su modo de sesión (rotating vs sticky de 120 min, [[2026-1027-dataimpulse-sesion-sticky-movil-hasta-120-minutos]]) es lo que decide cuánto se pierde.
La consecuencia metodológica para el vault: "mobile proxies" no es una categoría de calidad superior genérica, es **una apuesta por la tasa de bloqueo**, y esa apuesta solo tiene sentido cuando el destino bloquea. En scraping de fuentes abiertas, el datacenter a $0,50/GB es la elección correcta por el propio criterio del proveedor.

## Nota de verificación
Párrafo transcrito literalmente del FAQ "Are DataImpulse mobile proxies fast?". "Latency isn't the bottleneck – detection is", "higher trust scores" y "fewer blocks" son **argumentos del proveedor sin medición**: la captura **no** publica ninguna latencia por país, ninguna tasa de bloqueo, ni comparación entre pools. El único dato con número es "response times comparable to a regular mobile internet user in that location", que es una comparación sin unidad.
