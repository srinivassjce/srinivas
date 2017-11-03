#!/usr/bin/python


with  open('userlist.txt', 'r') as target :

	content = target.readlines()
l=[]
for x in content :
	 l.extend( x.rstrip().split(',') )

	

target.close


print  {i : l.count(i) for i in l }



