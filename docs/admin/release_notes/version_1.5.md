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

