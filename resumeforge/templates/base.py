from abc import ABC, abstractmethod


class BaseTemplate(ABC):

    @abstractmethod
    def apply(self, document):
        """Apply styling to the document."""
