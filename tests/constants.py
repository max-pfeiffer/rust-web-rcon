"""Constants used by tests."""

from pathlib import Path

PROJECT_ROOT_PATH: Path = Path(__file__).parent.parent.resolve()
VIRTUAL_ENVIRONMENT_PATH: Path = PROJECT_ROOT_PATH / ".venv"

REGISTRY_USERNAME: str = "foo"
REGISTRY_PASSWORD: str = "bar"
