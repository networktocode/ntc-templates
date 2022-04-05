Value lpolicy_name ([\-\w]+)
Value fw_action (permit|deny)
Value seq_num (\d+)
Value ip_type (ip)
Value ip_acl_name ([\w\-]+)
Value ipv6_type (ipv6)
Value ipv6_acl_name ([\w\-]+)
Value mac_type (mac)
Value mac_acl_name ([\w\-]+)
Value acl_state (active|inactive)
Value truncate (\d+)
Value br_strip (br-tag)
Value vlan_strip (vlan-tag)
Value vn_strip (vn-tag)
Value decap (decap)
Value vlan (\d+)
Value packets (\d+)
Value bytes (\d+)
Value packet_rate (\d+)
Value bit_rate (\d+)


Start
  ^\s*listener-policy\s+${lpolicy_name}\s+${seq_num}
  ^\s*forward-action\s+${fw_action}
  ^\s*match\s+${ip_type}\s+access-list\s+${ip_acl_name}\s+\(${acl_state}\)
  ^\s*match\s+${ipv6_type}\s+access-list\s+${ipv6_acl_name}\s+\(${acl_state}\)
  ^\s*match\s+${mac_type}\s+access-list\s+${mac_acl_name}\s+\(${acl_state}\)
  ^\s*truncate\s+${truncate}
  ^\s*strip\s+${br_strip}
  ^\s*strip\s+${vlan_strip}
  ^\s*strip\s+${vn_strip}
  ^\s*${decap}
  ^\s*vlan\s+${vlan}
  ^\s*Policy\s+matches:\s+${packets}\s+packets,\s+${bytes}\s+bytes,\s+${packet_rate}\s+PacketRate,\s+${bit_rate}\s+BitRate\s* -> Record
