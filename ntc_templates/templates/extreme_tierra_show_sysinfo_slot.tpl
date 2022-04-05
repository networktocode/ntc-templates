# 1.1 format
#Slot Information
#Slot  State         FRU-Id  FRU-Type    Description         
#-------------------------------------------------------------------
#1     Online        1       LC16x100G   16x100G QSFP28 Line Card
#2     Empty         0                                       
#3     Empty         0                                       
#4     Online        1       LC16x100G   16x100G QSFP28 Line Card
#5     Empty         0                                       
#6     Empty         0                                       
#7     Online        1       LC16x100G   16x100G QSFP28 Line Card
#8     Online        1       LC16x100G   16x100G QSFP28 Line Card
#
#1.2 format
#Slot Information
#Slot  State       FRU-Type    Uptime    Insertion-Time       Extraction-Time      Description
#-------------------------------------------------------------------------------------------------------
#1     Online      LC16x100G   26h18m25s 2021-10-20 18:32:02                       16x100G QSFP28 Line Card
#2     Online      LC16x100G   26h18m23s 2021-10-20 18:32:02                       16x100G QSFP28 Line Card
#3     Present     LC16x100G             2021-10-25 20:57:31                       16x100G QSFP28 Line Card
#4     Present     LC16x100G             2021-10-25 20:57:33                       16x100G QSFP28 Line Card
#6     InitializingLC16x100G             2021-10-25 20:57:38                       16x100G QSFP28 Line Card
#7     Empty    
#8     Online      LC16x100G   1m53s     2021-10-25 20:57:42                       16x100G QSFP28 Line Card
# Data
#
#
Value SLOT (\d+)
Value STATE (Online|Initializing|Empty|Present)
Value FRU_TYPE ([\w\d]+)
Value UPTIME ([\d\w]+|.)
Value INSERTION_TIME ([\d\-]+\s[\d:]+)
Value EXTRACTION_TIME ([\d\-]+\s[\d:]+|.)
Value DESCRIPTION ([\s\S]+)

Start
  ^Slot\s+State\s+FRU\-Id\s+FRU-Type\s+Description -> TABLE1_1FORMAT
  ^Slot\s+State\s+FRU\-Type\s+Uptime\s+Insertion\-Time\s+Extraction\-Time\s+Description -> TABLE1_2FORMAT

TABLE1_1FORMAT
  ^${SLOT}\s+${STATE}\s+\d -> Record
  ^${SLOT}\s+${STATE}\s+\d\s+${FRU_TYPE}\s+${DESCRIPTION} -> Record

TABLE1_2FORMAT
  ^${SLOT}\s+${STATE}\s+${FRU_TYPE}\s+${INSERTION_TIME}\s+${DESCRIPTION} -> Record
  ^${SLOT}\s+${STATE}\s+${FRU_TYPE}\s+${UPTIME}s\s+${INSERTION_TIME}\s+${EXTRACTION_TIME}\s+${DESCRIPTION} -> Record
  ^${SLOT}\s+${STATE} -> Record