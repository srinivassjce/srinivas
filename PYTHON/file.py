#!/usr/bin/python

f=open ('file','r')
s=f.read()
print s
 

#f.seek(0)

list1=[]
for line in f :
    list1.append(line.strip())


print list1
 
