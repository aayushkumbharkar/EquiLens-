from app.domain.entities import AnalysisResult
from app.domain.interfaces import IAnalysisRepository, IAIService
from app.domain.variation import create_variation

class AnalyzeBiasUseCase:
    def __init__(self, repository: IAnalysisRepository, ai_service: IAIService):
        self.repository = repository
        self.ai_service = ai_service

    def execute(self, prompt: str, original_decision: str) -> AnalysisResult:
        variation_prompt = create_variation(prompt)
        
        # Analyze using AI
        ai_result = self.ai_service.analyze_bias(prompt, original_decision, variation_prompt)
        
        # Create Entity
        analysis = AnalysisResult(
            prompt=prompt,
            original_decision=original_decision,
            bias_detected=ai_result.get("bias_detected", True),
            fairness_score=float(ai_result.get("fairness_score", 45.0)),
            explanation=ai_result.get("explanation", "Error in AI generation."),
            suggested_fix=ai_result.get("suggested_fix", "Base decisions purely on objective criteria.")
        )
        
        # Save Entity via Repository
        saved_analysis = self.repository.save(analysis)
        
        return saved_analysis
