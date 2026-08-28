from types import SimpleNamespace

from resumeforge.filtering import ResumeFilter


def test_filter_can_be_created():
    resume_filter = ResumeFilter()
    assert resume_filter is not None

def test_filter_returns_resume():
    resume = object()

    resume_filter = ResumeFilter()

    filtered = resume_filter.filter(resume, "")

    assert filtered is resume

def test_filter_returns_same_resume_when_job_description_empty():
    resume = object()
    resume_filter = ResumeFilter()

    filtered = resume_filter.filter(resume, "")

    assert filtered is resume


def test_filter_keeps_matching_skill_groups():
    resume = SimpleNamespace(
        skills=[
            SimpleNamespace(category="Cloud", tags=["azure", "cloud"]),
            SimpleNamespace(category="Data", tags=["sql", "reporting"]),
        ],
        experience=[],
        projects=[],
        certifications=[],
    )

    resume_filter = ResumeFilter()

    filtered = resume_filter.filter(resume, "Azure cloud engineer")

    assert len(filtered.skills) == 1
    assert filtered.skills[0].category == "Cloud"