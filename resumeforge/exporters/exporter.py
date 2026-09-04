from abc import ABC
from abc import abstractmethod


class ResumeExporter(ABC):

    @abstractmethod
    def export(
        self,
        document,
    ) -> str:
        """
        Export a rendered resume to the specified destination.
        """
        raise NotImplementedError