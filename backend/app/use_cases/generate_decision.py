from app.domain.interfaces import IAIService

class GenerateDecisionUseCase:
    def __init__(self, ai_service: IAIService):
        self.ai_service = ai_service

    def execute(self, prompt: str) -> str:
        return self.ai_service.generate_decision(prompt)
