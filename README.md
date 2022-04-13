[![Build Status](https://travis-ci.org/networktocode/ntc-templates.svg?branch=master)](https://travis-ci.org/networktocode/ntc-templates)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

NTC TEMPLATES
=============

Repository of TextFSM Templates for Network Devices, and Python wrapper for TextFSM's CliTable.

[TextFSM](https://github.com/google/textfsm/wiki) is a project built by Google that takes CLI string output and passes each line through a series of regular expressions until it finds a match. The regular expressions use named capture groups to build a text table out of the significant text. The names of the capture groups are used as column headers, and the captured values are stored as rows in the table.

This project provides a large collection of TextFSM Templates (text parsers) for a variety of Networking Vendors. In addition to the templates, there is a function that will convert the CLI output into a CliTable object; the resulting text table is converted into a list of dictionaries mapping the column headers with each row in the table.


> As of v2.0.0, this project uses [Poetry](https://python-poetry.org/) for packaging and distribution. In order to use poetry, the `templates` directory has been moved to `ntc_templates/templates`

Installation and Usage
----------------------
The project can be installed using either Git + Poetry or PyPI.

#### Git

```shell
$ git clone git@github.com:networktocode/ntc-templates.git
$ 
# Optional steps to install ntc-templates as a python package
$ poetry install
$ 
```

#### PyPI

```shell
$ pip install ntc_templates
$ 
```

#### Usage

```python
>>> from ntc_templates.parse import parse_output
>>> vlan_output = (
        "VLAN Name                             Status    Ports\n"
        "---- -------------------------------- --------- -------------------------------\n"
        "1    default                          active    Gi0/1\n"
        "10   Management                       active    \n"
        "50   VLan50                           active    Fa0/1, Fa0/2, Fa0/3, Fa0/4, Fa0/5,\n"
        "                                                Fa0/6, Fa0/7, Fa0/8\n"
    )
>>> vlan_parsed = parse_output(platform="cisco_ios", command="show vlan", data=vlan_output)
>>> vlan_parsed
[
    {
        'vlan_id': '1',
        'name': 'default',
        'status': 'active',
        'interfaces': ['Gi0/1']
    },
    {
        'vlan_id': '10',
        'name': 'Management',
        'status': 'active',
        'interfaces': []
    },
    {
        'vlan_id': '50',
        'name': 'VLan50', 'status': 'active',
        'interfaces': ['Fa0/1', 'Fa0/2', 'Fa0/3', 'Fa0/4', 'Fa0/5', 'Fa0/6', 'Fa0/7', 'Fa0/8']
    }
]
>>> 
```

### Define Custom Templates Directory

To use a custom templates directory set the environmental variable `NTC_TEMPLATES_DIR`.

**Requirements**
1. `index` file needs to be defined with standard structure. [See](#Index-File)
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

Contributing
------------

Pull requests are welcomed and automatically built and tested through TravisCI.

### New Templates
To contribute new templates, each new pull request must include the following:

- TextFSM template
- Modified version of the **index** file
- Tests
  * Raw version of text to be parsed
  * YAML file containing the expected parsed dictionary

#### TextFSM Template

TextFSM templates should be placed in the `./templates` directory and should adhere to the following NTC-Templates style.
The TextFSM template name should be in the following format:

##### Naming

The template should be named using: `{{ vendor_os }}_{{ command_with_underscores }}.textfsm`
> Ex: cisco_ios_show_cdp_neighbors.textfsm

Note: The vendor name must be valid from the [os_choices](https://github.com/networktocode/ntc-templates/blob/master/tests/test_index_order.py#L59) tests, which is primarily based on [Netmiko](https://github.com/ktbyers/netmiko/tree/master/netmiko) list of supported vendors. New vendors added should adhere to **vendor_os**.
> Ex: vmware_nsx

##### Values

The capture group names should be in UPPERCASE.

An example of the proper format is shown below.

```
Value TIME (\d+:\d+:\d+)
Value TIMEZONE (\S+)
Value DAYWEEK (\w+)
Value MONTH (\d+)
Value DAY (\d+)
Value YEAR (\d+)

Start
  ^${TIME}\s+${TIMEZONE}\s+${DAYWEEK}\s+${DAY}/${MONTH}/${YEAR} -> Record
  ^. -> Error
```
##### States

If the raw output has a heading, the `Start` state should match on the column headings and then transition to another state that will match the device's output table with the capture groups. This helps ensure the regex patterns for the capture groups are attempting to match the correct information, and allows templates to easily add additional States for tables that have different headings. 
Example:

*Raw Output*
```
... omitted
Network Next Hop Metric LocPrf Weight Path
*> 111.111.111.111/32 112.112.112.112 4294967295 4294967295 65535 1000 1000 1000 i
```

*Sample Template*
```
Start
# Checking for header
^\s*Network\s+Next(?:\s+|-)[Hh]op\s+Metric\s+LocPrf\s+Weight\s+Path\s*$$ -> BGPTable

BGPTable
 ... omitted
```

Each **state** should end with `^. -> Error`. This helps to ensure we're accounting for every line within the raw output for the command. This doesn't mean we have to capture all the data as a **Value**, but we do have to account for it. In addition, it is also good to provide an expression to match blank lines, `^\s*$$`

An example would be the following raw output:
```
NAME: "3640 chassis", DESCR: "3640 chassis"
PID: , VID: 0xFF, SN: FF1045C5
```

The template would be the following:
```
Value NAME (.*)
Value DESCRIPTION (.*)

Start
  ^NAME:\s+"${NAME}",\s*DESCR:\s+"${DESCRIPTION}"
  ^PID:\s*,\s*VID:\s*\S+,\s*SN:\s*\S+
  ^\s*$$
  ^. -> Error
```

Taking a look at the example template above, you notice that we're using **\s*** and **\s+**. These are the preferred way to match space characters, and should be used over the literal space character. For example, `This\s+is\s+preferred\s*$$` vs `This is not preferred$$`

- **\s*** accounts for zero or more spaces (use when the output may or may not have a space between characters)
- **\s+** accounts for one or more spaces (use when output will have a space, but could have more than one space)

#### Index File

The Index file binds the templates to the commands being run. Special care has been taken on ordering, as there is potential for issues. e.g. `show ip route` picking up for `show ip router vrf <vrf-name>`. We have used a combination of ordering, as defined:

 - OS in alphabetical order
 - Template name in length order (longest to shortest)
 - When length is the same, use alphabetical order of command name
 - Keep space between OS's

Example:

```
Template, Hostname, Platform, Command

# same os, same length, used alphabetical order of command name
arista_eos_show_mlag.textfsm, .*, arista_eos, sh[[ow]] ml[[ag]]
arista_eos_show_vlan.textfsm, .*, arista_eos, sh[[ow]] vl[[an]]

# os in alphabetical order and space between cisco_asa and arista_eos
cisco_asa_dir.textfsm,  .*, cisco_asa, dir

# same os, template name length different and space between cisco_asa and cisco_ios
cisco_ios_show_capability_feature_routing.textfsm,  .*, cisco_ios, sh[[ow]] cap[[ability]] f[[eature]] r[[outing]]
cisco_ios_show_interface_transceiver.textfsm, .*, cisco_ios, sh[[ow]] int[[erface]] trans[[ceiver]]
cisco_ios_show_cdp_neighbors_detail.textfsm, .*, cisco_ios, sh[[ow]] c[[dp]] neig[[hbors]] det[[ail]]
```

#### Tests
Tests will be located in `./tests` with the following hierarchy:
- `./tests/{{ vendor_os }}/{{ command_name }}/`

The `{{ command_name }}` directory should include the `.raw` file that includes the raw output of the command to be parsed, and the `.yml` file of the returned structured data.
```bash
$ ls tests/cisco_ios/show_clock/
cisco_ios_show_clock.yml
cisco_ios_show_clock.raw
$ 
```

##### Raw version of input text

The raw text file should contain **only** the output of the CLI command to be parsed. It should **not** contain the CLI command itself.

An example of the proper format is shown below:

```bash
$ cat tests/cisco_ios/show_clock/cisco_ios_show_clock.raw
*18:57:38.347 UTC Mon Oct 19 2015
$ 
```

##### YAML file containing expected parsed dictionary

The parsed file should match the data that is returned from the `parse_output` function discussed in the beginning. Dictionary keys should be in lowercase.

The parsed text file should be placed in a directory in the `./tests` directory with the same name as the template file but replace `.textfsm` file extension with `.yml`. The raw text file and the parsed text file should be in the same directory.
**ex. ./tests/cisco_ios/show_clock/**

There are available helpers to create the parsed file in the correct format (See _Development Helper Scripts_ below).

An example of the proper format is shown below:
```bash
$ cat ./tests/cisco_ios/show_clock/cisco_ios_show_clock.yml
---
parsed_sample:
  - time: "18:57:38.347"
    timezone: "UTC"
    dayweek: "Mon"
    month: "Oct"
    day: "19"
    year: "2015"
$ 
```

Multiple `raw` and `parsed` files are supported per directory, and are encouraged, as there are differences depending on version, length, etc. Additional test files and more real life data helps ensure backwards compatibility is maintained as each template is updated and merged into the repo.

All YAML files must adhere to the YAML standards defined in the `.yamllint` file in the root directory. Yamllint provides thorough documentation of their configuration settings [here](https://yamllint.readthedocs.io/en/stable/rules.html). 

##### Development Helper Scripts

A cli utility is provided to assist with properly building the parsed files. This utility depends on some packages listed in the dev install requirements; see _Install and Usage_ for directions on installing the dev requirements. All arguments that can be passed to the script are mutually exclusive (i.e. you can only pass one argument). The file can be made executable with the `chmod +x development_scripts.py` command. The arguments are:

  * `-y`: Takes the path to a YAML file and ensures that the file adheres to the .yamllint settings
  * `-yd`: Takes a glob path to a directory or directories that will ensure all files ending in `.yml` adhere to the .yamllint settings
  * `-c`: Takes the path to a `.raw` file, and generates the parsed data and saves the results adjacent to the `.raw` file following the defined standards in .yamllint.
  * `-cd`: Takes a glob path to a directory or directories containing `.raw` files, and creates the appropriate parsed files in the appropriate directory.

  The `-y` and `-yd` arguments are designed to allow developers to generate the expected parsed file how they want, and ensure that the formatting adheres to the defined standard for this project.

  The `-c` and `-cd` arguments use `ntc_templates.parse.parse_output()` to generate the parsed data; this means that you can use these arguments to auto-generate the test `.yml` file(s) for new templates; just be sure that the template's parsing behavior meets expectations. In order for the data to be parsed, the template must be placed in `ntc_templates/templates/` and the `ntc_templates/templates/index` file must be updated to correctly point to the template file(s).

```bash
$ ./development_scripts.py -yd tests/cisco_ios/show_mac-address-table
tests/cisco_ios/show_mac-address-table/cisco_ios_show_mac-address-table2.yml
tests/cisco_ios/show_mac-address-table/cisco_ios_show_mac-address-table3.yml
tests/cisco_ios/show_mac-address-table/cisco_ios_show_mac-address-table5.yml
tests/cisco_ios/show_mac-address-table/cisco_ios_show_mac-address-table4.yml
tests/cisco_ios/show_mac-address-table/cisco_ios_show_mac-address-table.yml
$
$ ls tests/arista_eos/show_version/
arista_eos_show_version.raw
$
$ ./development_scripts.py -c tests/arista_eos/show_version/arista_eos_show_version.txt
$ ls tests/arista_eos/show_version/
arista_eos_show_version.raw   arista_eos_show_version.yml
$
```

### Updating/Fixing Existing Templates
When either fixing a bug within a template or adding additional **Values** to be captured, additional test files should be added to ensure backwards compatibility and that the new data is being parsed correctly.

To add additional raw/parsed tests for a command:
- Navigate to `./tests/{{ vendor_os }}/{{ command_name }}/`
- Create new `.raw` and `.yml` files within the directory, preferrably with a name identifying why the data is unique:
  * Existing raw: `./tests/cisco_ios/show_version/cisco_ios_show_version.raw`
  * New raw: `./tests/cisco_ios/show_version/cisco_ios_show_version_stack_platforms.raw`
  * Existing parsed: `./tests/cisco_ios/show_version/cisco_ios_show_version.yml`
  * New parsed: `./tests/cisco_ios/show_version/cisco_ios_show_version_stack_platforms.yml`

#### Testing
You can test your changes locally within your Git branch before submitting a PR. If you do not have **tox** already installed, you can do that using pip or your systems package manager. Tox should be ran inside the **ntc-templates** root directory. The tox file is configured to run against python3.6,python3.7, and python3.8, if none/some of those python versions are unavailable **tox** will skip them. The tox.ini file can be updated with an available Python version.
```bash
$ tox
GLOB sdist-make: /home/travis/build/networktocode/ntc-templates/setup.py
py36 create: /home/travis/build/networktocode/ntc-templates/.tox/py36
py36 inst: /home/travis/build/networktocode/ntc-templates/.tox/.tmp/package/1/ntc_templates-1.6.0.zip
py36 installed: appdirs==1.4.4,attrs==20.3.0,black==20.8b1,click==7.1.2,dataclasses==0.8,future==0.18.2,importlib-metadata==3.7.0,iniconfig==1.1.1,mypy-extensions==0.4.3,ntc-templates==1.6.0,packaging==20.9,pathspec==0.8.1,pluggy==0.13.1,py==1.10.0,pyparsing==2.4.7,pytest==6.2.2,PyYAML==5.4.1,regex==2020.11.13,ruamel.yaml==0.16.12,ruamel.yaml.clib==0.2.2,six==1.15.0,textfsm==1.1.0,toml==0.10.2,typed-ast==1.4.2,typing-extensions==3.7.4.3,yamllint==1.26.0,zipp==3.4.0
py36 run-test-pre: PYTHONHASHSEED='4147443973'
py36 run-test: commands[0] | black ./ --diff --check
All done! ✨ 🍰 ✨
9 files would be left unchanged.
py36 run-test: commands[1] | yamllint tests/
py36 run-test: commands[2] | pytest -vv
============================= test session starts ==============================
platform linux -- Python 3.6.7, pytest-6.2.2, py-1.10.0, pluggy-0.13.1 -- /home/travis/build/networktocode/ntc-templates/.tox/py36/bin/python
cachedir: .tox/py36/.pytest_cache
rootdir: /home/travis/build/networktocode/ntc-templates
collected 1065 items                                                           

tests/test_development_scripts.py::test_ensure_spacing_for_multiline_comment PASSED [  0%]
tests/test_development_scripts.py::test_ensure_space_after_octothorpe PASSED [  0%]
tests/test_development_scripts.py::test_ensure_space_comments PASSED     [  0%]
tests/test_development_scripts.py::test_update_yaml_comments PASSED      [  0%]
tests/test_development_scripts.py::test_transform_file PASSED            [  0%]
tests/test_testcases_exists.py::test_verify_parsed_and_reference_data_exists[tests/yamaha/show_environment] PASSED [ 99%]
tests/test_testcases_exists.py::test_verify_parsed_and_reference_data_exists[tests/yamaha/show_ip_route] PASSED [100%]

============================ 1065 passed in 22.59s =============================
py37 create: /home/travis/build/networktocode/ntc-templates/.tox/py37
SKIPPED: InterpreterNotFound: python3.7
py38 create: /home/travis/build/networktocode/ntc-templates/.tox/py38
SKIPPED: InterpreterNotFound: python3.8
___________________________________ summary ____________________________________
  py36: commands succeeded
SKIPPED:  py37: InterpreterNotFound: python3.7
SKIPPED:  py38: InterpreterNotFound: python3.8
  congratulations :)
The command "tox" exited with 0.


Done. Your build exited with 0.
$
```

Questions
---------

For any questions or comments, please feel free to swing by the [networktocode slack channel](https://networktocode.slack.com).

Sign up [here](http://slack.networktocode.com/)

CHANGELOG
---------

Changelog should be generated using [github_changelog_generator](https://github.com/github-changelog-generator/github-changelog-generator)

FAQ
---

From an outsiders view, some design choices, requirements, and testing procedures can seem arbitrary. The following list of FAQ is intended to 
help provide context and better guide users and contributors of ntc-templates.

_Why is there a requirement to use `Error` in every template?_

Ensuring that the textfsm template can account for every line is the only method to ensure that data was not accidentally missed. Take the following example. Initially we account for status to be:

`Value STATUS (up|down)`

Given the result of:
```
Interface                      Status         Protocol Description
Gi0/0/1                        admin down     down
Gi0/0/2                        up             up       ISP Connection
Gi0/0/3                        down           down
```

The output would miss the G0/0/1 interface, since the `STATUS` of `admin down` not known. If this was a low percentage use case, it can go 
undetected, and result in incorrect information being returned. Instead, by ensuring that we fail fast, an `Error` is raised and hopefully 
GitHub Issue is put in. 

_Then why isn't `Error` used in all templates?_

Initially the controls were not as strong, so many templates were put in until issues like the previous became an issue.

_Does the project support requests for additional templates or additional data in an existing template?_

We are no longer considering additional template requests at this time. The project has existed for over 5 years (initially within ntc-ansible)
and nearly 200 template at this point any additional requests are essentially edge use cases. Meaning, for five years of usage, no one else 
has asked for this feature. There is a limited maintainers who primarily use their free time to maintain the project.

_Are you open to adding maintainers to the project?_

Yes, we would consider giving a proven member of the project and community maintainer rights. Please inquiry emailing info@networktocode.com.

_I simply want to add my template to the project, I do not want to add all of these tests and controls, can I just do so?_

Short answer no, from an outsiders point of view the contributor requirements may seem overly complex, however features added by engineers 
rarely come back to support them. The burden of support is on the maintainers and a certain level of quality assurance is required for that to 
happen. That includes updating the index file appropriately and adding proper raw and expected value files.

_Why don't you grab all of the data in the template?_

There is no intention for ntc-templates to become feature complete, some of the data is less interesting, or can be better understood from 
other commands. This is actually an area where the project chose to be loose, as we do not want to over-burden the contributor. If you feel 
that the additional data should be added, you are welcome to add the feature, but it would not be considered a bug, and thus not supported by 
the maintainers of the this project.

_Why does the index order matter?_

The "greediness" of the template match ensures that there longest matches first. For example, if `show ip ospf` was above `show ip ospf database`, the `show ip ospf` template would be used in both cases. The additional steps are because of general programmatic hygiene.

_Will you accept my template if I create it?_

In most cases, yes. However, there are a few edge cases. For example if requesting to add a `show cdp neighbors` when there is already a `show cdp neighbors details` template created. That is additional complexity added to the project with little value.

_Why was my issue closed?_

The most likely reasons are:

* Did not follow the Issue creation template.
* Did not provide the data required to act upon the request.
* A prolonged time with no response.  

_What is meant that this is a parsing project, not a data modeling project?_

The project intends to parse, meaning post processing is assumed in order to normalize the data. This project does not intend to solve that 
problem set. This is often noted in keys being different between the same command on multiple OS's. This was not intentional as at first there was not strict enforcement. That being said, there is no intention to retrofit this use case for the above stated reasons. This use case is 
best handled in post processing.

_I have never submitted a Pull Request before, how do I do so?_

This is outside the scope of this project, but this [video](https://www.youtube.com/watch?v=rgbCcBNZcdQ) should provide the instructions on 
how to do so.

_Does this work on windows?_

Based on this [PR](https://github.com/networktocode/ntc-templates/pull/672) it should, however this is not a supported option. We are willing 
to take in qualified Pull Requests to have the feature, but have no intention of actively supporting.

_Can you provide general guidance?_

This is best handled via real time communication. Feel free to join our slack community (sign up information above) and reach out on the #networktocode channel. Please be aware of timezones, downtimes, and help is performed based on goodwill and timing, and not guaranteed.

### Known Issues

#### Cannot import name clitable from textfsm
**ntc-templates** depends on **textfsm**, which hasn't published a source distribution to pypi in a while. See https://github.com/google/textfsm/issues/65.

This means that for users with a build chain that depends on source distributions only (i.e. no wheels), ntc-templates appears to have a bug:

```
File "/usr/local/Cellar/foo/version/libexec/lib/python3.7/site-packages/ntc_templates/parse.py", line 3, in <module>
    from textfsm import clitable
ImportError: cannot import name 'clitable' from 'textfsm' 
```

What's actually happening here is that textfsm provides a source distribution only up to version 0.4.1 (2018-04-09) but the ntc-templates code relies on the interface from version 1.1.0 (2019-07-24) which is only available as a wheel. So the way for users to fix this problem if they encounter it is to install textfsm 1.1.0.

`pip install textfsm==1.1.0`

> This was taken from https://github.com/networktocode/ntc-templates/issues/731
