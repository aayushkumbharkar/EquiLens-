from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class AnalysisResult:
    prompt: str
    original_decision: str
    bias_detected: bool
    fairness_score: float
    explanation: str
    suggested_fix: str
    id: Optional[int] = None
    created_at: Optional[datetime] = None
