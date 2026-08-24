from pathlib import Path

from resumeforge.loader import load_resume
from resumeforge.builder import ResumeBuilder
from resumeforge.sections import header, summary


def test_build_resume():
    resume = load_resume()

    builder = ResumeBuilder()

    header.render(builder.document, resume)
    summary.render(builder.document, resume)

    output = Path("output") / "test_resume.docx"

    builder.save(output)

    assert output.exists()

    # Clean up after the test
    output.unlink(missing_ok=True)