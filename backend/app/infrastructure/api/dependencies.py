from fastapi import Depends
from app.infrastructure.database.session import SessionLocal
from app.infrastructure.database.repository import SqlAlchemyAnalysisRepository
from app.infrastructure.external.gemini_ai import GeminiAIService
from app.domain.interfaces import IAnalysisRepository, IAIService
from app.use_cases.generate_decision import GenerateDecisionUseCase
from app.use_cases.analyze_bias import AnalyzeBiasUseCase

def get_db_session():
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()

def get_repository(db_session=Depends(get_db_session)) -> IAnalysisRepository:
    return SqlAlchemyAnalysisRepository(db_session)

def get_ai_service() -> IAIService:
    return GeminiAIService()

def get_generate_decision_use_case(ai_service: IAIService = Depends(get_ai_service)) -> GenerateDecisionUseCase:
    return GenerateDecisionUseCase(ai_service)

def get_analyze_bias_use_case(
    repository: IAnalysisRepository = Depends(get_repository),
    ai_service: IAIService = Depends(get_ai_service)
) -> AnalyzeBiasUseCase:
    return AnalyzeBiasUseCase(repository, ai_service)
