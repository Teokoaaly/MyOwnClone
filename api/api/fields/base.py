"""ResponseModel stub for API serialization."""
from pydantic import BaseModel

class ResponseModel(BaseModel):
    """Pydantic base for API response models."""
    model_config = {"extra": "allow"}
__all__ = ['ResponseModel']
