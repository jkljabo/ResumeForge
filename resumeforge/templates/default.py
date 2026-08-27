from docx.shared import Inches, Pt

from resumeforge.templates.base import BaseTemplate


class DefaultTemplate(BaseTemplate):
    def apply(self, document):
        section = document.sections[0]
        section.top_margin = Inches(0.6)
        section.bottom_margin = Inches(0.6)
        section.left_margin = Inches(0.75)
        section.right_margin = Inches(0.75)

        normal = document.styles["Normal"]
        normal.font.name = "Calibri"
        normal.font.size = Pt(10.5)
        normal.paragraph_format.space_after = Pt(0)
        normal.paragraph_format.line_spacing = 1.0

        for style_name, size in (("Heading 1", 13), ("Heading 2", 11)):
            style = document.styles[style_name]
            style.font.name = "Calibri"
            style.font.bold = True
            style.font.size = Pt(size)
            style.paragraph_format.space_before = Pt(6)
            style.paragraph_format.space_after = Pt(3)