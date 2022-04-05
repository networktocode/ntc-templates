Value Filldown egress_name ([\-\w]+)
Value lpolicy_name ([\-\w]+)
Value precedence (\d+)
Value port_channel (\d+)
Value port (\d/\d+)

Start
  ^\s*egress\s+${egress_name} -> Record
  ^\s*listener-policy\s+${lpolicy_name} -> Record
  ^\s*precedence\s+${precedence}\s+interface\s+port-channel\s+${port_channel} -> Record
  ^\s*precedence\s+${precedence}\s+interface\s+ethernet\s+${port} -> Record
