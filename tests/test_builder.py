"""
Unit tests for ResumeBuilder.

These tests verify renderer registration and pipeline behavior.
"""

from resumeforge.builder import ResumeBuilder
from resumeforge.loader import load_resume
from resumeforge.profiles import ProfileRepository
from resumeforge.templates.base import BaseTemplate
from resumeforge.layout import WordLayout
from resumeforge.themes.base import BaseTheme


def test_builder_accepts_custom_renderers():
    calls = []

    class FakeRenderer:
        def render(self, document, resume):
            calls.append("called")

    builder = ResumeBuilder([FakeRenderer()])

    repo = ProfileRepository()
    profile = repo.get_default()

    resume = load_resume(profile.resume_path)

    builder.render(resume)
    
    assert calls == ["called"]


class FakeTemplate(BaseTemplate):
    def __init__(self):
        self.called = False

    def apply(self, document):
        self.called = True


def test_builder_accepts_template():
    template = FakeTemplate()

    ResumeBuilder(template=template)

    assert template.called

def test_builder_creates_word_layout():
    builder = ResumeBuilder()

    assert isinstance(builder.layout, WordLayout)
    assert builder.layout.document is builder.document

class FakeTheme(BaseTheme):
    def __init__(self):
        self.called = False

    def apply(self, document):
        self.called = True


def test_builder_accepts_theme():
    theme = FakeTheme()

    ResumeBuilder(theme=theme)

    assert theme.called