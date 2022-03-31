# John the Ripper Notes
[SecLists](https://github.com/danielmiessler/SecLists)

>
rockyou.txt wordlist from the SecLists repository under the /Passwords/Leaked-Databases subsection. You may need to extract it from .tar.gz format, using tar xvzf rockyou.txt.tar.gz.
>

- basic use for wordlists
- john --wordlist=[path to wordlist] [path to file]

# Identifying hashing ** Use this more**
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

# Custom Rules
- custom rule are defined by using 
  - john.config
- [List.Rules:RuleName] - is used to define the name of your rule

- Rules are defined using Regex identifiers
 - common examples are:
 - Az - Takes the word and appends it with the characters you define
- A0 - Takes the word and prepends it with the characters you define
- c - Capitalises the character positionally
- [0-9] - Will include numbers 0-9
- [0] - Will include only the number 0
- [A-z] - Will include both upper and lowercase
- [A-Z] - Will include only uppercase letters
- [a-z] - Will include only lowercase letters
- [a] - Will include only a
- [!£$%@] - Will include the symbols !£$%@

- example to run full custom password rule
  - john --wordlist=[path to wordlist] --rule=RuleName [path to file]

# Cracking password protected Zip files
- basic usage
  - zip2john [options] [zip file] > [output file]
  - john --wordlist=/usr/share/wordlists/rockyou.txt zip_hash.txt

  # Cracking Password protected RAR Files
  - rar2john [rar file] > [output file]
    -this works in theory but I couldnt get the attack box version of Kali to recognize rar2john command
    - before running the JTR basic command, it may be required to DL unrar to further read the unlocked rar file

    # cracking ssh with john
    - ssh2john [id_rsa.rar file] > id_rsa.txt
    - *** if john cannot find ssh2john (like me) run the following:
      - locate ssh2john
      - /opt/john/ssh2john.py

      - command to run will like the following
        - python3 /opt/john/ssh2john.py [id_rsa.rar file] > id_rsa.txt
        - john --wordlist=/usr/share/wordlists/rockyou.txt id_rsa.txt