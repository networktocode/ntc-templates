[![Build Status](https://travis-ci.org/networktocode/ntc-templates.svg?branch=master)](https://travis-ci.org/networktocode/ntc-templates)

REPOSITORY OF TEXTFSM TEMPLATES FOR NETWORK DEVICES


NTC-Templates contains a set of multi-vendor templates based around TEXTFSM parsing engine.

These templates take the raw string input from the CLI of network infrastructure devices, such as Cisco IOS, Juniper JUNOS
or HPE Comware devices, run them through a TEXTFSM template and return structured text in the form of a python dictionary.


#Contributing

Pull request are welcomed and will be automatically built and tested through TravisCI.

To contribute new templates, each new pull request *must* include the folowing

-  TextFSM template
-  raw version of text to be parsed
-  YAML file containing the expected parsed dictionary
- Modified version of the **index** file


Some notes on contributing that should help you ensure that your TravisCI builds comes back as successfull





## TextFSM Templates

TextFSM templates should be placed in the ./templates folder and should adhere to the NTC-Templates style.
The TextFSM template name should be in the following format

{{ vendor_name }}_{{show_command}}

Note: The vendor name must be valid from the [Netmiko](https://github.com/ktbyers/netmiko/tree/master/netmiko)  


The **Value** variable should be in UPPERCASE. 

An example of the proper format is shown below.

<pre>Value TIME (\d+:\d+:\d+)
Value TIMEZONE (\S+)
Value DAYWEEK (\w+)
Value MONTH (\d+)
Value DAY (\d+)
Value YEAR (\d+)

Start
  ^${TIME}\s+${TIMEZONE}\s+${DAYWEEK}\s+${DAY}/${MONTH}/${YEAR} -> Record  </pre>

## Raw version of Input Text


The raw text file should contain **only** the output of the CLI command to be parsed. It should **not** contain the CLI command itself
The raw text file should be placed in a folder in the ./tests directory with the same name as the template file minus the .template extension

An example of the proper format is shown below

<pre>
19:35:31 UTC Sat 01/08/2011
</pre>

## YAML file containing expected parsed dictionary


The parsed dictionary must be in a dictionary format. All keys in the dictionary should be in all lowercase

The parsed text file should be placed in a folder in the ./tests directory with the same name as the template file minus the .template extension.
The raw text file and the parsed text file should be in the same folder.

An example of the proper format is shown below


<pre>

---

parsed_sample:


- {day: '01', dayweek: Sat, month: 08, time: '19:35:31', timezone: UTC, year: '2011'}
</pre>


### Automating the creation of the parsed file

This sample code was used to successfuly dump the parsed file contents and is provided for information only. 


<pre> 

template = open("./templates/hp_comware_display_interfaces.template")
re_table = textfsm.TextFSM(template)
fsm_results = re_table.ParseText(displayinterfaces)

results = []
for i in fsm_results:
    keys = (re_table.header)
    keys = [ i.lower() for i in keys]
    values = i
    record = dict(zip(keys, values))
    results.append(record)

print (yaml.dump(results, indent = 4))

</pre>


## Index File

The index file is located in the ./templates directory and must be updaetd with new templates. 
Please note that the file is processed in order using a first match method.
If there is overlap in the name of commands, please put the more specific commands closer to the top of the file to ensure that the greedier match does prevent the more specific match from being selected.




#Questions

For any questions or comments, please feel free to swing by the [networktocode slack channel](https://networktocode.slack.com)

sign up [here](http://slack.networktocode.com/)