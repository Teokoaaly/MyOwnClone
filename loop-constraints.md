# Loop Constraints

> Add rules below with `/constraints <rule>` in your agent.
> The `loop-constraints` skill reads this file at the start of every run.
> Constraints here are **binding** — the agent MUST follow them.

## Push & Merge
- Don't push before telling me
- Never auto-merge to main without human approval
- Always create a draft PR first; let me review before marking ready

## Paths
- Never edit .env, .env.*, auth/, payments/, secrets/, credentials/
- Never edit infrastructure configs without human approval

## Code
- Always run tests before proposing a fix
- Never disable tests to make CI green
- Never refactor unrelated code — one fix per run
- Max 3 fix attempts per item; escalate after

## Communication
- Always tell me what you're about to do before doing it
- Never close an issue or PR without my approval

## Budget
- If token spend hits 80% of daily cap, switch to report-only
- If loop-pause-all is active, exit immediately

## MyOwnClone — Reglas del Proyecto
- Trabajar solo en la rama `audit/sisyphus-vps-integration` a menos que se indique otra cosa
- No modificar el checkout del VPS en vivo ni los scripts de deploy (`ops/deploy-*.sh`) sin aprobación explícita
- No modificar archivos `.sisyphus/` sin aprobación — son el tracker de hitos
- No mezclar `origin/master` en el flujo de integración sin aprobación
- Ejecutar `git diff --check` antes de cada commit
- No hacer deploy hasta que los scripts de rollback estén verificados
- Cada tarea debe actualizar `.sisyphus/progress.json`

---
<!-- Add your own rules below. Use plain English. The loop reads this verbatim. -->
