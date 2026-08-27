from docx.shared import Inches, Pt

from resumeforge.templates.default import DefaultTemplate


class ExecutiveTemplate(DefaultTemplate):
    def apply(self, document):
        super().apply(document)

        section = document.sections[0]
        section.top_margin = Inches(0.45)
        section.bottom_margin = Inches(0.45)
        section.left_margin = Inches(0.65)
        section.right_margin = Inches(0.65)

        normal = document.styles["Normal"]
        normal.font.name = "Cambria"
        normal.font.size = Pt(10.5)

        heading1 = document.styles["Heading 1"]
        heading1.font.name = "Cambria"
        heading1.font.size = Pt(14)
        heading1.font.bold = True