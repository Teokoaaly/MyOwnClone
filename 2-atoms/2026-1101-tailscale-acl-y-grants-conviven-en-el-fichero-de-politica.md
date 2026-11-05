---
id: 2026-1101-tailscale-acl-y-grants-conviven-en-el-fichero-de-politica
type: atom
certainty: solid
sources: [sources/2026-11-01-tailscale-docs.md]
links: ["[[2026-1031-tailscale-docs]]", "[[2026-1022-myclone-access-control-por-persona]]", "[[2026-1022-myownclone-dos-repos-flask-nextjs]]"]
---

## Claim
La sección "Reference" del índice de Tailscale ofrece **dos sistemas de control de acceso distintos** sobre el mismo fichero de política: una página de **"Tailnet policy file syntax"**, una de **"ACL examples"** y otra de **"Grant examples"**, además de "Production best practices" y "Shared responsibility". Es decir, la documentación de Tailscale no trata ACL y grants como sinónimos: son dos primitivas de política con ejemplos separados, y ambos viven en un **único fichero de política del tailnet** (política central, no configuración por nodo).

## Why It Matters
El control de acceso por tenant que ya necesita MyOwnClone ([[2026-1022-myclone-access-control-por-persona]]) se decide hoy en Flask/Next.js con dos repos ([[2026-1022-myownclone-dos-repos-flask-nextjs]]); Tailscale propone una **capa de red por identidad** con una única política centralizada del tailnet, donde ACL (allow/deny por IP:puerto) y grants (extensión con identidad, grupos y usuario/grupo por recurso) conviven. La consecuencia de diseño es que el plano de autorización se divide en dos: identidad de red (Tailscale, por nodo) y autorización de negocio (la app, por tenant). Eso no exime a la app de mantener su propio control por tenant, pero sí permite que api ↔ worker ↔ db se hablen **sin abrir puertos y sin reglas por IP**, que es justo lo que [[2026-1031-tailscale-docs]] deja abierto. La captura no describe la sintaxis ni la semántica de ninguna de las dos primitivas: solo prueba que existen como páginas diferenciadas de la documentación.
