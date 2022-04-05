Value ethernet (\d+\/\d+|UNKNOWN)
Value packets (\d+)
Value packet_length (\d+)
Value packet_dir (RX|TX)
Value packet_filter (\S+)

Start
 ^\s*---.*
 ^\s*Frames\s+Logged\s+on\s+interface\s+=\s+.*
 ^\s*---.*
 ^\s*$$ -> packet_metadata

packet_metadata
 ^\s*---.*
 ^\s*Pkt\s+Capture\s+Metadata\s*:\s+#\d+\s+of\s+${packets}\s+Packets\s*
 ^\s*---.*
 ^\s*Frame\s+Received\s+Time\s+:\s+.*
 ^\s*Packet\s+Length\(bytes\)\s*:\s+${packet_length}
 ^\s*Packet\s+Direction\s+:\s+${packet_dir}
 ^\s*Packet\s+Filter\s+:\s+${packet_filter}
 ^\s*Front\s+Panel\s+Port\s+:\s+${ethernet} -> Record
 ^\s*---.*
