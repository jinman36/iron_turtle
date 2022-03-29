# John the Ripper Notes
[SecLists](https://github.com/danielmiessler/SecLists)

>
rockyou.txt wordlist from the SecLists repository under the /Passwords/Leaked-Databases subsection. You may need to extract it from .tar.gz format, using tar xvzf rockyou.txt.tar.gz.
>

- basic use for wordlists
- john --wordlist=[path to wordlist] [path to file]

# Identifying hashing
- occasionally john cant identify hashes correctly - use the following to identify the hash type
  - wget https://gitlab.com/kalilinux/packages/hash-identifier/-/raw/kali/master/hash-id.py
  - and then run the following to identify the hash
    python3 hash-id.py

# Format-specific Cracking
- john --format=[format] --wordlist=[path to wordlist] [path to file]

# Unshadowing
- unshadow [path to passwd] [path to shadow]
- unshadow - invokes the unshadow tool
- [path to passwd] - the file that contains thecopy of the /etc/passwd file youve taken from the tarrget machine
- [path to shadow] - file that contains the copy of th e/etc/shadow file youve taken from the target machine
 - Example
    - unshadow local_passwd local_shadow > unshadowed.txt

# Single Crack mode
- john --single --format=[format] [path to file]

