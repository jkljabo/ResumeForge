from docx import Document

class ResumeBuilder:

    def __init__(self):
        self.document = Document()

    def save(self, filename):
        self.document.save(filename)