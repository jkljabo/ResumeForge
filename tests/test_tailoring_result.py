from resumeforge.tailoring.explainability_report import ExplainabilityReport
from resumeforge.tailoring.plan import TailoringPlan
from resumeforge.tailoring.result import TailoringResult


def test_tailoring_result_contains_plan_and_report():

    plan = TailoringPlan()
    plan.rationale.append(
        "Promoted skill: Azure (matched requested skills)"
    )

    result = TailoringResult(
        plan=plan,
        explainability_report=ExplainabilityReport().build(plan),
    )

    assert result.plan is plan

    assert result.explainability_report == (
        "Promoted skill: Azure "
        "(matched requested skills)"
    )