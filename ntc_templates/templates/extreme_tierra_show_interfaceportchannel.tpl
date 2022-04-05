Value portchannel (\d+)
Value Oper_State (up|down)
Value Mtu (\d+)
Value Ifindex (0x\S+)
Value minlinks (\d+)
Value loadbalance (.*)
Value active_ports ([Eth\s+\d\//d+,]+|Nil)
Value member_ports ([Eth\s+\d\//d+,]+|Nil)
Value Carrier_Transitions (\d+)
Value LastClear (\S+)
Value Broadcast_Pkts_In (\d+)
Value Discard_Pkts_In (\d+)
Value Errors_Pkts_In (\d+)
Value FCS_Errors_In (\d+)
Value Mcast_Pkts_In (\d+)
Value Octets_In (\d+)
Value UCast_Pkts_In (\d+)
Value Unknown_Protocols (\d+)
Value Broadcast_Pkts_Out (\d+)
Value Discard_Pkts_Out (\d+)
Value Errors_Pkts_Out (\d+)
Value Mcast_Pkts_Out (\d+)
Value Octets_Out (\d+)
Value UCast_Pkts_Out (\d+)


Start
  ^\s*port-channel ${portchannel} is ${Oper_State}
  ^\s*MTU\s+${Mtu}\s+Bytes
  ^\s*IfIndex\s+${Ifindex}
  ^\s*Port\s+mode\s+is\s+Full\s+Duplex,\s+100\s+Gb/s
  ^\s*LagType\s+is\s+Static 
  ^\s*MinLinks\s+is\s+${minlinks}
  #^\s*Load\s+balance\s+method\s+uses\s+Src/Dst\s+IP,\s+Src/Dst\s+L4\s+port(,\s+|\s+and\s+)protocol\s*(and)?\s*(tunnel\s+ID)?
  ^\s*Load\s+balance\s+method\s+uses\s+${loadbalance}
  ^\s*Active\s+Members\s+in\s+this\s+channel:\s+${active_ports}
  ^\s*Members\s+in\s+this\s+channel:\s+${member_ports} -> Continue
  ^\s*$$
  ^\s*Statistics\s*
  ^\s*Carrier\s+Transitions:\s+${Carrier_Transitions}
  ^\s*LastClear:\s+${LastClear}
  ^\s*Input:\s* -> Input

Input
  ^\s*Broadcast\s+Pkts:\s+${Broadcast_Pkts_In}
  ^\s*Discard\s+Pkts:\s+${Discard_Pkts_In}
  ^\s*Errors\s+Pkts:\s+${Errors_Pkts_In}
  ^\s*FCS\s+Errors:\s+${FCS_Errors_In}
  ^\s*MCast\s+Pkts:\s+${Mcast_Pkts_In}
  ^\s*Octets:\s+${Octets_In}
  ^\s*UCast\s+Pkts:\s+${UCast_Pkts_In}
  ^\s*Unknown\s+Protocols:\s+${Unknown_Protocols}
  ^\s*Out:\s* -> Out

Out
  ^\s*Broadcast\s+Pkts:\s+${Broadcast_Pkts_Out}
  ^\s*Discard\s+Pkts:\s+${Discard_Pkts_Out}
  ^\s*Errors\s+Pkts:\s+${Errors_Pkts_Out}
  ^\s*MCast\s+Pkts:\s+${Mcast_Pkts_Out}
  ^\s*Octets:\s+${Octets_Out}
  ^\s*UCast\s+Pkts:\s+${UCast_Pkts_Out} -> Record
