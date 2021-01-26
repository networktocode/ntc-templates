Value IP (\S+)
Value MAC ([0-9a-fA-F]{6}-[0-9a-fA-F]{6})
Value TYPE (\S+)
Value PORT (\S+)

Start
  ^.*IP ARP table -> ARP

ARP
  ^\s+${IP}\s+${MAC}\s+${TYPE}\s+${PORT} -> Record
