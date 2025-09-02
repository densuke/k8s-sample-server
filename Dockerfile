ARG TARGETPLATFORM
FROM --platform=$TARGETPLATFORM ghcr.io/astral-sh/uv AS uv

FROM --platform=$TARGETPLATFORM python:slim AS base
COPY --from=uv /uv /uvx /usr/local/bin/

WORKDIR /app
COPY . .
EXPOSE 80
CMD ["uv", "run", "main.py"]
ARG TARGETPLATFORM
FROM --platform=$TARGETPLATFORM ghcr.io/astral-sh/uv AS uv

FROM --platform=$TARGETPLATFORM python:slim AS base
COPY --from=uv /uv /uvx /usr/local/bin/

WORKDIR /app
COPY . .
EXPOSE 80
CMD ["uv", "run", "main.py"]
ARG TARGETPLATFORM
FROM --platform=$TARGETPLATFORM ghcr.io/astral-sh/uv AS uv

FROM --platform=$TARGETPLATFORM python:slim AS base
COPY --from=uv /uv /uvx /usr/local/bin/

WORKDIR /app
COPY . .
EXPOSE 80
CMD ["uv", "run", "main.py"]

