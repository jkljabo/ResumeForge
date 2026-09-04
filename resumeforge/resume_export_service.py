class ResumeExportService:

    def __init__(
        self,
        exporter=None,
    ):
        self.exporter = (
            exporter
            or MarkdownExporter()
        )