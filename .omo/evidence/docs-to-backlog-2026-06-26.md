# Docs to Backlog - Post-Sisyphus Product Wave

Date: 2026-06-26
Source ref: `origin/main` at `8b9d3c1cc7c819831358a3018abd1a28e27a23de`

## Purpose

This document distills the wiki / OSINT corpus into an implementation backlog.
It is intentionally separate from the Sisyphus M8-M13 stabilization plan.

Rule: do not copy competitor endpoints or credentials. Convert product lessons
into MyOwnClone-native features that fit the current Flask + Next.js codebase.

## Source Map

Use these documents as follows:

| Source | Role in implementation |
| --- | --- |
| `SCHEMA.md` | Wiki structure and provenance rules |
| `index.md` | Navigation map for the corpus |
| `queries/myownclone-blueprint.md` | Architecture synthesis and product principles |
| `comparisons/myownclone-vs-delfi.md` | Differentiation: contextual instances, anti-hallucination, multi-mode retrieval |
| `concepts/retrieval-augmented-cognition.md` | RAC behavior: retrieval before answer, separated silos, fallback when similarity is low |
| `concepts/context-aware-instances.md` | Context-specific clone links and lead magnet use cases |
| `concepts/synthetic-data-testing.md` | Test strategy for conversational quality |
| `raw/articles/myownclone-osint-implementation-handoff-2026-06-24.md` | Raw gap analysis and proposed implementation steps |
| `raw/articles/myownclone-osint-implementation-plan-2026-06-24.md` | Feature priority list; useful, but must be filtered |

## Already Exists Or Is In Progress

These should not become new product work until Sisyphus is stabilized.

| Capability | Current evidence | Backlog treatment |
| --- | --- | --- |
| Multi-tenant admin and platform views | `api/controllers/console/myownclone/admin_platform.py`, `MyOwnClone/src/app/admin/*` | Keep; verify after Sisyphus |
| Clone CRUD and mode prompts | `api/controllers/console/myownclone/clone.py`, `api/models/clone.py` | Extend, do not replace |
| Three retrieval modes / silos | `api/models/clone.py`, `api/core/myownclone/silos.py`, `api/core/retrieval.py` | Preserve as differentiator |
| Memories / signatures / templates | `api/controllers/console/myownclone/creator_memory.py`, `MyOwnClone/src/app/(dashboard)/cerebro/page.tsx` | Normalize schema before adding new UX |
| Knowledge library / ingestion surface | `MyOwnClone/src/app/(dashboard)/biblioteca/page.tsx`, `api/core/ingestion.py` | Later: connect to contextual links |
| AI model routing and observability foundation | Sisyphus M1-M13 worktree | Finish first |

## Must Fix Before Product Expansion

These are not shiny features; they are foundation repairs.

### A1 - Normalize mode contracts

Problem:

- Backend uses `CloneSilo.TEACH = "teach"`.
- Drizzle schema uses `"pedagogy"` in `cloneModeEnum`.
- Existing controller code already imports `normalize_silo` / `normalize_silo_list`, which suggests a partial repair exists.

Implementation direction:

- Make one canonical cross-boundary mapping module for `teach` <-> `pedagogy`.
- Cover API payloads, DB reads/writes, UI forms, and public chat mode selection.
- Do not rename production DB enum values blindly; map at boundaries first.

Acceptance:

- Tests prove `teach`, `pedagogy`, `support`, and `sales` round-trip correctly.
- Public chat and dashboard prompt editing use the same normalized mode values.

### A2 - Normalize memory schema drift

Problem:

- Frontend memory routes require `title`.
- Drizzle `memories` has `title` and `updatedAt`.
- SQLAlchemy `CreatorMemory` currently exposes `content`, `trigger_condition`, and `priority`, but no `title` field in the current model snapshot.

Implementation direction:

- Decide whether `creator_memory` and `memories` are meant to be one logical table or two integration surfaces.
- Add missing backend model/API fields only after checking the real database migration state.
- Preserve backward compatibility for existing rows by deriving a title from content if needed.

Acceptance:

- Creating, editing, listing, and using memories preserves `title`.
- Chat prompt enrichment can include memory titles when present without breaking old rows.

### A3 - Reconcile prompt timestamp drift

Problem:

- SQLAlchemy models inherit `updated_at`.
- Drizzle `clone_mode_prompts` currently lacks `updatedAt`.

Implementation direction:

- Add the missing Drizzle field if the database column exists.
- If not, add a migration only after confirming deploy state.

Acceptance:

- Prompt edits expose a reliable update timestamp to the UI and API.

## Post-Sisyphus Backlog

### P1 - Prompt versioning

Why:

- This is the highest-value feature from the OSINT corpus.
- It fits the existing `CloneModePrompt` model and `cerebro` editing surface.
- It reduces operational risk because prompt edits become reversible.

