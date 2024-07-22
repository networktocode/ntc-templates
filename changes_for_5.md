# Changes for 5.0 Release

## Core changes
Exception on parsing failure has been changed from generic `Exception` to custom `ParsingException`.

Issue: https://github.com/networktocode/ntc-templates/issues/369
Changed: https://github.com/networktocode/ntc-templates/pull/1682

Rename `extreme` platform to `extreme_exos`
https://github.com/networktocode/ntc-templates/pull/1576

## Template changes
Below are the NTC Template keys that are changing as part of 5.0. These may not line up exactly of what is changing from what to what, but the keys of what are old and what are new are calculated with set calculations.

| Template Name | Previous  | New       |
| ------------- |-----------|-----------|
| brocade_netiron_show_running-config_interface.textfsm | IPHELPERS | IP_HELPER |
| cisco_ios_show_ip_bgp_summary.textfsm | ADDR_FAMILY | ADDRESS_FAMILY |
| cisco_ios_show_ip_bgp_summary.textfsm | BGP_NEIGH | BGP_NEIGHBOR |
| cisco_ios_show_ip_bgp_summary.textfsm | NEIGH_AS | NEIGHBOR_AS |
| cisco_ios_show_ip_bgp_summary.textfsm | NEIGH_AS | NEIGHBOR_AS |
| cisco_ios_show_ip_bgp_summary.textfsm | STATE_PFXRCD | STATE_OR_PREFIXES_RECEIVED |
