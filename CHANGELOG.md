# Changelog

## [Unreleased]

### What's Changed
* New template: cisco_ios_show_crypto_pki_certificates.textfsm by @nsnelson402

## [3.1.0]

### What's Changed
* New template: cisco_ios_show_ip_eigrp_interfaces_detail.textfsm by @nsnelson402 in https://github.com/networktocode/ntc-templates/pull/1181
* New template: cisco_ios_show_snmp_group.textfsm by @nsnelson402 in https://github.com/networktocode/ntc-templates/pull/1183
* New templates & updates: Updated support for Arista EOS devices by @ReK42 in https://github.com/networktocode/ntc-templates/pull/1174
* New template: cisco_xr_show_ipv4_interface.textfsm by @dainok in https://github.com/networktocode/ntc-templates/pull/1162
* New templates: Add multiple zyxel templates by @elavaud in https://github.com/networktocode/ntc-templates/pull/1142
* Bug fix: Change huawei_vrf shortest command by @Elinpf in https://github.com/networktocode/ntc-templates/pull/1141
* Bug fix: Path separator error on windows by  @Elinpf in https://github.com/networktocode/ntc-templates/pull/1139
* New templates: Adding multiple mikrotik routeros templates by @elavaud in https://github.com/networktocode/ntc-templates/pull/1136
* New template: aruba_os_show_ap_database_long.textfsm by @hagleyj in https://github.com/networktocode/ntc-templates/pull/1134
* New template: aruba_os_show_ap_radio-database.textfsm by @hagleyj in https://github.com/networktocode/ntc-templates/pull/1133
* Bug fix: EOS 4.28.XF updated output of codes in `show ip route` by @networkop in https://github.com/networktocode/ntc-templates/pull/1127
* New template: juniper_junos_show_vlans.textfsm by @showipintbri in https://github.com/networktocode/ntc-templates/pull/1125
* Bug fix: cisco_ios show ip bgp neighbors advertised-routes output where metric is wider than 6 chars by @viktorkertesz in https://github.com/networktocode/ntc-templates/pull/1124
* Bug fix: cisco_ios show ip bgp output where metric is wider than 6 chars by @viktorkertesz in https://github.com/networktocode/ntc-templates/pull/1123
* Bug fix: cisco_nxos_show_int_breief do not match mgmt and vlan by @diepes in https://github.com/networktocode/ntc-templates/pull/1119
* Bug fix: cisco_ios_show_module updated output for c9200 @diepes in https://github.com/networktocode/ntc-templates/pull/1117
* Changed: add vlan_id to cisco_ios_show_interfaces by @dainok in https://github.com/networktocode/ntc-templates/pull/1115
* Bug fix: fix not advertised vlan in cisco_nxos_show_lldp_neighbors_detail by @dainok in https://github.com/networktocode/ntc-templates/pull/1114
* Added: Additional fields for cisco_ios_show_ip_access-lists.textfsm by @mjuenema in https://github.com/networktocode/ntc-templates/pull/1113
* Bug fix: Multiple line parsing using lists with textfsm extracting wrong details by @diepes in https://github.com/networktocode/ntc-templates/pull/1112
* Bug fix: Cisco IOS show boot missing parameter by @diepes in https://github.com/networktocode/ntc-templates/pull/1111
* New template: arista_eos_show_processes_top_once.textfsm by @pauljorgenson in https://github.com/networktocode/ntc-templates/pull/1110
* Bug fix: Adding a record without the vlan field for very old HP Procurve switches by @dainok in https://github.com/networktocode/ntc-templates/pull/1108
* New template: cisco_xr_show_install_active.textfsm by @verbosemode in https://github.com/networktocode/ntc-templates/pull/1105
* Changed: Clarifies docs about length order by @jvanderaa in https://github.com/networktocode/ntc-templates/pull/1099
* New template: ubiquiti_edgerouter_show_dhcp_leases.textfsm by @jvanderaa in https://github.com/networktocode/ntc-templates/pull/1097
* Bug fix: hanges the CRLF to LF to pass tests by @jvanderaa in https://github.com/networktocode/ntc-templates/pull/1096
* Changed: Additional fields for cisco_nxos_show_ip_route.textfsm by @lamiskin in https://github.com/networktocode/ntc-templates/pull/1093
* Changed: Additional fields for cisco_nxos_show_ip_interface.textfsm by @lamiskin in https://github.com/networktocode/ntc-templates/pull/1092
* Changed: Additional fields for cisco_ios_show_standby.textfsm by @lamiskin in https://github.com/networktocode/ntc-templates/pull/1091
* Changed: Additional fields for cisco_ios_show_module_status.textfsm by @lamiskin in https://github.com/networktocode/ntc-templates/pull/1090
* Changed: Additional fields for cisco_ios_show_ip_interface.textfsm by @lamiskin in https://github.com/networktocode/ntc-templates/pull/1089
* Changed: Additional fields for cisco_ios_show_interfaces_switchport.textfsm by @lamiskin in https://github.com/networktocode/ntc-templates/pull/1088
* Changed: Additional fields for cisco_ios_show_etherchannel_summary.textfsm by @lamiskin in https://github.com/networktocode/ntc-templates/pull/1087
* Changed: Additional fields for cisco_ios_show_lldp_neighbors_detail.textfsm by @lamiskin in https://github.com/networktocode/ntc-templates/pull/1086
* Changed: Additional fields for cisco_asa_show_interface.textfsm by @lamiskin in https://github.com/networktocode/ntc-templates/pull/1084
* Bug fix: show platform diag does not return the rommon version of the line cards by @network-shark in https://github.com/networktocode/ntc-templates/pull/1081
* New template: zyxel_os_cfg_nat_get.textfsm by @elavaud in https://github.com/networktocode/ntc-templates/pull/1073
* New template: zyxel_os_cfg_ipalias_get.textfsm by @elavaud in https://github.com/networktocode/ntc-templates/pull/1068
* New template: ubiquiti_edgerouter_show_version.textfsm by @elavaud in https://github.com/networktocode/ntc-templates/pull/1065
* New template: ubiquiti_edgerouter_show_interfaces_ethernet_physical.textfsm by @elavaud in https://github.com/networktocode/ntc-templates/pull/1064
* New template: ubiquiti_edgerouter_show_arp.textfsm by @elavaud in https://github.com/networktocode/ntc-templates/pull/1062
* Bug fix: aruba_os_show_ap_database model parsing error by @hagleyj in https://github.com/networktocode/ntc-templates/pull/1055
* Bug fix: cisco_nxos_show_ip_interface parsing error by @diepes in https://github.com/networktocode/ntc-templates/pull/1046
* Bug fix: Update choices for Protocol to include 'notpresent' option on arista_eos_show_interfaces_description by @scetron in https://github.com/networktocode/ntc-templates/pull/1044
* New template: aruba_os_show_ap_database.textfsm by @hagleyj in https://github.com/networktocode/ntc-templates/pull/1042
* Bug fix: cisco_nxos_show_cdp_neighbors_detail update for supporting multiple versions by @Niltak in https://github.com/networktocode/ntc-templates/pull/1039
* Changed: Updated show boot template to include new formatting for Cisco IOS Gibraltar output by @shanecbauman in https://github.com/networktocode/ntc-templates/pull/1038
* Bug fix: cisco_nxos_show_ip_bgp.textfsm not parsing correctly by @diepes in https://github.com/networktocode/ntc-templates/pull/1033
* Added: FTD output example from Cisco support site by @jvanderaa in https://github.com/networktocode/ntc-templates/pull/1032
* New template: cisco_ios_show_ip_nat_translations.textfsm by @ksaegusa in https://github.com/networktocode/ntc-templates/pull/1028
* Bug fix: cisco_ios_show_interfaces_status.textfsm State Error by @ZamElek in https://github.com/networktocode/ntc-templates/pull/1023
* Bug fix: IOS show mac address Type3 and Type4. Additional test files by @armartirosyan in https://github.com/networktocode/ntc-templates/pull/1019
* New template: cisco_asa_show_cpu_usage_detailed.textfsm by @yone2ks in https://github.com/networktocode/ntc-templates/pull/1014
* Bug fix: cisco_ios_show_ip_eigrp_topology not parsing correctly by @diepes in https://github.com/networktocode/ntc-templates/pull/1013

## [3.0.0](https://github.com/networktocode/ntc-templates/tree/3.0.0) (2021-10-28)

