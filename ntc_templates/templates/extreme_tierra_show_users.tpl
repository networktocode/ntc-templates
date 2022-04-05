#output
#Username                         Role       Host IP                                  Device          Time Logged In
#================================ ========== ======================================== =============== ==============================
#admin                            admin      10.10.10.10                              SSH             2021-10-20 20:46
# Data returned
#headers
#['USERNAME', 'ROLE', 'HOST_IP', 'DEVICE', 'LOGIN_TIMESTAMP']
#Data
#['admin', 'admin', '10.10.10.10', 'SSH', '2021-10-20 20:46']
#
Value USERNAME (\S+)
Value ROLE (\S+)
Value HOST_IP (\S+)
Value DEVICE (\S+)
Value LOGIN_TIMESTAMP ([\s\S]+)

Start
  ^===== -> TABLE

TABLE
  ^${USERNAME}\s+${ROLE}\s+${HOST_IP}\s+${DEVICE}\s+${LOGIN_TIMESTAMP}