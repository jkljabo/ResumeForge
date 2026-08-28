import re


class KeywordExtractor:
    def extract(self, text: str) -> set[str]:
        words = re.findall(r"[A-Za-z0-9.+#-]+", text.lower())

        return set(words)