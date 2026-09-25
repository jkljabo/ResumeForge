from pathlib import Path

from resumeforge.factory import create_resume_generator
from resumeforge.configuration.configuration_service import (
    ConfigurationService,
)
from resumeforge.configuration.json_configuration_repository import (
    JsonConfigurationRepository,
)


def create_generator():
    """Construct the ResumeForge generation pipeline."""
    return create_resume_generator()


def _create_configuration_path() -> Path:
    return Path.cwd() / "configuration.json"


def create_configuration_service() -> ConfigurationService:
    repository = JsonConfigurationRepository(
        _create_configuration_path()
    )

    return ConfigurationService(repository)


