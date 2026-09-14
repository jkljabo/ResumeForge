from resumeforge import generator
from resumeforge.factory import create_resume_generator
from resumeforge.generator import ResumeGenerator
from resumeforge.scoring import Matcher
from resumeforge.exporters import MarkdownExporter
from resumeforge.output.resume_writer import ResumeWriter
from resumeforge.tailoring.engine import TailoringEngine
from resumeforge.tailoring.tailored_resume_builder import (
    TailoredResumeBuilder,
)


def test_create_resume_generator_builds_complete_object_graph():
    generator = create_resume_generator()

    assert isinstance(generator.matcher, Matcher)
    assert isinstance(generator.tailoring_engine, TailoringEngine)
    assert isinstance(generator.builder, TailoredResumeBuilder)
    assert isinstance(generator.exporter, MarkdownExporter)
    assert isinstance(generator.writer, ResumeWriter)