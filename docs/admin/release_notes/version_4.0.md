
# v4.0.0

This is a major release. There are breaking changes. See https://github.com/networktocode/ntc-templates/blob/master/changes_for_4.md for the changes, and this blog post for more information. http://blog.networktocode.com/post/ntc-templates-data-modeling/

## What's Changed

* feat(cisco_xr): Add VLAN ID to show interfaces template by @elavaud in https://github.com/networktocode/ntc-templates/pull/1371
* Updates show transceivers by @jvanderaa in https://github.com/networktocode/ntc-templates/pull/1365
* Fix #1390 by @tom0010 in https://github.com/networktocode/ntc-templates/pull/1391
* Change: add tag and id to capture groups for Paloalto interface logical template by @mjbear in https://github.com/networktocode/ntc-templates/pull/1394
* FR: Add support for Cisco nxos show bgp vrf all ipv4 unicast neighbors by @tom0010 in https://github.com/networktocode/ntc-templates/pull/1401
* Fix #1321 - Cisco NXOS show ip bgp add support for empty status by @tom0010 in https://github.com/networktocode/ntc-templates/pull/1404
* Update cisco nxos show ip bgp neighbors by @tom0010 in https://github.com/networktocode/ntc-templates/pull/1403
* add support for bgp summary found on 7124SX by @stesla in https://github.com/networktocode/ntc-templates/pull/1410
* Docs: add invoke local usage example to docs by @mjbear in https://github.com/networktocode/ntc-templates/pull/1395
* Standardize Mikrotik capture groups to uppercase by @mjbear in https://github.com/networktocode/ntc-templates/pull/1398
* Standardize description capture group name by @mjbear in https://github.com/networktocode/ntc-templates/pull/1399
* Standardize VLAN-related capture group names in the Avaya ERS show vlan template by @mjbear in https://github.com/networktocode/ntc-templates/pull/1400
* Standardize capture group for vlan id by @mjbear in https://github.com/networktocode/ntc-templates/pull/1416
* Standardize MAC address capture group name by @mjbear in https://github.com/networktocode/ntc-templates/pull/1420
* Standardize interface capture group by @mjbear in https://github.com/networktocode/ntc-templates/pull/1419
* Corrected Mikrotik routeros ip route template to manage dynamic route without index by @k-ribot in https://github.com/networktocode/ntc-templates/pull/1236
* Fix cisco access list template by @guillaume-mbali in https://github.com/networktocode/ntc-templates/pull/1353
* Standardize huawei capture group to all uppercase and insert underscore by @mjbear in https://github.com/networktocode/ntc-templates/pull/1417
* Standardize virtual ip  and mac address capture groups by @mjbear in https://github.com/networktocode/ntc-templates/pull/1423
* Standardize bia capture group by @mjbear in https://github.com/networktocode/ntc-templates/pull/1424
* Standardize vlan name capture group  by @mjbear in https://github.com/networktocode/ntc-templates/pull/1418
* Standardize router mac (rmac) capture group to mac_address by @mjbear in https://github.com/networktocode/ntc-templates/pull/1422
* Standardize capture group IPVER with IP_VERSION by @mjbear in https://github.com/networktocode/ntc-templates/pull/1425
* Standardize capture groups containing ip alias by @mjbear in https://github.com/networktocode/ntc-templates/pull/1426
* Fix HPE int without mode by @dainok in https://github.com/networktocode/ntc-templates/pull/1405
* Add hp_procurve_show_cdp_neighbors_detail by @dainok in https://github.com/networktocode/ntc-templates/pull/1407
* replace capture group IP_GATEWAY with GATEWAY by @mjbear in https://github.com/networktocode/ntc-templates/pull/1427
* Enhancement: ASA OSPF interface - split IP_ADDRESS_MASK into IP_ADDRESS and NETMASK by @mjbear in https://github.com/networktocode/ntc-templates/pull/1428
* Enhancement: IOS OSPF interface - split IP_ADDRESS_MASK into IP_ADDRESS and PREFIX_LENGTH by @mjbear in https://github.com/networktocode/ntc-templates/pull/1429
* Add hp_procurve_show_ip by @dainok in https://github.com/networktocode/ntc-templates/pull/1408
* Add hp_procurve_show_ip_route by @dainok in https://github.com/networktocode/ntc-templates/pull/1409
* Cisxo XR sh ipv4 int: ignore lines by @dainok in https://github.com/networktocode/ntc-templates/pull/1414
* Standardize capture group NETMASK by @mjbear in https://github.com/networktocode/ntc-templates/pull/1430
* Enhancement: split PREFIX capture group into its parts IP_ADDRESS and PREFIX_LENGTH by @mjbear in https://github.com/networktocode/ntc-templates/pull/1431
* Standardize capture group to PREFIX_LENGTH by @mjbear in https://github.com/networktocode/ntc-templates/pull/1432
* Standardize capture group IP_ADDRESS by @mjbear in https://github.com/networktocode/ntc-templates/pull/1439
* Enhancement: mikrotik_routeros_ip_firewall_address-list by @mjbear in https://github.com/networktocode/ntc-templates/pull/1438
* fix PR 1439 - incorrectly modifying ADDRESS to be IP_ADDRESS instead of MAC ADDRESS by @mjbear in https://github.com/networktocode/ntc-templates/pull/1444
* Standardize capture group IPV6_ADDRESS by @mjbear in https://github.com/networktocode/ntc-templates/pull/1441
* Fix command extraction when test 'index' order by @max-dw-i in https://github.com/networktocode/ntc-templates/pull/1435
* remove invalid file by @whitej6 in https://github.com/networktocode/ntc-templates/pull/1446
* fix issue #1318 when ports are in monitor or nve interface is present by @mjbear in https://github.com/networktocode/ntc-templates/pull/1450
* Adjust VLAN_ID pattern to match either numbers of specific keywords to fix issue#1397 by @mjbear in https://github.com/networktocode/ntc-templates/pull/1449
* Normalize - align cisco_nxos ospf neighbor capture group names with other OSPF neighbor templates by @mjbear in https://github.com/networktocode/ntc-templates/pull/1448
* add cisco template for show file systems by @pedro-damasceno in https://github.com/networktocode/ntc-templates/pull/1443
* [fixed]: arista includes "/" in the port number on some models. by @kunitake in https://github.com/networktocode/ntc-templates/pull/1447
* Add support for Arista EOS show ip bgp detail by @tom0010 in https://github.com/networktocode/ntc-templates/pull/1451
* replace LINK_LAYER with MAC_ADDRESS in huawei_vrp_display_ipv6_neighbors by @mjbear in https://github.com/networktocode/ntc-templates/pull/1465
* Support unknown protocol in arista_eos_show_interfaces_description by @mouse91 in https://github.com/networktocode/ntc-templates/pull/1540
* Changes for 4.0 by @jvanderaa in https://github.com/networktocode/ntc-templates/pull/1541

