from docx import Document

from resumeforge.loader import load_resume

from resumeforge.renderers.base import BaseRenderer
from resumeforge.renderers.header import HeaderRenderer
from resumeforge.renderers.summary import SummaryRenderer
from resumeforge.renderers.experience import ExperienceRenderer
from resumeforge.renderers.education import EducationRenderer
from resumeforge.renderers.skills import SkillsRenderer

def test_header_renderer_is_base_renderer():
    assert issubclass(HeaderRenderer, BaseRenderer)

def test_summary_renderer_is_base_renderer():
    assert issubclass(SummaryRenderer, BaseRenderer)

def test_experience_renderer_is_base_renderer():
    assert issubclass(ExperienceRenderer, BaseRenderer)

def test_education_renderer_is_base_renderer():
    assert issubclass(EducationRenderer, BaseRenderer)

def test_skills_renderer_is_base_renderer():
    assert issubclass(SkillsRenderer, BaseRenderer)


def test_experience_renderer_runs():
    document = Document()
    resume = load_resume()

    renderer = ExperienceRenderer()

    renderer.render(document, resume)

    assert document is not None

def test_education_renderer_runs():

    document = Document()

    resume = load_resume()

    renderer = EducationRenderer()

    renderer.render(document, resume)

    assert "Education" in "\n".join(p.text for p in document.paragraphs)

def test_skills_renderer_runs():

    document = Document()

    resume = load_resume()

    renderer = SkillsRenderer()

    renderer.render(document, resume)

    text = "\n".join(p.text for p in document.paragraphs)

    assert "Technical Skills" in text
    assert "C#" in text
