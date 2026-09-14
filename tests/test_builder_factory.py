from resumeforge.resume.factory import create_builder
from resumeforge.tailoring.tailored_resume_builder import (
    TailoredResumeBuilder,
)


def test_create_builder():
    builder = create_builder()

    assert isinstance(
        builder,
        TailoredResumeBuilder,
    )