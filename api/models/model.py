"""Core Dify models — stubbed for MyOwnClone."""
from typing import Optional

class App:
    id: str
    name: str
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

class Conversation:
    id: str
    app_id: str
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

class Message:
    id: str
    conversation_id: str
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

__all__ = ['App', 'Conversation', 'Message']
