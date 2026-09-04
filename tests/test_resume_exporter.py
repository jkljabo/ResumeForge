from resumeforge.exporters import MarkdownExporter
from tests.helpers import make_document

class DummyRenderer:

    def render(self, document):
        return "dummy output"
    
def test_export_returns_string():

    exporter = MarkdownExporter()

    result = exporter.export(
        make_document(),
    )

    assert isinstance(result, str)

def test_export_contains_name():

    exporter = MarkdownExporter()

    markdown = exporter.export(
        make_document(name="Jason Little"),
    )

    assert "Jason Little" in markdown

def test_export_uses_renderer():

    exporter = MarkdownExporter(
        renderer=DummyRenderer(),
    )

    assert exporter.export(None) == "dummy output"

