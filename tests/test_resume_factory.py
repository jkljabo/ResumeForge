from resumeforge.resume.factory import create_resume_service
from resumeforge.resume.repository import ResumeRepository
from resumeforge.services.resume_service import ResumeService


def test_factory_returns_resume_service():
    service = create_resume_service()

    assert isinstance(
        service,
        ResumeService,
    )


def test_factory_uses_resume_repository():
    service = create_resume_service()

    assert isinstance(
        service.repository,
        ResumeRepository,
    )