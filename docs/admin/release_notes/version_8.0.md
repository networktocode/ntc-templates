# Release Notes v8.0.0

## 🎉 Major Release Highlights

This major release introduces several **breaking changes** and significant improvements to ensure better consistency and maintainability across all templates.

## ⚠️ Breaking Changes

### Python Version Support
* **Dropped Python 3.8 support** - Minimum Python version is now 3.9+ by @mjbear in https://github.com/networktocode/ntc-templates/pull/2154

### Field Name Standardization (Breaking Changes)
* **Arista EOS**: Renamed `interface_up_time` to `last_link_flapped` in show interfaces by @mjbear in https://github.com/networktocode/ntc-templates/pull/2126
* **Cisco NX-OS**: Multiple field renames in show interface for consistency by @Mikeg2881 in https://github.com/networktocode/ntc-templates/pull/2112:
  - Renamed error counters to standardized names
  - Renamed statistics fields for consistency
  - Updated packet counter field names
* **Normalized PVID with VLAN_ID** across multiple templates by @mjbear in https://github.com/networktocode/ntc-templates/pull/2019

### Template Improvements with Schema Changes
* **Huawei VRP**: Major updates to display vlan template with improved parsing by @evilmonkey19 in https://github.com/networktocode/ntc-templates/pull/2164

## 🚀 What's Changed

### New Templates
* Add Cisco IOS show vlan group by @jfaulkner-fmr in https://github.com/networktocode/ntc-templates/pull/2093
* Juniper JunOS show system configuration database usage by @jnicholson56 in https://github.com/networktocode/ntc-templates/pull/2087
* Add Huawei VRP dir by @brian-s-cao in https://github.com/networktocode/ntc-templates/pull/2133
* Add Huawei VRP virtual-cable-test by @evilmonkey19 in https://github.com/networktocode/ntc-templates/pull/2138
* Add Huawei VRP display license verbose by @brian-s-cao in https://github.com/networktocode/ntc-templates/pull/2127
* Add Huawei VRP display eth-trunk by @evilmonkey19 in https://github.com/networktocode/ntc-templates/pull/2139
* Add Huawei SmartAX display ont-srvprofile gpon all by @evilmonkey19 in https://github.com/networktocode/ntc-templates/pull/2134
* Add Linux iwconfig by @evilmonkey19 in https://github.com/networktocode/ntc-templates/pull/2122
* Add Mikrotik RouterOS ip hotspot ip-binding print terse without-paging by @evilmonkey19 in https://github.com/networktocode/ntc-templates/pull/2149

### Enhanced Templates
* Update Huawei VRP display lldp neighbor by @evilmonkey19 in https://github.com/networktocode/ntc-templates/pull/2104
* Modify Juniper JunOS show rsvp interface by @jnicholson56 in https://github.com/networktocode/ntc-templates/pull/2095
* Improve Huawei VRP display interface by @evilmonkey19 in https://github.com/networktocode/ntc-templates/pull/2137
* Improve Huawei VRP display interface brief by @evilmonkey19 in https://github.com/networktocode/ntc-templates/pull/2140
* Improve Alcatel AOS show lldp remote-system by @evilmonkey19 in https://github.com/networktocode/ntc-templates/pull/2064
* Support Linux iwconfig monitor mode by @evilmonkey19 in https://github.com/networktocode/ntc-templates/pull/2160
* Update Mikrotik RouterOS DHCP server lease templates by @evilmonkey19 in https://github.com/networktocode/ntc-templates/pull/2145 and https://github.com/networktocode/ntc-templates/pull/2146

### Bug Fixes & Improvements
* Fix Arista EOS show version for containerlab cEOS by @gsnider2195 in https://github.com/networktocode/ntc-templates/pull/2169
* Modify ASA show access-list PROTOCOL to accept numeric values by @mjbear in https://github.com/networktocode/ntc-templates/pull/2166
* Include Nexus model suffix in show version by @mtinberg in https://github.com/networktocode/ntc-templates/pull/2161
* Updated template to account for BFD echo mode by @mscain in https://github.com/networktocode/ntc-templates/pull/2163
* Fix Arista port-channel member bug and support dense by @mjbear in https://github.com/networktocode/ntc-templates/pull/2143
* Add lines for Arista cEOS version output by @mjbear in https://github.com/networktocode/ntc-templates/pull/2136
* Update cisco_ios_show_interface_link by @Malvin3197 in https://github.com/networktocode/ntc-templates/pull/2128
* Fix Huawei VRP display version template by @kribot-rch in https://github.com/networktocode/ntc-templates/pull/2150
* Fix Huawei VRP display startup template by @ArthurCCT in https://github.com/networktocode/ntc-templates/pull/2151
* Support Alcatel service service-using names with spaces by @jorlandobr in https://github.com/networktocode/ntc-templates/pull/2152
* Fix date,vrf in Mikrotik interface print terse without paging by @dcop25 in https://github.com/networktocode/ntc-templates/pull/2156
* Sanitize test data for Alcatel service-name-using by @jorlandobr in https://github.com/networktocode/ntc-templates/pull/2157

### Code Quality & Testing
* Test for unused capture groups by @mjbear in https://github.com/networktocode/ntc-templates/pull/2155
* Fix broken uppercase capture group test by @mjbear in https://github.com/networktocode/ntc-templates/pull/2144
* Modify TextFSM pinned version via poetry by @mjbear in https://github.com/networktocode/ntc-templates/pull/2153
* Dependabot security fixes and dependency updates by @mjbear in https://github.com/networktocode/ntc-templates/pull/2154

## 👥 New Contributors

* @jfaulkner-fmr made their first contribution in https://github.com/networktocode/ntc-templates/pull/2093
* @Malvin3197 made their first contribution in https://github.com/networktocode/ntc-templates/pull/2128
* @kribot-rch made their first contribution in https://github.com/networktocode/ntc-templates/pull/2150
* @dcop25 made their first contribution in https://github.com/networktocode/ntc-templates/pull/2156
* @ArthurCCT made their first contribution in https://github.com/networktocode/ntc-templates/pull/2151
* @mscain made their first contribution in https://github.com/networktocode/ntc-templates/pull/2163
* @mtinberg made their first contribution in https://github.com/networktocode/ntc-templates/pull/2161
* @gsnider2195 made their first contribution in https://github.com/networktocode/ntc-templates/pull/2169

## 🔄 Migration Guide

### Python Version
Ensure you are running Python 3.9 or higher before upgrading.

### Field Name Changes
If you are using any of the following templates, update your code to use the new field names:

**Arista EOS show interfaces:**
- `interface_up_time` → `last_link_flapped`

**Cisco NX-OS show interface:**
- Multiple field renames for error counters and statistics (see PR #2112 for complete list)

**VLAN ID Normalization:**
- `pvid` fields have been normalized to `vlan_id` across multiple templates

### Template Schema Updates
Review your parsing logic if using:
- Huawei VRP display vlan
- Cisco NX-OS show interface

## 📈 Statistics

- **Total Changes**: 35 pull requests
- **New Templates**: 9
- **Enhanced Templates**: 12
- **Bug Fixes**: 14
- **New Contributors**: 8

**Full Changelog**: https://github.com/networktocode/ntc-templates/compare/v7.9.0...v8.0.0
