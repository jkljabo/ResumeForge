from abc import ABC, abstractmethod


class BaseLayout(ABC):

    @abstractmethod
    def heading(self, text, level=1):
        pass

    @abstractmethod
    def paragraph(self, text="", style=None):
        pass