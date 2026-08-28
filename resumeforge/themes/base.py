from abc import ABC, abstractmethod


class BaseTheme(ABC):
    @abstractmethod
    def apply(self, document):
        """Apply theme styling to a document."""
        pass