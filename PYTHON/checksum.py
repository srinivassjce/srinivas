#!/usr/bin/python
import re
filename='ip_header.txt'
f=open(filename,'r') 
line=f.readline()

list1=re.split(',|\n|\r',line)
sum=0

for i in  list1 :
	sum += int(i,32)

 
print hex(sum)
