from resumeforge.exporters import MarkdownExporter
from resumeforge.generator import ResumeGenerator
from resumeforge.output.resume_writer import ResumeWriter
from resumeforge.scoring import Matcher
from resumeforge.tailoring.engine import TailoringEngine
from resumeforge.tailoring.tailored_resume_builder import (
    TailoredResumeBuilder,
)
from resumeforge.tailoring.factory import (
    create_tailoring_engine,
)

def create_generator() -> ResumeGenerator:
    """Construct the ResumeForge generation pipeline."""
    matcher = Matcher()

    tailoring_engine = create_tailoring_engine()

    builder = TailoredResumeBuilder()

    exporter = MarkdownExporter()

    writer = ResumeWriter()

    return ResumeGenerator(
        matcher=matcher,
        tailoring_engine=tailoring_engine,
        builder=builder,
        exporter=exporter,
        writer=writer,
    )