---
id: 2026-1024-evoxt-despliegue-100-automatico-y-upgrade-con-un-boton
type: atom
certainty: solid
sources: [sources/2026-10-23-evoxt-vps-pricing.md]
links: ["[[2026-1024-evoxt-sla-99-99-y-despliegue-en-2-5-minutos]]", "[[2026-1024-evoxt-escalera-de-precios-nueve-planes]]", "[[2026-1024-evoxt-api-y-rescue-mode-para-gestion-de-vms]]"]
---

## Claim
El FAQ de Evoxt afirma que el servidor queda listo en **"Less than 5 minutes"** tras el pago, con *"Server deployment on Evoxt is 100% automatic"*, y que el escalado se hace *"by clicking on the upgrade button on your VPS control panel"*. La captura no dice cuánto tarda el upgrade ni qué ocurre con el disco y la IP al cambiar de plan.

## Why It Matters
Es la pieza operativa que permite **previsionar el coste de una subida de tier sin rehacer nada**: si el botón de upgrade actualiza el plan dentro de la escalera publicada ([[2026-1024-evoxt-escalera-de-precios-nueve-planes]]) en minutos, el paso de VM-1 ($5.99, 2 GB) a VM-2 ($11.99, 4 GB) es una decisión de coste de minutos, no una migración de afternoon. Eso importa porque el producto ya está en beta y su objetivo declarado es salir al mercado rápido ([[2026-1022-mvp-salir-al-mercado-pronto]]): un proveedor que permite escalar en un clic convierte el crecimiento de tenants en un ajuste mensual, sin ventana de mantenimiento.

## [FRICTION]
> [[2026-1024-evoxt-sla-99-99-y-despliegue-en-2-5-minutos]] afirma, citando la home del proveedor, que Evoxt declara **"listo para conectar y usar en 2.5 minutos"**.
> Este átomo presiona esa cifra porque la página de precios dice **"Less than 5 minutes"** para el mismo evento (despliegue tras el pago) — la misma operación con dos plazos declarados en dos páginas del mismo proveedor.
> Ambas no pueden ser simultáneamente verdaderas como descripciones del mismo evento: o la home redondea la promesa comercial y la página de precios da el plazo operativo real, o son dos métricas distintas (preparación frente a plenamente utilizable). Marcado para juicio humano, no auto-resuelto: la captura no define qué significa "ready" ni "less than 5 minutes".

## Nota de verificación
Ambas frases transcritas literalmente de dos páginas distintas de evoxt.com (la segunda del FAQ de esta captura). La captura **no** publica duración del upgrade, ventana de mantenimiento, ni política de rollback.
