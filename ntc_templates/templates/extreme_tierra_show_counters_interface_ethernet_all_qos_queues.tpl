#Port   Q1       Q2       Q3       Q4       Q5       Q6       Q7       Q8
#===============================================================================
#1/1    0        0        0        0        0        0        0        0      
#Data
#
#
Value PORT ([\d/:]+)
Value Q1 (\d+)
Value Q2 (\d+)
Value Q3 (\d+)
Value Q4 (\d+)
Value Q5 (\d+)
Value Q6 (\d+)
Value Q7 (\d+)
Value Q8 (\d+)

Start
 ^===== ->  TABLE

TABLE
 ^${PORT}\s+${Q1}\s+${Q2}\s+${Q3}\s+${Q4}\s+${Q5}\s+${Q6}\s+${Q7}\s+${Q8} -> Record
