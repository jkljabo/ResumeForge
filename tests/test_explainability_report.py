from resumeforge.tailoring.explainability_report import ExplainabilityReport
from resumeforge.tailoring.plan import TailoringPlan


def test_build_empty_report():
    
    plan = TailoringPlan()

    report = ExplainabilityReport().build(plan)

    assert report == ""

def test_build_report_from_rationale():

    plan = TailoringPlan()

    plan.rationale.append(
        "Promoted skill: Azure (matched requested skills)"
    )

    report = ExplainabilityReport().build(plan)

    assert report == (
        "Promoted skill: Azure "
        "(matched requested skills)"
    )

def test_build_report_multiple_rationale_entries():

    plan = TailoringPlan()

    plan.rationale.extend(
        [
            "Promoted skill: Azure (matched requested skills)",
            "Promoted project: ResumeForge (matched requested projects)",
        ]
    )

    report = ExplainabilityReport().build(plan)

    assert report == (
        "Promoted skill: Azure (matched requested skills)\n"
        "Promoted project: ResumeForge (matched requested projects)"
    )

def test_build_report_does_not_modify_plan():

    plan = TailoringPlan()

    plan.rationale.append(
        "Promoted skill: Azure (matched requested skills)"
    )

    original = list(plan.rationale)

    ExplainabilityReport().build(plan)

    assert plan.rationale == original

def test_build_report_returns_new_string():

    plan = TailoringPlan()

    plan.rationale.append(
        "Promoted skill: Azure (matched requested skills)"
    )

    report1 = ExplainabilityReport().build(plan)
    report2 = ExplainabilityReport().build(plan)

    assert report1 == report2
    assert report1 is not None

