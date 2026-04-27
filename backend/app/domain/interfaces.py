from abc import ABC, abstractmethod
from typing import List
from app.domain.entities import AnalysisResult

class IAnalysisRepository(ABC):
    @abstractmethod
    def save(self, analysis: AnalysisResult) -> AnalysisResult:
        pass

    @abstractmethod
    def get_history(self, skip: int = 0, limit: int = 20) -> List[AnalysisResult]:
        pass

class IAIService(ABC):
    @abstractmethod
    def generate_decision(self, prompt: str) -> str:
        pass

    @abstractmethod
    def analyze_bias(self, original_prompt: str, original_decision: str, variation_prompt: str) -> dict:
        pass
