from types import SimpleNamespace
from tests.helpers import make_resume

from resumeforge.tailoring.engine import TailoringEngine
from resumeforge.tailoring.plan import TailoringPlan


def test_engine_returns_tailoring_plan():
    engine = TailoringEngine()

    plan = engine.create_plan(
        resume=make_resume(),
        match_result=None,
    )

    assert isinstance(
        plan,
        TailoringPlan,
    )

def test_engine_populates_experience():

    resume = make_resume(
        experience=[
            "Senior Engineer",
        ],
    )

    engine = TailoringEngine()

    plan = engine.create_plan(
        resume,
        None,
    )

    assert plan.experience == [
        "Senior Engineer",
    ]

def test_engine_populates_certifications():

    resume = make_resume(
        certifications=[
            "Azure Fundamentals",
        ]
    )

    engine = TailoringEngine()

    plan = engine.create_plan(
        resume,
        None,
    )

    assert plan.certifications == [
        "Azure Fundamentals",
    ]

def test_engine_populates_summary_keywords():

    resume = make_resume(
        summary_keywords=[
            "Azure",
            "Python",
        ]
    )

    engine = TailoringEngine()

    plan = engine.create_plan(
        resume,
        None,
    )

    assert plan.summary_keywords == [
        "Azure",
        "Python",
    ]

def test_engine_builds_complete_tailoring_plan():

    resume = make_resume(
        skills=["Python"],
        experience=["Senior Engineer"],
        projects=["ResumeForge"],
        certifications=["Azure Fundamentals"],
        summary_keywords=["cloud", "microservices"],
    )

    engine = TailoringEngine()

    plan = engine.create_plan(
        resume,
        None,
    )

    assert plan.skills == ["Python"]
    assert plan.experience == ["Senior Engineer"]
    assert plan.projects == ["ResumeForge"]
    assert plan.certifications == ["Azure Fundamentals"]
    assert plan.summary_keywords == [
        "cloud",
        "microservices",
    ]

def test_engine_handles_empty_resume():

    engine = TailoringEngine()

    plan = engine.create_plan(
        make_resume(),
        None,
    )

    assert plan.skills == []
    assert plan.experience == []
    assert plan.projects == []
    assert plan.certifications == []
    assert plan.summary_keywords == []

    