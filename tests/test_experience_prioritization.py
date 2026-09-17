from types import SimpleNamespace

from resumeforge.tailoring.plan import TailoringPlan
from resumeforge.tailoring.prioritizer import TailoringPrioritizer


def test_prioritize_leaves_experience_order_unchanged_when_no_promotions():

    plan = TailoringPlan(
        experience=[
            "Retail POS",
            "Azure Migration",
            "Legacy VB",
        ]
    )

    prioritizer = TailoringPrioritizer()

    result = prioritizer.prioritize(
        plan,
        SimpleNamespace(),
    )

    assert result.experience == [
        "Retail POS",
        "Azure Migration",
        "Legacy VB",
    ]


def test_prioritize_promotes_experience():

    plan = TailoringPlan(
        experience=[
            "Retail POS",
            "Azure Migration",
            "Legacy VB",
        ]
    )

    match_result = SimpleNamespace(
        promoted_experience=[
            "Azure Migration",
        ]
    )

    prioritizer = TailoringPrioritizer()

    result = prioritizer.prioritize(
        plan,
        match_result,
    )

    assert result.experience == [
        "Azure Migration",
        "Retail POS",
        "Legacy VB",
    ]

    assert result.promoted == [
        "Azure Migration",
    ]