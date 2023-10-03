# see: https://github.com/devcontainers/images/blob/main/src/javascript-node/README.md
FROM mcr.microsoft.com/devcontainers/javascript-node:20

WORKDIR /workspaces/next-app

ENV NEXT_TELEMETRY_DISABLED 1

COPY package.json pnpm-lock.yaml* ./
COPY app ./app
COPY public ./public
COPY next.config.js tsconfig.json ./

RUN \
  chown -R node:node /workspaces/next-app/  && \
  yarn global add pnpm && pnpm i
