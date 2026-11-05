---
id: 2026-1103-auth0-log-streaming-a-siem-incluido-en-essentials
type: atom
certainty: solid
sources: [sources/2026-11-03-auth0-pricing.md]
links: ["[[2026-1101-auth0-b2c-essentials-escala-por-mau]]", "[[2026-1031-workos-audit-logs-125-por-siem-y-99-por-millon-de-eventos]]", "[[2026-1101-auth0-numero-de-tenants-por-plan]]", "[[2026-1022-costes-por-categoria-tenant]]"]
---

## Claim
El plan **Essentials de Auth0 ($35/mes)** incluye, sin add-on ni coste adicional publicado, "**Stream Auth0 Audit Logs to Datadog, Splunk, AWS, Azure, etc.**" — es decir, el streaming de logs de auditoría a destinos SIEM/nube viene de serie en el plan de entrada de pago.

## Why It Matters
Es el reverso exacto del modelo de WorkOS, que documenta el vault: allí el streaming de logs a un SIEM es un add-on de **$125/mes por conexión** y la retención de eventos cuesta $99/mes por millón ([[2026-1031-workos-audit-logs-125-por-siem-y-99-por-millon-de-eventos]]). En Auth0 el mismo entregable —auditoría que llega al SIEM del cliente— entra en el precio de $35/mes. Operativamente esto significa que **la partida "auditoría por tenant" del modelo de costes de MyOwnClone ([[2026-1022-costes-por-categoria-tenant]]) no necesita una línea separada si se usa Auth0**: es un feature del plan base, no un consumo variable por tenant. Contraste importante para el founder: la captura de la derecha no es gratuita en WorkOS y aquí sí lo es, lo que invierte la comparación de coste en el caso del cliente corporativo que exige logs en su Splunk. Lo que la página **no** publica es el precio del almacenamiento de los logs (solo el streaming), que es justo la línea de consumo acumulativo que sí se cobra en WorkOS.

## Nota de verificación
El bullet "Stream Auth0 Audit Logs to Datadog, Splunk, AWS, Azure, etc." y el precio de $35/mes del plan Essentials son lectura literal de `sources/2026-11-03-auth0-pricing.md`. La comparación con WorkOS y con el modelo de costes del vault es lectura de este átomo, no frase de la fuente.
