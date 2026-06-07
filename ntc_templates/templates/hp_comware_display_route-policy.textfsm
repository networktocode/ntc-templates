Value Filldown POLICY_NAME (\S+)
Value Required ACTION (Permit|Deny)
Value Required NODE (\d+)
Value List IF_MATCH (.+)
Value List APPLY (.+)

Start
  ^Route-policy:\s+ -> Continue.Record
  ^Route-policy:\s+${POLICY_NAME}\s*$$
  ^\s+(Permit|Deny)\s+:\s+\d+ -> Continue.Record
  ^\s+${ACTION}\s+:\s+${NODE}\s*$$
  ^\s+if-match\s+${IF_MATCH}\s*$$
  ^\s+apply\s+${APPLY}\s*$$
  ^\s*$$ -> Record
  ^. -> Error
