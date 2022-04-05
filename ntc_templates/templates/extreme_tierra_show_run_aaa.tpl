######################CLI output#########################
#ngnpb# show run aaa
#aaa authentication login tacacs+ local-auth-fallback
#aaa accounting commands default start-stop none
#####################parsed output#######################
#--- Header ---
#['Authentication', 'Accounting']
#--- Parsed Data ---
#[['tacacs+', 'tacacs+']]
#----------------------------------------
#--- Header ---
#['Authentication', 'Accounting']
#--- Parsed Data ---
#[['tacacs+', 'none']]
####################Parser###############################
Value Authentication ([\s+a-zA-Z\/]+)
Value Accounting ([\s+a-zA-Z\/]+)

Start
  ^\s*aaa\s+authentication\s+login\s+${Authentication}\s+local-auth-fallback
  ^\s*aaa\s+accounting\s+commands\s+default\s+start-stop\s+${Accounting} -> Record