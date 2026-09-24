from pathlib import Path
from typing import Protocol

from .configuration import ApplicationConfiguration


class ConfigurationRepository(Protocol):

    def load(
        self,
    ) -> ApplicationConfiguration:
        ...

    def save(
        self,
        configuration: ApplicationConfiguration,
    ) -> None:
        ...

class ConfigurationRepositoryError(Exception):
    """Raised when configuration persistence fails."""