from resumeforge.resume.repository import ResumeRepository
from resumeforge.services.resume_service import ResumeService


def create_resume_service() -> ResumeService:
    return ResumeService(
        repository=ResumeRepository(),
    )