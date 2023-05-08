# 0x10. HTTPS SSL

## HTTP(Hypertext Transfer Protocol) 
- protocol used to transfer data over the internet.
- an application layer protocol that uses the __TCP/IP__ protocol to transfer data.
- it is stateless protocol therefore each reqquests is independent and does not rely on previous requests.


## SSL(Secure Sockets Layer) 
- Security protocol used to establish a secure and encrypted connection between a client and server.
- It is used tp protect sensitive informatiom such as passwords ,credit card numbers and personal informationfrom being intercepted and stollen by attackers.
- it is replaced by __TLS(Transport Layer Security)__ a s primary security protocol for the internet but to refer to __TLS__.

## HTTPS(HTTP Secure)
- is an extension of HTTP that uses __SSL/TLS__ to encrypt the data being transferred between a client and server.
- Used to provide a secure and encrypted connection for websites that handle sensitive information such as online bankin or e-commerce websites.
- it uses __SSL/TLS__ to create a scure connection between a clinet and server therefore it ensures that all the data exchanged between them is encrypted and protected from intercption and tampering by attackers.

## Resources

**Read or watch**:

- [What is HTTPS?](https://intranet.alxswe.com/rltoken/XT1BAiBL3Jpq1bn1q6IYXQ "What is HTTPS?")
- [What are the 2 main elements that SSL is providing](https://intranet.alxswe.com/rltoken/STj5WkAPACBxOvwB77Ycrw "What are the 2 main elements that SSL is providing")
- [HAProxy SSL termination on Ubuntu16.04](https://intranet.alxswe.com/rltoken/mJNlqZkTBxIxM2bpDK_VoA "HAProxy SSL termination on Ubuntu16.04")
- [SSL termination](https://intranet.alxswe.com/rltoken/CKUICfppIWI6UC0coEMB8g "SSL termination")
- [Bash function](https://intranet.alxswe.com/rltoken/zPjZ7-eSSQsLFsGA16C1HQ "Bash function")

**man or help**:

- `awk`
- `dig`

## Learning Objectives

you are expected to be able to explain to anyone:

### General

- What is HTTPS SSL 2 main roles
- What is the purpose encrypting traffic
- What SSL termination means

## Requirements

### General

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted on Ubuntu 16.04 LTS
- All your files should end with a new line
- A `README.md` file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- Your Bash script must pass `Shellcheck` (version `0.3.7`) without any error
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all your Bash scripts should be a comment explaining what is the script doing
