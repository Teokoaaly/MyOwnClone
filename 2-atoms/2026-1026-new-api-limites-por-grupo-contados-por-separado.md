---
id: 2026-1026-new-api-limites-por-grupo-contados-por-separado
type: atom
certainty: solid
sources: [sources/2026-10-25-new-api-releases.md]
links: ["[[2026-1023-new-api-routing-por-grupo-prioridad-y-afinidad]]", "[[2026-1023-new-api-grupos-como-eje-de-precio-del-relay]]", "[[2026-1023-new-api-seguridad-env-vars-y-rate-limit-por-nodo]]"]
---

## Claim
**v1.0.0-rc.45** corrige el **conteo de límites de tasa**: antes, los límites de los **distintos grupos se sumaban entre sí**. Ahora, **un grupo que tiene su propio límite se cuenta aparte**: sus peticiones se miden contra su propio límite y no contra el del resto.

La misma versión añade que el aviso de **saldo bajo** salta **una vez** cuando el saldo baja del umbral fijado, y **vuelve a saltar la siguiente vez** que baja después de una recarga.

## Why It Matters
El **grupo deja de ser solo una etiqueta de asignación** (canal, key, precio) y pasa a ser **también una unidad de cuota**. Es un cambio de semántica que importa para un operador de reventa: un grupo puede ser **un plan de consumo** —por ejemplo, "grupo premium: 1.000 peticiones/día"— y no solo un segmento de precio.
Y es exactamente la integración entre los dos ejes que el vault tiene separados: routing por grupo/prioridad/peso/afinidad ([[2026-1023-new-api-routing-por-grupo-prioridad-y-afinidad]]) y el grupo como eje de precio ([[2026-1023-new-api-grupos-como-eje-de-precio-del-relay]]). rc.45 los **fusiona en una sola dimensión de producto**: el grupo es precio + cuota + permisos, y el límite ya no es global sino **por grupo**.
El detalle del aviso de saldo bajo (una vez por bajada, y se rearma tras recargar) importa para el vault porque es **política de comunicación de saldo**, que es el mecanismo central de otro sector que el vault estudia: los proveedores de números de verificación y de cuentas, donde el stock se repone y se avisa ([[2026-1023-priceai-channels-correo-y-jianma-a-centimos-como-insumo-de-alta]]). Y recorda el caso ya documentado de que **los límites cuentan por nodo** si no hay Redis compartido ([[2026-1023-new-api-seguridad-env-vars-y-rate-limit-por-nodo]]): con grupos, esa fragmentación se multiplica por el número de grupos.
