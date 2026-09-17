from resumeforge.scoring import KeywordScore


def test_keyword_score_properties():
    score = KeywordScore(
        keyword="Azure",
        score=0.95,
        matched=True,
    )

    assert score.keyword == "Azure"
    assert score.score == 0.95
    assert score.matched is True