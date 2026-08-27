from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Pt

from resumeforge.renderers.base import BaseRenderer


class HeaderRenderer(BaseRenderer):

    def render(self, layout, resume):
        header = resume.header

        title = layout.heading(header.name, 0)
        title.alignment = WD_ALIGN_PARAGRAPH.CENTER

        p = layout.paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER

        run = p.add_run(header.headline + "\n")
        run.bold = True
        run.font.size = Pt(14)

        p.add_run(header.tagline)