from resumeforge.reporting.report_renderer import ReportRenderer
from resumeforge.scoring.match_result import MatchResult


def test_render_basic_report():
    result = MatchResult(
        score=86,
        coverage=71.4,
        matched=[
            "microservices",
            "azure",
            "blazor",
        ],
        missing=[
            "terraform",
            "docker",
        ],
        section_scores={
            "skills": 40,
            "experience": 32,
            "projects": 10,
            "certifications": 4,
        },
        matched_by_section={
            "skills": ["blazor", "azure"],
            "experience": ["microservices"],
            "projects": [],
            "certifications": [],
        },
        missing_by_section={
            "skills": ["docker"],
            "experience": [],
            "projects": ["terraform"],
            "certifications": [],
        },
    )

    renderer = ReportRenderer()

    report = renderer.render(result)

    assert "Resume Match Report" in report
    assert "Overall Score: 86" in report
    assert "Coverage: 71.4%" in report

    assert "Section Scores" in report
    assert "Skills: 40" in report
    assert "Experience: 32" in report
    assert "Projects: 10" in report
    assert "Certifications: 4" in report

    assert "Matched Keywords" in report
    assert "Missing Keywords" in report

    assert "Skills" in report
    assert "Experience" in report
    assert "Projects" in report
    assert "Certifications" in report

    assert "azure" in report
    assert "blazor" in report
    assert "microservices" in report

    assert "docker" in report
    assert "terraform" in report

    assert "\nSkills\n" in report
    assert "azure" in report
    assert "blazor" in report

    assert "\nExperience\n" in report
    assert "microservices" in report

    assert "\nProjects\n" in report
    assert "terraform" in report

    assert "\nCertifications\n" in report
    assert "(none)" in report

    assert report.index("Skills") < report.index("Experience")
    assert report.index("Experience") < report.index("Projects")
    assert report.index("Projects") < report.index("Certifications")

    assert report.index("azure") < report.index("blazor")
    assert report.index("blazor") < report.index("microservices")

    assert report.index("docker") < report.index("terraform")