# MyOwnClone Launch Plan — Make It Operational

## TL;DR

> **Quick Summary**: Fix 3 critical bugs, rename public route group from `(clonify)` to `(public)`, update branding to YouOwnClone, and verify the full stack works end-to-end.
>
> **Deliverables**:
> - Public API endpoints functional (no more 404)
> - Memory injection working in AI prompts
> - Admin panel shows tenant names (not UUIDs)
> - Route group renamed `(clonify)` → `(public)`
> - Frontend metadata says "YouOwnClone"
> - `api/.env.example` created
> - Docker stack verified working
> - Seed data script for testing
>
> **Estimated Effort**: Short (2-3 hours)
> **Parallel Execution**: YES — Wave 1 and Wave 2 are independent
> **Critical Path**: Bug Fix #1 → Verify → Seed Data → Final QA

---

## Context

### Original Request
"Revisa este repositivo y el repositivo online https://github.com/Teokoaaly/MyOwnClone has una auditoria de que falta, como seguir y crea un plan exhaustivo para tenerlo en macha lo antes posible, auditalo todo y que no tenga referencia a clonify todo sera youownclone. haz el plan"

### Audit Summary
**Bugs Found (3 critical)**:
1. `register_myownclone_blueprints(app)` defined but NEVER called → all public endpoints return 404
2. `_add_memories_to_prompt()` return value discarded → memories never injected
3. `admin_platform.py` tenant lookup fallback returns UUID instead of name

**Clonify References Found**:
- Route group `(clonify)` with `ClonifyLayout` — active, needs rename
- `dify_backup/` — old backup, leave untouched
- 13+ markdown files — historical docs, leave as-is

**Infrastructure**: Docker (4 services), Backend (8 console + 6 public endpoints), Frontend (19 pages)

**Git Status**: Local synced with master, PR #1 (clonify→myownclone) merged

### Metis Review (Identified Gaps)
- Scope creep risk: "remove Clonify references" could balloon — LOCKED to folder rename only
- Missing env vars for auth/Stripe — need documentation
- No test coverage — manual QA only, no automated tests
- "Operational" = bugs fixed + boots + verified, NOT full CI/CD

### User Decisions
- **Route group name**: `(public)` (not `(yourownclone)`)
- **Seed data**: Flask CLI command
- **Seed included**: YES — include seed data script in plan

---

## Work Objectives

### Core Objective
Get MyOwnClone fully operational with all critical bugs fixed, public route group renamed, and YouOwnClone branding.

### Concrete Deliverables
- `api/api/app_factory.py` — register blueprint function called at startup
- `api/api/controllers/myownclone_public.py` — memory injection works
- `api/api/controllers/console/myownclone/admin_platform.py` — tenant name shows correctly
- `replica/src/app/(public)/` — renamed from `(clonify)`
- `replica/src/app/(public)/layout.tsx` — `YouOwnCloneLayout` + "YouOwnClone" metadata
- `api/.env.example` — created from docker-compose.yml
- Seed data command: `flask seed-demo-data`
- Verification: all 6 public endpoints return valid responses

### Definition of Done
- [ ] `curl http://localhost:5001/api/myownclone/public/clones/<slug>` returns clone JSON (not 404)
- [ ] `curl -X POST http://localhost:5001/api/myownclone/public/clones/<slug>/chat` returns SSE or JSON (not 404)
- [ ] Admin impersonation endpoint returns tenant name (not UUID)
- [ ] Route `(clonify)` renamed to `(public)` — page loads at `/<slug>`
- [ ] Metadata says "YouOwnClone" not "Réplica"
- [ ] `docker compose up -d` starts all 4 services
- [ ] `flask seed-demo-data` creates test clone + admin user
- [ ] `flask db upgrade` runs all 5 migrations without error

### Must Have
- Bug #1 (blueprint registration) MUST be fixed — blocks ALL public endpoints
- Bug #2 (memory injection) MUST be fixed — core AI functionality
- `(clonify)` → `(public)` rename MUST happen — route group is active
- Docker MUST start without errors
- At least ONE public endpoint MUST be verified with curl

### Must NOT Have (Guardrails)
- DO NOT touch `dify_backup/` directory
- DO NOT touch `v2*` remote branches
- DO NOT merge any open PRs
- DO NOT add automated tests (no pytest, no vitest test files)
- DO NOT set up CI/CD pipelines
- DO NOT install new packages (npm or pip)
- DO NOT modify database schema (no new migrations)
- DO NOT do global find-replace of "Clonify" — ONLY rename folder and update direct references

---

## Verification Strategy (MANDATORY)

