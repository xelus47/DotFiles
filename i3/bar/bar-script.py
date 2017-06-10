#!/usr/bin/env python

from i3pystatus import Status, get_module
import subprocess
from requests import get


@get_module
def change_text(self):
	self.output['text']='Clicked text'


def update_ext_ip():
	# This example requires the requests library be installed.  You can learn more
	# about the Requests library here: http://docs.python-requests.org/en/latest/
	from requests import get

	ip = get('https://wtfismyip.com/text').text
	file = open('/home/alexander/DotFiles/python/i3/ip.txt','w')
	file.write(ip)
	file.close()

def ext_ip():
	file = open('/home/alexander/DotFiles/python/i3/ip.txt','r')
	ip=file.read()
	file.close()

if __name__=="__main__":

	update_ext_ip()

	status = Status()
	# Displays clock like this:
	# Tue 30 Jul 11:59:46 PM KW31
	#                          ^-- calendar week
	status.register("clock",format="%a %-d %b %X KW%V",)
	status.register("text",
		text="Initial text",
		on_rightclick=change_text,
		)

	"""
	status.register("disk",
		path='/mnt/Elements',
		format="external {free}"
		)

	status.register("disk",
		path='/',
		format="root {free}"
		)
	"""

	status.run()