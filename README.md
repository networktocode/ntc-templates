

REPOSITORY OF TEXTFSM TEMPLATES FOR NETWORK DEVICES


NTC-Templates contains a set of multi-vendor templates based around TEXTFSM parsing engine.

These templates take the raw string input from the CLI of network infrastructure devices, such as Cisco IOS, Juniper JUNOS
or HPE Comware devices, run them through a TEXTFSM template and return structured text in the form of a Python dictionary.


# Contributing

Pull request are welcomed and automatically built and tested through TravisCI.

## New Templates
To contribute new templates, each new pull request must include the following:

- TextFSM template
- Tests
  - Raw version of text to be parsed
  - YAML file containing the expected parsed dictionary
- Modified version of the **index** file

### TextFSM Template

TextFSM templates should be placed in the `./templates` folder and should adhere to the following NTC-Templates style.
The TextFSM template name should be in the following format:

```
{{ vendor_name }}_{{show_command}}

ex. cisco_ios_show_cdp_neighbors.template
```
Note: The vendor name must be valid from the [os_choices](https://github.com/networktocode/ntc-templates/blob/master/tests/test_index_order.py#L59) tests, which is primarily based on [Netmiko](https://github.com/ktbyers/netmiko/tree/master/netmiko) list of supported vendors. New vendors added should adhere to **vendor**_**os**.
**ex. vmware_nsx**

**Values**
The **Value** variable should be in UPPERCASE.

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
**STATES**
If the raw output has a heading, **Start** state should match on the column headings and then transition to another state that will match the column headings and capture groups. This helps ensure the regex patterns for the capture groups are attempting to match the correct information and help if the raw output does change in the future that a new state can be created to match both the old and new format of the raw data.
**Raw Output**
```
... omitted
Network Next Hop Metric LocPrf Weight Path
*> 111.111.111.111/32 112.112.112.112 4294967295 4294967295 65535 1000 1000 1000 i
```
**Sample Template**
```
Start
# Checking for header
^\s*Network\s+Next(?:\s+|-)[Hh]op\s+Metric\s+LocPrf\s+Weight\s+Path\s*$$ -> BGPTable

BGPTable
 ... omitted
```
Each **state** should end with `^. -> Error`. This helps to ensure we're accounting for every line within the raw output for the command. This doesn't mean we have to capture all the data as a **Value**, but we do have to account for it.

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
  ^\s*
  ^. -> Error
```
Later on we could simply add **PID**, **VID**, and **SN** as **Values** to be captured within the template.

Taking a look at the example template above, you notice that we're using **\s*** and **\s+**. These both are accounting for spaces between characters. These are the preferred method to account for spaces between characters rather than statically accounting for the spaces.
- **\s*** accounts for zero or more spaces (use when the output may or may not have a space between characters)
- **\s+** accounts for one or more spaces (use when output will have a space, but could have more than one space)

### Tests
Tests will be located in `./tests` with the following hierarchy:
- `./tests/{{ vendor_name }}/{{ command_name }}/`

Within the `{{ command_name }}` folder should include the `.raw` file that includes the raw output of the command to be parsed, and the `.parsed` file of the returned structured data.
```
(main) ~/ntc-templates[update-readme !]:~$ ls tests/cisco_ios/show_clock/
cisco_ios_show_clock.parsed
cisco_ios_show_clock.raw
```

#### Raw version of input text

The raw text file should contain **only** the output of the CLI command to be parsed. It should **not** contain the CLI command itself.
The raw text file should be placed in a folder in the `./tests` directory with the same name as the template file minus the .template extension

An example of the proper format is shown below:

**./tests/cisco_ios/show_clock/cisco_ios_show_clock.raw**
```
19:35:31 UTC Sat 01/08/2011
```

#### YAML file containing expected parsed dictionary

The parsed dictionary must be in a dictionary format. All keys in the dictionary should be in all lowercase.

The parsed text file should be placed in a folder in the `./tests` directory with the same name as the template file but replace `.template` file extension with `.parsed`. The raw text file and the parsed text file should be in the same folder.
**ex. ./tests/cisco_ios/show_clock/**

There is an available helper that uses **Ansible** and **ntc-ansible** custom modules to create the parsed file automatically into the correct format. Helpers are located within `./helpers/`.

An example of the proper format is shown below:
**./tests/cisco_ios/show_clock/cisco_ios_show_clock.parsed**
```yaml
---

parsed_sample:
- time: "18:57:38.347"
  timezone: "UTC"
  dayweek: "Mon"
  month: "Oct"
  day: "19"
  year: "2015"
```

Multiple RAW and Parsed files are supported per folder, and are encouraged, as there are differences depending on version, length, etc... that additional testing and more real life data helps ensure backwards compatibility is maintained as each template is updated and merged into the repo.

### Index File

The Index file binds the templates to the commands being run. Special care has been taken on ordering, as there is potential for issues. e.g. `show ip route` picking up for `show ip router vrf <vrf-name>`. We have used a combination of ordering, as defined:

 - OS in alphabetical order
 - Command in length order
 - When length is the same, use alphabetical order of command name
 - Keep space between OS's

Example:

```
Template, Hostname, Platform, Command

**same os, same length, used alphabetical order of command name**
arista_eos_show_mlag.template, .*, arista_eos, sh[[ow]] ml[[ag]]
arista_eos_show_vlan.template, .*, arista_eos, sh[[ow]] vl[[an]]

**os in alphabetical order and space between cisco_asa and arista_eos**
cisco_asa_dir.template,  .*, cisco_asa, dir

**same os, command length different and space between cisco_asa and cisco_ios**
cisco_ios_show_capability_feature_routing.template,  .*, cisco_ios, sh[[ow]] cap[[ability]] f[[eature]] r[[outing]]
cisco_ios_show_interface_transceiver.template, .*, cisco_ios, sh[[ow]] int[[erface]] trans[[ceiver]]
cisco_ios_show_cdp_neighbors_detail.template, .*, cisco_ios, sh[[ow]] c[[dp]] neig[[hbors]] det[[ail]]
```
## Updating/Fixing Existing Templates
When either fixing a bug within a template or adding additional **Values** to be captured additional tests should be added for the template on top of the already existing templates to ensure backwards compatibility and that the new data is being parsed correctly.

To add additional raw/parsed tests for a command:
- Navigate to `./tests/{{ vendor_name }}/{{ command_name }}/`
- Create new `.raw` and `.parsed` files within the directory, but append the next number up
        - Existing raw: `./tests/cisco_ios/show_clock/cisco_ios_show_clock1.raw`
        - New raw: `./tests/cisco_ios/show_clock/cisco_ios_show_clock2.raw`
        - Existing parsed: `./tests/cisco_ios/show_clock/cisco_ios_show_clock1.parsed`
        - New parsed: `./tests/cisco_ios/show_clock/cisco_ios_show_clock2.parsed`

### Testing
You can test your changes locally within your Git branch before submitting a PR. This can be done by installing **tox** within your environment using pip and then running **tox** within the **ntc-templates** root directory:
```
(main) ~/ntc-templates[update-readme !]:~$ tox
GLOB sdist-make: /home/myohman/ntc-templates/setup.py
py36 inst-nodeps: /home/myohman/ntc-templates/.tox/dist/ntc_templates-1.1.0.zip
py36 installed: atomicwrites==1.3.0,attrs==19.1.0,importlib-metadata==0.18,more-itertools==7.1.0,ntc-templates==1.1.0,packaging==19.0,pkg-resources==0.0.0,pluggy==0.12.0,py==1.8.0,pyparsing==2.4.0,pytest==5.0.1,PyYAML==5.1.1,six==1.12.0,terminal==0.4.0,textfsm==0.4.1,wcwidth==0.1.7,zipp==0.5.2
py36 runtests: PYTHONHASHSEED='1913863515'
py36 runtests: commands[0] | pytest
=============================================================================== test session starts ================================================================================
platform linux -- Python 3.6.8, pytest-5.0.1, py-1.8.0, pluggy-0.12.0
rootdir: /home/myohman/ntc-templates
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

# Questions

For any questions or comments, please feel free to swing by the [networktocode slack channel](https://networktocode.slack.com).

Sign up [here](http://slack.networktocode.com/)
