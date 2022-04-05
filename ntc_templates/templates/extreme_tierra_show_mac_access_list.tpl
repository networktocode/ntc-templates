################cmd###############
#mac access-list test
#  seq 10 permit 00:00:11:00:00:01 ff:ff:ff:ff:ff:ff 00:00:22:00:00:01 ff:ff:ff:ff:ff:00 vlan 201 count ( 0 Packets, 0 Bytes, 0 PacketRate, 0 BitRate )
#  seq 20 permit 00:00:11:00:00:02 ff:ff:ff:ff:ff:ff 00:00:22:00:00:02 ff:ff:ff:ff:ff:00 vlan 202 count ( 0 Packets, 0 Bytes, 0 PacketRate, 0 BitRate )
#mac access-list test2
#  seq 10 permit 00:00:11:00:00:01 ff:ff:ff:ff:ff:ff 00:00:22:00:00:01 ff:ff:ff:ff:ff:00 vlan 201 log count ( 0 Packets, 0 Bytes, 0 PacketRate, 0 BitRate )
#  seq 20 permit 00:00:11:00:00:02 ff:ff:ff:ff:ff:ff 00:00:22:00:00:02 ff:ff:ff:ff:ff:00 vlan 202 log count ( 0 Packets, 0 Bytes, 0 PacketRate, 0 BitRate )
############Output###############
#--- Header ---
#['acl_name',
# 'ip_version',
# 'rule',
# 'packets',
# 'Bytes',
# 'packet_rate',
# 'bit_rate']
#--- Parsed Data ---
#[['test',
#  'mac',
#  'seq 10 permit 00:00:11:00:00:01 ff:ff:ff:ff:ff:ff 00:00:22:00:00:01 '
#  'ff:ff:ff:ff:ff:00 vlan 201 count ',
#  '0',
#  '0',
#  '0',
#  '0'],
# ['test',
#  'mac',
#  'seq 20 permit 00:00:11:00:00:02 ff:ff:ff:ff:ff:ff 00:00:22:00:00:02 '
#  'ff:ff:ff:ff:ff:00 vlan 202 count ',
#  '0',
#  '0',
#  '0',
#  '0'],
# ['test2',
#  'mac',
#  'seq 10 permit 00:00:11:00:00:01 ff:ff:ff:ff:ff:ff 00:00:22:00:00:01 '
#  'ff:ff:ff:ff:ff:00 vlan 201 log count ',
#  '0',
#  '0',
#  '0',
#  '0'],
# ['test2',
#  'mac',
#  'seq 20 permit 00:00:11:00:00:02 ff:ff:ff:ff:ff:ff 00:00:22:00:00:02 '
#  'ff:ff:ff:ff:ff:00 vlan 202 log count ',
#  '0',
#  '0',
#  '0',
#  '0']
################ip acl output############
#--- Header ---
#['acl_name',
# 'ip_version',
# 'rule',
# 'packets',
# 'Bytes',
# 'packet_rate',
# 'bit_rate']
#--- Parsed Data ---
#[['Test', 'ip', 'seq 10 permit 1 any any count ', '0', '0', '0', '0'],
# ['Test',
#  'ip',
#  'seq 20 permit 10 10.10.1.1 255.255.255.255 any log count ',
#  '0',
#  '0',
#  '0',
#  '0'],
############Parser################
Value Filldown acl_name (\w+)
Value Filldown ip_version (\w+)
Value rule ([\w+\?\-\d+\s+\.:/]*)
Value packets ([\w+\?\-\d+\s+\.:/]*)
Value Bytes ([\w+\?\-\d+\s+\.:/]*)
Value packet_rate ([\w+\?\-\d+\s+\.:/]*)
Value bit_rate ([\w+\?\-\d+\s+\.:/]*)

Start
  ^${ip_version}\s+access-list\s+${acl_name}\s*
  ^\s*(${rule})\s*\(\s*${packets}\s+Packets,\s+${Bytes}\s+Bytes,\s+${packet_rate}\s+PacketRate,\s+${bit_rate}\s+BitRate\s*\) -> Continue.Record