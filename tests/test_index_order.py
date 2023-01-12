"""Tests to check the order of the index file."""
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
    "dlink_ds",
    "enterasys",
    "ericsson_ipos",
    "extreme",
    "f5_ltm",
    "fortinet",
    "hp_comware",
    "hp_procurve",
    "huawei_vrp",
    "ipinfusion_ocnos",
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


def check_order(  # pylint: disable=too-many-arguments,too-many-arguments,too-many-return-statements
    current_os, prior_os, cmd_len, prior_len, os_choices, used_os, cmd, prior_cmd
):
    """Enforcing the complex logic to ensure that the index file is ordered correctly."""
    add_os_check = []

    if current_os not in used_os and used_os is not None:
        add_os_check.extend(used_os)
        add_os_check.append(current_os)

    if used_os != sorted(used_os):
        msg = f"OS's are not in alpabetical order, current order: '{used_os}'"
        return False, msg
    if add_os_check != sorted(add_os_check):
        msg = f"OS's are not in alpabetical order, current order: '{add_os_check}'"
        return False, msg

    if current_os not in os_choices:
        msg = f"'{current_os}' is not one of the valid options '{used_os}'"
        return False, msg

    if not prior_os and prior_len == 0:
        # Starting Point
        return True, ""
    if current_os == prior_os and cmd_len == prior_len and cmd == min(prior_cmd, cmd):
        msg = f"OS is the same and command same length, please set {cmd} before {prior_cmd} to be in alphabetical order"
        return False, msg
    if current_os == prior_os and cmd_len <= prior_len:
        # OS is the same as previous, and cmd_len is smaller or equal to prior so good
        return True, ""
    if current_os != prior_os and current_os not in used_os:
        # prior OS has changed, do not need to check for length yet
        return True, ""
    if current_os == prior_os and cmd_len > prior_len:
        msg = f"Current Command len '{cmd_len}' larger then previous '{prior_len}', for command '{cmd}'"
        return False, msg
    if current_os != prior_os and current_os in used_os:
        msg = f"'{current_os}' OS was already used in list on command '{cmd}'"
        return False, msg
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
        current_os = os_match.group(0)
        cmd = "_".join(template.split("_")[2:])
        cmd_len = len(cmd)
        check_val, check_msg = check_order(
            current_os, prior_os, cmd_len, prior_len, OS_CHOICES, used_os, cmd, prior_cmd
        )
        if not check_val:
            # assertFalse(check_val, msg=check_msg)
            print(f"Error on line: {row}")
            print(f"Error Message: {check_msg}")
        assert check_val
        if current_os not in used_os:
            used_os.append(current_os)
        prior_len = cmd_len
        prior_cmd = cmd
        prior_os = current_os
