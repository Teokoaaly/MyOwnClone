---
slug: sisyphus-system-improvement
status: awaiting-approval
intent: unclear
pending-action: write .omo/plans/sisyphus-system-improvement.md
approach: Reconcile the mixed Sisyphus M8-M13 worktree into verifiable milestone slices first, stabilize admin/VPS deployment surfaces second, and only then open a new product-improvement wave for prompt versioning and observability.
---

# Draft: sisyphus-system-improvement

## Components (topology ledger)
<!-- Lock the SHAPE before depth. One row per top-level component that can succeed or fail independently. -->
<!-- id | outcome (one line) | status: active|deferred | evidence path -->
| C1 | Reconcile repo state, tracker state, and branch reality into one trustworthy execution lane | active | `.omo/evidence/task-1-sisyphus-system-improvement.md` |
| C2 | Finish and verify backend runtime milestones M8-M10 with isolated commits and evidence | active | `.omo/evidence/task-2-sisyphus-system-improvement.md` |
| C3 | Finish and verify admin/ops milestones M11-M13, including visible model controls and deploy readiness | active | `.omo/evidence/task-3-sisyphus-system-improvement.md` |
| C4 | Validate the integrated result on VPS without touching the live checkout until rollback and smoke gates pass | active | `.omo/evidence/task-4-sisyphus-system-improvement.md` |
| C5 | Open the next product-improvement wave from the OSINT handoff only after Sisyphus is stable | deferred | `.omo/evidence/task-5-sisyphus-system-improvement.md` |

## Open assumptions (announced defaults)
<!-- Intent is UNCLEAR: research resolves ambiguity, defaults are adopted (not asked), and each is surfaced in the plan's human TL;DR for veto. -->
<!-- assumption | adopted default | rationale | reversible? -->
| Dirty worktree handling | Reconcile and commit only milestone-scoped slices; do not mass-commit the current tree | The repo already contains mixed M8-M13 work plus local hotfixes, so batch committing would destroy auditability | yes |
| VPS workflow | Use VPS only for integration validation and controlled deploys, never as the primary development checkout | `TASKS.md` and prior VPS incidents already establish this as the safer lane | yes |
| Priority of improvements | Finish Sisyphus stability and admin visibility before starting prompt-versioning or other OSINT-derived features | The current branch is already ahead of the remote plan and has incomplete verification debt | yes |
| Auth/admin scope | Keep the existing admin-login hotfix path and only revisit auth if regression tests fail | The current auth change is already coupled to production admin access | yes |
| Git discipline | Preserve one milestone = one commit = one push for all remaining work | This is already the repo rule and is the best defense against losing progress across sessions | no |

## Findings (cited - path:lines)
- `TASKS.md:7-20` already defines the safe execution rules: `audit/sisyphus-vps-integration`, no live VPS checkout edits, one task/commit/push, and no deploy before rollback is verified.
- `HANDOFF_LLM.md:8-13` is stale about the local branch (`master`) while the real branch head is now `audit/sisyphus-vps-integration`; another agent reading only that file would start from the wrong assumption.
- `.sisyphus/progress.json:97-159` marks M8-M10 as `in_progress` and M11-M13 as `pending`, but the worktree already contains modified evidence files and implementation files for M11-M13, so tracker state and code state have drifted.
- `MyOwnClone/src/lib/auth.ts:105-124` contains an admin bootstrap path that now reuses an existing `accounts` row when present; this is operationally important and must be preserved during any auth-adjacent cleanup.
- `api/controllers/console/myownclone/ai_models.py:131-176` shows the admin AI-model CRUD path already exists and invalidates `ModelRegistry`; remaining work is not greenfield, it is reconciliation plus surface completion.

## Decisions (with rationale)
- Treat the next execution wave as a stabilization-and-reconciliation project, not as feature-first development.
- Use the existing Sisyphus milestone structure (M8-M13) as the execution spine instead of inventing a parallel roadmap.
- Separate "finish what is already in the tree" from "start new product improvements" so the user gets a shippable, reviewable state before widening scope.
- Keep all evidence in `.sisyphus/evidence/` for milestone work and use `.omo/evidence/` only for the meta-plan and tranche-level execution evidence.

## Scope IN
- Reconcile `HANDOFF_LLM.md`, `.sisyphus/progress.json`, milestone evidence, and the real branch/worktree state.
- Verify and complete the remaining Sisyphus milestones M8-M13.
- Ensure the admin IA surface is visible, quantifiable, and operable once deployed.
- Validate deploy readiness and VPS rollout discipline before any production promotion.
- Prepare the follow-on improvement lane for prompt versioning and related OSINT-derived features.

## Scope OUT (Must NOT have)
- No direct development inside the live VPS checkout.
- No blind merge of `origin/master` into the Sisyphus integration branch.
- No deploy of partially verified milestone batches.
- No broad auth rewrite while admin access is currently stabilized by a known hotfix.
- No start of prompt-versioning implementation until Sisyphus M8-M13 is reconciled and verified.

## Open questions
- None worth blocking on. The remaining ambiguity is execution order, and the repo state already answers that: stabilize first, expand later.

## Approval gate
status: awaiting-approval
<!-- When exploration is exhausted and unknowns are answered, set status: awaiting-approval. -->
<!-- That durable record is the loop guard: on a later turn read it and resume at the gate instead of re-running exploration. -->
