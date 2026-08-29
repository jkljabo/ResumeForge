from resumeforge.concepts import TechnologyConcepts


def test_dotnet_alias_exists():
    concepts = TechnologyConcepts()

    assert ".net 8" in concepts.aliases["dotnet"]


def test_function_apps_alias_exists():
    concepts = TechnologyConcepts()

    assert "function apps" in concepts.aliases["azure_functions"]


def test_entity_framework_alias_exists():
    concepts = TechnologyConcepts()

    assert "ef core" in concepts.aliases["entity_framework"]


def test_git_alias_exists():
    concepts = TechnologyConcepts()

    assert "github" in concepts.aliases["git"]