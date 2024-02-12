#!/usr/bin/sh
# https://raw.githubusercontent.com/grunwmar/mklogin/main/web_install.sh
git clone https://github.com/grunwmar/mklogin.git .mklogin_inst
cd .mklogin_inst
zsh ./install.zsh
cd ..
rm -rf .mklogin_inst