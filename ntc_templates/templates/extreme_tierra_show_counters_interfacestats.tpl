#Interface Statistics: ethernet 1/1
# Carrier Transitions: 1
#           LastClear: 0s
#Input:
#              Total pkts: 10
#          Broadcast pkts: 0
#            Discard pkts: 0
#             Errors pkts: 0
#              FCS Errors: 0
#              MCast pkts: 0
#                  Octets: 0
#              UCast pkts: 0
#               Runt pkts: 0
#              CRC Errors: 0
#Input Distribution:
#            64 byte pkts: 64
#        65-127 byte pkts: 65
#       128-255 byte pkts: 128
#       256-511 byte pkts: 256
#      512-1023 byte pkts: 512
#     1024-1518 byte pkts: 1024
#              Jumbo pkts: 9216
#Out:
#              Total pkts: 2895
#          Broadcast pkts: 0
#            Discard pkts: 0
#             Errors pkts: 0
#              MCast pkts: 2895
#                  Octets: 518205
#              UCast pkts: 0
#Rate Info:
#                   Input: 0.000000 Mbits/sec, 0 pkts/sec 1.11% of line-rate
#                  Output: 0.000000 Mbits/sec, 0 pkts/sec 1.22% of line-rate
#
#Interface Statistics: ethernet 1/2
# Carrier Transitions: 1
#           LastClear: 0s
#Input:
#              Total pkts: 0
#          Broadcast pkts: 0
#            Discard pkts: 0
#             Errors pkts: 0
#              FCS Errors: 0
#              MCast pkts: 0
#                  Octets: 0
#              UCast pkts: 0
#               Runt pkts: 0
#              CRC Errors: 0
#Input Distribution:
#            64 byte pkts: 0
#        65-127 byte pkts: 0
#       128-255 byte pkts: 0
#       256-511 byte pkts: 0
#      512-1023 byte pkts: 0
#     1024-1518 byte pkts: 0
#              Jumbo pkts: 0
#Out:
#              Total pkts: 2895
#          Broadcast pkts: 0
#            Discard pkts: 0
#             Errors pkts: 0
#              MCast pkts: 2895
#                  Octets: 518205
#              UCast pkts: 0
#Rate Info:
#                   Input: 0.000000 Mbits/sec, 0 pkts/sec 2.11% of line-rate
#                  Output: 0.000000 Mbits/sec, 0 pkts/sec 2.22% of line-rate
#
# Data Returned
#['ETHERNET', 'CARRIER_TRANSITION_COUNT', 'LAST_CLEAR', 'TOTAL_PKTS_IN', 'BROADCAST_PKTS_IN', 'DISCARD_PKTS_IN', 'ERRORS_PKTS_IN', 'FCS_ERRORS_IN', 'MCAST_PKTS_IN', 'OCTETS_IN', 'UCAST_PKTS_IN', 'RU#NT_IN', 'CRC_IN', 'DISTRO_64B', 'DISTRO_65B_127B', 'DISTRO_128B_255B', 'DISTRO_256B_511B', 'DISTRO_512B_1023B', 'DISTRO_1024B_1518B', 'DISTRO_JUMBO', 'TOTAL_PKTS_OUT', 'BROADCAST_PKTS_OUT', 'DISCARD_PKTS_OUT', 'ERRORS_PKTS_OUT', 'MCAST_PKTS_OUT', 'OCTETS_OUT', 'UCAST_PKTS_OUT', 'RATE_IN_MBPS', 'RATE_IN_PPS', 'RATE_IN_PERCENT', 'RATE_OUT_MBPS', 'RATE_OUT_PPS', 'RATE_OUT_PERCENT']
#['1/1', '1', '0', '10', '0', '0', '0', '0', '', '0', '0', '0', '0', '64', '65', '128', '256', '512', '1024', '9216', '2895', '0', '0', '0', '2895', '518205', '0', '0.000000', '0', '1.11', '0.000000', '0', '1.22']
#['1/2', '1', '0', '0', '0', '0', '0', '0', '', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '2895', '0', '0', '0', '2895', '518205', '0', '0.000000', '0', '2.11', '0.000000', '0', '2.22']
Value ETHERNET ([\d/\:]+)
Value CARRIER_TRANSITION_COUNT (\d+)
Value LAST_CLEAR (\d+)
Value TOTAL_PKTS_IN (\d+)
Value BROADCAST_PKTS_IN (\d+)
Value DISCARD_PKTS_IN (\d+)
Value ERRORS_PKTS_IN (\d+)
Value FCS_ERRORS_IN (\d+)
Value MCAST_PKTS_IN (\d+)
Value OCTETS_IN (\d+)
Value UCAST_PKTS_IN (\d+)
Value RUNT_IN (\d+)
Value CRC_IN (\d+)
Value DISTRO_64B (\d+)
Value DISTRO_65B_127B (\d+)
Value DISTRO_128B_255B (\d+)
Value DISTRO_256B_511B (\d+)
Value DISTRO_512B_1023B (\d+)
Value DISTRO_1024B_1518B (\d+)
Value DISTRO_JUMBO (\d+)
Value TOTAL_PKTS_OUT (\d+)
Value BROADCAST_PKTS_OUT (\d+)
Value DISCARD_PKTS_OUT (\d+)
Value ERRORS_PKTS_OUT (\d+)
Value MCAST_PKTS_OUT (\d+)
Value OCTETS_OUT (\d+)
Value UCAST_PKTS_OUT (\d+)
Value RATE_IN_MBPS ([\d.]+)
Value RATE_IN_PPS ([\d]+)
Value RATE_IN_PERCENT ([\d.]+)
Value RATE_OUT_MBPS ([\d.]+)
Value RATE_OUT_PPS ([\d]+)
Value RATE_OUT_PERCENT ([\d.]+)

