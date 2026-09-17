from types import SimpleNamespace

from resumeforge.tailoring.plan import TailoringPlan
from resumeforge.tailoring.prioritizer import TailoringPrioritizer


def test_prioritize_promotes_education():

    plan = TailoringPlan(
        education=[
            "B.S. Computer Science",
            "AWS Academy",
            "Azure Learning Path",
        ]
    )

    match = SimpleNamespace(
        promoted_education=[
            "AWS Academy",
        ]
    )

    result = TailoringPrioritizer().prioritize(
        plan,
        match,
    )

    assert result.education == [
        "AWS Academy",
        "B.S. Computer Science",
        "Azure Learning Path",
    ]

    assert result.promoted_education == [
        "AWS Academy",
    ]