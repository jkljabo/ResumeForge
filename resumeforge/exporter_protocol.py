from typing import Protocol, runtime_checkable


@runtime_checkable
class ResumeExporterProtocol(Protocol):

    def export(
        self,
        resume,
        destination,
    ) -> None:
        ...