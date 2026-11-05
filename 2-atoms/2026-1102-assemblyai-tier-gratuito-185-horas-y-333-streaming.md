---
id: 2026-1102-assemblyai-tier-gratuito-185-horas-y-333-streaming
type: atom
certainty: solid
sources: [sources/2026-11-02-assemblyai-pricing.md]
links: ["[[2026-1101-assemblyai-tarifas-por-hora-no-por-minuto]]", "[[2026-1022-myclone-limites-plan-free]]", "[[2026-1022-costes-por-categoria-tenant]]"]
---

## Claim
El tier gratuito de AssemblyAI cubre **hasta 185 horas de transcripción pre-recorded y hasta 333 horas de streaming**, sin tarjeta de crédito: "You can create an account and start transcribing immediately with no credit card required. The free tier includes up to 185 hours of pre-recorded transcription and up to 333 hours of streaming transcription."

## Why It Matters
Es una línea de coste con dos efectos opuestos para el vault. A favor: permite prototipar y validar el módulo de voz del clon **sin gastar ni un céntimo** — 185 horas de pre-recorded equivalen a $27,75 de Universal-2 o $38,85 de Universal-3.5 Pro si se pagaran, es decir el tier gratuito cubre el equivalente a varios meses de un único tenant antes de la primera factura. En contra, para el modelo multi-tenant el tier gratuito es **por cuenta, no por tenant**: no se reparte, y un solo usuario abusivo consume las 333 horas de streaming del grupo entero. Y en el corte de costes del vault ([[2026-1022-costes-por-categoria-tenant]]) esto es una partida de plataforma que no aparece en ninguna de las tres categorías documentadas, igual que el hosting — otra línea de coste fijo que la estructura de `categoryPlatformOps` tendría que cubrir. La comparación con el límite del producto competidor ([[2026-1022-myclone-limites-plan-free]]) es la que importa: 10 minutos de voz al mes contra 185 horas de transcripción.
