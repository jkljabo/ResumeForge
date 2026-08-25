from docx import Document

from resumeforge.renderers.header import HeaderRenderer
from resumeforge.renderers.summary import SummaryRenderer
from resumeforge.renderers.experience import ExperienceRenderer
from resumeforge.renderers.education import EducationRenderer
from resumeforge.renderers.skills import SkillsRenderer


DEFAULT_RENDERERS = [
    HeaderRenderer(),
    SummaryRenderer(),
    ExperienceRenderer(),
    EducationRenderer(),
    SkillsRenderer(),
]

class ResumeBuilder:
    def __init__(self, renderers=None):
        self.document = Document()
        self.renderers = list(renderers) if renderers is not None else DEFAULT_RENDERERS.copy()

    def render(self, resume):
        for renderer in self.renderers:
            renderer.render(self.document, resume)

    def add_renderer(self, renderer):
        self.renderers.append(renderer)

    def save(self, filename):
        self.document.save(filename)