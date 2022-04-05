######################CLI output#########################
#S3_PB1# show system service
#SERVICE                       CURRENT       ROLLBACK      READY       STATE       RESTARTS
#                              VERSION       VERSION
#---------------------------------------------------------------------------------------------
#-
#api-gw                        1.1.0         None          true        Running     1
#chassis-mgr                   1.1.0         None          true        Running     1
#cli                           1.1.0         None          true        Running     1
#config-db                     1.1.0         None          true        Running     1
#interface-agent               1.1.0         None          true        Running     1
#interface-mgr                 1.1.0         None          true        Running     1
#lacp                          1.0.0         None          true        Running     1
#lldp                          1.0.0         None          true        Running     1
#msg-bus                       1.1.0         None          true        Running     1
#nexthop-agent                 1.1.0         None          true        Running     1
#packet-mgr                    1.1.0         None          true        Running     1
#pbd-agent                     1.1.0         None          true        Running     1
#pcap-agent                    1.1.0         None          true        Running     1
#persistent-state-db           1.1.0         None          true        Running     1
#pipeline-agent                1.1.0         None          true        Running     1
#security                      1.1.0         None          true        Running     1
#sfcs-agent                    1.1.0         None          true        Running     1
#snmp                          1.1.0         None          true        Running     1
#state-db                      1.1.0         None          true        Running     1
#stratum                       0.3.3         None          true        Running     1
#svcplane-agent                1.1.0         None          true        Running     1
#target-proxy-agent            1.1.0         None          true        Running     1
#S3_PB1#
#
#####################parsed output#######################
#--- Header ---
#['Service_name', 'Current', 'Rollback', 'Ready', 'State', 'Restarts']
#-- Parsed data ---
#['api-gw', '1.1.0', 'None', 'true', 'Running', '0']
#['chassis-mgr', '1.1.0', 'None', 'true', 'Running', '0']
#['cli', '1.1.0', 'None', 'true', 'Running', '0']
#['config-db', '1.1.0', 'None', 'true', 'Running', '0']
#['interface-agent', '1.1.0', 'None', 'true', 'Running', '0']
#['interface-mgr', '1.1.0', 'None', 'true', 'Running', '0']
#['lacp', '1.0.0', 'None', 'true', 'Running', '0']
#['msg-bus', '1.1.0', 'None', 'true', 'Running', '0']
#['nexthop-agent', '1.1.0', 'None', 'true', 'Running', '0']
#['packet-mgr', '1.1.0', 'None', 'true', 'Running', '0']
#['pbd-agent', '1.1.0', 'None', 'true', 'Running', '0']
#['pcap-agent', '1.1.0', 'None', 'true', 'Running', '0']
#['persistent-state-db', '1.1.0', 'None', 'true', 'Running', '0']
#['pipeline-agent', '1.1.0', 'None', 'true', 'Running', '0']
#['security', '1.1.0', 'None', 'true', 'Running', '0']
#['sfcs-agent', '1.1.0', 'None', 'true', 'Running', '0']
#['snmp', '1.1.0', 'None', 'true', 'Running', '0']
#['state-db', '1.1.0', 'None', 'true', 'Running', '0']
#['stratum', '0.2.32', 'None', 'true', 'Running', '0']
#['svcplane-agent', '1.1.0', 'None', 'true', 'Running', '0']
#['target-proxy-agent', '1.1.0', 'None', 'true', 'Running', '0']
####################Parser###############################
Value Key Service_name ([\w\-]+)
Value Current ([\d\.]+)
Value Rollback ([None|\d\.]+)
Value Ready ([tTrue|fFalse]+)
Value State ([\w\-]+)
Value Restarts ([\d]+)

Start
 ^---- -> TABLE

TABLE
 ^\s*${Service_name}\s+${Current}\s+${Rollback}\s+${Ready}\s+${State}\s+${Restarts} -> Record