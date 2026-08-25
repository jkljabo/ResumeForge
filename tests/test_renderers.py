from docx import Document

from resumeforge.loader import load_resume

from resumeforge.renderers.base import BaseRenderer
from resumeforge.renderers.header import HeaderRenderer
from resumeforge.renderers.summary import SummaryRenderer
from resumeforge.renderers.experience import ExperienceRenderer


def test_header_renderer_is_base_renderer():
    assert issubclass(HeaderRenderer, BaseRenderer)


def test_summary_renderer_is_base_renderer():
    assert issubclass(SummaryRenderer, BaseRenderer)


def test_experience_renderer_is_base_renderer():
    assert issubclass(ExperienceRenderer, BaseRenderer)


def test_experience_renderer_runs():
    document = Document()
    resume = load_resume()

    renderer = ExperienceRenderer()

    renderer.render(document, resume)

    assert document is not None