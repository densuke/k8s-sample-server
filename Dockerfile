FROM ghcr.io/astral-sh/uv AS uv

FROM python:slim AS base
COPY --from=uv /uv /uvx /usr/local/bin/

WORKDIR /app
COPY . .
EXPOSE 80
CMD ["uv", "run", "main.py"]

