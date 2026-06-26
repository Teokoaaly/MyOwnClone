# sisyphus-system-improvement - Work Plan

## TL;DR (For humans)
<!-- Fill this LAST, after the detailed plan below is written, so it summarizes the REAL plan. -->
<!-- Plain English for a non-engineer: NO file paths, NO todo numbers, NO wave/agent/tool names. -->

**What you'll get:** a clean continuation path that finishes the configurable-AI system already started, keeps VPS risk low, and leaves the next agent with a trustworthy sequence instead of a mixed branch. It ends with the admin AI surface and deployment flow in a state that can be measured, reviewed, and promoted safely.

**Why this approach:** the repo is not blocked by missing features first; it is blocked by mixed milestone state, stale handoff metadata, and partially verified work spread across backend, frontend, and VPS integration. Reconciling that first is the fastest way to stop breaking production and stop losing progress between sessions.

**What it will NOT do:** it will not turn the live VPS checkout into a dev sandbox. It will not merge unfinished work straight into production. It will not start the next product wave until the current AI-configurable foundation is actually stable.

**Effort:** Large
**Risk:** Medium - most of the code already exists, but verification debt and dirty-state drift make false completion the main danger.
**Decisions I made for you:** finish Sisyphus M8-M13 before starting prompt-versioning; use VPS only for integration/deploy validation; keep one milestone per commit/push; preserve the current admin-login fix unless tests prove it wrong.

Your next move: approve this plan and execute it tranche by tranche. Full execution detail follows below.

---

> TL;DR (machine): large / medium-risk stabilization plan to reconcile mixed M8-M13 work, finish admin/VPS visibility, then open the next product-improvement wave.

## Scope
### Must have
- Reconcile milestone tracker, evidence, branch state, and actual modified files into one trustworthy execution lane.
- Finish Sisyphus M8-M13 with isolated verification, evidence, commits, and pushes.
- Validate the integrated result on VPS through a non-live worktree/release path with rollback and smoke checks.
- Leave a follow-on tranche defined for prompt-versioning and related OSINT-derived improvements.
### Must NOT have (guardrails, anti-slop, scope boundaries)
- Do not develop inside the live VPS checkout.
- Do not batch unrelated changes into one commit.
- Do not deploy anything lacking rollback proof, milestone evidence, and smoke validation.
- Do not widen scope into new product work before M8-M13 is stable.

## Verification strategy
> Zero human intervention - all verification is agent-executed.
- Test decision: tests-after + pytest, targeted frontend build/typecheck, and VPS smoke checks
- Evidence: `.omo/evidence/task-<N>-sisyphus-system-improvement.md` plus milestone evidence in `.sisyphus/evidence/`

## Execution strategy
### Parallel execution waves
> Target 5-8 todos per wave. Fewer than 3 (except the final) means you under-split.
- Wave 1: state reconciliation and milestone slicing.
- Wave 2: backend runtime completion (M8-M10).
- Wave 3: admin surface and operational closure (M11-M13).
- Wave 4: VPS integration validation and controlled promotion readiness.
- Wave 5: post-stabilization product-improvement plan activation.

### Dependency matrix
| Todo | Depends on | Blocks | Can parallelize with |
| --- | --- | --- | --- |
| 1 | none | 2,3,4,5,6 | none |
| 2 | 1 | 4,5 | 3 |
| 3 | 1 | 4,5 | 2 |
| 4 | 2,3 | 6 | 5 |
| 5 | 2,3 | 6 | 4 |
| 6 | 4,5 | 7 | none |
| 7 | 6 | done | none |

## Todos
> Implementation + Test = ONE todo. Never separate.
<!-- APPEND TASK BATCHES BELOW THIS LINE WITH edit/apply_patch - never rewrite the headers above. -->
- [ ] 1. Reconcile branch, tracker, and evidence into one truthful execution baseline
  What to do / Must NOT do: update the operational docs so they describe the real branch, real remote baseline, the last pushed milestone, and the mixed local state; normalize `.sisyphus/progress.json` so every remaining milestone is either `pending` or `in_progress` for a defensible reason; do not mark anything `done` without a commit SHA and passing verification evidence.
  Parallelization: Wave 1 | Blocked by: none | Blocks: 2, 3, 4, 5, 6
  References (executor has NO interview context - be exhaustive): `TASKS.md:7-20`, `HANDOFF_LLM.md:8-44`, `.sisyphus/progress.json:1-160`, `git log --oneline --decorate -n 20 --graph` current branch history, current `git status --short`
  Acceptance criteria (agent-executable): `git diff --check`; `python scripts/check-plan-progress.py`; `rg -n "audit/sisyphus-vps-integration|origin/audit/vps-sync-and-docs|M8|M13" HANDOFF_LLM.md .sisyphus/progress.json TASKS.md`
  QA scenarios (name the exact tool + invocation): happy = a fresh agent can read `HANDOFF_LLM.md`, `TASKS.md`, `.sisyphus/progress.json` and derive the same next milestone order; failure = checker or grep still shows stale branch/state claims. Evidence `.omo/evidence/task-1-sisyphus-system-improvement.md`
  Commit: Y | `docs(sisyphus): reconcile execution baseline for remaining milestones`
