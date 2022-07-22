Resetting passwords
Bypassing access controls to compromise protected data
Editing software configurations
Enabling persistence
Changing the privilege of existing (or new) users
Execute any administrative command

Enumeration commands
- hostname
- uname -a
- lsb_release -a
- /proc/version
- /etc/issue
- ps
- env
- sudo -l
- ls
- id
- /etc/passwd
- history
- ifconfig
- ip route
- netstat --pant

find commands
find . -name flag1.txt
find /home -name flag1.txt
find / -type d -name config
find / -type f -perm 0777  - (files readable, writable, and executable by all users)
find / -perm a=x   : find executable files
find /home -user frank   : find all files for user “frank” under “/home”
find / -mtime 10   : find files that were modified in the last 10 days
find / -atime 10   : find files that were accessed in the last 10 day
find / -cmin -60   : find files changed within the last hour (60 minutes)
find / -amin -60   : find files accesses within the last hour (60 minutes)
find / -size 50M

find / -writable -type d 2>/dev/null : Find world-writeable folders
find / -perm -222 -type d 2>/dev/null: Find world-writeable folders
find / -perm -o w -type d 2>/dev/null: Find world-writeable folders

find / -name perl*
find / -name python*
find / -name gcc*

## Automated Enumeration - links
LinPeas: https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite/tree/master/linPEAS
LinEnum: https://github.com/rebootuser/LinEnum
LES (Linux Exploit Suggester): https://github.com/mzet-/linux-exploit-suggester
Linux Smart Enumeration: https://github.com/diego-treitos/linux-smart-enumeration
Linux Priv Checker: https://github.com/linted/linuxprivchecker