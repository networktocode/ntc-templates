#!/usr/bin/env python

import pytest
import csv
import os
import glob
import csv



def load_indexdata():
    """Load data from index file."""
    index_data = []
    with open('./templates/index') as indexfs:
        data = csv.reader(indexfs)
        for row in data:
            if len(row) > 2 and row[0] != 'Template':
                index_data.append(row)
    return index_data

def check_order(current_os, prior_os,cmd_len, prior_len, os_choices, used_os, cmd, prior_cmd):
    add_os_check = []

    if current_os not in used_os and used_os is not None:
        add_os_check.extend(used_os)
        add_os_check.append(current_os)

    if used_os != sorted(used_os):
        msg = "OS's are not in alpabetical order, current order: '{}'".format(used_os)
        return False , msg
    elif add_os_check != sorted(add_os_check):
        msg = "OS's are not in alpabetical order, current order: '{}'".format(add_os_check)
        return False , msg

    if current_os not in os_choices:
        msg = "'{}' is not one of the valid options '{}'".format(current_os, used_os)
        return False, msg

    if not prior_os and prior_len == 0:
        # Starting Point 
        return True , ''
    elif current_os == prior_os and cmd_len == prior_len and cmd == min(prior_cmd, cmd):
        msg = "OS is the same and command same length, please set {} before {} to be in alphabetical order".format(cmd, prior_cmd)
        return False, msg
    elif current_os == prior_os and cmd_len <= prior_len:
        # OS is the same as previous, and cmd_len is smaller or equal to prior so good
        return True , ''
    elif current_os != prior_os and current_os not in used_os:
        # prior OS has changed, do not need to check for length yet
        return True , ''
    elif current_os == prior_os and cmd_len > prior_len:
        msg = "Current Command len '{}' larger then previous '{}', for command '{}'".format(cmd_len, prior_len, cmd )
        return False , msg
    elif current_os != prior_os and current_os in used_os:
        msg = "'{}' OS was already used in list on command '{}'".format(current_os, cmd)
        return False , msg
    else:
        msg = "Failed for unknown reason"
        return False , msg

def test_index_ordering():

    os_choices = [
        'a10', 'alcatel_sros', 'arista_eos', 'aruba_os', 'avaya_ers', 'avaya_vsp',
        'brocade_fastiron', 'brocade_netiron', 'brocade_nos', 'brocade_vdx', 'brocade_vyos',
        'cisco_asa', 'cisco_ios', 'cisco_nxos', 'cisco_s300', 'cisco_wlc', 'cisco_xe', 'cisco_xr',
        'dell_force10', 'enterasys', 'extreme', 'f5_ltm', 'fortinet', 'hp_comware', 'hp_procurve',
        'huawei', 'juniper', 'juniper_junos', 'linux', 'ovs_linux', 'paloalto_panos',
        'quanta_mesh', 'vmware_nsxv', 'vyatta_vyos', 'vyos'
        ] 

    prior_os = ""
    prior_len = 0
    prior_cmd = ""
    used_os = []

    index = load_indexdata()
    for row in index:
        template = row[0].strip()
        os = '_'.join(template.split('_')[:2])
        cmd = '_'.join(template.split('_')[2:])
        cmd_len = len(cmd)
        check_val, check_msg = check_order(os, prior_os, cmd_len, prior_len, os_choices, used_os, cmd, prior_cmd)
        if not check_val:
        #assertFalse(check_val, msg=check_msg)
            print "Error on line: {}".format(row)
            print "Error Message: {}".format(check_msg)
        assert check_val != False
        if os not in used_os:
            used_os.append(os)
        prior_len = cmd_len
        prior_cmd = cmd
        prior_os = os

def main():
    test_index_ordering()

if __name__ == "__main__":
    main()
