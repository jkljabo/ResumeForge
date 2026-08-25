from resumeforge.domain import Project


def test_project_model():
    project = Project(
        name="ResumeForge",
        description="Generate tailored resumes from structured data.",
        technologies=["Python", "pytest", "python-docx"],
        url="https://github.com/jkljabo/ResumeForge",
    )

    assert project.name == "ResumeForge"
    assert "Python" in project.technologies