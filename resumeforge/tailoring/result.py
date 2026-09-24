from dataclasses import dataclass

from resumeforge.tailoring.plan import TailoringPlan


@dataclass
class TailoringResult:
    plan: TailoringPlan
    explainability_report: str