#!/usr/bin/python2

import sys,os,commands,re, argparse, time

def log(msg='', t = 1):
	print msg
	time.sleep(t)

if __name__=="__main__":
	parser = argparse.ArgumentParser()
	
	parser.add_argument("-d","--debug",action='store_true',default=False,
		help = 'debug mode')

	parser.add_argument("-f","--full",action='store_false',default=True,
		help = 'do not replace $HOME with tilde')
	parser.add_argument("-w",'--head',action='store_true',default=False,
		help = 'trim condensed path to show only upper most folder')
	parser.add_argument("-t","--tail",action='store_true',default=False,
		help = 'return whole path minus last folder')
	parser.add_argument("-n",default=False,action='store_true',
		help = 'add leading newline character')

	parser.add_argument("length",default=30,nargs='?',type=int,
		help = 'total (max) length of (condensed) path')
	parser.add_argument("density",default=6,nargs='?',type=int,
		help = 'stop condensing after this many maximally condensed paths')
	args = parser.parse_args()
	if args.head and args.tail:
		# if querying for both head and tail, then ignore both
		args.head=False
		args.tail=False

	path=commands.getoutput("pwd")
	if args.full:
		# tilde will be added on at the very end
		path=path.replace(os.environ['HOME'],"")
		# adding tilde will add to resulting path length
		args.length-=1
	toodense = re.compile ( r"(\/\w){%s,}" % args.density )
	
	# :start
	if args.debug:
		log(path)
		args.n = True
	while len(path)>args.length:
		if toodense.match(path): # if it gets too condensed
			break
		else:
			dirs = path.split("/")
			x=0
			while x < len(dirs):
				if len(dirs[x])>1: # if longer than a single char
					dirs[x]=dirs[x][:-1] # delete last char and goto :start
					path = "/".join(dirs)
					if args.debug:
						log(path)
					break
				else:
					x+=1 # try next
			if len(dirs)*2>=len(path):
				log("[break]")
				# break when reaching maximum compactness
				break
	
	if args.full and os.environ['HOME'] in commands.getoutput("pwd"):
		path="~"+path
		if args.debug:
			log("[-f]\n"+path)

	if args.tail:
		if path=="~":
			path=""
		else:
			path = "/".join(path.split("/")[:-1])+"/"
		if args.debug:
			log("[-t]\n"+path)

	if args.head:
		path = path.split("/")[-1]
		if args.debug:
			log("[-h]\n"+path)

	sys.stdout.write(path)
	if args.n:
		sys.stdout.write("\n")
