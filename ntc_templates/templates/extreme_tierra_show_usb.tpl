######################CLI output#########################
#S3_PB1# show usb
#USB Enabled:  true
#####################parsed output#######################
#--- Header ---
#['USB_status']
#--- Parsed Data ---
#[['false']]
#--- Header ---
#['USB_status']
#--- Parsed Data ---
#[['true']]
####################Parser###############################
Value USB_status (\w+)

Start
 ^USB Enabled:  ${USB_status}