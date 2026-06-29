from __future__ import annotations

from types import SimpleNamespace

from api.core.myownclone.silos import CloneSilo
from api.core.retrieval import _retrieve_from_local_chunks


def _row(*, content: str, embedding: list[float] | None, silo: str = "teach"):
    chunk = SimpleNamespace(
        id="chunk-1",
        content=content,
        embedding=embedding,
        chunk_metadata={},
    )
    source = SimpleNamespace(
        id="source-1",
        clone_id="clone-1",
        status="ready",
        title="Source",
        source_metadata={"silo": silo},
    )
    return (chunk, source)


class _FakeSession:
    def __init__(self, rows):
        self._rows = rows

    def execute(self, _stmt):
        return SimpleNamespace(all=lambda: list(self._rows))


def test_local_chunk_retrieval_uses_semantic_query_embedding(monkeypatch):
    def fake_embed_texts(self, texts, *, tenant_id=None, model=None):
        assert texts == ["hello world"]
        assert tenant_id == "tenant-1"
        return [[1.0, 0.0, 0.0]]

    monkeypatch.setattr("api.core.retrieval.EmbeddingService.embed_texts", fake_embed_texts)

    result = _retrieve_from_local_chunks(
        session=_FakeSession([_row(content="nada parecido", embedding=[1.0, 0.0, 0.0])]),
        tenant_id="tenant-1",
        clone_id="clone-1",
        query="hello world",
        silo=CloneSilo.TEACH,
        context_id=None,
        top_k=5,
        score_threshold=0.7,
    )

    assert result.found is True
    assert result.segments[0].metadata["vector_score"] == 1.0


def test_local_chunk_retrieval_falls_back_to_lexical_embedding(monkeypatch):
    def boom(self, texts, *, tenant_id=None, model=None):
        raise RuntimeError("embedding provider unavailable")

    monkeypatch.setattr("api.core.retrieval.EmbeddingService.embed_texts", boom)

    result = _retrieve_from_local_chunks(
        session=_FakeSession([_row(content="hello world pricing", embedding=[1.0, 0.0, 0.0])]),
        tenant_id="tenant-1",
        clone_id="clone-1",
        query="hello world",
        silo=CloneSilo.TEACH,
        context_id=None,
        top_k=5,
        score_threshold=0.2,
    )

    assert result.found is True
    assert result.segments[0].metadata["term_score"] > 0.0
