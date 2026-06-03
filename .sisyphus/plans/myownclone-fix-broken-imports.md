# MyOwnClone — Fix Broken Imports After Rename

## TL;DR

> **Quick Summary**: Arreglar los imports rotos en el backend después del rename `dify/` → `api/`, y restaurar/configurar docker-compose.
> 
> **Deliverables**:
> - `app_factory.py` import corregido
> - `controllers/__init__.py` limpiado de imports Dify inexistentes
> - Docker compose funcional
> 
> **Estimated Effort**: Short (1-2 horas)
> **Parallel Execution**: YES — 3 tasks
> **Critical Path**: Task 1 → Task 2 → Task 3

---

## Context

### Original Request
"hay partes del plan que no estas funcionando" — el plan anterior (myownclone-dify-cleanup) marcó tareas como completadas pero hay imports rotos que impiden que Flask funcione.

### Issues Identified

1. **`app_factory.py` línea 5**: `from api.api.controllers.myownclone_public import myownclone_public_bp` — el path `api/api/` no existe desde dentro de `api/api/`. Debe ser `from controllers.myownclone_public import myownclone_public_bp`.

2. **`controllers/__init__.py`**: Tiene imports a módulos Dify que NO existen en el proyecto:
   - `from libs.external_api import ExternalApi` — `libs/` no existe o no tiene `external_api.py`
   - `RESOURCE_MODULES` incluye `controllers.console.app.app_import`, `controllers.console.explore.*`, etc. — módulos que no existen
   - Estos imports rotos impiden que Flask arranque

3. **No hay `docker-compose.yml`**: El archivo de Docker no existe en el proyecto. El plan anterior dijo "BLOCKER: pre-existing" pero claramente necesita crearse o restaurarse.

### Metis Review

**Identified Gaps**:
- El rename `dify/` → `api/` cambió la estructura de directorios pero los imports en `app_factory.py` quedaron con paths absolutos que no funcionan
- `controllers/__init__.py` tiene imports a módulos Dify que ya no existen — necesita limpieza completa
- Docker compose era necesario para el proyecto — hay que crearlo o buscarlo

---

## Work Objectives

### Core Objective
Hacer que Flask pueda iniciar correctamente y que Docker compose funcione.

### Concrete Deliverables
- `app_factory.py` con import corregido
- `controllers/__init__.py` limpio de imports a módulos inexistentes
- `docker-compose.yml` funcional
- Flask puede crear la app sin errores de import

### Definition of Done
- [ ] `cd api/api && python -c "from app_factory import create_app; print('OK')"` funciona sin errores
- [ ] `docker compose up -d` levanta todos los servicios
- [ ] No más `ModuleNotFoundError` al importar desde `api/api/`

---

## Execution Strategy

```
Wave 1 (Immediate — critical fixes):
├── Task 1: Fix app_factory.py import [quick]
├── Task 2: Clean controllers/__init__.py [quick]
├── Task 3: Create/restore docker-compose.yml [quick]

Wave FINAL:
├── Verify Flask starts without errors
└── Verify Docker compose works
```

---

## TODOs

- [x] 1. Fix app_factory.py import

  **What to do**:
  - Leer `api/api/app_factory.py`
  - Cambiar línea 5: `from api.api.controllers.myownclone_public import myownclone_public_bp` → `from controllers.myownclone_public import myownclone_public_bp`
  - Verificar que el archivo `api/api/controllers/myownclone_public.py` existe y tiene el blueprint `myownclone_public_bp`

  **Must NOT do**:
  - NO cambiar la lógica de la función `register_myownclone_blueprints()`
  - NO eliminar el import — solo corregir el path

  **Recommended Agent Profile**:
  - **Category**: `quick`
  - **Skills**: []

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Blocks**: Task 4 (Flask verification)
  - **Blocked By**: None

  **References**:
  - `C:\Users\haxth3\Documents\MyOwnClone\api\api\app_factory.py:5` — Import a corregir
  - `C:\Users\haxth3\Documents\MyOwnClone\api\api\controllers\myownclone_public.py` — Archivo que debe existir

  **Acceptance Criteria**:
  - [ ] `app_factory.py` usa `from controllers.myownclone_public import myownclone_public_bp`
  - [ ] El import no busca `api.api.controllers`

  **QA Scenarios**:

  ```
  Scenario: Verify app_factory.py import is fixed
    Tool: Bash
    Preconditions: File exists at api/api/app_factory.py
    Steps:
      1. Read api/api/app_factory.py
      2. Verify line 5 is "from controllers.myownclone_public import myownclone_public_bp"
      3. Verify the file controllers/myownclone_public.py exists
    Expected Result: Import path is correct (no api.api prefix)
    Failure Indicators: Still has "from api.api.controllers" or file not found
    Evidence: .sisyphus/evidence/fix-1-app-factory.txt
  ```

  **Commit**: YES
  - Message: `fix(imports): correct app_factory.py import path`
  - Files: `api/api/app_factory.py`

