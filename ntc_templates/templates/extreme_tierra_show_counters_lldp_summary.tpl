#LLDP Global Statistics:
#             FrameIn: 7526
#            FrameOut: 244601
#           LastClear: 0s
# Data
#
Value FRAMEIN (\d+)
Value FRAMEOUT (\d+)
Value LAST_CLEAR (\d+)

Start
 ^\s+FrameIn: ${FRAMEIN}
 ^\s+FrameOut: ${FRAMEOUT}
 ^\s+LastClear: ${LAST_CLEAR}s -> Record