#                      Packets                              Errors                               Discards                      CRC
#Port           rx                 tx                rx                 tx                rx                 tx                rx
#=======================================================================================================================================
#Eth 1/1        0                  3017              0                  0                 0                  0                 0
#Eth 1/2        0                  3017              0                  0                 0                  0                 0
#Data
#
#
Value PORT ([\w\s\d/:]+)
Value PACKETS_RX (\d+)
Value PACKETS_TX (\d+)
Value ERRORS_RX (\d+)
Value ERRORS_TX (\d+)
Value DISCARDS_RX (\d+)
Value DISCARDS_TX (\d+)
Value CRC_RX (\d+)


Start
 ^===== ->  TABLE

TABLE
 ^${PORT}\s+${PACKETS_RX}\s+${PACKETS_TX}\s+${ERRORS_RX}\s+${ERRORS_TX}\s+${DISCARDS_RX}\s+${DISCARDS_TX}\s+${CRC_RX} -> Record