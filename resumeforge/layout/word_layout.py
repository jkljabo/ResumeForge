from .base import BaseLayout


class WordLayout(BaseLayout):

    def __init__(self, document):
        self.document = document

    def heading(self, text, level=1):
        return self.document.add_heading(text, level)

    def paragraph(self, text="", style=None):
        return self.document.add_paragraph(text, style)