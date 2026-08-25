from resumeforge.domain import Summary


def test_summary_model():

    summary = Summary(
        text="Senior Software Engineer with 20+ years of experience."
    )

    assert summary.text.startswith("Senior")