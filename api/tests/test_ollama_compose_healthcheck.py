"""Regression coverage for the production Ollama container probe."""

from pathlib import Path


COMPOSE_PATH = Path(__file__).resolve().parents[2] / "ops" / "docker-compose.backend.prod.yml"


def test_production_ollama_service_has_a_healthcheck() -> None:
    """The model service remains independently observable by Compose."""
    compose = COMPOSE_PATH.read_text(encoding="utf-8")

    assert "ollama:" in compose
    assert "healthcheck:" in compose


def test_production_ollama_healthcheck_uses_native_cli_not_curl() -> None:
    """The stock Ollama image need not include curl for its own probe."""
    compose = COMPOSE_PATH.read_text(encoding="utf-8")

    assert 'test: ["CMD", "ollama", "list"]' in compose
    assert (
        'test: ["CMD-SHELL", "curl -fsS '
        'http://localhost:11434/api/tags >/dev/null || exit 1"]'
    ) not in compose
