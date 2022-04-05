################Output####################################
#ethernet 6/16 Admin state UP      Operational state UP
# Interface index is 268435624 (0x100000a8)
# MTU 9216 bytes
# Hardware is Ethernet  mac address 40:88:2f:c0:f8:50
# Current Speed  100G
# FEC Mode: RS-FEC
#
#Statistics
# Carrier Transitions: 4
#           LastClear: 0s
#Input:
#              Total pkts: 697534372
#          Broadcast pkts: 100001
#            Discard pkts: 200002
#             Errors pkts: 300003
#              FCS Errors: 100
#              MCast pkts: 200
#                  Octets: 357137598464
#              UCast pkts: 697534372
#               Runt pkts: 10
#              CRC Errors: 20
#Input Distribution:
#            64 byte pkts: 64
#        65-127 byte pkts: 127
#       128-255 byte pkts: 128
#       256-511 byte pkts: 256
#      512-1023 byte pkts: 1023
#     1024-1518 byte pkts: 158
#              Jumbo pkts: 9001
#Out:
#              Total pkts: 1
#          Broadcast pkts: 2
#            Discard pkts: 3
#             Errors pkts: 4
#              MCast pkts: 5
#                  Octets: 6
#              UCast pkts: 7
#Rate Info:
#                   Input: 2000.910390 Mbits/sec, 470138 pkts/sec 2.00% #of line-rate
#                  Output: 4000.000000 Mbits/sec, 870138 pkts/sec 4.00% #of line-rate
#
#####################Parsed output######################
#--- Header ---
#['Ethernet',
# 'Admin_status',
# 'Operational_status',
# 'Interface_Index',
# 'MTU',
# 'HW_mac_address',
# 'Speed',
# 'FEC_mode',
# 'Carrier_Transition',
# 'Total_pkts_In',
# 'Broadcast_Pkts_In',
# 'Discard_Pkts_In',
# 'Errors_Pkts_In',
# 'FCS_Errors_In',
# 'Mcast_Pkts_In',
# 'Octets_In',
# 'UCast_Pkts_In',
# 'Runts_In',
# 'CRC_Errors_In',
# 'byte_64_pkts',
# 'byte_65_127_pkts',
# 'byte_128_255_pkts',
# 'byte_256_511_pkts',
# 'byte_512_1023_pkts',
# 'byte_1024_1518_pkts',
# 'Jumbo_pkts',
# 'Total_pkts_out',
# 'Broadcast_Pkts_Out',
# 'Discard_Pkts_Out',
# 'Errors_Pkts_Out',
# 'Mcast_Pkts_Out',
# 'Octets_Out',
# 'UCast_Pkts_Out',
# 'Rate_In_Mbps',
# 'Rate_In_pps',
# 'Line_Rate_In',
# 'Rate_out_Mbps',
# 'Rate_out_pps',
# 'Line_Rate_out']
#--- Parsed Data ---
#[['6/16',
#  'UP',
#  'UP',
#  '268435624',
#  '9216',
#  '40:88:2f:c0:f8:50',
#  '100G',
#  'RS-FEC',
#  '4',
#  '697534372',
#  '100001',
#  '200002',
#  '300003',
#  '100',
#  '200',
#  '357137598464',
#  '697534372',
#  '10',
#  '20',
#  '64',
#  '127',
#  '128',
#  '256',
#  '1023',
#  '158',
#  '9001',
#  '1',
#  '2',
#  '3',
#  '4',
#  '5',
#  '6',
#  '7',
#  '2000.910390',
#  '470138',
#  '2.00',
#  '4000.000000',
#  '870138',
#  '4.00']]
#######################Parser#############################
#######################Parser#############################
Value Ethernet ([\d+\/:]+)
Value Admin_status ([a-zA-Z-]+)
Value Operational_status ([a-zA-Z-]+)
Value Interface_Index (\d+)
Value MTU (\d+)
Value HW_mac_address ([\d+[a-z+A-Z-\d\/:]+)
Value Speed (\d+[a-zA-Z-])
Value FEC_mode ([a-zA-Z-]+\s*)
Value Carrier_Transition (\d+)
Value Total_pkts_In (\d+)
Value Broadcast_Pkts_In (\d+)
Value Discard_Pkts_In (\d+)
Value Errors_Pkts_In (\d+)
Value FCS_Errors_In (\d+)
Value Mcast_Pkts_In (\d+)
Value Octets_In (\d+)
Value UCast_Pkts_In (\d+)
Value Runts_In (\d+)
Value CRC_Errors_In (\d+)
Value byte_64_pkts (\d+)
Value byte_65_127_pkts (\d+)
Value byte_128_255_pkts (\d+)
Value byte_256_511_pkts (\d+)
Value byte_512_1023_pkts (\d+)
Value byte_1024_1518_pkts (\d+)
Value Jumbo_pkts (\d+)
Value Total_pkts_out (\d+)
Value Broadcast_Pkts_Out (\d+)
Value Discard_Pkts_Out (\d+)
Value Errors_Pkts_Out (\d+)
Value Mcast_Pkts_Out (\d+)
Value Octets_Out (\d+)
Value UCast_Pkts_Out (\d+)
Value Rate_In_Mbps ([\d+\.\/]+)
Value Rate_In_pps ([\d+\.\/]+)
Value Line_Rate_In ([\d\.]+)
Value Rate_out_Mbps ([\d+\.\/]+)
Value Rate_out_pps ([\d+\.\/]+)
Value Line_Rate_out ([\d\.]+)

Start
  ^\s*ethernet\s+${Ethernet}\s+Admin\s+state\s+${Admin_status}\s+Operational\s+state\s+${Operational_status}
  ^\s*Interface\s+index\s+is\s+${Interface_Index}
  ^\s*MTU\s+${MTU}\s+bytes
  ^\s*Hardware\s+is\s+Ethernet\s+mac\s+address\s+${HW_mac_address}
  ^\s*Current\s+Speed\s+${Speed}
  ^\s*FEC\s+Mode:\s+${FEC_mode}
  ^\s*Statistics -> Statistics

Statistics
  ^\s*Carrier\s+Transitions:\s+${Carrier_Transition}
  ^\s*LastClear:\s+\S+
  ^\s*Input: -> Input

Input
  ^\s*Total pkts:\s+${Total_pkts_In}
  ^\s*Broadcast pkts:\s+${Broadcast_Pkts_In}
  ^\s*Discard pkts:\s+${Discard_Pkts_In}
  ^\s*Errors pkts:\s+${Errors_Pkts_In}
  ^\s*FCS Errors:\s+${FCS_Errors_In}
  ^\s*MCast pkts:\s+${Mcast_Pkts_In}
  ^\s*Octets:\s+${Octets_In}
  ^\s*UCast pkts:\s+${UCast_Pkts_In}
  ^\s*Runt pkts:\s+${Runts_In}
  ^\s*CRC Errors:\s+${CRC_Errors_In}
  ^\s*Input Distribution: -> Input_Distribution

Input_Distribution
  ^\s*64 byte pkts:\s+${byte_64_pkts}
  ^\s*65-127 byte pkts:\s+${byte_65_127_pkts}
  ^\s*128-255 byte pkts:\s+${byte_128_255_pkts}
  ^\s*256-511 byte pkts:\s+${byte_256_511_pkts}
  ^\s*512-1023 byte pkts:\s+${byte_512_1023_pkts}
  ^\s*1024-1518 byte pkts:\s+${byte_1024_1518_pkts}
  ^\s*Jumbo pkts:\s+${Jumbo_pkts}
  ^\s*Out: -> Out

Out
  ^\s*Total pkts:\s+${Total_pkts_out}
  ^\s*Broadcast pkts:\s+${Broadcast_Pkts_Out}
  ^\s*Discard pkts:\s+${Discard_Pkts_Out}
  ^\s*Errors pkts:\s+${Errors_Pkts_Out}
  ^\s*MCast pkts:\s+${Mcast_Pkts_Out}
  ^\s*Octets:\s+${Octets_Out}
  ^\s*UCast pkts:\s+${UCast_Pkts_Out}
  ^\s*Rate Info: -> Rate_Info

Rate_Info
  ^\s*Input:\s+${Rate_In_Mbps}[\s\w/]+,\s+${Rate_In_pps}[\s\w/]+\s${Line_Rate_In}[%\s\w\-]+
  ^\s*Output:\s+${Rate_out_Mbps}[\s\w/]+,\s+${Rate_out_pps}[\s\w/]+\s${Line_Rate_out}[%\s\w\-]+ -> Record
