from .base import BaseLayout


class WordLayout(BaseLayout):

    def __init__(self, document, theme = None):
        self.document = document
        self.theme = theme

    def heading(self, text: str, level: int = 1):
        paragraph = self.document.add_heading(text, level)

        if self.theme:
            self.theme.style_heading(paragraph, level)

        return paragraph

    def paragraph(self, text: str = "", style = None):
        paragraph = self.document.add_paragraph(text, style)

        if self.theme:
            self.theme.style_paragraph(paragraph)

        return paragraph

    def bullet(self, text: str = ""):
        paragraph = self.document.add_paragraph(
            text,
            style="List Bullet",
        )

        if self.theme:
            self.theme.style_bullet(paragraph)

        return paragraph

    def bold(self, paragraph, text: str):
        run = paragraph.add_run(text)
        run.bold = True
        return run

    def text(self, paragraph, text: str):
            return paragraph.add_run(text)
    
    def line(self, text: str = ""):
        return self.document.add_paragraph(text)

    