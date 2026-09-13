"""
Integration tests for the build process.

These tests verify that ResumeForge can generate a Word document.
"""

from tests.helpers import make_resume_profile

from resumeforge.builder import ResumeBuilder
from resumeforge.resume.factory import create_resume_service


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

    class FakeResumeService:
        def load(self, path):
            return make_resume_profile()

    monkeypatch.setattr(
        build_resume,
        "create_resume_service",
        lambda: FakeResumeService(),
    )

    monkeypatch.setattr(
        "sys.argv",
        [
            "build_resume.py",
            "generate",
            "--template",
            "modern",
            "--theme",
            "corporate",
            "--output",
            str(output),
        ],
    )

    build_resume.main()

    assert output.exists()