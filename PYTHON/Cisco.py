#!usr/bin/python
import re
import requests
#from pexpect import pxssh
from datetime  import datetime
import json
import requests
from resourceFile import Cisco1200_AP1,Cisco1200_AP2

def main() :
	devicelist=[Cisco1200_AP1,Cisco1200_AP2]
	start_time=datetime.now()
	print 'elased _timei {} '.format (datetime.now()-start_time)
  	print __name__
	print start_time 
	print devicelist[0] ['username']









if __name__ ==  '__main__' :
	main()










