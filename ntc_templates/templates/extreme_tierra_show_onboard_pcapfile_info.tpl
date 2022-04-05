Value pcap_name (\w+.pcapng)
Value pcap_size (\d+\.\d+\s+(KB|MB))
Value pkt_cnt (\d+)

Start
 ^\s*-+
 ^\s*PCAP\s+File(s)\s+Details:\s*
 ^\s*Pcap\s+File\s+Name\s+:\s+${pcap_name}
 ^\s*Last\s+Modified\s+:\s+.*
 ^\s*PcapFile\s+Size\s+:\s+${pcap_size}
 ^\s*Packet\s+Count\s+:\s+${pkt_cnt} -> Record
 ^\s*-+
