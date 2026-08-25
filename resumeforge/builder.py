from docx import Document

from resumeforge.renderers import header
from resumeforge.renderers import summary

DEFAULT_RENDERERS = [
    header.render,
    summary.render,
]


class ResumeBuilder:
    def __init__(self, renderers=None):
        self.document = Document()
        self.renderers = list(renderers) if renderers is not None else DEFAULT_RENDERERS.copy()

    def render(self, resume):
        for renderer in self.renderers:
            renderer(self.document, resume)

    def add_renderer(self, renderer):
        self.renderers.append(renderer)

    def save(self, filename):
        self.document.save(filename)