from docx.shared import Inches, Pt, RGBColor

from resumeforge.themes.base import BaseTheme


class DefaultTheme(BaseTheme):
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

        heading1 = document.styles["Heading 1"]
        heading1.font.name = "Calibri"
        heading1.font.bold = True
        heading1.font.size = Pt(13)
        heading1.font.color.rgb = RGBColor(0, 0, 0)
        heading1.paragraph_format.space_before = Pt(6)
        heading1.paragraph_format.space_after = Pt(3)

        heading2 = document.styles["Heading 2"]
        heading2.font.name = "Calibri"
        heading2.font.bold = True
        heading2.font.size = Pt(11)
        heading2.font.color.rgb = RGBColor(60, 60, 60)
        heading2.paragraph_format.space_before = Pt(4)
        heading2.paragraph_format.space_after = Pt(2)