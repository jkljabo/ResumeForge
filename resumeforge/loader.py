import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def load_resume(profile="resume"):

    file = BASE_DIR / "data" / f"{profile}.json"

    with open(file, encoding="utf-8") as f:
        return json.load(f)