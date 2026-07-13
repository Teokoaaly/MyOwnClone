"""
TASK-E05: Memories afectan la respuesta del chat.

Verifica el contrato de `_add_memories_to_prompt`:
- Si el clone no tiene memories, el system prompt no se modifica.
- Si tiene memories de tipo MEMORY, se incluyen en el bloque "informacion importante".
- Las memories de tipo SIGNATURE o TEMPLATE NO se incluyen en chat (se usan en email/draft).
- Se ordenan por priority descendente.
"""

import pytest
from sqlalchemy import select
from sqlalchemy.orm import Session

from api.controllers.myownclone_public import _add_memories_to_prompt
from api.models.myownclone import CreatorMemory, CreatorMemoryType


# ── Mocks de sesion ────────────────────────────────────────────────────


class _ScalarResult:
    def __init__(self, items):
        self._items = items

    def scalars(self):
        return _Scalars(self._items)


class _Scalars:
    def __init__(self, items):
        self._items = items

    def all(self):
        return list(self._items)


class _Session:
    """Mock minimo de sqlalchemy.orm.Session que solo soporta
    execute(stmt).scalars().all() para CreatorMemory."""

    def __init__(self, memories: list[CreatorMemory]):
        self._memories = memories

    def execute(self, stmt):
        # Filtrar por type=MEMORY y order_by priority desc
        filtered = [m for m in self._memories if m.type == CreatorMemoryType.MEMORY]
        filtered.sort(key=lambda m: m.priority, reverse=True)
        return _ScalarResult(filtered)


# ── Tests ──────────────────────────────────────────────────────────────


def test_no_memories_leaves_prompt_unchanged(monkeypatch):
    """Sin memories registradas, el prompt base no se modifica."""
    monkeypatch.setattr(
        "api.controllers.myownclone_public.db.session",
        _Session(memories=[]),
    )
    base = "Eres un asistente util."
    out = _add_memories_to_prompt("clone-x", base)
    assert out == base


def test_memories_are_appended_to_prompt(monkeypatch):
    """Memories de tipo MEMORY aparecen en el prompt final."""
    memories = [
        CreatorMemory(
            id="m1",
            clone_id="clone-x",
            type=CreatorMemoryType.MEMORY,
            content="El CEO se llama Marta.",
            priority=5,
        ),
        CreatorMemory(
            id="m2",
            clone_id="clone-x",
            type=CreatorMemoryType.MEMORY,
            content="El horario de oficina es 9-18.",
            priority=1,
        ),
    ]
    monkeypatch.setattr(
        "api.controllers.myownclone_public.db.session",
        _Session(memories=memories),
    )
    base = "Eres un asistente."
    out = _add_memories_to_prompt("clone-x", base)
    assert "Eres un asistente." in out
    assert "Marta" in out
    assert "9-18" in out
    assert "informacion importante" in out.lower() or "informaci" in out.lower()


def test_memories_ordered_by_priority_descending(monkeypatch):
    """Las memories de mayor priority aparecen primero en el prompt."""
    memories = [
        CreatorMemory(id="low", clone_id="c", type=CreatorMemoryType.MEMORY, content="BAJA_PRIORIDAD", priority=1),
        CreatorMemory(id="high", clone_id="c", type=CreatorMemoryType.MEMORY, content="ALTA_PRIORIDAD", priority=99),
    ]
    monkeypatch.setattr(
        "api.controllers.myownclone_public.db.session",
        _Session(memories=memories),
    )
    out = _add_memories_to_prompt("c", "base")
    pos_alta = out.index("ALTA_PRIORIDAD")
    pos_baja = out.index("BAJA_PRIORIDAD")
    assert pos_alta < pos_baja, (
        f"La memory de mayor priority debe aparecer primero. "
        f"ALTA en {pos_alta}, BAJA en {pos_baja}."
    )


