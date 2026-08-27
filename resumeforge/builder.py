from docx import Document

from resumeforge.renderers.header import HeaderRenderer
from resumeforge.renderers.summary import SummaryRenderer
from resumeforge.renderers.experience import ExperienceRenderer
from resumeforge.renderers.education import EducationRenderer
from resumeforge.renderers.skills import SkillsRenderer
from resumeforge.renderers.certification import CertificationRenderer
from resumeforge.renderers.project import ProjectRenderer
from resumeforge.templates import DefaultTemplate

DEFAULT_RENDERERS = [
    HeaderRenderer(),
    SummaryRenderer(),
    ExperienceRenderer(),
    EducationRenderer(),
    SkillsRenderer(),
    CertificationRenderer(),
    ProjectRenderer(),
]

class ResumeBuilder:
    def __init__(self, renderers=None, template=None):
        self.document = Document()

        self.template = template or DefaultTemplate()

        self.template.apply(self.document)

        self.renderers = (
            list(renderers)
            if renderers is not None
            else DEFAULT_RENDERERS.copy()
        )
    def render(self, resume):
        for renderer in self.renderers:
            renderer.render(self.document, resume)

    def add_renderer(self, renderer):
        self.renderers.append(renderer)

    def save(self, filename):
        self.document.save(filename)