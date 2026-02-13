# Release Notes v9.0.0

## Major Release Highlights

This major release introduces several **breaking changes**, updates Python version support, and adds many new templates and improvements.

## Breaking Changes Summary

The following templates have breaking changes in this release. If you use any of these templates, review the details below and the [Migration Guide](#migration-guide) before upgrading.

| Template | Change Type | Details |
|----------|------------|---------|
| `cisco_ios_show_sdwan_bfd_sessions_table` | Field renamed | `proto` → `protocol` |
| `cisco_ios_show_interfaces_switchport` | Output format changed | `trunking_vlans` now returns individual entries instead of comma-separated strings |
| `aruba_aoscx_show_interface` | New field added | `secondary_ip_address` (list) |
| `fortinet_fnsysctl_ifconfig` | New fields added | `ipv6_address`, `prefix_length` |
| `fortinet_get_system_status` | New field added | `first_ga_patch_build_date` |
| `cisco_ios_show_redundancy` | New fields added | `fast_switchover`, `initial_garp` |
| `mikrotik_routeros_ip_dhcp-server_lease_print_terse_without-paging` | New field added | `class_id` |
| `aruba_aoscx_show_system` | Parsing behavior changed | `vendor` now captures multi-word names |
| `hp_comware_display_interface` | Parsing behavior changed | `untagged_vlan_id` now correctly populates |
| `arista_eos_show_interfaces_transceiver_detail` | Index pattern changed | Minimum abbreviation `tr` → `tra` |

## Breaking Changes

### Python Version Support

* **Dropped Python 3.9 support** - Minimum Python version is now 3.10+
* **Added Python 3.13 support** - Now supports Python 3.10, 3.11, 3.12, and 3.13

### Field Name Changes (Breaking)

* **Cisco IOS SD-WAN BFD Sessions Table**: Renamed `proto` to `protocol` for field name normalization in [#2275](https://github.com/networktocode/ntc-templates/pull/2275)

### Output Format Changes (Breaking)

* **Cisco IOS show interfaces switchport**: `trunking_vlans` list items are now split into individual entries instead of comma-separated strings in [#2271](https://github.com/networktocode/ntc-templates/pull/2271)
  - Old: `["1,12,15,31-36,40-42", "900,910,920"]`
  - New: `["1", "12", "15", "31-36", "40-42", "900", "910", "920"]`

### New Fields Added to Existing Templates (Schema Changes)

* **Aruba AOS-CX show interface**: New `secondary_ip_address` list field added in [#2274](https://github.com/networktocode/ntc-templates/pull/2274)
* **Fortinet fnsysctl ifconfig**: New `ipv6_address` and `prefix_length` fields added in [#2255](https://github.com/networktocode/ntc-templates/pull/2255)
* **Fortinet get system status**: New `first_ga_patch_build_date` field added in [#2250](https://github.com/networktocode/ntc-templates/pull/2250)
* **Cisco IOS show redundancy**: New `fast_switchover` and `initial_garp` fields added in [#2193](https://github.com/networktocode/ntc-templates/pull/2193)
* **Mikrotik DHCP server lease**: New `class_id` field added in [#2234](https://github.com/networktocode/ntc-templates/pull/2234)

### Parsing Behavior Changes

* **Aruba AOS-CX show system**: `vendor` field now captures multi-word vendor names (e.g., `"HPE"` becomes `"HPE ANW"`) in [#2237](https://github.com/networktocode/ntc-templates/pull/2237)
* **HP Comware display interface**: `untagged_vlan_id` field now correctly captures VLAN IDs that were previously returned as empty strings in [#2197](https://github.com/networktocode/ntc-templates/pull/2197)
* **Arista EOS show interfaces transceiver detail**: Index pattern minimum abbreviation for `transceiver` changed from `tr` to `tra` in [#2230](https://github.com/networktocode/ntc-templates/pull/2230)

## What's Changed

### New Templates

* Add Cisco IOS show running-config interface in [#2246](https://github.com/networktocode/ntc-templates/pull/2246)
* Add Cisco IOS show interfaces status err-disabled in [#2261](https://github.com/networktocode/ntc-templates/pull/2261)
* Add Cisco IOS show sdwan bfd summary in [#2216](https://github.com/networktocode/ntc-templates/pull/2216)
* Add Cisco IOS show sdwan bfd sessions table in [#2217](https://github.com/networktocode/ntc-templates/pull/2217)
* Add Cisco IOS show sdwan control connection in [#2215](https://github.com/networktocode/ntc-templates/pull/2215)
* Add Cisco IOS show sdwan omp peers in [#2214](https://github.com/networktocode/ntc-templates/pull/2214)
* Add Cisco IOS show sdwan tunnel statistics table in [#2213](https://github.com/networktocode/ntc-templates/pull/2213)
* Add Cisco IOS show endpoint-tracker in [#2219](https://github.com/networktocode/ntc-templates/pull/2219)
* Add Cisco IOS show endpoint-tracker tracker-group in [#2218](https://github.com/networktocode/ntc-templates/pull/2218)
* Add Cisco NX-OS show interface breakout in [#2272](https://github.com/networktocode/ntc-templates/pull/2272)
* Add Cisco NX-OS show interface status err-disabled in [#2262](https://github.com/networktocode/ntc-templates/pull/2262)
* Add Cisco NX-OS show interface capabilities in [#2211](https://github.com/networktocode/ntc-templates/pull/2211)
* Add Cisco XR show eigrp neighbors in [#2183](https://github.com/networktocode/ntc-templates/pull/2183)
* Add Cisco Viptela show omp peers in [#2202](https://github.com/networktocode/ntc-templates/pull/2202)
* Add Cisco Viptela show control connections in [#2203](https://github.com/networktocode/ntc-templates/pull/2203)
* Add Juniper JunOS show ethernet-switching interfaces in [#2263](https://github.com/networktocode/ntc-templates/pull/2263)
* Add Arista EOS show interfaces transceiver hardware in [#2230](https://github.com/networktocode/ntc-templates/pull/2230)
* Add Aruba OS show inventory in [#2188](https://github.com/networktocode/ntc-templates/pull/2188)
* Add HP Comware display link-aggregation member-port in [#2210](https://github.com/networktocode/ntc-templates/pull/2210)
* Add Linux bluetoothctl show in [#2212](https://github.com/networktocode/ntc-templates/pull/2212)
* Add Mikrotik ip firewall connection print terse without-paging in [#2232](https://github.com/networktocode/ntc-templates/pull/2232)
* Add Mikrotik ip dns cache print terse without-paging in [#2233](https://github.com/networktocode/ntc-templates/pull/2233)
* Add Mikrotik interface wireguard print terse without-paging in [#2256](https://github.com/networktocode/ntc-templates/pull/2256)
* Add Mikrotik interface wireguard peers print terse without-paging in [#2257](https://github.com/networktocode/ntc-templates/pull/2257)
* Add Palo Alto PAN-OS show routing route in [#2201](https://github.com/networktocode/ntc-templates/pull/2201)
* Add Palo Alto PAN-OS show routing resource in [#2199](https://github.com/networktocode/ntc-templates/pull/2199)
* Add Palo Alto PAN-OS show routing protocol bgp summary in [#2200](https://github.com/networktocode/ntc-templates/pull/2200)
* Add Palo Alto PAN-OS show high-availability path-monitoring in [#2198](https://github.com/networktocode/ntc-templates/pull/2198)

### Enhanced Templates

* Support secondary IP addresses on Aruba AOS-CX show interface in [#2274](https://github.com/networktocode/ntc-templates/pull/2274)
* Capture multi-word vendor names in Aruba AOS-CX show system in [#2237](https://github.com/networktocode/ntc-templates/pull/2237)
* Support dotted-decimal area ID in Cisco IOS show ip ospf interface brief in [#2254](https://github.com/networktocode/ntc-templates/pull/2254)
* Support ipv4 command variant in Cisco XR show ip interface brief in [#2239](https://github.com/networktocode/ntc-templates/pull/2239)
* Add addr6 support to Fortinet fnsysctl ifconfig in [#2255](https://github.com/networktocode/ntc-templates/pull/2255)
* Update Fortinet get system status for v7.4.8 in [#2250](https://github.com/networktocode/ntc-templates/pull/2250)
* Update Cisco NX-OS show module for N9K linecard statuses in [#2264](https://github.com/networktocode/ntc-templates/pull/2264)
* Modify HP Comware display interface for Comware5/7 variations in [#2197](https://github.com/networktocode/ntc-templates/pull/2197)
* Modify HP Comware display ip interface for DHCP assigned IP in [#2207](https://github.com/networktocode/ntc-templates/pull/2207)
* Modify HP Comware display device manuinfo for Comware5/7 in [#2196](https://github.com/networktocode/ntc-templates/pull/2196)
* Update HP Comware display vlan all for Comware5 variations in [#2209](https://github.com/networktocode/ntc-templates/pull/2209)
* Improve Mikrotik ip dhcp-server lease print terse without-paging in [#2234](https://github.com/networktocode/ntc-templates/pull/2234)
* Add new fields to Cisco IOS show redundancy for stackwise in [#2193](https://github.com/networktocode/ntc-templates/pull/2193)

### Bug Fixes

* Fix Cisco IOS show sdwan bfd sessions table header parsing in [#2275](https://github.com/networktocode/ntc-templates/pull/2275)
* Fix Cisco IOS show env power parser in [#2270](https://github.com/networktocode/ntc-templates/pull/2270)
* Fix Cisco IOS traceroute for no VRF info in [#2205](https://github.com/networktocode/ntc-templates/pull/2205)
* Fix Cisco IOS show redundancy for 93xx stackwise in [#2193](https://github.com/networktocode/ntc-templates/pull/2193)
* Fix Cisco NX-OS tunnel support in show interface in [#2267](https://github.com/networktocode/ntc-templates/pull/2267)
* Fix Cisco NX-OS VXLAN nve interfaces in show interface in [#2195](https://github.com/networktocode/ntc-templates/pull/2195)
* Fix Cisco NX-OS interface by matching old FC stats in [#2192](https://github.com/networktocode/ntc-templates/pull/2192)
* Fix Cisco NX-OS show interface for no lead whitespace on uni/multicast pkts in [#2236](https://github.com/networktocode/ntc-templates/pull/2236)
* Fix Cisco ASA show interface output nuances for FPR in [#2224](https://github.com/networktocode/ntc-templates/pull/2224)
* Fix Cisco ASA show interface ip brief for FPR admin down in [#2223](https://github.com/networktocode/ntc-templates/pull/2223)
* Fix Cisco ASA show bgp summary BGP multipath in [#2222](https://github.com/networktocode/ntc-templates/pull/2222)
* Fix Aruba AOS-CX show interface sync devices from network in [#2269](https://github.com/networktocode/ntc-templates/pull/2269)
* Fix Aruba AOS-CX show system vendor line in [#2227](https://github.com/networktocode/ntc-templates/pull/2227)
* Fix Arista EOS show interfaces for VXLAN and no IP addr in [#2235](https://github.com/networktocode/ntc-templates/pull/2235)
* Fix Huawei VRP display lldp neighbor device lines in [#2226](https://github.com/networktocode/ntc-templates/pull/2226)
* Fix Cisco IOS show redundancy for different active/standby location name in [#2225](https://github.com/networktocode/ntc-templates/pull/2225)

## Migration Guide

### Python Version

Ensure you are running Python 3.10 or higher before upgrading. Python 3.9 is no longer supported.

### Field Name Changes

If you are using the following template, update your code to use the new field name:

**Cisco IOS show sdwan bfd sessions table:**
- `proto` -> `protocol`

```python
# Before (v8.x)
result["proto"]

# After (v9.0)
result["protocol"]
```

### Output Format Changes

**Cisco IOS show interfaces switchport - `trunking_vlans`:**

The `trunking_vlans` field now returns individual VLAN/range entries instead of comma-separated strings per line. Update any code that splits on commas:

```python
# Before (v8.x) - each line was a single comma-separated string
# trunking_vlans: ["1,12,15,31-36,40-42,80,85", "900,910,920,930"]
for line in result["trunking_vlans"]:
    vlans = line.split(",")

# After (v9.0) - each VLAN/range is its own list entry
# trunking_vlans: ["1", "12", "15", "31-36", "40-42", "80", "85", "900", "910", "920", "930"]
vlans = result["trunking_vlans"]  # already split
```

### New Fields in Existing Templates

The following templates now include additional fields in their output. If your code does strict schema validation or exact dictionary comparison, update accordingly:

| Template | New Field(s) |
|----------|-------------|
| `aruba_aoscx_show_interface` | `secondary_ip_address` (list) |
| `fortinet_fnsysctl_ifconfig` | `ipv6_address`, `prefix_length` |
| `fortinet_get_system_status` | `first_ga_patch_build_date` |
| `cisco_ios_show_redundancy` | `fast_switchover`, `initial_garp` |
| `mikrotik_routeros_ip_dhcp-server_lease_print_terse_without-paging` | `class_id` |

### Parsing Behavior Changes

**Aruba AOS-CX show system:**
The `vendor` field now captures multi-word vendor names. If you relied on single-word vendor values, update your logic:
- Old: `"HPE"`
- New: `"HPE ANW"`

**HP Comware display interface:**
The `untagged_vlan_id` field now correctly populates where it previously returned empty strings. Code that checked for empty `untagged_vlan_id` may need adjustment.

**Arista EOS show interfaces transceiver detail:**
The minimum command abbreviation for matching this template changed. If you use `show int tr detail` (2-letter abbreviation for transceiver), use `show int tra detail` instead (minimum 3 letters).

## Statistics

- **Total Changes**: 67 commits
- **New Templates**: 28
- **Enhanced Templates**: 13
- **Bug Fixes**: 16

**Full Changelog**: [v8.1.0...v9.0.0](https://github.com/networktocode/ntc-templates/compare/v8.1.0...v9.0.0)
