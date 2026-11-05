---
id: 2026-1027-proton-business-vpn-netshield-filtra-en-dns-y-declara-hipaa-ccpa-y-gdpr
type: atom
certainty: solid
sources: [sources/2026-10-26-proton-business-vpn-overview.md, sources/2026-10-26-proton-business-vpn-pricing.md]
links: ["[[2026-1027-proton-business-vpn-essentials-minimo-2-usuarios-con-2fa-organizacion-y-kill-switch]]", "[[2026-1023-hetzner-sla-99-9-gdpr-e-iso-27001]]", "[[2026-1024-1984-hosting-certificacion-iso-27001]]"]
---

## Claim
La página de producto B2B describe NetShield con un detalle técnico ausente en las páginas de consumo: **"Proton NetShield blocks malware, phishing, scams, and ads at the DNS level on every connection, out of the box."** Y abre con un bloque **"Supports your compliance standards"**: "Proton VPN built with **HIPAA, CCPA, and GDPR** regulations in mind." La tabla de precios B2B lo reformula como una fila de capacidad incluida en las cuatro columnas: **"Easy data protection compliance, including GDPR and HIPAA"**.

## Why It Matters
El nivel de la intervención es lo que aporta: **filtrado en DNS, no en el túnel**, es decir que el bloqueo ocurre **antes y fuera de la conexión VPN**, y por tanto **no protege el tráfico que no va por el cliente**. Eso la convierte en una función comparable a la del proxy en la §7 del thread (bloqueo de DNS como servicio de la capa de acceso), no en una función de cifrado. Y la lista de cumplimiento es un **claim de "built with in mind"**: no hay certificación nombrada, ni auditor, ni fecha —el contraste es directo con Hetzner, que sí publica ISO/IEC 27001, BSI C5 y un SLA con créditos ([[2026-1023-hetzner-sla-99-9-gdpr-e-iso-27001]]), y con 1984 Hosting, que publica su ISO 27001 ([[2026-1024-1984-hosting-certificacion-iso-27001]]). **"GDPR" como claim de página no es un cumplimiento auditable**, y el vault ya lo tiene registrado como tal en el otro lado del corpus.
