---
id: 2026-1024-flokinet-sin-acceso-del-proveedor-a-los-datos
type: atom
certainty: solid
sources: [sources/2026-10-24-flokinet-vps-pricing.md]
links: ["[[2026-1024-flokinet-ram-ampliada-para-picos-pero-no-es-recurso]]", "[[2026-1024-buyvm-ddos-protegido-3-dolares-por-ip-y-cifrado-de-disco-completo]]", "[[2026-1024-flokinet-ubicaciones-offshore-ripe-e-isnic]]"]
---

## Claim
FlokiNET declara por escrito la **no retención de acceso a los datos del cliente**: *"You will be the only one who has full control over your server! We do not keep any kind of access or backdoor to monitor or access your data"* y, en la FAQ sobre root, *"We do not retain any ability to access your stored data through any tool for management or monitoring. We only monitor overall resource usage. Additionally, we do not share any information with any third parties regarding your traffic or patterns in any circumstance."* En paralelo, admite una **limitación técnica de cifrado**: el cifrado pre-boot no es aplicable al VPS porque, *"in theory, the pre-boot key can potentially be extracted from the virtual container while it is running"*, y recomienda en su lugar **cifrado de disco aplicado a particiones o carpetas**.

## Why It Matters
Es el único proveedor del vault que publica explícitamente el compromiso de **no compartir datos de tráfico con terceros** —un eje que hasta ahora solo aparecía implícito. BuyVM, el otro que ofrece FDE out of the box, lo hace con cifrado de disco completo vía KVM ([[2026-1024-buyvm-ddos-protegido-3-dolares-por-ip-y-cifrado-de-disco-completo]]); FlokiNET llega al mismo sitio por el caminho inverso, declarando que **no tiene acceso al dato** pero que **el cifrado pre-boot es inejecutable en un contenedor virtual**, y ofrece **cifrado por partición** como alternativa. La observación metodológica es reusable: **"el proveedor no puede leer tus datos" y "tus datos están cifrados" son dos promesas distintas**, y la segunda tiene aquí un límite técnico explícito. Para el vault esto pesa en el punto donde el nodo guarda conocimiento por tenant y sirve inferencia: la postura declarada es fuerte (offshore, sin retención, sin backdoor) pero el cifrado depende de que el cliente lo aplique, porque el proveedor no puede ofrecerlo a nivel de hypervisor.

## Nota de verificación
Son **declaraciones del proveedor, no garantías auditadas**: la captura no publica política de acceso de personal, cifrado en reposo de los snapshots, ni auditoría de terceros. La explicación del cifrado pre-boot es una explicación técnica ("in theory... in practice this is impractical with our security measures") **sin verificación externa**.
