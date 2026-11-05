---
id: 2026-1104-azure-architecture-center-el-render-delgado-omite-get-started-seguridad-y-frameworks
type: atom
certainty: solid
sources: [sources/2026-11-04-azure-architecture-center.md]
links: ["[[2026-1104-azure-architecture-center-cuarta-captura-identica-a-la-del-11-02]]", "[[2026-1104-azure-architecture-center-la-captura-renderiza-urls-relativas-y-no-absolutas]]", "[[2026-1101-azure-architecture-center-hub-spoke-y-dmz-para-hibrido-seguro]]"]
---

## Claim
El modo de render "cuerpo limpio" que produce la captura del **2026-11-04** (idéntica al 11-02) **omite exactamente tres bloques** que sí estaban en la captura completa del 2026-11-01: la sección **"Get started"** con sus 4 puntos de entrada, el área **"Secure and connect workloads"** (sexta de seis) y la sección **"Frameworks and reference"** con sus cuatro enlaces (Cloud Adoption Framework, Well-Architected Framework, Azure migration guidance, "What's new in the Architecture Center"). El resultado es un catálogo de **5 áreas, 15 enlaces y ninguna entrada de navegación** (`browse/`, `guide/`, `icons/`, `changelog`, `technology-choices-overview` tampoco aparecen).

## Why It Matters
Convierte la ausencia de secciones en una **fricción de render con un patrón fijo**, no en un hueco del sitio: la captura del 11-04 vuelve a perder exactamente el mismo material que perdió la del 11-02, en los mismos bloques. La consecuencia práctica para el vault es doble. (a) **Regla de citación**: cualquier claim sobre el área de seguridad (hub-and-spoke, DMZ segura — ver [[2026-1101-azure-architecture-center-hub-spoke-y-dmz-para-hibrido-seguro]]) o sobre los 4 puntos de entrada solo es citable desde la captura del **11-01**, porque el 11-04 no lo renderiza; no debe atribuirse al 11-04 ni inferirse de su ausencia. (b) **Regla de pipeline**: si en la próxima captura el slug vuelve a salir en modo completo, el contraste 11-01 ↔ 11-02/11-04 seguirá siendo el que permita fechar la última versión del catálogo; y si sale en modo delgado, se confirms que el render delgado es el estado estable del slug en esta ventana, no un fallo transitorio — tal como ya se vio con el precedente de Tailscale en el vault ([[2026-1104-tailscale-quinta-captura-byte-identica-a-la-del-11-02]]).

## Nota de verificación
Comparación de cabeceras y enlaces: `sources/2026-11-01-azure-architecture-center.md` contiene "## Get started", 6 bloques de área de diseño (incluida "Secure and connect workloads" con `security/security-get-started`, `networking/architecture/hub-spoke`, `reference-architectures/dmz/secure-vnet-dmz`) y "## Frameworks and reference"; `sources/2026-11-04-azure-architecture-center.md` contiene únicamente "## Design areas" con 5 bloques y 15 enlaces de contenido, y ninguna de las 3 URLs de seguridad. Diferencia estructural ya registrada en [[2026-1104-azure-architecture-center-la-captura-renderiza-urls-relativas-y-no-absolutas]].
