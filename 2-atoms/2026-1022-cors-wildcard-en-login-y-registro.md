---
id: 2026-1022-cors-wildcard-en-login-y-registro
type: atom
certainty: solid
sources: [raw/articles/myownclone-vulnerabilities-confirmed.md]
links: ["[[myownclone]]", "[[2026-1022-superficie-oculta-robots-txt]]", "[[2026-1022-admin-p2-fuga-codigo-panel-sin-auth]]", "[[2026-1022-sin-rate-limiting]]"]
---
## Claim
Las rutas `/login` y `/registro` de [[myownclone]] responden con `access-control-allow-origin: *` y `access-control-allow-methods: OPTIONS, GET, HEAD`, de modo que cualquier dominio puede leer esas páginas vía JavaScript cross-origin.

## Why It Matters
`access-control-allow-origin: *` en las dos páginas de acceso es el punto de entrada más sensible para un CORS abierto: un script de terceros puede leer el HTML de login y de registro desde el navegador de un visitante sin que la respuesta sea opaca. En un producto con beta cerrada y onboarding manual (ver [[2026-1022-superficie-oculta-robots-txt]], que confirma que las únicas rutas públicas reales son landing, login, signup, contacto y legales), estas dos páginas son literalmente la superficie pública completa del onboarding. Sumado a la fuga del payload admin en [[2026-1022-admin-p2-fuga-codigo-panel-sin-auth]], la lectura conjunta es que la política de CORS y la de autenticación están ambas definidas en el cliente en lugar de en el borde.
