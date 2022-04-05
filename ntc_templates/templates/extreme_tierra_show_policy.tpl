Value ingressgroup_name ([\-\w]+)
Value rmap_name ([\-\w]+)
Value desc ([\-\w+\s+]+)
Value traffic_type (\S+)
Value tunnel_id (\d+|any)
Value mode (\S+)
Value interface ((ethernet\s+\d\/\d+\s*)+|none)

Start
  ^\s*Name\s+:\s+${ingressgroup_name}
  ^\s*Route-Map\s+:\s+${rmap_name}
  ^\s*Description\s+:\s+${desc}
  ^\s*Traffic-Type\s+:\s+${traffic_type}
  ^\s*Tunnel-Id\s+:\s+${tunnel_id}
  ^\s*Mode\s+:\s+${mode}
  ^\s*Interfaces\s+:\s+${interface} -> Record
