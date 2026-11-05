---
id: 2026-1031-r2-infrequent-access-cuesta-al-recuperar
type: atom
certainty: solid
sources: [sources/2026-10-31-cloudflare-r2-storage.md]
links: ["[[2026-1031-cloudflare-r2-storage]]", "[[2026-1031-r2-clases-de-operacion-a-y-b]]", "[[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]"]
---

## Claim
La capa Infrequent Access de Cloudflare R2 cobra $0.01 por GB-month de almacenamiento (frente a $0.015 de Standard), pero sus operaciones son más caras: Class A a $9.00 por millón, Class B a $0.90 por millón, y añade Data Retrieval a $0.01 por GB; no tiene nivel gratuito (Free: —) en ninguno de sus componentes.

## Why It Matters
La capa barata se paga a la entrada y al salir: un objeto de 100 GB en Infrequent Access cuesta $1,00/mes de almacenamiento pero $1,00 cada vez que se recupera, con el doble de precio por operación que Standard. Para MyOwnClone esto aplica a lo que se escribe mucho y se lee poco — artefactos de clones, backups de conversation history, datasets de entrenamiento de los clones — que es justo el perfil de uso de [[2026-1031-cloudflare-r2-storage]] pero en la dirección contraria a su modelo "coste = GB × $0.015 sin importar cuántas veces leas". El punto de equilibrio aritmético es claro: frente a Standard, la capa IA ahorra $0.005/GB-month pero cobra $0.01/GB en cada recuperación, de modo que una única lectura de un objeto ya compensa el ahorro solo si el objeto lleva más de 2 meses almacenado. En la práctica, para MyOwnClone la capa Standard es la opción por defecto y la Infrequent Access solo aplica a backups que nadie toca; conviene además tener en cuenta que cada escritura en IA cuesta el doble que en Standard en clase A ([[2026-1031-r2-clases-de-operacion-a-y-b]]), lo que penaliza exactamente el caso de uso de "escribir mucho, leer poco". Con el presupuesto duro de ≤ €4/mes ([[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]) la diferencia total en magnitudes pequeñas es de céntimos, así que la decisión debe tomarse por el patrón de acceso, no por el ahorro absoluto.
