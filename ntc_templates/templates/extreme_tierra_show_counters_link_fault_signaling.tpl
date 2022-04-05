#Port       Local-Fault-Count  Last-Local-Fault     Remote-Fault-Count Last-Remote-Fault
#========== ================== ==================== ================== ====================
#Eth 1/1    1                  2021-10-20T18:35:41Z 0                  NA
#Eth 1/2    0                  NA                   0                  NA
#Eth 1/3    0                  NA                   0                  NA
#Eth 1/4    0                  NA                   0                  NA
#Eth 1/5    0                  NA                   0                  NA
#Eth 1/6    0                  NA                   0                  NA
#Eth 1/7    0                  NA                   0                  NA
#Eth 1/8    0                  NA                   0                  NA
#Eth 1/9    0                  NA                   0                  NA
#Eth 1/10   1                  2021-10-20T18:35:41Z 1                  2021-10-20T18:35:46Z
#Data
#
#
Value PORT ([\w\s\d/:]+)
Value LOCAL_FAULT_COUNT (\d+)
Value LAST_LOCAL_FAULT (NA|[\d\-]+T[\d:\w]+)
Value REMOTE_FAULT_COUNT (\d+)
Value LAST_REMOTE_FAULT (NA|[\d\-]+T[\d:\w]+)




Start
 ^===== ->  TABLE

TABLE
 ^${PORT}\s+${LOCAL_FAULT_COUNT}\s+${LAST_LOCAL_FAULT}\s+${REMOTE_FAULT_COUNT}\s+${LAST_REMOTE_FAULT} -> Record