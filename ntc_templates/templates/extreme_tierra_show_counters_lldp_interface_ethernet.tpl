#LLDP Interface Statistics: ethernet 1/1
#             FrameIn: 0
#            FrameOut: 3747
#           LastClear: 0s
#
#LLDP Interface Statistics: ethernet 1/2
#             FrameIn: 0
#            FrameOut: 3748
#           LastClear: 0s
#
# Data
#
Value PORT ([\w\s\d/:]+)
Value FRAMEIN (\d+)
Value FRAMEOUT (\d+)
Value LAST_CLEAR (\d+)

Start
 ^LLDP Interface Statistics: ${PORT}
 ^\s+FrameIn: ${FRAMEIN}
 ^\s+FrameOut: ${FRAMEOUT}
 ^\s+LastClear: ${LAST_CLEAR}s -> Record