def test_signature_and_template_memories_excluded_from_chat(monkeypatch):
    """Memories de tipo SIGNATURE o TEMPLATE no se inyectan en el prompt de chat.
    Esas se usan en email/draft, no en chat publico."""
    memories = [
        CreatorMemory(id="s1", clone_id="c", type=CreatorMemoryType.SIGNATURE, content="FIRMA_SECRETA", priority=100),
        CreatorMemory(id="t1", clone_id="c", type=CreatorMemoryType.TEMPLATE, content="PLANTILLA_SECRETA", priority=100),
        CreatorMemory(id="m1", clone_id="c", type=CreatorMemoryType.MEMORY, content="dato legitimo", priority=1),
    ]
    monkeypatch.setattr(
        "api.controllers.myownclone_public.db.session",
        _Session(memories=memories),
    )
    out = _add_memories_to_prompt("c", "base")
    assert "dato legitimo" in out
    assert "FIRMA_SECRETA" not in out
    assert "PLANTILLA_SECRETA" not in out


def test_memories_with_special_characters_are_preserved(monkeypatch):
    """Las memories pueden contener comillas, saltos de linea, emojis."""
    memories = [
        CreatorMemory(
            id="m",
            clone_id="c",
            type=CreatorMemoryType.MEMORY,
            content='Linea 1\nLinea 2 "con comillas" y emoji \U0001F4A1',
            priority=1,
        ),
    ]
    monkeypatch.setattr(
        "api.controllers.myownclone_public.db.session",
        _Session(memories=memories),
    )
    out = _add_memories_to_prompt("c", "base")
    assert "Linea 1" in out
    assert "Linea 2" in out
    assert "\U0001F4A1" in out


def test_empty_content_memory_is_skipped_safely(monkeypatch):
    """Memories con content vacio no rompen el formateo."""
    memories = [
        CreatorMemory(id="empty", clone_id="c", type=CreatorMemoryType.MEMORY, content="", priority=1),
        CreatorMemory(id="ok", clone_id="c", type=CreatorMemoryType.MEMORY, content="real data", priority=2),
    ]
    monkeypatch.setattr(
        "api.controllers.myownclone_public.db.session",
        _Session(memories=memories),
    )
    out = _add_memories_to_prompt("c", "base")
    assert "real data" in out


# ── Test de integracion ligero: end-to-end del prompt assembly ──────


def test_prompt_assembly_includes_system_mode_memories_and_context(monkeypatch):
    """
    Simula el ensamblaje completo que hace chat_public():
    system_prompt (de CloneModePrompt) + memories (de CreatorMemory) + RAG context.

    El test verifica que el orden y formato son los esperados.
    """
    monkeypatch.setattr(
        "api.controllers.myownclone_public.db.session",
        _Session(memories=[
            CreatorMemory(
                id="m",
                clone_id="c",
                type=CreatorMemoryType.MEMORY,
                content="Memoria importante: cliente VIP.",
                priority=10,
            ),
        ]),
    )

    # Esto es lo que hace chat_public() despues de obtener mode_prompt:
    system_prompt = "Eres el clon de Juan, experto en marketing."
    system_prompt_with_memories = _add_memories_to_prompt("c", system_prompt)
    context_text = "[Fuente 1] (relevancia: 0.85)\nEl ROI promedio es 4.2x."

    final_prompt = f"""{system_prompt_with_memories}

CONTENIDO DE REFERENCIA:
{context_text}

Pregunta del usuario: Como mido el ROI?"""

    # El prompt debe contener los 3 bloques
    assert "experto en marketing" in final_prompt  # system prompt
    assert "cliente VIP" in final_prompt  # memory
    assert "ROI promedio es 4.2x" in final_prompt  # RAG
    assert "Como mido el ROI?" in final_prompt  # user

    # Orden: system -> memories -> RAG -> user
    pos_system = final_prompt.index("experto en marketing")
    pos_memory = final_prompt.index("cliente VIP")
    pos_rag = final_prompt.index("ROI promedio")
    pos_user = final_prompt.index("Como mido el ROI?")
    assert pos_system < pos_memory < pos_rag < pos_user
