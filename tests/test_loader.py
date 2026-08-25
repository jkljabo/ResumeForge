from resumeforge.loader import load_resume
from resumeforge.domain import ResumeProfile


def test_resume_loads():
    resume = load_resume()

    assert isinstance(resume, ResumeProfile)
    assert resume.header.name == "Jason Little"