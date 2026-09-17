from typing import Protocol, runtime_checkable


@runtime_checkable
class MatcherProtocol(Protocol):

    def match(
        self,
        resume,
        job_description,
    ):
        ...