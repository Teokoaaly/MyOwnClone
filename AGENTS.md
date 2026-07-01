# AGENTS.md — Opencode Minimal Loop

These rules are loaded by opencode before loop work.

## Loop Mode

- Start in L1 report-only mode.
- Read `STATE.md` before any triage.
- Update `STATE.md` after every loop run.
- Do not edit source code until the human explicitly enables L2.

## Safety

- Never push or merge without human approval.
- Never edit `.env`, `.env.*`, `auth/`, `payments/`, `secrets/`, or `credentials/`.
- Use a git worktree for every code-changing attempt.
- Max 3 fix attempts per item; escalate after that.

## Verification

- For L2+ changes, dispatch a verifier sub-agent after implementation.
- Run `pytest` before proposing a fix (project uses pytest).
- Record test evidence in `STATE.md`.

## MyOwnClone Specific

- Working branch: `audit/sisyphus-vps-integration`
- Do not touch VPS live checkout or deploy scripts without approval.
- Respect `.sisyphus/` tracker — do not modify without approval.
- Run `git diff --check` before every commit.
