"""
Unit tests for ResumeBuilder.

These tests verify renderer registration and pipeline behavior.
"""

from resumeforge.builder import ResumeBuilder
from resumeforge.loader import load_resume
from resumeforge.templates.base import BaseTemplate


def test_builder_accepts_custom_renderers():
    calls = []

    class FakeRenderer:
        def render(self, document, resume):
            calls.append("called")

    builder = ResumeBuilder([FakeRenderer()])

    builder.render(load_resume())

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