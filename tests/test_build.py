"""
Integration tests for the build process.

These tests verify that ResumeForge can generate a Word document.
"""

from tests.helpers import make_resume_profile

from resumeforge.builder import ResumeBuilder
from resumeforge.loader import load_resume


def test_build_resume(tmp_path):
    resume = make_resume_profile()

    builder = ResumeBuilder()

    builder.render(resume)

    output = tmp_path / "test_resume.docx"

    builder.save(output)

    assert output.exists()

def test_main_builds_resume(monkeypatch, tmp_path):
    import build_resume

    output = tmp_path / "resume.docx"

    monkeypatch.setattr(
        "sys.argv",
        [
            "build_resume.py",
            "--template",
            "modern",
            "--theme",
            "corporate",
            "--output",
            str(output),
        ],
    )

    monkeypatch.setattr(
        build_resume,
        "load_resume",
        lambda: make_resume_profile(),
    )

    build_resume.main()

    assert output.exists()