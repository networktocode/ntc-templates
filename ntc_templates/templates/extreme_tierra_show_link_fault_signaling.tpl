#
#Rx and Tx link-fault-signaling status
#Port       Link-Faults
#========== ===============
#Eth 1/1    ON
#Eth 1/2    ON
#Eth 1/3    ON
#Data
#
#
Value PORT ([\w\s\d/:]+)
Value LFS_STATUS (\S+)


Start
 ^===== ->  TABLE

TABLE
 ^${PORT}\s+${LFS_STATUS} -> Record