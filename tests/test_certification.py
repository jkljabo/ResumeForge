from resumeforge.domain import Certification


def test_certification_model():
    cert = Certification(
        name="Microsoft Certified: Azure Fundamentals",
        issuer="Microsoft",
        year="2024",
    )

    assert cert.name.startswith("Microsoft Certified")
    assert cert.issuer == "Microsoft"