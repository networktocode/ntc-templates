[![Build Status](https://travis-ci.org/networktocode/ntc-templates.svg?branch=master)](https://travis-ci.org/networktocode/ntc-templates)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

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

The install can also include the required dev packages, which can be useful for adding or editing templates:

```shell
$ git clone git@github.com:networktocode/ntc-templates.git
$ 
# Optional steps to install ntc-templates as a python package
$ pip install -e ntc-templates/[dev]
$ 
```

#### PyPI

```shell
$ pip install ntc_templates
$ 
```

To include the dev packages:
```
$ pip install ntc_templates[dev]
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

  The `-c` and `-cd` arguments use `lib.ntc_templates.parse.parse_output()` to generate the parsed data; this means that you can use these arguments to auto-generate the test `.yml` file(s) for new templates; just be sure that the template's parsing behavior meets expectations. In order for the data to be parsed, the template must be placed in `templates/` and the `templates/index` file must be updated to correctly point to the template file(s).

```bash
$ /development_scripts.py -yd tests/cisco_ios/show_mac-address-table
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
You can test your changes locally within your Git branch before submitting a PR. If you do not have **tox** already installed, you can do that using pip or your systems package manager. Tox should be ran inside the **ntc-templates** root directory. The tox file is configured to run against python3.6, so either python3.6 needs to be available, or the tox.ini file will need to be updated with an available Python version.
```bash
$ tox
GLOB sdist-make: /home/admin/ntc-templates/setup.py
py36 inst-nodeps: /home/admin/ntc-templates/.tox/dist/ntc_templates-1.3.0.zip
py36 installed: appdirs==1.4.3,atomicwrites==1.3.0,attrs==19.3.0,black==19.10b0,Click==7.0,future==0.18.2,importlib-metadata==0.23,more-itertools==7.2.0,ntc-templates==1.3.0,packaging==19.2,pathspec==0.6.0,pluggy==0.13.0,py==1.8.0,pyparsing==2.4.5,pytest==5.2.4,PyYAML==5.1.2,regex==2019.11.1,six==1.13.0,terminal==0.4.0,textfsm==1.1.0,toml==0.10.0,typed-ast==1.4.0,wcwidth==0.1.7,yamllint==1.18.0,zipp==0.6.0
py36 runtests: PYTHONHASHSEED='3677750645'
py36 runtests: commands[0] | black ./ --diff --check
All done! ✨ 🍰 ✨
8 files would be left unchanged.
py36 runtests: commands[1] | yamllint tests/
py36 runtests: commands[2] | pytest -vv
================================================================ test session starts =================================================================
platform linux -- Python 3.6.8, pytest-5.2.4, py-1.8.0, pluggy-0.13.0 -- /home/jmcgill/repos/ntc-templates/.tox/py36/bin/python3.6
cachedir: .pytest_cache
rootdir: /home/jmcgill/repos/ntc-templates
collected 428 items                                                                                                                                  

tests/test_index_order.py::test_index_ordering PASSED                                                                                          [  0%]
tests/test_structured_data_against_parsed_reference_files.py::test_raw_data_against_mock[tests/alcatel_sros/oam_mac-ping/alcatel_sros_oam_mac-ping.raw] PASSED [  0%]
tests/test_structured_data_against_parsed_reference_files.py::test_raw_data_against_mock[tests/alcatel_sros/show_service_id_base/alcatel_sros_show_service_id_base.raw] PASSED [  0%]
tests/test_structured_data_against_parsed_reference_files.py::test_raw_data_against_mock[tests/alcatel_sros/show_router_bgp_routes_vpn-ipv4/alcatel_sros_show_router_bgp_routes_vpn-ipv4.raw] PASSED [  0%]
tests/test_structured_data_against_parsed_reference_files.py::test_raw_data_against_mock[tests/brocade_fastiron/show_lldp_neighbors/brocade_fastiron_show_lldp_neighbors.raw] PASSED [  1%]
...
tests/test_structured_data_against_parsed_reference_files.py::test_raw_data_against_mock[tests/cisco_nxos/show_ip_interface_brief/cisco_nxos_show_ip_interface_brief.raw] PASSED [ 99%]
tests/test_testcases_exists.py::test_verify_parsed_and_reference_data_exists PASSED                                                            [100%]

================================================================ 428 passed in 43.84s ================================================================
______________________________________________________________________ summary _______________________________________________________________________
  py36: commands succeeded
  congratulations :)
$
```

Questions
---------

For any questions or comments, please feel free to swing by the [networktocode slack channel](https://networktocode.slack.com).

Sign up [here](http://slack.networktocode.com/)
