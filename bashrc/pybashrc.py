#!/usr/bin/python2

import commands, os, sys


if __name__=="__main__":
	ps1=r""
	ps1+=r"\[\e[0m\]"
	ps1+=r"\u@\h (alex)  \W $ "
	sys.stdout.write(ps1)
