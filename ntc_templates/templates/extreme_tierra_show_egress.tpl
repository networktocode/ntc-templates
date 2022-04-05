Value egress_name ([\-\w]+)
Value DESCRIPTION (\S+)
Value encap ([\-\w]+)
Value lpolicy_name ([\-\w]+)
Value precedence (\d+)
Value interface (port-channel|ethernet)
Value port (\d/\d+|\d+)

Start
  ^\s*Name\s+:\s+${egress_name}
  ^\s*Description\s+:\s+${DESCRIPTION}
  ^\s*Encap\s+:\s+${encap}
  ^\s*Listener\s+Policy\s+:\s+${lpolicy_name}
  ^\s*Precedence\s+:\s+${precedence}
  ^\s*Interface\s+:\s+${interface}\s+${port} -> Record
