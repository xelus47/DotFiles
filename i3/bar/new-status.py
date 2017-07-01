#!/usr/bin/python2
# -*- coding: utf-8 -*-

import threading,sys,time,os,json, argparse, commands, re

from ismuted import ismuted

class i3block():
	def __init__(self,text="Initial text"):
		self.full_text=text
		self.name=""
		self.markup="Pango"
		self.urgent=False
		self.short_text=''
		self.color=''
		self.background=''
		self.border=''
		self.min_width=''
		self.align=''
		self.separator=''
		self.separator_block_width=''
		#self.instance=str(long((time.time() + 0.5) * 100000))
		self.instance=''
		self._fields=['full_text','name','markup','urgent','instance',
			'short_text','color','background','border','min_width',
			'align','separator','separator_block_width']
	def __str__(self):
		return json.dumps(self.obj())
	def obj(self):
		# create object from NameSpace
		# skips properties equal to empty string or None
		obj={}
		for x in self._fields:
			if x not in dir(self) or getattr(self,x)=='' or getattr(self,x) is None:
				continue
			obj[x]=getattr(self,x)
		return obj


def mpc_song():
	query = commands.getstatusoutput("mpc --port 6601 current -f '[%title%]|[%file%]'")
	if query[0]!=0: # not OK
		return ("","")
	else:
		full = commands.getoutput("mpc --port 6601")
		try:
			l1=full.split("\n")[1]
			playstate = l1.split()[0]
			return (query[1], playstate)
		except IndexError:
			return ("","")

def df(path='/home',name=None):
	s = commands.getoutput("df -BG -h %s"%path)
	l = s.split('\n')[1]
	p,used = (l.split()[-1], l.split()[3])
	if name is not None:
		p=name
	return (p, used)


def readconfig(path="status"):
	f = open(path)
	data = f.read()
	f.close()
	# remove comments
	for line in data.split("\n"):
		if len(line.split("#"))>1:
			data=data.replace(line,"#".join(line.split("#")[:-1]),1) # all except the last cardinal
	
	# remove empty lines
	while re.search(r'\n\n',data):
		data = re.sub(r"\n\n","\n", data)
	
	# purge final \n
	if re.search(r"\n$",data):
		data = re.sub(r"\n$","", data)

	return data



def get_volume():
	volume = commands.getoutput('cd ~/DotFiles/i3/bar && ./getvolume.sh')
	muted = bool(int(commands.getoutput('cd ~/DotFiles/i3/bar && ./ismuted.py'))) # returns '0' or '1'
	if muted:
		return "<s>%s</s>"%volume
	else:
		return volume


def build():
	
	clock=i3block(time.strftime('  <span foreground="#cc11aa">%x</span>   <span foreground="#bbaacc"><big>%H:%M</big></span>  '))
	clock.name="clock"	

	txt2=i3block('<span font_weight="bold" foreground="blue">Blue text</span> <i>is</i> cool! ')

	usage_home=i3block('%s <span foreground="#cc8811">%s</span>'%df('/home'))
	usage_root=i3block('%s <span foreground="#cc8811">%s</span>'%df('/'))
	usage_ext=i3block('%s <span foreground="#cc8811">%s</span>'%df('/dev/sdh1','/dev/sdh1'))

	volume = i3block(u'♪ <span weight="bold" foreground="#dd5555">%s</span>' % get_volume())
	songdat=mpc_song()
	if songdat[1]=='[paused]':
		song = i3block(" <span color='#666'>[%s]</span> "%songdat[0])
	elif songdat[0]=='':
		song = i3block(" <span color='#666'>[off]</span> ")
	else:
		song = i3block(' <i>%s</i> '% songdat[0])

	return [
		song.obj(),
		volume.obj(),
		usage_root.obj(),
		usage_home.obj(),
		usage_ext.obj(),
		clock.obj(), 
		]


if __name__=="__main__":
	# TODO add argparse option for timeout between draws

	print "\""+readconfig()+"\""

	#print( '{\"version": 1, "click_events": false}\n[\n[],')
	# print '{ "version": 1, "click_events": true}'
	# print '['
	# print '[],'	


	#time.sleep(2)
	# while True:
		# print json.dumps(build()) + ","
		# sys.stdout.flush()
		#log = open('log.txt','w')
		#log.write(sys.stdin.readline())
		#log.close()
		# time.sleep(1)
		
