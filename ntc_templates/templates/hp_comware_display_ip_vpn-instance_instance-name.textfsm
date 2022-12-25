Value Required NAME ([^,]+)
Value Required ID (\d+)
Value RD (\d+:\d+)
Value List IPV4_EXPORT_RTS (\d+:\d+)
Value List IPV4_IMPORT_RTS (\d+:\d+)
Value List IPV6_EXPORT_RTS (\d+:\d+)
Value List IPV6_IMPORT_RTS (\d+:\d+)
Value DESCRIPTION (.*)
Value IPV4_EXPORT_POLICY (\S+)
Value IPV4_IMPORT_POLICY (\S+)
Value IPV4_TUNNEL_POLICY (\S+)
Value IPV6_EXPORT_POLICY (\S+)
Value IPV6_IMPORT_POLICY (\S+)
Value IPV6_TUNNEL_POLICY (\S+)
Value List INTERFACES ([^,]+)


Start
  ^\s*VPN-Instance\s+Name\s+and\s+(Index|ID)\s*:\s+${NAME}, ${ID}
  ^\s*Route\s+Distinguisher\s*:\s+${RD}
  ^\s*Description\s*:\s*${DESCRIPTION}
  # IPv4 targets (block)
  ^\s*Address-family|s+IPv4 -> AFIPv4
  # Export IPv4 targets (inline)
  ^\s*Export\s+VPN\s+Targets\s*:\s+${IPV4_EXPORT_RTS} -> Continue
  ^\s*Export\s+VPN\s+Targets\s*:(?:\s+\d+:\d+){1}\s+${IPV4_EXPORT_RTS},* -> Continue
  ^\s*Export\s+VPN\s+Targets\s*:(?:\s+\d+:\d+){2}\s+${IPV4_EXPORT_RTS},* -> Continue
  ^\s*Export\s+VPN\s+Targets\s*:(?:\s+\d+:\d+){3}\s+${IPV4_EXPORT_RTS},* -> Continue
  ^\s*Export\s+VPN\s+Targets\s*:(?:\s+\d+:\d+){4}\s+${IPV4_EXPORT_RTS},* -> Continue
  ^\s*Export\s+VPN\s+Targets\s*:(?:\s+\d+:\d+){5}\s+${IPV4_EXPORT_RTS},* -> Continue
  ^\s*Export\s+VPN\s+Targets\s*:(?:\s+\d+:\d+){6}\s+${IPV4_EXPORT_RTS},* -> Continue
  ^\s*Export\s+VPN\s+Targets\s*:
  # Import IPv4 targets
  ^\s*Import\s+VPN\s+Targets\s*:\s+${IPV4_IMPORT_RTS} -> Continue
  ^\s*Import\s+VPN\s+Targets\s*:(?:\s+\d+:\d+){1}\s+${IPV4_IMPORT_RTS},* -> Continue
  ^\s*Import\s+VPN\s+Targets\s*:(?:\s+\d+:\d+){2}\s+${IPV4_IMPORT_RTS},* -> Continue
  ^\s*Import\s+VPN\s+Targets\s*:(?:\s+\d+:\d+){3}\s+${IPV4_IMPORT_RTS},* -> Continue
  ^\s*Import\s+VPN\s+Targets\s*:(?:\s+\d+:\d+){4}\s+${IPV4_IMPORT_RTS},* -> Continue
  ^\s*Import\s+VPN\s+Targets\s*:(?:\s+\d+:\d+){5}\s+${IPV4_IMPORT_RTS},* -> Continue
  ^\s*Import\s+VPN\s+Targets\s*:(?:\s+\d+:\d+){6}\s+${IPV4_IMPORT_RTS},* -> Continue
  ^\s*Import\s+VPN\s+Targets\s*:
  # IPv4 policies
  ^\s*Import\s+Route\s+Policy\s*:\s+${IPV4_IMPORT_POLICY}
  ^\s*Export\s+Route\s+Policy\s*:\s+${IPV4_EXPORT_POLICY}
  ^\s*Tunnel\s+Policy\s*:\s+${IPV4_TUNNEL_POLICY}
  # Export IPv6 targets
  ^\s*IPv6\s+Export\s+VPN\s+Targets\s*:\s+${IPV6_EXPORT_RTS} -> Continue
  ^\s*IPv6\s+Export\s+VPN\s+Targets\s*:(?:\s+\d+:\d+){1}\s+${IPV6_EXPORT_RTS},* -> Continue
  ^\s*IPv6\s+Export\s+VPN\s+Targets\s*:(?:\s+\d+:\d+){2}\s+${IPV6_EXPORT_RTS},* -> Continue
  ^\s*IPv6\s+Export\s+VPN\s+Targets\s*:(?:\s+\d+:\d+){3}\s+${IPV6_EXPORT_RTS},* -> Continue
  ^\s*IPv6\s+Export\s+VPN\s+Targets\s*:(?:\s+\d+:\d+){4}\s+${IPV6_EXPORT_RTS},* -> Continue
  ^\s*IPv6\s+Export\s+VPN\s+Targets\s*:(?:\s+\d+:\d+){5}\s+${IPV6_EXPORT_RTS},* -> Continue
  ^\s*IPv6\s+Export\s+VPN\s+Targets\s*:(?:\s+\d+:\d+){6}\s+${IPV6_EXPORT_RTS},* -> Continue
  ^\s*IPv6\s+Export\s+VPN\s+Targets\s*:
  # Import IPv6 targets
  ^\s*IPv6\s+Import\s+VPN\s+Targets\s*:\s+${IPV6_IMPORT_RTS} -> Continue
  ^\s*IPv6\s+Import\s+VPN\s+Targets\s*:(?:\s+\d+:\d+){1}\s+${IPV6_IMPORT_RTS},* -> Continue
  ^\s*IPv6\s+Import\s+VPN\s+Targets\s*:(?:\s+\d+:\d+){2}\s+${IPV6_IMPORT_RTS},* -> Continue
  ^\s*IPv6\s+Import\s+VPN\s+Targets\s*:(?:\s+\d+:\d+){3}\s+${IPV6_IMPORT_RTS},* -> Continue
  ^\s*IPv6\s+Import\s+VPN\s+Targets\s*:(?:\s+\d+:\d+){4}\s+${IPV6_IMPORT_RTS},* -> Continue
  ^\s*IPv6\s+Import\s+VPN\s+Targets\s*:(?:\s+\d+:\d+){5}\s+${IPV6_IMPORT_RTS},* -> Continue
  ^\s*IPv6\s+Import\s+VPN\s+Targets\s*:(?:\s+\d+:\d+){6}\s+${IPV6_IMPORT_RTS},* -> Continue
  ^\s*IPv6\s+Import\s+VPN\s+Targets\s*:
  # IPv6 policies
  ^\s*IPv6\s+Import\s+Route\s+Policy\s*:\s+${IPV6_IMPORT_POLICY}
  ^\s*IPv6\s+Export\s+Route\s+Policy\s*:\s+${IPV6_EXPORT_POLICY}
  ^\s*IPv6\s+Tunnel\s+Policy\s*:\s+${IPV6_TUNNEL_POLICY}
  # Interfaces
  ^\s*Interfaces\s*:\s+${INTERFACES},* -> Continue
  ^\s*Interfaces\s*:(?:\s+[^,]+,){1}\s+${INTERFACES},* -> Continue
  ^\s*Interfaces\s*:(?:\s+[^,]+,){2}\s+${INTERFACES},* -> Continue
  ^\s*Interfaces\s*:(?:\s+[^,]+,){3}\s+${INTERFACES},* -> Continue
  ^\s*Interfaces\s*:(?:\s+[^,]+,){4}\s+${INTERFACES},* -> Continue
  ^\s{12,}${INTERFACES},* -> Continue
  ^\s{12,}(?:\s+[^,]+,){1}\s+${INTERFACES},* -> Continue
  ^\s{12,}(?:\s+[^,]+,){2}\s+${INTERFACES},* -> Continue
  ^\s{12,}(?:\s+[^,]+,){3}\s+${INTERFACES},* -> Continue
  ^\s{12,}(?:\s+[^,]+,){4}\s+${INTERFACES},* -> Continue
  # End of Interfaces
  ^\s*Interfaces\s*:
  ^\s{12,}
  # Drop
  ^\s*Create\s+time
  ^\s*Up\s+time
  ^\s*.*Maximum\s+Routes\s+Limit
  ^\s{4,}
  ^. -> Error

