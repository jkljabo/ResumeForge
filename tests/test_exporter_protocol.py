from resumeforge.exporter_protocol import (
    ResumeExporterProtocol,
)


class FakeExporter:

    def export(
        self,
        resume,
        destination,
    ):
        pass


def test_fake_exporter_satisfies_protocol():
    assert isinstance(
        FakeExporter(),
        ResumeExporterProtocol,
    )