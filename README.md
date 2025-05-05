[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Pipeline](https://github.com/max-pfeiffer/rust-web-rcon/actions/workflows/pipeline.yaml/badge.svg)](https://github.com/max-pfeiffer/rust-web-rcon/actions/workflows/pipeline.yaml)
# Rust Web Rcon Client - Docker Image
Docker image providing the [websocket Rcon client from Facepunch](https://github.com/Facepunch/webrcon). This multi-architecture image supports 
linux/amd64 and linux/arm64 architectures.

## Usage
Run the Docker image like this:
```shell
docker run --rm -it --publish 80:80 pfeiffermax/rust-web-rcon:latest
```
Then point your browser to `http://localhost`.
