from resumeforge.filtering import ResumeFilter


def test_filter_can_be_created():
    resume_filter = ResumeFilter()

    assert resume_filter is not None


def test_filter_returns_resume():
    resume = object()

    resume_filter = ResumeFilter()

    filtered = resume_filter.filter(resume, "")

    assert filtered is resume