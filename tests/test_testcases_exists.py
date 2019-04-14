"""Ensure that testcases exist for all templates."""
import glob

from tests import load_index_data

KNOWN_MISSING_TESTS = [
    'cisco_ios_show_vlan',
    'cisco_nxos_show_interface_brief',
    'cisco_nxos_show_ip_ospf_neighbor_vrf',
    'cisco_xr_show_controllers',
    '.*vyos.*_os_show_interfaces',
    '.*vyos.*_os_show_arp',
]


def test_verify_parsed_and_reference_data_exists():
    """Verify that at least one test exists for all entries in the index file."""
    index = sorted(load_index_data())
    coverage = {}
    for row in index:
        template = row[0].strip()
        platform = row[2].strip()
        cut = len(platform) + 1
        command = template[cut:].split('.')[0]
        cases = 'tests/%s/%s/*.raw' % (platform, command)
        test_list = glob.glob(cases)
        coverage['%s_%s' % (platform, command)] = len(test_list)

    for test in coverage:
        if coverage[test] == 0 and test not in KNOWN_MISSING_TESTS:
            assert test == 'No test cases found'
