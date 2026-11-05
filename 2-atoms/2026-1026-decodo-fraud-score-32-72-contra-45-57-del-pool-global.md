---
id: 2026-1026-decodo-fraud-score-32-72-contra-45-57-del-pool-global
type: atom
certainty: solid
sources: [sources/2026-10-25-decodo-residential-pricing.md]
links: ["[[2026-1024-brightdata-400m-de-ips-en-195-paises-con-targeting-gratis]]", "[[2026-1024-iproyal-pool-de-64m-sin-desglose-geografico]]", "[[2026-1023-hero-sms-ip-y-vpn-coincidentes-con-el-pais-del-numero]]"]
---

## Claim
El FAQ de Decodo publica un **número de calidad de IP con su fuente y su metodología**: el score de calidad se basa en la investigación de Proxyway 2024, que usó la base de datos **IPQualityScore** para comprobar **10 000 IPs de EE. UU. y 20 000 IPs de distintas ubicaciones**. El dato que la página destaca es el **fraud score**: "The average fraud score in the Global pool was **45.57**, with **Decodo's IP pool being abused the least – 32.72**".

## Why It Matters
Es la **primera métrica de calidad de pool con metodología auditable en todo el corpus de proxy del vault**. Hasta ahora, los tres proveedores medidos (DataImpulse, Bright Data, IPRoyal) publicaban **magnitudes de pool y promesas de bloqueo** —"the most defended IPs", "400M+ monthly IPs", "the most accurate residential proxies"— **sin una sola medición**; el único dato comparable era el desglose de IPs por país de DataImpulse, que mide cobertura, no calidad ([[2026-1024-brightdata-400m-de-ips-en-195-paises-con-targeting-gratis]], [[2026-1024-iproyal-pool-de-64m-sin-desglose-geografico]]).
El orden de magnitud es lo que importa: **32,72 frente a 45,57 es una diferencia de 12,85 puntos en el score de fraude**, es decir, **un 28 % menos abuso que la media del pool global**, medido por un tercero con una base de datos propia. Para un flujo que depende de que la IP no esté bloqueada, **esa es la variable que decide el coste real**: dos proxies al mismo $/GB con scores de fraude 32 y 45 no cuestan lo mismo por sesión, porque uno provoca más reintentos.
Y es también la clase de dato que el vault ha echado de menos en otros proveedores: la métrica que decide la calidad del proxy **no es el tamaño del pool** (115M+/125M+ contradictorios, ver [[2026-1026-decodo-pool-de-115m-en-el-cuerpo-y-125m-en-el-pie]]) sino su tasa de abuso. El matiz honesto: **la medición es de 2024**, no de la fecha de captura, y no publica el score por país ni por ASN.

## Nota de verificación
Cifras y metodología transcritas literalmente. La captura **no** publica: el desglose del score por país, el nombre de la versión de IPQualityScore, ni la fecha de corte de los 30 000 IPs analizados.
