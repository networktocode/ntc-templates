ARG PYTHON_VER
FROM python:${PYTHON_VER}-slim

# hadolint ignore=DL3008
RUN set -eux; \
  export DEBIAN_FRONTEND=noninteractive; \
  apt-get update; \
  apt-get install --no-install-recommends -y \
  git \
  curl \
  libxml2 \
  libmariadb3 \
  openssl \
  build-essential \
  pkg-config \
  media-types \
  mailcap \
  ; \
  rm -rf /var/lib/apt/lists/*

# Upgrade pip & wheel once
RUN pip --no-cache-dir install --upgrade pip wheel

# Install Poetry (no venvs in container)
RUN which poetry || curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="${PATH}:/root/.local/bin"

WORKDIR /local
COPY pyproject.toml poetry.lock README.md /local/

RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi --no-root

# Copy project last to preserve layer caching
COPY . .
RUN poetry install
