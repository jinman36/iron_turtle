What does nmap stand for?
Network Mapper
How do you specify which port(s) to scan?
-p
How do you do a "ping scan"(just tests if the host(s) is up)?
-sN
What is the flag for a UDP scan? 
-sU
How do you run default scripts?
-sC
How do you enable "aggressive mode"(Enables OS detection, version detection, script scanning, and traceroute)
-A
What flag enables OS detection
-O
How do you get the versions of services running on the target machine    
-sV
Port Scan Type	    Example Command
TCP Connect Scan	  nmap -sT 10.10.33.135
TCP SYN Scan	      sudo nmap -sS 10.10.33.135
UDP Scan	          sudo nmap -sU 10.10.33.135

These scan types should get you started discovering running TCP and UDP services on a target host.

Option	                Purpose
-p-	                    all ports
-p1-1023	              scan ports 1 to 1023
-F	                    100 most common ports
-r	                    scan ports in consecutive order
-T<0-5>	                -T0 being the slowest and T5 the fastest
--max-rate 50	          rate <= 50 packets/sec
--min-rate 15	          rate >= 15 packets/sec
--min-parallelism 100	  at least 100 probes in parallel