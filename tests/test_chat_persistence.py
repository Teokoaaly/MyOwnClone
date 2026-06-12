from flask import Flask

from api.controllers import myownclone_public
from api.controllers.myownclone_public import _conversation_mode_for_silo, _persist_chat_turn
from api.models.analytics import AnalyticsQuestion
from api.models.conversation import Conversation, Message


class _ScalarResult:
    def __init__(self, value=None):
        self.value = value

    def scalar_one_or_none(self):
        return self.value


class _FakeSession:
    def __init__(self):
        self.added = []
        self.committed = False

    def execute(self, _stmt):
        return _ScalarResult(None)

    def add(self, value):
        self.added.append(value)

    def flush(self):
        for value in self.added:
            if isinstance(value, Conversation) and not value.id:
                value.id = "conv_1"

    def commit(self):
        self.committed = True


def test_conversation_mode_maps_teach_to_pedagogy():
    assert _conversation_mode_for_silo("teach") == "pedagogy"
    assert _conversation_mode_for_silo("support") == "support"
    assert _conversation_mode_for_silo("sales") == "sales"


def test_persist_chat_turn_creates_conversation_messages_and_question(monkeypatch):
    fake_session = _FakeSession()
    monkeypatch.setattr(myownclone_public.db, "session", fake_session)

    app = Flask(__name__)
    with app.test_request_context(
        "/api/myownclone/public/clones/demo/chat",
        headers={"User-Agent": "pytest"},
        environ_base={"REMOTE_ADDR": "127.0.0.1"},
    ):
        conversation_id = _persist_chat_turn(
            clone_id="clone_1",
            conversation_id=None,
            silo="teach",
            user_message="How does pricing work?",
            assistant_message="Pricing starts free.",
            confidence=0.74,
            sources=[{"chunkId": "chunk_1", "score": 0.74}],
        )

    assert conversation_id == "conv_1"
    assert fake_session.committed is True
    assert any(isinstance(item, Conversation) and item.mode == "pedagogy" for item in fake_session.added)
    assert len([item for item in fake_session.added if isinstance(item, Message)]) == 2
    assert any(isinstance(item, AnalyticsQuestion) and item.count == 1 for item in fake_session.added)
