import json
from pathlib import Path

from resumeforge.configuration.configuration_repository import ConfigurationRepositoryError

from .configuration import ApplicationConfiguration


class JsonConfigurationRepository:

    def __init__(
        self,
        configuration_path: Path,
    ):
        self._configuration_path = configuration_path

    def load(self) -> ApplicationConfiguration:

        if not self._configuration_path.exists():
            return ApplicationConfiguration.default()

        try:
            with self._configuration_path.open(
                "r",
                encoding="utf-8",
            ) as file:
                data = json.load(file)

            return ApplicationConfiguration.from_dict(data)

        except (
            json.JSONDecodeError,
            KeyError,
            TypeError,
            ValueError,
        ) as exc:
            raise ConfigurationRepositoryError(
                "Configuration file is invalid."
            ) from exc

    def save(
        self,
        configuration: ApplicationConfiguration,
    ) -> None:

        self._configuration_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with self._configuration_path.open(
            "w",
            encoding="utf-8",
        ) as file:
            json.dump(
                configuration.to_dict(),
                file,
                indent=4,
            )