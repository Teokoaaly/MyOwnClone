# Audit Remediation - Base Platform Import Investigation

## Investigation Date: 2026-06-03

## 1. FILES FOUND

### Existing base platform files:
- `api/api/core/__init__.py` - EXISTS
- `api/api/core/silos.py` - EXISTS
- `api/api/core/retrieval.py` - EXISTS
- `api/api/core/ingestion.py` - EXISTS
- `api/api/core/email_processor.py` - EXISTS
- `api/api/core/email_ai.py` - EXISTS

### Files NOT FOUND (MISSING from base platform):
- `libs/login.py` - MISSING
- `libs/datetime_utils.py` - MISSING
- `libs/uuid_utils.py` - MISSING
- `fields/base.py` - MISSING
- `configs/` directory - MISSING
- `core/model_manager.py` - MISSING
- `core/rag/` directory - MISSING
- `graphon/` directory - MISSING
- `models/account.py` - NOT IMPORTED (not found in search)
- `models/model.py` - NOT IMPORTED (not found in search)

---

## 2. IMPORT MAP

### A. Imports from `core.myownclone.*` (INTERNAL - work correctly)
Files in `api/api/core/` are imported as `core.myownclone.*`:

| File | Import |
|------|--------|
| `core/__init__.py` | `from core.myownclone.email_ai import classify_email, generate_draft_reply` |
| `core/__init__.py` | `from core.myownclone.email_processor import parse_inbound_email, resolve_clone_by_domain` |
| `core/__init__.py` | `from core.myownclone.ingestion import IngestionMetadata` |
| `core/__init__.py` | `from core.myownclone.retrieval import SiloRetrievalResult, retrieve_from_silo` |
| `core/__init__.py` | `from core.myownclone.silos import CloneSilo, dataset_name_for_silo, filter_segments_by_context, get_dataset_id_for_silo, silo_from_dataset_name` |
| `core/retrieval.py` | `from core.myownclone.silos import CloneSilo, filter_segments_by_context, get_dataset_id_for_silo` |
| `core/ingestion.py` | `from core.myownclone.silos import CloneSilo, dataset_name_for_silo` |
| `controllers/myownclone_public.py` | `from core.myownclone.email_ai import _get_clone_context, classify_email, generate_draft_reply` |
| `controllers/myownclone_public.py` | `from core.myownclone.email_processor import parse_inbound_email, resolve_clone_by_domain` |
| `controllers/myownclone_public.py` | `from core.myownclone.retrieval import retrieve_from_silo` |
| `controllers/myownclone_public.py` | `from core.myownclone.silos import CloneSilo` |
| `controllers/console/myownclone/inbox.py` | `from core.myownclone.email_ai import _get_clone_context, classify_email, generate_draft_reply` |
| `controllers/console/myownclone/inbox.py` | `from core.myownclone.email_processor import parse_inbound_email, resolve_clone_by_domain` |

### B. Imports from `core.rag.*` (MISSING - external base platform)

| File | Import | Status |
|------|--------|--------|
| `core/retrieval.py` | `from core.rag.datasource.retrieval_service import RetrievalService` | MISSING |
| `core/retrieval.py` | `from core.rag.retrieval.retrieval_methods import RetrievalMethod` | MISSING |
| `controllers/myownclone_public.py` | `from core.rag.retrieval.retrieval_methods import RetrievalMethod` | MISSING |

### C. Imports from `libs.*` (MISSING - external base platform)

