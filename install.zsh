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

if [[ -d /usr/sbin ]]; then
  sudo ln -s $LOGIN_SRC/mk_login.py /usr/sbin/mklogin
  else
  cp ../.mklogin_inst .mklogin
  ln -s $HOME/.mklogin/mk_login.py $HOME/mklogin
fi
