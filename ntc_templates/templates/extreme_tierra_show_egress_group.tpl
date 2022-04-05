#    Name : eg_2055
#          egress : ep_po7
#          egress : ep_po8
#
#
#    Name : eg_2090
#          egress : ep_7-04
# Data
#['EGRESS_GROUP_COUNT', 'NAME', 'DESCRIPTION', 'EGRESS_NAME']
#['79', '', '', []]
#['79', 'eg_1010', 'vcp_0', ['ep_vcp_tool_01']]
#['79', '', '', []]
#['79', 'eg_2000', '', ['ep_po8', 'ep_po6']]
#
Value Filldown EGRESS_GROUP_COUNT (\d+)
Value Key NAME (\S+)
Value DESCRIPTION (\S+)
Value List EGRESS_NAME (\S+)

Start
  ^Number[\w\-\s:]+\s+${EGRESS_GROUP_COUNT}
  ^[\r\n\s]*[Name]+\s+:\s+${NAME}
  ^\s+Description\s+:\s+${DESCRIPTION}
  ^\s+egress\s+:\s+${EGRESS_NAME}
  ^$$ -> Record
