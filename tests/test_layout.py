from docx import Document

from resumeforge.layout import BaseLayout, WordLayout


def test_word_layout_is_base_layout():
    assert issubclass(WordLayout, BaseLayout)


def test_word_layout_creates_heading():
    document = Document()

    layout = WordLayout(document)

    layout.heading("Hello")

    assert "Hello" in "\n".join(
        p.text for p in document.paragraphs
    )