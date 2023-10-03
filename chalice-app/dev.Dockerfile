
# see: https://github.com/devcontainers/images/blob/main/src/python/README.md
FROM mcr.microsoft.com/devcontainers/python:3.10-bullseye

WORKDIR /workspaces/chalice-app

COPY requirements.txt ./

RUN pip install -r requirements.txt