Start
  ^\s*Interface\s+Statistics:\s+ethernet\s+${ETHERNET}
  ^\s*Carrier\s+Transitions:\s+${CARRIER_TRANSITION_COUNT}
  ^\s*LastClear:\s+${LAST_CLEAR}s
  ^\s*Input: -> INPUT

  

INPUT
 ^\s+Total pkts: ${TOTAL_PKTS_IN}
 ^\s+Broadcast pkts: ${BROADCAST_PKTS_IN}
 ^\s+Discard pkts: ${DISCARD_PKTS_IN}
 ^\s+Errors pkts: ${ERRORS_PKTS_IN}
 ^\s+FCS Errors: ${FCS_ERRORS_IN}
 ^\s+MCast pkts:${MCAST_PKTS_IN}
 ^\s+Octets: ${OCTETS_IN}
 ^\s+UCast pkts: ${UCAST_PKTS_IN}
 ^\s+Runt pkts: ${RUNT_IN}
 ^\s+CRC Errors: ${CRC_IN} 
 ^\s*Input\s+Distribution: -> IN_DISTRO

IN_DISTRO
 ^\s+64 byte pkts: ${DISTRO_64B}
 ^\s+65-127 byte pkts: ${DISTRO_65B_127B}
 ^\s+128-255 byte pkts: ${DISTRO_128B_255B}
 ^\s+256-511 byte pkts: ${DISTRO_256B_511B}
 ^\s+512-1023 byte pkts: ${DISTRO_512B_1023B}
 ^\s+1024-1518 byte pkts: ${DISTRO_1024B_1518B}
 ^\s+Jumbo pkts: ${DISTRO_JUMBO}
 ^\s*Out: -> OUT

OUT
 ^\s+Total pkts: ${TOTAL_PKTS_OUT}
 ^\s+Broadcast pkts: ${BROADCAST_PKTS_OUT}
 ^\s+Discard pkts: ${DISCARD_PKTS_OUT}
 ^\s+Errors pkts: ${ERRORS_PKTS_OUT}
 ^\s+MCast pkts: ${MCAST_PKTS_OUT}
 ^\s+Octets: ${OCTETS_OUT}
 ^\s+ UCast pkts: ${UCAST_PKTS_OUT}
 ^\s*Rate Info: -> RATE

RATE
 ^\s+Input: ${RATE_IN_MBPS} Mbits/sec, ${RATE_IN_PPS} pkts/sec ${RATE_IN_PERCENT}% of line-rate
 ^\s+Output: ${RATE_OUT_MBPS} Mbits/sec, ${RATE_OUT_PPS} pkts/sec ${RATE_OUT_PERCENT}% of line-rate -> Record
 ^ -> Start