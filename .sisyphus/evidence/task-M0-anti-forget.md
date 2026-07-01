# Evidence — M0: Capa anti-olvido

**Milestone:** M0
**Fecha QA:** 2026-06-21
**Resultado:** ✅ PASS

## Artefactos creados

| Archivo | Proposito |
|---------|-----------|
| `.sisyphus/progress.json` | Estado canonico de las 15 tareas (M0-M13). Schema: `{id, milestone, title, status, evidence_file, committed_sha, qa_at, symbols}`. |
| `scripts/check-plan-progress.py` | Verificador. Valida: max 1 `in_progress`, orden `done` respeta `order`, toda `done` tiene evidence_file commiteado + SHA valido. Exit 1 bloquea commit/CI. |
| `tests/test_plan_completion.py` | Smoke test policia. 15 tests (1 por milestone) que importan simbolos canonicos. Rojo mientras el hito no exista. |
| `scripts/pre-commit-hook.sh` + `.git/hooks/pre-commit` (git-common-dir) | Hook que ejecuta el checker antes de cada commit. |

## Verificacion ejecutada

```
$ python scripts/check-plan-progress.py
Sisyphus plan: Sistema de Modelos IA Configurables por Tarea (M0-M13)
  done:        0/15  []
  in_progress: 1        ['M0']
  pending:     14       [...]
[OK] progreso consistente.
EXIT=0

$ python -m pytest tests/test_plan_completion.py -q
FAILED tests/test_plan_completion.py::test_m1_ai_model_classes_exist
  ModuleNotFoundError: No module named 'api.models.ai_models'
```

**Demostracion del mecanismo:** el primer test falla en rojo porque M1 no existe.
Esto confirma que ningun agente puede declarar M1 "done" sin haberlo codeado:
el simbolo canonico debe ser importable para que el test pase.

## Defecto preexistente corregido (fuera de plan, bloqueaba baseline)

`tests/test_local_knowledge_retrieval.py` importaba `_EMBEDDING_DIMENSIONS`
(privado, inexistente) pero el simbolo publico es `EMBEDDING_DIMENSIONS`
(re-exportado por `api/core/retrieval.py:28`). Corregido el import en 2 sitios.
Baseline: **96 passed**.

## Guardrails cubiertos
- El checker valida el orden declarado en `order`: M3 no puede estar `done` si M2 no lo esta.
- Como maximo 1 `in_progress` a la vez (evita trabajo paralelo confuso).
- `done` exige evidence_file tracked en git + committed_sha valido.
