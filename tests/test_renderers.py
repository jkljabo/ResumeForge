from resumeforge.renderers.base import BaseRenderer
from resumeforge.renderers.header import HeaderRenderer
from resumeforge.renderers.summary import SummaryRenderer


def test_header_renderer_is_base_renderer():
    assert issubclass(HeaderRenderer, BaseRenderer)


def test_summary_renderer_is_base_renderer():
    assert issubclass(SummaryRenderer, BaseRenderer)