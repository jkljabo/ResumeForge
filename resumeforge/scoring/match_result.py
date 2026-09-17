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
        recommendations=None,
        keyword_scores=None,
        total_keywords=0,
    ):
        self.score = score
        self.matched = matched or []
        self.missing = missing or []
        self.section_scores = section_scores or {}
        self.coverage = coverage
        self.matched_by_section = matched_by_section or {}
        self.missing_by_section = missing_by_section or {}

        self.recommendations = recommendations or []
        self.keyword_scores = keyword_scores or {}
        self.total_keywords = total_keywords

    @property
    def matched_count(self):
        return len(self.matched)

    @property
    def missing_count(self):
        return len(self.missing)

    @property
    def total_matches(self):
        return self.matched_count + self.missing_count

    @property
    def percent_matched(self):
        if self.total_matches == 0:
            return 0.0

        return (
            self.matched_count
            / self.total_matches
        ) * 100