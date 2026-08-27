from docx import Document
from docx.shared import Inches, Pt

from resumeforge.templates import BaseTemplate, DefaultTemplate
from resumeforge.templates.default import DefaultTemplate
from resumeforge.templates.modern import ModernTemplate


def test_default_template_is_base_template():
    assert issubclass(DefaultTemplate, BaseTemplate)

def test_modern_template_is_base_template():
    assert issubclass(ModernTemplate, BaseTemplate)


def test_default_template_applies_document_styles():
    document = Document()
    DefaultTemplate().apply(document)

    section = document.sections[0]
    assert section.top_margin == Inches(0.6)
    assert section.left_margin == Inches(0.75)
    assert document.styles["Normal"].font.name == "Calibri"
    assert document.styles["Normal"].font.size == Pt(10.5)

def test_modern_template_applies_tighter_margins():
    document = Document()
    ModernTemplate().apply(document)

    section = document.sections[0]
    assert section.left_margin == Inches(0.6)
    assert section.top_margin == Inches(0.5)