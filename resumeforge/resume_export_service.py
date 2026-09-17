from resumeforge.exporters.markdown_exporter import MarkdownExporter
from resumeforge.exporter_protocol import ResumeExporterProtocol


class ResumeExportService:

    def __init__(
        self,
        exporter: ResumeExporterProtocol | None = None,
    ):
        self.exporter = (
            exporter
            or MarkdownExporter()
        )