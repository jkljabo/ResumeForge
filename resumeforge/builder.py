from docx import Document

from resumeforge.sections import header
from resumeforge.sections import summary


class ResumeBuilder:

    def __init__(self):
        self.document = Document()

    def render(self, resume):
        header.render(self.document, resume)
        summary.render(self.document, resume)

    def save(self, filename):
        self.document.save(filename)