from docx.shared import Inches, Pt

from resumeforge.templates.default import DefaultTemplate


class ModernTemplate(DefaultTemplate):
    def apply(self, document):
        super().apply(document)

        section = document.sections[0]
        section.top_margin = Inches(0.5)
        section.bottom_margin = Inches(0.5)
        section.left_margin = Inches(0.6)
        section.right_margin = Inches(0.6)

        normal = document.styles["Normal"]
        normal.font.size = Pt(10)
        normal.paragraph_format.space_after = Pt(1)

        heading1 = document.styles["Heading 1"]
        heading1.font.size = Pt(12.5)
        heading1.paragraph_format.space_before = Pt(4)
        heading1.paragraph_format.space_after = Pt(2)