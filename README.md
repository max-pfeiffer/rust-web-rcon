[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Pipeline](https://github.com/max-pfeiffer/rust-web-rcon/actions/workflows/pipeline.yaml/badge.svg)](https://github.com/max-pfeiffer/rust-web-rcon/actions/workflows/pipeline.yaml)
[![Release Helm Charts](https://github.com/max-pfeiffer/rust-web-rcon/actions/workflows/helm-release.yaml/badge.svg)](https://github.com/max-pfeiffer/rust-web-rcon/actions/workflows/helm-release.yaml)
![Docker Image Size (latest semver)](https://img.shields.io/docker/image-size/pfeiffermax/rust-web-rcon?sort=semver)
![Docker Pulls](https://img.shields.io/docker/pulls/pfeiffermax/rust-web-rcon)

# Rust Web Rcon Client - Docker Image and Helm Chart
Docker image providing the [websocket Rcon client from Facepunch](https://github.com/Facepunch/webrcon). This multi-architecture image supports 
linux/amd64 and linux/arm64 architectures.

## Docker Image Usage
Run the Docker image like this:
```shell
docker run --rm -it --publish 80:80 pfeiffermax/rust-web-rcon:latest
```
Then point your browser to `http://localhost`.

## Helm Chart
The installation is done as follows:
```shell
$ helm repo add rust-web-rcon https://max-pfeiffer.github.io/rust-web-rcon
$ helm install rust-web-rcon rust-web-rcon/rust-web-rcon --values your_values.yaml --namespace yournamespace 
```
