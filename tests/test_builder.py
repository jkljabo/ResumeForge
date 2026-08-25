"""
Unit tests for ResumeBuilder.

These tests verify renderer registration and pipeline behavior.
"""

from resumeforge.builder import ResumeBuilder
from resumeforge.loader import load_resume


def test_builder_accepts_custom_renderers():
    calls = []

    def fake_renderer(document, resume):
        calls.append("called")

    builder = ResumeBuilder(renderers=[fake_renderer])

    builder.render(load_resume())

    assert calls == ["called"]