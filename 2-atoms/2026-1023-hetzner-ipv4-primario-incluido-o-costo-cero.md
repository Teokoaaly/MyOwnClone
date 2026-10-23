---
id: 2026-1023-hetzner-ipv4-primario-incluido-o-costo-cero
type: atom
certainty: tentative
sources: [sources/2026-10-22-hetzner-cloud.md]
links: ["[[2026-1023-hetzner-cpx02-1-vcpu-5-99-al-mes]]", "[[2026-1023-hetzner-facturacion-por-hora-0-0096]]", "[[2026-1022-live-verify-superficie-dns-reducida-a-dos-hosts]]"]
---

## Claim
La calculadora de Hetzner Cloud ofrece un conmutador **IPv6 only / Primary IPv4** con un precio asociado que en la captura aparece como **€ 0.00**, es decir el IPv4 primario se muestra sin sobrecoste en la configuración por defecto. La lectura es tentativa: la captura intercala el conmutador y el importe de forma que no queda inequívoco si ese € 0.00 corresponde al IPv4 primario, al total estimado de la configuración, o a ambos.

## Why It Matters
El precio del IPv4 primario es una de las partidas que suele surprising en el precio final de un VPS y es directamente relevante para la infraestructura viva del vault: la superficie DNS medida en [[2026-1022-live-verify-superficie-dns-reducida-a-dos-hosts]] está en dos hosts con IP `212.227.169.99` (IPv4), de modo que la decisión "IPv6 only" no es gratuita para un producto que ya tiene un dominio público en IPv4. Si el IPv4 primario fuera de pago y no solo de configuración, entraría en el cálculo del presupuesto de infra que se está contrastando en [[2026-1023-hetzner-cpx02-1-vcpu-5-99-al-mes]] y [[2026-1023-hetzner-facturacion-por-hora-0-0096]].

## Nota de verificación
La captura no publica ningún precio explícito de "Primary IPv4" ni de "IPv6 only" por separado, ni el coste por TB cuando se elige solo IPv6. La cifra € 0.00 y el propio conmutador sí están transcritos literalmente.
