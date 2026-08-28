from build_resume import build_parser

from build_resume import TEMPLATES, THEMES

def test_corporate_theme_exists():
    assert "corporate" in THEMES

def test_dark_theme_exists():
    assert "dark" in THEMES
    
def test_default_template_exists():
    assert "default" in TEMPLATES


def test_modern_template_exists():
    assert "modern" in TEMPLATES

def test_executive_template_exists():
    assert "executive" in TEMPLATES

def test_job_argument_exists():
    parser = build_parser()

    args = parser.parse_args(
        ["--job", "jobs/test.txt"]
    )

    assert args.job == "jobs/test.txt"