# NTC Templates

<p align="center">
  <img src="https://raw.githubusercontent.com/networktocode/ntc-templates/master/docs/images/icon-ntc-templates.png" class="logo" height="200px">
  <br>
  <a href="https://github.com/networktocode/ntc-templates/actions"><img src="https://github.com/networktocode/ntc-templates/actions/workflows/ci.yml/badge.svg?branch=main"></a>
  <a href="https://ntc-templates.readthedocs.io/en/latest"><img src="https://readthedocs.org/projects/ntc-templates/badge/"></a>
  <a href="https://pypi.org/project/ntc-templates/"><img src="https://img.shields.io/pypi/v/ntc-templates"></a>
  <a href="https://pypi.org/project/ntc-templates/"><img src="https://img.shields.io/pypi/dm/ntc-templates"></a>
  <br>
</p>

## Overview

Repository of TextFSM Templates for Network Devices, and Python wrapper for TextFSM's CliTable. TextFSM is a tool to help make parsing cli commands more manageable.

## Documentation

Full web-based HTML documentation for this library can be found over on the [NTC Templates Docs](https://ntc-templates.readthedocs.io) website:

- [User Guide](https://ntc-templates.readthedocs.io/en/latest/user/lib_overview/) - Overview, Using the library, Getting Started.
- [Administrator Guide](https://ntc-templates.readthedocs.io/en/latest/admin/install/) - How to Install, Configure, Upgrade, or Uninstall the library.
- [Developer Guide](https://ntc-templates.readthedocs.io/en/latest/dev/contributing/) - Extending the library, Code Reference, Contribution Guide.
- [Release Notes / Changelog](https://ntc-templates.readthedocs.io/en/latest/admin/release_notes/).
- [Frequently Asked Questions](https://ntc-templates.readthedocs.io/en/latest/user/faq/).

### Contributing to the Docs

All the Markdown source for the library documentation can be found under the [docs](https://github.com/networktocode/ntc-templates/tree/develop/docs) folder in this repository. For simple edits, a Markdown capable editor is sufficient - clone the repository and edit away.

If you need to view the fully generated documentation site, you can build it with [mkdocs](https://www.mkdocs.org/). A container hosting the docs will be started using the invoke commands (details in the [Development Environment Guide](https://ntc-templates.readthedocs.io/en/latest/dev/dev_environment/#docker-development-environment)) on [http://localhost:8001](http://localhost:8001). As your changes are saved, the live docs will be automatically reloaded.

Any PRs with fixes or improvements are very welcome!

## Questions

For any questions or comments, please check the [FAQ](https://ntc-templates.readthedocs.io/en/latest/user/faq/) first. Feel free to also swing by the [Network to Code Slack](https://networktocode.slack.com/) (channel `#networktocode`), sign up [here](http://slack.networktocode.com/) if you don't have an account.
