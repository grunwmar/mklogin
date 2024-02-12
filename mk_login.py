#!/usr/bin/python3
import os
import argparse
import sys

parser = argparse.ArgumentParser(description='Create ZSH login script for remote computer through secure shell')
parser.add_argument('--user', "-u", required=True, type=str,
                    help='username')
parser.add_argument('--host', "-H", required=True, type=str,
                    help='hostname')


def main(args):
    filename = f"{args.user}@{args.host}.login"
    script = """#!/usr/bin/zsh
BASE=$(basename "$0")
PARSED=(${(s/@/)BASE})
USER=$PARSED[1]
HOST=$PARSED[2]; HOST=${HOST/.login/}; HOST=${HOST/.zsh/}

echo -e ">>> Login to" "\033[32m$USER\033[0m"@"\033[36m$HOST\033[0m >>>"

LOGIN=$USER@$HOST

SSH_ID=$HOME/.ssh/id_$LOGIN

if ! [[ -f $SSH_ID ]]; then
    ssh-keygen -t rsa -f $HOME/.ssh/id_$LOGIN -N "" 1> /dev/null
    ssh-copy-id -i $SSH_ID $LOGIN &> /dev/null
fi
TIME_STAMP_1=$(date +%s)
ssh -i $SSH_ID $LOGIN
TIME_STAMP_2=$(date +%s)

DUR=$(((TIME_STAMP_2 - TIME_STAMP_1)))
echo -e ">>> Exited from \033[32m$USER\033[0m"@"\033[36m$HOST\033[0m, duration= $DUR sec >>>"

"""
    filepath = os.path.join(os.environ["HOME"], "logins", filename)
    with open(filepath, "w+") as f:
        f.write(script)
    os.system(f"chmod +x {filepath}")
    print(f"File created \033[92m{filepath}\033[0m")


if __name__ == "__main__":
    main(parser.parse_args())
