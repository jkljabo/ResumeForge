from docx import Document


from resumeforge.themes import (
    BaseTheme,
    DefaultTheme,
    CorporateTheme,
    DarkTheme,
)

def test_default_theme_is_base_theme():
    assert issubclass(DefaultTheme, BaseTheme)

def test_corporate_theme_is_base_theme():
    assert issubclass(CorporateTheme, BaseTheme)

def test_dark_theme_is_base_theme():
    assert issubclass(DarkTheme, BaseTheme)
    
def test_default_theme_applies():
    document = Document()

    theme = DefaultTheme()

    theme.apply(document)

    assert document is not None