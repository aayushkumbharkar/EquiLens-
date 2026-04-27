from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from app.domain.entities import AnalysisResult

class GenerateRequest(BaseModel):
    prompt: str

class GenerateResponse(BaseModel):
    decision: str

class EvaluateRequest(BaseModel):
    prompt: str
    decision: str

class AnalysisResponse(BaseModel):
    id: Optional[int] = None
    prompt: str
    original_decision: str
    bias_detected: bool
    fairness_score: float
    explanation: str
    suggested_fix: str
    created_at: Optional[datetime] = None

    @classmethod
    def from_entity(cls, entity: AnalysisResult):
        return cls(
            id=entity.id,
            prompt=entity.prompt,
            original_decision=entity.original_decision,
            bias_detected=entity.bias_detected,
            fairness_score=entity.fairness_score,
            explanation=entity.explanation,
            suggested_fix=entity.suggested_fix,
            created_at=entity.created_at
        )

    class Config:
        from_attributes = True
