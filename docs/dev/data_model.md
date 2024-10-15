# Goals

- The table below becomes an evolving reference of common capture group names
- Normalize common capture groups across templates (including cross-vendor)

# Reasoning

Normalized capture group names enable more predictable structured data across templates where similar data exists.

Example: Imagine the extra programming logic needed to consume structured data when capture groups could have two or more names across several templates or several vendors! Yikes! This is why we seek to normalize.

# Considerations

- Some capture groups are a single value and others are lists of values despite containing similar data as one another
    - Example: single IP address vs list of IP addresses
- Normalizing and using standard capture group names will take time, persistence, and patience from the community
- Other than new templates, these normalization changes modify the expected template output and are considered "breaking changes" to be included in version releases

# Common Capture Groups

| Capture Group                    | Usage Description |
|----------------------------------|:------------------|
| `BIA`                            | use this if the template already has MAC_ADDRESS in use for the active MAC address |
| `BUNDLE_NAME`                    | virtual interface name for etherchannel, LACP, LAG, or port-channel interfaces |
| `BUNDLE_PROTOCOL`                | virtual interface protocol type (LACP, PAgP) for etherchannel or port-channel interfaces |
| `BUNDLE_PROTOCOL_STATE`          | virtual interface protocol state for etherchannel or port-channel interfaces |
| `BUNDLE_STATUS`                  | virtual interface status for etherchannel, LACP, LAG, or port-channel interfaces |
| `CAPABILITIES`                   | often represents active/operational neighbor capabilities shared via CDP or LLDP |
| `CAPABILITIES_SUPPORTED`         | often represents supported neighbor capabilities shared via CDP or LLDP |
| `CHASSIS_ID`                     | often represents CDP or LLDP neighbor chassis ID |
| `DESCRIPTION`                    | often used for port or interface descriptions |
| `GATEWAY`                        | gateway address for a subnet |
| `INTERFACE`                      | full word instead of IFACE, INTF, INTFC, etc |
| `IP_ADDRESS`                     | for a single IP address, often IPv4 |
| `IP_ADDRESSES`                   | for lists of IPv4 addresses, but in the case of some templates there may be a mix of IP protocol versions |
| `IP_HELPER`                      | for lists DHCP IP helper addresses |
| `IP_VERSION`                     | Internet Protocol (IP) version in the case of multiple versions appearing in output (use where necessary) |
| `IPV6_ADDRESS`                   | for a single IPv6 address |
| `IPV6_ADDRESSES`                 | for lists of IPv6 addresses |
| `IPV6_GATEWAY`                   | for IPv6 gateway address |
| `LOCAL_INTERFACE`                | often represents local interface or port for CDP or LLDP |
| `LOCAL_IP_ADDRESS`               | local IP address in the case of First Hop Redundancy Protocols (FHRP) |
| `MAC_ADDRESS`                    | instead of MAC or MACADDR |
| `MEMBER_INTERFACE`               | list of physical member interface names that are bundled to make an etherchannel, LACP, LAG, or port-channel interface |
| `MEMBER_INTERFACE_STATUS`        | list of member interface statuses for an etherchannel, LACP, LAG, or port-channel interface |
| `MGMT_ADDRESS`                   | management address, used when data could be an ***Ethernet MAC address or an IP address*** (ex: CDP or LLDP templates) |
| `MGMT_IP_ADDRESS`                | instead of MGMT_IP or MGMT_ADDRESS or MANAGEMENT_IP or REMOTE_MANAGEMENT_ADDRESS |
| `NEIGHBOR_DESCRIPTION`           | often represents CDP or LLDP neighbor or system name description |
| `NEIGHBOR_ID`                    | for router IDs remote to the system being parsed |
| `NEIGHBOR_INTERFACE`             | often represents neighbor or remote interface or port for CDP or LLDP |
| `NEIGHBOR_INTERFACE_DESCRIPTION` | represents CDP or LLDP neighbor (remote host) interface or port descriptions (Note: see NEIGHBOR_INTERFACE) |
| `NEIGHBOR_NAME`                  | often represents neighbor name for CDP or LLDP |
| `NETMASK`                        | for IPv4 dotted quad masks |
| `NETWORK`                        | for network numbers or subnet address (without the mask or prefix/slash notation); in place of ROUTE |
| `PID`                            | represents Part IDs (PIDs), Stock Keeping Units (SKUs), and in some cases Models or Model Numbers
| `PLATFORM`                       | often represents CDP or LLDP neighbor's platform or model name/number |
| `PREFIX_LENGTH`                  | instead of PREFIX or CIDR for the numbers of a slash notation or CIDR mask |
| `PROTOCOL`                       | instead of PROTO |
| `ROUTER_ID`                      | for local router IDs (local to the device being parsed) |
| `VLAN_ID`                        | instead of VLAN or TAG |
| `VLAN_NAME`                      | VLAN name or description |
