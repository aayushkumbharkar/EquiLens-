from sqlalchemy import Column, Integer, String, Boolean, Float, DateTime
from sqlalchemy.sql import func
from app.infrastructure.database.session import Base

class AnalysisRecordModel(Base):
    __tablename__ = "analysis_records"

    id = Column(Integer, primary_key=True, index=True)
    prompt = Column(String, nullable=False)
    original_decision = Column(String, nullable=False)
    bias_detected = Column(Boolean, nullable=False)
    fairness_score = Column(Float, nullable=False)
    explanation = Column(String, nullable=False)
    suggested_fix = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
