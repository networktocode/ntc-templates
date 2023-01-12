# Building Your Development Environment

## Quickstart

The development environment can be used in two ways:

1. `Recommended` All services are spun up using Docker and a local mount so you can develop locally, but NTC Templates is spun up within the Docker container.
2. With a local poetry environment if you wish to develop outside of Docker.

This is a quick reference guide if you're already familiar with the development environment provided, which you can read more about later in this document.

### Invoke

The [Invoke](http://www.pyinvoke.org/) library is used to provide some helper commands based on the environment. There are a few configuration parameters which can be passed to Invoke to override the default configuration:

- `local`: a boolean flag indicating if invoke tasks should be run on the host or inside the docker containers (default: False, commands will be run in docker containers)

Using **Invoke** these configuration options can be overridden using [several methods](https://docs.pyinvoke.org/en/stable/concepts/configuration.html). Perhaps the simplest is setting an environment variable `INVOKE_NETUTILS_VARIABLE_NAME` where `VARIABLE_NAME` is the variable you are trying to override. There is an example `invoke.yml` (`invoke.example.yml`) in this directory which can be used as a starting point.

### Docker Development Environment

!!! tip
    This is the recommended option for development.

This project is managed by [Python Poetry](https://python-poetry.org/) and has a few requirements to setup your development environment:

1. Install Poetry, see the [Poetry Documentation](https://python-poetry.org/docs/#installation) for your operating system.
2. Install Docker, see the [Docker documentation](https://docs.docker.com/get-docker/) for your operating system.

Once you have Poetry and Docker installed you can run the following commands (in the root of the repository) to install all other development dependencies in an isolated Python virtual environment:

```shell
poetry shell
poetry install
cp development/creds.example.env development/creds.env
invoke build
invoke start
```

Live documentation can be viewed at [http://localhost:8001](http://localhost:8001).

To either stop or destroy the development environment use the following options.

- **invoke stop** - Stop the containers, but keep all underlying systems intact
- **invoke destroy** - Stop and remove all containers, volumes, etc. (This results in data loss due to the volume being deleted)

## Poetry

Poetry is used in lieu of the "virtualenv" commands and is leveraged in both environments. The virtual environment will provide all of the Python packages required to manage the development environment such as **Invoke**. See the [Local Development Environment](#local-poetry-development-environment) section to see how to install NTC Templates if you're going to be developing locally (i.e. not using the Docker container).

The `pyproject.toml` file outlines all of the relevant dependencies for the project:

- `tool.poetry.dependencies` - the main list of dependencies.
- `tool.poetry.dev-dependencies` - development dependencies, to facilitate linting, testing, and documentation building.

The `poetry shell` command is used to create and enable a virtual environment managed by Poetry, so all commands ran going forward are executed within the virtual environment. This is similar to running the `source venv/bin/activate` command with virtualenvs. To install project dependencies in the virtual environment, you should run `poetry install` - this will install **both** project and development dependencies.

For more details about Poetry and its commands please check out its [online documentation](https://python-poetry.org/docs/).

## Full Docker Development Environment

This project is set up with a number of **Invoke** tasks consumed as simple CLI commands to get developing fast. You'll use a few `invoke` commands to get your environment up and running.

## CLI Helper Commands

The project features a CLI helper based on [invoke](http://www.pyinvoke.org/) to help setup the development environment. The commands are listed below in 3 categories:
- `dev environment`
- `utility`
- `testing`

Each command can be executed with `invoke <command>`. Each command also has its own help `invoke <command> --help`

### Local dev environment

```
  build              Build all docker images.
  clean              Remove the project specific image.
  docs               Build and serve docs locally.
  rebuild            Clean the Docker image and then rebuild without using cache.
```

### Utility

```
  clean-yaml-file    Transform a yaml file to expected output.
  clean-yaml-folder  Transform a yaml file to expected output to a folder.
  cli                Enter the image to perform troubleshooting or dev work.
  gen-yaml-file      Generate a yaml file from raw a data file.
  gen-yaml-folder    Generate a yaml file from folder of raw data files.
```

### Testing

```
  bandit             Run bandit to validate basic static code security analysis.
  black              Run black to check that Python files adhere to its style standards.
  coverage           Run the coverage report against pytest.
  flake8             Run flake8 to check that Python files adhere to its style standards.
  mypy               Run mypy to validate typing-hints.
  pylint             Run pylint code analysis.
  pydocstyle         Run pydocstyle to validate docstring formatting adheres to NTC defined standards.
  pytest             Run pytest for the specified name and Python version.
  tests              Run all tests for the specified name and Python version.
  yamllint           Run yamllint to validate formatting adheres to NTC defined YAML standards.
```