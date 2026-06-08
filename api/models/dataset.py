"""Dataset/RAG models — stubbed for MyOwnClone."""
from typing import Optional

class Dataset:
    id: str
    name: str
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

class DocumentSegment:
    id: str
    dataset_id: str
    content: str
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

__all__ = ['Dataset', 'DocumentSegment']
