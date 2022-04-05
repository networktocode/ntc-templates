####################output#######################################
#S3_PB1# show route-map map_vcp
#route-map map_vcp 10
#forward-action permit
#match ip access-list v4_vcp_0 (active)
#match ipv6 access-list v6_vcp_0 (active)
#egress-group eg_1010
#Policy matches: 0 packets, 0 bytes, 0 Packets/sec, 0 Bits/sec
#
#route-map map_vcp 20
#forward-action permit
#match ip access-list v4_vcp_1 (active)
#match ipv6 access-list v6_vcp_1 (active)
#egress-group eg_1020
#Policy matches: 0 packets, 0 bytes, 0 Packets/sec, 0 Bits/sec
#
#route-map map_vcp 30
#forward-action permit
#match ip access-list v4_vcp_2 (active)
#match ipv6 access-list v6_vcp_2 (active)
#egress-group eg_1030
#Policy matches: 0 packets, 0 bytes, 0 Packets/sec, 0 Bits/sec
#
#route-map map_vcp 40
#forward-action permit
#match ip access-list v4_vcp_3 (active)
#match ipv6 access-list v6_vcp_3 (active)
#egress-group eg_1040
#Policy matches: 0 packets, 0 bytes, 0 Packets/sec, 0 Bits/sec
################################################################
Value rmap_name ([\-\w]+)
Value fw_action (permit|deny)
Value seq_num (\d+)
Value acl_type (ip|ipv6|mac)
Value acl_name ([\w\-]+)
Value eg_name ([\w\-]+)
Value truncate (\d+)
Value packets (\d+)
Value bytes (\d+)
Value packet_rate (\d+)
Value bit_rate (\d+)

Start
  ^\s*route-map\s+${rmap_name}\s+${seq_num}
  ^\s*forward-action\s+${fw_action}
  ^\s*match\s+${acl_type}\s+access-list\s+${acl_name} -> Record
  ^\s*egress-group\s*${eg_name}
  ^\s*truncate\s+${truncate}
  ^\s*Policy\s+matches:\s+${packets}\s+packets,\s+${bytes}\s+bytes,\s*${packet_rate}\s+Packets\/sec,\s*${bit_rate}\s+Bits\/sec\s* -> Record
