#!/usr/bin/python

a=raw_input ('Enter a string')

count_small=0
count_capital=0
for i in a :
    value= ord(i)
   
#    if value  > 97 and value < 122 :
    if  i.islower() :
       count_small += 1


    if value  > 64 and value < 91 :
       count_capital += 1



print "Count of small letters " + str ( count_small ) 

print "Count of capital letters " + str ( count_capital )

      



