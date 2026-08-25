from resumeforge.domain import Experience


def test_experience_model():
    exp = Experience(
        employer="CoffeeTree Software",
        title="Senior Software Engineer",
        location="Remote",
        start_date="2025",
        end_date="2026",
        summary="Modernized enterprise applications.",
        accomplishments=[
            "Migrated legacy systems to Azure",
            "Improved security and uptime",
        ],
        technologies=["C#", ".NET", "Azure"],
    )

    assert exp.employer == "CoffeeTree Software"
    assert "Azure" in exp.technologies