AFIPv4
  ^\s*Export\s+VPN\s+Targets -> ExportIPv4Targets

ExportIPv4Targets
  ^\s{4,}${IPV4_EXPORT_RTS} -> Continue
  ^\s{4,}(?:\s+\d+:\d+){1}\s+${IPV4_EXPORT_RTS} -> Continue
  ^\s{4,}(?:\s+\d+:\d+){2}\s+${IPV4_EXPORT_RTS} -> Continue
  ^\s{4,}(?:\s+\d+:\d+){3}\s+${IPV4_EXPORT_RTS} -> Continue
  ^\s{4,}(?:\s+\d+:\d+){4}\s+${IPV4_EXPORT_RTS} -> Continue
  ^\s{4,}(?:\s+\d+:\d+){5}\s+${IPV4_EXPORT_RTS} -> Continue
  ^\s{4,}(?:\s+\d+:\d+){6}\s+${IPV4_EXPORT_RTS} -> Continue
  ^\s{4,}\d+:\d+
  ^\s*Import\s+VPN\s+Targets -> ImportIPv4Targets
  ^. -> Error

ImportIPv4Targets
  ^\s{4,}${IPV4_IMPORT_RTS} -> Continue
  ^\s{4,}(?:\s+\d+:\d+){1}\s+${IPV4_IMPORT_RTS} -> Continue
  ^\s{4,}(?:\s+\d+:\d+){2}\s+${IPV4_IMPORT_RTS} -> Continue
  ^\s{4,}(?:\s+\d+:\d+){3}\s+${IPV4_IMPORT_RTS} -> Continue
  ^\s{4,}(?:\s+\d+:\d+){4}\s+${IPV4_IMPORT_RTS} -> Continue
  ^\s{4,}(?:\s+\d+:\d+){5}\s+${IPV4_IMPORT_RTS} -> Continue
  ^\s{4,}(?:\s+\d+:\d+){6}\s+${IPV4_IMPORT_RTS} -> Continue
  ^\s{4,}\d+:\d+
  ^. -> Error
