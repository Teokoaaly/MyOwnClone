---
id: 2026-1024-noones-tabla-de-limites-por-nivel
type: atom
certainty: solid
sources: [sources/2026-10-23-noones-limits-and-verification.md]
links: ["[[2026-1024-noones-escalera-de-verificacion-l1-l1plus-l2-l3]]", "[[2026-1023-5sim-sms-verificacion-como-coste-marginal-de-alta]]", "[[2026-1024-noones-nivel-2-sin-limites-diarios-y-100k-por-operacion]]", "[[2026-1023-5sim-numero-de-un-solo-uso-una-verificacion]]"]
---
## Claim
La KB "Limits and Verification" de NoOnes da dos tablas de límites por nivel (L1 = *Email, Name, DOB*; L1+ = *Basic\**; L2 = *ID*; L3 = *Address*). **Wallet limits**: Free wallet = Yes en los cuatro; Daily Limit = **$5K / ∞ / ∞ / ∞**; Lifetime Send-out Limit = **$20K / ∞ / ∞ / ∞**; Send-out Tx Limit = **$1K / ∞ / ∞ / ∞**; Lightning deposit Tx Limit = **$1K / $1K / $5K / $5K**; Lightning send-out Tx Limit = **$1k / $1k / $1k / $1k**. **P2P Trade limits**: Publish Offers = **No / Yes / Yes / Yes**; Daily Limit = **$5K / ∞ / $100K / 1 million**; Per trade limit = **$5K / ∞ / $100K / 1 million**; Lifetime Trade Limit = **$20K / ∞ / ∞ / ∞**. El pie recuerda que *"Basic verification is a manual review performed by our compliance team. It can take up to 72h."*

## Why It Matters
Los límites de NoOnes están **anclados a un dato de identidad por peldaño, no a un modelo de tarifa**: el mismo usuario con el mismo saldo ve un techo de $5K diarios en L1 y de 1 millón en L3. Para el phone farm esto convierte el KYC de una **puerta binaria** en una **variable de capacidad**: el operador decide cuántos "picos de $100K por operación" necesita tener cuentas en L2/L3, y el coste es la fricción de verificación, no el capital ([2026-1023-5sim-sms-verificacion-como-coste-marginal-de-alta]] compara el caso SMS, donde la verificación es marginal). Nota operativa: los límites de Lightning **no escalan con el nivel** (el send-out por tx se queda en $1k en los cuatro niveles), así que la vía rápida para mover volumen pequeño y rápido no mejora con la verificación ([2026-1023-5sim-numero-de-un-solo-uso-una-verificacion]]).
