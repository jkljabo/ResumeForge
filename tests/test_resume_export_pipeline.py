from types import SimpleNamespace

from resumeforge.output.resume_writer import ResumeWriter
from resumeforge.renderers.markdown_renderer import MarkdownRenderer
from resumeforge.resume.builder import ResumeBuilder

def test_resume_can_be_exported(tmp_path):
    profile = SimpleNamespace(
        summary="Senior Software Engineer",
        skills=[
            "Python",
            "C#",
        ],
        experience=[],
        education=[],
        certifications=[],
        projects=[],
    )

    builder = ResumeBuilder()
    resume = builder.build(profile)

    renderer = MarkdownRenderer()
    markdown = renderer.render(resume)

    output = tmp_path / "resume.md"

    writer = ResumeWriter()
    writer.write(
        markdown,
        output,
    )

    assert output.exists()

    contents = output.read_text(encoding="utf-8")

    assert contents == markdown
    assert "# Resume" in contents
    assert "Senior Software Engineer" in contents
    assert "Python" in contents
    assert "C#" in contents