# 0x0C. Web server

## Resources

**Read or watch**:

- [How the web works](https://intranet.alxswe.com/rltoken/6TI3HiyFdwrbXWKVF24Gxw "How the web works")
- [Nginx](https://intranet.alxswe.com/rltoken/vkVMGlaf39j2DWAQWzo6EA "Nginx")
- [How to Configure Nginx](https://intranet.alxswe.com/rltoken/zKrpVxWuUHVdW4URAjdFbw "How to Configure Nginx")
- [Child process concept page](https://intranet.alxswe.com/rltoken/Ar18u5sRis1fkvkVgzdcqg "Child process concept page")
- [Root and sub domain](https://intranet.alxswe.com/rltoken/xi3peVqYl02PfpHHHlCtxQ "Root and sub domain")
- [HTTP requests](https://intranet.alxswe.com/rltoken/sBrrP4EAmI3NoYjIgZrUhw "HTTP requests")
- [HTTP redirection](https://intranet.alxswe.com/rltoken/Eaa4ZuKvye941hTkP8VlBQ "HTTP redirection")
- [Not found HTTP response code](https://intranet.alxswe.com/rltoken/eJSp2QFTY6jqqNtz8OVDEw "Not found HTTP response code")
- [Logs files on Linux](https://intranet.alxswe.com/rltoken/7WMNY5CWD-CBrxmQrdmfPg "Logs files on Linux")

**For reference:**

- [RFC 7231 (HTTP/1.1)](https://intranet.alxswe.com/rltoken/BGa6RrS0dnM6EdBGS_ZDUw "RFC 7231 (HTTP/1.1)")
- [RFC 7540 (HTTP/2)](https://intranet.alxswe.com/rltoken/IZ2fyYn1qNZ9RXXsg5vG1g "RFC 7540 (HTTP/2)")

**man or help**:

- `scp`
- `curl`

## General

- What is the main role of a web server
- What is a child process
- Why web servers usually have a parent process and child processes
- What are the main HTTP requests

### DNS

- What DNS stands for
- What is DNS main role

### DNS Record Types

- `A`
- `CNAME`
- `TXT`
- `MX`

### Copyright - Plagiarism

- You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
- You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
- You are not allowed to publish any content of this project.
- Any form of plagiarism is strictly forbidden and will result in removal from the program.

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
- You can’t use `systemctl` for restarting a process
