from pathlib import Path

from resumeforge.resume.repository import ResumeRepository
from resumeforge.services.resume_service import ResumeService

class FakeResumeRepository(ResumeRepository):
    def __init__(self):
        self.called_with = None

    def load(self, path):
        self.called_with = path
        return "resume"

    
def test_service_uses_injected_repository():
    repository = ResumeRepository()

    service = ResumeService(repository)

    assert service.repository is repository

def test_service_load_uses_repository():
    repository = FakeResumeRepository()

    service = ResumeService(repository)

    path = Path("resume.json")

    result = service.load(path)

    assert result == "resume"
    assert repository.called_with == path