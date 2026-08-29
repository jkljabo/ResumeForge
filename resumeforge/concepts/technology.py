class TechnologyConcepts:
    def __init__(self):
        self.aliases = {
            "dotnet": frozenset({
                ".net",
                ".net core",
                ".net framework",
                ".net 8",
                ".net 9",
                ".net 10",
            }),

            "azure_functions": frozenset({
                "azure function",
                "azure functions",
                "function app",
                "function apps",
            }),

            "entity_framework": frozenset({
                "entity framework",
                "ef",
                "ef core",
            }),

            "git": frozenset({
                "git",
                "github",
                "github enterprise",
            }),
        }

    def __contains__(self, concept):
        return concept.lower() in self.aliases

    def get(self, concept):
        return self.aliases.get(
            concept.lower(),
            frozenset(),
        )