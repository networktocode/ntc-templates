# Output
#Number of ingress-groups: 5
#        Name : ig_fw
#No ingress-group stats found
#
#
#Ingress-group Packet Statistics (IP-GRE Tunnel)
#
#        Name : ig_gre
#   RX Frames : 254974655421
#    RX Bytes : 65372998862882
#
#
#Ingress-group Packet Statistics (GTPU Tunnel)
#
#        Name : ig_gtp
#   RX Frames : 254174481975
#    RX Bytes : 65279872546846
#
#
#Ingress-group Packet Statistics (Vxlan Tunnel)
#
#        Name : ig_vcp
#   RX Frames : 0
#    RX Bytes : 0
#
#        Name : ig_cloud_gre
#No ingress-group stats found
# Data returned
# HEADER
# ['group_count', 'name', 'tunnel_type', 'rx_frames', 'rx_bytes']
# Data returned
#['5', 'ig_fw', '', '', '']
#['5', 'ig_gre', 'IP-GRE', '254974655421', '65372998862882']
#['5', 'ig_gtp', 'GTPU', '254174481975', '65279872546846']
#['5', 'ig_vcp', 'Vxlan', '0', '0']
#['5', 'ig_cloud_gre', '', '', '']
#['5', '', '', '', '']
#
Value Filldown group_count (\d+)
Value Key name (\S+)
Value tunnel_type ([\S\-]+)
Value rx_frames (\d+)
Value rx_bytes (\d+)
Value no_stats (No ingress-group stats found)

Start
 ^Number of ingress-groups: ${group_count}
 ^Ingress-group Packet Statistics \(${tunnel_type} Tunnel
 ^\s+Name\s+:\s+${name}
 ^\s+RX Frames\s+:\s+${rx_frames}
 ^\s+RX Bytes\s+:\s+${rx_bytes}|^${no_stats} -> Record