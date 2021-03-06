#!/usr/bin/env python

import colorama
colorama.init()

hide_path= "…" 
hide_path_length=1



import os,sys

args = sys.argv[1:]

current_path=os.getcwd()
# change $HOME to "~"
home = os.getenv("HOME")
current_path = current_path.replace(home,'~')

dirs = current_path.split("/")
for i in range(len(dirs)):
	if len(dirs[i])>12:
		cut = 12 - hide_path_length
		dirs[i]=dirs[i][:cut]+hide_path
path = "/".join(dirs)
if '-bs' in args or '--basename' in args:
	sys.stdout.write(os.path.basename(path))
else:
	sys.stdout.write(path)
