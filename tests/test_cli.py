from build_resume import TEMPLATES


def test_default_template_exists():
    assert "default" in TEMPLATES


def test_modern_template_exists():
    assert "modern" in TEMPLATES

def test_executive_template_exists():
    assert "executive" in TEMPLATES