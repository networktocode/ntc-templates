#Interface Statistics: port-channel 1
# Carrier Transitions: 0
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
#Out:
#              Total pkts: 0
#          Broadcast pkts: 0
#            Discard pkts: 0
#             Errors pkts: 0
#              MCast pkts: 0
#                  Octets: 0
#              UCast pkts: 0
#
#Interface Statistics: port-channel 2
# Carrier Transitions: 0
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
#Out:
#              Total pkts: 0
#          Broadcast pkts: 0
#            Discard pkts: 0
#             Errors pkts: 0
#              MCast pkts: 0
#                  Octets: 0
#              UCast pkts: 0
#
# Data Returned
#['ETHERNET', 'CARRIER_TRANSITION_COUNT', 'LAST_CLEAR', 'TOTAL_PKTS_IN', 'BROADCAST_PKTS_IN', 'DISCARD_PKTS_IN', 'ERRORS_PKTS_IN', 'FCS_ERRORS_IN', 'MCAST_PKTS_IN', 'OCTETS_IN', 'UCAST_PKTS_IN', 'RU#NT_IN', 'CRC_IN', 'DISTRO_64B', 'DISTRO_65B_127B', 'DISTRO_128B_255B', 'DISTRO_256B_511B', 'DISTRO_512B_1023B', 'DISTRO_1024B_1518B', 'DISTRO_JUMBO', 'TOTAL_PKTS_OUT', 'BROADCAST_PKTS_OUT', 'DISCARD_PKTS_OUT', 'ERRORS_PKTS_OUT', 'MCAST_PKTS_OUT', 'OCTETS_OUT', 'UCAST_PKTS_OUT', 'RATE_IN_MBPS', 'RATE_IN_PPS', 'RATE_IN_PERCENT', 'RATE_OUT_MBPS', 'RATE_OUT_PPS', 'RATE_OUT_PERCENT']
#['1/1', '1', '0', '10', '0', '0', '0', '0', '', '0', '0', '0', '0', '64', '65', '128', '256', '512', '1024', '9216', '2895', '0', '0', '0', '2895', '518205', '0', '0.000000', '0', '1.11', '0.000000', '0', '1.22']
#['1/2', '1', '0', '0', '0', '0', '0', '0', '', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '2895', '0', '0', '0', '2895', '518205', '0', '0.000000', '0', '2.11', '0.000000', '0', '2.22']
Value PORT_CHANNEL ([\d/\:]+)
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
Value TOTAL_PKTS_OUT (\d+)
Value BROADCAST_PKTS_OUT (\d+)
Value DISCARD_PKTS_OUT (\d+)
Value ERRORS_PKTS_OUT (\d+)
Value MCAST_PKTS_OUT (\d+)
Value OCTETS_OUT (\d+)
Value UCAST_PKTS_OUT (\d+)

Start
  ^\s*Interface\s+Statistics:\s+port\-channel\s+${PORT_CHANNEL}
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
 ^\s*Out: -> OUT

OUT
 ^\s+Total pkts: ${TOTAL_PKTS_OUT}
 ^\s+Broadcast pkts: ${BROADCAST_PKTS_OUT}
 ^\s+Discard pkts: ${DISCARD_PKTS_OUT}
 ^\s+Errors pkts: ${ERRORS_PKTS_OUT}
 ^\s+MCast pkts: ${MCAST_PKTS_OUT}
 ^\s+Octets: ${OCTETS_OUT}
 ^\s+ UCast pkts: ${UCAST_PKTS_OUT} -> Record
 ^ -> Start