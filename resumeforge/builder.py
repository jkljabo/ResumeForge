from docx import Document

from resumeforge.sections import header
from resumeforge.sections import summary


class ResumeBuilder:
    def __init__(self):
        self.document = Document()
        self.renderers = [
            header.render,
            summary.render,
        ]

    def render(self, resume):
        for renderer in self.renderers:
            renderer(self.document, resume)

    def add_renderer(self, renderer):
        self.renderers.append(renderer)

    def save(self, filename):
        self.document.save(filename)