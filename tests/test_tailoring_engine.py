from types import SimpleNamespace

from resumeforge.tailoring.engine import TailoringEngine
from resumeforge.tailoring.plan import TailoringPlan


def test_engine_returns_tailoring_plan():
    engine = TailoringEngine()

    plan = engine.build_plan(
        resume=make_resume(),
        match_result=None,
    )

    assert isinstance(
        plan,
        TailoringPlan,
    )

def make_resume(**overrides):
    data = {
        "skills": [],
        "experience": [],
        "projects": [],
        "certifications": [],
        "summary": "",
    }
    data.update(overrides)
    return SimpleNamespace(**data)

def test_engine_populates_experience():

    resume = make_resume(
        experience=[
            "Senior Engineer",
        ],
    )

    engine = TailoringEngine()

    plan = engine.build_plan(
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

    plan = engine.build_plan(
        resume,
        None,
    )

    assert plan.certifications == [
        "Azure Fundamentals",
    ]