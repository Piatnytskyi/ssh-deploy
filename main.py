import sys
import os
import paramiko
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Deploy and run a script on a remote host, along with its dependencies.')
    parser.add_argument('--host', help='Remote hostname or IP', required=True)
    parser.add_argument('--username', help='Username for remote host', required=True)
    parser.add_argument('--password', help='Password for remote host', required=True)
    parser.add_argument('--script', help='Script to run on remote host', required=True)
    parser.add_argument('--dependencies', help='Dependency files for the script', required=True, nargs='*')

    args = parser.parse_args()

    if not args.host or not args.username or not args.password or not args.script:
        print("Please provide host, username, password, and script.")
        sys.exit(1)

    # Connect to remote host
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(args.host, username=args.username, password=args.password)

    # Setup sftp connection and transmit the specified script and dependencies
    sftp = client.open_sftp()
    remote_script = '/tmp/' + os.path.basename(args.script)
    sftp.put(args.script, remote_script)
    if args.dependencies:
        for dependency in args.dependencies:
            sftp.put(dependency, '/tmp/' + os.path.basename(dependency))
    sftp.close()

    # Run the transmitted script remotely without args and show its output.
    print(f"Executing {remote_script} ...")
    stdout = client.exec_command(f'python {remote_script}')[1]
    for line in stdout:
        # Process each line in the remote output
        print(line.strip())

    client.close()
    sys.exit(0)
