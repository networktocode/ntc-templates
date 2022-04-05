Value namespace (kube-system|ngnpb)
Value name (\S+)
Value ready (\d+/\d+)
Value status (\S+)
Value restarts (\d+)

Start
  ^\s*${namespace}\s+${name}\s+${ready}\s+${status}\s+${restarts} -> Record
