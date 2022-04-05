Value Filldown Rollback_FW_Version ([\S]+)
Value Filldown Current_FW_Version ([\S]+)
Value Filldown BMC_FW_Version ([\S]+)
Value Filldown Kernel ([\S]+)
Value Filldown SWITCH_CPLD_VERSION ([\S\s]+)
Value Filldown FAN_CPLD_VERSION ([\S\s]+)
Value Filldown POWER_CPLD_VERSION ([\S\s]+)
Value Filldown FPGA_CPLD_VERSION ([\S]+)
Value Filldown System_Uptime ([\d,\sdays\(\)\:]+)
Value Service_name ([\w\-]+)
Value Current ([\d\.]+)
Value Rollback ([None|\d\.]+)
Value Ready ([tTrue|fFalse]+)
Value State ([\w\-]+)
Value Restarts ([\d]+)

Start
 ^\s*Current Firmware Version:\s+${Current_FW_Version}
 ^\s*Rollback Firmware Version:\s+${Rollback_FW_Version}
 ^\s*BMC Firmware Version:\s+${BMC_FW_Version}
 ^\s*Kernel:\s+${Kernel}
 ^Switch Board CPLD Version:\s+${SWITCH_CPLD_VERSION}
 ^Fan Board CPLD Version:\s+${FAN_CPLD_VERSION}
 ^Power Board CPLD Version:\s+${POWER_CPLD_VERSION}
 ^FPGA Version:\s+v${FPGA_CPLD_VERSION}
 ^\s*System\s*Uptime:\s*${System_Uptime}
 ^\s*${Service_name}\s+${Current}\s+${Rollback}\s+${Ready}\s+${State}\s+${Restarts} -> Record
