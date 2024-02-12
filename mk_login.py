import  os
import argparse
import sys

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--user',"-u", type=str,
                    help='username')
parser.add_argument('--host',"-H", type=str,
                    help='hostname')


def main(args):
    pswd = ""

    filename = f"{args.user}@{args.host}.login"
    script="""#!/usr/bin/zsh
BASE=$(basename "$0")
PARSED=(${(s/@/)BASE})
USER=$PARSED[1]
HOST=$PARSED[2]; HOST=${HOST/.login/}; HOST=${HOST/.zsh/}
echo -e "Login to" "\e[32m$USER\e[0m"@"\e[36m$HOST\e[0m"
LOGIN=$USER@$HOST

SSH_ID=$HOME/.ssh/id_$LOGIN

if ! [[ -f $SSH_ID ]] {
ssh-keygen -t rsa -f $HOME/.ssh/id_$LOGIN -N ""
ssh-copy-id -i $HOME/.ssh/id_$LOGIN
}

ssh "$LOGIN"

    """

    with open(filename, "w+") as f:
        f.write(script)
    os.system(f"chmod +x {filename}")

if __name__ == "__main__":
    main(parser.parse_args())