### Test Decision
- **Infrastructure exists**: NO (backend has no test framework, frontend has vitest but no test files)
- **Automated tests**: NONE
- **Framework**: N/A
- **Agent-Executed QA**: MANDATORY — every task verified with curl/bash

### QA Policy
Every task includes agent-executed QA scenarios (no human intervention). Evidence saved to `.sisyphus/evidence/`.

- **Backend verification**: Use `curl` commands against localhost:5001
- **Frontend verification**: Use Playwright if UI task, otherwise visual inspection of file changes
- **Docker verification**: `docker compose ps`, `docker compose logs api`
- **Database verification**: `docker compose exec api flask db upgrade`

---

## Execution Strategy

### Parallel Execution Waves

```
Wave 1 (Foundation — fix bugs, independent tasks):
├── Task 1: Fix blueprint registration (app_factory.py)
├── Task 2: Fix memory injection (_add_memories_to_prompt)
├── Task 3: Fix admin tenant name fallback
└── Task 4: Create api/.env.example

Wave 2 (Branding — rename and update, MAX PARALLEL):
├── Task 5: Rename (clonify) → (public) folder
├── Task 6: Rename ClonifyLayout → YouOwnCloneLayout
├── Task 7: Update metadata "YouOwnClone" in layout
└── Task 8: Verify no broken imports after rename

Wave 3 (Verification + Seed):
├── Task 9: Run Docker and verify services start
├── Task 10: Run DB migrations
├── Task 11: Create seed-demo-data Flask command
└── Task 12: Verify public endpoints work with curl

Final (4 agents in parallel):
├── Task F1: Plan compliance audit (oracle)
├── Task F2: Code quality review
├── Task F3: Real manual QA (curl all endpoints)
└── Task F4: Scope fidelity check
-> Present results -> Get explicit user okay
```

### Dependency Matrix

- **1-4**: No dependencies — can start immediately
- **5-8**: Depend on Bug Fix tasks (1-4) completing first — but can run parallel WITH them since they're separate concerns. Actually: NO DEPENDENCY — Wave 2 can run in parallel with Wave 1 if desired.
- **9-12**: Depend on Wave 1 completing (Docker needs working app)
- **F1-F4**: Depend on ALL implementation tasks completing

### Agent Dispatch Summary

- **Wave 1**: `quick` (4 tasks - single file changes) — parallel possible
- **Wave 2**: `quick` (4 tasks - simple rename operations) — parallel possible
- **Wave 3**: `quick` (2 tasks) + `unspecified-high` (2 tasks - seed + verification)
- **Final**: `oracle` + `unspecified-high` + `unspecified-high` + `deep`

---

## TODOs

- [x] 1. Fix blueprint registration — call `register_myownclone_blueprints(app)`

  **What to do**:
  - Find where the Flask app is created in the API project
  - The function `register_myownclone_blueprints(app)` exists in `api/api/app_factory.py` but is never called
  - Need to find the main entry point (`run.py` or `__init__.py` or wherever `app = Flask(...)` happens)
  - Add `from api.app_factory import register_myownclone_blueprints; register_myownclone_blueprints(app)` after app creation
  - Note: `FLASK_APP=app_factory` is set in docker-compose.yml, so flask run will look for `app` or `create_app()`

  **Must NOT do**:
  - DO NOT create a new file — only modify existing
  - DO NOT change the app_factory.py function itself, just ensure it's called

  **Recommended Agent Profile**:
  > **Category**: `quick` (single-file, targeted fix)
  > **Skills**: none needed — straightforward Python/Flask pattern
  > **Skills Evaluated but Omitted**:
  >   - `git-master`: not needed, no git operations involved

  **Parallelization**:
  - **Can Run In Parallel**: YES (with Tasks 2, 3, 4)
  - **Parallel Group**: Wave 1 (with Tasks 2, 3, 4)
  - **Blocks**: Tasks 9-12 (Docker verification needs working app)
  - **Blocked By**: None (can start immediately)

  **References**:
  - `api/api/app_factory.py:1-9` — defines `register_myownclone_blueprints(app)` but never calls it
  - `api/docker-compose.yml:70` — `FLASK_APP=app_factory` env var set
  - `api/api/__init__.py` — does NOT exist (no main app entry found)
  - `api/Dockerfile:16` — `CMD ["flask", "run", ...]` relies on FLASK_APP finding `app` or `create_app`

  **Acceptance Criteria**:
  - [ ] File modified: `api/api/__init__.py` or `api/run.py` or wherever Flask app is created
  - [ ] `register_myownclone_blueprints(app)` is called after app instantiation
  - [ ] `docker compose up -d && docker compose logs api | grep -i blueprint` shows registration message

  **QA Scenarios**:

  ```
  Scenario: Public blueprint is registered and responding
    Tool: Bash (curl)
    Preconditions: Docker services running, DB migrated
    Steps:
      1. docker compose up -d
      2. docker compose exec api flask db upgrade 2>/dev/null || true
      3. curl -s http://localhost:5001/api/myownclone/public/clones/test-slug -w "\n%{http_code}"
    Expected Result: HTTP 404 (clone not found) but NOT 404 from blueprint not registered — this proves endpoint exists
    Failure Indicators: "404 Not Found" with no JSON response = blueprint NOT registered; "404" with JSON body = blueprint registered but clone doesn't exist = SUCCESS
    Evidence: .sisyphus/evidence/task-1-blueprint-registered.txt
  ```

  **Commit**: YES
  - Message: `fix(api): call register_myownclone_blueprints() at app startup`
  - Files: `api/api/app_factory.py` (or whichever file calls it)

