from .base import BaseLayout


class WordLayout(BaseLayout):

    def __init__(self, document):
        self.document = document

    def heading(self, text: str, level: int = 1):
        return self.document.add_heading(text, level)

    def paragraph(self, text: str = "", style = None):
        return self.document.add_paragraph(text, style)

    def bullet(self, text: str = ""):
        return self.document.add_paragraph(text, style = "List Bullet")

    def bold(self, paragraph, text: str):
        run = paragraph.add_run(text)
        run.bold = True
        return run

    def text(self, paragraph, text: str):
            return paragraph.add_run(text)
    
    def line(self, text: str = ""):
        return self.document.add_paragraph(text)

    