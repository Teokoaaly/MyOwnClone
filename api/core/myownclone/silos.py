"""Silo-aware dataset manager for the MyOwnClone RAG pipeline.

Each clone maps to 3 datasets (one per silo: teach, support, sales).
This module manages the mapping, naming convention, and dataset resolution.

The naming convention is:  clone_{clone_id}_{silo}

When a user uploads content to a silo, it goes to the corresponding dataset.
Retrieval selects the correct dataset based on the active silo.

Context filtering (context_id) is implemented as metadata on document segments,
applied as a post-retrieval filter rather than altering the base platform core.

Per TASK-C02: the legacy Dataset/DocumentSegment models are stubs in this
repo. When they are present and functional we use them; otherwise retrieval
falls back to the local_hybrid_v1 source/chunk path (see api/core/retrieval.py).
This module detects stub models defensively and returns None so the caller
treats it as "no legacy dataset available" instead of crashing.
"""

import logging

from sqlalchemy import select
from sqlalchemy.orm import Session

from api.models.myownclone.clone import CloneSilo

logger = logging.getLogger(__name__)


def _import_dataset_models():
    """Import legacy Dataset/DocumentSegment. Returns (Dataset, DocumentSegment)
    or (None, None) if the stub models are too incomplete to use."""
    try:
        from api.models.dataset import Dataset, DocumentSegment
    except Exception:
        logger.exception("Failed to import legacy Dataset/DocumentSegment models")
        return None, None

    required_dataset = ("id", "tenant_id", "name")
    required_segment = ("id", "tenant_id", "doc_metadata")
    for attr in required_dataset:
        if not hasattr(Dataset, attr):
            return None, None
    for attr in required_segment:
        if not hasattr(DocumentSegment, attr):
            return None, None
    return Dataset, DocumentSegment


DATASET_NAME_TEMPLATE = "clone_{clone_id}_{silo}"


def dataset_name_for_silo(clone_id: str, silo: CloneSilo) -> str:
    return DATASET_NAME_TEMPLATE.format(clone_id=clone_id, silo=silo.value)


def silo_from_dataset_name(name: str) -> CloneSilo | None:
    for silo in CloneSilo:
        if name.endswith(f"_{silo.value}"):
            return silo
    return None


def get_dataset_id_for_silo(
    session: Session,
    tenant_id: str,
    clone_id: str,
    silo: CloneSilo,
) -> str | None:
    Dataset, _ = _import_dataset_models()
    if Dataset is None:
        # Legacy dataset model is a stub. Local chunks are the only source
        # of truth (TASK-C02). Treat as "no legacy dataset".
        return None

    name = dataset_name_for_silo(clone_id, silo)
    try:
        stmt = select(Dataset.id).where(
            Dataset.tenant_id == tenant_id,
            Dataset.name == name,
        )
        result = session.execute(stmt).scalar_one_or_none()
        return result
    except Exception:
        logger.warning(
            "Dataset resolution failed for clone=%s silo=%s tenant=%s; "
            "falling back to local chunks only",
            clone_id,
            silo.value,
            tenant_id,
        )
        return None


def filter_segments_by_context(
    session: Session,
    segment_ids: list[str],
    context_id: str,
    tenant_id: str,
) -> list[str]:
    """Post-retrieval filter: keep only segments whose doc_metadata contains the context_id."""
    if not segment_ids:
        return []

    _, DocumentSegment = _import_dataset_models()
    if DocumentSegment is None:
        return list(segment_ids)

    try:
        stmt = select(DocumentSegment.id).where(
            DocumentSegment.id.in_(segment_ids),
            DocumentSegment.tenant_id == tenant_id,
            DocumentSegment.doc_metadata["context_id"].astext == context_id,
        )
        rows = session.execute(stmt).fetchall()
        return [row[0] for row in rows]
    except Exception:
        logger.warning(
            "Context filtering failed for tenant=%s context=%s; returning unfiltered",
            tenant_id,
            context_id,
        )
        return list(segment_ids)