[Full Changlog](https://github.com/networktocode/ntc-templates/compare/v2.3.2...3.0.0)

### Breaking Changes

- Template `cisco_ios_show_mac-address-table` has `DESTINATION_PORT` as a list of ports now instead of a single string entry (#994)

### What's Changed
* cisco_ios_show_access-session: Adding Identity to MAC column by @ahlara-devcore in https://github.com/networktocode/ntc-templates/pull/990
* [New Template] Ciena - traffic-profile standard-profile  by @georgesnow in https://github.com/networktocode/ntc-templates/pull/981
* New template: cisco_nxos_show_ip_interface_vrf_all.textfsm by @AJatCDW in https://github.com/networktocode/ntc-templates/pull/978
* New template: juniper_junos_show_system_uptime.textfsm by @antonalekseev in https://github.com/networktocode/ntc-templates/pull/975
* Template Change: cisco_ios, show archive by @QuasarKid in https://github.com/networktocode/ntc-templates/pull/905
* Bugfix: change date format in hp_comware_display_clock.textfsm by @antonalekseev in https://github.com/networktocode/ntc-templates/pull/977
* update arista interface template + raw by @scetron in https://github.com/networktocode/ntc-templates/pull/963
* New Template: cisco_ios_show_dhcp_lease by @lamiskin in https://github.com/networktocode/ntc-templates/pull/991
* Fix ios_mac-addr type2 by @armartirosyan in https://github.com/networktocode/ntc-templates/pull/994
* fix parsing with int addresses = 0 by @dainok in https://github.com/networktocode/ntc-templates/pull/982
* New template for huawei VRP + fix. by @ak-empiak in https://github.com/networktocode/ntc-templates/pull/998
* added VLAN value and search pattern by @dm-bell-networking in https://github.com/networktocode/ntc-templates/pull/1002
* Ciso IOS show mac and show module fix by @armartirosyan in https://github.com/networktocode/ntc-templates/pull/1006
* Junos show chassis by @georgesnow in https://github.com/networktocode/ntc-templates/pull/997

### New Contributors
* @ahlara-devcore made their first contribution in https://github.com/networktocode/ntc-templates/pull/990
* @AJatCDW made their first contribution in https://github.com/networktocode/ntc-templates/pull/978
* @antonalekseev made their first contribution in https://github.com/networktocode/ntc-templates/pull/975
* @lamiskin made their first contribution in https://github.com/networktocode/ntc-templates/pull/991
* @armartirosyan made their first contribution in https://github.com/networktocode/ntc-templates/pull/994
* @ak-empiak made their first contribution in https://github.com/networktocode/ntc-templates/pull/998
* @dm-bell-networking made their first contribution in https://github.com/networktocode/ntc-templates/pull/1002

**Full Changelog**: https://github.com/networktocode/ntc-templates/compare/v2.3.2...v3.0.0
## [2.3.2](https://github.com/networktocode/ntc-templates/tree/2.3.2) (2021-09-13)

[Full Changelog](https://github.com/networktocode/ntc-templates/compare/v2.3.1...2.3.2)

**Bugfixes**

- cisco\_ios\_show\_ip\_bgp\_summary Account for dotted ASN notation [\#987](https://github.com/networktocode/ntc-templates/pull/987) ([thomasbridge74](https://github.com/thomasbridge74))
- cisco\_nxos\_show\_interface\_status Account for blank type [\#980](https://github.com/networktocode/ntc-templates/pull/980) ([Kani999](https://github.com/Kani999))
- cisco\_ios\_show\_interfaces Account for `App Interface` [\#968](https://github.com/networktocode/ntc-templates/pull/968) ([a-finocchiaro](https://github.com/a-finocchiaro))

## [2.3.1](https://github.com/networktocode/ntc-templates/tree/2.3.1) (2021-08-30)

[Full Changelog](https://github.com/networktocode/ntc-templates/compare/v2.3.0...2.3.1)

**Closed issues:**

- cisco\_ios\_show\_ip\_access-lists Account for singluar match [\#972](https://github.com/networktocode/ntc-templates/issues/972) ([mitchell-foxworth](https://github.com/mitchell-foxworth))

**Merged pull requests:**

- ntc_templates/templates/cisco_ios_show_ip_access-lists.textfsm [\#973](https://github.com/networktocode/ntc-templates/pull/973) ([mitchell-foxworth](https://github.com/mitchell-foxworth))

## [2.3.0](https://github.com/networktocode/ntc-templates/tree/2.3.0) (2021-08-27)

[Full Changelog](https://github.com/networktocode/ntc-templates/compare/v2.2.2...2.3.0)

**Closed issues:**

- cisco\_ios\_show\_ip\_access-lists template needs updated to include LOG_TYPE options [\#969](https://github.com/networktocode/ntc-templates/issues/969) ([joewesch](https://github.com/joewesch))

**Merged pull requests:**

- ntc_templates/templates/aruba_aoscx_show_aaa_authentication_port-access_interface_all_client-status.textfsm [\#927](https://github.com/networktocode/ntc-templates/pull/927) ([scetron](https://github.com/scetron))

**New Templates:**

- aruba_aoscx_show_aaa_authentication_port-access_interface_all_client-status.textfsm
- aruba_aoscx_show_arp_all-vrfs.textfsm
- aruba_aoscx_show_bfd_all-vrfs.textfsm
- aruba_aoscx_show_bgp_all-vrfs_all_summary.textfsm
- aruba_aoscx_show_bgp_all_all-vrfs_summary.textfsm
- aruba_aoscx_show_interface.textfsm
- aruba_aoscx_show_interface_dom_detail.textfsm
- aruba_aoscx_show_ip_route_all-vrfs.textfsm
- aruba_aoscx_show_lldp_neighbors-info_detail.textfsm
- aruba_aoscx_show_mac-address-table.textfsm
- aruba_aoscx_show_ntp_associations.textfsm
- aruba_aoscx_show_vsf_detail.textfsm

## [2.2.2](https://github.com/networktocode/ntc-templates/tree/2.1.0) (2021-08-02)

[Full Changelog](https://github.com/networktocode/ntc-templates/compare/v2.2.0...2.2.2)

**Closed issues:**

- cisco\_ios\_show\_ip\_access-lists template needs updated to include additional ICMP_TYPE options [\#964](https://github.com/networktocode/ntc-templates/issues/964)
- cisco\_ios\_show\_version template needs updated to account for StackWise Virtual Domains [\#924](https://github.com/networktocode/ntc-templates/issues/924)

**Merged pull requests:**

- cisco\_ios\_show\_ip\_access-lists.textfsm: Updated to include mask-request in template. [\#965](https://github.com/networktocode/ntc-templates/pull/944) ([nsnelson402](https://github.com/nsnelson402))
- cisco\_ios\_show\_version.textfsm: Updated to account for StackWise Virtual Domains template. [\#960](https://github.com/networktocode/ntc-templates/pull/960) ([itdependsnetworks](https://github.com/itdependsnetworks))

## [2.2.0](https://github.com/networktocode/ntc-templates/tree/2.1.0) (2021-08-02)

[Full Changelog](https://github.com/networktocode/ntc-templates/compare/v2.1.0...2.2.0)

**Closed issues:**

- cisco\_ios\_show\_ip\_access-lists template needs updated to include precedence and tos in *_PORT_MATCH [\#954](https://github.com/networktocode/ntc-templates/issues/954)
- cisco\_nxos\_show\_interface\_transceiver transceiver template failure [\#952](https://github.com/networktocode/ntc-templates/issues/952)

**Merged pull requests:**

- cisco_ios_show_version: Cisco IOS uptime parsing more granular (days, hours, etc.) [\#944](https://github.com/networktocode/ntc-templates/pull/944) ([joewesch](https://github.com/joewesch))
- New Template: cisco_ios_show_crypto_session_details [\#947](https://github.com/networktocode/ntc-templates/pull/947) ([h4ndzdatm0ld](https://github.com/h4ndzdatm0ld))
- cisco_ios_show_vrf.texfsm: Parse a vrf with no interfaces [\#918](https://github.com/networktocode/ntc-templates/pull/918) ([dpnetca](https://github.com/dpnetca))
- cisco_ios_show_interfaces_switchport: Modified Trunk state to handle multiline trunking lists [\#907](https://github.com/networktocode/ntc-templates/pull/907) ([mickyhale](https://github.com/mickyhale))
- Fix nxos_show_interface_transceiver failure [\#953](https://github.com/networktocode/ntc-templates/pull/953) ([chipn](https://github.com/chipn))
- Updated cisco_ios_show_ip_access-lists.textfsm to include the SRC_PORT_MATCH and DST_PORT_MATCH values for precedence and tos [\#955](https://github.com/networktocode/ntc-templates/pull/955) ([nsnelson402](https://github.com/nsnelson402))

## [2.1.0](https://github.com/networktocode/ntc-templates/tree/2.1.0) (2021-06-24)

[Full Changelog](https://github.com/networktocode/ntc-templates/compare/v2.0.0...2.1.0)

**Implemented enhancements:**

- Move to Poetry for dependency and publishing [\#729](https://github.com/networktocode/ntc-templates/issues/729)

**Closed issues:**

- cisco\_nxos\_show\_cdp\_neighbors\_detail   'str' object has no attribute 'seek'. [\#936](https://github.com/networktocode/ntc-templates/issues/936)
- show int status returns error \(seems template error\) for particular switch for other switches it does work \(iOS\). [\#922](https://github.com/networktocode/ntc-templates/issues/922)
- IPinfusuion OCNOS support request  [\#913](https://github.com/networktocode/ntc-templates/issues/913)
- cisco\_ios\_show\_interfaces\_status.textfsm \(no interface in monitoring state\) [\#878](https://github.com/networktocode/ntc-templates/issues/878)
- Arista\_eos: show ip bgp summary Error  [\#844](https://github.com/networktocode/ntc-templates/issues/844)
- arista\_eos\_show\_ip\_route parse exception [\#811](https://github.com/networktocode/ntc-templates/issues/811)
- cisco nxos show interface status issue when FC ports are present [\#788](https://github.com/networktocode/ntc-templates/issues/788)
- cisco\_asa\_show\_running\_cryprom\_map does not parse crypto maps without "set security association lifetime" [\#784](https://github.com/networktocode/ntc-templates/issues/784)
- Cisco ASA show vpn-sessiondb invalid and not returning data after ASA SW update [\#773](https://github.com/networktocode/ntc-templates/issues/773)
- cannot import name 'clitable' from 'textfsm' [\#731](https://github.com/networktocode/ntc-templates/issues/731)

**Merged pull requests:**

- Adding Restarted to show version template for cisco ios [\#940](https://github.com/networktocode/ntc-templates/pull/940) ([ksrattani](https://github.com/ksrattani))
- cisco\_nxos add f-path vlan type [\#937](https://github.com/networktocode/ntc-templates/pull/937) ([JargeZ](https://github.com/JargeZ))
- Fix issue \#929 [\#934](https://github.com/networktocode/ntc-templates/pull/934) ([matt852](https://github.com/matt852))
- New Template: Alcatel, sh router ospf int [\#931](https://github.com/networktocode/ntc-templates/pull/931) ([h4ndzdatm0ld](https://github.com/h4ndzdatm0ld))
- New Template: SROS "show system cpu" [\#930](https://github.com/networktocode/ntc-templates/pull/930) ([h4ndzdatm0ld](https://github.com/h4ndzdatm0ld))
- Adds monitoring port for show interfaces status [\#928](https://github.com/networktocode/ntc-templates/pull/928) ([jvanderaa](https://github.com/jvanderaa))
- New Template: All BGP VPNv4 Neighbors [\#911](https://github.com/networktocode/ntc-templates/pull/911) ([markh0338](https://github.com/markh0338))
- Added Known Issues section to document Micah's finding/issue [\#902](https://github.com/networktocode/ntc-templates/pull/902) ([FragmentedPacket](https://github.com/FragmentedPacket))
- Added deploy option to auto deploy on tags [\#901](https://github.com/networktocode/ntc-templates/pull/901) ([FragmentedPacket](https://github.com/FragmentedPacket))
- sros, new template - sh router interface,  -vrf \# optional [\#898](https://github.com/networktocode/ntc-templates/pull/898) ([h4ndzdatm0ld](https://github.com/h4ndzdatm0ld))
- Add end of line for matching empty lines [\#897](https://github.com/networktocode/ntc-templates/pull/897) ([jmcgill298](https://github.com/jmcgill298))
- New Template: ruckus\_fastiron, show mac-address [\#896](https://github.com/networktocode/ntc-templates/pull/896) ([QuasarKid](https://github.com/QuasarKid))
- New Template: ruckus\_fastiron, show version [\#894](https://github.com/networktocode/ntc-templates/pull/894) ([QuasarKid](https://github.com/QuasarKid))
- New Template: alcatel\_sros, sh router mpls lsp [\#893](https://github.com/networktocode/ntc-templates/pull/893) ([h4ndzdatm0ld](https://github.com/h4ndzdatm0ld))
- New Template: alcatel\_sros, sap-using  [\#892](https://github.com/networktocode/ntc-templates/pull/892) ([h4ndzdatm0ld](https://github.com/h4ndzdatm0ld))
- New Template: alcatel\_sros, sdp-using [\#891](https://github.com/networktocode/ntc-templates/pull/891) ([h4ndzdatm0ld](https://github.com/h4ndzdatm0ld))
- add new template show port-security interface [\#885](https://github.com/networktocode/ntc-templates/pull/885) ([jeffkala](https://github.com/jeffkala))
- Bugfix: Type for cisco\_nxos\_show\_interface\_status [\#880](https://github.com/networktocode/ntc-templates/pull/880) ([FragmentedPacket](https://github.com/FragmentedPacket))

## [v2.0.0](https://github.com/networktocode/ntc-templates/tree/v2.0.0) (2021-03-12)

[Full Changelog](https://github.com/networktocode/ntc-templates/compare/v1.7.0...v2.0.0)

**Merged pull requests:**

- Release v2.0.0 [\#890](https://github.com/networktocode/ntc-templates/pull/890) ([jmcgill298](https://github.com/jmcgill298))
- Migrate packaging to use poetry [\#882](https://github.com/networktocode/ntc-templates/pull/882) ([jmcgill298](https://github.com/jmcgill298))
- Add Dell Force 10 show ip interface brief [\#875](https://github.com/networktocode/ntc-templates/pull/875) ([soer7022](https://github.com/soer7022))
- cisco\_wlc\_ssh\_show\_wlan\_sum update - make PMIP\_MOBILITY optional [\#872](https://github.com/networktocode/ntc-templates/pull/872) ([progala](https://github.com/progala))

## [v1.7.0](https://github.com/networktocode/ntc-templates/tree/v1.7.0) (2021-03-12)

[Full Changelog](https://github.com/networktocode/ntc-templates/compare/v1.6.0...v1.7.0)

**Implemented enhancements:**

- Potential naming inconsistencies between ntc-templates and netmiko for fortinet devices [\#534](https://github.com/networktocode/ntc-templates/issues/534)

**Closed issues:**

- arista\_eos\_show\_interfaces incomplete [\#887](https://github.com/networktocode/ntc-templates/issues/887)
- cisco\_wlc\_ssh\_show\_wlan\_sum update - make PMIP\_MOBILITY optional [\#871](https://github.com/networktocode/ntc-templates/issues/871)
- cisco\_nxos\_show\_ip\_route errors out on Route Not Found [\#869](https://github.com/networktocode/ntc-templates/issues/869)
- cisco\_ios\_show\_interfaces\_description.textfsm fails to parse [\#866](https://github.com/networktocode/ntc-templates/issues/866)
- Having trouble with textfsm [\#858](https://github.com/networktocode/ntc-templates/issues/858)
- cisco\_nxos\_show\_ip\_arp\_detail.textfsm fails to parse Age field \(Age results are of form 00:14:15 AND 0.732312\) [\#851](https://github.com/networktocode/ntc-templates/issues/851)
- arista\_eos\_show\_interfaces\_status parse failures [\#834](https://github.com/networktocode/ntc-templates/issues/834)
- cisco\_ios\_show\_mac-address-table support for pvlans [\#830](https://github.com/networktocode/ntc-templates/issues/830)
- Don’t work when parse output of “show fc zone” for Dell s5000 [\#825](https://github.com/networktocode/ntc-templates/issues/825)
- update nxos show interface to capture discards [\#819](https://github.com/networktocode/ntc-templates/issues/819)
- change key names to match ios template [\#816](https://github.com/networktocode/ntc-templates/issues/816)
- cisco\_nxos\_show\_environment return an empty list [\#790](https://github.com/networktocode/ntc-templates/issues/790)
- cisco show sip-ua register  status [\#787](https://github.com/networktocode/ntc-templates/issues/787)
- Issue with cisco\_ios\_show\_vrf.textfsm template [\#786](https://github.com/networktocode/ntc-templates/issues/786)
- version of OS can differ o/p, how to handle such cases [\#782](https://github.com/networktocode/ntc-templates/issues/782)
- NXSOS SHOW\_INVENTORY ALL [\#778](https://github.com/networktocode/ntc-templates/issues/778)
- ISSUE with show bgp neighboor template IOS XR [\#746](https://github.com/networktocode/ntc-templates/issues/746)

**Merged pull requests:**

- New Template: ruckus\_fastiron, show interfaces brief [\#895](https://github.com/networktocode/ntc-templates/pull/895) ([QuasarKid](https://github.com/QuasarKid))
- Release v1.7.0 [\#889](https://github.com/networktocode/ntc-templates/pull/889) ([jmcgill298](https://github.com/jmcgill298))
- new alcatel\_sros tmpl, 'show service sdp' [\#886](https://github.com/networktocode/ntc-templates/pull/886) ([h4ndzdatm0ld](https://github.com/h4ndzdatm0ld))
- New Template: alcatel\_sros\_show\_router\_rsvp\_interface [\#884](https://github.com/networktocode/ntc-templates/pull/884) ([h4ndzdatm0ld](https://github.com/h4ndzdatm0ld))
- \#784-cisco\_asa\_show\_running-config\_all\_crypto\_map.textfsm [\#883](https://github.com/networktocode/ntc-templates/pull/883) ([diepes](https://github.com/diepes))
- New template: cisco\_ios\_show\_alert\_counters.textfsm [\#881](https://github.com/networktocode/ntc-templates/pull/881) ([FragmentedPacket](https://github.com/FragmentedPacket))
- Bugfix: Media type update for cisco\_ios\_show\_interfaces [\#879](https://github.com/networktocode/ntc-templates/pull/879) ([FragmentedPacket](https://github.com/FragmentedPacket))
- new sros template [\#877](https://github.com/networktocode/ntc-templates/pull/877) ([h4ndzdatm0ld](https://github.com/h4ndzdatm0ld))
- Fixs \#869 cisco nxos show ip route not found [\#870](https://github.com/networktocode/ntc-templates/pull/870) ([diepes](https://github.com/diepes))
- Fix readme [\#868](https://github.com/networktocode/ntc-templates/pull/868) ([jeffkala](https://github.com/jeffkala))
- add test security-policy-match to palo alto [\#867](https://github.com/networktocode/ntc-templates/pull/867) ([jeffkala](https://github.com/jeffkala))
- New template: yamaha [\#865](https://github.com/networktocode/ntc-templates/pull/865) ([akira6592](https://github.com/akira6592))
- Add Environment Variable Option for Custom Template Location [\#863](https://github.com/networktocode/ntc-templates/pull/863) ([jeffkala](https://github.com/jeffkala))
- New Template: hp\_procurve\_show\_port-security [\#862](https://github.com/networktocode/ntc-templates/pull/862) ([adraf82](https://github.com/adraf82))
- Adding in/out route-map parsing to cisco ios show ip bgp nei template [\#861](https://github.com/networktocode/ntc-templates/pull/861) ([nnaukwal](https://github.com/nnaukwal))
- Fortinet updates [\#860](https://github.com/networktocode/ntc-templates/pull/860) ([refriedjello](https://github.com/refriedjello))
- Fixes \#851 and add new template  [\#857](https://github.com/networktocode/ntc-templates/pull/857) ([diepes](https://github.com/diepes))
- New Templates: Cisco IOS show vrrp brief and all [\#856](https://github.com/networktocode/ntc-templates/pull/856) ([mjbear](https://github.com/mjbear))
- Adding new templates for show \(radius|tacacs\) summary output [\#855](https://github.com/networktocode/ntc-templates/pull/855) ([mjbear](https://github.com/mjbear))
- New Template: Cisco WLC show port summary and show stats port summary [\#854](https://github.com/networktocode/ntc-templates/pull/854) ([mjbear](https://github.com/mjbear))
- New Template: Cisco WLC show time \(for time and NTP information\) [\#853](https://github.com/networktocode/ntc-templates/pull/853) ([mjbear](https://github.com/mjbear))
- New Template - cisco\_ios\_show\_object-group [\#850](https://github.com/networktocode/ntc-templates/pull/850) ([pkomissarov](https://github.com/pkomissarov))
- cisco\_nxos\_show\_ip\_bgp\_summary\_vrf update to support 32-bits ASN outputs [\#849](https://github.com/networktocode/ntc-templates/pull/849) ([burningnode](https://github.com/burningnode))
- New Template: Cisco WLC show mobility anchor [\#847](https://github.com/networktocode/ntc-templates/pull/847) ([mjbear](https://github.com/mjbear))
- New Template: Cisco WLC show redundancy summary and detail [\#846](https://github.com/networktocode/ntc-templates/pull/846) ([mjbear](https://github.com/mjbear))
- Fixes \#773 CiscoASA-show\_vpn-sessiondb\_SW\_update [\#845](https://github.com/networktocode/ntc-templates/pull/845) ([diepes](https://github.com/diepes))
- Fixes\#811 arista eos show ip route [\#843](https://github.com/networktocode/ntc-templates/pull/843) ([diepes](https://github.com/diepes))
- updated template and added test file [\#842](https://github.com/networktocode/ntc-templates/pull/842) ([adraf82](https://github.com/adraf82))
- Fix\#784 new:  cisco asa show running all cryprom map [\#840](https://github.com/networktocode/ntc-templates/pull/840) ([diepes](https://github.com/diepes))
- Fix\#788 ios show int fc [\#839](https://github.com/networktocode/ntc-templates/pull/839) ([diepes](https://github.com/diepes))
- Fixes \#790 - new template cisco\_nxos\_show\_environment.textfsm  [\#838](https://github.com/networktocode/ntc-templates/pull/838) ([diepes](https://github.com/diepes))
- Add codeowners file [\#837](https://github.com/networktocode/ntc-templates/pull/837) ([jmcgill298](https://github.com/jmcgill298))
- Enhancment: EOS show int status - account for LAG members [\#835](https://github.com/networktocode/ntc-templates/pull/835) ([jmcgill298](https://github.com/jmcgill298))
- update Cisco IOS show tacacs template to support parsing of server name in newer configurations [\#833](https://github.com/networktocode/ntc-templates/pull/833) ([anirudhkamath](https://github.com/anirudhkamath))
- added fortinet get system arp [\#832](https://github.com/networktocode/ntc-templates/pull/832) ([wmclendon](https://github.com/wmclendon))
- Enhancement: Change fortinet\_fortios to fortinet per Netmiko [\#831](https://github.com/networktocode/ntc-templates/pull/831) ([jmcgill298](https://github.com/jmcgill298))
- New Template: hp\_procurve\_show\_interfaces\_brief.textfsm [\#829](https://github.com/networktocode/ntc-templates/pull/829) ([adraf82](https://github.com/adraf82))
- New template: Vyatta/VyOS BGP summary [\#828](https://github.com/networktocode/ntc-templates/pull/828) ([jpbede](https://github.com/jpbede))
- New template: dell\_powerconnect [\#827](https://github.com/networktocode/ntc-templates/pull/827) ([nidebr](https://github.com/nidebr))
- Some sros commands [\#824](https://github.com/networktocode/ntc-templates/pull/824) ([kvlangenhove](https://github.com/kvlangenhove))
- updated hp\_procurve\_show\_interfaces template for backward compatibility [\#823](https://github.com/networktocode/ntc-templates/pull/823) ([adraf82](https://github.com/adraf82))
- New template: arista\_eos\_show\_interfaces\_description [\#822](https://github.com/networktocode/ntc-templates/pull/822) ([rich-day](https://github.com/rich-day))
- Bugfix: issues with cisco\_nxos\_show\_ip\_dhcp\_relay\_address [\#821](https://github.com/networktocode/ntc-templates/pull/821) ([wvandeun](https://github.com/wvandeun))
- Bugfix: URL ACL property in cisco\_wlc\_ssh\_show\_interface\_detailed [\#820](https://github.com/networktocode/ntc-templates/pull/820) ([wvandeun](https://github.com/wvandeun))
- Bugfix: added 'Autostate exclude' to avoid error [\#818](https://github.com/networktocode/ntc-templates/pull/818) ([abaretta](https://github.com/abaretta))
- fix unconfigured DHCP issue in cisco\_wlc\_ssh\_show\_interface\_detailed [\#817](https://github.com/networktocode/ntc-templates/pull/817) ([wvandeun](https://github.com/wvandeun))
- cisco\_nxos show version - extract serial from "Processor board ID" [\#813](https://github.com/networktocode/ntc-templates/pull/813) ([diepes](https://github.com/diepes))
- Bugfix: cisco ios show ip access-list [\#809](https://github.com/networktocode/ntc-templates/pull/809) ([jpobeda](https://github.com/jpobeda))
- Bugfix: IOS show lldp neig - fix neighbor name with spaces [\#799](https://github.com/networktocode/ntc-templates/pull/799) ([realvitya](https://github.com/realvitya))

## [v1.6.0](https://github.com/networktocode/ntc-templates/tree/v1.6.0) (2020-10-26)

[Full Changelog](https://github.com/networktocode/ntc-templates/compare/v1.5.0...v1.6.0)

**Implemented enhancements:**

- Creation of a Faq [\#716](https://github.com/networktocode/ntc-templates/issues/716)

**Closed issues:**

- This is not a data modeling project. So is there any data modeling project can work with this? [\#802](https://github.com/networktocode/ntc-templates/issues/802)
- Black 20.b0 breaks tox test [\#794](https://github.com/networktocode/ntc-templates/issues/794)
- Unable to Parse show version on IOSv Device [\#780](https://github.com/networktocode/ntc-templates/issues/780)
- TXTFSM will not process template even though Regex checker  says line is acceptable for ciena SAOS [\#779](https://github.com/networktocode/ntc-templates/issues/779)
- cisco\_nxos\_show\_ip\_bgp\_summary.textfsm doesn't account for dual line bgp when output is too wide [\#766](https://github.com/networktocode/ntc-templates/issues/766)
- arista eos show mac address-table is choking on case sensitivity on line Total Mac Addresses for this criterion: 0 [\#764](https://github.com/networktocode/ntc-templates/issues/764)

**Merged pull requests:**

- Bugfix: ASA show interface - missing case handled for no values for duplex & speed [\#815](https://github.com/networktocode/ntc-templates/pull/815) ([starlightdreamer](https://github.com/starlightdreamer))
- Linux arp a [\#814](https://github.com/networktocode/ntc-templates/pull/814) ([jifox](https://github.com/jifox))
- add template and tests for cisco\_wlc\_ssh\_show\_interface\_detailed [\#812](https://github.com/networktocode/ntc-templates/pull/812) ([wvandeun](https://github.com/wvandeun))
- fix issue in cisco\_wlc\_ssh\_show\_interface\_summary template [\#810](https://github.com/networktocode/ntc-templates/pull/810) ([wvandeun](https://github.com/wvandeun))
- Bugfix: cisco\_ios\_show\_running\_partition\_access\_list [\#808](https://github.com/networktocode/ntc-templates/pull/808) ([jpobeda](https://github.com/jpobeda))
- Release 1.6.0 [\#807](https://github.com/networktocode/ntc-templates/pull/807) ([jmcgill298](https://github.com/jmcgill298))
- changes tests to import from lib [\#806](https://github.com/networktocode/ntc-templates/pull/806) ([jmcgill298](https://github.com/jmcgill298))
- modify for show inventory all. [\#804](https://github.com/networktocode/ntc-templates/pull/804) ([yshu95](https://github.com/yshu95))
- Change TextFSM Windows failure to a runtime failure \(instead of an import failure\) [\#803](https://github.com/networktocode/ntc-templates/pull/803) ([ktbyers](https://github.com/ktbyers))
- Added juniper\_junos\_show\_lldp\_neighbors [\#797](https://github.com/networktocode/ntc-templates/pull/797) ([qduk](https://github.com/qduk))
- New Template - hp\_procurve\_show\_interfaces [\#796](https://github.com/networktocode/ntc-templates/pull/796) ([adraf82](https://github.com/adraf82))
- Bugfix: Re-formatted development\_scripts.py and tests/test\_testcases\_… [\#795](https://github.com/networktocode/ntc-templates/pull/795) ([mjuenema](https://github.com/mjuenema))
- Fix typos in README.md [\#792](https://github.com/networktocode/ntc-templates/pull/792) ([epryan](https://github.com/epryan))
- update arista\_eos\_show\_inventory [\#791](https://github.com/networktocode/ntc-templates/pull/791) ([yshu95](https://github.com/yshu95))
- Detect hostname on NX-OS platforms [\#789](https://github.com/networktocode/ntc-templates/pull/789) ([Yakuza-UA](https://github.com/Yakuza-UA))
- Cisco ASA show access-list command templates update. [\#783](https://github.com/networktocode/ntc-templates/pull/783) ([HideoYukutake](https://github.com/HideoYukutake))
- Updates to include capture on single word, no number model number [\#781](https://github.com/networktocode/ntc-templates/pull/781) ([jvanderaa](https://github.com/jvanderaa))
- Bugfix: Account for "powered-up" value in the output of nxos show module [\#774](https://github.com/networktocode/ntc-templates/pull/774) ([mtbutler07](https://github.com/mtbutler07))
- Dual line support for Cisco NX-OS 'ip bgp summary' command [\#772](https://github.com/networktocode/ntc-templates/pull/772) ([rtkennedy](https://github.com/rtkennedy))
- Arista eos show mac address table [\#765](https://github.com/networktocode/ntc-templates/pull/765) ([JoeyG1973](https://github.com/JoeyG1973))
- New Template: cisco\_nxos\_show\_ip\_interface [\#761](https://github.com/networktocode/ntc-templates/pull/761) ([network-dave](https://github.com/network-dave))
- New Template: cisco\_nxos\_show\_hsrp\_all [\#760](https://github.com/networktocode/ntc-templates/pull/760) ([network-dave](https://github.com/network-dave))
- New Template: cisco\_nxos\_show\_license\_usage [\#759](https://github.com/networktocode/ntc-templates/pull/759) ([network-dave](https://github.com/network-dave))
- New Template: cisco\_nxos\_show\_interface\_description [\#758](https://github.com/networktocode/ntc-templates/pull/758) ([network-dave](https://github.com/network-dave))
- Fixes \#716 [\#753](https://github.com/networktocode/ntc-templates/pull/753) ([itdependsnetworks](https://github.com/itdependsnetworks))

## [v1.5.0](https://github.com/networktocode/ntc-templates/tree/v1.5.0) (2020-06-15)

[Full Changelog](https://github.com/networktocode/ntc-templates/compare/v1.4.2...v1.5.0)

**Implemented enhancements:**

- Broadcom ICOS/Fastpath Support? [\#726](https://github.com/networktocode/ntc-templates/issues/726)

**Fixed bugs:**

- Cisco IOS show cdp neighbors issue [\#727](https://github.com/networktocode/ntc-templates/issues/727)
- Cisco IOS Show Interface Switchport does not parse multi-line VLAN Trunks [\#642](https://github.com/networktocode/ntc-templates/issues/642)
- Cisco ASA Show interface does not catch unnamed interfaces [\#627](https://github.com/networktocode/ntc-templates/issues/627)
- Fixes missing interfaces on down interfaces [\#734](https://github.com/networktocode/ntc-templates/pull/734) ([jvanderaa](https://github.com/jvanderaa))

**Closed issues:**

- Cisco ASA "show vpn-sessiondb anyconnect" parser doesn't support IPv6 addresses [\#751](https://github.com/networktocode/ntc-templates/issues/751)
- failing testsuite [\#743](https://github.com/networktocode/ntc-templates/issues/743)
- I would like to contribute the PR for adding new cisco\_wlc\_ssh\_show\_ap\_image\_all [\#739](https://github.com/networktocode/ntc-templates/issues/739)
- Template help for multiple states [\#737](https://github.com/networktocode/ntc-templates/issues/737)
- textfsm.parser.TextFSMError: State Error raised. Rule Line: 15. Input Line: show ip arp [\#686](https://github.com/networktocode/ntc-templates/issues/686)
- Arista eos - sh ip bgp summ vrf all and sh ip route vrf all template [\#666](https://github.com/networktocode/ntc-templates/issues/666)
- Template Creation Help: cisco\_xr\_admin\_show\_environment\_power to get power supply, voltage and current   [\#648](https://github.com/networktocode/ntc-templates/issues/648)
- New template: hp\_comware\_display\_interface\_textFSM [\#634](https://github.com/networktocode/ntc-templates/issues/634)
- cisco\_asa\_show\_failover\_state [\#546](https://github.com/networktocode/ntc-templates/issues/546)

**Merged pull requests:**

- Bumping to version 1.5.0 [\#763](https://github.com/networktocode/ntc-templates/pull/763) ([FragmentedPacket](https://github.com/FragmentedPacket))
- Arista eos show port channel summary [\#757](https://github.com/networktocode/ntc-templates/pull/757) ([JoeyG1973](https://github.com/JoeyG1973))
- Arista eos show mac address table [\#756](https://github.com/networktocode/ntc-templates/pull/756) ([JoeyG1973](https://github.com/JoeyG1973))
- Template correction for broadcom\_icos\_show\_mac-address-table [\#754](https://github.com/networktocode/ntc-templates/pull/754) ([alepodj](https://github.com/alepodj))
- Fixes \#751 - IPv6 support for Cisco ASA 'show vpn-sessiondb anyconnect' [\#752](https://github.com/networktocode/ntc-templates/pull/752) ([smfeldman](https://github.com/smfeldman))
- New Template added support for broadcom\_icos\_show\_vlan\_brief [\#750](https://github.com/networktocode/ntc-templates/pull/750) ([alepodj](https://github.com/alepodj))
- New Template added support for broadcom\_icos\_show\_lldp\_remote-device\_all [\#749](https://github.com/networktocode/ntc-templates/pull/749) ([alepodj](https://github.com/alepodj))
- New Template added support for broadcom\_icos\_show\_isdp\_neighbors [\#748](https://github.com/networktocode/ntc-templates/pull/748) ([alepodj](https://github.com/alepodj))
- Bugfix: Account for totals - cisco\_ios\_show\_processes\_memory\_sorted.textfsm [\#747](https://github.com/networktocode/ntc-templates/pull/747) ([FragmentedPacket](https://github.com/FragmentedPacket))
- Enhancement for Cisco IOS show interfaces [\#745](https://github.com/networktocode/ntc-templates/pull/745) ([Yakuza-UA](https://github.com/Yakuza-UA))
- Added interfaces to arista\_eos\_show\_vrf template [\#744](https://github.com/networktocode/ntc-templates/pull/744) ([JoeyG1973](https://github.com/JoeyG1973))
- Add new template for cisco\_wlc\_ssh\_sh\_ap\_image\_all [\#742](https://github.com/networktocode/ntc-templates/pull/742) ([conorwoo](https://github.com/conorwoo))
- Update index to handle cisco\_ios show\_ip\_bgp\_all\_summary [\#738](https://github.com/networktocode/ntc-templates/pull/738) ([Niclnx](https://github.com/Niclnx))
- Added support for broadcom\_icos command show\_mac-address-table [\#736](https://github.com/networktocode/ntc-templates/pull/736) ([alepodj](https://github.com/alepodj))
- BugFix: IOS CDP - Better handling of output [\#735](https://github.com/networktocode/ntc-templates/pull/735) ([jmcgill298](https://github.com/jmcgill298))
- New Template support for broadcom\_icos as a new OS and added show\_version command [\#733](https://github.com/networktocode/ntc-templates/pull/733) ([alepodj](https://github.com/alepodj))
- New template for ubiquity edgeswitch: show version [\#732](https://github.com/networktocode/ntc-templates/pull/732) ([saaverdo](https://github.com/saaverdo))
- New Template for Cisco NX-OS: show forwarding adjacency [\#722](https://github.com/networktocode/ntc-templates/pull/722) ([Yakuza-UA](https://github.com/Yakuza-UA))
- BugFix: cisco\_ios\_show\_interfaces\_switchport: Made trunking\_vlans a list, and changed regex [\#671](https://github.com/networktocode/ntc-templates/pull/671) ([FragmentedPacket](https://github.com/FragmentedPacket))

## [v1.4.2](https://github.com/networktocode/ntc-templates/tree/v1.4.2) (2020-05-26)

[Full Changelog](https://github.com/networktocode/ntc-templates/compare/v1.4.1...v1.4.2)

**Fixed bugs:**

- cisco\_ios "show ip ospf database router" fails if OSPF domain includes an ASBR or an ABR [\#690](https://github.com/networktocode/ntc-templates/issues/690)
- Arista EOS show ip route parse error [\#668](https://github.com/networktocode/ntc-templates/issues/668)
- cisco\_ios\_show\_ip\_interface does not deal with ip address negotiated on Tunnel interface [\#644](https://github.com/networktocode/ntc-templates/issues/644)

**Closed issues:**

- Cisco IOS - textfsm.parser.TextFSMError: State Error raised. Rule Line: 17.   [\#718](https://github.com/networktocode/ntc-templates/issues/718)
- show mac address-table Error: State Error raised. Rule Line: 41. [\#715](https://github.com/networktocode/ntc-templates/issues/715)
- show mac address-table no dictionary in response [\#714](https://github.com/networktocode/ntc-templates/issues/714)
- Having trouble with alcatel\_sros templates  [\#698](https://github.com/networktocode/ntc-templates/issues/698)
- Cisco show cdp neighbor details leaves whitespace in capabilities field [\#683](https://github.com/networktocode/ntc-templates/issues/683)
- cisco\_ios neighbor summary per address family new request. [\#664](https://github.com/networktocode/ntc-templates/issues/664)
- cisco\_ios BGP neighbor advertised and received routes request. [\#663](https://github.com/networktocode/ntc-templates/issues/663)
- Ciena naming doesn’t conform to Netmiko [\#662](https://github.com/networktocode/ntc-templates/issues/662)
- Problem to add or install ntc-templates: [\#658](https://github.com/networktocode/ntc-templates/issues/658)
- show\_vlan template for cisco ios does not return more than 60 interfaces [\#653](https://github.com/networktocode/ntc-templates/issues/653)
- Unable to parse data by using "cisco\_ios\_show\_ip\_route\_summary.textfsm" [\#643](https://github.com/networktocode/ntc-templates/issues/643)
- template request: show ip bgp neighbors x.x.x.x advertised-routes  [\#639](https://github.com/networktocode/ntc-templates/issues/639)

**Merged pull requests:**

- Bump version to 1.4.2 [\#728](https://github.com/networktocode/ntc-templates/pull/728) ([FragmentedPacket](https://github.com/FragmentedPacket))
- 718 fix [\#725](https://github.com/networktocode/ntc-templates/pull/725) ([itdependsnetworks](https://github.com/itdependsnetworks))
- Update to enforce double-quote [\#724](https://github.com/networktocode/ntc-templates/pull/724) ([itdependsnetworks](https://github.com/itdependsnetworks))
- Enhance Template for Cisco IOS: show adjacency [\#721](https://github.com/networktocode/ntc-templates/pull/721) ([Yakuza-UA](https://github.com/Yakuza-UA))
- New templates: Cisco s300 - LLDP Neighbors, Interfaces status, Mac address table [\#719](https://github.com/networktocode/ntc-templates/pull/719) ([FragmentedPacket](https://github.com/FragmentedPacket))
- EOS can have N/A in the age field for show ip arp [\#717](https://github.com/networktocode/ntc-templates/pull/717) ([ktbyers](https://github.com/ktbyers))
- New Template: juniper\_junos\_show\_lacp\_interfaces [\#713](https://github.com/networktocode/ntc-templates/pull/713) ([ichisuke55](https://github.com/ichisuke55))
- New Template: paloalto\_panos\_show\_interface\_management.textfsm [\#712](https://github.com/networktocode/ntc-templates/pull/712) ([FragmentedPacket](https://github.com/FragmentedPacket))
- Bugfix: EOS - show\_interfaces - Added proper link\_status capture for admin down [\#711](https://github.com/networktocode/ntc-templates/pull/711) ([FragmentedPacket](https://github.com/FragmentedPacket))
- Bugfix: Panos sh intf hardware - Account for unk for SPEED/Duplex [\#710](https://github.com/networktocode/ntc-templates/pull/710) ([FragmentedPacket](https://github.com/FragmentedPacket))
- BugFix: Updated index file to work for show ip bgp neighbors x.x.x.x adv-routes [\#709](https://github.com/networktocode/ntc-templates/pull/709) ([FragmentedPacket](https://github.com/FragmentedPacket))
- BugFix: Ciena Saos: Added more use cases to vlan\_show [\#707](https://github.com/networktocode/ntc-templates/pull/707) ([FragmentedPacket](https://github.com/FragmentedPacket))
- paloalto\_panos\_debug\_swm\_status.textfsm new template [\#706](https://github.com/networktocode/ntc-templates/pull/706) ([ancoleman](https://github.com/ancoleman))
- New Template for Cisco NX-OS: show ip adjacency [\#704](https://github.com/networktocode/ntc-templates/pull/704) ([Yakuza-UA](https://github.com/Yakuza-UA))
- New Template for Cisco IOS: show ip vrf interfaces [\#702](https://github.com/networktocode/ntc-templates/pull/702) ([Yakuza-UA](https://github.com/Yakuza-UA))
- Existing Template for Cisco NX-OS: show ip interface brief \(VRF support added\) [\#701](https://github.com/networktocode/ntc-templates/pull/701) ([Yakuza-UA](https://github.com/Yakuza-UA))
- New Template: juniper\_junos\_show\_ethenet-switching\_table.textfsm [\#700](https://github.com/networktocode/ntc-templates/pull/700) ([ichisuke55](https://github.com/ichisuke55))
- New Template for Cisco IOS: traceroute \<destination\> \[options\] [\#699](https://github.com/networktocode/ntc-templates/pull/699) ([Yakuza-UA](https://github.com/Yakuza-UA))
- BugFix: show vpn-sessiondb anyconnect - Index and Username ends up on… [\#697](https://github.com/networktocode/ntc-templates/pull/697) ([anttof](https://github.com/anttof))
- Asa bgp summary [\#696](https://github.com/networktocode/ntc-templates/pull/696) ([corvese](https://github.com/corvese))
- New Template for Cisco IOS: show ip cef \[detail\] [\#695](https://github.com/networktocode/ntc-templates/pull/695) ([Yakuza-UA](https://github.com/Yakuza-UA))
- Ciena sshkeystatus [\#693](https://github.com/networktocode/ntc-templates/pull/693) ([georgesnow](https://github.com/georgesnow))
- Cisco IOS 'show adjacency .\* detail' [\#692](https://github.com/networktocode/ntc-templates/pull/692) ([Yakuza-UA](https://github.com/Yakuza-UA))
- Bugfix: Accounted for ASBR/ABR in cisco\_ios\_show\_ip\_ospf\_database\_router [\#691](https://github.com/networktocode/ntc-templates/pull/691) ([FragmentedPacket](https://github.com/FragmentedPacket))
- HP Procurve show lldp info remote device [\#689](https://github.com/networktocode/ntc-templates/pull/689) ([sliddjur](https://github.com/sliddjur))
- HP Procurve show lldp info remote-device detail [\#688](https://github.com/networktocode/ntc-templates/pull/688) ([sliddjur](https://github.com/sliddjur))
- HP Procurve show trunks [\#687](https://github.com/networktocode/ntc-templates/pull/687) ([sliddjur](https://github.com/sliddjur))
- BugFix: \(IOS\) - show cdp neighbors detail - Prevent capturing trailing whitespace for capabilities [\#684](https://github.com/networktocode/ntc-templates/pull/684) ([FragmentedPacket](https://github.com/FragmentedPacket))
- BugFix: IOS - show ip bgp summary: Added new field ADDR\_FAMILY for any that may have an address family [\#679](https://github.com/networktocode/ntc-templates/pull/679) ([FragmentedPacket](https://github.com/FragmentedPacket))
- BugFix: IOS - show ip bgp - Account for VRF info within routing table [\#678](https://github.com/networktocode/ntc-templates/pull/678) ([FragmentedPacket](https://github.com/FragmentedPacket))
- New Template: \(IOS\) show\_ip\_bgp\_neighbors\_advertised\_routes [\#674](https://github.com/networktocode/ntc-templates/pull/674) ([FragmentedPacket](https://github.com/FragmentedPacket))
- Enhancement: Added CRC and Abort Values to ios\_show\_interfaces template [\#673](https://github.com/networktocode/ntc-templates/pull/673) ([mtbutler07](https://github.com/mtbutler07))
- Remove "terminal" dependency [\#672](https://github.com/networktocode/ntc-templates/pull/672) ([ktbyers](https://github.com/ktbyers))
- BugFix: cisco\_ios\_show\_ip\_interface: Account for Internet address that is negotiated [\#670](https://github.com/networktocode/ntc-templates/pull/670) ([FragmentedPacket](https://github.com/FragmentedPacket))
- BugFix: arista\_eos\_show\_ip\_route: Accounting for new data for WARNING output & capture ecmp routes [\#669](https://github.com/networktocode/ntc-templates/pull/669) ([FragmentedPacket](https://github.com/FragmentedPacket))
- Enhancement: cisco\_ios\_show\_redundancy - Add New fields [\#667](https://github.com/networktocode/ntc-templates/pull/667) ([FragmentedPacket](https://github.com/FragmentedPacket))
- Ciena SAOS templates \(naming fix\) [\#665](https://github.com/networktocode/ntc-templates/pull/665) ([georgesnow](https://github.com/georgesnow))
- Adds support for Cisco FTD [\#654](https://github.com/networktocode/ntc-templates/pull/654) ([micahculpepper](https://github.com/micahculpepper))
- New Template: hp\_comware\_display\_ip\_routing-table & hp\_comware\_display\_device\_manuinfo [\#623](https://github.com/networktocode/ntc-templates/pull/623) ([xdai555](https://github.com/xdai555))

## [v1.4.1](https://github.com/networktocode/ntc-templates/tree/v1.4.1) (2020-04-23)

[Full Changelog](https://github.com/networktocode/ntc-templates/compare/v1.4.0...v1.4.1)

**Closed issues:**

- cisco\_ios\_show\_mac-address-table.textfsm "N/A" in vlan field. [\#657](https://github.com/networktocode/ntc-templates/issues/657)
- platform="cisco\_ios", command="sh ip route summary" returning an empty array.  [\#655](https://github.com/networktocode/ntc-templates/issues/655)
- Beginning of output for cisco\_ios "show ip ospf database \<lsa-type\>" may or may not be a space character [\#649](https://github.com/networktocode/ntc-templates/issues/649)
- Cisco ASA show\_route parsing for alternative multiline format [\#646](https://github.com/networktocode/ntc-templates/issues/646)
- Cisco ASA AnyConnect Errors with Tunnel Group on different line [\#630](https://github.com/networktocode/ntc-templates/issues/630)
- Create Template for Cisco ASA - show vpn-sessiondb anyconnect [\#624](https://github.com/networktocode/ntc-templates/issues/624)
- Juniper Junos add fpc:X, {master:X} for many commans stdout [\#621](https://github.com/networktocode/ntc-templates/issues/621)

**Merged pull requests:**

- Forgot to bump version in lib/ntc\_templates/\_\_init\_\_.py [\#661](https://github.com/networktocode/ntc-templates/pull/661) ([FragmentedPacket](https://github.com/FragmentedPacket))
- Added information for all new changes between 1.4.0 and now [\#660](https://github.com/networktocode/ntc-templates/pull/660) ([FragmentedPacket](https://github.com/FragmentedPacket))
- BugFix: cisco\_ios\_show\_mac-address-table: Allows N/A in the VLAN field by changing it from word to non-whitespace [\#659](https://github.com/networktocode/ntc-templates/pull/659) ([FragmentedPacket](https://github.com/FragmentedPacket))
- BugFix: cisco\_ios show ip ospf database router and network: Make leading spaces optional [\#650](https://github.com/networktocode/ntc-templates/pull/650) ([ariesgeek](https://github.com/ariesgeek))
- Cisco ASA show\_route [\#647](https://github.com/networktocode/ntc-templates/pull/647) ([fatred](https://github.com/fatred))
- Enhancement: cisco\_asa\_show\_inventory support inventory items w/o SN [\#638](https://github.com/networktocode/ntc-templates/pull/638) ([wvandeun](https://github.com/wvandeun))
- show band-select template [\#637](https://github.com/networktocode/ntc-templates/pull/637) ([timjsmith24](https://github.com/timjsmith24))
- Adds Cisco ASA show vpn-sessiondb [\#636](https://github.com/networktocode/ntc-templates/pull/636) ([jvanderaa](https://github.com/jvanderaa))
- add cisco\_ios\_show\_ip\_route\_summary [\#635](https://github.com/networktocode/ntc-templates/pull/635) ([kjoyce77](https://github.com/kjoyce77))
- Bugfix: cisco asa show nat [\#632](https://github.com/networktocode/ntc-templates/pull/632) ([joewesch](https://github.com/joewesch))
- Updates based on hung sessions and different command output [\#631](https://github.com/networktocode/ntc-templates/pull/631) ([jvanderaa](https://github.com/jvanderaa))
- Bugfix: Cisco ASA ipsec sa name compatibility [\#629](https://github.com/networktocode/ntc-templates/pull/629) ([joewesch](https://github.com/joewesch))
- cisco\_wlc show mobility summary [\#628](https://github.com/networktocode/ntc-templates/pull/628) ([timjsmith24](https://github.com/timjsmith24))
- Updates Cisco ASA `show vpn-sessiondb anyconnect` [\#626](https://github.com/networktocode/ntc-templates/pull/626) ([jvanderaa](https://github.com/jvanderaa))
- Adds template for Cisco ASA "show vpn-sessiondb anyconnect" [\#625](https://github.com/networktocode/ntc-templates/pull/625) ([jvanderaa](https://github.com/jvanderaa))
- Junos virtual chassis [\#622](https://github.com/networktocode/ntc-templates/pull/622) ([ainamori](https://github.com/ainamori))
- allow space in fex description [\#620](https://github.com/networktocode/ntc-templates/pull/620) ([daanvdsanden](https://github.com/daanvdsanden))
- New Template: hp\_comware\_display\_lldp\_neighbor-information\_verbose [\#619](https://github.com/networktocode/ntc-templates/pull/619) ([xdai555](https://github.com/xdai555))
- New Template: cisco\_ios\_show\_ip\_ospf\_database\_network [\#618](https://github.com/networktocode/ntc-templates/pull/618) ([ChristopherJHart](https://github.com/ChristopherJHart))
- BugFix: Remove reliance on static spacing for cisco\_ios\_show\_ip\_ospf\_database\_router [\#617](https://github.com/networktocode/ntc-templates/pull/617) ([ChristopherJHart](https://github.com/ChristopherJHart))
- BugFix: Removed reliance on static spacing for cisco\_ios\_show\_interfaces\_status [\#614](https://github.com/networktocode/ntc-templates/pull/614) ([FragmentedPacket](https://github.com/FragmentedPacket))

## [v1.4.0](https://github.com/networktocode/ntc-templates/tree/v1.4.0) (2020-03-09)

[Full Changelog](https://github.com/networktocode/ntc-templates/compare/v1.3.0...v1.4.0)

**Implemented enhancements:**

- Testing that test cases exist has an exception for 4 templates that need to be rectified [\#550](https://github.com/networktocode/ntc-templates/issues/550)
- Huawei - display lldp neighbor formatting [\#396](https://github.com/networktocode/ntc-templates/issues/396)
- Adding vlan name to access vlan and native vlan on NXOS [\#612](https://github.com/networktocode/ntc-templates/pull/612) ([daanvdsanden](https://github.com/daanvdsanden))
- Enhancement: cisco\_nxos\_show\_vlan: Added interfaces [\#604](https://github.com/networktocode/ntc-templates/pull/604) ([FragmentedPacket](https://github.com/FragmentedPacket))
- Enhancement: IOS lldp neighbors - add capabilities capture group [\#553](https://github.com/networktocode/ntc-templates/pull/553) ([ewmanthei](https://github.com/ewmanthei))
- Enhancement: Use ".textfsm" extension for IDEs [\#543](https://github.com/networktocode/ntc-templates/pull/543) ([jmcgill298](https://github.com/jmcgill298))
- YAMLLINT: Add yamllint to tox testing [\#406](https://github.com/networktocode/ntc-templates/pull/406) ([jmcgill298](https://github.com/jmcgill298))

**Fixed bugs:**

- parse\_output returns empty after interface has been modified by first run of script [\#613](https://github.com/networktocode/ntc-templates/issues/613)
-  arista\_eos\_show\_ip\_route.textfsm fails on vrrp route display [\#588](https://github.com/networktocode/ntc-templates/issues/588)
- ASA show failover bug when using IPS module [\#547](https://github.com/networktocode/ntc-templates/issues/547)
- cisco\_nxos\_show\_version does not display N5K platform [\#545](https://github.com/networktocode/ntc-templates/issues/545)
- Fix regex: Update VyOS template to match addresses without netmask de… [\#608](https://github.com/networktocode/ntc-templates/pull/608) ([sliddjur](https://github.com/sliddjur))
- Fixed regex for fortinet bgp template and added new template standards [\#592](https://github.com/networktocode/ntc-templates/pull/592) ([corvese](https://github.com/corvese))
- BugFix: Cisco show switch detail with mac persistency wait time [\#584](https://github.com/networktocode/ntc-templates/pull/584) ([msom](https://github.com/msom))

**Closed issues:**

- cisco\_nxos\_show\_vlan does not show ports, thank god cisco\_ios\_show\_vlan works [\#601](https://github.com/networktocode/ntc-templates/issues/601)
- regex to match whitespace, words, or mix of both, and cut off trailing whitespace? [\#566](https://github.com/networktocode/ntc-templates/issues/566)
- Bug: Alcatel SROS show service id index issue [\#556](https://github.com/networktocode/ntc-templates/issues/556)
- Cisco IOS Show MAC Address-Table Errors on Last Line [\#544](https://github.com/networktocode/ntc-templates/issues/544)
- Cisco IOS Show Run Template [\#469](https://github.com/networktocode/ntc-templates/issues/469)
- show ip route IOS vs NXOS [\#382](https://github.com/networktocode/ntc-templates/issues/382)
- Add tests for index file to Travis [\#207](https://github.com/networktocode/ntc-templates/issues/207)
- Using the .textfsm extension for templates [\#171](https://github.com/networktocode/ntc-templates/issues/171)

**Merged pull requests:**

- Bumping version to 1.4.0 [\#616](https://github.com/networktocode/ntc-templates/pull/616) ([FragmentedPacket](https://github.com/FragmentedPacket))
- Documentation: Update changelog for 1.4.0 release [\#615](https://github.com/networktocode/ntc-templates/pull/615) ([FragmentedPacket](https://github.com/FragmentedPacket))
- Added line to get the port mode of an interface [\#611](https://github.com/networktocode/ntc-templates/pull/611) ([daanvdsanden](https://github.com/daanvdsanden))
- update show arp for aruba\_os [\#610](https://github.com/networktocode/ntc-templates/pull/610) ([dmwcode](https://github.com/dmwcode))
- New Template: hp comware show ip interface [\#609](https://github.com/networktocode/ntc-templates/pull/609) ([sliddjur](https://github.com/sliddjur))
- New Template: cisco\_ios\_show\_ip\_ospf\_database\_router [\#606](https://github.com/networktocode/ntc-templates/pull/606) ([ChristopherJHart](https://github.com/ChristopherJHart))
- New Template: cisco\_s300\_show\_version [\#605](https://github.com/networktocode/ntc-templates/pull/605) ([wdennis](https://github.com/wdennis))
- Enhancements: IOS show ip access-list [\#603](https://github.com/networktocode/ntc-templates/pull/603) ([jpobeda](https://github.com/jpobeda))
- Cisco nxos show vrf interface [\#602](https://github.com/networktocode/ntc-templates/pull/602) ([JoeyG1973](https://github.com/JoeyG1973))
- New Template Show Mpls interface [\#600](https://github.com/networktocode/ntc-templates/pull/600) ([alekgozali](https://github.com/alekgozali))
- New Template : Show Etherchannel Summary [\#599](https://github.com/networktocode/ntc-templates/pull/599) ([alekgozali](https://github.com/alekgozali))
- Fixes for cisco\_ios\_show\_running-config\_partition\_access-list template [\#598](https://github.com/networktocode/ntc-templates/pull/598) ([jpobeda](https://github.com/jpobeda))
- add huawei vrp display version [\#597](https://github.com/networktocode/ntc-templates/pull/597) ([lutfisan](https://github.com/lutfisan))
- Cisco XR - admin show environment power - template [\#596](https://github.com/networktocode/ntc-templates/pull/596) ([hijm](https://github.com/hijm))
- Added Checkpoint GAIA show arp dynamic all template [\#595](https://github.com/networktocode/ntc-templates/pull/595) ([dys152](https://github.com/dys152))
- add show arp for aruba\_os [\#594](https://github.com/networktocode/ntc-templates/pull/594) ([dmwcode](https://github.com/dmwcode))
- New Template - CISCO IOS - Show Module [\#593](https://github.com/networktocode/ntc-templates/pull/593) ([alekgozali](https://github.com/alekgozali))
- New Template: cisco\_nxos\_show\_vdc.textfsm [\#591](https://github.com/networktocode/ntc-templates/pull/591) ([FragmentedPacket](https://github.com/FragmentedPacket))
- New Template: cisco\_ios\_show\_ip\_bgp\_neighbors.textfsm [\#590](https://github.com/networktocode/ntc-templates/pull/590) ([FragmentedPacket](https://github.com/FragmentedPacket))
- BugFix: arista\_eos\_show\_ip\_route: added new vrf format and secondary route catch [\#589](https://github.com/networktocode/ntc-templates/pull/589) ([FragmentedPacket](https://github.com/FragmentedPacket))
- Bug Fix: Cisco IOS show interfaces switchport [\#587](https://github.com/networktocode/ntc-templates/pull/587) ([kwrobert](https://github.com/kwrobert))
- Bug Fix: Cisco IOS show mac address-table [\#585](https://github.com/networktocode/ntc-templates/pull/585) ([kwrobert](https://github.com/kwrobert))
- Jschulman cisco nxos allow missing transceiver type [\#582](https://github.com/networktocode/ntc-templates/pull/582) ([jeremyschulman](https://github.com/jeremyschulman))
- New Template: Cisco WLC show wlan summary [\#581](https://github.com/networktocode/ntc-templates/pull/581) ([FragmentedPacket](https://github.com/FragmentedPacket))
- New Template Pull Request - cisco\_xr\_show\_interfaces\_summary [\#580](https://github.com/networktocode/ntc-templates/pull/580) ([hijm](https://github.com/hijm))
- New Templates: Fortinet get system interface and status [\#578](https://github.com/networktocode/ntc-templates/pull/578) ([FragmentedPacket](https://github.com/FragmentedPacket))
- Bug Fix for cisco ios show mac address-table parser [\#577](https://github.com/networktocode/ntc-templates/pull/577) ([kwrobert](https://github.com/kwrobert))
- New Templat: Huawei display lldp neighbor [\#576](https://github.com/networktocode/ntc-templates/pull/576) ([FragmentedPacket](https://github.com/FragmentedPacket))
- BugFix: NXOS show version - Add n5k platform regex [\#575](https://github.com/networktocode/ntc-templates/pull/575) ([FragmentedPacket](https://github.com/FragmentedPacket))
- Bug Fix: ASA Show failover - Account for new data [\#574](https://github.com/networktocode/ntc-templates/pull/574) ([FragmentedPacket](https://github.com/FragmentedPacket))
- New Template: Show arp - ASA [\#573](https://github.com/networktocode/ntc-templates/pull/573) ([FragmentedPacket](https://github.com/FragmentedPacket))
- Add SERIAL to Cisco IOS LLDP Neighbors Detail [\#572](https://github.com/networktocode/ntc-templates/pull/572) ([FragmentedPacket](https://github.com/FragmentedPacket))
- New Template: Cisco XR - show arp [\#567](https://github.com/networktocode/ntc-templates/pull/567) ([migueloangelo](https://github.com/migueloangelo))
- cisco\_ios\_show\_license - avoid trailing white spaces [\#565](https://github.com/networktocode/ntc-templates/pull/565) ([migueloangelo](https://github.com/migueloangelo))
- New Template for Cisco NXOS - show\_interface\_transceiver [\#564](https://github.com/networktocode/ntc-templates/pull/564) ([dgarros](https://github.com/dgarros))
- Enhancement: IOS show int switchport - Add ADMIN\_MODE Group [\#563](https://github.com/networktocode/ntc-templates/pull/563) ([jmcgill298](https://github.com/jmcgill298))
- Cisco ASA Show Logging Template [\#562](https://github.com/networktocode/ntc-templates/pull/562) ([afoster213](https://github.com/afoster213))
- New Template for Cisco IOS Log Messages [\#554](https://github.com/networktocode/ntc-templates/pull/554) ([afoster213](https://github.com/afoster213))
- Cleanup some testing [\#551](https://github.com/networktocode/ntc-templates/pull/551) ([FragmentedPacket](https://github.com/FragmentedPacket))
- Fixes \#544: Added new parsed sample based on 3750G 15.0\(2\)SE11 code, … [\#548](https://github.com/networktocode/ntc-templates/pull/548) ([jvanderaa](https://github.com/jvanderaa))
- PYTHON FORMATTING: Add Black to tox file [\#407](https://github.com/networktocode/ntc-templates/pull/407) ([jmcgill298](https://github.com/jmcgill298))

## [v1.3.0](https://github.com/networktocode/ntc-templates/tree/v1.3.0) (2019-11-18)

[Full Changelog](https://github.com/networktocode/ntc-templates/compare/v1.2.1...v1.3.0)

**Implemented enhancements:**

- cisco\_ios\_show\_standby\_brief.template support for interfaces and output in two lines [\#483](https://github.com/networktocode/ntc-templates/issues/483)
- New template cisco\_ios\_show\_snmp\_user.template [\#390](https://github.com/networktocode/ntc-templates/issues/390)
- added last\_link\_flapped to nxos\_show\_interface [\#531](https://github.com/networktocode/ntc-templates/pull/531) ([aSauerwein](https://github.com/aSauerwein))
- Adding Values for route-map names fetch for nxos\_sh\_ip\_bgp\_nei [\#481](https://github.com/networktocode/ntc-templates/pull/481) ([nnaukwal](https://github.com/nnaukwal))
- Added BGP up/down time to sh ip bgp summary [\#476](https://github.com/networktocode/ntc-templates/pull/476) ([corvese](https://github.com/corvese))
- Update cisco\_ios\_show\_ip\_eigrp\_topology.template [\#445](https://github.com/networktocode/ntc-templates/pull/445) ([thomasbridge74](https://github.com/thomasbridge74))
- Cisco wlc template [\#391](https://github.com/networktocode/ntc-templates/pull/391) ([hisaza](https://github.com/hisaza))
- Cisco xr show route vrf all [\#378](https://github.com/networktocode/ntc-templates/pull/378) ([Warsenius](https://github.com/Warsenius))

**Fixed bugs:**

- cisco\_ios\_show\_interfaces\_switchport.template broken [\#537](https://github.com/networktocode/ntc-templates/issues/537)
- "Cisco IOS show authentication session" issue when session count exceeds ~10 [\#473](https://github.com/networktocode/ntc-templates/issues/473)
- cisco\_ios\_show\_ip\_interface.template does not deal with peer address on virtual-access interface [\#461](https://github.com/networktocode/ntc-templates/issues/461)
- arista\_eos\_show\_interfaces\_status.template does not deal with disabled ports properly [\#460](https://github.com/networktocode/ntc-templates/issues/460)
- cisco\_ios\_show\_ip\_eigrp\_topology.template does not deal with redistributed routes. [\#459](https://github.com/networktocode/ntc-templates/issues/459)
- Cisco ASA - show failover error [\#424](https://github.com/networktocode/ntc-templates/issues/424)
- wrong info returned when not space between interface name and number from show cdp neighbor [\#415](https://github.com/networktocode/ntc-templates/issues/415)
- show\_mac\_address-table - Output contains single dictionary [\#385](https://github.com/networktocode/ntc-templates/issues/385)
- Fix netflow and wccp lines [\#494](https://github.com/networktocode/ntc-templates/pull/494) ([targuan](https://github.com/targuan))
- Fix mac address table [\#485](https://github.com/networktocode/ntc-templates/pull/485) ([FragmentedPacket](https://github.com/FragmentedPacket))
- Issue 415 cdp [\#480](https://github.com/networktocode/ntc-templates/pull/480) ([mullaneywt](https://github.com/mullaneywt))
- Issue 472 patch [\#479](https://github.com/networktocode/ntc-templates/pull/479) ([mullaneywt](https://github.com/mullaneywt))
- fixed ports [\#471](https://github.com/networktocode/ntc-templates/pull/471) ([dainok](https://github.com/dainok))
- Fixes \#424: Cisco ASA - show failover error. [\#465](https://github.com/networktocode/ntc-templates/pull/465) ([deesel](https://github.com/deesel))
- Issue \#384 cisco\_asa\_show\_route - Fix uptime issue [\#401](https://github.com/networktocode/ntc-templates/pull/401) ([brandomando](https://github.com/brandomando))

**Closed issues:**

- cisco\_asa bug in 9.10.1.22 causes `show inventory` template to fail [\#498](https://github.com/networktocode/ntc-templates/issues/498)
- Cisco IOS LLDP [\#484](https://github.com/networktocode/ntc-templates/issues/484)
- cisco\_nxos\_show\_interface\_brief does not deal with pvlan and fabric interfaces  [\#472](https://github.com/networktocode/ntc-templates/issues/472)
- cisco\_ios\_show\_lldp\_neighbors\_detail failing when last neighbor includes" MED information" section [\#444](https://github.com/networktocode/ntc-templates/issues/444)
- New Template: cisco\_ios\_show\_license [\#440](https://github.com/networktocode/ntc-templates/issues/440)
- nxos\_show\_interface\_status\_template error [\#420](https://github.com/networktocode/ntc-templates/issues/420)
- README Documentation missing setup information [\#411](https://github.com/networktocode/ntc-templates/issues/411)
- Arista and show int status [\#410](https://github.com/networktocode/ntc-templates/issues/410)
- Cisco ASA show route template error [\#384](https://github.com/networktocode/ntc-templates/issues/384)
- Build is failing in Travis CI [\#240](https://github.com/networktocode/ntc-templates/issues/240)

**Merged pull requests:**

- Update CHANGELOG and bump version [\#542](https://github.com/networktocode/ntc-templates/pull/542) ([jmcgill298](https://github.com/jmcgill298))
- Update state transitions to provide more consistency across platforms [\#541](https://github.com/networktocode/ntc-templates/pull/541) ([jmcgill298](https://github.com/jmcgill298))
- cisco\_ios\_show\_environment\_temperature.template, iOS, show environment temperature [\#540](https://github.com/networktocode/ntc-templates/pull/540) ([bobbytayar](https://github.com/bobbytayar))
- show interface summary [\#539](https://github.com/networktocode/ntc-templates/pull/539) ([timjsmith24](https://github.com/timjsmith24))
- Fixes 537 - IOS show interfaces switchport - Changed output [\#538](https://github.com/networktocode/ntc-templates/pull/538) ([FragmentedPacket](https://github.com/FragmentedPacket))
- Issue 440 [\#533](https://github.com/networktocode/ntc-templates/pull/533) ([FragmentedPacket](https://github.com/FragmentedPacket))
- Show snmp user [\#532](https://github.com/networktocode/ntc-templates/pull/532) ([FragmentedPacket](https://github.com/FragmentedPacket))
- Enhancement - fortinet - get router info bgp summary [\#529](https://github.com/networktocode/ntc-templates/pull/529) ([corvese](https://github.com/corvese))
- Enhancement: Update templates to record on new entry [\#528](https://github.com/networktocode/ntc-templates/pull/528) ([jmcgill298](https://github.com/jmcgill298))
- Cisco voice vlan [\#527](https://github.com/networktocode/ntc-templates/pull/527) ([ThreeFDDI](https://github.com/ThreeFDDI))
- Adv 802dot11 channel [\#526](https://github.com/networktocode/ntc-templates/pull/526) ([timjsmith24](https://github.com/timjsmith24))
- BugFix: IOS - Add capturing of timestamp data for vty lines that auto print one [\#525](https://github.com/networktocode/ntc-templates/pull/525) ([jmcgill298](https://github.com/jmcgill298))
- New Template - EOS - show vrf [\#524](https://github.com/networktocode/ntc-templates/pull/524) ([jmcgill298](https://github.com/jmcgill298))
- Enhancement - IOS - show mac-address - add data validation and tests [\#523](https://github.com/networktocode/ntc-templates/pull/523) ([jmcgill298](https://github.com/jmcgill298))
- Enhancement - EOS - Allow show bgp summary to be used for show bgp evpn summary [\#522](https://github.com/networktocode/ntc-templates/pull/522) ([jmcgill298](https://github.com/jmcgill298))
- Enhancement - EOS|NXOS - sh ip route add capturing of VRF [\#521](https://github.com/networktocode/ntc-templates/pull/521) ([jmcgill298](https://github.com/jmcgill298))
- Enhancement: IOS|EOS - show bgp summ - Account for VRF syntax [\#520](https://github.com/networktocode/ntc-templates/pull/520) ([jmcgill298](https://github.com/jmcgill298))
- BugFix: XR - show version - account for CRS output [\#519](https://github.com/networktocode/ntc-templates/pull/519) ([jmcgill298](https://github.com/jmcgill298))
- New Template - Ciena - software show [\#518](https://github.com/networktocode/ntc-templates/pull/518) ([jmcgill298](https://github.com/jmcgill298))
- BugFix: EOS - show bgp summ - match RID/AS more precisely [\#517](https://github.com/networktocode/ntc-templates/pull/517) ([jmcgill298](https://github.com/jmcgill298))
- BugFix: IOS - show ip int - account for serial intfs [\#516](https://github.com/networktocode/ntc-templates/pull/516) ([jmcgill298](https://github.com/jmcgill298))
- New Template: WLC - show inventory [\#515](https://github.com/networktocode/ntc-templates/pull/515) ([jmcgill298](https://github.com/jmcgill298))
- New Template - IOS - show process memory sorted [\#514](https://github.com/networktocode/ntc-templates/pull/514) ([jmcgill298](https://github.com/jmcgill298))
- New Template: WLC - show rf profile-summary [\#513](https://github.com/networktocode/ntc-templates/pull/513) ([jmcgill298](https://github.com/jmcgill298))
- New Templates - Huawei VRP - display interface and display temp [\#512](https://github.com/networktocode/ntc-templates/pull/512) ([jmcgill298](https://github.com/jmcgill298))
- New Template: WLC - show 802.11 cleanair config [\#510](https://github.com/networktocode/ntc-templates/pull/510) ([jmcgill298](https://github.com/jmcgill298))
- BugFix: WLC 80211 - Add missing EoL to matching empty lines [\#508](https://github.com/networktocode/ntc-templates/pull/508) ([jmcgill298](https://github.com/jmcgill298))
- cisco nxos bgp neighbor defect fix [\#505](https://github.com/networktocode/ntc-templates/pull/505) ([nnaukwal](https://github.com/nnaukwal))
- BugFix: IOS show standby brief - support multiline output [\#503](https://github.com/networktocode/ntc-templates/pull/503) ([jmcgill298](https://github.com/jmcgill298))
- Cisco WLC Command - Show 802 11a|b [\#501](https://github.com/networktocode/ntc-templates/pull/501) ([timjsmith24](https://github.com/timjsmith24))
- Fixes498 - Cisco ASA with Extra Output in `show inventory` [\#499](https://github.com/networktocode/ntc-templates/pull/499) ([jvanderaa](https://github.com/jvanderaa))
- Enhancement: ASA - Convert show version serial to list [\#497](https://github.com/networktocode/ntc-templates/pull/497) ([jmcgill298](https://github.com/jmcgill298))
- Add arista eos show ip helper [\#496](https://github.com/networktocode/ntc-templates/pull/496) ([targuan](https://github.com/targuan))
- Fix \#461 [\#495](https://github.com/networktocode/ntc-templates/pull/495) ([FragmentedPacket](https://github.com/FragmentedPacket))
- Add ruckus\_fastiron show arp template [\#493](https://github.com/networktocode/ntc-templates/pull/493) ([QuasarKid](https://github.com/QuasarKid))
- New Template: cisco\_xr\_show\_ipv6\_neighbors [\#492](https://github.com/networktocode/ntc-templates/pull/492) ([charlesmonson](https://github.com/charlesmonson))
- Switch detail [\#491](https://github.com/networktocode/ntc-templates/pull/491) ([jmcgill298](https://github.com/jmcgill298))
- Cisco NXoS template for "show forwarding ipv4 route" [\#489](https://github.com/networktocode/ntc-templates/pull/489) ([nnaukwal](https://github.com/nnaukwal))
- Fix \#460 [\#488](https://github.com/networktocode/ntc-templates/pull/488) ([targuan](https://github.com/targuan))
- Add test case for 3650/3850 output [\#487](https://github.com/networktocode/ntc-templates/pull/487) ([targuan](https://github.com/targuan))
- nxos - Template for show route-map command [\#486](https://github.com/networktocode/ntc-templates/pull/486) ([nnaukwal](https://github.com/nnaukwal))
- Cisco XR admin show inventory [\#482](https://github.com/networktocode/ntc-templates/pull/482) ([charlesmonson](https://github.com/charlesmonson))
- Add template cisco\_nxos\_show\_ip\_interface\_brief [\#478](https://github.com/networktocode/ntc-templates/pull/478) ([mullaneywt](https://github.com/mullaneywt))
- BugFix: allow various time formats for ip mroute [\#474](https://github.com/networktocode/ntc-templates/pull/474) ([jmcgill298](https://github.com/jmcgill298))
- template for show arp in watchguard [\#468](https://github.com/networktocode/ntc-templates/pull/468) ([dainok](https://github.com/dainok))
- Paloalto panos arp fix [\#466](https://github.com/networktocode/ntc-templates/pull/466) ([dainok](https://github.com/dainok))
- HP Comware `display counters \(inbound|outbound\) interface` [\#464](https://github.com/networktocode/ntc-templates/pull/464) ([ad8-bdl](https://github.com/ad8-bdl))
- ASA show asp drop changes [\#446](https://github.com/networktocode/ntc-templates/pull/446) ([vaneuk](https://github.com/vaneuk))
- add cisco\_wlc\_ssh\_show\_exclusionlist [\#425](https://github.com/networktocode/ntc-templates/pull/425) ([ancker010](https://github.com/ancker010))
- fix: show ip bgp examples appear to be swapped [\#421](https://github.com/networktocode/ntc-templates/pull/421) ([cmccormack](https://github.com/cmccormack))
- Bugfix: asa\_dir template to account for change in raw output [\#419](https://github.com/networktocode/ntc-templates/pull/419) ([FragmentedPacket](https://github.com/FragmentedPacket))

## [v1.2.1](https://github.com/networktocode/ntc-templates/tree/v1.2.1) (2019-09-26)

[Full Changelog](https://github.com/networktocode/ntc-templates/compare/v1.2.0...v1.2.1)

## [v1.2.0](https://github.com/networktocode/ntc-templates/tree/v1.2.0) (2019-09-26)

[Full Changelog](https://github.com/networktocode/ntc-templates/compare/v1.1.1...v1.2.0)

**Implemented enhancements:**

- FileNotFoundError on Windows 10 [\#455](https://github.com/networktocode/ntc-templates/issues/455)
- Cisco ASA - Missing capture of Software Compile Date [\#387](https://github.com/networktocode/ntc-templates/issues/387)

**Merged pull requests:**

- Updates as requested [\#470](https://github.com/networktocode/ntc-templates/pull/470) ([jvanderaa](https://github.com/jvanderaa))
- Remove extraneous \(duplicate\) test [\#463](https://github.com/networktocode/ntc-templates/pull/463) ([ad8-bdl](https://github.com/ad8-bdl))
- Support for locating templates when installing local directory on Windows - Fixes \#455 [\#456](https://github.com/networktocode/ntc-templates/pull/456) ([jmcgill298](https://github.com/jmcgill298))
- Update cisco\_xr\_show\_version.template [\#442](https://github.com/networktocode/ntc-templates/pull/442) ([mspiez](https://github.com/mspiez))
- Cisco xr show interfaces duplex and mac for bundle ethernet [\#389](https://github.com/networktocode/ntc-templates/pull/389) ([Warsenius](https://github.com/Warsenius))

## [v1.1.1](https://github.com/networktocode/ntc-templates/tree/v1.1.1) (2019-08-08)

[Full Changelog](https://github.com/networktocode/ntc-templates/compare/0.9.0...v1.1.1)

**Implemented enhancements:**

- cisco\_ios\_show\_version.template Add Licensing [\#256](https://github.com/networktocode/ntc-templates/issues/256)
- Adding cisco\_ios\_show\_ip\_interface [\#322](https://github.com/networktocode/ntc-templates/pull/322) ([vladola](https://github.com/vladola))
- Packaging [\#288](https://github.com/networktocode/ntc-templates/pull/288) ([micahculpepper](https://github.com/micahculpepper))

**Fixed bugs:**

- nxos show interface status issue [\#426](https://github.com/networktocode/ntc-templates/issues/426)
- CISCO\_XR\_SH\_INTF: Parsed file shows that not all interfaces in raw are being parsed/recorded [\#282](https://github.com/networktocode/ntc-templates/issues/282)
- Test files for aruba os need renamed. [\#224](https://github.com/networktocode/ntc-templates/issues/224)

**Closed issues:**

- show\_lldp\_neighbors.template failing when switch + domain name is \> 19 characters [\#375](https://github.com/networktocode/ntc-templates/issues/375)
- cisco\_ios\_show\_lldp\_neighbor\_detail failing when `Physical media capabilities` are `Other/unknown` [\#374](https://github.com/networktocode/ntc-templates/issues/374)
- Master branch fails tox tests [\#361](https://github.com/networktocode/ntc-templates/issues/361)
- cisco\_nxos\_show\_interface\_status.template [\#333](https://github.com/networktocode/ntc-templates/issues/333)
- cisco\_nxos\_show\_interface\_status.template: error on 10G and 40G interfaces [\#331](https://github.com/networktocode/ntc-templates/issues/331)
- cisco\_ios\_show\_vlan.template not recorded complete list of interfaces [\#328](https://github.com/networktocode/ntc-templates/issues/328)
- Problem with parsing ASA ACL [\#287](https://github.com/networktocode/ntc-templates/issues/287)
- New Template Request [\#286](https://github.com/networktocode/ntc-templates/issues/286)
- cisco\_xr\_show\_interfaces.template line 4 regex incorrect [\#280](https://github.com/networktocode/ntc-templates/issues/280)
- cisco\_xr\_show\_cdp\_neighbors\_detail.template shows remote and local interface incorrectly [\#277](https://github.com/networktocode/ntc-templates/issues/277)
- Multiple Failing Use Cases in Cisco IOS ACL Template [\#245](https://github.com/networktocode/ntc-templates/issues/245)
- cisco\_asa\_show\_vpn-sessiondb\_detail\_l2l.template not parsing [\#231](https://github.com/networktocode/ntc-templates/issues/231)
- show interface status for cisco\_nxos returns incorrect 'name' and 'port' objects if there are spaces in the description. [\#196](https://github.com/networktocode/ntc-templates/issues/196)
- cisco\_xr\_show\_ip\_route uptime format and protocol sub-type support [\#185](https://github.com/networktocode/ntc-templates/issues/185)

**Merged pull requests:**

- Update readme [\#452](https://github.com/networktocode/ntc-templates/pull/452) ([jmcgill298](https://github.com/jmcgill298))
- Fix spacing new templates [\#443](https://github.com/networktocode/ntc-templates/pull/443) ([FragmentedPacket](https://github.com/FragmentedPacket))
- Fixes \#224 Updating aurba test file names to match folder/file naming pattern [\#439](https://github.com/networktocode/ntc-templates/pull/439) ([myyellowshoe](https://github.com/myyellowshoe))
- add Cisco IOS XR 'show ip interface brief' command [\#438](https://github.com/networktocode/ntc-templates/pull/438) ([dampfhamm3r](https://github.com/dampfhamm3r))
- Cisco nxos show interfaces switchport [\#434](https://github.com/networktocode/ntc-templates/pull/434) ([dainok](https://github.com/dainok))
- Cisco ios show interfaces switchport [\#433](https://github.com/networktocode/ntc-templates/pull/433) ([dainok](https://github.com/dainok))
- Paloalto panos show arp all [\#432](https://github.com/networktocode/ntc-templates/pull/432) ([dainok](https://github.com/dainok))
- Paloalto panos show mac all [\#431](https://github.com/networktocode/ntc-templates/pull/431) ([dainok](https://github.com/dainok))
- Hp procurve show mac address [\#430](https://github.com/networktocode/ntc-templates/pull/430) ([dainok](https://github.com/dainok))
- New template cisco\_ios\_show\_snmp\_user.template [\#429](https://github.com/networktocode/ntc-templates/pull/429) ([jifox](https://github.com/jifox))
- nxos\_show\_interface\_status: Allows capture of Fabric Exte type  [\#427](https://github.com/networktocode/ntc-templates/pull/427) ([FragmentedPacket](https://github.com/FragmentedPacket))
- Tests [\#402](https://github.com/networktocode/ntc-templates/pull/402) ([jmcgill298](https://github.com/jmcgill298))
- Feature/improve cisco ios show vrf [\#395](https://github.com/networktocode/ntc-templates/pull/395) ([MatthiasGabriel](https://github.com/MatthiasGabriel))
- Feature/cisco ios show hosts [\#394](https://github.com/networktocode/ntc-templates/pull/394) ([MatthiasGabriel](https://github.com/MatthiasGabriel))
- cisco\_nxos\_show\_version extension for pulling PLATFORM from N9K [\#393](https://github.com/networktocode/ntc-templates/pull/393) ([jonesbra](https://github.com/jonesbra))
- Cisco IOS - show dmvpn - New template [\#392](https://github.com/networktocode/ntc-templates/pull/392) ([adrydale](https://github.com/adrydale))
- updated template to catch NSR N/A state [\#381](https://github.com/networktocode/ntc-templates/pull/381) ([Warsenius](https://github.com/Warsenius))
- show ospf neighbor NEIGHBOR\_UPTIME no match when output in 1w2d format [\#380](https://github.com/networktocode/ntc-templates/pull/380) ([Warsenius](https://github.com/Warsenius))
- Fixes 374 - Adds example of Other/unknown media on LLDP for a device … [\#377](https://github.com/networktocode/ntc-templates/pull/377) ([jvanderaa](https://github.com/jvanderaa))
- Updated the template to get first 20 chars on LLDP neighbor for case … [\#376](https://github.com/networktocode/ntc-templates/pull/376) ([jvanderaa](https://github.com/jvanderaa))
- add Cisco IOS show ip flow toptalkers [\#373](https://github.com/networktocode/ntc-templates/pull/373) ([lscarmic](https://github.com/lscarmic))
- Updated LLDP Neighbor Detail for matching on some devices that were missing. [\#372](https://github.com/networktocode/ntc-templates/pull/372) ([jvanderaa](https://github.com/jvanderaa))
- Add show\_boot template for cisco\_ios [\#371](https://github.com/networktocode/ntc-templates/pull/371) ([FragmentedPacket](https://github.com/FragmentedPacket))
- Update cisco\_nxos\_show\_interface\_status.template [\#370](https://github.com/networktocode/ntc-templates/pull/370) ([Pluppo](https://github.com/Pluppo))
- IOS SHOW INTERFACES : adding regexes for skipped values & parsed results [\#368](https://github.com/networktocode/ntc-templates/pull/368) ([lachlanjholmes](https://github.com/lachlanjholmes))
-  Add Cisco IOS show ipv6 neighbors  [\#363](https://github.com/networktocode/ntc-templates/pull/363) ([kimoldfield](https://github.com/kimoldfield))
-  XR SHOW LPTS PIFIB HARDWARE POLICE LOCATION: Add new template [\#360](https://github.com/networktocode/ntc-templates/pull/360) ([jmcgill298](https://github.com/jmcgill298))
- XR SHOW DROPS NP ALL: Add new template [\#359](https://github.com/networktocode/ntc-templates/pull/359) ([jmcgill298](https://github.com/jmcgill298))
- XR SHOW CONTROLLERS FABRIC FIA ERRORS INGRESS: Add new template [\#358](https://github.com/networktocode/ntc-templates/pull/358) ([jmcgill298](https://github.com/jmcgill298))
- XR SHOW CONTROLLERS FABRIC FIA ERRORS EGRESS: Add new template [\#357](https://github.com/networktocode/ntc-templates/pull/357) ([jmcgill298](https://github.com/jmcgill298))
- XR SHOW CONTROLLERS FABRIC FIA DROPS INGRESS: Add new template [\#356](https://github.com/networktocode/ntc-templates/pull/356) ([jmcgill298](https://github.com/jmcgill298))
- XR SHOW CONTROLLERS FABRIC FIA DROPS EGRESS: Add new template [\#355](https://github.com/networktocode/ntc-templates/pull/355) ([jmcgill298](https://github.com/jmcgill298))
- CISCO XR SHOW CEF DROPS LOCATION: Add new template [\#354](https://github.com/networktocode/ntc-templates/pull/354) ([jmcgill298](https://github.com/jmcgill298))
- XR SHOW ASIC ERRORS: Add new template [\#353](https://github.com/networktocode/ntc-templates/pull/353) ([jmcgill298](https://github.com/jmcgill298))
- XR SHOW BGP: Add new template [\#351](https://github.com/networktocode/ntc-templates/pull/351) ([jmcgill298](https://github.com/jmcgill298))
- XR SHOW HSRP: Add new template [\#350](https://github.com/networktocode/ntc-templates/pull/350) ([jmcgill298](https://github.com/jmcgill298))
- XR SHOW CONTROLLERS: Bug Fix [\#349](https://github.com/networktocode/ntc-templates/pull/349) ([jmcgill298](https://github.com/jmcgill298))
- Create cisco\_ios\_show\_interfaces\_description.template [\#348](https://github.com/networktocode/ntc-templates/pull/348) ([adrydale](https://github.com/adrydale))
- Aos vlan [\#345](https://github.com/networktocode/ntc-templates/pull/345) ([jmcgill298](https://github.com/jmcgill298))
- Tacacs cisco [\#344](https://github.com/networktocode/ntc-templates/pull/344) ([jmcgill298](https://github.com/jmcgill298))
- EOS SHOW MODULE: Add new template [\#343](https://github.com/networktocode/ntc-templates/pull/343) ([jmcgill298](https://github.com/jmcgill298))
- Patch 2 [\#342](https://github.com/networktocode/ntc-templates/pull/342) ([jmcgill298](https://github.com/jmcgill298))
- CISCO XR SHOW BGP NEIGH: Add new template [\#341](https://github.com/networktocode/ntc-templates/pull/341) ([jmcgill298](https://github.com/jmcgill298))
- cisco\_ios\_show\_ip\_bgp: Fix whitespace change in command output [\#340](https://github.com/networktocode/ntc-templates/pull/340) ([paneu](https://github.com/paneu))
- CISCO\_ASA\_SHOW\_LICENSE\_ALL: Add new template [\#339](https://github.com/networktocode/ntc-templates/pull/339) ([jmcgill298](https://github.com/jmcgill298))
- CISCO\_ASA\_SHOW\_ASP\_DROP: Add new template [\#338](https://github.com/networktocode/ntc-templates/pull/338) ([jmcgill298](https://github.com/jmcgill298))
- `ASA INTERFACE DETAIL`: Add new template [\#337](https://github.com/networktocode/ntc-templates/pull/337) ([jmcgill298](https://github.com/jmcgill298))
- `NETIRON SHOW RUN INTF`: Broaden template scope [\#336](https://github.com/networktocode/ntc-templates/pull/336) ([jmcgill298](https://github.com/jmcgill298))
- checkpoint\_gaia\_show\_ntp\_servers: Add new template [\#335](https://github.com/networktocode/ntc-templates/pull/335) ([JCapretta](https://github.com/JCapretta))
- `cisco\_nxos\_show\_interface\_status`: Fixes issue \#333 [\#334](https://github.com/networktocode/ntc-templates/pull/334) ([JCapretta](https://github.com/JCapretta))
- `cisco\_nxos\_show\_interface\_status`: Fixes issue \#331 [\#332](https://github.com/networktocode/ntc-templates/pull/332) ([JCapretta](https://github.com/JCapretta))
- Checkpoint gaia show dns.template [\#330](https://github.com/networktocode/ntc-templates/pull/330) ([JCapretta](https://github.com/JCapretta))
- Modified cisco\_ios\_show\_vlan.template \(\#328\) [\#329](https://github.com/networktocode/ntc-templates/pull/329) ([JCapretta](https://github.com/JCapretta))
- cisco ios show ip interface: Incorporate \#229 into \#322 [\#326](https://github.com/networktocode/ntc-templates/pull/326) ([jmcgill298](https://github.com/jmcgill298))
- ASA SHOW RESOURCE: Add new template [\#325](https://github.com/networktocode/ntc-templates/pull/325) ([jmcgill298](https://github.com/jmcgill298))
- ASA VPN-SESSIONDB: Bug Fixes with new data [\#323](https://github.com/networktocode/ntc-templates/pull/323) ([jmcgill298](https://github.com/jmcgill298))
- IOS DIR: Account for spaces in permissions [\#321](https://github.com/networktocode/ntc-templates/pull/321) ([jmcgill298](https://github.com/jmcgill298))
- NX-OS show l2rib internal permanently-frozen-list template [\#320](https://github.com/networktocode/ntc-templates/pull/320) ([vaneuk](https://github.com/vaneuk))
- Bugfix: cisco asa show access list [\#313](https://github.com/networktocode/ntc-templates/pull/313) ([joewesch](https://github.com/joewesch))
- Adding cisco\_asa\_show\_nat [\#312](https://github.com/networktocode/ntc-templates/pull/312) ([joewesch](https://github.com/joewesch))
- cisco\_ios\_show\_dot1x\_all command [\#308](https://github.com/networktocode/ntc-templates/pull/308) ([realvitya](https://github.com/realvitya))
- Add INPUT\_PACKETS, INPUT\_ERRORS, OUTPUT\_PACKETS, OUTPUT\_ERRORS fields to cisco\_ios\_show\_interfaces & cisco\_nxos\_show\_interface templates [\#307](https://github.com/networktocode/ntc-templates/pull/307) ([wvandeun](https://github.com/wvandeun))
- Added cisco\_asa "show running-config object network" template [\#306](https://github.com/networktocode/ntc-templates/pull/306) ([joewesch](https://github.com/joewesch))
- PARSE: Update parse module to account for new and old TextFSM packaging [\#305](https://github.com/networktocode/ntc-templates/pull/305) ([jmcgill298](https://github.com/jmcgill298))
- Modified cisco\_asa\_show\_crypto\_ipsec\_sa [\#304](https://github.com/networktocode/ntc-templates/pull/304) ([joewesch](https://github.com/joewesch))
- Added cisco\_asa\_show\_asp\_table\_vpn-context\_detail [\#303](https://github.com/networktocode/ntc-templates/pull/303) ([joewesch](https://github.com/joewesch))
- Modified cisco\_asa\_show\_object-group\_network.template [\#302](https://github.com/networktocode/ntc-templates/pull/302) ([joewesch](https://github.com/joewesch))
- Adding support for avaya\_ers\_show\_logging\_config command [\#301](https://github.com/networktocode/ntc-templates/pull/301) ([kadecole](https://github.com/kadecole))
- change travis and tox to use textfsm [\#300](https://github.com/networktocode/ntc-templates/pull/300) ([jmcgill298](https://github.com/jmcgill298))
- Change requirements to use `textfsm` instead of `gtextfsm` [\#299](https://github.com/networktocode/ntc-templates/pull/299) ([jmcgill298](https://github.com/jmcgill298))
- added juniper\_junos\_show\_version.template [\#298](https://github.com/networktocode/ntc-templates/pull/298) ([jkraszewski](https://github.com/jkraszewski))
- added juniper\_junos\_show\_chassis\_cluster\_status.template [\#297](https://github.com/networktocode/ntc-templates/pull/297) ([jkraszewski](https://github.com/jkraszewski))
- add juniper\_junos\_show\_chassis\_cluster\_interfaces [\#296](https://github.com/networktocode/ntc-templates/pull/296) ([jkraszewski](https://github.com/jkraszewski))
- added juniper\_junos\_show\_arp\_no-resolve.template [\#295](https://github.com/networktocode/ntc-templates/pull/295) ([jkraszewski](https://github.com/jkraszewski))
- modified cisco\_ios\_show\_ip\_arp.template [\#293](https://github.com/networktocode/ntc-templates/pull/293) ([jkraszewski](https://github.com/jkraszewski))
- added brocade\_fastiron\_show\_mac-address.template [\#292](https://github.com/networktocode/ntc-templates/pull/292) ([jkraszewski](https://github.com/jkraszewski))
- added brocade\_fastiron\_show\_lldp\_neighbors [\#291](https://github.com/networktocode/ntc-templates/pull/291) ([jkraszewski](https://github.com/jkraszewski))
- modified brocade\_fastiron\_show\_interfaces\_brief.template [\#290](https://github.com/networktocode/ntc-templates/pull/290) ([jkraszewski](https://github.com/jkraszewski))
- Brocade fastiron show arp [\#289](https://github.com/networktocode/ntc-templates/pull/289) ([jkraszewski](https://github.com/jkraszewski))
- Add template for "show ip eigrp neighbors" on Cisco IOS [\#285](https://github.com/networktocode/ntc-templates/pull/285) ([Tachashi](https://github.com/Tachashi))
- INDEX UPDATES: Fix filenames to use full command syntax [\#284](https://github.com/networktocode/ntc-templates/pull/284) ([jmcgill298](https://github.com/jmcgill298))
- XR\_SH\_INTF: Update regex to properly capture data - Fixes \#282 [\#283](https://github.com/networktocode/ntc-templates/pull/283) ([jmcgill298](https://github.com/jmcgill298))
- XR\_SHOW\_INTF: Correct capturing of IP Address info - Fixes \#280 [\#281](https://github.com/networktocode/ntc-templates/pull/281) ([jmcgill298](https://github.com/jmcgill298))
- XR\_SH\_CDP: Reverse 'REMOTE\_PORT' and 'LOCAL\_PORT' Groups - Fixes \#277 [\#279](https://github.com/networktocode/ntc-templates/pull/279) ([jmcgill298](https://github.com/jmcgill298))
- CISCO\_ASA\_SH\_FAIL: Update 'SERVICE\_STATE' groups to conform to Cisco'… [\#278](https://github.com/networktocode/ntc-templates/pull/278) ([jmcgill298](https://github.com/jmcgill298))
- Account for  device 'Not Ready' [\#276](https://github.com/networktocode/ntc-templates/pull/276) ([jmcgill298](https://github.com/jmcgill298))
- CISCO ASA SHOW FAILOVER: Update parsers to account for new data [\#275](https://github.com/networktocode/ntc-templates/pull/275) ([jmcgill298](https://github.com/jmcgill298))
- Added template for show ip eigrp topology [\#274](https://github.com/networktocode/ntc-templates/pull/274) ([jmcgill298](https://github.com/jmcgill298))
- Cisco wlc ssh show ap config general [\#273](https://github.com/networktocode/ntc-templates/pull/273) ([jmcgill298](https://github.com/jmcgill298))
-  added show ap summary for Cisco WLC [\#272](https://github.com/networktocode/ntc-templates/pull/272) ([jmcgill298](https://github.com/jmcgill298))
- Add RELOAD\_REASON to Record [\#271](https://github.com/networktocode/ntc-templates/pull/271) ([jmcgill298](https://github.com/jmcgill298))
- Add templates for Vyatta [\#270](https://github.com/networktocode/ntc-templates/pull/270) ([jmcgill298](https://github.com/jmcgill298))
- Add new OS and commands: Ubiquiti edgeswitch: show vlan and show arp support [\#269](https://github.com/networktocode/ntc-templates/pull/269) ([jmcgill298](https://github.com/jmcgill298))
-  Adding support for avaya\_ers\_show\_mlt command  [\#268](https://github.com/networktocode/ntc-templates/pull/268) ([jmcgill298](https://github.com/jmcgill298))
- adding cisco\_xr\_show\_controllers\_hundredgigabitethernet.template [\#267](https://github.com/networktocode/ntc-templates/pull/267) ([jmcgill298](https://github.com/jmcgill298))
- Update Cisco IOS-XR template for `show ip route` command [\#266](https://github.com/networktocode/ntc-templates/pull/266) ([jmcgill298](https://github.com/jmcgill298))
- added template for cisco xr : "admin show environment fan" ,"admin show vm" and "show version" [\#264](https://github.com/networktocode/ntc-templates/pull/264) ([jmcgill298](https://github.com/jmcgill298))
- CISCO IOS SHOW REDUNDANCY: Add new template [\#263](https://github.com/networktocode/ntc-templates/pull/263) ([jmcgill298](https://github.com/jmcgill298))
- CISCO ASA SHOW XLATE: Add new template [\#262](https://github.com/networktocode/ntc-templates/pull/262) ([jmcgill298](https://github.com/jmcgill298))
- CISCO ASA SHOW FAILOVER: Add template for failover status [\#260](https://github.com/networktocode/ntc-templates/pull/260) ([jmcgill298](https://github.com/jmcgill298))
- Add match for empty lines or lines that are only spaces [\#257](https://github.com/networktocode/ntc-templates/pull/257) ([jmcgill298](https://github.com/jmcgill298))
- Updated show inventory to catch space on the name field [\#252](https://github.com/networktocode/ntc-templates/pull/252) ([amb1s1](https://github.com/amb1s1))
- CISCO\_IOS\_SHOW\_IP\_PREFIX-LIST: Add new template [\#251](https://github.com/networktocode/ntc-templates/pull/251) ([jmcgill298](https://github.com/jmcgill298))
- Ios show ip access list [\#250](https://github.com/networktocode/ntc-templates/pull/250) ([jmcgill298](https://github.com/jmcgill298))
- Add support for standard ACL to include matching the 'match counts' [\#249](https://github.com/networktocode/ntc-templates/pull/249) ([jmcgill298](https://github.com/jmcgill298))
- CISCO\_IOS\_SHOW\_IP\_ACCESS-LISTS: Add support for parsing connection st… [\#248](https://github.com/networktocode/ntc-templates/pull/248) ([jmcgill298](https://github.com/jmcgill298))
- FIXES \#245 - CISCO\_IOS\_SHOW\_IP\_ACCESS-LISTS: [\#247](https://github.com/networktocode/ntc-templates/pull/247) ([jmcgill298](https://github.com/jmcgill298))
- CISCO\_IOS\_SHOW\_ROUTE-MAP: Add new template [\#244](https://github.com/networktocode/ntc-templates/pull/244) ([jmcgill298](https://github.com/jmcgill298))
- Cisco asa show inventory [\#243](https://github.com/networktocode/ntc-templates/pull/243) ([amb1s1](https://github.com/amb1s1))
- CISCO\_IOS\_SHOW\_IP\_BGP\_SUMMARY: Add collecting ROUTER\_ID and LOCAL\_AS to parser. [\#242](https://github.com/networktocode/ntc-templates/pull/242) ([jmcgill298](https://github.com/jmcgill298))
- Brocade fastiron show version [\#241](https://github.com/networktocode/ntc-templates/pull/241) ([jmcgill298](https://github.com/jmcgill298))
- Fixed cisco\_ios\_show\_cdp\_neighbors when devices has 4+ capabilities [\#235](https://github.com/networktocode/ntc-templates/pull/235) ([bdowling](https://github.com/bdowling))
- CISCO\_IOS\_SHOW\_RUNNING-CONFIG\_PARTITION\_ROUTE-MAP: Update record stat… [\#233](https://github.com/networktocode/ntc-templates/pull/233) ([jmcgill298](https://github.com/jmcgill298))
- added show running-config partition route-map [\#228](https://github.com/networktocode/ntc-templates/pull/228) ([AutoJunjie](https://github.com/AutoJunjie))
- Update TravisCI to use pypi instead of git clone with Pip [\#226](https://github.com/networktocode/ntc-templates/pull/226) ([jmcgill298](https://github.com/jmcgill298))
- Added/modified show cap/lldp neighbors detail for cisco\*, brocade\*. Added cisco\_ios\_show\_ip\_device\_tracking\_all, cisco\_ios\_show\_ip\_source\_binding [\#225](https://github.com/networktocode/ntc-templates/pull/225) ([hilash](https://github.com/hilash))
- Nxos communit list [\#220](https://github.com/networktocode/ntc-templates/pull/220) ([jmcgill298](https://github.com/jmcgill298))
- Add support for cisco show ip mroute [\#216](https://github.com/networktocode/ntc-templates/pull/216) ([rhoriguchi](https://github.com/rhoriguchi))
- Find MAC addresses in cisco IOS show version. [\#214](https://github.com/networktocode/ntc-templates/pull/214) ([kimoldfield](https://github.com/kimoldfield))
- NXOS\_SHOW\_INTERFACE\_STATUS: Update template to better handle name wit… Fixes \#196 [\#204](https://github.com/networktocode/ntc-templates/pull/204) ([jmcgill298](https://github.com/jmcgill298))
- Adding support for avaya\_ers\_show\_mlt\_all-members command [\#202](https://github.com/networktocode/ntc-templates/pull/202) ([kadecole](https://github.com/kadecole))
- add arista dir flash: [\#187](https://github.com/networktocode/ntc-templates/pull/187) ([ydave](https://github.com/ydave))
- Update the file to support Cap F on output [\#156](https://github.com/networktocode/ntc-templates/pull/156) ([amb1s1](https://github.com/amb1s1))
- update cisco\_nxos\_show\_version to support 5ks [\#154](https://github.com/networktocode/ntc-templates/pull/154) ([amb1s1](https://github.com/amb1s1))

## [0.9.0](https://github.com/networktocode/ntc-templates/tree/0.9.0) (2018-07-05)

[Full Changelog](https://github.com/networktocode/ntc-templates/compare/cc61388f3c6e4543b878e426b30420173d6b6bc4...0.9.0)

**Closed issues:**

- Unable to parse out subinterface information from Cisco IOS content [\#197](https://github.com/networktocode/ntc-templates/issues/197)
- how to use this template can any once give 1 example and its result for more and better understanding  [\#193](https://github.com/networktocode/ntc-templates/issues/193)
- show cdp neighbors for cisco\_ios returns string instead of structured list [\#189](https://github.com/networktocode/ntc-templates/issues/189)
- Template update: cisco\_ios\_show\_vlan to get interface list  [\#175](https://github.com/networktocode/ntc-templates/issues/175)
- python3 support  [\#149](https://github.com/networktocode/ntc-templates/issues/149)
- Template update: cisco\_nxos\_show\_cdp\_neighbors [\#147](https://github.com/networktocode/ntc-templates/issues/147)
- NXOS-Show\_Interfaces not finding Vlan Interfaces when additional interfaces are past the config. Also potential to provide wrong information. [\#135](https://github.com/networktocode/ntc-templates/issues/135)
- hp\_procurve\_show\_vlans.template empty output [\#124](https://github.com/networktocode/ntc-templates/issues/124)
- 'show memory statistics' cisco switch/rotuer template [\#121](https://github.com/networktocode/ntc-templates/issues/121)
- Cisco ASA show version template [\#110](https://github.com/networktocode/ntc-templates/issues/110)
- License question [\#92](https://github.com/networktocode/ntc-templates/issues/92)
- cisco\_ios\_show\_ip\_bgp.template some entries are not parsed [\#87](https://github.com/networktocode/ntc-templates/issues/87)
- missing tests folder for cisco\_ios\_show\_ip\_bgp [\#74](https://github.com/networktocode/ntc-templates/issues/74)
- Issues with trying to use the test-template playbook [\#73](https://github.com/networktocode/ntc-templates/issues/73)
- ios show mac address-table [\#59](https://github.com/networktocode/ntc-templates/issues/59)
- nxos show lldp neighbors failing when there is hostname is long [\#58](https://github.com/networktocode/ntc-templates/issues/58)
- arista route template [\#57](https://github.com/networktocode/ntc-templates/issues/57)
- ios show standby brief active/standby state  [\#52](https://github.com/networktocode/ntc-templates/issues/52)
- Need help on parsing the show platform diag output [\#48](https://github.com/networktocode/ntc-templates/issues/48)
- need a help on escaping the parenthesis  [\#47](https://github.com/networktocode/ntc-templates/issues/47)
- Need an info  [\#46](https://github.com/networktocode/ntc-templates/issues/46)
- Difference between Start and Record Start? [\#41](https://github.com/networktocode/ntc-templates/issues/41)

**Merged pull requests:**

- Cleanup [\#221](https://github.com/networktocode/ntc-templates/pull/221) ([GGabriele](https://github.com/GGabriele))
- Fixed README formatting and typos [\#215](https://github.com/networktocode/ntc-templates/pull/215) ([LindsayHill](https://github.com/LindsayHill))
- Move Record to Interface opening line to ensure each unaccounted for … [\#212](https://github.com/networktocode/ntc-templates/pull/212) ([jmcgill298](https://github.com/jmcgill298))
- CISCO\_IOS\_SHOW\_VLAN: Add support for capturing interfaces associated … [\#210](https://github.com/networktocode/ntc-templates/pull/210) ([jmcgill298](https://github.com/jmcgill298))
- Update with virtual interfaces [\#209](https://github.com/networktocode/ntc-templates/pull/209) ([jvanderaa](https://github.com/jvanderaa))
- NXOS\_SHOW\_CDP\_NEIGHBORS: Add additonal capture groups [\#208](https://github.com/networktocode/ntc-templates/pull/208) ([jmcgill298](https://github.com/jmcgill298))
- IOS\_SHOW\_INTERFACES: Add additional logic to account for sub-interfaces [\#206](https://github.com/networktocode/ntc-templates/pull/206) ([jmcgill298](https://github.com/jmcgill298))
- INDEX: Fix index file out of order [\#205](https://github.com/networktocode/ntc-templates/pull/205) ([jmcgill298](https://github.com/jmcgill298))
- Procurve show vlans [\#201](https://github.com/networktocode/ntc-templates/pull/201) ([jmcgill298](https://github.com/jmcgill298))
- add pytest chache to gitignore [\#200](https://github.com/networktocode/ntc-templates/pull/200) ([jmcgill298](https://github.com/jmcgill298))
- Fix index file out of order [\#199](https://github.com/networktocode/ntc-templates/pull/199) ([jmcgill298](https://github.com/jmcgill298))
- Fix printing to use function for py3 compatibility [\#198](https://github.com/networktocode/ntc-templates/pull/198) ([jmcgill298](https://github.com/jmcgill298))
- Adding 4 templates [\#192](https://github.com/networktocode/ntc-templates/pull/192) ([rishabh5j](https://github.com/rishabh5j))
- adding bash\_df\_-h and show\_reload\_cause templates for arista\_eos [\#182](https://github.com/networktocode/ntc-templates/pull/182) ([Sandeepsr](https://github.com/Sandeepsr))
- adding cisco\_xr show\_controller\_fabric\_plane\_all and admin\_show\_contr… [\#181](https://github.com/networktocode/ntc-templates/pull/181) ([Sandeepsr](https://github.com/Sandeepsr))
- Adding "get route" template for IPv4 for Juniper NetScreen \(screenos\) [\#180](https://github.com/networktocode/ntc-templates/pull/180) ([burningnode](https://github.com/burningnode))
- cisco xr lldp and route [\#176](https://github.com/networktocode/ntc-templates/pull/176) ([itdependsnetworks](https://github.com/itdependsnetworks))
- adding arista\_macsec\_templates [\#174](https://github.com/networktocode/ntc-templates/pull/174) ([Sandeepsr](https://github.com/Sandeepsr))
- adding cisco\_xr\_show\_ip\_bgp\_summary.template [\#170](https://github.com/networktocode/ntc-templates/pull/170) ([Sandeepsr](https://github.com/Sandeepsr))
- added show vrf and show ip arp for nxos [\#167](https://github.com/networktocode/ntc-templates/pull/167) ([vaneuk](https://github.com/vaneuk))
- IOS\_SHOW\_RUN\_CONFIG\_PARTITION\_ACL: Add new template [\#166](https://github.com/networktocode/ntc-templates/pull/166) ([jmcgill298](https://github.com/jmcgill298))
- IOS\_SHOW\_IP\_ACL: new template [\#165](https://github.com/networktocode/ntc-templates/pull/165) ([jmcgill298](https://github.com/jmcgill298))
- ASA\_SHOW\_IP\_ACCESS\_LIST: Add catch-all error [\#164](https://github.com/networktocode/ntc-templates/pull/164) ([jmcgill298](https://github.com/jmcgill298))
- change top dir logic [\#163](https://github.com/networktocode/ntc-templates/pull/163) ([itdependsnetworks](https://github.com/itdependsnetworks))
- Update cisco\_nxos\_show\_lldp\_neighbors.template & index file [\#162](https://github.com/networktocode/ntc-templates/pull/162) ([termlen0](https://github.com/termlen0))
- Avaya vsp show software [\#161](https://github.com/networktocode/ntc-templates/pull/161) ([kadecole](https://github.com/kadecole))
- added show config sess summ [\#160](https://github.com/networktocode/ntc-templates/pull/160) ([jedelman8](https://github.com/jedelman8))
- adding arista\_eos\_show\_interfaces\_transceiver.template and edit arist… [\#159](https://github.com/networktocode/ntc-templates/pull/159) ([Sandeepsr](https://github.com/Sandeepsr))
- Alex up [\#158](https://github.com/networktocode/ntc-templates/pull/158) ([itdependsnetworks](https://github.com/itdependsnetworks))
- Avaya ers show interface name [\#157](https://github.com/networktocode/ntc-templates/pull/157) ([kadecole](https://github.com/kadecole))
- Added Avaya ERS templates [\#155](https://github.com/networktocode/ntc-templates/pull/155) ([kadecole](https://github.com/kadecole))
- Adjusted hp\_procurve\_show\_vlans.template to account for varying outputs. [\#148](https://github.com/networktocode/ntc-templates/pull/148) ([tsimson](https://github.com/tsimson))
- Added Avaya ERS templates [\#146](https://github.com/networktocode/ntc-templates/pull/146) ([OfWolfAndMan](https://github.com/OfWolfAndMan))
- Show power commands [\#144](https://github.com/networktocode/ntc-templates/pull/144) ([ericdost](https://github.com/ericdost))
- Fix CDP to work with 3 capablities in cdp output [\#143](https://github.com/networktocode/ntc-templates/pull/143) ([itdependsnetworks](https://github.com/itdependsnetworks))
- update nxos show interface for vlan [\#140](https://github.com/networktocode/ntc-templates/pull/140) ([itdependsnetworks](https://github.com/itdependsnetworks))
- Ios sh status [\#139](https://github.com/networktocode/ntc-templates/pull/139) ([itdependsnetworks](https://github.com/itdependsnetworks))
- Update NXOS show-ip-route for more scenarios [\#138](https://github.com/networktocode/ntc-templates/pull/138) ([jamiecaesar](https://github.com/jamiecaesar))
- Show environment power all [\#137](https://github.com/networktocode/ntc-templates/pull/137) ([ericdost](https://github.com/ericdost))
- Add ASA VPN Troubelshooting Commands [\#136](https://github.com/networktocode/ntc-templates/pull/136) ([jmcgill298](https://github.com/jmcgill298))
- Added new template: Cisco ASA show interface [\#134](https://github.com/networktocode/ntc-templates/pull/134) ([jvanderaa](https://github.com/jvanderaa))
- Updated IOS show-ip-route to handle additional cases [\#133](https://github.com/networktocode/ntc-templates/pull/133) ([jamiecaesar](https://github.com/jamiecaesar))
- Add ASA Templates [\#131](https://github.com/networktocode/ntc-templates/pull/131) ([jmcgill298](https://github.com/jmcgill298))
- fix pfs when no value present [\#129](https://github.com/networktocode/ntc-templates/pull/129) ([jmcgill298](https://github.com/jmcgill298))
- add asa sh run crypto map [\#128](https://github.com/networktocode/ntc-templates/pull/128) ([jmcgill298](https://github.com/jmcgill298))
- Dgjustice nxos show ip bgp nei [\#126](https://github.com/networktocode/ntc-templates/pull/126) ([dgjustice](https://github.com/dgjustice))
- Fixing cisco\_ios\_show\_interfaces\_status [\#125](https://github.com/networktocode/ntc-templates/pull/125) ([GGabriele](https://github.com/GGabriele))
- update xr controllers [\#123](https://github.com/networktocode/ntc-templates/pull/123) ([itdependsnetworks](https://github.com/itdependsnetworks))
- Additional Templates for Cisco IOS [\#122](https://github.com/networktocode/ntc-templates/pull/122) ([rpollard00](https://github.com/rpollard00))
- change show interface to interfaces [\#120](https://github.com/networktocode/ntc-templates/pull/120) ([itdependsnetworks](https://github.com/itdependsnetworks))
- add speed + duplex to ios show interfaces [\#119](https://github.com/networktocode/ntc-templates/pull/119) ([itdependsnetworks](https://github.com/itdependsnetworks))
- update ios show proc cpu [\#118](https://github.com/networktocode/ntc-templates/pull/118) ([itdependsnetworks](https://github.com/itdependsnetworks))
- update nxos show proc cpu [\#117](https://github.com/networktocode/ntc-templates/pull/117) ([itdependsnetworks](https://github.com/itdependsnetworks))



\* *This Changelog was automatically generated by [github_changelog_generator](https://github.com/github-changelog-generator/github-changelog-generator)*
