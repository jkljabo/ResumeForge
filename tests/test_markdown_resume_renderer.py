from tests.helpers import make_document

from resumeforge.renderers.markdown_resume_renderer import MarkdownResumeRenderer


def test_renderer_returns_string():

    renderer = MarkdownResumeRenderer()

    result = renderer.render(None)

    assert result == ""

def test_empty_document_renders_empty():

    renderer = MarkdownResumeRenderer()

    document = make_document()

    markdown = renderer.render(document)

    assert markdown == ""

def test_renderer_renders_name():

    renderer = MarkdownResumeRenderer()

    document = make_document(
        name="Jason Little",
    )

    markdown = renderer.render(document)

    assert "# Jason Little" in markdown

def test_renderer_renders_email():

    renderer = MarkdownResumeRenderer()

    document = make_document(
        email="jason@example.com",
    )

    markdown = renderer.render(document)

    assert "jason@example.com" in markdown

def test_renderer_renders_phone():

    renderer = MarkdownResumeRenderer()

    document = make_document(
        phone="555-555-5555",
    )

    markdown = renderer.render(document)

    assert "555-555-5555" in markdown

def test_renderer_renders_contact_header():

    renderer = MarkdownResumeRenderer()

    document = make_document(
        name="Jason Little",
        email="jason@example.com",
        phone="555-555-5555",
    )

    markdown = renderer.render(document)

    assert markdown == (
        "# Jason Little\n\n"
        "jason@example.com\n"
        "555-555-5555"
    )

def test_renderer_renders_summary_heading():

    renderer = MarkdownResumeRenderer()

    document = make_document(
        summary="Experienced software engineer.",
    )

    markdown = renderer.render(document)

    assert "## Professional Summary" in markdown

def test_renderer_renders_summary_text():

    renderer = MarkdownResumeRenderer()

    document = make_document(
        summary="Experienced software engineer.",
    )

    markdown = renderer.render(document)

    assert "Experienced software engineer." in markdown

def test_renderer_omits_empty_summary():

    renderer = MarkdownResumeRenderer()

    document = make_document(
        summary="",
    )

    markdown = renderer.render(document)

    assert "Professional Summary" not in markdown

def test_renderer_places_summary_after_contact():

    renderer = MarkdownResumeRenderer()

    document = make_document(
        name="Jason Little",
        email="jason@example.com",
        phone="555-555-5555",
        summary="Experienced software engineer.",
    )

    markdown = renderer.render(document)

    expected = (
        "# Jason Little\n\n"
        "jason@example.com\n"
        "555-555-5555\n\n"
        "## Professional Summary\n\n"
        "Experienced software engineer."
    )

    assert markdown == expected

def test_renderer_renders_skills_heading():

    renderer = MarkdownResumeRenderer()

    document = make_document(
        skills=[
            "C#",
        ],
    )

    markdown = renderer.render(document)

    assert "## Skills" in markdown

def test_renderer_renders_single_skill():

    renderer = MarkdownResumeRenderer()

    document = make_document(
        skills=[
            "Azure",
        ],
    )

    markdown = renderer.render(document)

    assert "- Azure" in markdown

def test_renderer_renders_multiple_skills():

    renderer = MarkdownResumeRenderer()

    document = make_document(
        skills=[
            "C#",
            ".NET",
            "Azure",
        ],
    )

    markdown = renderer.render(document)

    assert "- C#" in markdown
    assert "- .NET" in markdown
    assert "- Azure" in markdown

def test_renderer_omits_empty_skills():

    renderer = MarkdownResumeRenderer()

    document = make_document(
        skills=[],
    )

    markdown = renderer.render(document)

    assert "## Skills" not in markdown

def test_renderer_places_skills_after_summary():

    renderer = MarkdownResumeRenderer()

    document = make_document(
        summary="Experienced engineer.",
        skills=[
            "Azure",
        ],
    )

    markdown = renderer.render(document)

    expected = (
        "## Professional Summary\n\n"
        "Experienced engineer.\n\n"
        "## Skills\n\n"
        "- Azure"
    )

    assert expected in markdown