## New Contributors

* @stesla made their first contribution in https://github.com/networktocode/ntc-templates/pull/1410
* @max-dw-i made their first contribution in https://github.com/networktocode/ntc-templates/pull/1435
* @pedro-damasceno made their first contribution in https://github.com/networktocode/ntc-templates/pull/1443
* @kunitake made their first contribution in https://github.com/networktocode/ntc-templates/pull/1447
* @mouse91 made their first contribution in https://github.com/networktocode/ntc-templates/pull/1540

**Full Changelog**: https://github.com/networktocode/ntc-templates/compare/v3.5.0...v4.0.0

# v4.0.1

## What's Changed

* Fix 'cisco_ios_show_logging' template with unnecessary '*' by @PavloSkliarenko in https://github.com/networktocode/ntc-templates/pull/1536
* Cisco ios show ip interface bugfix #1532 by @mncrftfrcnm in https://github.com/networktocode/ntc-templates/pull/1533
* Fix #1549 by @tom0010 in https://github.com/networktocode/ntc-templates/pull/1550
* Updates pyproject.toml to 4.0.1 by @jvanderaa in https://github.com/networktocode/ntc-templates/pull/1547

## New Contributors

* @PavloSkliarenko made their first contribution in https://github.com/networktocode/ntc-templates/pull/1536
* @mncrftfrcnm made their first contribution in https://github.com/networktocode/ntc-templates/pull/1533

**Full Changelog**: https://github.com/networktocode/ntc-templates/compare/v4.0.0...v4.0.1
