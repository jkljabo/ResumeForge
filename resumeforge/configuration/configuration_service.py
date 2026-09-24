from dataclasses import replace

from resumeforge.configuration.configuration import (
    ApplicationConfiguration,
)
from resumeforge.configuration.configuration_repository import (
    ConfigurationRepository,
)


class ConfigurationService:

    def __init__(
        self,
        repository: ConfigurationRepository,
    ) -> None:
        self._repository = repository

    def get_configuration(self) -> ApplicationConfiguration:
        return self._repository.load()

    def save_configuration(
        self,
        configuration: ApplicationConfiguration,
    ) -> None:
        self._repository.save(configuration)

    def reset_configuration(
        self,
    ) -> ApplicationConfiguration:
        configuration = ApplicationConfiguration.default()

        self._repository.save(configuration)

        return configuration

    def update_default_profile(
        self,
        default_profile: str,
    ) -> ApplicationConfiguration:
        return self.update_configuration(
            default_profile=default_profile,
        )

    def update_configuration(
        self,
        **changes,
    ) -> ApplicationConfiguration:
        configuration = self._repository.load()

        updated = replace(
            configuration,
            **changes,
        )

        self._repository.save(updated)

        return updated

