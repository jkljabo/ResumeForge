from resumeforge.resume.factory import create_resume_service
from resumeforge.domain import ResumeProfile
from resumeforge.profiles.repository import ProfileRepository


def test_resume_loads():
    repository = ProfileRepository()
    profile = repository.get_default()

    service = create_resume_service()
    resume = service.load(profile.resume_path)

    assert isinstance(resume, ResumeProfile)
    assert resume.header.name == "Jason Little"