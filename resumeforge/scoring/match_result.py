class MatchResult:
    def __init__(
        self,
        score=0,
        matched=None,
        missing=None,
        section_scores=None,
        coverage=0.0,
        matched_by_section=None,
        missing_by_section=None,
    ):
        self.score = score
        self.matched = matched or []
        self.missing = missing or []
        self.section_scores = section_scores or {}
        self.coverage = coverage
        self.matched_by_section = matched_by_section or {}
        self.missing_by_section = (
            missing_by_section or {}
        )