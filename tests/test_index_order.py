#!/usr/bin/env python
import re

from tests import load_index_data


OS_CHOICES = [
    "a10",
    "alcatel_aos",
    "alcatel_sros",
    "arista_eos",
    "aruba_aoscx",
    "aruba_os",
    "avaya_ers",
    "avaya_vsp",
    "broadcom_icos",
    "brocade_fastiron",
    "brocade_netiron",
    "brocade_nos",
    "brocade_vdx",
    "brocade_vyos",
    "checkpoint_gaia",
    "ciena_saos",
    "cisco_apic",
    "cisco_asa",
    "cisco_ftd",
    "cisco_ios",
    "cisco_nxos",
    "cisco_s300",
    "cisco_wlc",
    "cisco_xe",
    "cisco_xr",
    "dell_force10",
    "dell_powerconnect",
    "enterasys",
    "extreme",
    "f5_ltm",
    "fortinet",
    "hp_comware",
    "hp_procurve",
    "huawei_vrp",
    "juniper",
    "juniper_junos",
    "juniper_screenos",
    "linux",
    "mikrotik_routeros",
    "ovs_linux",
    "paloalto_panos",
    "quanta_mesh",
    "ruckus_fastiron",
    "ubiquiti_edgerouter",
    "ubiquiti_edgeswitch",
    "vmware_nsxv",
    "vyatta_vyos",
    "vyos",
    "watchguard_firebox",
    "yamaha",
    "zyxel_os",
]
CHOICES_STRING = "|".join(OS_CHOICES)
RE_TEMPLATE_OS = re.compile(rf"^({CHOICES_STRING})")


def check_order(
    current_os, prior_os, cmd_len, prior_len, os_choices, used_os, cmd, prior_cmd
):
    add_os_check = []

    if current_os not in used_os and used_os is not None:
        add_os_check.extend(used_os)
        add_os_check.append(current_os)

    if used_os != sorted(used_os):
        msg = "OS's are not in alpabetical order, current order: '{0}'".format(used_os)
        return False, msg
    elif add_os_check != sorted(add_os_check):
        msg = "OS's are not in alpabetical order, current order: '{0}'".format(
            add_os_check
        )
        return False, msg

    if current_os not in os_choices:
        msg = "'{0}' is not one of the valid options '{1}'".format(current_os, used_os)
        return False, msg

    if not prior_os and prior_len == 0:
        # Starting Point
        return True, ""
    elif current_os == prior_os and cmd_len == prior_len and cmd == min(prior_cmd, cmd):
        msg = (
            "OS is the same and command same length, "
            "please set {0} before {1} to be in alphabetical order".format(cmd, prior_cmd)
        )
        return False, msg
    elif current_os == prior_os and cmd_len <= prior_len:
        # OS is the same as previous, and cmd_len is smaller or equal to prior so good
        return True, ""
    elif current_os != prior_os and current_os not in used_os:
        # prior OS has changed, do not need to check for length yet
        return True, ""
    elif current_os == prior_os and cmd_len > prior_len:
        msg = "Current Command len '{0}' larger then previous '{1}', for command '{2}'".format(
            cmd_len, prior_len, cmd
        )
        return False, msg
    elif current_os != prior_os and current_os in used_os:
        msg = "'{0}' OS was already used in list on command '{1}'".format(current_os, cmd)
        return False, msg
    else:
        msg = "Failed for unknown reason"
        return False, msg


def test_index_ordering():
    prior_os = ""
    prior_len = 0
    prior_cmd = ""
    used_os = []

    index = load_index_data()
    for row in index:
        template = row[0].strip()
        os_match = RE_TEMPLATE_OS.match(template)
        os = os_match.group(0)
        cmd = "_".join(template.split("_")[2:])
        cmd_len = len(cmd)
        check_val, check_msg = check_order(
            os, prior_os, cmd_len, prior_len, OS_CHOICES, used_os, cmd, prior_cmd
        )
        if not check_val:
            # assertFalse(check_val, msg=check_msg)
            print("Error on line: {0}".format(row))
            print("Error Message: {0}".format(check_msg))
        assert check_val
        if os not in used_os:
            used_os.append(os)
        prior_len = cmd_len
        prior_cmd = cmd
        prior_os = os
