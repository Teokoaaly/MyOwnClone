"""Clonify core module — silo-aware RAG, email triage, clone management.

Extends Dify without modifying core. All Clonify-specific logic lives here.
"""

from core.myownclone.email_ai import classify_email, generate_draft_reply
from core.myownclone.email_processor import parse_inbound_email, resolve_clone_by_domain
from core.myownclone.ingestion import IngestionMetadata
from core.myownclone.retrieval import SiloRetrievalResult, retrieve_from_silo
from core.myownclone.silos import CloneSilo, dataset_name_for_silo, filter_segments_by_context, get_dataset_id_for_silo, silo_from_dataset_name

__all__ = [
    "CloneSilo",
    "IngestionMetadata",
    "SiloRetrievalResult",
    "classify_email",
    "dataset_name_for_silo",
    "filter_segments_by_context",
    "generate_draft_reply",
    "get_dataset_id_for_silo",
    "parse_inbound_email",
    "resolve_clone_by_domain",
    "retrieve_from_silo",
    "silo_from_dataset_name",
]
