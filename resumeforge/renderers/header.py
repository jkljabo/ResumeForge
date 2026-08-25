from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Pt


class HeaderRenderer:
    def render(self, document, resume):
        header = resume.header

        title = document.add_heading(header.name, 0)
        title.alignment = WD_ALIGN_PARAGRAPH.CENTER

        p = document.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER

        run = p.add_run(header.headline + "\n")
        run.bold = True
        run.font.size = Pt(14)

        p.add_run(header.tagline)