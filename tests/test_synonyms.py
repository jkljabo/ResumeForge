from resumeforge.scoring.synonyms import SynonymTable


def test_expand_function_apps():
    table = SynonymTable()

    expanded = table.expand({"function app"})

    assert "azure functions" in expanded

def test_expand_dotnet():
    table = SynonymTable()

    expanded = table.expand({".net 8"})

    assert ".net" in expanded

def test_expand_unknown_keyword():
    table = SynonymTable()

    expanded = table.expand({"rabbitmq"})

    assert expanded == {"rabbitmq"}