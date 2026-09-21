from resumeforge.tailoring.explainability_formatter import (
    ExplainabilityFormatter,
)
from resumeforge.tailoring.plan import TailoringPlan


def test_format_empty_plan():

    plan = TailoringPlan()

    formatter = ExplainabilityFormatter()

    assert formatter.format(plan) == ""

def test_format_skill_rationale():

    plan = TailoringPlan()

    plan.rationale.append(
        "Promoted skill: Azure (matched requested skills)"
    )

    formatter = ExplainabilityFormatter()

    assert formatter.format(plan) == (
        "Promoted skill: Azure "
        "(matched requested skills)"
    )

def test_format_multiple_rationale_entries():

    plan = TailoringPlan()

    plan.rationale.extend(
        [
            "Promoted skill: Azure (matched requested skills)",
            "Promoted project: ResumeForge (matched requested projects)",
        ]
    )

    formatter = ExplainabilityFormatter()

    assert formatter.format(plan) == (
        "Promoted skill: Azure (matched requested skills)\n"
        "Promoted project: ResumeForge (matched requested projects)"
    )

def test_format_lines_returns_rationale():

    plan = TailoringPlan()

    plan.rationale.extend(
        [
            "One",
            "Two",
        ]
    )

    formatter = ExplainabilityFormatter()

    assert formatter.format_lines(plan) == [
        "One",
        "Two",
    ]

def test_format_preserves_rationale_order():
    plan = TailoringPlan()

    plan.rationale.extend(
        [
            "Third",
            "First",
            "Second",
        ]
    )

    formatter = ExplainabilityFormatter()

    assert formatter.format_lines(plan) == [
        "Third",
        "First",
        "Second",
    ]

