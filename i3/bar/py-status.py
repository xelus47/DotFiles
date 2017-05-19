#!/usr/bin/python2


import sys,time,os,json, argparse

class i3block():
	def __init__(self,text="Initial text"):
		self.full_text=text
		self.name="i3customstatus.text.Text"
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
		self.instance=str(long((time.time() + 0.5) * 100000))
		self._fields=['full_text','name','markup','urgent','instance',
			'short_text','color','background','border','min_width',
			'align','separator','separator_block_width']
	def __str__(self):
		return json.dumps(self.obj())
	def obj(self):
		obj={}
		for x in self._fields:
			if x not in dir(self) or getattr(self,x)=='':
				continue
			obj[x]=getattr(self,x)
		return obj


def build():
	
	#txt1=i3block('Test')

	clock=i3block(time.strftime('%A W%W %x  %X'))
	
	#txt2=i3block('<span font_weight="bold" foreground="blue">Blue text</span> <i>is</i> cool!')


	return [
		#txt1.obj(), 
		clock.obj(), 
		#txt2.obj()
		]

if __name__=="__main__":
	print( '{\"version": 1, "click_events": false}\n[\n[],')

	#time.sleep(2)
	while True:
		print json.dumps(build()) + ","
		time.sleep(2)
		
