# Contributing

Pull requests are welcomed and automatically built and tested against multiple versions of Python through GitHub Actions. 

Except for unit tests, testing is only supported on Python 3.9.

The project is packaged with a light development environment based on `Docker` to help with the local development of the project and to run tests within  GitHub Actions.

The project is following Network to Code software development guidelines and are leveraging the following:

- Black, Pylint, Bandit, Mypy, flake8, and pydocstyle for Python linting and formatting.
- pytest, coverage, and unittest for unit tests.

There are a number of things that are required in order to have a successful PR.

- Docstrings must conform to the google docstring [convention](https://google.github.io/styleguide/pyguide.html#381-docstrings).
- Following and adherence to [Extending Parsers](dev_parser.md).
- Run tests with `invoke tests`.

Documentation is built using [mkdocs](https://www.mkdocs.org/). The [Docker based development environment](dev_environment.md#docker-development-environment) can be started by running `invoke docs` [http://localhost:8001](http://localhost:8001) that auto-refreshes when you make any changes to your local files.


## Branching Policy

The branching policy includes the following tenets:

- The develop branch is the primary branch to develop off of.
- If there is a reason to have a patch version, the maintainers may use cherry-picking strategy.
- PRs intended to add new features should be sourced from the develop branch.
- PRs intended to address bug fixes and security patches should be sourced from the develop branch.
- PRs intended to add new features that break backward compatibility should be discussed before a PR is created.

NTC-Templates will observes semantic versioning. This may result in an quick turn around in minor versions to keep pace with an ever growing feature set.

## Release Policy

NTC Templates has currently no intended scheduled release schedule, and will release new features in minor versions.

When a new release is created the following should happen.

- A release PR is created with:
    - Update to the changelog in `docs/admin/release_notes/version_<major>.<minor>.md` file to reflect the changes.
    - Change the version from `<major>.<minor>.<patch>-beta` to `<major>.<minor>.<patch>` in pyproject.toml.
    - Set the PR to the master
- Ensure the tests for the PR pass.
- Merge the PR.
- Create a new tag:
    - The tag should be in the form of `v<major>.<minor>.<patch>`.
    - The title should be in the form of `v<major>.<minor>.<patch>`.
    - The description should be the changes that were added to the `version_<major>.<minor>.md` document.
- If merged into `master`, then push from `master` to `develop`, in order to retain the merge commit created when the PR was merged
- A post release PR is created with.
    - Change the version from `<major>.<minor>.<patch>` to `<major>.<minor>.<patch + 1>-beta` pyproject.toml.
    - Set the PR to the `develop`.
    - Once tests pass, merge.