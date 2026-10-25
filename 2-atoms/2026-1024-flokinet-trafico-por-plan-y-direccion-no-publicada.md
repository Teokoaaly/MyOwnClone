---
id: 2026-1024-flokinet-trafico-por-plan-y-direccion-no-publicada
type: atom
certainty: solid
sources: [sources/2026-10-24-flokinet-vps-pricing.md]
links: ["[[2026-1024-flokinet-escalera-de-precios-siete-planes]]", "[[2026-1024-skhron-trafico-contado-en-dos-sentidos]]", "[[2026-1023-hetzner-trafico-20-tb-inclusivos-y-1-euro-por-tb-extra]]", "[[2026-1024-buyvm-ancho-de-banda-unmetered-y-sin-cota-de-egreso-publicada]]"]
---

## Claim
Cada plan publica un **tráfico incluido explícito** junto al uplink: **3 TB** (VPS I, €7.99), **6 TB** (II, €14.99), **9 TB** (III, €27.99), **12 TB** (IV, €41.99), **15 TB** (V, €53.99), **18 TB** (VI, €61.99) y **20 TB** (VII, €73.90), todos con **1 Gbit Uplink**. La dirección del cómputo **no se declara**: la página dice "Traffic" sin especificar si es salida, entrada o suma de ambas, y añade que *"Each location and each package includes its own limits, please be sure to check the limits in the package and order more bandwidth/traffic on check-out if needed"*. El precio del tráfico adicional **no se publica**.

## Why It Matters
Aporta el dato más fino del vault sobre egreso normalizado: **el ratio TB-por-euro cae monótonamente** de 0,38 TB/€ (VPS I) a 0,27 TB/€ (VPS VII) — es decir, **el byte incluido se encarece conforme subes de plan**, al revés que en Hetzner (20 TB incluidos por €5,99, [[2026-1023-hetzner-trafico-20-tb-inclusivos-y-1-euro-por-tb-extra]]). Puesto en la misma tabla de "TB de salida equivalentes" del thread, FlokiNET queda **8,9 veces peor que Hetzner en su plan de entrada** y **12,3 veces peor en su plan alto**: el plan que iguala los 20 TB de Hetzner cuesta €73,90 en lugar de €5,99. Y el caso es peor aún por la ambigüedad: Skhron declara explícitamente que cuenta **entrada + salida** ([[2026-1024-skhron-trafico-contado-en-dos-sentidos]]), BuyVM no publica ninguna cifra ([[2026-1024-buyvm-ancho-de-banda-unmetered-y-sin-cota-de-egreso-publicada]]) y FlokiNET publica una cifra **sin dirección**, que es la forma más difícil de normalizar. Para un producto que sirve respuestas en streaming y además ingiere documentos, la conclusión es que FlokiNET **no es comparable en egreso sin revalidar la definición en el checkout**.

## Nota de verificación
Cifras transcritas literalmente. La captura **no** publica: si el tráfico es de salida, de entrada o bidireccional, el umbral de corte, el precio del tráfico extra, ni el precio de "more bandwidth/traffic" en el checkout. El cálculo TB/€ es del átomo.
