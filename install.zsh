#!/usr/bin/zsh
export LOGINS="$HOME/logins"
export LOGIN_SRC="$HOME/.local/share/mklogin"

if ! [[ -d $LOGINS ]]; then
    mkdir -p $LOGINS
fi

if ! [[ -d $LOGIN_SRC ]]; then
  mkdir -p $LOGIN_SRC
fi

cp ./mk_login.py $LOGIN_SRC/mk_login.py

chmod  +x $LOGIN_SRC/mk_login.py

if [[ -d /usr/bin/share ]]; then
  sudo ln -s $LOGIN_SRC/mk_login.py /usr/bin/mklogin
else
  if [[ -d /data/data/com.termux/files/usr/bin ]]; then
    mkdir -p /data/data/com.termux/files/usr/bin
    ln -s $LOGIN_LOGIN_SRC/mk_login.py /data/data/com.termux/files/usr/bin/mklogin
  fi
fi