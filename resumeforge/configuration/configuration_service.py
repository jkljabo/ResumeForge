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
        **updates,
    ) -> ApplicationConfiguration:
        configuration = self.get_configuration()

        self._validate_updates(updates)

        updated = replace(
            configuration,
            **updates,
        )

        self._repository.save(updated)

        return updated

    def _validate_updates(
        self,
        updates: dict[str, object],
    ) -> None:
        if "default_theme" in updates:
            valid_themes = {
                "executive",
                "modern",
            }

            if updates["default_theme"] not in valid_themes:
                raise ValueError(
                    f"Invalid theme: {updates['default_theme']}"
                )

        if "page_size" in updates:
            valid_page_sizes = {
                "LETTER",
                "LEGAL",
                "A4",
            }

            if updates["page_size"] not in valid_page_sizes:
                raise ValueError(
                    f"Invalid page size: {updates['page_size']}"
                )

        if "default_profile" in updates:
            profile = str(updates["default_profile"]).strip()

            if not profile:
                raise ValueError(
                    "Default profile cannot be empty."
                )