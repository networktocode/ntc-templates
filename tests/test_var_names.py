"""Verify that Template capture groups comply with naming standards."""

import os
import re

import pytest

from jarowinkler import jarowinkler_similarity


COMMON_CAPTURE_GROUP_NAMES = {
    # more common ABC order
    "ACTION",
    "ADVERTISING",
    "AUTO_NEGOTIATION",
    "BIA",
    "COMMENT",
    "CURRENT_FIRMWARE",
    "DESCRIPTION",
    "DESTINATION_PORT",
    "DISTANCE",
    "FIRMWARE_TYPE",
    "ID",
    "INDEX",
    "IP_ADDRESS",
    "IP_VERSION",
    "IPV4_ADDRESS",
    "IPV6_ADDRESS",
    "INTERFACE",
    "LOCAL_ASN",
    "FLAGS",
    "FULL_DUPLEX",
    "GATEWAY",
    "HARDWARE_MODEL",
    "HOSTNAME",
    "LOCAL_ADDRESS",
    "MAC_ADDRESS",
    "NAME",
    "NEIGHBOR_ID",
    "NETMASK",
    "NETWORK",
    "PEER_GROUP",
    "PREFIX_LENGTH",
    "PROTOCOL",
    "RATE",
    "RATE_LIMIT",
    "REMOTE_ASN",
    "REVISION",
    "SCOPE",
    "SERIAL_NUMBER",
    "SERVER",
    "STATUS",
    "SOURCE_PORT",
    "TYPE",
    "VLAN_ID",
    "VLAN_NAME",
    # less common ABC order
    "ADDRESSES",
    "BOARD_NAME",
    "CE_VLAN",
    "CHAIN",
    "CONNECTION_NAT_STATE",
    "CONNECTION_STATE",
    "DST_ADDRESS",
    "DST_ADDRESS_LIST",
    "DST_MAC_ADDRESS",
    "DST_PORT",
    "FACTORY_FIRMWARE",
    "GATEWAY_STATUS",
    "HW_OFFLOAD",
    "IMMEDIATE_GW",
    "IN_INTERFACE",
    "IN_INTERFACE_LIST",
    "IP_ALIAS_ACTIVE",
    "IP_ALIAS_ADDRESS",
    "IP_ALIAS_NETMASK",
    "IP_STATE",
    "IPSEC_POLICY",
    "LAST_SEEN",
    "LINK_PARTNER_ADVERTISING",
    "LOG",
    "LOG_PREFIX",
    "MASTER_IP_ADDRESS",
    "OPERATOR_DESTINATION_PORT",
    "OPERATOR_SOURCE_PORT",
    "OUT_INTERFACE",
    "OUT_INTERFACE_LIST",
    "PREF_SRC",
    "PUBLAN_IP_ADDRESS",
    "READ_ACCESS",
    "ROUTERBOARD",
    "ROUTING_TABLE",
    "RX_FLOW_CONTROL",
    "SECURITY",
    "SRC_ADDRESS",
    "SRC_ADDRESS_LIST",
    "SRC_MAC_ADDRESS",
    "SRC_PORT",
    "SUPPRESS_HW_OFFLOAD",
    "TARGET_SCOPE",
    "TO_ADDRESSES",
    "TO_PORTS",
    "TX_FLOW_CONTROL",
    "UPGRADE_FIRMWARE",
    "VIRTUAL_IP_ADDRESS",
    "VIRTUAL_MAC_ADDRESS",
    "VLAN_ACTIVE",
    "VLAN_IVL_SVL",
    "VLAN_MGMT",
    "VLAN_PID",
    "VLAN_PORT_MEMBERS",
    "VLAN_PROTOCOL",
    "VLAN_TYPE",
    "WRITE_ACCESS",
}


changed_filenames = os.getenv("ALL_CHANGED_FILES")
if changed_filenames:
    changed_files = changed_filenames.split()
else:
    changed_files = []


changed_templates = [filename for filename in changed_files if filename.endswith(".textfsm")]


@pytest.mark.parametrize("filename", changed_templates)
def test_capture_group_names(filename: str):
    with open(filename, encoding="utf-8") as fh:
        capture_group_names = re.findall(
            r"^Value\s+(?:(?:Filldown|Key|Required|List|Fillup)\s+)?(\S+)",
            fh.read(),
            re.MULTILINE,
        )
    error_message = "The following capture group names should be updated to follow standard naming convention:"
    has_invalid_capture_group_names = False
    for capture_group_name in capture_group_names:
        if capture_group_name not in COMMON_CAPTURE_GROUP_NAMES:
            for common_capture_group_name in COMMON_CAPTURE_GROUP_NAMES:
                if (
                    # used name is shortened form of standard name
                    capture_group_name in common_capture_group_name
                    # used name is an elongated form of standard name
                    or common_capture_group_name in capture_group_name
                    # used name is very similar to standard name (may be false positive)
                    or jarowinkler_similarity(capture_group_name, common_capture_group_name) >= 0.8
                ):
                    error_message += f"\n  * {capture_group_name} should be {common_capture_group_name}"
                    has_invalid_capture_group_names = True
                    break
    assert not has_invalid_capture_group_names, error_message
