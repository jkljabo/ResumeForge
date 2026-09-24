from resumeforge.tailoring.plan import TailoringPlan
from resumeforge.tailoring.result import TailoringResult
from resumeforge.tailoring.workflow import TailoringWorkflow


def test_build_result_returns_tailoring_result():

    plan = TailoringPlan()

    plan.rationale.append(
        "Promoted skill: Azure (matched requested skills)"
    )

    result = TailoringWorkflow().build_result(plan)

    assert isinstance(result, TailoringResult)
    assert result.plan is plan

    assert result.explainability_report == (
        "Promoted skill: Azure (matched requested skills)"
    )

def test_build_result_preserves_plan_identity():

    plan = TailoringPlan()

    result = TailoringWorkflow().build_result(plan)

    assert result.plan is plan