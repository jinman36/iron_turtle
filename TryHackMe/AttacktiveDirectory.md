> sudo nmap -A -Pn 10.10.156.178 -vv

I had to install go to install kerbrute - the other methods didnt seem to work really well

> kerbrute -users '/home/Desktop/THM/Attacktive/userlist' -dc-ip $IP -domain spookysec.local