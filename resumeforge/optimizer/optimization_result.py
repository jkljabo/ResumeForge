class OptimizationResult:

    def __init__(
        self,
        resume,
        applied=None,
        skipped=None,
    ):
        self.resume = resume
        self.applied = applied or []
        self.skipped = skipped or []