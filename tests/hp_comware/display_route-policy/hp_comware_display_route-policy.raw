Route-policy: ACTIVE_OUT
  Permit : 10
         if-match ip address prefix-list pl_customer_only

Route-policy: BACKUP_ACT_OUT
  Permit : 10
         if-match ip address prefix-list pl_customer_only
         apply community 1111:135
  Deny   : 99

Route-policy: BACKUP_SBY_OUT
  Permit : 10
         if-match ip address prefix-list pl_customer_only
         apply community 1111:130
  Deny   : 99
