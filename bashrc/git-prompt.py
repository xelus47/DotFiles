#!/usr/bin/env python2

import sys, commands, re

git_error_msg, gitmsg=commands.getstatusoutput('git status -sb --porcelain')

"""
      (branch)    up-to-date
?/AD  (branch *)  untracked files or changes (esp. added/removed files)
A/M/D (branch ^)  ready for commit: adds, mods and dels tracked
      (branch *^) ready for commit but missing some changes
"""

if git_error_msg==0:
	branch = gitmsg.split('\n')[0][3:]
	files = "\n".join(gitmsg.split('\n')[1:])
	status = ''
	regex = r"(?P<both>^[ADM]{2})|(?P<tracked>^[ADM])|(?P<untracked>^.[ADM]|\?\?)"
	matches = re.finditer(regex, files, re.MULTILINE)
	for match in matches:
		if match.group('untracked') is not None and "*" not in status:
			status = "*" + status

		if match.group('tracked') is not None and "^" not in status:
			status += "^"
			
		if match.group('both') is not None:
			status = " *^"

	if status!="":
		status = " " + status
	sys.stdout.write( "({branch}{status}) ".format(branch=branch,status=status) )
else:
	sys.stdout.write("")