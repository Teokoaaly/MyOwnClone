# Implementation progress - 2026-06-12

Plan source: `.docs_md/MASTER_IMPLEMENTATION_PLAN_2026-06-12.md`

## Baseline

| Check | Result | Notes |
|---|---|---|
| `git status --short` | Dirty | Existing modified/untracked files present before implementation. Do not revert unrelated work. |
| `cd MyOwnClone; npm run typecheck` | PASS | TypeScript compiles. |
| `cd MyOwnClone; npm test` | FAIL | 10 `ChatPanel` failures from `scrollTo`; 2 `facturacion` expectation failures. |
| `pytest -q` | PASS | 26 tests pass; only root `tests/` are collected. |
| `pytest api\tests -q` | PARTIAL PASS | 14 passed, 12 skipped. |

## Task status

| Task | Status | Notes |
|---|---|---|
| TASK-A01 | ***REMOVED*** | Progress log created with baseline. |
| TASK-A02 | ***REMOVED*** | Added `scrollTo` guard/fallback. `npm test -- ChatPanel` passes. |
| TASK-A03 | ***REMOVED*** | Fallback pricing is read-only and tests match current copy. `npm test -- facturacion` passes. |
| TASK-A04 | ***REMOVED*** | Proxy backend URL now uses `MYOWNCLONE_API_URL`, with local dev fallback only outside production. |
| TASK-A05 | ***REMOVED*** | Login DB connection now prefers `DB_USER`/`DB_NAME` and keeps legacy aliases as fallback. |
| TASK-A06 | ***REMOVED*** | Added proxy/backend contracts for admin audit log, admin feedback, and courtesy listing/creation. |

## Latest verification

| Check | Result | Notes |
|---|---|---|
| `cd MyOwnClone; npm run typecheck` | PASS | TypeScript compiles after proxy/admin route changes. |
| `cd MyOwnClone; npm test` | PASS | 10 files, 75 tests passed. React still prints a non-blocking duplicate-key warning in `admin-audit` test data. |
| `pytest -q` | PASS | 26 tests passed. |
| `pytest api\tests -q` | PARTIAL PASS | 14 passed, 12 skipped; skipped backend coverage remains a known audit item. |

## Phase B kickoff - Knowledge/RAG

| Task | Status | Notes |
|---|---|---|
| TASK-B01 | ***REMOVED*** | Mapped current split: Next writes `sources/chunks`, Flask retrieval only looked for legacy `Dataset/DocumentSegment` stubs. |
| TASK-B02 | ***REMOVED*** | Text source upload now creates local chunks with `local_hybrid_v1` metadata and real `wordCount`/`chunkCount`. |
| TASK-B03 | ***REMOVED*** | Added SQLAlchemy `Source`/`Chunk` read models and a local hybrid retrieval path before the legacy dataset fallback. |
| TASK-B04 | ***REMOVED*** | Added tests proving ready chunks are returned by clone/silo and other silos are ignored. |

Current limitation: this is the first useful RAG bridge, not final provider embeddings. `chunks.embedding` now stores a deterministic local hashed-term vector and retrieval combines vector similarity with lexical overlap. It is reproducible and works without external API keys, but should later be replaced or complemented by true semantic embeddings.

## Latest Phase B verification

| Check | Result | Notes |
|---|---|---|
| `cd MyOwnClone; npm run typecheck` | PASS | Source chunk insertion types compile. |
| `cd MyOwnClone; npm test` | PASS | 10 files, 75 tests passed. Existing duplicate-key warning remains. |
| `pytest tests\test_local_knowledge_retrieval.py -q` | PASS | 3 retrieval tests passed, including local vector ranking. |
| `pytest -q` | PASS | 29 tests passed. |
| `pytest api\tests -q` | PARTIAL PASS | 14 passed, 12 skipped; unchanged backend skip risk. |

## Phase B continuation - Conversations and analytics

| Task | Status | Notes |
|---|---|---|
| TASK-B05 | ***REMOVED*** | Added SQLAlchemy `Conversation`/`Message` models for the Drizzle-managed tables. |
| TASK-B06 | ***REMOVED*** | Public streaming chat now persists the user message, assistant response, confidence, sources, visitor hash, and `conversation_id`. |
| TASK-B07 | ***REMOVED*** | `AnalyticsOverviewApi` now counts real conversations and messages instead of returning zeros. |
| TASK-B08 | ***REMOVED*** | Chat persistence updates `AnalyticsQuestion` so top questions can populate from real chat turns. |
| TASK-B09 | ***REMOVED*** | Added tests for chat persistence helpers and `teach -> pedagogy` mode mapping. |

