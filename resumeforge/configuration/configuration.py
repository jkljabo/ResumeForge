from dataclasses import asdict
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class ApplicationConfiguration:
    default_profile: str
    default_theme: str
    output_directory: Path
    default_output_filename: str
    page_size: str
    font_name: str

    @classmethod
    def default(cls) -> "ApplicationConfiguration":
        return cls(
            default_profile="resume",
            default_theme="executive",
            output_directory=Path("output"),
            default_output_filename="Executive_Master_Resume.docx",
            page_size="LETTER",
            font_name="Calibri",
        )

    def to_dict(self) -> dict[str, str]:
        data = asdict(self)
        data["output_directory"] = str(self.output_directory)
        return data

    @classmethod
    def from_dict(
        cls,
        data: dict[str, str],
    ) -> "ApplicationConfiguration":
        return cls(
            default_profile=data["default_profile"],
            default_theme=data["default_theme"],
            output_directory=Path(data["output_directory"]),
            default_output_filename=data["default_output_filename"],
            page_size=data["page_size"],
            font_name=data["font_name"],
        )