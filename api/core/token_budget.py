"""TokenBudgeter: estimate tokens + truncate context to fit budget.

Uses gpt-tokenizer (cl100k_base encoding) as a cross-model approximation.
Errors of 5-15% are expected for non-GPT models; we leave a 10% margin.

Also provides DimensionGuard: validates embedding dimensions match across
Postgres (information_schema) and Weaviate (schema endpoint).
"""
from __future__ import annotations
import os
from typing import Optional
from dataclasses import dataclass

try:
    import tiktoken
    _HAS_TIKTOKEN = True
except ImportError:
    _HAS_TIKTOKEN = False

try:
    from gpt_tokenizer import Tokenizer
    _HAS_GPT_TOKENIZER = True
except ImportError:
    _HAS_GPT_TOKENIZER = False


DEFAULT_SAFETY_MARGIN = 0.10  # 10% margin for cross-model tokenization error
DEFAULT_CHARS_PER_TOKEN = 4  # rough fallback estimate


def _get_tokenizer():
    """Get a tokenizer (gpt-tokenizer preferred, tiktoken fallback)."""
    if _HAS_GPT_TOKENIZER:
        return GptTokenizerWrapper()
    if _HAS_TIKTOKEN:
        return TiktokenWrapper()
    return FallbackTokenizer()


@dataclass
class TokenEstimate:
    tokens: int
    method: str  # "gpt-tokenizer", "tiktoken", "fallback"
    char_count: int


class _TokenizerBase:
    def count(self, text: str) -> TokenEstimate:
        raise NotImplementedError


class GptTokenizerWrapper(_TokenizerBase):
    def __init__(self):
        self._tok = Tokenizer()
    
    def count(self, text: str) -> TokenEstimate:
        n = len(self._tok.encode(text))
        return TokenEstimate(tokens=n, method="gpt-tokenizer", char_count=len(text))


class TiktokenWrapper(_TokenizerBase):
    def __init__(self):
        self._enc = tiktoken.get_encoding("cl100k_base")
    
    def count(self, text: str) -> TokenEstimate:
        n = len(self._enc.encode(text))
        return TokenEstimate(tokens=n, method="tiktoken", char_count=len(text))