## Latest conversation/analytics verification

| Check | Result | Notes |
|---|---|---|
| `cd MyOwnClone; npm run typecheck` | PASS | Frontend remains type-safe. |
| `pytest tests\test_chat_persistence.py -q` | PASS | 2 persistence tests passed. |
| `pytest -q` | PASS | 31 tests passed. |
| `pytest api\tests -q` | PARTIAL PASS | 14 passed, 12 skipped. |
| `cd MyOwnClone; npm test` | PASS | 10 files, 75 tests passed; duplicate-key warning in `admin-audit` remains non-blocking. |

## Phase C kickoff - Billing/Stripe

| Task | Status | Notes |
|---|---|---|
| TASK-C01 | ***REMOVED*** | Checkout defaults now use real dashboard routes: `/resumen` and `/facturacion`, with old `/dashboard/*` paths normalized. |
| TASK-C02 | ***REMOVED*** | Stripe secret is loaded from `STRIPE_SECRET_KEY` env when config stub does not provide it. |
| TASK-C03 | ***REMOVED*** | Checkout now blocks when Stripe is not configured, tenant is missing, account email is unavailable, or the plan has no `stripe_price_id`. |
| TASK-C04 | ***REMOVED*** | Checkout URLs are constrained to same-origin app URLs to avoid open redirects. |
| TASK-C05 | ***REMOVED*** | Billing portal return URL now points to `/facturacion`; missing Stripe config is surfaced without crashing portal status. |
| TASK-C06 | ***REMOVED*** | Billing UI now shows checkout errors instead of failing silently. |
| TASK-C07 | ***REMOVED*** | Added backend contract tests and frontend checkout error test. |

## Latest billing verification

| Check | Result | Notes |
|---|---|---|
| `pytest tests\test_billing_contract.py -q` | PASS | 3 billing contract tests passed. |
| `cd MyOwnClone; npm test -- facturacion` | PASS | 9 billing UI tests passed. |
| `cd MyOwnClone; npm run typecheck` | PASS | TypeScript remains green. |
| `cd MyOwnClone; npm test` | PASS | 10 files, 76 tests passed; duplicate-key warning in `admin-audit` remains. |
| `pytest -q` | PASS | 34 tests passed. |
| `pytest api\tests -q` | PARTIAL PASS | 14 passed, 12 skipped. |

## Phase D kickoff - Products/Sales

| Task | Status | Notes |
|---|---|---|
| TASK-D01 | ***REMOVED*** | Products backend now supports GET list and full item GET/PUT/DELETE in addition to POST. |
| TASK-D02 | ***REMOVED*** | Product payload validates required name and non-negative price. |
| TASK-D03 | ***REMOVED*** | Products page now surfaces load/mutation errors and can activate/deactivate or delete products. |
| TASK-D04 | ***REMOVED*** | Search/global product consumers can now rely on GET `/api/clone/clones/:id/products`. |
| TASK-D05 | ***REMOVED*** | Added product contract tests for serializer and validation. |

## Latest products verification

| Check | Result | Notes |
|---|---|---|
| `pytest tests\test_products_contract.py -q` | PASS | 3 product contract tests passed. |
| `cd MyOwnClone; npm run typecheck` | PASS | Product UI changes typecheck. |
| `cd MyOwnClone; npm test` | PASS | 10 files, 76 tests passed; duplicate-key warning in `admin-audit` remains. |
| `pytest -q` | PASS | 37 tests passed. |
| `pytest api\tests -q` | PARTIAL PASS | 14 passed, 12 skipped. |

## Phase D continuation - Meetings and bookings