Scope:

- Add prompt version table for clone + mode snapshots.
- Snapshot the previous prompt before every update.
- Add history, restore, compare, and timeline endpoints.
- Add a compact history/diff UI in `cerebro`.

Native endpoint shape:

- `GET /myownclone/clones/{clone_id}/prompts/history`
- `POST /myownclone/clones/{clone_id}/prompts/restore/{version}`
- `GET /myownclone/clones/{clone_id}/prompts/diff?v1=...&v2=...`

Do not copy:

- Do not mirror MyClone endpoint names unless they fit existing MyOwnClone routing.
- Do not ingest competitor prompt templates verbatim.

Tests:

- Version increments per clone + mode.
- Restore creates a new current prompt or clearly records restored state.
- Diff handles missing versions and cross-tenant access denial.

### P2 - Context-aware clone instances

Why:

- This is a core differentiator in the wiki.
- It ties together retrieval, knowledge sources, lead capture, and shareable links.

Scope:

- Add a lightweight `clone_contexts` or equivalent model.
- Each context points to clone, mode/silo, optional source/module/product metadata.
- Public links pass context into retrieval filters.
- Dashboard shows context links for creators.

Dependencies:

- Finish M8 embeddings/retrieval stabilization.
- Ensure source metadata is reliable enough to filter.

Tests:

- A context link limits retrieval to the expected source metadata.
- Missing context falls back to clone-wide retrieval.
- Cross-tenant context access is denied.

### P3 - Lead and visitor capture

Why:

- The corpus repeatedly frames contextual clone links as a lead magnet.
- MyOwnClone currently has feedback and analytics, but not a full visitor/lead loop.

Scope:

- Track anonymous clone sessions.
- Capture email/name after a configurable event, such as N messages or explicit CTA.
- Add creator-facing visitors table and simple metrics.
- Record source context when available.

Dependencies:

- Context-aware instances become more useful first.

Tests:

- Lead capture validates email and tenant/clone ownership.
- Duplicate visitors update `last_accessed_at`, not uncontrolled duplicates.
- Dashboard lists only tenant-owned leads.

### P4 - Synthetic conversation testing

Why:

- The wiki describes synthetic customer simulations as the quality loop.
- This is safer and cheaper than adding advanced voice/monetization too early.

Scope:

- Add a CLI or admin-only test runner for clone conversations.
- Seed synthetic personas/questions per mode.
- Store result summaries: pass/fail, retrieval quality, refusal correctness.
- Use AI model registry after Sisyphus so model costs are tracked.

Tests:

- Runner can execute a bounded test set without external side effects.
- Low-similarity questions verify the "I do not know" path.

### P5 - Prompt observability

Why:

- The raw handoff mentions Langfuse, but MyOwnClone now has its own AI invocation/cost foundation from Sisyphus.
- Start with native observability before adding another vendor.

Scope:

- Track prompt version id on AI invocations.
- Add per-prompt latency, cost, token, and error breakdown.
- Add quality notes or manual rating before automated LLM judges.

Do not start with:

- Langfuse integration, unless native telemetry proves insufficient.

### P6 - Workflows

Why:

- Workflows are useful but structurally larger than prompt versioning or leads.

Scope:

- Template model.
- Workflow assignment to clone/context.
- Session state and step answering.
- Creator analytics.

Defer until:

- Prompt versioning, context links, and lead capture are shipped.

### P7 - Monetization, custom domains, and voice

Why defer:

- They touch external providers, billing, DNS, real-time media, and support burden.
- They are valuable but not the next safest product increment.

Future order:

1. custom domains, because `CloneConfig.custom_domain` already exists
2. creator monetization via Stripe Connect
3. voice / LiveKit / ElevenLabs / Cartesia

## Do Not Copy Directly

- Competitor credentials from raw OSINT documents.
- Competitor endpoint paths as public contracts.
- Prompt text extracted from a competitor as production default.
- Claims from raw articles without checking against code or current product direction.

## Recommended Execution Order

1. Finish Sisyphus M8-M13 stabilization.
2. Ship A1-A3 as a foundation repair tranche.
3. Ship P1 prompt versioning.
4. Ship P2 context-aware clone instances.
5. Ship P3 lead capture.
6. Ship P4 synthetic conversation testing.
7. Ship P5 prompt observability.
8. Re-evaluate P6/P7 once the above has real usage data.

## Immediate Next Work Plan

Create a dedicated implementation plan named `post-sisyphus-prompt-foundation`
after Sisyphus is stable. Its first tranche should include:

- A1 mode normalization
- A2 memory schema normalization
- A3 prompt timestamp drift
- P1 prompt versioning backend
- P1 prompt versioning UI

That tranche is small enough to ship in isolated commits and valuable enough to
unlock safer prompt experimentation immediately.
