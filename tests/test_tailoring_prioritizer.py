from types import SimpleNamespace

from resumeforge.tailoring.plan import TailoringPlan
from resumeforge.tailoring.prioritizer import TailoringPrioritizer


def test_prioritize_orders_recommendations_by_impact():

    plan = TailoringPlan(
        recommendations=[
            SimpleNamespace(keyword="docker", impact=3),
            SimpleNamespace(keyword="azure", impact=10),
            SimpleNamespace(keyword="kubernetes", impact=7),
        ]
    )

    prioritizer = TailoringPrioritizer()

    result = prioritizer.prioritize(
        plan,
        None,
    )

    assert [
        r.keyword
        for r in result.recommendations
    ] == [
        "azure",
        "kubernetes",
        "docker",
    ]

def test_prioritize_does_not_modify_skills():

    skills = [
        "Azure",
        "C#",
    ]

    plan = TailoringPlan(
        skills=skills.copy(),
    )

    prioritizer = TailoringPrioritizer()

    result = prioritizer.prioritize(
        plan,
        None,
    )

    assert result.skills == skills