#Number of ingress-groups: 128
#
#    Name : ig_1-01
#             Route-Map : mall_1-01
#           Description : -
#            Interfaces :  ethernet 3/1  ethernet 7/1
#
#    Name : ig_1-02
#             Route-Map : mall_1-02
#           Description : -
#            Interfaces :  ethernet 3/2  ethernet 7/2
#
#    Name : ig_gtp
#             Route-Map : map_gtp
#           Description : -
#            Interfaces :  ethernet 7/1  ethernet 7/2  ethernet 8/1  ethernet 8/2  ethernet 7/15  ethernet 8/15
#          Traffic-Type : GTPU
#             Tunnel-Id : any
#                  Mode : none
#   Destination-ip-addr : any
#        Source-ip-addr : any
#DATA
#['INGRESS_GROUP_COUNT', 'INGRESSGROUP_NAME', 'RMAP_NAME', 'DESC', 'INTERFACES', 'TRAFFIC_TYPE', 'TUNNEL_ID', 'MODE', 'DEST_IP', 'SOURCE_IP']
#['128', '', '', '', '', '', '', '', '', '']
#['128', 'ig_1-01', 'mall_1-01', '-', 'ethernet 3/1  ethernet 7/1', '', '', '', '', '']
#['128', 'ig_1-02', 'mall_1-02', '-', 'ethernet 3/2  ethernet 7/2', '', '', '', '', '']
#['128', 'ig_gtp', 'map_gtp', '-', 'ethernet 7/1  ethernet 7/2  ethernet 8/1  ethernet 8/2  ethernet 7/15  ethernet 8/15', 'GTPU', 'any', 'none', 'any', 'any']
#
Value Filldown INGRESS_GROUP_COUNT (\d+)
Value INGRESSGROUP_NAME (\S+)
Value RMAP_NAME (\S+)
Value DESC (\S+)
Value INTERFACES (([ethrn\d\s/]+)|none)
Value TRAFFIC_TYPE (\S+)
Value TUNNEL_ID (\d+|any)
Value MODE (\S+)
Value DEST_IP ([any]+|[\d\w:\.]+)
Value SOURCE_IP ([any]+|[\d\w:\.]+)

Start
  ^Number of ingress-groups: ${INGRESS_GROUP_COUNT}[\r\n]*
  ^\s*Name\s+:\s+${INGRESSGROUP_NAME}
  ^\s*Route-Map\s+:\s+${RMAP_NAME}
  ^\s*Description\s+:\s+${DESC}
  ^\s+Interfaces :\s+${INTERFACES}
  ^\s*Traffic-Type\s+:\s+${TRAFFIC_TYPE}
  ^\s*Tunnel-Id\s+:\s+${TUNNEL_ID}
  ^\s*Mode\s+:\s+${MODE}
  ^\s*Destination-ip-addr : ${DEST_IP}
  ^\s*Source-ip-addr : ${SOURCE_IP}
  ^ -> Record
