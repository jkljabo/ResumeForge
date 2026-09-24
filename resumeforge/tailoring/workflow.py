from resumeforge.tailoring.explainability_report import ExplainabilityReport
from resumeforge.tailoring.result import TailoringResult


class TailoringWorkflow:

    def build_result(self, plan):
        report = ExplainabilityReport().build(plan)

        return TailoringResult(
            plan=plan,
            explainability_report=report,
        )