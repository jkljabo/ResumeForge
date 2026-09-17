from types import SimpleNamespace
from resumeforge.recommendations.recommendation import Recommendation
from tests.helpers import make_resume

from resumeforge.tailoring.engine import TailoringEngine
from resumeforge.tailoring.plan import TailoringPlan


class FakeSkillSelector:

    def select(
        self,
        resume,
        match_result,
    ):
        return ["Injected Skill"]


class FakePrioritizer:

    def __init__(self):
        self.called = False

    def prioritize(
        self,
        plan,
        match_result,
    ):
        self.called = True
        return plan

    
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

def test_create_plan_returns_prioritized_recommendations():

    class FakeSelector:
        def select(self, resume, match_result):
            return []

    engine = TailoringEngine(
        skill_selector=FakeSelector(),
        experience_selector=FakeSelector(),
        project_selector=FakeSelector(),
        certification_selector=FakeSelector(),
        summary_selector=FakeSelector(),
    )

    match_result = SimpleNamespace(
        recommendations=[
            Recommendation(
                keyword="Recommendation A",
                section="Skills",
                impact=1,
                reason="",
            ),
            Recommendation(
                keyword="Recommendation B",
                section="Skills",
                impact=2,
                reason="",
            ),
        ]
    )

    plan = engine.create_plan(
        resume=object(),
        match_result=match_result,
    )

    assert len(plan.recommendations) == 2

    assert plan.recommendations[0].keyword == "Recommendation B"
    assert plan.recommendations[1].keyword == "Recommendation A"
    
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

def test_engine_uses_injected_skill_selector():

    engine = TailoringEngine(
        skill_selector=FakeSkillSelector(),
    )

    plan = engine.create_plan(
        resume=make_resume(),
        match_result=None,
    )

    assert plan.skills == [
        "Injected Skill",
    ]

def test_engine_uses_prioritizer():

    prioritizer = FakePrioritizer()

    engine = TailoringEngine(
        prioritizer=prioritizer,
    )

    engine.create_plan(
        resume=make_resume(),
        match_result=None,
    )

    assert prioritizer.called