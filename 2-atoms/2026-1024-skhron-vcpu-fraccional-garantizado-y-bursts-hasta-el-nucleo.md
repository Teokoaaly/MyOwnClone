---
id: 2026-1024-skhron-vcpu-fraccional-garantizado-y-bursts-hasta-el-nucleo
type: atom
certainty: solid
sources: [sources/2026-10-23-skhron-bitcoin-vps.md]
links: ["[[2026-1024-skhron-precios-2-34-a-177-65]]", "[[2026-1023-hetzner-compartido-vs-dedicado-criterio-de-uso]]", "[[2026-1023-hetzner-cpx02-1-vcpu-5-99-al-mes]]"]
---

## Claim
Skhron expresa el CPU como **fracción garantizada con burst al núcleo completo**: por ejemplo XSIG-SE-0 declara "CPU Cores 1 (shared) / **0.06 vCPU** is guaranteed, bursts up to 1 vCPU according to FUP"; XSIG-SE-1, 0.13 vCPU garantizados bursting a 1; XSIG-SE-2, 0.25 a 1; XSIG-PL-2, 0.63 a 2; XSIG-SE-4, 0.5 a 2; XSIG-SE-8, 1 a 4; XSIG-PL-8, 2 a 8. La FAQ afirma **"NO [no hacemos oversell]**: "We plan node capacity so your server stays responsive and CPU steal approaches zero in practice. Fair-use limits are only there to curb the rare guest that abuses shared capacity, not to throttle normal use."

## Why It Matters
Es la diferencia de fondo entre "VPS barato" y "VPS utilizable": **0.06 vCPU garantizados con burst a 1** significa que el plan de €2.34 solo rinde 1 vCPU en picos y 0.06 vCPU sostenidos. El burst no es una garantía de rendimiento, es un techo. La página de Hetzner define el compartido como "desarrollo y pruebas" y el dedicado como "carga de producción alta" ([[2026-1023-hetzner-compartido-vs-dedicado-criterio-de-uso]]); Skhron aplica un criterio aún más estricto en su extremo barato, con un plan cuyo CPU garantizado es 1/16 de un núcleo. Para un relay de inferencia de clones ([[2026-1023-priceai-sponsors-vps-chinos-para-auto-hospedar-relay]]) el argumento "no hay oversell" es una afirmación de marketing: lo verificable es la fracción garantizada, y esa es baja.
