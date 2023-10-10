###############################
# Dev Base
###############################
# see: https://github.com/devcontainers/images/blob/main/src/python/README.md
FROM mcr.microsoft.com/devcontainers/python:3.10-bullseye as dev-base

ENV PYTHONUNBUFFERED=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=0 \
    POETRY_VIRTUALENVS_CREATE=0 \
    POETRY_CACHE_DIR=/tmp/poetry_cache \
    WORKDIR_PATH=/workspaces/chalice-app

###############################
# Dev Poetry init
###############################
FROM dev-base as dev-init

RUN pip install poetry==1.6.1

WORKDIR $WORKDIR_PATH

###############################
# Dev Main
###############################
FROM dev-init as dev-main

WORKDIR $WORKDIR_PATH

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root
