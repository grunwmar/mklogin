#!/usr/bin/sh
git clone ... .mklogin_inst
cd .mklogin_inst
zsh install.zsh
cd ..
rm -rf .mklogin_inst