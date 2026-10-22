---
id: 2026-1022-myclone-access-control-por-persona
type: atom
certainty: solid
sources: [raw/articles/myclone-deep-api-osint-2026-06-24.md]
links: ["[[2026-1022-myclone-auth-jwt-account-type-creator]]", "[[2026-1022-myclone-competidor-arquitectura]]", "[[2026-1022-myclone-widget-embed-modos]]"]
---
## Claim
MyClone.is separa **identidad del clon** (un `username` público, no un UUID) de **control de acceso**: `GET /personas/username/{username}/check-access`, `POST .../request-access`, `POST .../verify-access`, `POST .../init-session` y `PATCH /personas/{persona_id}/access-control`. En paralelo gestiona visitantes por persona y por usuario (`GET,POST /personas/{persona_id}/visitors`, `GET,POST /users/me/visitors`) y dominios de email permitidos por creator (`/users/me/email-domains`, con verificación).

## Why It Matters
El clon se consume por **username + session token**, no por ID: eso es lo que permite que un widget embebido en cualquier web solo necesite el username del creator. El `access-control` por persona es la primitiva que luego activa monetización ([[2026-1022-myclone-stripe-connect-monetizacion]]) y workflows: se puede decidir quién entra y con qué objetivo.
Los `email-domains` con verificación son un mecanismo de **seguridad anti-abuso**: restringen a qué dominio puede registrarse un visitante, lo que evita que alguien se registre con el email de un creator y reclame su identidad. Es un detalle fino que [[myownclone]] no documenta y que una replicación de [[myownclone]] debería copiar (ver también [[2026-1022-myclone-competidor-arquitectura]]).
