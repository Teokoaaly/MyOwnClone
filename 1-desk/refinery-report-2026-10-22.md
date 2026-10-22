# Refinery Report — 2026-10-22

Run: 03:00 shift (scheduled cron).

## Captures processed

`0-raw/` contained **no captures** — only `reading-list.md` (excluded by house rules) and an empty `archive/`. The Scout run at 23:00 fetched 0 URLs because the reading list has had zero active URLs since 2026-06-16.

**Backlog source used instead:** `raw/articles/` — 10 OSINT/research documents (~135 KB) that the weekly audits have flagged for 7 consecutive weeks as never atomized. The Prime Directive permits any real vault artifact as a source, and these files are the vault's own capture layer. All 10 were processed.

## Totals

| Metric | Count |
|---|---|
| Captures processed | 10 |
| Atoms created | 107 |
| Atoms extended | 38 (existing atoms patched with new source refs + nuance) |
| Atoms retired to `2-atoms/archive/` | 3 (2 duplicates + the `TEMPLATE_TASTE.md` scaffold) |
| Friction blocks | 31 across 30 atoms |
| Broken wikilinks | 0 |
| Unresolvable source paths | 0 |
| Credentials leaked into notes | 0 (verified by grep) |
| Threads created | 2 |

## Atoms by source

| Source file | Atoms citing it |
|---|---|
| `raw/articles/myclone-deep-api-osint-2026-06-24.md` | 25 |
| `raw/articles/myownclone-frontend-recon.md` | 22 |
| `raw/articles/myownclone-osint-implementation-plan-2026-06-24.md` | 20 |
| `raw/articles/myownclone-osint-implementation-handoff-2026-06-24.md` | 18 |
| `raw/articles/myownclone-founder-transcript.md` | 17 |
| `raw/articles/myownclone-new-findings-may-2026.md` | 15 |
| `raw/articles/myownclone-scrape_web-scrape.md` | 14 |
| `raw/articles/myownclone-technical-deep-dive-2026-06-23.md` | 10 |
| `raw/articles/myownclone-vulnerabilities-confirmed.md` | 10 |
| `raw/articles/myownclone-technical-research.md` | 10 |

## Certainty distribution

- `solid` — 81 atoms. Facts directly observed: endpoint counts, HTTP status codes, response headers, framework versions, and our own repo's code.
- `tentative` — 27 atoms. Inferences, JS-bundle-derived routes, founder statements, and implementation plans.

The line was enforced, not blurred: routes the June deep-dive explicitly labels "inferred from JS" are `tentative`; the 227-endpoint surface confirmed by the OpenAPI spec is `solid`.

## Frictions raised (31) — for the Editor

Highest-signal set; the full list is in the `[FRICTION]` blocks of the 30 atoms that carry them.

**Product / market**
1. `solo-personify-compite-de-verdad` ↔ `comparisons/myownclone-competitors.md` — the competitor map says only Personify competes directly and never mentions MyClone.is.
2. `myclone-verticalizacion-y-transparencia` ↔ `comparisons/myownclone-competitors.md` — MyClone.is is a direct rival with a more modern stack than the map records.
3. `guardarrail-no-alucinar` ↔ `comparisons/myownclone-vs-delfi.md` — the transcript does not support the legacy claim that Delfi hallucinates.
4. `myclone-carece-modos-memories-ni-visitors` ↔ itself — the handoff claims MyClone.is lacks visitor tracking, but its own endpoint list includes `/visitors` and `capture-lead`.
5. `plan-orden-implementacion-myownclone` ↔ `mvp-salir-al-mercado-pronto` — founder says MVP first; internal handoff marks prompt versioning 🔴 ALTA and first.

**Onboarding / GTM**
6. `onboarding-manual-sin-self-service` ↔ `beta-activo-trafico-real` — `/registro` redirects to `/contacto`, yet the tenant panel shows signups and MRR.
7. `onboarding-cuatro-pasos-encuestas` ↔ `onboarding-manual-sin-self-service` — a full 4-step funnel exists in code, but public access is closed.
8. `auth-magic-link-codigo-seis-digitos` ↔ `onboarding-manual-sin-self-service` — self-service auth machinery vs. manual onboarding.
9. `gap-lead-capture-visitors` ↔ `instancia-como-captador-de-leads` — the founder describes the clone as a lead gate; the code has no capture at all.
10. `gap-lead-capture-visitors` ↔ `myclone-vs-myownclone-gaps-api` — replicable ≠ implemented.

**Security / hardening**
11. `admin-p2-fuga-codigo-panel-sin-auth` ↔ `admin-rutas-bilingues-sin-subdominio` — 307 `NEXT_REDIRECT` vs HTTP 200 with the full RSC payload downloaded. **Requires re-verification with curl; two observations on different dates.**
12. `admin-p2-fuga-codigo-panel-sin-auth` ↔ `dns-superficie-publica-myownclone` — one says 200 with auth, the other says admin HTML without a session.
13. `ausencia-csp-xss-sin-mitigacion` ↔ `entities/myownclone.md` — the entity claims "complete isolation"; curl shows no CSP, no security headers, no rate limiting.
14. `sentry-dsn-publico-contamina-dashboards` ↔ `frontend-nextjs-vercel-sentry-posthog` — release hash differs between two reports for the same date.
15. `admin-bandeja-global-y-spam` ↔ `email-inbound-contacto-sin-dominio-propio` — wildcard `*@` implemented vs. a single `contacto@` box publicly.
16. `modulo-brain-cerebro-memorias-plantillas` ↔ `email-inbound-contacto-sin-dominio-propio` — inbound domain implemented vs. "Coming soon".

