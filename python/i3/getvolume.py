#!/usr/bin/env python

# DEPRECATED (because FUCK python3)

# i.e. python 3 is used because this file gets imported into bar-script

def getvolume():
	import sys, commands
	status, response = commands.getstatusoutput('pactl list sinks|grep Volume:\ front')
	if status==0:
		response = response.split('/')
		return response[1].replace(" ","")
	else:
		return "??"


if __name__=="__main__":
	print(getvolume())