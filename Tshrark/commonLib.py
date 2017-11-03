#!/usr/bin/python
import pdb
import sys
import os
import re
from optparse import OptionParser

class commonLib(object) :
	
	def __init__(self,parser) :
		self.parser=parser	
	def cmdLineParser(self) :
		
		self.parser.add_option("-a", "--apmac",type="string",help='XX:XX:XX:XX:XX:XX  <e. g> 11:22:33:44:55:66'
     			)
		self.parser.add_option("-s", "--stamac", metavar='N' , type="string" ,nargs=1 ,help='STA-MAC address <e.g> 11:22:33:44:55:66'
                  )
		self.parser.add_option("-f", "--file",type="string"
                      ) 

		self.parser.add_option("-p","--packet",type="string")
				
		return  self.parser.parse_args() 

	def checkargs(self,args) :
		if len(args) == 3 :
			self.apmac=sys.argv[1]
			self.stamac=sys.argv[2]
			self.pcap=sys.argv[3]
			self.checkmac(self.apmac)
			if not status :
				raise ValueError('AP mac address  is not in proper format'.upper())
                
			status=self.checkmac(self.stamac)
			if not status :
				raise ValueError('STA mac address  is not in proper format'.upper())
                
			status=self.checkfiletype(self.pcap)
			if not status :
				raise ValueError('filename  is not present  under provided directory or its not in pcap format'.upper())
		
			return (self.apmac,self.stamac,self.pcap)

		elif len(args) ==0 :
			pass
		
		else :
			print "USAGE : => python %s <apmac> <stamac> <pcap>"%sys.argv[0]
		

	def checkparseopts(self,options) :
		self.apmac=options.apmac
		
                self.stamac=options.stamac
		
                self.pcap= options.file
                status=self.checkmac(self.apmac)
		
		if not status :
			raise ValueError('AP mac address  is not in proper format'.upper())
                
		status=self.checkmac(self.stamac)
		if not status :
			raise ValueError('STA mac address  is not in proper format'.upper())
                
		status=self.checkfiletype(self.pcap)
		#print "status of file  %s"%status
		if not status :
			raise ValueError('filename  is not present or its not in pcap format'.upper())
		return (self.apmac,self.stamac,self.pcap)


	def  checkmac(self,mac) :
    		if mac.count(":")!=5:
        		return False
    		for i in mac.split(":"):
        		for j in i:
            			if not ( ( j <"F" or j > "A" or j.isdigit() ) or len(i) ==2 ):
                			return False
    		return True
	
	def checkfiletype(self,filename) :
		if not os.path.isfile(filename) :
			return False
		if not filename.endswith('cap') :
			return False
		return True 	

	
class sniffer(commonLib) :

	def __init__(self,options) :
	 	self.apmac=options[0]
		self.stamac=options[1]
		self.pcap=options[2]
		

	def  readpacket(self,filter1) :
		f=" \" wlan.addr == %s && wlan.addr== %s  && %s \" "%(self.apmac,self.stamac,filter1)
		command= "tshark -r %s -Y %s | grep -i eapol "%(self.pcap,f)
		#print command 
		out= os.popen(command).read()
		try :
			return re.findall(r'(\d+)\s*(\d+.\d+)\s*.*eapol(.*)',out,re.I)
			
		except Exception as e :
			print "Exception caught during tshark parsing %s"%e
			return False

	
			 		





if __name__ == "__main__" :
	pass
		#s	print len(options)


	
	
