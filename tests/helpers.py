from types import SimpleNamespace

from resumeforge.domain import (
    Header,
    ResumeProfile,
    Summary,
)

def make_resume(
    skills=None,
    experience=None,
    projects=None,
    certifications=None,
    summary="",
    summary_keywords=None,
):
    return SimpleNamespace(
        name="Jason Little",
        email="jason@example.com",
        phone="555-555-5555",
        skills=skills or [],
        experience=experience or [],
        projects=projects or [],
        certifications=certifications or [],
        summary=summary,
        summary_keywords=summary_keywords or [],
    )

def make_document(
    **kwargs,
):

    defaults = dict(
        name="",
        email="",
        phone="",
        summary="",
        skills=[],
        experience=[],
        projects=[],
        certifications=[],
    )

    defaults.update(kwargs)

    return SimpleNamespace(**defaults)

def make_resume_profile():
    return ResumeProfile(
        header=Header(
        name="Test User",
        headline="Software Engineer",
        tagline="Testing ResumeForge",
        location="Anywhere",
        phone="555-555-5555",
        email="test@example.com",
        linkedin="",
        github="",
        portfolio="",
    ),
        summary=Summary(
            text="Test Summary",
        ),
        education=[],
        experience=[],
        skills=[],
    )
