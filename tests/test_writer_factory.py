from resumeforge.output.factory import create_writer
from resumeforge.output.resume_writer import ResumeWriter


def test_create_writer():
    writer = create_writer()

    assert isinstance(writer, ResumeWriter)