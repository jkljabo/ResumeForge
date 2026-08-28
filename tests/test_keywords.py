from resumeforge.keywords import KeywordExtractor


def test_extract_returns_words():
    extractor = KeywordExtractor()

    words = extractor.extract(
        "Azure Functions with .NET 8"
    )

    assert "azure" in words
    assert "functions" in words
    assert ".net" in words

def test_extract_is_case_insensitive():
    extractor = KeywordExtractor()

    words = extractor.extract(
        "AZURE Azure azure"
    )

    assert words == {"azure"}

def test_extract_removes_duplicates():
    extractor = KeywordExtractor()

    words = extractor.extract(
        "Blazor Blazor Blazor"
    )

    assert len(words) == 1