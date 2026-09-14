from resumeforge.resume.repository import ResumeRepository
from resumeforge.services.resume_service import ResumeService
from resumeforge.tailoring.tailored_resume_builder import (
    TailoredResumeBuilder,
)

def create_resume_service() -> ResumeService:
    return ResumeService(
        repository=ResumeRepository(),
    )

def create_builder() -> TailoredResumeBuilder:
    return TailoredResumeBuilder()