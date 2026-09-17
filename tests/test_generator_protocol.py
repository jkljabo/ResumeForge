from resumeforge.generator import ResumeGenerator
from resumeforge.generator_protocol import ResumeGeneratorProtocol


def test_resume_generator_satisfies_protocol():
    assert issubclass(
        ResumeGenerator,
        ResumeGeneratorProtocol,
    )