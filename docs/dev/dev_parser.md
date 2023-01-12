# Config Parsers Development

To contribute new templates, each new pull request must include the following:

- Only update or create a single template per Pull Request
- TextFSM template
- Modified version of the **index** file
- Tests
    - Raw version of text to be parsed
    - YAML file containing the expected parsed dictionary

## TextFSM Template

TextFSM templates should be placed in the `./templates` directory and should adhere to the following NTC-Templates style. The TextFSM template name should be in the following format:

### Naming

The template should be named using: `{{ vendor_os }}_{{ command_with_underscores }}.textfsm`

> Example: cisco_ios_show_cdp_neighbors.textfsm

!!! tip
    The vendor name must be valid from the [os_choices](https://github.com/networktocode/ntc-templates/blob/master/tests/test_index_order.py#L59) tests, which is primarily based on [Netmiko](https://github.com/ktbyers/netmiko/tree/master/netmiko) list of supported vendors. New vendors added should adhere to **vendor_os**.

    Example: vmware_nsx

### Values

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
### States

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

#### Error Directive

Each **state** should end with `^. -> Error`. This helps to ensure that every line is accounted for within the raw output for the command. This doesn't mean we have to capture all the data as a **Value**, but we do have to account for it. In addition, it is also good to provide an expression to match blank lines, `^\s*$$`

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

Taking a look at the example template above, you notice that we're using `\s*` and `\s+`. This is the preferred way to match space characters, and should be used over the literal space character. For example, `This\s+is\s+preferred\s*$$` vs `This is not preferred$$`

- `\s*` accounts for zero or more spaces (use when the output may or may not have a space between characters)
- `\s+` accounts for one or more spaces (use when output will have a space, but could have more than one space)

## Index File

The Index file binds the templates to the commands being run. Special care has been taken on ordering, as there is potential for issues. e.g. `show ip route` picking up for `show ip router vrf <vrf-name>`. We have used the combination of ordering, as defined:

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

## Tests

Tests will be located in `./tests` with the following hierarchy:

- `./tests/{{ vendor_os }}/{{ command_name }}/`

The `{{ command_name }}` directory should include the `.raw` file that includes the raw output of the command to be parsed, and the `.yml` file of the returned structured data.

```bash
$ ls tests/cisco_ios/show_clock/
cisco_ios_show_clock.yml
cisco_ios_show_clock.raw
$ 
```

### Raw version of input text

The raw text file should contain **only** the output of the CLI command to be parsed. It should **not** contain the CLI command itself.

An example of the proper format is shown below:

```bash
$ cat tests/cisco_ios/show_clock/cisco_ios_show_clock.raw
*18:57:38.347 UTC Mon Oct 19 2015
$ 
```

### YAML file containing expected parsed dictionary

The parsed file should match the data that is returned from the `parse_output` function discussed in the beginning. Dictionary keys should be in lowercase.

The parsed text file should be placed in a directory in the `./tests` directory with the same name as the template file but replace `.textfsm` file extension with `.yml`. The raw text file and the parsed text file should be in the same directory.

> Example. ./tests/cisco_ios/show_clock/

There are available helpers to create the parsed file in the correct format (See below for details).

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

## Development Helper Scripts

A click cli utility is provided to assist with properly building the parsed files. This utility depends on some packages listed in the dev install requirements. The commands are:

- `clean-yaml-file`: Takes the path to a YAML file and updates to ensure that the file adheres to the .yamllint settings
- `clean-yaml-folder`: Takes a directory that will updates to ensure all files ending in `.yml` adhere to the .yamllint settings
- `gen-yaml-file`: Takes the path to a `.raw` file, and generates the parsed data and saves the results adjacent to the `.yml` file following the defined standards in .yamllint.
- `gen-yaml-folder`: Takes a glob path to a directory containing `.raw` files, and creates the appropriate parsed files in the appropriate directory.

```bash
$ python cli.py --help
Usage: cli.py [OPTIONS] COMMAND [ARGS]...

  Base entry for click.

Options:
  --help  Show this message and exit.

Commands:
  clean-yaml-file    Transform a yaml file to expected output.
  clean-yaml-folder  Transform a yaml file to expected output to a folder.
  gen-yaml-file      Generate a yaml file from raw a data file.
  gen-yaml-folder    Generate a yaml file from folder of raw data files.
$ 
```

The `clean-yaml-file` and `clean-yaml-folder` arguments are designed to allow developers to generate the expected parsed file how they want, and ensure that the formatting adheres to the defined standard for this project.

The `gen-yaml-file` and `gen-yaml-file` arguments generate the parsed data. This means that you can use these arguments to auto-generate the test `.yml` file(s) for new templates; just be sure that the template's parsing behavior meets expectations. In order for the data to be parsed, the template must be placed in `ntc_templates/templates/` and the `ntc_templates/templates/index` file must be updated to correctly point to the template file(s).

```bash
$ python cli.py clean-yaml-folder -f tests/cisco_ios/show_mac-address-table
tests/cisco_ios/show_mac-address-table/cisco_ios_show_mac-address-table.yml
tests/cisco_ios/show_mac-address-table/cisco_ios_show_mac-address-table12.yml
tests/cisco_ios/show_mac-address-table/cisco_ios_show_mac-address-table13.yml
tests/cisco_ios/show_mac-address-table/cisco_ios_show_mac-address-table2.yml
tests/cisco_ios/show_mac-address-table/cisco_ios_show_mac-address-table3.yml
tests/cisco_ios/show_mac-address-table/cisco_ios_show_mac-address-table4.yml
tests/cisco_ios/show_mac-address-table/cisco_ios_show_mac-address-table5.yml
tests/cisco_ios/show_mac-address-table/cisco_ios_show_mac-address-table6.yml
tests/cisco_ios/show_mac-address-table/cisco_ios_show_mac-address-table7.yml
tests/cisco_ios/show_mac-address-table/cisco_ios_show_mac-address-table8.yml
tests/cisco_ios/show_mac-address-table/cisco_ios_show_mac-address-table9.yml
$ 
```

Additionally, each of these commands are available via invoke commands to better support a docker environment. The arguement names match up, e.g. `python cli.py clean-yaml-file` has an equivalant `invoke clean-yaml-file`.

# Updating/Fixing Existing Templates
When either fixing a bug within a template or adding additional **Values** to be captured, additional test files should be added to ensure backwards compatibility and that the new data is being parsed correctly.

To add additional raw/parsed tests for a command:

- Navigate to `./tests/{{ vendor_os }}/{{ command_name }}/`
- Create new `.raw` and `.yml` files within the directory, preferrably with a name identifying why the data is unique:
    - Existing raw: `./tests/cisco_ios/show_version/cisco_ios_show_version.raw`
    - New raw: `./tests/cisco_ios/show_version/cisco_ios_show_version_stack_platforms.raw`
    - Existing parsed: `./tests/cisco_ios/show_version/cisco_ios_show_version.yml`
    - New parsed: `./tests/cisco_ios/show_version/cisco_ios_show_version_stack_platforms.yml`

## Testing

You can test your changes locally within your Git branch before submitting a PR.

```bash
% invoke tests
DOCKER - Running command: black --check --diff . container: ntc_templates:3.1.0-py3.7
All done! ✨ 🍰 ✨
9 files would be left unchanged.
DOCKER - Running command: flake8 . --config .flake8 container: ntc_templates:3.1.0-py3.7
DOCKER - Running command: find . -name "*.py" | xargs pylint container: ntc_templates:3.1.0-py3.7

------------------------------------
Your code has been rated at 10.00/10

DOCKER - Running command: yamllint . container: ntc_templates:3.1.0-py3.7
[...] 
```

> Note: Omitted for brevity.