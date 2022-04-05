#Firmware Version                          Install Date
#------------------------------------------------------------------------
#TierraOS-21.1.2.0-NPB-20211020_162740_UTC Wed, 20 Oct 2021 18:24:12 UTC
#TierraOS-21.1.2.0-NPB-20211019_134001_UTC Tue, 19 Oct 2021 18:51:57 UTC
#
Value FIRMWARE_VERSION (\S+)
Value INSTALL_DATE ([\w\s\d,:]+)

Start
 ^${FIRMWARE_VERSION}\s+${INSTALL_DATE} -> Record