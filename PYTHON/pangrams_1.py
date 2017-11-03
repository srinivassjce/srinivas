#!/usr/bin/python 
import string
a=raw_input("enter string to check pangram \n")

#print a
print 'validation of pangram'
asc=string.ascii_lowercase

print asc

a=set(a.lower())
b=set(asc)

#print a
#print b
if  len ((a & b) ) == int(26) :
	print 'pangram'
else :
	print 'non pangram'




