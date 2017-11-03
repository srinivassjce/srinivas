#!/usr/bin/python
from csv import reader
try :
	with open('file1.csv','r') as csvfile:
		csvreader=reader(csvfile,delimiter=',')
		for row in csvreader :
			print row


	 


except IOError :
	print 'failed to open the file'


