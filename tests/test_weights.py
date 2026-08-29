from resumeforge.scoring.weights import WeightTable


def test_unknown_keyword_has_default_weight():
    weights = WeightTable()

    assert weights.get("azure") == 1


def test_can_add_weight():
    weights = WeightTable()

    weights.add("azure", 8)

    assert weights.get("azure") == 8


def test_lookup_is_case_insensitive():
    weights = WeightTable()

    weights.add("Azure", 8)

    assert weights.get("AZURE") == 8

def test_unknown_weight_defaults_to_one():
    table = WeightTable()

    assert table.get("unknown") == 1