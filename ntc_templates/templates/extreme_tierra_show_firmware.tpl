Value CURRENT_FW_VERSION ([\S]+)
Value ROLLBACK_FW_VERSION ([\S]+)
Value BMC_FW_VERSION ([\S]+)
Value KERNEL ([\S]+)
Value SWITCH_CPLD_VERSION ([\S\s]+)
Value FAN_CPLD_VERSION ([\S\s]+)
Value POWER_CPLD_VERSION ([\S\s]+)
Value FPGA_CPLD_VERSION ([\S]+)
Value SYSTEM_UPTIME ([\d,\sdays\(\)\:]+)

Start
 ^\s*Current Firmware Version:\s+${CURRENT_FW_VERSION}
 ^\s*Rollback Firmware Version:\s+${ROLLBACK_FW_VERSION}
 ^\s*BMC Firmware Version:\s+${BMC_FW_VERSION}
 ^\s*Kernel:\s+${KERNEL}
 ^Switch Board CPLD Version:\s+${SWITCH_CPLD_VERSION}
 ^Fan Board CPLD Version:\s+${FAN_CPLD_VERSION}
 ^Power Board CPLD Version:\s+${POWER_CPLD_VERSION}
 ^FPGA Version:\s+v${FPGA_CPLD_VERSION}
 ^\s*System\s*Uptime:\s*${SYSTEM_UPTIME}