---
id: 2026-1023-hetzner-ipv4-primario-incluido-o-costo-cero
type: atom
certainty: tentative
sources: [sources/2026-10-22-hetzner-cloud.md, sources/2026-11-03-hetzner-cloud.md]
links: ["[[2026-1023-hetzner-cpx02-1-vcpu-5-99-al-mes]]", "[[2026-1023-hetzner-facturacion-por-hora-0-0096]]", "[[2026-1022-live-verify-superficie-dns-reducida-a-dos-hosts]]"]
---

## Claim
La calculadora de Hetzner Cloud ofrece un conmutador **IPv6 only / Primary IPv4** con un precio asociado que en la captura aparece como **€ 0.00**, es decir el IPv4 primario se muestra sin sobrecoste en la configuración por defecto. La lectura es tentativa: la captura intercala el conmutador y el importe de forma que no queda inequívoco si ese € 0.00 corresponde al IPv4 primario, al total estimado de la configuración, o a ambos.

## Why It Matters
El precio del IPv4 primario es una de las partidas que suele surprising en el precio final de un VPS y es directamente relevante para la infraestructura viva del vault: la superficie DNS medida en [[2026-1022-live-verify-superficie-dns-reducida-a-dos-hosts]] está en dos hosts con IP `212.227.169.99` (IPv4), de modo que la decisión "IPv6 only" no es gratuita para un producto que ya tiene un dominio público en IPv4. Si el IPv4 primario fuera de pago y no solo de configuración, entraría en el cálculo del presupuesto de infra que se está contrastando en [[2026-1023-hetzner-cpx02-1-vcpu-5-99-al-mes]] y [[2026-1023-hetzner-facturacion-por-hora-0-0096]].

## Nota de verificación
La captura no publica ningún precio explícito de "Primary IPv4" ni de "IPv6 only" por separado, ni el coste por TB cuando se elige solo IPv6. La cifra € 0.00 y el propio conmutador sí están transcritos literalmente.

## Nota de extensión 2026-11-03
Fuente: `sources/2026-10-31-hetzner-cloud.md`, `sources/2026-11-02-hetzner-cloud.md`. Ambas capturas repiten el mismo bloque de la calculadora: "IPv6 only / Primary IPv4" seguido de "**€ 0.00**", en la configuración por defecto de CPX02 1 VCPU AMD a € 5.99/mes. La lectura tentativa de este átomo **no se resuelve**: la ambigüedad de a qué partida corresponde ese € 0,00 persiste en las capturas nuevas, y el 2026-11-01 no renderiza la calculadora. Lo que sí queda confirmado es que **no aparece ningún sobrecoste visible por IPv4** en las dos capturas con widget, lo que mantiene la partida fuera del cálculo de presupuesto de ≤ €4/mes.

## 2026-11-03 — re-verificación
Fuente: `sources/2026-11-03-hetzner-cloud.md`. El bloque "IPv6 only / Primary IPv4" seguido de "**€ 0.00**" se repite en la calculadora de esta captura, dentro de la configuración por defecto de CPX02 1 VCPU AMD a € 5.99/mes. **La lectura tentativa de este átomo no se resuelve**: la captura sigue sin publicar un precio explícito separado para "Primary IPv4" ni para "IPv6 only", de modo que la ambigüedad de a qué partida corresponde ese € 0,00 persiste. Lo que queda confirmado es que **no aparece ningún sobrecoste visible por IPv4** en una cuarta captura con widget, lo que mantiene esa partida fuera del cálculo de ≤ €4/mes. Ver [[2026-1103-hetzner-cinco-capturas-estabilidad-catalogo-vs-widgets-dinamicos]].
