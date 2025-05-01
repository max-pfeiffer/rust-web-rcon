from subprocess import run, CompletedProcess
from testcontainers.registry import DockerRegistryContainer

from tests.constants import (
    REGISTRY_USERNAME,
    REGISTRY_PASSWORD,
    VIRTUAL_ENVIRONMENT_PATH,
)
from pathlib import Path

from tests.utils import activate_virtual_environment


def test_build_image(registry_container: DockerRegistryContainer) -> None:
    repo_root_path = Path(__file__).parent.parent.resolve()
    env: dict = activate_virtual_environment(VIRTUAL_ENVIRONMENT_PATH)
    env["STATIC_SITE_CONTAINERIZER_REGISTRY"] = registry_container.get_registry()
    env["STATIC_SITE_CONTAINERIZER_REGISTRY_USERNAME"] = REGISTRY_USERNAME
    env["STATIC_SITE_CONTAINERIZER_REGISTRY_PASSWORD"] = REGISTRY_PASSWORD

    result: CompletedProcess = run(
        [
            "poetry",
            "run",
            "static-site-containerizer",
            "--content",
            "rust-web-rcon",
            "--tag",
            f"{registry_container.get_registry()}/rust-web-rcon:test",
            "--platform",
            "linux/amd64",
            "--platform",
            "linux/arm64",
            "--push",
        ],
        env=env,
        cwd=repo_root_path,
    )
    assert result.returncode == 0