- [ ] 2. Slice and finish backend runtime work for M8 and M10
  What to do / Must NOT do: isolate and complete the embeddings/runtime integration changes already present in the tree, including `api/core/embeddings.py`, STT/runtime integration, and affected frontend proxy routes; do not drag M11-M13 admin/ops changes into this commit.
  Parallelization: Wave 2 | Blocked by: 1 | Blocks: 4, 5
  References (executor has NO interview context - be exhaustive): `.sisyphus/progress.json:107-131`, `.sisyphus/evidence/task-M8-embeddings-refactor.md`, `.sisyphus/evidence/task-M10-integration.md`, `api/core/embeddings.py`, `api/core/stt.py`, `api/controllers/myownclone_public.py`, `MyOwnClone/src/app/api/stt/route.ts`, `MyOwnClone/src/app/api/clone/sources/route.ts`
  Acceptance criteria (agent-executable): `git diff --check`; `pytest -v api/tests/test_embeddings_registry.py api/tests/test_ai_runtime_integration.py`; targeted endpoint smoke or import smoke for touched runtime modules
  QA scenarios (name the exact tool + invocation): happy = embeddings and runtime tests pass with the milestone evidence updated and `progress.json` reflecting M8/M10 completion; failure = one of the runtime tests still requires unrelated M11-M13 code to pass. Evidence `.omo/evidence/task-2-sisyphus-system-improvement.md`
  Commit: Y | `feat(ai): finish M8 embeddings and M10 runtime integrations`
- [ ] 3. Slice and finish admin/API work for M9 independently of UI polish
  What to do / Must NOT do: isolate the admin API/controller/model changes and backfill command wiring already introduced, verify CRUD/assignments/playground/runtime status endpoints, and keep UI-only changes out of this commit unless they are required for endpoint contracts.
  Parallelization: Wave 2 | Blocked by: 1 | Blocks: 4, 5
  References (executor has NO interview context - be exhaustive): `.sisyphus/evidence/task-M9-admin-api.md`, `api/controllers/console/myownclone/ai_models.py:1-260`, `api/controllers/console/__init__.py`, `api/controllers/console/myownclone/__init__.py`, `api/models/ai_models.py`, `api/commands/ai_backfill.py`, `api/tests/test_ai_models_endpoints.py`
  Acceptance criteria (agent-executable): `git diff --check`; `pytest -v api/tests/test_ai_models_endpoints.py tests/test_plan_completion.py`; command discovery smoke for `flask ai-backfill-from-env --help`
  QA scenarios (name the exact tool + invocation): happy = admin API tests pass and evidence records the exact endpoints now present; failure = hidden coupling to pending UI or ops work remains. Evidence `.omo/evidence/task-3-sisyphus-system-improvement.md`
  Commit: Y | `feat(ai): finish M9 admin API and backfill surface`
- [ ] 4. Finish M11 admin UI plus the missing visibility panels that make the system measurable
  What to do / Must NOT do: complete and verify `/admin/ia-modelos`, navigation wiring, admin fetch behavior, and the missing visibility layer the user called out: registry status, cache invalidation, embeddings limits/usage visibility, costs by model, and backfill trigger visibility; do not make a broad visual redesign outside this surface.
  Parallelization: Wave 3 | Blocked by: 2, 3 | Blocks: 6
  References (executor has NO interview context - be exhaustive): `.sisyphus/evidence/task-M11-admin-ui.md`, user requirement summary for missing M14 panels, `MyOwnClone/src/app/admin/ia-modelos/page.tsx`, `MyOwnClone/src/lib/nav-admin.ts`, `MyOwnClone/src/components/admin/useAdminFetch.ts:17-87`, `MyOwnClone/src/proxy.ts`, `api/controllers/console/myownclone/ai_models.py`, `api/controllers/console/myownclone/runtime.py`
  Acceptance criteria (agent-executable): `git diff --check`; `npm run typecheck`; `npm run build`; route-level smoke for `/admin/ia-modelos` and related `/api/admin/*` endpoints using the in-app/browser or HTTP checks
  QA scenarios (name the exact tool + invocation): happy = the admin page loads, shows the registry/embeddings/cost/backfill surfaces, and the API endpoints return expected JSON; failure = login redirect loop or missing panel data remains. Evidence `.omo/evidence/task-4-sisyphus-system-improvement.md`
  Commit: Y | `feat(admin): finish M11 AI model operations surface`
