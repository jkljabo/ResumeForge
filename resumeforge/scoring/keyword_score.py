class KeywordScore:

    def __init__(
        self,
        keyword: str,
        matched: bool,
        score: float = 0.0,
    ):
        self.keyword = keyword
        self.matched = matched
        self.score = score