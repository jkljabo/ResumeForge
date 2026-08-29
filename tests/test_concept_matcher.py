from resumeforge.concepts import ConceptMatcher


def test_exact_match():
    matcher = ConceptMatcher()

    assert matcher.matches(
        "azure functions",
        "azure functions",
    )