# MK LOGIN
### Installation
```zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/grunwmar/mklogin/main/web_install.sh)"
```

example
```shell
~$ mklogin --user tester --host some-server.org
File created /home/user/logins/tester@some-server.org.login   
```

content of `tester@some-server.org.login` file
```zsh
#!/usr/bin/zsh
BASE=$(basename "$0")
PARSED=(${(s/@/)BASE})
USER=$PARSED[1]
HOST=$PARSED[2]; HOST=${HOST/.login/}; HOST=${HOST/.zsh/}

echo -e ">>> Login to" "\e[32m$USER\e[0m"@"\e[36m$HOST\e[0m >>>"

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
echo -e ">>> Exited from \e[32m$USER\e[0m"@"\e[36m$HOST\e[0m, duration= $DUR sec >>>"

```
