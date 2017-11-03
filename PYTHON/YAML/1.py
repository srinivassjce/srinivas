#!/usr/bin/env python
# -*- coding: utf-8 -*-
import yaml
import re
import requests
import sys
import os

class  yaml_parsing() :

	def __init__(self):
		pass
	
	def readyaml(self,filename):
		self.filename=filename
		with open (self.filename,'r') as f :
			data=yaml.load_all(f)
			return data

	def writeyaml(self,filename1,data) :

		self.filename1=filename1
		self.data=data

		with open(filename1,"w")  as fd :
			yaml.dump(self.data,fd)




if __name__ == "__main__" :
	print __name__
	y=yaml_parsing()
	data=y.readyaml('1.yaml')
	for doc in data:
    		for k,v in doc.items():
       			print k, "->", v
    			print "\n",	
	y.writeyaml('2.yaml',data)

	