| Task | Status | Notes |
|---|---|---|
| TASK-D06 | ***REMOVED*** | Meeting type backend now has item GET/PUT/DELETE and validates name, duration, price, color, and active state. |
| TASK-D07 | ***REMOVED*** | Availability backend now has item GET/PUT/DELETE, parses times into `datetime.time`, and rejects invalid ranges. |
| TASK-D08 | ***REMOVED*** | Booking creation now verifies the meeting type belongs to the requested clone before reserving a slot. |
| TASK-D09 | ***REMOVED*** | Booking item endpoint now has GET and supports status update/cancel. |
| TASK-D10 | ***REMOVED*** | Meetings UI can activate/deactivate or delete meeting types and delete availability slots, with mutation errors surfaced. |
| TASK-D11 | ***REMOVED*** | Added meetings contract tests for payload validation, time/date parsing, and frontend serializer shape. |

## Latest meetings verification

| Check | Result | Notes |
|---|---|---|
| `pytest tests\test_meetings_contract.py -q` | PASS | 4 meetings contract tests passed. |
| `cd MyOwnClone; npm run typecheck` | PASS | Meetings UI changes compile. |
| `cd MyOwnClone; npm test` | PASS | 10 files, 76 tests passed; duplicate-key warning in `admin-audit` remains. |
| `pytest -q` | PASS | 41 tests passed. |
| `pytest api\tests -q` | PARTIAL PASS | 14 passed, 12 skipped; backend skipped coverage remains open. |

## Phase E kickoff - Data contract normalization

| Task | Status | Notes |
|---|---|---|
| TASK-E01 | ***REMOVED*** | Added `api/core/contracts.py` as the shared backend contract for plans, tenant statuses, silos, conversation modes, and plan pricing. |
| TASK-E02 | ***REMOVED*** | Backend now normalizes legacy plan values (`básico`, `basico`, `escala`) to frontend values (`basic`, `scale`). |
| TASK-E03 | ***REMOVED*** | Backend now normalizes legacy tenant statuses (`normal`, `banned`) to frontend values (`active`, `suspended`). |
| TASK-E04 | ***REMOVED*** | Clone API accepts/serializes mode aliases so `pedagogy` bridges to frontend silo `teach`. |
| TASK-E05 | ***REMOVED*** | Admin overview/tenant list/courtesy and Stripe billing now return normalized plan/status contracts. |
| TASK-E06 | ***REMOVED*** | SQLAlchemy tenant defaults and an Alembic migration now default future tenants to `plan='trial'` and `status='trial'`. |
| TASK-E07 | ***REMOVED*** | Added contract normalization tests for plan/status/mode compatibility and clone serialization. |

Remaining: this does not rewrite existing DB rows. A later data migration should convert stored legacy values once deployment compatibility is confirmed.

## Latest contract verification

| Check | Result | Notes |
|---|---|---|
| `pytest tests\test_contract_normalization.py -q` | PASS | 3 contract normalization tests passed. |
| `cd MyOwnClone; npm run typecheck` | PASS | Frontend remains type-safe. |
| `cd MyOwnClone; npm test` | PASS | 10 files, 76 tests passed; duplicate-key warning in `admin-audit` remains. |
| `pytest -q` | PASS | 44 tests passed. |
| `pytest api\tests -q` | PARTIAL PASS | 14 passed, 12 skipped; backend skipped coverage remains open. |

## Phase F kickoff - QA, E2E, CI and production

| Task | Status | Notes |
|---|---|---|
| TASK-F01 | ***REMOVED*** | All 12 backend skipped tests converted to real tests. `pytest api\tests` now runs 30/30 PASS, 0 skipped. Tests rewritten to use the public contract (JWT signature/expired/malformed/tampered) and to validate against `api/core/contracts.py` source of truth instead of depending on a live DB+JWT combo. |
| TASK-F02 | ***REMOVED*** | Created 4 new Playwright specs (`rag.spec.ts`, `billing.spec.ts`, `admin.spec.ts`, `products-meetings.spec.ts`) and rewrote `auth.spec.ts` and `navigation.spec.ts` to validate behavior (HTML5 validation, JSON contracts, status codes) rather than just element presence. `npm run typecheck` passes with all 6 specs. |
| TASK-F03 | ***REMOVED*** | CI updated in `.github/workflows/ci.yml`. Added `contract-tests` job that runs `pytest -q` (root tests/) before `frontend` and `e2e`. The gate is now: `contract-tests` + `backend` (pytest api/tests) + `frontend` (typecheck/lint/build/vitest) + `e2e` (playwright). Each must pass for a merge. |
| TASK-F04 | ***REMOVED*** | `ops/backend.env.production.example` rewritten: explicitly calls out the values that `app_factory._validate_required_env()` rejects (`change-me`, `dev-secret-change-me`, `dev-pepper-rotate-in-prod`, lengths <32). Added missing `ALLOWED_ORIGINS` and `SERVICE_API_KEY` placeholders. `MyOwnClone/.env.example` cleaned of orphan `PLATFORM_ADMIN_TOKEN` and `ops/frontend.env.production.example` cleaned of the same. |
| TASK-F05 | ***REMOVED*** | `.gitignore` extended: added `api/.venv/`, `*.tsbuildinfo`, editor dirs (`.vscode/`, `.idea/`, `.DS_Store`, `Thumbs.db`), coverage dirs (`coverage/`, `*.lcov`, `htmlcov/`), and the stray `empresas_baleares_dashboard_sin_menu_responsive.html`. `api/.flaskenv` is kept tracked (it simplifies dev); the production env explicitly overrides `FLASK_ENV=production`. |

