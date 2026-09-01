from resumeforge.optimizer.optimization_result import (
    OptimizationResult,
)


class ResumeOptimizer:

    def optimize(
        self,
        resume,
        recommendations,
    ):
        applied = []
        skipped = []

        for recommendation in recommendations:
            if self._can_apply(recommendation):
                applied.append(recommendation)
            else:
                skipped.append(recommendation)

        return OptimizationResult(
            resume=resume,
            applied=applied,
            skipped=skipped,
        )

    def _can_apply(self, recommendation):
        return True