Value direction (RX|TX)
Value ethernet (\d+\/\d+)
Value packets (\d+)

Start
 ^\s*All\s+protocol\s+${direction}\s+capture\s+is\s+enabled\s+on\s+interface\s+Eth\s+${ethernet}\.\s*(Number\s+of\s+packet\s+to\s+capture\s+${packets}\.)?\s* -> Record
