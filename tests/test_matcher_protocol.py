from resumeforge.scoring.matcher_protocol import (
    MatcherProtocol,
)


class FakeMatcher:

    def match(
        self,
        resume,
        job_description,
    ):
        return None


def test_fake_matcher_satisfies_protocol():
    assert isinstance(
        FakeMatcher(),
        MatcherProtocol,
    )