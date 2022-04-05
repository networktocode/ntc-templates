Value Filldown port_channel_count (\d+)
Value portchannel (\d+)
Value Mtu (\d+)
Value Admin_State (UP|DOWN)
Value Oper_State (UP|DOWN)
Value Ifindex (0x\S+)
Value Description (.*)

Start
  ^\s*Number\s+of\s+interfaces\s+${port_channel_count}
  ^\s*Name\s+Mtu\s+Admin-State\s+Oper-State\s+Ifindex\s+Description\s*
  ^----- -> Interface

Interface
  ^\s*Po${portchannel}\s+${Mtu}\s+${Admin_State}\s+${Oper_State}\s+${Ifindex}\s+${Description}\s* -> Record
