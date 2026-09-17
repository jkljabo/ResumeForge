from resumeforge.output.resume_writer import ResumeWriter
from resumeforge.resume.builder import ResumeBuilder
from resumeforge.resume.document import ResumeDocument
from resumeforge.generator_protocol import ResumeGeneratorProtocol
from resumeforge.scoring.matcher_protocol import MatcherProtocol
from resumeforge.tailoring.protocol import TailoringEngineProtocol
from resumeforge.exporter_protocol import ResumeExporterProtocol
from resumeforge.recommendations.engine import RecommendationEngine


class ResumeGenerator:

    def __init__(
        self,
        matcher: MatcherProtocol,
        recommendation_engine: RecommendationEngine,
        tailoring_engine: TailoringEngineProtocol,
        builder: ResumeBuilder,
        exporter: ResumeExporterProtocol,
        writer: ResumeWriter,
    ):
        self.matcher = matcher
        self.recommendation_engine = recommendation_engine
        self.tailoring_engine = tailoring_engine
        self.builder = builder
        self.exporter = exporter
        self.writer = writer

    def generate(
        self,
        profile,
        job,
        destination,
    ) -> ResumeDocument:
        """Generate a tailored resume and write it to the destination."""
        match = self.matcher.match(
            profile,
            job,
        )

        match.recommendations = (
            self.recommendation_engine.recommend(
                match,
            )
        )

        plan = self.tailoring_engine.create_plan(
            profile,
            match,
        )

        document = self.builder.build(
            profile,
            plan,
        )

        markdown = self.exporter.export(
            document,
        )

        self.writer.write(
            markdown,
            destination,
        )

        return document