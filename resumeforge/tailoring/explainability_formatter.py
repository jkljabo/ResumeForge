from resumeforge.tailoring.plan import TailoringPlan


class ExplainabilityFormatter:

    def format(
        self,
        plan: TailoringPlan,
    ) -> str:

        return "\n".join(self.format_lines(plan))

    def format_lines(
        self,
        plan: TailoringPlan,
    ) -> list[str]:
        
        return list(plan.rationale)