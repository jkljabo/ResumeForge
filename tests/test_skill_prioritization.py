from types import SimpleNamespace

from resumeforge.tailoring.plan import TailoringPlan
from resumeforge.tailoring.prioritizer import TailoringPrioritizer


def test_prioritize_promotes_skills():
    plan = TailoringPlan(
        skills=[
            "VB.NET",
            "Azure",
            "C#",
        ]
    )

    match = SimpleNamespace(
        promoted_skills=[
            "Azure",
            "C#",
        ]
    )

    result = TailoringPrioritizer().prioritize(
        plan,
        match,
    )

    assert result.skills == [
        "Azure",
        "C#",
        "VB.NET",
    ]

    assert result.promoted_skills == [
        "Azure",
        "C#",
    ]

def test_prioritize_promotes_projects():

    plan = TailoringPlan(
        projects=[
            "Inventory System",
            "Azure Migration",
            "Legacy Modernization",
        ]
    )

    match = SimpleNamespace(
        promoted_projects=[
            "Azure Migration",
        ]
    )

    result = TailoringPrioritizer().prioritize(
        plan,
        match,
    )

    assert result.projects == [
        "Azure Migration",
        "Inventory System",
        "Legacy Modernization",
    ]

    assert result.promoted_projects == [
        "Azure Migration",
    ]