---

- [x] 2. Clean controllers/__init__.py

  **What to do**:
  - Leer `api/api/controllers/__init__.py`
  - Identificar TODOS los imports que referencian módulos que no existen:
    - `from libs.external_api import ExternalApi` — verificar si `libs/external_api.py` existe
    - `RESOURCE_MODULES` tuple — todos estos módulos (`controllers.console.app.*`, `controllers.console.explore.*`, etc.) verificar si existen
  - Los módulos MyOwnClone (`from .console.myownclone import ...`) generalmente SÍ existen — verificar
  - **Opción A**: Si los módulos existen pero el import path es incorrecto, corregir
  - **Opción B**: Si los módulos no existen (Dify legacy), eliminar el import y dejar solo los que sí existen
  - Crear backup del archivo antes de modificar

  **Must NOT do**:
  - NO eliminar imports de módulos que SÍ existen (como `from .console.myownclone import ...`)
  - NO romper el Blueprint `bp` y el API namespace `api`
  - NO eliminar `console_ns = Namespace("console", ...)` — se necesita para los endpoints

  **Recommended Agent Profile**:
  - **Category**: `quick`
  - **Skills**: []

  **Parallelization**:
  - **Can Run In Parallel**: YES (with Task 1)
  - **Blocks**: Task 4 (Flask verification)
  - **Blocked By**: None

  **References**:
  - `C:\Users\haxth3\Documents\MyOwnClone\api\api\controllers\__init__.py` — Archivo a limpiar
  - `C:\Users\haxth3\Documents\MyOwnClone\api\api\controllers\console\myownclone\` — Módulos MyOwnClone que SÍ existen
  - `C:\Users\haxth3\Documents\MyOwnClone\api\api\controllers\console\myownclone_public.py` — Módulo público que SÍ existe

  **Acceptance Criteria**:
  - [ ] `from libs.external_api import ExternalApi` — verificado si existe o eliminado
  - [ ] RESOURCE_MODULES — verificado cuáles existen y eliminados los que no
  - [ ] Flask puede importar `controllers` sin `ModuleNotFoundError`
  - [ ] Blueprint `bp` y namespace `api` siguen definidos

  **QA Scenarios**:

  ```
  Scenario: Verify controllers/__init__.py is clean
    Tool: Bash
    Preconditions: File exists at api/api/controllers/__init__.py
    Steps:
      1. Read api/api/controllers/__init__.py
      2. For each import, verify the module exists:
         - libs/external_api.py → does it exist?
         - controllers.console.app.app_import → does it exist?
         - (etc.)
      3. If module doesn't exist, it should be removed from the import list
      4. Run: cd api/api && python -c "from controllers import bp, api; print('OK')"
    Expected Result: No ModuleNotFoundError, bp and api are defined
    Failure Indicators: Still importing non-existent modules
    Evidence: .sisyphus/evidence/fix-2-controllers-init.txt
  ```

  **Commit**: YES
  - Message: `fix(imports): clean controllers/__init__.py of non-existent modules`
  - Files: `api/api/controllers/__init__.py`

---

- [x] 3. Create or restore docker-compose.yml

  **What to do**:
  - Buscar si existe en algún lugar del repo (antes del rename o en otro branch)
  - Si no existe, crear uno básico con:
    - PostgreSQL service
    - Redis service
    - Flask API service
    - Weaviate service (si está disponible)
  - El archivo debe estar en `api/api/docker-compose.yml` o `api/docker-compose.yml`
  - Usar la imagen `langgenius/dify-api` si es la que se usaba (según AUDIT.md era image de Dify)

  **Must NOT do**:
  - NO usar `docker compose down -v` (no perder datos)
  - NO cambiar la estructura del proyecto

  **Recommended Agent Profile**:
  - **Category**: `quick`
  - **Skills**: []

  **Parallelization**:
  - **Can Run In Parallel**: YES (with Tasks 1-2)
  - **Blocks**: Task 5 (Docker verification)
  - **Blocked By**: None

  **References**:
  - `C:\Users\haxth3\Documents\MyOwnClone\CLAUDE.md:48` — Comando: `cd api/api && docker compose up -d`
  - `C:\Users\haxth3\Documents\MyOwnClone\PLAN MAESTRO - MyOwnClone.md` — Stack técnico

  **Acceptance Criteria**:
  - [ ] `docker-compose.yml` existe en ubicación válida
  - [ ] `docker compose config` no da errores de sintaxis
  - [ ] `docker compose up -d` levanta los servicios

  **QA Scenarios**:

  ```
  Scenario: Verify docker-compose.yml exists and is valid
    Tool: Bash
    Preconditions: None
    Steps:
      1. Search for docker-compose.yml in api/, api/api/, and parent dirs
      2. If found, run: docker compose -f <path> config
      3. If not found, create from scratch with PostgreSQL, Redis, Flask, Weaviate
      4. Verify docker compose config succeeds
    Expected Result: Valid docker-compose.yml exists
    Failure Indicators: File not found, syntax errors
    Evidence: .sisyphus/evidence/fix-3-docker-compose.txt
  ```

  **Commit**: YES
  - Message: `chore(docker): add docker-compose.yml`
  - Files: `api/docker-compose.yml` or `api/api/docker-compose.yml`

---

- [x] 4. Verify Flask app starts

  **What to do**:
  - Después de Tasks 1 y 2, verificar que Flask puede crear la app
  - Ejecutar: `cd api/api && python -c "from app_factory import create_app; app = create_app(); print('OK')"`
  - Si hay errores, diagnosticarlos y corregirlos

  **Must NOT do**:
  - NO iniciar el servidor completo (solo verificar que la app se crea)

  **Recommended Agent Profile**:
  - **Category**: `quick`
  - **Skills**: []

  **Parallelization**:
  - **Can Run In Parallel**: NO
  - **Blocks**: None
  - **Blocked By**: Tasks 1, 2

  **References**:
  - `C:\Users\haxth3\Documents\MyOwnClone\api\api\app_factory.py` — Flask app factory

  **Acceptance Criteria**:
  - [ ] `python -c "from app_factory import create_app; app = create_app(); print('OK')"` outputs "OK"
  - [ ] No ImportError or ModuleNotFoundError

  **QA Scenarios**:

  ```
  Scenario: Verify Flask app creation succeeds
    Tool: Bash
    Preconditions: Tasks 1 and 2 completed
    Steps:
      1. cd api/api
      2. python -c "from app_factory import create_app; app = create_app(); print('OK')"
    Expected Result: Output is "OK" with no errors
    Failure Indicators: ModuleNotFoundError, ImportError, any traceback
    Evidence: .sisyphus/evidence/fix-4-flask-start.txt
  ```

  **Commit**: NO (verification task)

---

- [x] 5. Verify Docker compose works

  **What to do**:
  - Verificar que docker-compose.yml es válido
  - Ejecutar `docker compose up -d`
  - Verificar que todos los servicios inician: `docker compose ps`

  **Must NOT do**:
  - NO ejecutar `docker compose down -v`

  **Recommended Agent Profile**:
  - **Category**: `quick`
  - **Skills**: []

  **Parallelization**:
  - **Can Run In Parallel**: NO
  - **Blocks**: None
  - **Blocked By**: Task 3

  **References**:
  - Docker Compose file location (from Task 3)

  **Acceptance Criteria**:
  - [ ] `docker compose ps` shows all services as "Up"
  - [ ] `docker compose logs --tail=20` shows no critical errors

  **QA Scenarios**:

  ```
  Scenario: Verify Docker services start
    Tool: Bash
    Preconditions: Task 3 completed (docker-compose.yml exists)
    Steps:
      1. cd to docker-compose.yml directory
      2. docker compose up -d
      3. Wait 10 seconds
      4. docker compose ps
    Expected Result: All services show "Up"
    Failure Indicators: Services in "Exit" or "Restarting" state, errors in logs
    Evidence: .sisyphus/evidence/fix-5-docker-start.txt
  ```

  **Commit**: NO (verification task)

---

## Final Verification

- [ ] F1. **Flask App Test** — `python -c "from app_factory import create_app; print('OK')"` succeeds
- [ ] F2. **Docker Compose Test** — `docker compose up -d` and `docker compose ps` show all services Up

---

## Success Criteria

### Verification Commands
```bash
# Flask app
cd api/api && python -c "from app_factory import create_app; app = create_app(); print('OK')"
# Expected: OK (no errors)

# Docker compose
cd api/api && docker compose up -d && docker compose ps
# Expected: All services Up
```

---

## Commit Strategy

- **Fix Wave**: `fix(imports): correct app_factory.py and clean controllers/__init__.py`
- **Docker Wave**: `chore(docker): add docker-compose.yml`

---

## Notes

- El problema principal es que el rename `dify/` → `api/` dejó imports con paths incorrectos
- `app_factory.py` usa `api.api.controllers` que no existe desde `api/api/`
- `controllers/__init__.py` importa módulos Dify que no existen en el codebase
- El docker-compose.yml nunca existió en el repo — necesita crearse