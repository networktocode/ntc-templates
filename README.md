[![Build Status](https://travis-ci.org/networktocode/ntc-templates.svg?branch=master)](https://travis-ci.org/networktocode/ntc-templates)

NTC TEMPLATES
=============

Repository of TextFSM Templates for Network Devices, and Python wrapper for TextFSM's CliTable.

[TextFSM](https://github.com/google/textfsm/wiki) is a project built by Google that takes CLI string output and passes each line through a series of regular expressions until it finds a match. The regular expressions use named capture groups to build a text table out of the significant text. The names of the capture groups are used as column headers, and the captured values are stored as rows in the table.

This project provides a large collection of TextFSM Templates (text parsers) for a variety of Networking Vendors. In addition to the templates, there is a function that will convert the CLI output into a CliTable object; the resulting text table is converted into a list of dictionaries mapping the column headers with each row in the table.


Installation and Usage
----------------------
The project can be installed using either Git or PyPI; if you would like to use the templates outside of this project, then Git is the recommended approach.

#### Git

```shell
$ git clone git@github.com:networktocode/ntc-templates.git
$ 
# Optional steps to install ntc-templates as a python package
$ pip install -e ntc-templates/
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

The template should be named using: `{{ vendor_os }}_{{ command_with_underscores }}.template`
> Ex: cisco_ios_show_cdp_neighbors.template

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

If the raw output has a heading, the `Start` state should match on the column headings and then transition to another state that will match the device's output table with the capture groups. This helps ensure the regex patterns for the capture groups are attempting to match the correct information, and allows templates to easily add additional States for tables that have different headings. Example:

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
 - Template name in length order
 - When length is the same, use alphabetical order of command name
 - Keep space between OS's

Example:

```
Template, Hostname, Platform, Command

# same os, same length, used alphabetical order of command name
arista_eos_show_mlag.template, .*, arista_eos, sh[[ow]] ml[[ag]]
arista_eos_show_vlan.template, .*, arista_eos, sh[[ow]] vl[[an]]

# os in alphabetical order and space between cisco_asa and arista_eos
cisco_asa_dir.template,  .*, cisco_asa, dir

# same os, template name length different and space between cisco_asa and cisco_ios
cisco_ios_show_capability_feature_routing.template,  .*, cisco_ios, sh[[ow]] cap[[ability]] f[[eature]] r[[outing]]
cisco_ios_show_interface_transceiver.template, .*, cisco_ios, sh[[ow]] int[[erface]] trans[[ceiver]]
cisco_ios_show_cdp_neighbors_detail.template, .*, cisco_ios, sh[[ow]] c[[dp]] neig[[hbors]] det[[ail]]
```

#### Tests
Tests will be located in `./tests` with the following hierarchy:
- `./tests/{{ vendor_os }}/{{ command_name }}/`

The `{{ command_name }}` directory should include the `.raw` file that includes the raw output of the command to be parsed, and the `.parsed` file of the returned structured data.
```bash
$ ls tests/cisco_ios/show_clock/
cisco_ios_show_clock.parsed
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

The parsed text file should be placed in a directory in the `./tests` directory with the same name as the template file but replace `.template` file extension with `.parsed`. The raw text file and the parsed text file should be in the same directory.
**ex. ./tests/cisco_ios/show_clock/**

There is an available helper that uses **Ansible** and **ntc-ansible** custom modules to create the parsed file automatically into the correct format. Helpers are located within `./helpers/`.

An example of the proper format is shown below:
```bash
$ cat ./tests/cisco_ios/show_clock/cisco_ios_show_clock.parsed
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

### Updating/Fixing Existing Templates
When either fixing a bug within a template or adding additional **Values** to be captured, additional test files should be added to ensure backwards compatibility and that the new data is being parsed correctly.

To add additional raw/parsed tests for a command:
- Navigate to `./tests/{{ vendor_os }}/{{ command_name }}/`
- Create new `.raw` and `.parsed` files within the directory, preferrably with a name identifying why the data is unique:
  * Existing raw: `./tests/cisco_ios/show_version/cisco_ios_show_version.raw`
  * New raw: `./tests/cisco_ios/show_version/cisco_ios_show_version_stack_platforms.raw`
  * Existing parsed: `./tests/cisco_ios/show_version/cisco_ios_show_version.parsed`
  * New parsed: `./tests/cisco_ios/show_version/cisco_ios_show_version_stack_platforms.parsed`

#### Testing
You can test your changes locally within your Git branch before submitting a PR. If you do not have **tox** already installed, you can do that using pip or your systems package manager. Tox should be ran inside the **ntc-templates** root directory. The tox file is configured to run against python3.6, so either python3.6 needs to be available, or the tox.ini file will need to be updated with an available Python version.
```bash
$ tox
GLOB sdist-make: /home/admin/ntc-templates/setup.py
py36 inst-nodeps: /home/admin/ntc-templates/.tox/dist/ntc_templates-1.1.0.zip
py36 installed: atomicwrites==1.3.0,attrs==19.1.0,importlib-metadata==0.18,more-itertools==7.1.0,ntc-templates==1.1.0,packaging==19.0,pkg-resources==0.0.0,pluggy==0.12.0,py==1.8.0,pyparsing==2.4.0,pytest==5.0.1,PyYAML==5.1.1,six==1.12.0,terminal==0.4.0,textfsm==0.4.1,wcwidth==0.1.7,zipp==0.5.2
py36 runtests: PYTHONHASHSEED='1913863515'
py36 runtests: commands[0] | pytest
=============================================================================== test session starts ================================================================================
platform linux -- Python 3.6.8, pytest-5.0.1, py-1.8.0, pluggy-0.12.0
rootdir: /home/admin/ntc-templates
collected 364 items

tests/test_index_order.py .                                                                                                                                                  [  0%]
tests/test_structured_data_against_parsed_reference_files.py ............................................................................................................... [ 30%]
............................................................................................................................................................................ [ 78%]
...............................................................................                                                                                              [ 99%]
tests/test_testcases_exists.py .                                                                                                                                             [100%]

=========================================================================== 364 passed in 15.69 seconds ============================================================================
_____________________________________________________________________________________ summary ______________________________________________________________________________________
  py36: commands succeeded
  congratulations :)
```

Questions
---------

For any questions or comments, please feel free to swing by the [networktocode slack channel](https://networktocode.slack.com).

Sign up [here](http://slack.networktocode.com/)
