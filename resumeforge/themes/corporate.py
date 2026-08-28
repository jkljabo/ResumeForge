from docx.shared import Inches, Pt, RGBColor

from .base import BaseTheme


class CorporateTheme(BaseTheme):
    def apply(self, document):
        section = document.sections[0]
        section.top_margin = Inches(0.6)
        section.bottom_margin = Inches(0.6)
        section.left_margin = Inches(0.75)
        section.right_margin = Inches(0.75)

        styles = document.styles

        normal = styles["Normal"]
        normal.font.name = "Calibri"
        normal.font.size = Pt(11)

        heading1 = styles["Heading 1"]
        heading1.font.name = "Calibri"
        heading1.font.bold = True
        heading1.font.size = Pt(16)
        heading1.font.color.rgb = RGBColor(0, 51, 102)
        heading1.paragraph_format.space_before = Pt(12)
        heading1.paragraph_format.space_after = Pt(6)

        heading2 = styles["Heading 2"]
        heading2.font.name = "Calibri"
        heading2.font.bold = True
        heading2.font.size = Pt(12)
        heading2.font.color.rgb = RGBColor(0, 76, 153)
        heading2.paragraph_format.space_before = Pt(6)
        heading2.paragraph_format.space_after = Pt(3)

    def style_heading(self, paragraph, level):
        if level == 1:
            paragraph.paragraph_format.space_before = Pt(12)
            paragraph.paragraph_format.space_after = Pt(6)

    def style_bullet(self, paragraph):
        paragraph.paragraph_format.space_after = Pt(2)

    def style_paragraph(self, paragraph):
        paragraph.paragraph_format.space_after = Pt(1)