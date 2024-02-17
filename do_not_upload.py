#!/usr/bin/env python3

import textfsm
import pprint

command = "show_interface"
template_file = f'ntc_templates/templates/allied_telesis_awplus_{command}.textfsm'
raw_output_file = f'tests/allied_telesis_awplus/{command}/allied_telesis_awplus_{command}1.raw'

with open(template_file) as fd_t, open(raw_output_file) as fd_o:
    re_table = textfsm.TextFSM(fd_t)
    parsed_header = re_table.header
    parsed_output = re_table.ParseText(fd_o.read())

pprint.pprint(parsed_header)
pprint.pprint(parsed_output)

