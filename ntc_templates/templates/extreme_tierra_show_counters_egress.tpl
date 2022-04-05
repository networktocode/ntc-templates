Value egress_name ([\S]+)
Value tx_frames (\d+)
Value tx_bytes (\d+)

Start
  ^\s*Egress\s+Packet\s+Statistics\s+:\s+${egress_name}
  ^\s*$$
  ^\s*TX\s+Frames\s+:\s+${tx_frames}
  ^\s*TX\s+Bytes\s+:\s+${tx_bytes} -> Record
