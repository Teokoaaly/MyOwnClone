# api/ (root) — Dead Code Audit

**Date:** 2026-06-07
**Auditor:** sisyphus orchestrator

## Conclusion

**DEAD CODE — safe to remove in future PR**

The `api/` (root) directory is an empty parent directory that contains only the live `api/api/` subdirectory. It has no `__init__.py`, no setup files, no `MANIFEST.in`, no `setup.cfg`, and no external references from outside the `api/api/` tree.

## Directory Listing

```
api/                          # ← ROOT: empty parent directory (DEAD)
  api/                        # ← LIVE package (DO NOT TOUCH)
    __init__.py
    app_factory.py
    base.py
    db_types.py
    pytest.ini
    requirements.txt
    commands/
    configs/
    controllers/
    core/
    extensions/
    fields/
    libs/
    migrations/
    models/
    tests/
```

The `api/` root has no `__init__.py`, `setup.py`, `pyproject.toml`, `MANIFEST.in`, or `setup.cfg`.

## Grep Results

### `grep -rE "from api\.|^import api\b" . --include="*.py" --exclude-dir=api`

All hits are within `api/api/` (the live package). None reference `api/` root:

```
api/api/extensions/__init__.py:3: from api.extensions.ext_database import db
api/api/commands/seed.py:6: from api.extensions import db
api/api/commands/seed.py:7: from api.models.myownclone import CloneConfig, MeetingType_, Availability
api/api/app_factory.py:18: from api.extensions import db
api/api/app_factory.py:19: from api.models import (
api/api/app_factory.py:34: from api.controllers.myownclone_public import myownclone_public_bp
api/api/app_factory.py:37: from api.controllers.console import bp as console_bp
api/api/app_factory.py:38: from api.controllers.console.auth import auth_bp
api/api/app_factory.py:41: from api.commands.seed import seed_demo_data
api/api/core/ingestion.py:12: from api.core.myownclone.silos import CloneSilo, dataset_name_for_silo
api/api/core/email_processor.py:21: from api.extensions.ext_database import db
api/api/core/email_processor.py:22: from api.models.myownclone import CloneConfig, EmailInbound, EmailInboundStatus
api/api/core/email_processor.py:23: from api.models.myownclone.clone import CloneSilo
api/api/models/__init__.py:3: Controllers import from api.models and api.models.myownclone.*
api/api/models/__init__.py:5: from api.models.analytics import (
api/api/models/__init__.py:9: from api.models.clone import (
api/api/models/__init__.py:13: from api.models.email import EmailInbound, EmailInboundStatus, EmailTemplate
api/api/models/__init__.py:14: from api.models.meeting import (
api/api/models/myownclone/__init__.py:1: """Re-export from parent for 'from api.models.myownclone import X' compatibility."""
api/api/models/myownclone/__init__.py:2: from api.models import (
... (more internal references within api/api/)
```

### `grep -rE "import api" . --include="*.py" --exclude-dir=api`

**No matches found.**

### `grep -rE "from api\." . --include="*.py" --exclude-dir=api`

All hits are within `api/api/` (the live package), using relative imports within the package. Zero external references.

## References Found

None. The `api/` root is not referenced by anything outside `api/api/`.

## Safe Removal Procedure (DEAD CODE — safe to remove)

1. Confirm 0 references via grep (DONE — verified above)
2. `git rm -r api/` — remove the empty parent directory only (NOT `api/api/`)
3. Run `python -m pytest` and `npm run build` to verify nothing breaks
4. Commit as `chore: remove dead api/ (root) tree — empty parent dir`

## Evidence Files

- `.sisyphus/evidence/b-1-grep.txt` — full grep output
- `.sisyphus/evidence/b-1-dead-code-md.txt` — this file