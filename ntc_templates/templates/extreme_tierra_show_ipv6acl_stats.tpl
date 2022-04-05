Value Filldown acl_type (ipv6)
Value Filldown acl_name ([\w-]+)
Value seq_num (\d+)
Value fw_action (permit|deny)
#Value acl_params ([\w+\s+]+)
Value acl_params (.*)
Value packets (\d+)
Value bytes (\d+)
Value packet_rate (\d+)
Value bit_rate (\d+)


Start
  ^\s*${acl_type}\s+access-list\s+${acl_name}\s*
  ^\s*seq\s+${seq_num}\s+${fw_action}\s+${acl_params}\s+\(\s*${packets}\s+Packets,\s+${bytes}\s+Bytes,\s+${packet_rate}\s+Packets\/sec,\s+${bit_rate}\s+Bits\/sec\s*\)$$ -> Continue.Record

EOF
