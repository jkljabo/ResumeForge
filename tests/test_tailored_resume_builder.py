from types import SimpleNamespace

from resumeforge.resume.document import ResumeDocument
from resumeforge.tailoring.plan import TailoringPlan
from resumeforge.tailoring.tailored_resume_builder import (
    TailoredResumeBuilder,
)


def test_builder_returns_resume_document():

    builder = TailoredResumeBuilder()

    document = builder.build(
        profile=None,
        plan=TailoringPlan(),
    )

    assert isinstance(
        document,
        ResumeDocument,
    )

def test_builder_copies_contact_information():

    profile = SimpleNamespace(
        name="Jason Little",
        title="Senior Software Engineer",
        email="jason@example.com",
        phone="555-555-5555",
        location="Marietta, GA",
        linkedin="linkedin.com/in/jason",
        github="github.com/jason",
    )

    builder = TailoredResumeBuilder()

    document = builder.build(
        profile,
        TailoringPlan(),
    )

    assert document.name == profile.name
    assert document.title == profile.title
    assert document.email == profile.email
    assert document.phone == profile.phone
    assert document.location == profile.location
    assert document.linkedin == profile.linkedin
    assert document.github == profile.github

def test_builder_generates_summary():

    builder = TailoredResumeBuilder()

    plan = TailoringPlan(
        summary_keywords=[
            "Cloud",
            "Azure",
            "Microservices",
        ],
    )

    document = builder.build(
        profile=None,
        plan=plan,
    )

    assert document.summary == (
        "Cloud Azure Microservices"
    )

def test_builder_populates_skills():

    builder = TailoredResumeBuilder()

    plan = TailoringPlan(
        skills=[
            "C#",
            ".NET",
            "Azure",
        ],
    )

    document = builder.build(
        profile=None,
        plan=plan,
    )

    assert document.skills == [
        "C#",
        ".NET",
        "Azure",
    ]

def test_builder_populates_experience():

    builder = TailoredResumeBuilder()

    plan = TailoringPlan(
        experience=[
            "Senior Software Engineer",
            "Lead .NET Developer",
        ],
    )

    document = builder.build(
        profile=None,
        plan=plan,
    )

    assert document.experience == [
        "Senior Software Engineer",
        "Lead .NET Developer",
    ]

def test_builder_populates_projects():

    builder = TailoredResumeBuilder()

    plan = TailoringPlan(
        projects=[
            "ResumeForge",
            "Blazor Expo",
        ],
    )

    document = builder.build(
        profile=None,
        plan=plan,
    )

    assert document.projects == [
        "ResumeForge",
        "Blazor Expo",
    ]

def test_builder_populates_certifications():

    builder = TailoredResumeBuilder()

    plan = TailoringPlan(
        certifications=[
            "Azure Fundamentals",
            "AWS Cloud Practitioner",
        ],
    )

    document = builder.build(
        profile=None,
        plan=plan,
    )

    assert document.certifications == [
        "Azure Fundamentals",
        "AWS Cloud Practitioner",
    ]

def test_builder_creates_document_from_complete_plan():

    builder = TailoredResumeBuilder()

    plan = TailoringPlan(
        skills=["Python"],
        experience=["Senior Engineer"],
        projects=["ResumeForge"],
        certifications=["Azure Fundamentals"],
        summary_keywords=["Cloud", "Azure"],
    )

    document = builder.build(
        profile=None,
        plan=plan,
    )

    assert document.summary == "Cloud Azure"
    assert document.skills == ["Python"]
    assert document.experience == ["Senior Engineer"]
    assert document.projects == ["ResumeForge"]
    assert document.certifications == [
        "Azure Fundamentals",
    ]

