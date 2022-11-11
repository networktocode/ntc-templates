# Installation

> As of v2.0.0, this project uses [Poetry](https://python-poetry.org/) for packaging and distribution. In order to use poetry, the `templates` directory has been moved to `ntc_templates/templates`

Option 1: Install from PyPI.

```bash
$ pip install ntc-templates
```

Option 2: Install from a GitHub branch, such as develop as shown below.

```bash
$ pip install git+https://github.com/networktocode/ntc-templates.git@develop
```

# Define Custom Templates Directory

To use a custom templates directory set the environmental variable `NTC_TEMPLATES_DIR`.

**Requirements**

1. `index` file needs to be defined with standard structure.
2. Each custom template should be defined.

To manaully set variable:
```shell
export NTC_TEMPLATES_DIR=/path/to/new/location/templates
```

To set within your program:
```python
import os
os.environ["NTC_TEMPLATES_DIR"] = "/path/to/new/templates/location/templates"
```
