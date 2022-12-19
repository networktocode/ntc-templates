# Frequently Asked Questions

From an outsiders view, some design choices, requirements, and testing procedures can seem arbitrary. The following list of FAQ is intended to help provide context and better guide users and contributors of ntc-templates.

## How do I test my templates?

You can follow the local development procedures, but for your convenience here are included locations to test your template:

* [textfsm.nornir.tech](https://textfsm.nornir.tech/) - An online textfsm editor.
* [Itential](https://template.itential.io/) - An online textfsm editor by Itential.

## Why is there a requirement to use `Error` in every template?

Ensuring that the textfsm template can account for every line is the only method to ensure that data was not accidentally missed. Take the following example. Initially we account for status to be:

`Value STATUS (up|down)`

Given the result of:
```
Interface                      Status         Protocol Description
Gi0/0/1                        admin down     down
Gi0/0/2                        up             up       ISP Connection
Gi0/0/3                        down           down
```

The output would miss the G0/0/1 interface, since the `STATUS` of `admin down` not known. If this was a low percentage use case, it can go undetected, and result in incorrect information being returned. Instead, by ensuring that we fail fast, an `Error` is raised and hopefully GitHub Issue is put in. 

### Then why isn't `Error` used in all templates?

Initially the controls were not as strong, so many templates were put in until issues like the previous became an issue.

## Does the project support requests for additional templates or additional data in an existing template?

We are no longer considering additional template requests at this time. The project has existed for over 7 years (initially within ntc-ansible) and over 200 template at this point any additional requests are essentially edge use cases. Meaning, for seven years of usage, no one else has asked for this feature. There is a limited maintainers who primarily use their free time to maintain the project.

## Are you open to adding maintainers to the project?

Yes, we would consider giving a proven member of the project and community maintainer rights. Please inquiry emailing info@networktocode.com.

## I simply want to add my template to the project, I do not want to add all of these tests and controls, can I just do so?

Short answer no, from an outsiders point of view the contributor requirements may seem overly complex, however features added by engineers rarely come back to support them. The burden of support is on the maintainers and a certain level of quality assurance is required for that to happen. That includes updating the index file appropriately and adding proper raw and expected value files.

## Why don't you grab all of the data in the template?

There is no intention for ntc-templates to become feature complete, some of the data is less interesting, or can be better understood from other commands. This is actually an area where the project chose to be loose, as we do not want to over-burden the contributor. If you feel that the additional data should be added, you are welcome to add the feature, but it would not be considered a bug, and thus not supported by the maintainers of the this project.

## Why does the index order matter?

The "greediness" of the template match ensures that there longest matches first. For example, if `show ip ospf` was above `show ip ospf database`, the `show ip ospf` template would be used in both cases. The additional steps are because of general programmatic hygiene.

## Will you accept my template if I create it?

In most cases, yes. However, there are a few edge cases. For example if requesting to add a `show cdp neighbors` when there is already a `show cdp neighbors details` template created. That is additional complexity added to the project with little value.

## Why was my issue closed?

The most likely reasons are:

- Did not follow the Issue creation template.
- Did not provide the data required to act upon the request.
- Did not provide the error that was created.
- Was actually a feature request that is not supported.
- A prolonged time with no response.  

## What is meant that this is a parsing project, not a data modeling project?

The project intends to parse, meaning post processing is assumed in order to normalize the data. This project does not intend to solve that problem set. This is often noted in keys being different between the same command on multiple OS's. This was not intentional as at first there was not strict enforcement. That being said, there is no intention to retrofit this use case for the above stated reasons. This use case is best handled in post processing.

## I have never submitted a Pull Request before, how do I do so?

This is outside the scope of this project, but this [video](https://www.youtube.com/watch?v=rgbCcBNZcdQ) should provide the instructions on how to do so.

## Does this work on windows?

Based on this [PR](https://github.com/networktocode/ntc-templates/pull/672) it should, however this is not a supported option. We are willing to take in qualified Pull Requests to have the feature, but have no intention of actively supporting.

## Can you provide general guidance?

This is best handled via real time communication. Feel free to join our slack community (sign up information above) and reach out on the #networktocode channel. Please be aware of timezones, downtimes, and help is performed based on goodwill and timing, and not guaranteed.

## Cannot import name clitable from textfsm - Known Issue

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
