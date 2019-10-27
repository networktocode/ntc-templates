"""Ensure that testcases exist for all templates."""
import os
import glob
import re

from tests import load_index_data


KNOWN_MISSING_TESTS = {
    'cisco_ios_show_vlan',
    'cisco_nxos_show_interface_brief',
    'cisco_nxos_show_ip_ospf_neighbor_vrf',
    'cisco_xr_show_controllers',
}


def test_verify_parsed_and_reference_data_exists():
    """Verify that at least one test exists for all entries in the index file.

    TODO:
        Add test cases for ``KNOWN_MISSING_TESTS`` and remove related conditional.
        Remove "_ssh" from ``cisco_wlc_ssh`` and rely on vendor_platform_command syntax
            instead of using regex on the directories.
    """
    index = sorted(load_index_data())
    for row in index:
        template = row[0].strip()
        template_short = template.split('.template')[0]
        platform = row[2].strip()
        for directory in os.listdir("tests"):
            if re.match(platform, directory):
                platform_directory = directory
                break
        cut = len(platform_directory) + 1
        command = template_short[cut:]
        if template_short not in KNOWN_MISSING_TESTS:
            cases = 'tests/%s/%s/*.raw' % (platform_directory, command)
            test_list = glob.glob(cases)
            assert len(test_list) != 0, 'Could not find tests for %s' % template
