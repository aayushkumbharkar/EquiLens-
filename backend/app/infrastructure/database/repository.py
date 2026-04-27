from typing import List
from sqlalchemy.orm import Session
from app.domain.entities import AnalysisResult
from app.domain.interfaces import IAnalysisRepository
from app.infrastructure.database.models import AnalysisRecordModel

class SqlAlchemyAnalysisRepository(IAnalysisRepository):
    def __init__(self, db_session: Session):
        self.db = db_session

    def save(self, analysis: AnalysisResult) -> AnalysisResult:
        db_record = AnalysisRecordModel(
            prompt=analysis.prompt,
            original_decision=analysis.original_decision,
            bias_detected=analysis.bias_detected,
            fairness_score=analysis.fairness_score,
            explanation=analysis.explanation,
            suggested_fix=analysis.suggested_fix
        )
        self.db.add(db_record)
        self.db.commit()
        self.db.refresh(db_record)
        
        # Update entity with DB generated fields
        analysis.id = db_record.id
        analysis.created_at = db_record.created_at
        return analysis

    def get_history(self, skip: int = 0, limit: int = 20) -> List[AnalysisResult]:
        records = self.db.query(AnalysisRecordModel).order_by(AnalysisRecordModel.created_at.desc()).offset(skip).limit(limit).all()
        return [
            AnalysisResult(
                id=r.id,
                prompt=r.prompt,
                original_decision=r.original_decision,
                bias_detected=r.bias_detected,
                fairness_score=r.fairness_score,
                explanation=r.explanation,
                suggested_fix=r.suggested_fix,
                created_at=r.created_at
            ) for r in records
        ]
