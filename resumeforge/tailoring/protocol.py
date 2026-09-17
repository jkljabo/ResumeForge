from typing import Protocol

from resumeforge.tailoring.plan import TailoringPlan


class TailoringEngineProtocol(Protocol):

    def create_plan(
        self,
        resume,
        match_result,
    ) -> TailoringPlan:
        ...