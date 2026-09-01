from resumeforge.resume.document import ResumeDocument


def test_resume_document_defaults():

    resume = ResumeDocument()

    assert resume.summary == ""

    assert resume.skills == []

    assert resume.experience == []

    assert resume.education == []

    assert resume.certifications == []

    assert resume.projects == []

def test_resume_document_accepts_values():

    resume = ResumeDocument(
        summary="Senior .NET Developer",
        skills=["C#", ".NET"],
        experience=["Experience Item"],
    )

    assert resume.summary == "Senior .NET Developer"

    assert resume.skills == ["C#", ".NET"]

    assert resume.experience == ["Experience Item"]