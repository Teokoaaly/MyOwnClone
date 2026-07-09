"""Runtime integration endpoints for configurable AI services."""

from __future__ import annotations

import logging

from flask import request
from flask_restx import Resource

from api.controllers.console import console_ns
from api.core.embeddings import EmbeddingService
from api.core.providers.base import ModelInvocationError
from api.core.stt import SpeechToTextService
from api.libs.login import current_account_with_tenant, login_required

logger = logging.getLogger(__name__)

# Defect #6: bound the number of texts accepted in a single embeddings request.
_MAX_EMBED_TEXTS = 256


def _check_rate_limit(endpoint: str, limit: int = 30, window: int = 60) -> tuple[bool, int | None]:
    """Check rate limit for console endpoints. Returns (allowed, retry_after)."""
    try:
        from api.core.rate_limit import check_rate_limit, RateLimitConfig, RateLimitKeyType
        from api.libs.login import current_account_with_tenant
        _, tenant_id = current_account_with_tenant()
        identifier = tenant_id or request.remote_addr or "unknown"
        config = RateLimitConfig(limit=limit, window_seconds=window)
        allowed, remaining, reset_time = check_rate_limit(
            identifier=identifier,
            endpoint=endpoint,
            key_type=RateLimitKeyType.AUTHENTICATED,
            config=config,
        )
        return allowed, reset_time
    except Exception:
        return True, None


@console_ns.route("/myownclone/embeddings")
class RuntimeEmbeddingsApi(Resource):
    @login_required
    def post(self):
        allowed, retry_after = _check_rate_limit("embeddings", limit=20, window=60)
        if not allowed:
            return {"error": "rate limit exceeded", "retry_after": retry_after}, 429

        _account, tenant_id = current_account_with_tenant()
        payload = request.get_json(silent=True) or {}
        texts = payload.get("texts") or []
        if not isinstance(texts, list) or not texts or not all(isinstance(text, str) for text in texts):
            return {"error": "texts must be a non-empty list of strings"}, 400

        if len(texts) > _MAX_EMBED_TEXTS:
            logger.warning(
                "Embeddings request rejected: %d texts exceeds limit %d (tenant=%s)",
                len(texts),
                _MAX_EMBED_TEXTS,
                tenant_id,
            )
            return {
                "error": f"too many texts: {len(texts)} > {_MAX_EMBED_TEXTS}",
                "max_texts": _MAX_EMBED_TEXTS,
            }, 413

        try:
            vectors = EmbeddingService().embed_texts(texts, tenant_id=tenant_id)
        except (ModelInvocationError, ValueError) as exc:
            logger.exception(
                "Embeddings request failed (tenant=%s, count=%d)", tenant_id, len(texts)
            )
            return {"error": str(exc)}, 422

        return {
            "vectors": vectors,
            "count": len(vectors),
            "tenant_id": tenant_id,
        }, 200


@console_ns.route("/myownclone/stt/transcribe")
class RuntimeSpeechToTextApi(Resource):
    @login_required
    def post(self):
        allowed, retry_after = _check_rate_limit("stt", limit=10, window=60)
        if not allowed:
            return {"error": "rate limit exceeded", "retry_after": retry_after}, 429

        _account, tenant_id = current_account_with_tenant()
        audio = request.files.get("audio")
        if audio is None:
            return {"error": "audio is required"}, 400

        try:
            text = SpeechToTextService().transcribe(
                tenant_id=tenant_id,
                audio_bytes=audio.read(),
                filename=audio.filename or "audio.webm",
                content_type=audio.mimetype,
                language=request.form.get("language") or "es",
            )
        except ModelInvocationError as exc:
            return {"error": str(exc)}, 422

        return {"text": text}, 200
