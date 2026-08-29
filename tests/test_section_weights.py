from resumeforge.scoring import SectionWeights


def test_default_section_weights():
    weights = SectionWeights()

    assert weights.get("experience") == 5
    assert weights.get("projects") == 3
    assert weights.get("skills") == 2
    assert weights.get("certifications") == 1


def test_unknown_section_weight():
    weights = SectionWeights()

    assert weights.get("foobar") == 1