"""myownclone core — silos, retrieval, ingestion, email_ai, email_processor."""

from core.myownclone.email_ai import (
    ClassificationResult,
    DRAFT_PROMPT,
    DraftResult,
    classify_email,
    generate_draft_reply,
)
from core.myownclone.email_processor import (
    ParsedEmail,
    parse_inbound_email,
    resolve_clone_by_domain,
)
from core.myownclone.ingestion import IngestionMetadata
from core.myownclone.retrieval import SiloRetrievalResult, retrieve_from_silo
from core.myownclone.silos import (
    CloneSilo,
    DATASET_NAME_TEMPLATE,
    dataset_name_for_silo,
    filter_segments_by_context,
    get_dataset_id_for_silo,
    silo_from_dataset_name,
)

__all__ = [
    "CloneSilo",
    "DATASET_NAME_TEMPLATE",
    "dataset_name_for_silo",
    "silo_from_dataset_name",
    "get_dataset_id_for_silo",
    "filter_segments_by_context",
    "SiloRetrievalResult",
    "retrieve_from_silo",
    "IngestionMetadata",
    "ParsedEmail",
    "parse_inbound_email",
    "resolve_clone_by_domain",
    "ClassificationResult",
    "DraftResult",
    "CLASSIFICATION_PROMPT",
    "DRAFT_PROMPT",
    "classify_email",
    "generate_draft_reply",
]