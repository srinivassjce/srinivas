#############
'''Script to validate the fourway handshake using tshark'''
###########3
import re
import pprint
import os
import sys
import logging
from optparse import OptionParser
import pdb
from termcolor import colored, cprint
from pythonds.basic.stack import Stack
import time

try :
	#import constants
	from commonLib import *

except Exception as err :
	print "unbale to import the library package -%s"%err


#####Generic Result variable###############
class Global :
	
	comment=""
	result = True
	
	
#data=os.system("tshark -r /home/act/Downloads/2016.07.26_17-37-39-GMT+5_30.wcap  -Y 'eapol '  | awk '{print $1 }' ")
class validation(Global) :
	
	def __init__(self) :
		self.eapol={}
	
	def startup(self) :
        	c=commonLib(OptionParser())
        	(self.options,self.args)=c.cmdLineParser()
		if len(self.args) == 3  and len(sys.argv) == 3:
        		return c.checkargs(self.args)
		elif len(self.args) == 0 and len (sys.argv) > 6 :
			return c.checkparseopts(self.options)
	
		else :
			usage1= "python %s <ap_mac> <sta_mac> <pcap_file>"%sys.argv[0]
			usage2= """python script_name [--apmac/-a]  AP_MAC_ADDRESS [--stamac/-s] STA_MAC_ADDRESS [-f/--file] pcap file] [--packet/-p] packet_type	
				---packet/-p optional field  e.g -p deauth
				-a ,-s,-f or --apmac, --stamac , --file  are mandatory filed 
				\n"""	 	
			print "USAGE :=> \n"+usage1 + " \n\n" + "\t\tOR"+"\n\n" + usage2 
			sys.exit(0)
	

	def parser(self,parser_args) :
		self._sniff_object=sniffer(parser_args)
		status=self._sniff_object.readpacket('eapol')
		
		if not status :
			Global.comment += " EAPOL handshake FAIL ".upper()	
			Global.result &= False
			return (Global.result,Global.comment)
		return status
			
	def checkeapolseq(self,parse_out) :
		list_eapol = ['first','1','second','2','third','3','four','4' ]
		self.flag=True
		self.eapolstack = Stack()

		def seqcatcher(key,index,flag) : 
			self.flag=flag
			for  i in parse_out:
				if not self.eapolstack.isEmpty() :
					if self.eapolstack.pop() :
						return 

							
				
				string="Message " + str(index) 
				if string.lower() in i[2].lower()  and self.flag :
					print key + " eapol frame is %s" %i[0]
					self.eapol[key] =[i[0],i[1]] 
					self.eapolstack.push (self.flag) 



		
		for i in range (len(list_eapol) ) :
			if i % 2 ==0 :
				self.eapolstack = Stack()
				seqcatcher(list_eapol[i],list_eapol[i + 1],self.flag)	

		if self.flag :
			if not  self.eapol.has_key('first')  :
				Gloabal.comment += "EAPOL MSG 1 FAILURE" 
				Global.result &= False	

			if not self.eapol.has_key('second')  :
				Gloabal.comment += "EAPOL MSG 2 FAILURE"
				Global.result &= False
			
			if not self.eapol.has_key('second')  :
                                Gloabal.comment += "EAPOL MSG 3 FAILURE"
				Global.result &= False

			if not self.eapol.has_key('second')  :
                                Gloabal.comment += "EAPOL MSG 4 FAILURE"
				Global.result &= False 
	

				 
			t=float(self.eapol['four'] [1] ) - float (self.eapol['first'] [1] ) 
			if float(t) < float(1.00) :
				cprint ("EAPOL_HANDSHAKE TAKEN TIME: %s "%t,'green')
				 
			else :
				cprint ("EAPOL_HANDSHAKE TAKEN MORE THAN A SECOND: %s "%t,'red')	
		time.sleep(1)
		return True
			 
	def checkeapolmsg1(self) :
		frame_num=self.eapol['first'] [0]
		flag=True
		cprint ("\n*************************\nValidation of EAPOL-MSG-1 flags and IE's\n*************************\n",'cyan')
                time.sleep(0.5)
		msg_1_key_list = [

				'wlan_rsna_eapol.keydes.key_info.key_ack==0' ,
				'wlan_rsna_eapol.keydes.key_info.key_type==1',
				'wlan_rsna_eapol.keydes.key_info.install == 0',
                		'wlan_rsna_eapol.keydes.key_info.secure == 0',
                		'wlan_rsna_eapol.keydes.key_info.key_mic == 0' ,  
                		'wlan_rsna_eapol.keydes.key_info.install == 0',
                		'wlan_rsna_eapol.keydes.data_len == 0' ,
				]  

		for subfilter in msg_1_key_list :
			filter1= "frame.number == %s &&  %s "%(frame_num,subfilter) 
			status =self._sniff_object.readpacket(filter1) 
			if not len(status)  :
				Global.comment += "Msg1 : " + str(subfilter)+ " is failed \n"
				Global.result &=False
				flag &= False

		return flag
			
		

	def checkeapolmsg2(self) :
		frame_num=self.eapol['second'] [0] 
		flag=True
		cprint ("\n*************************\nValidation of EAPOL-MSG-2 flags and IE's\n*************************\n" ,'cyan')
                time.sleep(0.5)

		msg_2_key_list = [

				'wlan_rsna_eapol.keydes.key_info.key_ack==0' ,
				'wlan_rsna_eapol.keydes.key_info.key_type==1',
				'wlan_rsna_eapol.keydes.key_info.install == 0',
                		'wlan_rsna_eapol.keydes.key_info.secure == 0',
                		'wlan_rsna_eapol.keydes.key_info.key_mic == 1' ,  
                		'wlan_rsna_eapol.keydes.key_info.install == 0',
                		'wlan_rsna_eapol.keydes.data_len !=  0' ,
				]  

		for subfilter in msg_2_key_list :
			filter1= "frame.number == %s &&  %s "%(frame_num,subfilter) 
			status =self._sniff_object.readpacket(filter1) 
		
			if not len(status)  :
				Global.comment += "Msg2 : " +str(subfilter)+ " is failed \n"
				Global.result &=False
				flag &=False
		return flag

	def checkeapolmsg3(self) :
		frame_num=self.eapol['third'] [0] 
		flag=True
		cprint ("\n*************************\nValidation of EAPOL-MSG-3 flags and IE's\n*************************\n",'cyan')
		time.sleep(0.5)
		msg_3_key_list = [

				'wlan_rsna_eapol.keydes.key_info.key_ack==1' ,
				'wlan_rsna_eapol.keydes.key_info.key_type==1',
				'wlan_rsna_eapol.keydes.key_info.install == 1',
                		'wlan_rsna_eapol.keydes.key_info.secure ',
                		'wlan_rsna_eapol.keydes.key_info.key_mic == 1' ,  
                		'wlan_rsna_eapol.keydes.key_info.install == 1',
                		'wlan_rsna_eapol.keydes.data_len != 0' ,
				]  

		for subfilter in msg_3_key_list :
			filter1= "frame.number == %s &&  %s "%(frame_num,subfilter) 
			status =self._sniff_object.readpacket(filter1) 
				
			if not len(status)  :
				Global.comment += "Msg3 : " + str(subfilter)+ " is failed \n"
				Global.result &=False
				flag &= False
		return flag
 
 
	
	def checkeapolmsg4(self) :
		frame_num=self.eapol['four'] [0] 
		flag=True
		cprint ("\n*************************\nValidation of EAPOL-MSG-4 flags and IE's\n*************************\n",'cyan')
                time.sleep(0.5)
		msg_4_key_list = [

				'wlan_rsna_eapol.keydes.key_info.key_ack==0' ,
				'wlan_rsna_eapol.keydes.key_info.key_type==1',
				'wlan_rsna_eapol.keydes.key_info.install == 0',
                		'wlan_rsna_eapol.keydes.key_info.secure == 1',
                		'wlan_rsna_eapol.keydes.key_info.key_mic == 1' ,  
                		'wlan_rsna_eapol.keydes.key_info.install == 0',
                		'wlan_rsna_eapol.keydes.data_len == 0' ,
				]  

		for subfilter in msg_4_key_list :
			filter1= "frame.number == %s &&  %s "%(frame_num,subfilter) 
			status =self._sniff_object.readpacket(filter1) 
		
			if not len(status)  :
				Global.comment += "Msg4 : " + str(subfilter)+ " is failed \n"
				Global.result &=False
				flag &=False

		return flag

	def result(self) :
        	cprint ("\n********************************\n\nTEST-FAIL::\n%s\n\n********************************\n\n"%Global.comment,'red' )
        	sys.exit(0)




'''
if __name__ == "__main__" :
	tuple_args= validation().startup()
	parse_out=validation().parser(tuple_args)
	if not parse_out [0] : 
		cprint ("\n********************************\n\nTEST FAIL : %s\n\n********************************\n\n"%Global.comment,'red' ) 
	else :
		if not validation().checkeapolseq(parse_out) :
			cprint ("\n********************************\n\nTEST FAIL : %s\n\n********************************\n\n"%Global.comment,'red' )
		
		else :
			validation().checkeapolmsg1() 
			validation().checkeapolmsg2()
			validation().checkeapolmsg3()
			validation().checkeapolmsg4()
'''
