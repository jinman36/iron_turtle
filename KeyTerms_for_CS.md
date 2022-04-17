# Encryption

- Ciphertext - The result of encrypting a plaintext, encrypted data

- Cipher - A method of encrypting or decrypting data. Modern ciphers are cryptographic, but there are many non cryptographic ciphers like Caesar.

- Plaintext - Data before encryption, often text but not always. Could be a photograph or other file

- Encryption - Transforming data into ciphertext, using a cipher.

- Encoding - NOT a form of encryption, just a form of data representation like base64. Immediately reversible.

- Key - Some information that is needed to correctly decrypt the ciphertext and obtain the plaintext.

- Passphrase - Separate to the key, a passphrase is similar to a password and used to protect a key.

- Asymmetric encryption - Uses different keys to encrypt and decrypt.

- Symmetric encryption - Uses the same key to encrypt and decrypt

B- rute force - Attacking cryptography by trying every different password or every different key

- Cryptanalysis - Attacking cryptography by finding a weakness in the underlying maths

- Symmetric encryption - uses the same key to encrypt and decrypt the data. Examples of Symmetric encryption are DES (Broken) and AES. These algorithms tend to be faster than asymmetric cryptography, and use smaller keys (128 or 256 bit keys are common for AES, DES keys are 56 bits long).

- Asymmetric encryption - uses a pair of keys, one to encrypt and the other in the pair to decrypt. Examples are RSA and Elliptic Curve Cryptography. Normally these keys are referred to as a public key and a private key. Data encrypted with the private key can be decrypted with the public key, and vice versa. Your private key needs to be kept private, hence the name. Asymmetric encryption tends to be slower and uses larger keys, for example RSA typically uses 2048 to 4096 bit keys

### Using SSH keys to get a better shell
SSH keys are an excellent way to “upgrade” a reverse shell, assuming the user has login enabled (www-data normally does not, but regular users and root will). ***Leaving an SSH key in authorized_keys on a box can be a useful backdoor***, and you don't need to deal with any of the issues of unstabilised reverse shells like Control-C or lack of tab completion.
- ssh-keygen, ssh-copy-id, or manually copying the key into authorized_keys with cat

- Diffie Hellman Key Exchange(DH Key - Symmetric Keys)
  - Video - https://www.youtube.com/watch?v=NmM9HA2MQGI

- Reverse shells are when the target is forced to execute code that connects back to your computer. On your own computer you would use one of the tools mentioned in the previous task to set up a listener which would be used to receive the connection. Reverse shells are a good way to bypass firewall rules that may prevent you from connecting to arbitrary ports on the target; however, the drawback is that, when receiving a shell from a machine across the internet, you would need to configure your own network to accept the shell. This, however, will not be a problem on the TryHackMe network due to the method by which we connect into the network.
- Bind shells are when the code executed on the target is used to start a listener attached to a shell directly on the target. This would then be opened up to the internet, meaning you can connect to the port that the code has opened and obtain remote code execution that way. This has the advantage of not requiring any configuration on your own network, but may be prevented by firewalls protecting the target.

- Horizontal privilege escalation: This is where you expand your reach over the compromised system by taking over a different user who is on the same privilege level as you. For instance, a normal user hijacking another normal user (rather than elevating to super user). This allows you to inherit whatever files and access that user has. This can be used, for example, to gain access to another normal privilege user, that happens to have an SUID file attached to their home directory (more on these later) which can then be used to get super user access. [Travel sideways on the tree]

- Vertical privilege escalation (privilege elevation): This is where you attempt to gain higher privileges or access, with an existing account that you have already compromised. For local privilege escalation attacks this might mean hijacking an account with administrator privileges or root privileges. [Travel up on the tree]