| File | Import | Status |
|------|--------|--------|
| `models/meeting.py` | `from libs.datetime_utils import naive_utc_now` | MISSING |
| `models/meeting.py` | `from libs.uuid_utils import uuidv7` | MISSING |
| `models/email.py` | `from libs.datetime_utils import naive_utc_now` | MISSING |
| `models/email.py` | `from libs.uuid_utils import uuidv7` | MISSING |
| `models/clone.py` | `from libs.datetime_utils import naive_utc_now` | MISSING |
| `models/clone.py` | `from libs.uuid_utils import uuidv7` | MISSING |
| `models/analytics.py` | `from libs.datetime_utils import naive_utc_now` | MISSING |
| `models/analytics.py` | `from libs.uuid_utils import uuidv7` | MISSING |
| `controllers/console/myownclone/clone.py` | `from libs.login import current_account_with_tenant, login_required` | MISSING |
| `controllers/console/myownclone/booking.py` | `from libs.login import current_account_with_tenant, login_required` | MISSING |
| `controllers/console/myownclone/analytics.py` | `from libs.login import current_account_with_tenant, login_required` | MISSING |
| `controllers/console/myownclone/admin_platform.py` | `from libs.login import current_account_with_tenant, login_required` | MISSING |
| `controllers/console/myownclone/inbox.py` | `from libs.login import current_account_with_tenant, login_required` | MISSING |
| `controllers/console/myownclone/feedback.py` | `from libs.login import current_account_with_tenant, login_required` | MISSING |
| `controllers/console/myownclone/creator_memory.py` | `from libs.login import current_account_with_tenant, login_required` | MISSING |
| `controllers/console/myownclone/stripe_ctrl.py` | `from libs.login import current_account_with_tenant, login_required` | MISSING |

### D. Imports from `fields.*` (MISSING - external base platform)

| File | Import | Status |
|------|--------|--------|
| `controllers/console/myownclone/clone.py` | `from fields.base import ResponseModel` | MISSING |
| `controllers/console/myownclone/analytics.py` | `from fields.base import ResponseModel` | MISSING |
| `controllers/console/myownclone/inbox.py` | `from fields.base import ResponseModel` | MISSING |
| `controllers/console/myownclone/creator_memory.py` | `from fields.base import ResponseModel` | MISSING |

### E. Imports from `core.model_manager` (MISSING - external base platform)

| File | Import | Status |
|------|--------|--------|
| `controllers/myownclone_public.py` | `from core.model_manager import ModelManager` | MISSING |
| `controllers/console/myownclone/inbox.py` | `from core.model_manager import ModelManager` | MISSING |

### F. Imports from `graphon.*` (MISSING - external base platform)

| File | Import | Status |
|------|--------|--------|
| `controllers/myownclone_public.py` | `from graphon.model_runtime.entities.model_entities import ModelType` | MISSING |
| `controllers/console/myownclone/inbox.py` | `from graphon.model_runtime.entities.model_entities import ModelType` | MISSING |

---

## 3. SUMMARY: MISSING FILES

| Missing Module | Files That Import It | Count |
|----------------|---------------------|-------|
| `libs.datetime_utils` | models/* | 4 |
| `libs.uuid_utils` | models/* | 4 |
| `libs.login` | controllers/console/myownclone/* | 7 |
| `fields.base` | controllers/console/myownclone/* | 4 |
| `core.model_manager` | controllers/* | 2 |
| `graphon.model_runtime.entities.model_entities` | controllers/* | 2 |
| `core.rag.datasource.retrieval_service` | core/retrieval.py | 1 |
| `core.rag.retrieval.retrieval_methods` | core/retrieval.py, controllers/* | 2 |

---

## 4. RECOMMENDATION

**Action: CREATE PLACEHOLDERS** for the following missing base platform modules:

1. `api/api/libs/login.py` - login_required, current_account_with_tenant
2. `api/api/libs/datetime_utils.py` - naive_utc_now
3. `api/api/libs/uuid_utils.py` - uuidv7
4. `api/api/fields/base.py` - ResponseModel
5. `api/api/core/model_manager.py` - ModelManager
6. `api/api/graphon/model_runtime/entities/model_entities.py` - ModelType
7. `api/api/core/rag/datasource/retrieval_service.py` - RetrievalService
8. `api/api/core/rag/retrieval/retrieval_methods.py` - RetrievalMethod

The `core.myownclone.*` imports work correctly because the files exist in `api/api/core/*.py`.

---

## 5. NOTES

- The `core/__init__.py` uses `core.myownclone.*` imports even though the actual files are at `api/api/core/*.py`. This works because `core/` is the package and `myownclone` is a subpackage that doesn't exist - but somehow the imports still work? Need to verify this import path resolution.