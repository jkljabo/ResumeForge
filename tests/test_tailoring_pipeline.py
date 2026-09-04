from types import SimpleNamespace
from tests.helpers import make_resume

from resumeforge.tailoring.engine import TailoringEngine
from resumeforge.tailoring.tailored_resume_builder import (
    TailoredResumeBuilder,
)
from resumeforge.tailoring.plan import TailoringPlan

def test_complete_tailoring_pipeline():

    profile = make_resume(
        skills=["Python"],
        experience=["Senior Engineer"],
        projects=["ResumeForge"],
        certifications=["Azure Fundamentals"],
        summary_keywords=["Cloud", "Azure"],
    )

    engine = TailoringEngine()

    plan = engine.create_plan(
        profile,
        None,
    )

    builder = TailoredResumeBuilder()

    document = builder.build(
        profile,
        plan,
    )

    assert document.skills == profile.skills
    assert document.experience == profile.experience
    assert document.projects == profile.projects
    assert document.certifications == profile.certifications
    assert document.summary == "Cloud Azure"

