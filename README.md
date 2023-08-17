# ssh-deploy

ssh-deploy is a command-line utility designed to facilitate remote operations over SSH. With a focus on simplicity and flexibility, this tool allows users to execute commands on remote servers and transfer files, making it a valuable asset for system administrators and developers alike.

## Features

- **Remote Command Execution**: Run multiple commands on a remote server with ease.
- **File Transfer**: Send files to a specified remote directory.
- **Cross-Platform**: Works with remote Linux and Windows hosts.
- **Real-Time Output**: View command output in real-time, just like a local terminal.

## Requirements

- Python 3.x
- Paramiko library

## Installation

Clone the repository and install the required dependencies:

```bash
git clone https://github.com/Piatnytskyi/ssh-deploy.git
pip install paramiko
```

## Usage

### Transfer Files:

Transfer specified files to a remote path:

```bash
python transfer script.py --host HOST --username USERNAME --password PASSWORD --files file1.txt file2.txt --remote-path /remote/path
```

### Execute Command:

Execute specified command on a remote host:

```bash
python execute script.py --host HOST --username USERNAME --password PASSWORD --command "cmd1"
```

## Contribution

We welcome contributions from the community. Feel free to submit issues, feature requests, and pull requests!
