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


try :
	#import constants
	from commonLib import *
	from validation import *

except Exception as err :
	print "unbale to import the library package -%s"%err




if __name__ == "__main__" :
	test_args= validation()
	tuple_args=test_args.startup()
	parse_out=test_args.parser(tuple_args)
	if not parse_out [0] : 
		test_args.result()
	else :
		if not test_args.checkeapolseq(parse_out) :
			test_args.result()		
		else :
			if not test_args.checkeapolmsg1()  :
				test_args.result()
			if not test_args.checkeapolmsg2() :
				test_args.result()
			if not test_args.checkeapolmsg3() :
				test_args.result()
			if not test_args.checkeapolmsg4() :
                                test_args.result()

	if Global.result :
		cprint ("\n********************************\n\nPASS::\n\n********************************\n\n",'green' )
