from abc import ABC, abstractmethod


class BaseRenderer(ABC):
    """Abstract base class for all resume renderers."""

    @abstractmethod
    def render(self, document, resume):
        """Render a section of the resume."""
        raise NotImplementedError