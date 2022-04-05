Value Filldown egressgroup_name ([\-\w]+)
Value egress_name ([\-\w]+)

Start
  ^\s*egress-group\s+${egressgroup_name}
  ^\s*egress\s+${egress_name} -> Continue.Record
