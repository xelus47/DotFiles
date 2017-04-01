#!/usr/bin/env python2

def ismuted():
	import sys, commands
	status, response = commands.getstatusoutput('pactl list sinks|grep Mute:\ no')
	return response==""


if __name__=="__main__":
	print(ismuted())