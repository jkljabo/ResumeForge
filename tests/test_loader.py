from resumeforge.loader import load_resume
from resumeforge.domain import ResumeProfile
from resumeforge.profiles.repository import ProfileRepository


def test_resume_loads():
    repository = ProfileRepository()
    profile = repository.get_default()
    resume = load_resume(profile.resume_path)

    assert isinstance(resume, ResumeProfile)
    assert resume.header.name == "Jason Little"