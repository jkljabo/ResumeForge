from types import SimpleNamespace

from resumeforge.tailoring.summary_selector import SummarySelector


def test_returns_empty_list_when_profile_has_no_summary():
    selector = SummarySelector()

    result = selector.select(
        profile=None,
        match=None,
    )

    assert result == []

def test_returns_profile_summary_keywords():

    profile = SimpleNamespace(
        summary_keywords=[
            "Azure",
            "Microservices",
            "Leadership",
        ]
    )

    selector = SummarySelector()

    result = selector.select(
        profile,
        None,
    )

    assert result == [
        "Azure",
        "Microservices",
        "Leadership",
    ]

def test_returns_only_matching_summary_keywords():

    profile = SimpleNamespace(
        summary_keywords=[
            "Azure",
            "Leadership",
            "Python",
        ]
    )

    match = SimpleNamespace(
        matched=[
            "azure",
            "python",
        ]
    )

    selector = SummarySelector()

    result = selector.select(
        profile,
        match,
    )

    assert result == [
        "Azure",
        "Python",
    ]

def test_matching_is_case_insensitive():

    profile = SimpleNamespace(
        summary_keywords=[
            "Azure",
        ]
    )

    match = SimpleNamespace(
        matched=[
            "AZURE",
        ]
    )

    selector = SummarySelector()

    result = selector.select(
        profile,
        match,
    )

    assert result == [
        "Azure",
    ]

