Value tt_name ([-\w]+)
Value rx_frames (\d+)
Value rx_bytes (\d+)

Start
  ^\s*.*show\s+transport-tunnel\s+counters\s+${tt_name}
  ^\s*$$
  ^\s*Transport\s*tunnel\s+Packet\s+Statistics
  ^\s*$$
  ^\s*RX\s+Frames\s+:\s+${rx_frames}
  ^\s*RX\s+Bytes\s+:\s+${rx_bytes} -> Record
