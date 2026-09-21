from resumeforge.tailoring.explainability_formatter import ExplainabilityFormatter


class ExplainabilityReport:

    def build(
        self,
        plan,
    ):
        return ExplainabilityFormatter().format(plan)