- [ ] 5. Finish M12 and M13 operational closure without mixing deployment
  What to do / Must NOT do: complete the audit rollup, key rotation, defect fixes, final docs, and tracker close-out in repo form only; do not deploy from this todo.
  Parallelization: Wave 3 | Blocked by: 2, 3 | Blocks: 6
  References (executor has NO interview context - be exhaustive): `.sisyphus/evidence/task-M12-audit-rotation.md`, `.sisyphus/evidence/task-M13-defects-backfill-docs.md`, `api/core/ai_audit.py`, `api/commands/crypto.py`, `api/libs/crypto.py`, `api/migrations/versions/2026_06_23_0003_cost_daily_rollup.py`, `docs/model-secrets-key-management.md`, `api/tests/test_ai_audit_rotation.py`
  Acceptance criteria (agent-executable): `git diff --check`; `pytest -v api/tests/test_ai_audit_rotation.py api/tests/test_crypto.py tests/test_plan_completion.py`; docs grep for rotation/backfill procedure
  QA scenarios (name the exact tool + invocation): happy = audit/rotation/backfill tests pass and M12/M13 evidence includes final remote SHA placeholders ready for push confirmation; failure = commands exist but are not wired or idempotent. Evidence `.omo/evidence/task-5-sisyphus-system-improvement.md`
  Commit: Y | `feat(ai): finish M12 audit rotation and M13 close-out`
- [ ] 6. Validate the integrated branch on VPS through a safe integration lane
  What to do / Must NOT do: fetch/pull the committed branch into the VPS integration worktree or release path, run migrations in order, restart only the necessary services, and verify admin login, admin overview, AI-model admin routes, and core runtime smoke tests; do not edit the live checkout directly.
  Parallelization: Wave 4 | Blocked by: 4, 5 | Blocks: 7
  References (executor has NO interview context - be exhaustive): `TASKS.md:22-61`, `HANDOFF_LLM.md:15-30`, current VPS notes from prior sessions, deploy scripts under `ops/`, current auth hotfix behavior in `MyOwnClone/src/lib/auth.ts:105-124`
  Acceptance criteria (agent-executable): record VPS branch/SHA; run migrations; verify health endpoints and admin/API pages return success; capture service status and rollback command in evidence
  QA scenarios (name the exact tool + invocation): happy = VPS integration checkout runs the finished branch and the critical flows succeed; failure = migration, auth, or admin/API regressions are caught before production promotion. Evidence `.omo/evidence/task-6-sisyphus-system-improvement.md`
  Commit: N | operational validation only; repo commit should already exist before VPS validation
- [ ] 7. Open the next improvement tranche from the OSINT handoff only after stabilization
  What to do / Must NOT do: once M8-M13 and VPS validation are done, create the next execution plan for prompt versioning, schema-drift cleanup, and related observability/lead features; do not start coding those features in the same tranche as stabilization.
  Parallelization: Wave 5 | Blocked by: 6 | Blocks: done
  References (executor has NO interview context - be exhaustive): OSINT handoff analysis from this thread, current clone/chat/prompt surfaces in `MyOwnClone/src/app/api/clone/*`, prompt/runtime layers in `api/core/*`, and the completed Sisyphus artifacts
  Acceptance criteria (agent-executable): a new plan artifact exists with clear boundaries, dependencies, and verification strategy; no product code changed in this todo
  QA scenarios (name the exact tool + invocation): happy = next-wave plan is written after a stable base exists; failure = plan tries to fold new product work into unfinished stabilization. Evidence `.omo/evidence/task-7-sisyphus-system-improvement.md`
  Commit: Y | `docs(plan): define post-Sisyphus improvement tranche`

## Final verification wave
> Runs in parallel after ALL todos. ALL must APPROVE. Surface results and wait for the user's explicit okay before declaring complete.
- [ ] F1. Plan compliance audit
- [ ] F2. Code quality review
- [ ] F3. Real manual QA
- [ ] F4. Scope fidelity

## Commit strategy
- One commit per milestone-aligned todo: 1, 2, 3, 4, 5, and 7 each produce their own commit and push.
- Todo 6 is a VPS validation step and should not introduce repo changes; if VPS-only operational docs need updating, do that as a follow-up docs commit after validation.
- Never amend prior milestone commits; add follow-up fixes as new commits with evidence updates.

## Success criteria
- Another agent can resume from `HANDOFF_LLM.md`, `TASKS.md`, `.sisyphus/progress.json`, and this plan without guessing the branch or milestone state.
- Remaining milestones M8-M13 are each tied to passing tests, evidence, and isolated commits/pushes.
- The admin AI surface is visible and operable enough to inspect registry state, costs, embeddings status, and backfill/assignment controls after deployment.
- VPS validation proves the integrated branch works without using the live checkout as the dev area.
- The next product-improvement wave begins from a stable, observable base instead of a mixed branch.
