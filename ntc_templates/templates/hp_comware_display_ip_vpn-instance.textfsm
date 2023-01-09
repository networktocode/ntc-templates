Value Required NAME (\S+)
Value RD (\d+:\d+)

Start
  ^\s*VPN-Instance Name -> VPNInstances

VPNInstances
  ^\s*${NAME}\s+${RD}\s+.* -> Record
  ^\s*${NAME}\s+.* -> Record
  ^\s*$$
  ^. -> Error
