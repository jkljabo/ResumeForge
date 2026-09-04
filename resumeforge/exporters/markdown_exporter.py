
from resumeforge.exporters.exporter import ResumeExporter
from resumeforge.renderers.markdown_resume_renderer import (
    MarkdownResumeRenderer,
)


class MarkdownExporter(ResumeExporter):

    def __init__(self, renderer=None):
        self.renderer = renderer or MarkdownResumeRenderer()

    def export(self, document) -> str:

        return self.renderer.render(document)