from resumeforge.resume.document import ResumeDocument


class ResumeGenerator:

    def __init__(
        self,
        matcher,
        tailoring_engine,
        builder,
        exporter,
        writer,
    ):
        self.matcher = matcher
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