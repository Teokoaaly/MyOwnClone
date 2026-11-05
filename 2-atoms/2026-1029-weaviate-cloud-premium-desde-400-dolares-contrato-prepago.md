---
id: 2026-1029-weaviate-cloud-premium-desde-400-dolares-contrato-prepago
type: atom
certainty: solid
sources: [sources/2026-10-29-weaviate-cloud-pricing.md]
links: ["[[2026-1029-weaviate-cloud-flex-minimo-45-dolares-al-mes]]", "[[2026-1029-weaviate-cloud-free-tier-100000-objetos-1gb-memoria]]", "[[2026-1022-costes-por-categoria-tenant]]"]
---
## Claim
El plan **Premium** de Weaviate Cloud es de **contrato prepago** y la FAQ fija su mínimo en **"from $400/month on Premium"** (frente a los $45/mes de Flex). La tabla de comparación **distingue dos columnas Premium, Shared y Dedicated**, y las diferencias son materiales:

| Rasgo | Premium **Shared** | Premium **Dedicated** |
| --- | --- | --- |
| SLA de disponibilidad | 99,9 % | 99,95 % |
| Respuesta Sev 1 | 4 horas | 1 hora |
| Upgrades de cluster | Weaviate-managed | **Customer-directed** |
| Regiones | Limitadas (7) | **Todas (~40)** |
| Clouds | GCP, AWS | GCP, AWS, **Azure** |
| SSO / SAML | ✓ | ✓ |
| HIPAA, PrivateLink (AWS), volúmenes cifrados con claves del cliente | × | ✓ |
| Endpoint de métricas | ✓ | ✓ |
| Phone y Slack support | ✓ | ✓ |
| Technical Account Team | add-on | add-on |
| Backup retention | 30 días | 45 días |

Tarifas de lista Premium: **dimensiones desde $0.003875/1M (shared) y $0.002718/1M (dedicado)**, **storage desde $0.10/GiB (shared) y $0.33/GiB (dedicado)**, **backup desde $0.021/GiB (shared) y $0.014/GiB (dedicado)**. El mínimo que figura en la tabla para ambas columnas es **"Contact sales for more information"**; la cifra de **$400/mes** viene de la FAQ. Dos features aparecen como **Coming soon** en Premium Dedicated: **"Bring your own IdP"** y **Embeddings**.

## Why It Matters
Es la línea de coste que el vault puede descartar de entrada y dejar documentada como techo: **$400/mes ≈ €363,64/mes** al cambio de referencia de ~1,10 USD/EUR, es decir **~90× el presupuesto de ≤ €4/mes** de infraestructura ([[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]). Pero el valor de la cifra no es solo el precio: **Premium es la única variante que convierte el vector store en una partida de coste de plataforma con SLA de 99,95 %**, y por tanto en la única que podría commensurarse con el corte de costes por categoría del panel de administración, donde las categorías `categoryCloneResponses` y `categoryIngestion` son facturables al tenant y `categoryPlatformOps` las paga la plataforma ([[2026-1022-costes-por-categoria-tenant]]). El Premium no cabe en esa caja: es una **tercera línea de coste fijo de plataforma** que no aparece en ninguna de las dos categorías documentadas.

La tabla premia justo lo que el vault intenta evitar: **el control operativo real (upgrades dirigidos por el cliente, Bring-your-own-IdP, cifrado con claves del cliente) solo existe en la variante dedicada**, es decir, se paga en el extremo más caro, y aun así **dos de esas features no están disponibles en 2026** ("Coming soon"). Para un stack autoalojado la conclusión práctica es que **Premium Shared se parece al self-hosted en control (upgrades gestionados por el proveedor) y es la más barata de las dos**, mientras que Dedicated es la única con SLA de 99,95 % — un 0,05 % que no se paga solo.

## Nota de verificación
La conversión a euros (≈ €363,64) y el multiplicador "~90× el techo de €4" son **cálculo de este átomo** a ~1,10 USD/EUR; la fuente publica solo en dólares. La distinción Shared/Dedicated en todas las cifras procede de las **columnas separadas de la tabla "Compare Database plans"**, no de una simplificación "Premium = una sola cosa".
