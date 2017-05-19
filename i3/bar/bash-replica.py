#!/usr/bin/python2

import time, sys

if __name__ == "__main__":
	print '{ "version": 1 }'
	#sys.stdout.flush()
	print '['
	#sys.stdout.flush()
	print '[],'
	#sys.stdout.flush()
	while True:
		x = '{ "full_text": "%s", "color": "#bbaacc" }'%time.strftime("%X")
		print '[%s],'%x
		sys.stdout.flush()
		time.sleep(0.1)
		
