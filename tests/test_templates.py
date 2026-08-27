from resumeforge.templates import BaseTemplate, DefaultTemplate


def test_default_template_is_base_template():
    assert issubclass(DefaultTemplate, BaseTemplate)