from docx.shared import Pt, RGBColor

from .base import BaseTheme


class DarkTheme(BaseTheme):
    def apply(self, document):
        styles = document.styles

        normal = styles["Normal"]
        normal.font.name = "Segoe UI"
        normal.font.size = Pt(11)
        normal.font.color.rgb = RGBColor(240, 240, 240)

        heading = styles["Heading 1"]
        heading.font.name = "Segoe UI"
        heading.font.size = Pt(16)
        heading.font.bold = True
        heading.font.color.rgb = RGBColor(0, 200, 255)