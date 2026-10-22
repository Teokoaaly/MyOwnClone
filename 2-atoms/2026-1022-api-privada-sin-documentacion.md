---
id: 2026-1022-api-privada-sin-documentacion
type: atom
certainty: solid
sources: [raw/articles/myownclone-technical-research.md, raw/articles/myownclone-frontend-recon.md]
links: ["[[myownclone]]", "[[ai-clones]]", "[[2026-1022-mutaciones-rsc-sin-api-rest]]", "[[2026-1022-myclone-api-rest]]"]
---
## Claim
La API de [[myownclone]] es completamente privada: no existe docs.myownclone.com funcional (devolvía 404) ni ruta api.myownclone.com/public-api, y el producto no expone documentación pública de su API. El recon de bundles confirma el motivo: no hay API REST en absoluto — las mutaciones van por Next.js Server Actions (protocolo RSC) contra el mismo servidor Next.js, `api.myownclone.com` sirve el mismo HTML de la app, y no aparecen GraphQL, tRPC, WebSocket ni SSE en el cliente.

## Why It Matters
Cerrar la documentación de la API es una decisión de producto consistente con un modelo B2B de creators donde la superficie pública es el clon, no el developer platform. Distingue el negocio de [[myownclone]] de productos de clones como Coachvox o Cpycat listados en [[myownclone-competitors]]. El mecanismo (RSC, sin contrato de API) matiza y refuerza la tesis: no es que la API esté documentada en privado, es que no existe como API. Ver [[2026-1022-mutaciones-rsc-sin-api-rest]] y el contraste con [[2026-1022-myclone-api-rest]].

## [FRICTION]
> [[2026-1022-myclone-api-rest]] (escrita hace ~4 meses) afirma que [[myownclone]] "expone su API por OpenAPI en `myownclone/dify/api/openapi/`".
> Esta nota presiona eso porque el informe técnico no encuentra ni `docs.myownclone.com` funcional (404) ni `api.myownclone.com/public-api`, y califica la API de completamente privada.
> Ambas no pueden ser completamente correctas: o el checkout local de Dify en el vault no es la API pública del producto, o "documentada" no equivale a "públicamente accesible". Marcado para juicio humano, no auto-resuelto.
