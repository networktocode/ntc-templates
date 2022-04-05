Value Filldown num_interfaces (\d+)
Value Required ethernet (\d+\/\d+)
Value Mtu (\d+)
#Value Enabled (true|false)
Value Admin_State (UP|DOWN)
Value Oper_State (UP|DOWN)
Value Description (.*)

Start
  ^\s*Number\s+of\s+interfaces\s+${num_interfaces}
  ^\s*Name\s+Mtu\s+Admin-State\s+Oper-State\s+Ifindex\s+Description\s*
  ^.*-----.* -> Interface

Interface
  ^\s*Eth\s+${ethernet}\s+${Mtu}\s+${Admin_State}\s+${Oper_State}\s+0x\S+\s+${Description}\s* -> Record
