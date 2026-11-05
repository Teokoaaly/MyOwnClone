---
id: 2026-1024-noones-publicar-ofertas-y-visa-virtual-exigen-id
type: atom
certainty: solid
sources: [sources/2026-10-23-noones-limits-and-verification.md]
links: ["[[2026-1024-noones-escalera-de-verificacion-l1-l1plus-l2-l3]]", "[[2026-1024-noones-verificacion-basica-l1plus-revision-manual-hasta-72h]]", "[[2026-1024-noones-tabla-de-limites-por-nivel]]", "[[2026-1024-extravm-pago-cripto-sin-kyc-ni-identidad]]"]
---
## Claim
El bloque **"Warning:"** de la KB de límites fija tres puertas blanquiales sobre servicios concretos: *"In order to publish an offer, you need to be ID-verified or pass Basic Verification."*; *"Some services, such as create a virtual Visa card, will require you to complete ID verification."*; y *"The per-trade limit for a trade is calculated based on the total volume of all active trades available for your current level."* La tabla refuerza la primera: **Publish Offers = No en L1**, Yes en L1+, L2 y L3.

## Why It Matters
El proveedor separa explícitamente **funciones que se pueden automatizar** (recibir, depositar, convertir, operar en el marketplace desde L1) de **funciones que requieren identidad documentada** (publicar oferta = L1+ o ID; tarjeta Visa virtual = ID completo). Para una operación tipo phone farm que quiere **monetizar como proveedor del otro lado del P2P** —poner ofertas, no solo consumirlas— el punto de fricción es L1+/L2, no L1: se puede estar dentro de la plataforma, con $5K diarios y sin un solo ID, y aun así **no poder vender**. Y la Visa virtual es la pieza que un proveedor de servicios de identidad ([[2026-1024-extravm-pago-cripto-sin-kyc-ni-identidad]]) querría precisamente para emitir instrumentos de pago sin pasar por un KYC bancario: aquí está atada al ID. La tercera línea (límite por operación calculado sobre el **volumen total de todos los trades activos** del nivel) implica además que el techo por operación **no es un límite por operación**: es un límite compartido con lo que ya está abierto en el libro.


## Nota de extensión 2026-10-26
La captura de la API de desarrollador añade un dato que este átomo no podía tener: entre los cuatro bullets de cabecera de `dev.noones.com` está **"Automatically update offer margins"**, y otro es **"Trade on behalf of your clients"**. Es decir, el proveedor **invita explícitamente a un tercero a automatizar el lado vendedor** del marketplace —el lado que este átomo describe como atado a identidad documentada por usuario (Publish Offers = No en L1, Yes desde L1+; Visa virtual = ID completo).

Lo que la extensión deja **sin resolver**, y que conviene tener presente al releer este átomo: la captura **no publica los scopes delegables**, ni dice si la capacidad de publicar ofertas y la de emitir Visa virtual **heredan el nivel de verificación del usuario delegante** o si se concede a la app instalada, ni si esos permisos pueden compartirse entre usuarios de una misma app. La escalera L1→L3 ([[2026-1024-noones-escalera-de-verificacion-l1-l1plus-l2-l3]]) sigue siendo la descripción válida de lo que la plataforma **publica**; lo que la API añade es la figura de un actor que opera **en nombre de** varios usuarios verificados, y cuyo alcance no está documentado.

Ver también: [[2026-1026-noones-trade-en-nombre-de-tus-clientes-como-modelo-de-negocio]] y [[2026-1026-noones-acceso-delegado-app-instalada-por-el-usuario]].
