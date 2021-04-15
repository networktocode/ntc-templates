# Changelog

## [2.0.0](https://github.com/networktocode/ntc-templates/tree/1.5.0) (2021-03-11)

[Full Changelog](https://github.com/networktocode/ntc-templates/compare/v2.0.0...v1.7.0)

**Merged pull requests:**

- Migrate packaging to use poetry [\#882](https://github.com/networktocode/ntc-templates/pull/882) ([jmcgill298](https://github.com/jmcgill298))

## [v1.7.0](https://github.com/networktocode/ntc-templates/tree/v1.7.0) (2021-03-11)

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

- Release v1.7.0 [\#889](https://github.com/networktocode/ntc-templates/pull/889) ([jmcgill298](https://github.com/jmcgill298))
- new alcatel\_sros tmpl, 'show service sdp' [\#886](https://github.com/networktocode/ntc-templates/pull/886) ([h4ndzdatm0ld](https://github.com/h4ndzdatm0ld))
- New Template: alcatel\_sros\_show\_router\_rsvp\_interface [\#884](https://github.com/networktocode/ntc-templates/pull/884) ([h4ndzdatm0ld](https://github.com/h4ndzdatm0ld))
- \#784-cisco\_asa\_show\_running-config\_all\_crypto\_map.textfsm [\#883](https://github.com/networktocode/ntc-templates/pull/883) ([diepes](https://github.com/diepes))
- New template: cisco\_ios\_show\_alert\_counters.textfsm [\#881](https://github.com/networktocode/ntc-templates/pull/881) ([FragmentedPacket](https://github.com/FragmentedPacket))
- Bugfix: Media type update for cisco\_ios\_show\_interfaces [\#879](https://github.com/networktocode/ntc-templates/pull/879) ([FragmentedPacket](https://github.com/FragmentedPacket))
- new sros template [\#877](https://github.com/networktocode/ntc-templates/pull/877) ([h4ndzdatm0ld](https://github.com/h4ndzdatm0ld))
- cisco\_wlc\_ssh\_show\_wlan\_sum update - make PMIP\_MOBILITY optional [\#872](https://github.com/networktocode/ntc-templates/pull/872) ([progala](https://github.com/progala))
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
- Add new template for cisco\_wlc\_ssh\_sh\_ap\_image\_all [\#742](https://github.com/networktocode/ntc-templates/pull/742) ([conorwu1107](https://github.com/conorwu1107))
- Update index to handle cisco\_ios show\_ip\_bgp\_all\_summary [\#738](https://github.com/networktocode/ntc-templates/pull/738) ([Niclnx](https://github.com/Niclnx))
- Added support for broadcom\_icos command show\_mac-address-table [\#736](https://github.com/networktocode/ntc-templates/pull/736) ([alepodj](https://github.com/alepodj))
- BugFix: IOS CDP - Better handling of output [\#735](https://github.com/networktocode/ntc-templates/pull/735) ([jmcgill298](https://github.com/jmcgill298))
- New Template support for broadcom\_icos as a new OS and added show\_version command [\#733](https://github.com/networktocode/ntc-templates/pull/733) ([alepodj](https://github.com/alepodj))
- New template for ubiquity edgeswitch: show version [\#732](https://github.com/networktocode/ntc-templates/pull/732) ([saaverdo](https://github.com/saaverdo))
- New Template for Cisco NX-OS: show forwarding adjacency [\#722](https://github.com/networktocode/ntc-templates/pull/722) ([Yakuza-UA](https://github.com/Yakuza-UA))
- BugFix: cisco\_ios\_show\_interfaces\_switchport: Made trunking\_vlans a list, and changed regex [\#671](https://github.com/networktocode/ntc-templates/pull/671) ([FragmentedPacket](https://github.com/FragmentedPacket))



\* *This Changelog was automatically generated by [github_changelog_generator](https://github.com/github-changelog-generator/github-changelog-generator)*
