ARG PYTHON_VER

FROM python:${PYTHON_VER}-slim

# Install all OS package upgrades and dependencies needed to run Nautobot in production
# hadolint ignore=DL3005,DL3008,DL3013
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install --no-install-recommends -y git mime-support curl libxml2 libmariadb3 openssl gcc musl-dev python3-dev && \
    apt-get autoremove -y && \
    apt-get clean all && \
    rm -rf /var/lib/apt/lists/* && \
    pip --no-cache-dir install --upgrade pip wheel

RUN pip install --upgrade pip

# Install Poetry manually via its installer script;
# We might be using an older version of ntc-templates that includes an older version of Poetry
# and CI and local development may have a newer version of Poetry
# Since this is only used for development and we don't ship this container, pinning Poetry back is not expressly necessary
# We also don't need virtual environments in container
RUN which poetry || curl -sSL https://install.python-poetry.org | python3 - 

# Add poetry install location to the $PATH
ENV PATH="${PATH}:/root/.local/bin"

WORKDIR /local
COPY pyproject.toml poetry.lock README.md /local/

RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi --no-root

# Do not break dependency caching before installing project
COPY . .
RUN poetry install
