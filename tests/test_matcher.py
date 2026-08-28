from resumeforge.scoring import Matcher


def test_matcher_can_be_created():
    matcher = Matcher()

    assert matcher is not None


def test_score_returns_integer():
    matcher = Matcher()

    score = matcher.score(None, "")

    assert isinstance(score, int)