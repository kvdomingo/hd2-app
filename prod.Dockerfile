FROM python:3.12-slim AS base

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV UV_VERSION=0.7.19
ENV PATH="/root/.local/bin:/root/.cargo/bin:${PATH}"

WORKDIR /app

FROM base AS build

SHELL [ "/bin/sh", "-eu", "-c" ]

SHELL [ "/bin/bash", "-euxo", "pipefail", "-c" ]
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl ca-certificates && \
    useradd --uid 1000 --shell /bin/bash --user-group --create-home app

ADD https://astral.sh/uv/${UV_VERSION}/install.sh /tmp/install-uv.sh

COPY ./api/pyproject.toml ./api/uv.lock ./

SHELL [ "/bin/sh", "-eu", "-c" ]
# hadolint ignore=DL4006
RUN chmod +x /tmp/install-uv.sh &&  \
    /tmp/install-uv.sh && \
    uv venv .venv && \
    uv export --format requirements.txt --no-hashes --no-annotate --no-header --no-dev | \
    uv pip install --no-cache-dir -r /dev/stdin

FROM base AS prod

WORKDIR /app

COPY ./api ./
COPY --from=build /app/.venv ./.venv/

SHELL [ "/bin/sh", "-eu", "-c" ]
RUN chown -R 1000:1000 /app

USER app

CMD [ "/app/.venv/bin/fastapi", "run", "--host", "0.0.0.0", "--port", "8000", "--proxy-headers", "api/app.py" ]
