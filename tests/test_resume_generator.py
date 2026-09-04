
from tests.helpers import make_resume

from resumeforge.generator import ResumeGenerator


class FakeMatcher:

    def __init__(self):
        self.called = False

    def match(
        self,
        profile,
        job,
    ):
        self.called = True
        return "match"

class FakeTailoringEngine:

    def __init__(self):
        self.called = False

    def create_plan(
        self,
        profile,
        match,
    ):
        self.called = True
        return "plan"

class FakeBuilder:

    def __init__(self):
        self.called = False

    def build(
        self,
        profile,
        plan,
    ):
        self.called = True
        return "document"
      
class FakeExporter:

    def __init__(self):
        self.called = False
        self.document = None

    def export(self, document):
        self.called = True
        self.document = document
        return "# Resume"

class FakeWriter:

    def __init__(self):
        self.called = False
        self.markdown = None
        self.destination = None

    def write(self, markdown, destination):
        self.called = True
        self.markdown = markdown
        self.destination = destination

def make_generator():

    matcher = FakeMatcher()
    tailoring = FakeTailoringEngine()
    builder = FakeBuilder()
    exporter = FakeExporter()
    writer = FakeWriter()

    generator = ResumeGenerator(
        matcher=matcher,
        tailoring_engine=tailoring,
        builder=builder,
        exporter=exporter,
        writer=writer,
    )

    return (
        generator,
        matcher,
        tailoring,
        builder,
        exporter,
        writer,
    )

def test_can_create_resume_generator():

    generator, *_ = make_generator()

    assert generator is not None

def test_generate_orchestrates_resume_pipeline():

    generator, matcher, tailoring, builder, exporter, writer = make_generator()

    generator.generate(
        make_resume(),
        "Python Azure Developer",
        "resume.md",
    )

    assert matcher.called
    assert tailoring.called
    assert builder.called
    assert exporter.called
    assert writer.called

    assert writer.markdown == "# Resume"
    assert writer.destination == "resume.md"
    assert exporter.document == "document"

def test_generate_returns_document():

    generator, *_ = make_generator()

    document = generator.generate(
        make_resume(),
        "Python Azure Developer",
        "resume.md",
    )

    assert document == "document"
    
