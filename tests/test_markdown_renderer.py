from resumeforge.resume.document import ResumeDocument
from resumeforge.renderers.markdown_renderer import MarkdownRenderer


def test_renderer_creates_markdown():

    document = ResumeDocument()

    renderer = MarkdownRenderer()

    markdown = renderer.render(document)

    assert markdown.startswith("# Resume")

def test_renderer_outputs_summary():

    document = ResumeDocument(
        summary="Senior .NET Engineer"
    )

    renderer = MarkdownRenderer()

    markdown = renderer.render(document)

    assert "## Summary" in markdown
    assert "Senior .NET Engineer" in markdown

def test_renderer_outputs_skills():

    document = ResumeDocument(
        skills=[
            "C#",
            ".NET",
            "Azure",
        ]
    )

    renderer = MarkdownRenderer()

    markdown = renderer.render(document)

    assert "## Skills" in markdown

    assert "- C#" in markdown
    assert "- .NET" in markdown
    assert "- Azure" in markdown

def test_renderer_skips_empty_sections():

    document = ResumeDocument()

    renderer = MarkdownRenderer()

    markdown = renderer.render(document)

    assert "## Skills" not in markdown
    assert "## Experience" not in markdown
    assert "## Education" not in markdown
    assert "## Certifications" not in markdown
    assert "## Projects" not in markdown

def test_renderer_outputs_complete_resume():

    document = ResumeDocument(
        summary="Senior Engineer",
        skills=["C#", ".NET"],
        experience=["Software Engineer"],
        education=["BS Computer Science"],
        certifications=["Azure Developer"],
        projects=["ResumeForge"],
    )

    renderer = MarkdownRenderer()

    markdown = renderer.render(document)

    assert "# Resume" in markdown

    assert "## Summary" in markdown
    assert "## Skills" in markdown
    assert "## Experience" in markdown
    assert "## Education" in markdown
    assert "## Certifications" in markdown
    assert "## Projects" in markdown

