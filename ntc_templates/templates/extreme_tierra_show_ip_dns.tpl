######################CLI output#########################
#ip dns domain name
# extremenetworks.com
# test.com
# google.com
#ip dns name-server
# 134.141.36.32
# 10.20.100.98
# 30.30.30.30
#####################parsed output#######################
#--- Header ---
#['domain_name', 'name_server']
#--- Parsed Data ---
#[['extremenetworks.com', ''],
# ['test.com', ''],
# ['google.com', ''],
# ['134.141.36.32', ''],
# ['10.20.100.98', ''],
# ['30.30.30.30', '']]
#
####################Parser###############################
Value domain_name ([\w\-\./]+)
Value name_server ([\d\.]+)

Start
 ^ip\s+dns domain name
 ^\s+${domain_name} -> Record
 ^ip dns name-server
 ^\s+${name_server} -> Record