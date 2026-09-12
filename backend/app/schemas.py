from typing import Literal

from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    status: Literal["ok"] = "ok"
    model_available: bool
    model_path: str


class PredictionResponse(BaseModel):
    status: Literal["model_unavailable", "predicted"]
    message: str
    crop: str | None = None
    disease: str | None = None
    confidence: float | None = Field(default=None, ge=0, le=1)
    next_steps: list[str] = Field(default_factory=list)


class AdvisoryItem(BaseModel):
    id: str
    title: str
    body: str
    category: str


class AdvisoryResponse(BaseModel):
    items: list[AdvisoryItem]
