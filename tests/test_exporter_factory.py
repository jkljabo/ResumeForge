from resumeforge.output.factory import create_exporter
from resumeforge.exporters import MarkdownExporter


def test_create_exporter():
    exporter = create_exporter()

    assert isinstance(
        exporter,
        MarkdownExporter,
    )