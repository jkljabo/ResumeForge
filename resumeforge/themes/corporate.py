from docx.shared import Pt
from docx.enum.style import WD_STYLE_TYPE

from .base import BaseTheme


class CorporateTheme(BaseTheme):
    def apply(self, document):
        styles = document.styles

        normal = styles["Normal"]
        normal.font.name = "Calibri"
        normal.font.size = Pt(11)

        if "Heading 1" in styles:
            heading = styles["Heading 1"]
            heading.font.name = "Calibri"
            heading.font.size = Pt(16)
            heading.font.bold = True