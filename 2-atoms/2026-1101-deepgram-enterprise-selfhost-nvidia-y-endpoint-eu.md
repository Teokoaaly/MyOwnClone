---
id: 2026-1101-deepgram-enterprise-selfhost-nvidia-y-endpoint-eu
type: atom
certainty: solid
sources: [sources/2026-11-01-deepgram-pricing.md, sources/2026-11-02-deepgram-pricing.md, sources/2026-11-03-deepgram-pricing.md]
links: ["[[2026-1101-deepgram-concurrencia-y-regiones-por-plan]]", "[[2026-1023-hetzner-regiones-y-zonas-de-disponibilidad]]", "[[2026-1031-deepgram-growth-4000-anuales-y-sobreconsumo-10]]"]
---

## Claim
Dos factores de enterprise separan a Deepgram del pay-as-you-go: (1) el **despliegue self-hosted** "run in your own VPC or on-prem hardware and **require NVIDIA GPUs**" y solo está en Enterprise, con "FIPS 140-3 images"; (2) un **endpoint en la UE** (`api.eu.deepgram.com`) con "GDPR Ready & EU Data Residency", además de SOC 2 Tipo 1 y 2, HIPAA con BAA, CCPA y PCI. En Enterprise los precios son "Custom pricing" en todas las tablas y "Enterprise pricing ladders down with committed volume".

## Why It Matters
El endpoint EU es el dato que importa en el eje de "hosting barato en la UE" del vault ([[2026-1023-hetzner-regiones-y-zonas-de-disponibilidad]]): permite que el audio de los tenants no salga de la Unión, lo que es la respuesta directa a la fricción GDPR de los clones de voz en vivo. El precio de esa garantía, sin embargo, es que **self-hosted exige GPU NVIDIA y agreement de Enterprise**, lo que está en las antípodas del techo de ≤ €4/mes de infraestructura: la opción "sin salir de la UE" está disponible en la nube (endpoint EU) sin GPUs, mientras que la opción "sin enviar audio a terceros" es Enterprise y con hardware propio. Son dos decisiones distintas, y confundirlas lleva a presupuestar GPUs de IA para resolver un problema de residencia de datos que la nube ya resuelve.

## [FRICTION]
> La página presenta Enterprise como "Custom pricing" sin cifras, pero también afirma que "Enterprise pricing ladders down with committed volume... Talk to sales if you are processing millions of minutes a month" — es decir, **existe una escalera de descuentos por volumen en Enterprise que no está publicada**, frente al Growth que sí publica su tabla completa.
> No es una contradicción dura, pero significa que cualquier comparación de "cuál proveedor es más barato a escala" entre Deepgram y AssemblyAI es incompleta: la mitad del rango de Deepgram (Enterprise) no es auditable con datos públicos. Marcado para juicio humano, no auto-resuelto.

## 2026-11-03 — re-verificación
Cuarta captura: los datos de Enterprise se confirman en la FAQ — "Self-hosted containers run in your own VPC or on-prem hardware and require NVIDIA GPUs. It is available on Enterprise", "SOC 2 Type 1 and Type 2, HIPAA with a BAA for Enterprise, GDPR with an EU endpoint, CCPA, and PCI. FIPS 140-3 images are available for self-hosted deployments" y "Enterprise pricing ladders down with committed volume... Talk to sales if you are processing millions of minutes a month". Matiz relevante: esta captura **no contiene el hostname `api.eu.deepgram.com` ni el bloque de compliance con las tarjetas SOC 2 / HIPAA / GDPR / CCPA / PCI**, que sí estaban en las capturas del 11-01 y 11-02; la FAQ solo conserva la fórmula "GDPR with an EU endpoint". El dato del átomo no se refuta —está mejor documentado por las fuentes que ya cita—, pero el dominio exacto no es re-verificable con esta captura, un caso de [[2026-1103-deepgram-captura-11-03-rendering-reducido-y-sin-enlaces]].

## Actualización 2026-11-04
Quinta captura: el hostname **`api.eu.deepgram.com` queda re-verificado** y el bloque de compliance vuelve a renderizarse íntegro — "GDPR Ready & EU Data Residency ... We offer a dedicated EU endpoint to ensure data processing stays within the European Union (api.eu.deepgram.com)" — junto con las tarjetas SOC 2 Type 1 & Type 2 Certified, HIPAA Compliant, CCPA Compliant y PCI Compliant. La FAQ repite los datos de Enterprise sin variación (self-hosted con GPUs NVIDIA, FIPS 140-3, descuentos por volumen con model training y account team). La captura del 11-04 es byte a byte idéntica a la del 11-01, de modo que la ausencia del hostname el 11-03 queda atribuida a la variante de render y no a un cambio de la web — ver [[2026-1104-deepgram-bloque-de-compliance-solo-en-tres-de-cinco-capturas]] y [[2026-1104-deepgram-renderizado-completo-restaurado-identico-al-11-01]].
