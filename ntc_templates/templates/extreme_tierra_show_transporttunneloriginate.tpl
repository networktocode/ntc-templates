Value tto_name ([\-\w]+)
Value src_ip ([\.\d]+)
Value dst_ip ([\.\d]+)
Value src_mac ([0-9a-fA-F\:]+)
Value dst_mac ([0-9a-fA-F\:]+)
Value vlan (\d+|none)
Value pcp (\d+|none)
Value tunnel_type (ERSPAN|GRE|none)
Value tunnel_id (\d+|none)

Start
  ^\s*Name\s*:\s*${tto_name}
  ^\s*Source-Ipv4-Addr\s*:\s*${src_ip}
  ^\s*Destination-Ipv4-Addr\s*:\s*${dst_ip}
  ^\s*Source-Mac-Addr\s*:\s*${src_mac}
  ^\s*Destination-Mac-Addr\s*:\s*${dst_mac}
  ^\s*Vlan-Id\s*:\s*${vlan}
  ^\s*Vlan-Pcp\s*:\s*${pcp}
  ^\s*Encap-Type\s*:\s*${tunnel_type}
  ^\s*Encap-Id\s*:\s*${tunnel_id} -> Record
