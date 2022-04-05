#Number of transport-tunnels: 1
#
#                  Name : dog
#         Ingress-Group : none
#ERSPAN Terminated Packet Statistics 
#
#   RX Frames : 0 
#    RX Bytes : 0 
#
#ERSPAN Dropped Packet Statistics 
#
# Dropped Frames : 0 
#  Dropped Bytes : 0 
#
#Data
#
Value Filldown TRANSPORT_TUNNEL_COUNT (\d+)
Value NAME (\S+)
Value INGRESS_GROUP (\S+)
Value RX_FRAMES (d+)
Value RX_BYTES (\d+)
Value DROPPED_FRAMES (\d+)
Value DROPPED_BYTES (\d+)

Start
 ^\s*Number of transport-tunnels: ${TRANSPORT_TUNNEL_COUNT}
 ^\s+Name : ${NAME}
 ^\s+Ingress-Group : ${INGRESS_GROUP}
 ^\s+RX Frames : ${RX_FRAMES}
 ^\s+RX Bytes : ${RX_BYTES}
 ^\s+Dropped Frames : ${DROPPED_FRAMES}
 ^\s+Dropped Bytes : ${DROPPED_BYTES} -> Record