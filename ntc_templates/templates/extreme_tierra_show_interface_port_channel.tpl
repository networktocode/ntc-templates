################CLI Output####################################
#port-channel 200 is up
#    MTU 9216 Bytes
#    IfIndex 0x400002c7
#    Port mode is Full Duplex, 100 Gb/s
#    LagType is Static
#    MinLinks is 1
#    Load balance method uses Src/Dst IP, Src/Dst L4 port and protocol
#    Active Members in this channel: Eth 1/15, Eth 3/12
#    Members in this channel: Eth 1/15, Eth 3/12
#
#Statistics
# Carrier Transitions: 7
#           LastClear: 0s
#Input:
#          Broadcast pkts: 10000
#            Discard pkts: 200
#             Errors pkts: 10
#              FCS Errors: 20
#              MCast pkts: 100
#                  Octets: 30
#              UCast pkts: 2000000
#       Unknown Protocols: 1
#Out:
#          Broadcast pkts: 10000
#            Discard pkts: 100
#             Errors pkts: 10
#              MCast pkts: 1000000000
#                  Octets: 2000
#              UCast pkts: 4000000
#NPB#
####################output################################
#--- Header ---
#['po_id',
# 'status',
# 'MTU',
# 'Interface_Index',
# 'port_mode',
# 'Speed',
# 'LAG_type',
# 'MinLinks',
# 'Load_balance_method',
# 'Active_member',
# 'members',
# 'Carrier_Transition',
# 'Broadcast_Pkts_In',
# 'Discard_Pkts_In',
# 'Errors_Pkts_In',
# 'FCS_Errors_In',
# 'Mcast_Pkts_In',
# 'Octets_In',
# 'UCast_Pkts_In',
# 'Unknown_protocols',
# 'Broadcast_Pkts_Out',
# 'Discard_Pkts_Out',
# 'Errors_Pkts_Out',
# 'Mcast_Pkts_Out',
# 'Octets_Out',
# 'UCast_Pkts_Out']
#--- Parsed Data ---
#[['200',
#  'up',
#  '9216',
#  '0x400002c7',
#  'Full Duplex',
#  '100 Gb/s',
#  'Static',
#  '1',
#  'Src/Dst IP, Src/Dst L4 port and protocol',
#  'Eth 1/15, Eth 3/12',
#  'Eth 1/15, Eth 3/12',
#  '7',
#  '10000',
#  '200',
#  '10',
#  '20',
#  '100',
#  '30',
#  '2000000',
#  '10',
#  '10000',
#  '100',
#  '10',
#  '1000000000',
#  '2000',
#  '4000000']]
#######################Parser#############################
Value po_id ([\d+\/:]+)
Value status ([a-zA-Z-]+)
Value MTU (\d+)
Value Interface_Index ([\d+\a-zA-Z-]+)
Value port_mode ([a-zA-Z-]+\s+[a-zA-Z]+)
Value Speed (\d+\s+[a-zA-Z+\/+]+)
Value LAG_type ([a-zA-Z-]+\s*)
Value MinLinks (\d+)
Value Load_balance_method ([\s+a-zA-Z\/,\d+]+)
Value Active_member ([\s+a-zA-Z\/,\d+:]+)
Value members ([\s+a-zA-Z\/,\d+:]+)
Value Carrier_Transition (\d+)
Value Broadcast_Pkts_In (\d+)
Value Discard_Pkts_In (\d+)
Value Errors_Pkts_In (\d+)
Value FCS_Errors_In (\d+)
Value Mcast_Pkts_In (\d+)
Value Octets_In (\d+)
Value UCast_Pkts_In (\d+)
Value Unknown_protocols (\d+)
Value Broadcast_Pkts_Out (\d+)
Value Discard_Pkts_Out (\d+)
Value Errors_Pkts_Out (\d+)
Value Mcast_Pkts_Out (\d+)
Value Octets_Out (\d+)
Value UCast_Pkts_Out (\d+)

Start
  ^\s*port-channel\s+${po_id}\s+is\s+${status}
  ^\s*MTU\s+${MTU}\s+Bytes
  ^\s*IfIndex\s+${Interface_Index}
  ^\s*Port\s+mode\s+is\s+${port_mode},\s+${Speed}
  ^\s*LagType\s+is\s+${LAG_type}
  ^\s*MinLinks\s+is\s+${MinLinks}
  ^\s*Load\s+balance\s+method\s+uses\s+${Load_balance_method}
  ^\s*Active\s+Members\s+in\s+this\s+channel:\s+${Active_member}
  ^\s*Members\s+in\s+this\s+channel:\s+${members}
  ^\s*Statistics -> Statistics

Statistics
  ^\s*Carrier\s+Transitions:\s+${Carrier_Transition}
  ^\s*LastClear:\s+\S+
  ^\s*Input: -> Input

Input
  ^\s*Broadcast pkts:\s+${Broadcast_Pkts_In}
  ^\s*Discard pkts:\s+${Discard_Pkts_In}
  ^\s*Errors pkts:\s+${Errors_Pkts_In}
  ^\s*FCS Errors:\s+${FCS_Errors_In}
  ^\s*MCast pkts:\s+${Mcast_Pkts_In}
  ^\s*Octets:\s+${Octets_In}
  ^\s*UCast pkts:\s+${UCast_Pkts_In}
  ^\s*Unknown\s+Protocols:\s+${Unknown_protocols}
  ^\s*Out: -> Out

Out
  ^\s*Broadcast pkts:\s+${Broadcast_Pkts_Out}
  ^\s*Discard pkts:\s+${Discard_Pkts_Out}
  ^\s*Errors pkts:\s+${Errors_Pkts_Out}
  ^\s*MCast pkts:\s+${Mcast_Pkts_Out}
  ^\s*Octets:\s+${Octets_Out}
  ^\s*UCast pkts:\s+${UCast_Pkts_Out} -> Record