---

- [x] 2. Fix memory injection — capture `_add_memories_to_prompt()` return value

  **What to do**:
  - In `api/api/controllers/myownclone_public.py` line 166
  - Change: `_add_memories_to_prompt(clone.id, system_prompt)`
  - To: `system_prompt = _add_memories_to_prompt(clone.id, system_prompt)`
  - The function at line 273 correctly returns `base_prompt`, but the caller ignores the return value

  **Must NOT do**:
  - DO NOT modify the function `_add_memories_to_prompt` itself — it already returns correctly
  - DO NOT change any other line in this file

  **Recommended Agent Profile**:
  > **Category**: `quick` (single line change)
  > **Skills**: none needed
  > **Skills Evaluated but Omitted**: none

  **Parallelization**:
  - **Can Run In Parallel**: YES (with Tasks 1, 3, 4)
  - **Parallel Group**: Wave 1
  - **Blocks**: None (doesn't affect runtime until chat is called)
  - **Blocked By**: None

  **References**:
  - `api/api/controllers/myownclone_public.py:166` — `_add_memories_to_prompt(clone.id, system_prompt)` return value ignored
  - `api/api/controllers/myownclone_public.py:273-285` — function definition, already returns base_prompt correctly

  **Acceptance Criteria**:
  - [ ] File modified: `api/api/controllers/myownclone_public.py`
  - [ ] Line 166: `system_prompt = _add_memories_to_prompt(clone.id, system_prompt)`

  **QA Scenarios**:

  ```
  Scenario: Memory injection fix verified by code inspection
    Tool: Bash (grep)
    Preconditions: None (file-only check)
    Steps:
      1. grep -n "_add_memories_to_prompt" api/api/controllers/myownclone_public.py
      2. Verify line 166 shows "system_prompt = _add_memories_to_prompt" (assignment, not bare call)
    Expected Result: Line 166 shows assignment of return value
    Failure Indicators: Line 166 still shows bare call without assignment
    Evidence: .sisyphus/evidence/task-2-memory-injection-fixed.txt
  ```

  **Commit**: YES
  - Message: `fix(api): capture return value from _add_memories_to_prompt()`
  - Files: `api/api/controllers/myownclone_public.py`

---

- [x] 3. Fix admin tenant name fallback — add warning log and improve fallback

  **What to do**:
  - In `api/api/controllers/console/myownclone/admin_platform.py` line 166
  - Current code: `tenant_name = tenant.name if tenant else data.tenant_id`
  - The lookup exists, but when tenant is None, it falls back to UUID which is semantically wrong
  - Improve: Add a warning log when tenant is None, and use a more descriptive fallback
  - Also look at line 169 area to understand what `tenant_name` is used for

  **Must NOT do**:
  - DO NOT remove the fallback — it's intentional for when tenant might not exist
  - DO NOT change any other behavior in this file
  - DO NOT modify the impersonation logic itself

  **Recommended Agent Profile**:
  > **Category**: `quick` (small change, logging improvement)
  > **Skills**: none needed
  > **Skills Evaluated but Omitted**: none

  **Parallelization**:
  - **Can Run In Parallel**: YES (with Tasks 1, 2, 4)
  - **Parallel Group**: Wave 1
  - **Blocks**: None
  - **Blocked By**: None

  **References**:
  - `api/api/controllers/console/myownclone/admin_platform.py:165-166` — tenant lookup and fallback
  - `api/api/controllers/console/myownclone/admin_platform.py:168-175` — return statement uses tenant_name

  **Acceptance Criteria**:
  - [ ] File modified: `api/api/controllers/console/myownclone/admin_platform.py`
  - [ ] When tenant is None, a warning is logged instead of silently using UUID
  - [ ] Return value `tenant_name` is more descriptive than raw UUID

  **QA Scenarios**:

  ```
  Scenario: Tenant name fallback improved — no UUID in logs
    Tool: Bash (curl + grep)
    Preconditions: Docker running, admin credentials available
    Steps:
      1. docker compose up -d
      2. docker compose exec api flask db upgrade 2>/dev/null || true
      3. Get admin token: curl -s -X POST http://localhost:5001/console/api/myownclone/admin/impersonate/start -H "Content-Type: application/json" -d '{"tenant_id": "fake-uuid"}' 2>&1 | grep -i "tenant_name"
    Expected Result: No raw UUID in response, or warning logged in api container
    Failure Indicators: Response contains raw UUID string as tenant_name
    Evidence: .sisyphus/evidence/task-3-tenant-fallback-fixed.txt
  ```

  **Commit**: YES
  - Message: `fix(api): add warning log when tenant lookup fails in admin`
  - Files: `api/api/controllers/console/myownclone/admin_platform.py`

---

- [x] 4. Create `api/.env.example` from docker-compose.yml

  **What to do**:
  - Create file `api/.env.example` listing all environment variables used by the API
  - Extract variable names from `docker-compose.yml` (lines 54-69) and `requirements.txt`
  - Format: one `VAR_NAME=value` per line with comment explaining purpose
  - DO NOT include real values — only placeholder examples

  **Must NOT do**:
  - DO NOT create actual .env file — only .env.example
  - DO NOT put real API keys or passwords
  - DO NOT change any existing file

  **Recommended Agent Profile**:
  > **Category**: `quick` (file creation, simple)
  > **Skills**: none needed
  > **Skills Evaluated but Omitted**: none

  **Parallelization**:
  - **Can Run In Parallel**: YES (with Tasks 1, 2, 3)
  - **Parallel Group**: Wave 1
  - **Blocks**: None
  - **Blocked By**: None

  **References**:
  - `api/docker-compose.yml:54-69` — all env vars used by API container
  - `api/requirements.txt` — Python dependencies (not env vars but document)

  **Acceptance Criteria**:
  - [ ] File created: `api/.env.example`
  - [ ] Contains all env vars from docker-compose.yml lines 54-69
  - [ ] Each var has a comment explaining its purpose
  - [ ] No real values or secrets included

  **QA Scenarios**:

  ```
  Scenario: .env.example contains all required vars
    Tool: Bash
    Preconditions: File created
    Steps:
      1. grep -c "=" api/.env.example
      2. grep "FLASK_ENV\|DB_HOST\|DB_PORT\|DB_NAME\|DB_USER\|DB_PASSWORD\|REDIS_HOST\|REDIS_PORT\|REDIS_PASSWORD\|OPENAI_API_BASE\|OPENAI_API_KEY\|STRIPE_SECRET_KEY\|RESEND_API_KEY\|WEAVIATE_URL\|WEAVIATE_API_KEY\|FLASK_APP" api/.env.example | wc -l
    Expected Result: Count matches env vars in docker-compose.yml
    Failure Indicators: Missing vars from docker-compose.yml
    Evidence: .sisyphus/evidence/task-4-env-example-created.txt
  ```

  **Commit**: YES
  - Message: `docs(api): add .env.example with all environment variables`
  - Files: `api/.env.example`

---

- [x] 5. Rename `(clonify)` folder → `(public)`

  **What to do**:
  - Rename directory `replica/src/app/(clonify)` to `replica/src/app/(public)`
  - Use `git mv` to preserve git history: `git mv replica/src/app/\(clonify\) replica/src/app/\(public\)`
  - This is a route group in Next.js App Router — the parentheses denote a group that doesn't create a URL segment

  **Must NOT do**:
  - DO NOT modify any files inside the folder — only rename the folder
  - DO NOT change any imports or references yet — Task 8 handles that

  **Recommended Agent Profile**:
  > **Category**: `quick` (directory rename)
  > **Skills**: `git-master` — use git mv for proper history
  > **Skills Evaluated but Omitted**: none

  **Parallelization**:
  - **Can Run In Parallel**: YES (with Tasks 1-4, 6, 7)
  - **Parallel Group**: Wave 2
  - **Blocks**: Task 8 (verify no broken imports)
  - **Blocked By**: None

  **References**:
  - `replica/src/app/(clonify)/layout.tsx` — the only file with Clonify reference inside
  - `replica/src/app/(clonify)/[slug]/page.tsx` — clone public chat page

  **Acceptance Criteria**:
  - [ ] Directory renamed: `replica/src/app/(public)` exists
  - [ ] Directory removed: `replica/src/app/(clonify)` does not exist
  - [ ] `git status` shows renamed file

  **QA Scenarios**:

  ```
  Scenario: (clonify) folder renamed to (public)
    Tool: Bash
    Preconditions: None
    Steps:
      1. ls replica/src/app/ | grep -E "^\(public\)|^\(clonify\)"
      2. git status --short replica/src/app/
    Expected Result: (public) exists, (clonify) does not exist, git shows rename
    Failure Indicators: (clonify) still exists or (public) doesn't exist
    Evidence: .sisyphus/evidence/task-5-folder-renamed.txt
  ```

  **Commit**: YES
  - Message: `refactor(frontend): rename (clonify) route group to (public)`
  - Files: `replica/src/app/(clonify)` → `replica/src/app/(public)`

---

- [x] 6. Rename `ClonifyLayout` → `YouOwnCloneLayout`

  **What to do**:
  - In `replica/src/app/(public)/layout.tsx`
  - Rename the exported function from `ClonifyLayout` to `YouOwnCloneLayout`
  - This component is only referenced by its location in the route group — no other imports

  **Must NOT do**:
  - DO NOT rename the file — only the function inside
  - DO NOT change any props or return JSX

  **Recommended Agent Profile**:
  > **Category**: `quick` (single function rename)
  > **Skills**: none needed
  > **Skills Evaluated but Omitted**: none

  **Parallelization**:
  - **Can Run In Parallel**: YES (with Tasks 1-5, 7, 8)
  - **Parallel Group**: Wave 2
  - **Blocks**: None
  - **Blocked By**: Task 5 (folder rename must complete first)

  **References**:
  - `replica/src/app/(public)/layout.tsx:9` — `export default function ClonifyLayout`

  **Acceptance Criteria**:
  - [ ] File modified: `replica/src/app/(public)/layout.tsx`
  - [ ] Function renamed: `ClonifyLayout` → `YouOwnCloneLayout`

  **QA Scenarios**:

  ```
  Scenario: ClonifyLayout renamed to YouOwnCloneLayout
    Tool: Bash
    Preconditions: Task 5 complete
    Steps:
      1. grep "YouOwnCloneLayout" replica/src/app/\(public\)/layout.tsx
      2. grep "ClonifyLayout" replica/src/app/\(public\)/layout.tsx | wc -l
    Expected Result: YouOwnCloneLayout found, ClonifyLayout not found (0 matches)
    Failure Indicators: ClonifyLayout still present
    Evidence: .sisyphus/evidence/task-6-layout-renamed.txt
  ```

  **Commit**: YES
  - Message: `refactor(frontend): rename ClonifyLayout to YouOwnCloneLayout`
  - Files: `replica/src/app/(public)/layout.tsx`

---

- [x] 7. Update metadata "YouOwnClone" in layout

  **What to do**:
  - In `replica/src/app/(public)/layout.tsx`
  - Change metadata from "Réplica" to "YouOwnClone"
  - Change description from "Chatea con el clon de IA..." to something appropriate
  - Also update the page title to reflect YouOwnClone branding

  **Must NOT do**:
  - DO NOT change any component logic or structure
  - DO NOT change the return JSX

  **Recommended Agent Profile**:
  > **Category**: `quick` (text change)
  > **Skills**: none needed
  > **Skills Evaluated but Omitted**: none

  **Parallelization**:
  - **Can Run In Parallel**: YES (with Tasks 1-6, 8)
  - **Parallel Group**: Wave 2
  - **Blocks**: None
  - **Blocked By**: Task 6 (same file)

  **References**:
  - `replica/src/app/(public)/layout.tsx:4-7` — metadata block

  **Acceptance Criteria**:
  - [ ] Metadata title says "YouOwnClone" not "Réplica"
  - [ ] Description updated appropriately

  **QA Scenarios**:

  ```
  Scenario: Metadata updated to YouOwnClone
    Tool: Read
    Preconditions: Task 6 complete
    Steps:
      1. grep -i "youownclone\|réplica" replica/src/app/\(public\)/layout.tsx
    Expected Result: "YouOwnClone" found, "Réplica" not found
    Failure Indicators: "Réplica" still present in metadata
    Evidence: .sisyphus/evidence/task-7-metadata-updated.txt
  ```

  **Commit**: YES
  - Message: `refactor(frontend): update metadata to YouOwnClone branding`
  - Files: `replica/src/app/(public)/layout.tsx`

---

- [x] 8. Verify no broken imports after rename

  **What to do**:
  - After all rename tasks complete, verify no imports reference `(clonify)` or `ClonifyLayout`
  - Search for: `from './(clonify)'`, `from './ClonifyLayout'`, `'./(clonify)/`, `'./ClonifyLayout'`
  - Also check `next.config.ts` for any path aliases
  - Run `cd replica && npm run build` to verify no import errors

  **Must NOT do**:
  - DO NOT fix any broken imports manually — only report them
  - If found, create issue for follow-up

  **Recommended Agent Profile**:
  > **Category**: `unspecified-high` (verification with build)
  > **Skills**: none needed
  > **Skills Evaluated but Omitted**: none

  **Parallelization**:
  - **Can Run In Parallel**: NO (runs after Tasks 5, 6, 7)
  - **Parallel Group**: Wave 2 (sequential after rename tasks)
  - **Blocks**: None
  - **Blocked By**: Tasks 5, 6, 7

  **References**:
  - `replica/src/app/(public)/layout.tsx` — the only file that had direct Clonify references
  - `replica/next.config.ts` — path aliases if any

  **Acceptance Criteria**:
  - [ ] No references to `(clonify)` or `ClonifyLayout` in codebase
  - [ ] `cd replica && npm run build` completes without errors
  - [ ] If errors found, they are reported as issues (not fixed in this plan)

  **QA Scenarios**:

  ```
  Scenario: No broken imports after rename
    Tool: Bash
    Preconditions: Tasks 5, 6, 7 complete
    Steps:
      1. grep -r "clonify\|Clonify" replica/src/ --include="*.tsx" --include="*.ts" | grep -v node_modules | grep -v ".next"
      2. cd replica && npm run build 2>&1 | tail -20
    Expected Result: No matches for clonify/Clonify, build completes
    Failure Indicators: Any grep matches, build fails
    Evidence: .sisyphus/evidence/task-8-imports-verified.txt
  ```

  **Commit**: NO (verification only)

---

- [x] 9. Run Docker and verify all services start

  **What to do**:
  - Run `cd api && docker compose up -d`
  - Wait for services to be healthy: `docker compose ps`
  - Check logs for any startup errors: `docker compose logs api --tail=50`
  - Verify postgres is accepting connections: `docker compose exec db_postgres pg_isready -U postgres`
  - Verify redis is accepting connections: `docker compose exec redis redis-cli -a dev_password_123 ping`

  **Must NOT do**:
  - DO NOT modify any files — only run commands
  - DO NOT change docker-compose.yml

  **Recommended Agent Profile**:
  > **Category**: `unspecified-high` (Docker operations)
  > **Skills**: none needed
  > **Skills Evaluated but Omitted**: none

  **Parallelization**:
  - **Can Run In Parallel**: NO (Task 9 runs after all Wave 1 tasks)
  - **Parallel Group**: Wave 3
  - **Blocks**: Tasks 10, 11, 12
  - **Blocked By**: Tasks 1, 2, 3, 4 (need app fixes in place)

  **References**:
  - `api/docker-compose.yml` — defines all 4 services
  - `api/Dockerfile` — API container build

  **Acceptance Criteria**:
  - [ ] `docker compose ps` shows all 4 services running
  - [ ] `docker compose logs api | grep -i error` shows no errors
  - [ ] Postgres and Redis are healthy

  **QA Scenarios**:

  ```
  Scenario: Docker stack starts successfully
    Tool: Bash
    Preconditions: Tasks 1-4 complete
    Steps:
      1. cd api && docker compose up -d
      2. sleep 10 && docker compose ps
      3. docker compose logs api --tail=30
    Expected Result: All 4 services running, no error logs
    Failure Indicators: Any service not running, error logs present
    Evidence: .sisyphus/evidence/task-9-docker-running.txt
  ```

  **Commit**: NO (verification only)

---

- [x] 10. Run database migrations

  **What to do**:
  - Run `cd api && docker compose exec api flask db upgrade`
  - Verify all 5 migrations applied: `docker compose exec api flask db current`
  - Check for any migration errors

  **Must NOT do**:
  - DO NOT modify any migration files
  - DO NOT run `flask db downgrade`

  **Recommended Agent Profile**:
  > **Category**: `quick` (database operation)
  > **Skills**: none needed
  > **Skills Evaluated but Omitted**: none

  **Parallelization**:
  - **Can Run In Parallel**: NO (after Task 9)
  - **Parallel Group**: Wave 3
  - **Blocks**: Task 12 (verification needs migrations)
  - **Blocked By**: Task 9

  **References**:
  - `api/api/migrations/versions/` — 5 migration files
  - `api/requirements.txt` — Flask-Migrate installed

  **Acceptance Criteria**:
  - [ ] `flask db upgrade` completes without errors
  - [ ] `flask db current` shows latest migration

  **QA Scenarios**:

  ```
  Scenario: Database migrations applied successfully
    Tool: Bash
    Preconditions: Task 9 complete
    Steps:
      1. cd api && docker compose exec api flask db upgrade
      2. docker compose exec api flask db current
      3. docker compose exec api flask db history
    Expected Result: All 5 migrations applied, no errors
    Failure Indicators: Migration errors, incomplete upgrade
    Evidence: .sisyphus/evidence/task-10-migrations-applied.txt
  ```

  **Commit**: NO (verification only)

---

- [x] 11. Create `flask seed-demo-data` command

  **What to do**:
  - Create a Flask CLI command that creates:
    - 1 demo tenant
    - 1 demo clone (with slug "demo-clone", name "Demo Clone")
    - 1 admin user (email: admin@youownclone.com, password: admin123)
    - 1 meeting type (name: "Consultation", duration: 30min, price: 9900 cents)
    - 1 availability slot
  - Register the command in the Flask app's CLI
  - Make it idempotent — check if data exists before creating

  **Must NOT do**:
  - DO NOT modify any existing models or migrations
  - DO NOT create new migrations
  - DO NOT hardcode real production values

  **Recommended Agent Profile**:
  > **Category**: `unspecified-high` (Flask CLI + seed logic)
  > **Skills**: none needed
  > **Skills Evaluated but Omitted**: none

  **Parallelization**:
  - **Can Run In Parallel**: NO (after Task 10)
  - **Parallel Group**: Wave 3
  - **Blocks**: Task 12 (needs seed data to verify)
  - **Blocked By**: Task 10

  **References**:
  - `api/api/models/clone.py` — CloneConfig model
  - `api/api/models/meeting.py` — MeetingType_, Availability models
  - `api/api/models/analytics.py` — Plan model
  - `api/api/controllers/console/myownclone/clone.py` — existing CRUD patterns

  **Acceptance Criteria**:
  - [ ] `flask seed-demo-data` command exists and runs
  - [ ] Creates demo tenant, clone, admin user, meeting type, availability
  - [ ] Idempotent: running twice doesn't create duplicates
  - [ ] Output shows what was created

  **QA Scenarios**:

  ```
  Scenario: Seed command creates demo data
    Tool: Bash
    Preconditions: Task 10 complete
    Steps:
      1. cd api && docker compose exec api flask seed-demo-data
      2. docker compose exec api flask seed-demo-data  # run again to verify idempotency
    Expected Result: First run creates data, second run says "already exists"
    Failure Indicators: Command fails, duplicates created
    Evidence: .sisyphus/evidence/task-11-seed-command.txt
  ```

  **Commit**: YES
  - Message: `feat(api): add flask seed-demo-data command for testing`
  - Files: New file in `api/api/commands/seed.py` (or similar)

---

- [x] 12. Verify public endpoints work with curl

  **What to do**:
  - After Docker is running and migrations applied, test all 6 public endpoints:
    1. `GET /api/myownclone/public/clones/demo-clone` — should return clone JSON
    2. `POST /api/myownclone/public/clones/demo-clone/chat-simple` — should return mock response
    3. `GET /api/myownclone/public/clones/demo-clone/meeting-types` — should return empty array or meeting types
    4. `POST /api/myownclone/public/clones/demo-clone/bookings` — should return validation error (missing fields)
    5. `POST /api/myownclone/public/inbound-email` — should accept webhook
    6. `POST /api/myownclone/public/clones/demo-clone/chat` — SSE endpoint, test with short timeout

  - Before testing, run seed command: `docker compose exec api flask seed-demo-data`

  **Must NOT do**:
  - DO NOT test with real AI (chat endpoint) — just verify it returns something
  - DO NOT modify any files

  **Recommended Agent Profile**:
  > **Category**: `unspecified-high` (API verification)
  > **Skills**: none needed
  > **Skills Evaluated but Omitted**: none

  **Parallelization**:
  - **Can Run In Parallel**: NO (final verification)
  - **Parallel Group**: Wave 3
  - **Blocks**: Final Wave (F1-F4)
  - **Blocked By**: Tasks 9, 10, 11

  **References**:
  - `api/api/controllers/myownclone_public.py` — all 6 endpoint definitions
  - `api/docker-compose.yml` — port 5001 mapping

  **Acceptance Criteria**:
  - [ ] All 6 endpoints return non-404 responses
  - [ ] Chat-simple returns valid JSON mock response
  - [ ] Meeting-types returns valid JSON array
  - [ ] Bookings returns validation error (not 404) — proves endpoint exists

  **QA Scenarios**:

  ```
  Scenario: All 6 public endpoints are reachable
    Tool: Bash (curl)
    Preconditions: Tasks 9, 10, 11 complete, seed data loaded
    Steps:
      1. docker compose exec api flask seed-demo-data
      2. curl -s http://localhost:5001/api/myownclone/public/clones/demo-clone | head -c 200
      3. curl -s -X POST http://localhost:5001/api/myownclone/public/clones/demo-clone/chat-simple -H "Content-Type: application/json" -d '{"message":"hello","mode":"teach"}' | head -c 200
      4. curl -s http://localhost:5001/api/myownclone/public/clones/demo-clone/meeting-types | head -c 200
      5. curl -s -X POST http://localhost:5001/api/myownclone/public/clones/demo-clone/bookings -H "Content-Type: application/json" -d '{}' | head -c 200
    Expected Result: All return JSON (not 404), even error responses prove endpoint exists
    Failure Indicators: Any 404 Not Found response means blueprint still not registered
    Evidence: .sisyphus/evidence/task-12-endpoints-verified.txt
  ```

  **Commit**: NO (verification only)

---

## Final Verification Wave (MANDATORY — after ALL implementation tasks)

> 4 review agents run in PARALLEL. ALL must APPROVE. Present consolidated results to user and get explicit "okay" before completing.
>
> **Do NOT auto-proceed after verification. Wait for user's explicit approval before marking work complete.**

- [x] F1. **Plan Compliance Audit** — `oracle`
  Read the plan end-to-end. For each "Must Have": verify implementation exists (read file, curl endpoint, run command). For each "Must NOT Have": search codebase for forbidden patterns — reject with file:line if found. Check evidence files exist in .sisyphus/evidence/. Compare deliverables against plan.
  Output: `Must Have [N/N] | Must NOT Have [N/N] | Tasks [N/N] | VERDICT: APPROVE/REJECT`

- [x] F2. **Code Quality Review** — `unspecified-high`
  Run `tsc --noEmit` + linter + `npm run build` for frontend. Python: check for `as any`/`@ts-ignore`, empty catches, console.log in prod, commented-out code, unused imports. Check AI slop: excessive comments, over-abstraction, generic names (data/result/item/temp).
  Output: `Build [PASS/FAIL] | Lint [PASS/FAIL] | Tests [N pass/N fail] | Files [N clean/N issues] | VERDICT`

- [x] F3. **Real Manual QA** — `unspecified-high` (+ `playwright` skill if UI)
  Start from clean state. Execute EVERY QA scenario from EVERY task — follow exact steps, capture evidence. Test cross-task integration (features working together, not isolation). Test edge cases: empty state, invalid input, rapid actions. Save to `.sisyphus/evidence/final-qa/`.
  Output: `Scenarios [N/N pass] | Integration [N/N] | Edge Cases [N tested] | VERDICT`

- [x] F4. **Scope Fidelity Check** — `deep`
  For each task: read "What to do", read actual diff (git log/diff). Verify 1:1 — everything in spec was built (no missing), nothing beyond spec was built (no creep). Check "Must NOT do" compliance. Detect cross-task contamination: Task N touching Task M's files. Flag unaccounted changes.
  Output: `Tasks [N/N compliant] | Contamination [CLEAN/N issues] | Unaccounted [CLEAN/N files] | VERDICT`

---

## Commit Strategy

- **Task 1**: `fix(api): call register_myownclone_blueprints() at app startup` — api/api/app_factory.py
- **Task 2**: `fix(api): capture return value from _add_memories_to_prompt()` — api/api/controllers/myownclone_public.py
- **Task 3**: `fix(api): add warning log when tenant lookup fails in admin` — api/api/controllers/console/myownclone/admin_platform.py
- **Task 4**: `docs(api): add .env.example with all environment variables` — api/.env.example
- **Task 5**: `refactor(frontend): rename (clonify) route group to (public)` — replica/src/app/(clonify) → (public)
- **Task 6**: `refactor(frontend): rename ClonifyLayout to YouOwnCloneLayout` — replica/src/app/(public)/layout.tsx
- **Task 7**: `refactor(frontend): update metadata to YouOwnClone branding` — replica/src/app/(public)/layout.tsx
- **Task 11**: `feat(api): add flask seed-demo-data command for testing` — New file in api/

---

## Success Criteria

### Verification Commands
```bash
# Docker stack
cd api && docker compose up -d && docker compose ps

# DB migrations
docker compose exec api flask db upgrade

# Seed data
docker compose exec api flask seed-demo-data

# Test public endpoint
curl http://localhost:5001/api/myownclone/public/clones/demo-clone

# Test chat-simple
curl -X POST http://localhost:5001/api/myownclone/public/clones/demo-clone/chat-simple \
  -H "Content-Type: application/json" \
  -d '{"message":"hello","mode":"teach"}'

# Frontend build
cd replica && npm run build
```

### Final Checklist
- [ ] All "Must Have" present
- [ ] All "Must NOT Have" absent
- [ ] All 6 public endpoints return non-404
- [ ] Docker stack runs without errors
- [ ] Seed command creates demo data
- [ ] No references to "Clonify" in active code
- [ ] Metadata says "YouOwnClone"
- [ ] `(public)` route group exists, `(clonify)` does not