from resumeforge.scoring.factory import create_matcher
from resumeforge.scoring import Matcher


def test_create_matcher():
    matcher = create_matcher()

    assert isinstance(matcher, Matcher)