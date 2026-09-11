from pathlib import Path

from resumeforge.domain.resume import ResumeProfile
from resumeforge.resume.repository import ResumeRepository
from resumeforge.resume.repository_protocol import ResumeRepositoryProtocol


def test_repository_implements_protocol():
    repository = ResumeRepository()

    assert isinstance(
        repository,
        ResumeRepositoryProtocol,
    )


def test_load_returns_resume_document():
    repository = ResumeRepository()

    document = repository.load(
        Path("resumeforge/data/resume.json")
    )

    assert isinstance(
        document,
        ResumeProfile,
    )


