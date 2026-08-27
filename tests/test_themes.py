from docx import Document

from resumeforge.themes import BaseTheme, DefaultTheme


def test_default_theme_is_base_theme():
    assert issubclass(DefaultTheme, BaseTheme)


def test_default_theme_applies():
    document = Document()

    theme = DefaultTheme()

    theme.apply(document)

    assert document is not None