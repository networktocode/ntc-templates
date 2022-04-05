Value acl_type (ipv6|ip|mac)
Value acl_name ([\w+-]+)
Value seq_num (\d+)
#Value acl_params ([\w+\s+]+)
Value acl_params (.*)

Start
  ^${acl_type}\s+access-list\s+${acl_name}\s*
  ^\s*seq\s+${seq_num}\s+permit\s+${acl_params} -> Continue.Record
