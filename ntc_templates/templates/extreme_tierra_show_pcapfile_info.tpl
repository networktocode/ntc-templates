Value pcap_name (\w+.pcapng)
Value last_modified_time (\d+\s+\S+\s+\d+\s+\d+:\d+\s+UTC)
Value pcap_size ((\d+[\.\d+])(KB|MB))
Value pkt_cnt (\d+)

Start
 ^\s*-+
 ^\s*PCAP\s+File(s)\s+Details:\s*
 ^\s*-+
 ^\s*Pcap\s+File\s+Name\s+:\s+${pcap_name}
 ^\s*$$
 ^\s*Last\s+Modified\s+:\s+${last_modified_time}
 ^\s*$$
 ^\s*PcapFile\s+Size\s+:\s+${pcap_size}
 ^\s*$$
 ^\s*Packet\s+Count\s+:\s+${pkt_cnt} -> Record
 ^\s*$$
 ^\s*-+