class FallbackTokenizer(_TokenizerBase):
    def count(self, text: str) -> TokenEstimate:
        # ~4 chars per token is the rough rule for English
        n = max(1, len(text) // DEFAULT_CHARS_PER_TOKEN)
        return TokenEstimate(tokens=n, method="fallback", char_count=len(text))


class TokenBudgeter:
    """Count tokens and truncate context to fit a model budget.
    
    Applies a 10% safety margin for cross-model tokenization error.
    """
    
    def __init__(
        self,
        safety_margin: float = DEFAULT_SAFETY_MARGIN,
        tokenizer: Optional[_TokenizerBase] = None,
    ):
        self.safety_margin = safety_margin
        self._tokenizer = tokenizer or _get_tokenizer()
    
    def count(self, text: str) -> int:
        return self._tokenizer.count(text).tokens
    
    def estimate(self, text: str) -> TokenEstimate:
        return self._tokenizer.count(text)
    
    def effective_budget(self, model_max_tokens: int) -> int:
        """Return usable budget after safety margin."""
        return int(model_max_tokens * (1 - self.safety_margin))
    
    def truncate_to_budget(
        self,
        text: str,
        model_max_tokens: int,
    ) -> str:
        """Truncate text to fit within effective budget. May lose content from end."""
        effective = self.effective_budget(model_max_tokens)
        est = self._tokenizer.count(text)
        if est.tokens <= effective:
            return text
        # Binary search for the right cutoff by characters
        # (approximate: assume token count is roughly linear with chars)
        ratio = effective / est.tokens
        target_chars = max(1, int(est.char_count * ratio * 0.95))  # 5% extra margin
        return text[:target_chars]
    
    def fit_chunks(
        self,
        chunks: list[str],
        model_max_tokens: int,
    ) -> list[str]:
        """Greedily pack chunks into the budget. Returns kept chunks in order."""
        effective = self.effective_budget(model_max_tokens)
        kept: list[str] = []
        used = 0
        for chunk in chunks:
            n = self.count(chunk)
            if used + n > effective:
                # Try to truncate the last chunk to fit
                remaining = effective - used
                # Only truncate if at least 10% of the chunk would survive
                if remaining >= n * 0.1:
                    kept.append(self.truncate_to_budget(chunk, remaining))
                break
            kept.append(chunk)
            used += n
        return kept


# ---------- Dimension Guard ----------

class DimensionMismatchError(Exception):
    """Raised when AIModel.embedding_dimensions doesn't match the actual store."""
    def __init__(self, message: str, *, expected: int, actual: int, store: str):
        super().__init__(message)
        self.expected = expected
        self.actual = actual
        self.store = store


class DimensionGuard:
    """Validate that AIModel.embedding_dimensions matches the actual vector store.
    
    Two checks:
    1. Postgres: SELECT atttypmod FROM pg_attribute WHERE attrelid = 'chunks'::regclass AND attname = 'embedding';
       The result is the dimension N for vector(N).
    2. Weaviate: GET /v1/schema/{class_name} and inspect vectorIndexConfig.size or vectorizer.
    """
    
    DEFAULT_CHUNKS_TABLE = "chunks"
    
    def __init__(self, *, expected_dim: int, store: str = "postgres"):
        self.expected_dim = expected_dim
        self.store = store
    
    def check_postgres(self, session, table_name: str = DEFAULT_CHUNKS_TABLE) -> None:
        """Verify Postgres vector column has the expected dimension.
        
        Uses raw SQL via session.execute() with bind params.
        Returns silently if OK; raises DimensionMismatchError otherwise.
        """
        from sqlalchemy import text
        sql = text("""
            SELECT atttypmod
            FROM pg_attribute
            WHERE attrelid = :table_name::regclass
              AND attname = 'embedding'
              AND attnum > 0
              AND NOT attisdropped
        """)
        row = session.execute(sql, {"table_name": table_name}).first()
        if row is None:
            raise DimensionMismatchError(
                f"No 'embedding' column found in Postgres table '{table_name}'",
                expected=self.expected_dim, actual=0, store="postgres",
            )
        actual_dim = int(row[0])
        if actual_dim != self.expected_dim:
            raise DimensionMismatchError(
                f"Postgres embedding dimension mismatch: expected {self.expected_dim}, got {actual_dim} in {table_name}.embedding",
                expected=self.expected_dim, actual=actual_dim, store="postgres",
            )
    
    def check_weaviate(self, weaviate_client, class_name: str) -> None:
        """Verify Weaviate class has the expected vector dimension.
        
        Uses client.schema.get(class_name) and inspects vectorIndexConfig.vectorSize
        (or vectorizer if it's a built-in model with known dimensions).
        """
        try:
            schema = weaviate_client.schema.get(class_name)
        except Exception as exc:
            raise DimensionMismatchError(
                f"Could not fetch Weaviate schema for {class_name!r}: {exc}",
                expected=self.expected_dim, actual=0, store="weaviate",
            )
        # Look for vectorIndexConfig.vectorSize (in newer Weaviate clients)
        vector_index = schema.get("vectorIndexConfig") or {}
        actual_dim = vector_index.get("size") or vector_index.get("vectorSize")
        if actual_dim is None:
            # Some Weaviate versions use different keys
            vectorizer = schema.get("vectorizer") or ""
            # Common built-in models
            known_dims = {
                "text2vec-openai": 1536,
                "text2vec-cohere": 4096,
                "text2vec-huggingface": 768,
            }
            for prefix, dim in known_dims.items():
                if vectorizer.startswith(prefix):
                    actual_dim = dim
                    break
        if actual_dim is None:
            raise DimensionMismatchError(
                f"Could not determine Weaviate vector dimension for class {class_name!r}",
                expected=self.expected_dim, actual=0, store="weaviate",
            )
        if int(actual_dim) != self.expected_dim:
            raise DimensionMismatchError(
                f"Weaviate embedding dimension mismatch: expected {self.expected_dim}, got {actual_dim} in {class_name!r}",
                expected=self.expected_dim, actual=int(actual_dim), store="weaviate",
            )
    
    def check_both(self, session, weaviate_client, class_name: str, table_name: str = DEFAULT_CHUNKS_TABLE) -> None:
        """Check both stores; raise on first mismatch with store name in error."""
        try:
            self.check_postgres(session, table_name)
        except DimensionMismatchError as e:
            raise
        self.check_weaviate(weaviate_client, class_name)
