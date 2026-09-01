from types import SimpleNamespace

from resumeforge.resume.builder import ResumeBuilder
from resumeforge.resume.document import ResumeDocument

def test_builder_creates_resume_document():

    resume = SimpleNamespace(
        summary="Senior .NET Engineer",
        skills=["C#", ".NET"],
        experience=["Developer"],
        education=["BS Computer Science"],
        certifications=["Azure"],
        projects=["ResumeForge"],
    )

    builder = ResumeBuilder()

    document = builder.build(resume)

    assert document.summary == "Senior .NET Engineer"
    assert document.skills == ["C#", ".NET"]
    assert document.experience == ["Developer"]
    assert document.education == ["BS Computer Science"]
    assert document.certifications == ["Azure"]
    assert document.projects == ["ResumeForge"]

def test_builder_returns_new_document():

    resume = SimpleNamespace(
        summary="Summary",
        skills=[],
        experience=[],
        education=[],
        certifications=[],
        projects=[],
    )

    builder = ResumeBuilder()

    document = builder.build(resume)

    assert document is not resume

from resumeforge.resume.document import ResumeDocument


def test_builder_returns_resume_document():

    resume = SimpleNamespace(
        summary="",
        skills=[],
        experience=[],
        education=[],
        certifications=[],
        projects=[],
    )

    builder = ResumeBuilder()

    document = builder.build(resume)

    assert isinstance(document, ResumeDocument)