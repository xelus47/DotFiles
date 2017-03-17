#!/usr/bin/env python2

import commands, sys
if __name__=="__main__":
	pactl_cmd="pactl "+" ".join(sys.argv[1:])
	# if [play] is not on your system, install sox
	commands.getstatusoutput(pactl_cmd)
	commands.getstatusoutput('play ~/DotFiles/assets/drip.ogg')


	# TODO: add error message