**Tech / architecture**
17. `auth-flask-nextauth-desconectados` ↔ `myownclone-jwt-token-required` — `@token_required` decorator vs. the actual Flask decorators.
18. `pgvector-embeddings-openai-inferidos` ↔ `ia-y-auth-totalmente-servidor` — Anthropic/OpenAI strings present vs. "no bundle contains them".
19. `mapa-modulos-internos-desde-bundles-js` ↔ `ia-y-auth-totalmente-servidor` — full internal naming visible in the bundle vs. total opacity.
20. `gap-workflows-myownclone` ↔ `plan-workflows-nuestro` — this plan puts workflows in phase 2; the handoff puts them last.
21. `plan-replicacion-myclone-fases-prioridad` ↔ `myclone-vs-myownclone-gaps-api` — 7 gaps in the plan vs. 8 in the OSINT report.
22. `myownclone-dos-repos-flask-nextjs` ↔ `entities/myownclone.md` — the entity lists a one-line stack with no Flask/SQLAlchemy backend.
23. `myclone-api-rest` ↔ `myclone-api-superficie-227-endpoints` — spec-documented surface vs. "inferred from bundles".
24. `myclone-chat-streaming-sse` ↔ `myclone-widget-comunicacion-websocket` — text over SSE vs. Socket.IO.
25. `myclone-vs-myownclone-gaps-api` ↔ `myclone-verticalizacion-y-transparencia` — 7 "missing" capabilities are partly already covered by the API.
26. `myclone-auth-jwt-account-type-creator` ↔ `myclone-api-rest` — the `{data, error}` wrapper doesn't appear in login; JWT carries PII in clear.
27. `api-privada-sin-documentacion` ↔ `myclone-api-rest` — our API exposed via OpenAPI vs. completely private.
28. `beta-activo-trafico-real` ↔ `entities/myownclone.md` — closed beta without self-service vs. `/registro` as a public route.
29. `frontend-nextjs-vercel-sentry-posthog` ↔ `entities/myownclone.md` — the entity says "Next.js 14+"; the bundle serves 16.2.4.
30. `neon-postgres-serverless` ↔ its own earlier version — "API Routes under api.myownclone.com" vs. `api.` being an alias of the same deployment.
31. `dns-superficie-publica-myownclone` ↔ its own earlier version — the 9-subdomain list vs. `admin.myownclone.com` not existing.

## Legacy issues NOT fixed (outside the refinery's write authority)

House rules restrict the Refinery to `1-desk/`, `2-atoms/`, `3-threads/`, `briefings/`. The following legacy issues are flagged by audits but live in `concepts/`, `entities/`, `comparisons/` — they need the Editor or a human.

- `[[delfi]]` typo in 4 files (actual note: `entities/delphi.md`) — `concepts/ai-clones.md:53`, `entities/eugenio-oller.md:24`, `entities/myownclone.md:102`, `comparisons/myownclone-vs-delfi.md:58`.
- `[[leader-sumaris]]` in `entities/eugenio-oller.md:18` — no such note exists anywhere.
- Dangling `sources:` refs in 4 legacy notes (`concepts/ai-clones-market.md`, `entities/myownclone.md` ×2, `entities/coachvox-ai.md`, `comparisons/myownclone-competitors.md`) — filenames don't resolve or point at a live URL instead of a vault artifact.
- `comparisons/myownclone-competitors.md` is a full orphan: zero incoming and zero outgoing wikilinks. Its content is now contradicted by two new atoms, so it needs a rewrite, not just a link.

## Files written this run

- `2-atoms/` — 107 new atoms + 38 extended + 3 retired to `2-atoms/archive/`
- `3-threads/myownclone-vs-myclone-is.md` — competitive comparison thread
- `3-threads/myownclone-security-surface.md` — security findings thread
- `briefings/2026-10-22.md` — morning briefing
- `briefings/scout-report-2026-10-21.md` — moved out of `1-desk/` (kept, not deleted)
- `1-desk/` — cleaned; contains only this report

## Errors

None unresolved. Two subagents reported transient `patch` failures on concurrent writes; both re-verified and landed. One subagent flagged a concurrent-write collision on `frontend-nextjs-vercel-sentry-posthog.md` (a sibling was adding a source ref at the same moment) and restored the lost ref — verified present in the final file.

## Next run

The reading list is still empty. The pipeline will keep producing zero-run briefings until at least one URL is added to `0-raw/reading-list.md`. The backlog in `raw/articles/` is now fully atomized, so the next real feedstock must come from new captures.
