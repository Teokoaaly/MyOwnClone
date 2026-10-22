---
id: 2026-1022-myownclone-jwt-token-required
type: atom
certainty: solid
sources: [raw/articles/myownclone-osint-implementation-plan-2026-06-24.md]
links: ["[[2026-1022-myclone-auth-jwt-account-type-creator]]", "[[2026-1022-gap-lead-capture-visitors]]", "[[2026-1022-ia-y-auth-totalmente-servidor]]"]
---
## Claim
La autenticación de [[myownclone]] es **JWT sobre Flask** (con NextAuth en el frontend), y el patrón obligatorio para cualquier endpoint nuevo es el decorator `@token_required`, siguiendo el `auth.py` que ya existe en `controllers/`. No hay API pública de datos autenticada: la superficie es server-side (ver [[2026-1022-ia-y-auth-totalmente-servidor]]).

## Why It Matters
Es la regla de implementación que condiciona todo el plan de replicación: los endpoints nuevos de versionado de prompt (`/prompts/history`, `/prompts/restore`, `/prompts/diff`), de visitantes (`/visitors`, `/analytics/visitors`) y de Stripe Connect deben ir decorados con `@token_required` y vivir en `controllers/console/myownclone/`.
El contraste con MyClone.is es estructural: allí el token es un JWT **autocontenido con PII en claro** y el login devuelve campos planos ([[2026-1022-myclone-auth-jwt-account-type-creator]]), mientras que el endpoint de captura de lead de MyClone.is es público y se autentica por `session_token` — el mismo `session_token` que el plan quiere usar para correlacionar `LeadCapture` ([[2026-1022-gap-lead-capture-visitors]]).

## [FRICTION]
> [[2026-1022-auth-flask-nextauth-desconectados]] afirma que en [[myownclone]] los dos sistemas de auth están **desconectados**: Flask usa decorators `@login_required`/`@account_initialization_required`/`@setup_required`, Next.js usa `auth()` de NextAuth, y la sesión de uno no gobierna al otro.
> Este átomo describe el patrón como "JWT vía Flask (NextAuth en frontend)" y señala `@token_required` como el decorator a usar, lo que sugiere una integración que el otro átomo niega.
> Ambas no pueden ser completamente correctas: o `@token_required` es un alias/alias-local de `@login_required` y ambos decoradores conviven sin que el JWT de NextAuth llegue a Flask, o la integración existe y la desconexión está acotada a rutas concretas. Marcado para juicio humano, no auto-resuelto.
