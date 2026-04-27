from fastapi import APIRouter, Depends
from typing import List

from app.infrastructure.api.dto import GenerateRequest, GenerateResponse, EvaluateRequest, AnalysisResponse
from app.use_cases.generate_decision import GenerateDecisionUseCase
from app.use_cases.analyze_bias import AnalyzeBiasUseCase
from app.domain.interfaces import IAnalysisRepository
from app.infrastructure.api.dependencies import get_generate_decision_use_case, get_analyze_bias_use_case, get_repository

router = APIRouter()

@router.post("/generate", response_model=GenerateResponse)
def generate(
    request: GenerateRequest,
    use_case: GenerateDecisionUseCase = Depends(get_generate_decision_use_case)
):
    decision = use_case.execute(request.prompt)
    return GenerateResponse(decision=decision)

@router.post("/evaluate", response_model=AnalysisResponse)
def evaluate(
    request: EvaluateRequest,
    use_case: AnalyzeBiasUseCase = Depends(get_analyze_bias_use_case)
):
    result = use_case.execute(request.prompt, request.decision)
    return AnalysisResponse.from_entity(result)

@router.get("/history", response_model=List[AnalysisResponse])
def get_history(
    skip: int = 0, limit: int = 20,
    repository: IAnalysisRepository = Depends(get_repository)
):
    records = repository.get_history(skip, limit)
    return [AnalysisResponse.from_entity(r) for r in records]
