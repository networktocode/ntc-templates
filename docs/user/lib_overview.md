# Library Overview

[TextFSM](https://github.com/google/textfsm/wiki) is a project built by Google that takes CLI string output and passes each line through a series of regular expressions until it finds a match. The regular expressions use named capture groups to build a text table out of the significant text. The names of the capture groups are used as column headers, and the captured values are stored as rows in the table.

This project provides a large collection of TextFSM Templates (text parsers) for a variety of Networking Vendors. In addition to the templates, there is a function that will convert the CLI output into a CliTable object; the resulting text table is converted into a list of dictionaries mapping the column headers with each row in the table.

## Audience (User Personas) - Who should use this Library?

Network engineers with the need to parse through standard cli based operational configurations.

## Authors and Maintainers

- @itdependsnetworks
- @jmcgill298
- @jvanderaa
