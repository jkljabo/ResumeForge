from types import SimpleNamespace

from resumeforge.scoring import Matcher


def test_matcher_can_be_created():
    matcher = Matcher()

    assert matcher is not None


def test_score_returns_integer():
    matcher = Matcher()

    score = matcher.score(None, "")

    assert isinstance(score, int)

def test_score_returns_zero_for_empty_job_description():
    matcher = Matcher()
    resume = SimpleNamespace(skills=[], experience=[], projects=[], certifications=[])

    assert matcher.score(resume, "") == 0


def test_score_counts_matching_skill_tags():
    matcher = Matcher()
    resume = SimpleNamespace(
        skills=[
            SimpleNamespace(tags=["azure", ".net"]),
        ],
        experience=[],
        projects=[],
        certifications=[],
    )

    score = matcher.score(
        resume,
        "Looking for Azure and .NET experience"
    )

    assert score == 2