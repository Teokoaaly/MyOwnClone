# MyOwnClone Docker Fix - Remaining Work

## TL;DR

> **Goal**: Get all 4 Docker services running (postgres, redis, weaviate, api)
> **Remaining**: Create missing `wraps.py` module, restart API container
> **Estimated Effort**: Quick (1 file)
> **Parallel Execution**: NO (sequential)

---

## Context

### Done
- ✅ Fixed `app_factory.py` imports
- ✅ Cleaned controller `__init__.py` files
- ✅ Created `docker-compose.yml` with 4 services
- ✅ Fixed Docker build context and WORKDIR
- ✅ Configured Weaviate with `DISABLE_AUTH: "true"`
- ✅ postgres, redis, weaviate containers running

### Blocked
- ❌ api container exited - missing `controllers/console/wraps.py`

---

## Work Objectives

### Core Objective
Complete Docker setup by creating missing module and verifying Flask starts.

### Must Have
- [ ] `wraps.py` created with `account_initialization_required` and `setup_required` decorators
- [ ] API container running and Flask app responding

### Definition of Done
- [ ] `docker ps` shows all 4 containers running
- [ ] `docker logs myownclone_api` shows Flask app started without import errors

---

## TODOs

- [ ] 1. Create `wraps.py` with decorators

  **What to do**:
  - Create `C:\Users\haxth3\Documents\MyOwnClone\api\api\controllers\console\wraps.py`
  - Add `account_initialization_required` decorator (checks `g.account`)
  - Add `setup_required` decorator (checks `g.workspace`)

  **References**:
  - `api/api/controllers/console/admin_platform.py:16` - imports these decorators

  **QA Scenarios**:
  ```
  Scenario: wraps.py file created
    Tool: Bash
    Steps: Test-Path "C:\Users\haxth3\Documents\MyOwnClone\api\api\controllers\console\wraps.py"
    Expected: True

  Scenario: Module imports work
    Tool: Bash  
    Steps: cd C:\Users\haxth3\Documents\MyOwnClone\api && docker compose up -d && docker logs myownclone_api 2>&1 | Select-Object -First 30
    Expected: No ModuleNotFoundError for controllers.console.wraps
  ```

- [ ] 2. Restart API container

  **What to do**:
  - Run `docker compose up -d` in api directory
  - Check container status with `docker ps`

  **QA Scenarios**:
  ```
  Scenario: API container starts
    Tool: Bash
    Steps: docker ps --filter "name=myownclone_api" --format "{{.Status}}"
    Expected: Up

  Scenario: Flask app responds
    Tool: Bash
    Steps: docker logs myownclone_api 2>&1 | Select-Object -First 50
    Expected: Flask app loaded, no import errors
  ```

- [ ] 3. Verify all 4 containers running

  **What to do**:
  - Check all 4 containers with `docker ps --filter "name=myownclone"`

  **QA Scenarios**:
  ```
  Scenario: All containers running
    Tool: Bash
    Steps: docker ps --filter "name=myownclone" --format "{{.Names}}\t{{.Status}}"
    Expected: postgres Up, redis Up, weaviate Up, api Up
  ```

## Final Verification Wave
- [ ] F1. Docker containers running: `docker ps --filter "name=myownclone" --format "{{.Names}}\t{{.Status}}"`

---

## Success Criteria
```bash
docker ps --filter "name=myownclone" --format "{{.Names}}\t{{.Status}}"
# Expected: postgres, redis, weaviate, api - all showing "Up"
```