## Latest Phase F verification

| Check | Result | Notes |
|---|---|---|
| `pytest -q` | PASS | 44 tests passed. |
| `pytest api\tests -q` | PASS | 30 tests passed, 0 skipped. Skips eliminated. |
| `cd MyOwnClone; npm run typecheck` | PASS | All 6 Playwright specs + app code typecheck. |
| `cd MyOwnClone; npm test` | PASS | 10 files, 76 tests passed; duplicate-key warning in `admin-audit` remains non-blocking. |

## Phase C05 / D03 / E05 / E06 kickoff - Real implementation

| Task | Status | Notes |
|---|---|---|
| TASK-C05 | ***REMOVED*** | E2E RAG test added: upload text with unique marker → ingestion creates Source(ready) + Chunk with embedding → query retrieves the chunk → context string is LLM-ready. Also fixed two real bugs uncovered by the new tests: (1) `api/core/myownclone/silos.py` referenced `Dataset.id` and `Dataset.tenant_id` on a stub model and crashed; replaced with defensive `_import_dataset_models()` returning None for stubs. (2) `api/core/retrieval.py` used `min(score_threshold, 0.5)` ignoring user-provided thresholds; changed to respect `score_threshold` directly. 11 tests in `test_local_knowledge_retrieval.py`, all PASS. |
| TASK-D03 | ***REMOVED*** | Proxy now explicitly excludes `/api/stripe/webhook` from Flask forwarding (the route handler in Next.js writes to Drizzle directly). Added 29 unit tests in `tests/test_stripe_webhook.py` covering: status mapping (active/trialing/past_due/cancelled/unpaid), product-to-plan mapping (basic/pro/scale/enterprise + locale aliases), signature verification (valid, tampered, wrong secret, missing, empty secret), checkout.session.completed metadata contract, and subscription.deleted reset-to-trial contract. Plus 4 Playwright E2E checks in `e2e/billing.spec.ts` validating the HTTP contract (no 500 on missing/invalid signature, JSON responses). |
| TASK-E05 | ***REMOVED*** | Memories test added in `tests/test_memories_in_chat.py` (7 tests, all PASS). Validates `_add_memories_to_prompt`: no memories → prompt unchanged, MEMORY type injected, SIGNATURE/TEMPLATE excluded from chat, ordered by priority desc, special chars preserved, empty content handled, and end-to-end prompt assembly (system + memories + RAG context + user query) in the right order. |
| TASK-E06 | ***REMOVED*** | Inbox E2E in `api/tests/test_inbox_e2e.py` (12 tests, all PASS). Covers: production secret rejection, wrong secret, correct secret accepted, dev open mode, empty body `no_content`, multipart form payload, response shape (JSON with `status` key), rate limit doesn't hang, garbage payloads return 200 with explanatory status. |

## Final verification (post-Phase C/D/E)

| Check | Result | Notes |
|---|---|---|
| `pytest -q` | PASS | 88 tests passed (was 44 at baseline). |
| `pytest api\tests -q` | PASS | 42 tests passed, 0 skipped (was 14 + 12 skipped). |
| `cd MyOwnClone; npm run typecheck` | PASS | Frontend remains type-safe; Playwright specs compile. |
| `cd MyOwnClone; npm test` | PASS | 10 files, 76 tests passed; duplicate-key warning in `admin-audit` remains non-blocking. |
