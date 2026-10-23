---
id: 2026-1023-hetzner-compartido-vs-dedicado-criterio-de-uso
type: atom
certainty: solid
sources: [sources/2026-10-22-hetzner-cloud.md]
links: ["[[2026-1023-hetzner-escalera-de-precios-y-salto-a-dedicados]]", "[[2026-1023-hetzner-cpx02-1-vcpu-5-99-al-mes]]", "[[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]"]
---

## Claim
La propia página define el criterio de elección entre las dos familias de recursos: los **planos compartidos** (Cost-Optimized y Regular Performance) están pensados para **desarrollo y pruebas**, con patrones de uso variables en lugar de carga sostenida — casos típicos: sitios personales y blogs, bases de datos pequeñas, servidores web de tráfico bajo o moderado — y el hardware se comparte con "vecinos". Los **servidores dedicados** asignan vCPU dedicadas al proyecto, con rendimiento no compartido y recursos altamente predecibles, para **aplicaciones de negocio con carga de producción alta**: sitios de alto tráfico, bases de datos grandes, servidores de juegos, machine learning o procesamiento de grandes volúmenes de datos.

## Why It Matters
La página no vende "más GHz" sino **previsibilidad**: el argumento comercial del dedicado es que el rendimiento no se degrada por vecinos, no que sea más rápido en el pico puntual. Eso importa para la decisión de infraestructura ya documentada en el vault: el despliegue vivo es un nginx autoalojado ([[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]) cuyo tráfico real se desconoce, de modo que la elección entre el escalón de €5.99 y el de €6.49 —o el salto a €43.49 ([[2026-1023-hetzner-escalera-de-precios-y-salto-a-dedicados]])— depende de si ese servidor sostiene carga sostenida o solo carga variable de beta. Con un producto en beta y un cliente de referencia que consume 3.000+ conversaciones al mes, el criterio compartido es defendible; con tenants de producción, la pregunta deja de ser el precio y pasa a ser la previsibilidad.
