---
id: 2026-1023-new-api-stack-go-gin-react19-y-electron
type: atom
certainty: solid
sources: [sources/2026-10-22-new-api-github.md]
links: ["[[2026-1023-new-api-tokenkit-conteo-de-tokens-calibrado]]", "[[2026-1023-new-api-relaykit-conversion-perdida-de-campos]]", "[[2026-1022-myclone-stack-tecnologico]]"]
---

## Claim
El stack declarado por el README: **backend en Go y Gin**; **consola web en React 19, TypeScript, Rsbuild, TanStack y Tailwind CSS 4**, con **Bun** como gestor de dependencias y runner de scripts del frontend. El flujo de build es explícito: `bun install --frozen-lockfile` → `bun run build` dentro de `web/`, y el backend **embebe `web/dist`** (`go run .`). En desarrollo, el servidor de frontend corre en el puerto **5173** y hace proxy de las peticiones API al backend en el **3000**. Además existe un **wrapper de escritorio Electron** (`electron/`) y la tabla de responsabilidades separa `router/`, `middleware/`, `controller/` (rutas, control de acceso, handlers), `relay/` (adaptadores upstream y routing), `service/`, `model/` (lógica de negocio y persistencia), `relaykit/`, `plugins/tasks/` y `web/`.

## Why It Matters
Es el **coste de entrada técnico del software**: una sola aplicación Go que embebe el frontend, con un stack de frontend moderno pero mainstream (React + Tailwind), y un modo de desarrollo de dos procesos.
La comparación útil para el vault: mientras MyClone.is reparte su dominio entre Next.js en Vercel y un backend Python/Uvicorn en AWS ([[2026-1022-myclone-stack-tecnologico]]), New API es **un monolito Go con el front embebido** — menos superficie operativa, pero también menos flexibility: no hay separations entre "API de producto" y "API de inferencia" porque la segunda **es** el producto.
Y un dato de mercado: la existencia de `electron/` significa que el mismo gateway se puede empaquetar como app de escritorio, lo que lo acerca al producto de marca blanca que el vault evalúa para sus clones ([[2026-1022-myclone-custom-domains-whitelabel]]).
