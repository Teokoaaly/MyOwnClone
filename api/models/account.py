"""Account/Tenant models — stubbed for MyOwnClone."""
from typing import Optional

class Tenant:
    id: str
    name: str
    status: str
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

class Account:
    id: str
    tenant_id: str
    email: str
    name: str
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

__all__ = ['Tenant', 'Account']
