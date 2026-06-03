"""Silo-aware dataset manager for the Clonify RAG pipeline.

Each clone maps to 3 Dify datasets (one per silo: teach, support, sales).
This module manages the mapping, naming convention, and dataset resolution.

The naming convention is:  clone_{clone_id}_{silo}

When a user uploads content to a silo, it goes to the corresponding Dify dataset.
Retrieval selects the correct dataset based on the active silo.

Context filtering (context_id) is implemented as metadata on document segments,
applied as a post-retrieval filter rather than modifying Dify core.
"""

import logging

from sqlalchemy import select
from sqlalchemy.orm import Session

from models.myownclone.clone import CloneSilo
from models.dataset import Dataset, DocumentSegment

logger = logging.getLogger(__name__)


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
    name = dataset_name_for_silo(clone_id, silo)
    stmt = select(Dataset.id).where(
        Dataset.tenant_id == tenant_id,
        Dataset.name == name,
    )
    result = session.execute(stmt).scalar_one_or_none()
    return result


def filter_segments_by_context(
    session: Session,
    segment_ids: list[str],
    context_id: str,
    tenant_id: str,
) -> list[str]:
    """Post-retrieval filter: keep only segments whose doc_metadata contains the context_id."""
    if not segment_ids:
        return []

    stmt = select(DocumentSegment.id).where(
        DocumentSegment.id.in_(segment_ids),
        DocumentSegment.tenant_id == tenant_id,
        DocumentSegment.doc_metadata["context_id"].astext == context_id,
    )
    rows = session.execute(stmt).fetchall()
    return [row[0] for row in rows]
