from resumeforge.renderers.base import BaseRenderer


class SummaryRenderer(BaseRenderer):

    def render(self, layout, resume):

        layout.heading("Executive Summary", 1)

        layout.paragraph(
            "Senior Software Engineer with more than twenty years..."
        )