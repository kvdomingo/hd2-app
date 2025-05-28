FROM python:3.12-bookworm

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONDONTWRITEBYTECODE=true
ENV PYTHONUNBUFFERED=1
ENV UV_VERSION=0.7.8
ENV PATH="/home/app/.local/bin:/home/app/.cargo/bin:${PATH}"

USER root

WORKDIR /tmp

SHELL [ "/bin/bash", "-euxo", "pipefail", "-c" ]
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl ca-certificates && \
    useradd --uid 1000 --shell /bin/bash --user-group --create-home app && \
    mkdir -p /app/.venv && \
    mkdir -p /home/app/.tmp && \
    chown -R 1000:1000 /app

ADD https://astral.sh/uv/${UV_VERSION}/install.sh /home/app/.tmp/install-uv.sh

SHELL [ "/bin/bash", "-euxo", "pipefail", "-c" ]
RUN chown -R 1000:1000 /home/app && \
    chmod +x /home/app/.tmp/install-uv.sh

WORKDIR /app

USER app

SHELL [ "/bin/sh", "-eu", "-c" ]
RUN /home/app/.tmp/install-uv.sh

ENTRYPOINT [ "/bin/bash", "-euxo", "pipefail", "-c" ]
