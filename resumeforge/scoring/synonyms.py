class SynonymTable:
    def __init__(self):
        self.synonyms = {
            ".net": {
                ".net",
                ".net framework",
                ".net core",
                ".net 6",
                ".net 7",
                ".net 8",
                ".net 9",
                ".net 10",
                "dotnet",
            },

            "azure functions": {
                "azure functions",
                "azure function",
                "azure function app",
                "azure function apps",
                "function app",
                "function apps",
            },

            "entity framework": {
                "entity framework",
                "entity framework core",
                "ef",
                "ef core",
            },

            "sql server": {
                "sql",
                "sql server",
                "mssql",
                "t-sql",
            },

            "blazor": {
                "blazor",
                "blazor server",
                "blazor wasm",
                "blazor webassembly",
            },

            "azure devops": {
                "azure devops",
                "devops",
                "ci/cd",
                "pipelines",
                "build pipelines",
                "release pipelines",
            },

            "git": {
                "git",
                "github",
                "azure repos",
            },
        }

    def expand(self, keywords):
        expanded = set(keywords)

        for group in self.synonyms.values():
            if expanded & group:
                expanded |= group

        return expanded