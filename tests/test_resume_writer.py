from types import SimpleNamespace

from resumeforge.output.resume_writer import ResumeWriter


def test_writer_creates_file(tmp_path):
    writer = ResumeWriter()

    output = tmp_path / "resume.md"

    writer.write(
        "# Resume",
        output,
    )

    assert output.exists()

def test_writer_saves_contents(tmp_path):
    writer = ResumeWriter()

    output = tmp_path / "resume.md"

    writer.write(
        "# Resume",
        output,
    )

    assert output.read_text(
        encoding="utf-8"
    ) == "# Resume"

def test_writer_returns_path(tmp_path):
    writer = ResumeWriter()

    output = tmp_path / "resume.md"

    result = writer.write(
        "abc",
        output,
    )

    assert result == output

def test_writer_creates_parent_directories(tmp_path):
    writer = ResumeWriter()

    output = (
        tmp_path
        / "generated"
        / "resume.md"
    )

    writer.write(
        "resume",
        output,
    )

    assert output.exists()

