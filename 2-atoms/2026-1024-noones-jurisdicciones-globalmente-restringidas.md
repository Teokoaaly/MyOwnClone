---
id: 2026-1024-noones-jurisdicciones-globalmente-restringidas
type: atom
certainty: solid
sources: [sources/2026-10-23-noones-blocked-jurisdictions.md]
links: ["[[2026-1024-noones-bloquea-ip-estadounidense-con-mensaje-explicito]]", "[[2026-1024-noones-mica-30-paises-no-servidos-desde-julio-2026]]", "[[2026-1024-noones-catalogo-de-paises-soportados-y-150-mas]]", "[[2026-1023-hero-sms-ip-y-vpn-coincidentes-con-el-pais-del-numero]]"]
---
## Claim
La KB "Blocked Jurisdictions and Restricted Regions" abre con la sección **"1. Globally Restricted Jurisdictions"**: *"Due to regulatory restrictions, we do not offer services or support onboarding for residents of the following countries and territories."* La lista de **9 países** es: Cuba, Iran, Myanmar (Burma), North Korea, Panama, Russian Federation, Syria, UAE, USA. Y la lista de **4 territorios de EE.UU.** es: Commonwealth of the Northern Mariana Islands, Guam, Puerto Rico, U.S. Virgin Island. El artículo no da ninguna razón distinta para cada país: la justificación es genérica ("regulatory restrictions") y la lista no distingue sanciones, AML o riesgo de fraude.

## Why It Matters
Dos lecturas que el vault necesita. (1) **El bloqueo es por residencia, no por nacionalidad ni por IP de salida**: el texto dice "residents of", y es coherente con la página de bloqueo por IP de la home ([[2026-1024-noones-bloquea-ip-estadounidense-con-mensaje-explicito]]). Eso significa que la IP abre la puerta y la residencia la cierra: un nodo en Nigeria ([[2026-1024-noones-catalogo-de-paises-soportados-y-150-mas]]) y una identidad residente en un país bloqueado son dos variables distintas, y la segunda es la que no se puede resolver con una VPN. (2) **Panama y UAE están bloqueados**, lo que es contraintuitivo: NoOnes es un exchange cripto con on-ramp/off-ramp en emergentes y precisamente dos de sus centros de referencia (Panama y los hubs de cripto de Oriente Medio, UAE) quedan fuera. Para un phone farm esto significa que el conjunto de jurisdicciones utilizables **no es "países no occidentales"** sino un recorte más estrecho: excluye a USA, a los cuatro territorios de EE.UU. listados y a dos centros de liquidez cripto. La consecuencia operativa para el vault es que **el pool de IPs del farm no puede elegir cualquier país emergente**: tiene que evitar los 9+4 bloqueados además de los 30 de MiCA.
