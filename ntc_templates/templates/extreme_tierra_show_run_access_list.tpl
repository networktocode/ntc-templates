################cmd###############
#NPB# show run access-list
#ip access-list shipra
#  seq 10 permit 1 any any count
#ipv6 access-list shipra1
#  seq 10 deny 100 any any log count
#mac access-list test
#  seq 10 permit 00:00:11:00:00:01 ff:ff:ff:ff:ff:ff 00:00:22:00:00:01 ff:ff:ff:ff:ff:00 vlan 201 count
#  seq 20 permit 00:00:11:00:00:02 ff:ff:ff:ff:ff:ff 00:00:22:00:00:02 ff:ff:ff:ff:ff:00 vlan 202 count
#mac access-list test2
#  seq 10 permit 00:00:11:00:00:01 ff:ff:ff:ff:ff:ff 00:00:22:00:00:01 ff:ff:ff:ff:ff:00 vlan 201 log count
#  seq 20 permit 00:00:11:00:00:02 ff:ff:ff:ff:ff:ff 00:00:22:00:00:02 ff:ff:ff:ff:ff:00 vlan 202 log count
#NPB#
############Output###############
#root@ubuntu-98:/root/20210203_df9fb7c6/bin# ./parse_output /home/user/euas_user_lib/templates/shipra_private_work/mac_acl_output.txt /home/user/euas_user_lib/templates/shipra_private_work/show_macacl.tpl
#Trying to parse output: /home/user/euas_user_lib/templates/shipra_private_work/mac_acl_output.txt using template : /home/user/euas_user_lib/templates/shipra_private_work/show_macacl.tpl
#--- Header ---
#['acl_version', 'acl_name', 'rule']
#--- Parsed Data ---
#[['ip', 'shipra', '10 permit 1 any any count'],
# ['ipv6', 'shipra1', '10 deny 100 any any log count'],
# ['mac',
#  'test',
#  '10 permit 00:00:11:00:00:01 ff:ff:ff:ff:ff:ff 00:00:22:00:00:01 '
#  'ff:ff:ff:ff:ff:00 vlan 201 count'],
# ['mac',
#  'test',
#  '20 permit 00:00:11:00:00:02 ff:ff:ff:ff:ff:ff 00:00:22:00:00:02 '
#  'ff:ff:ff:ff:ff:00 vlan 202 count'],
# ['mac',
#  'test',
#  '30 permit 00:00:11:00:00:03 ff:ff:ff:ff:ff:ff 00:00:22:00:00:03 '
#  'ff:ff:ff:ff:ff:00 vlan 203 count'],
# ['mac',
#  'test',
#  '40 permit 00:00:11:00:00:04 ff:ff:ff:ff:ff:ff 00:00:22:00:00:04 '
#  'ff:ff:ff:ff:ff:00 vlan 204 count'],
# ['mac',
#  'test2',
#  '10 permit 00:00:11:00:00:01 ff:ff:ff:ff:ff:ff 00:00:22:00:00:01 '
#  'ff:ff:ff:ff:ff:00 vlan 201 log count'],
# ['mac',
#  'test2',
#  '20 permit 00:00:11:00:00:02 ff:ff:ff:ff:ff:ff 00:00:22:00:00:02 '
#  'ff:ff:ff:ff:ff:00 vlan 202 log count'],
# ['mac',
#  'test2',
#  '30 permit 00:00:11:00:00:03 ff:ff:ff:ff:ff:ff 00:00:22:00:00:03 '
#  'ff:ff:ff:ff:ff:00 vlan 203 log count'],
# ['mac',
#  'test2',
#  '40 permit 00:00:11:00:00:04 ff:ff:ff:ff:ff:ff 00:00:22:00:00:04 '
#  'ff:ff:ff:ff:ff:00 vlan 204 log count'],
# ['mac', 'test2', '']]
############Parser################
Value Filldown acl_name (\w+)
Value Filldown acl_version (\w+)
Value rule ([\w+\?\-\d+\s+\.:/]*)

Start
  ^${acl_version}\s+access-list\s+${acl_name}
  ^\s*seq\s+${rule} -> Record