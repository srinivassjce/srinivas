#!/usr/bin/python
import re
import string
def pangarams (a,alphabet) :
 # print ( a ) 
 # print ( alphabet )
  alphaset=set (alphabet)
  stringset = set (a)

  print alphaset
  print stringset


  for i in alphabet :
    c=0
    for s in a :

        if int(ord(i))  ==  int(ord(s)) :
           print ( s + ': letter is present')
           c += 1

    if c == 0  and  ord(i ) > 96 and ord(i) < 123 :
       return 0


def pangrm(a,alphabet) :
	dict1={ i :a.count(i)  for i in a }
	flag=1
	for i in alphabet :
		
		if i not in dict1.keys() :
			flag=0
			break
	
	return flag

		
  
a= raw_input ('Enter a string')
alphabet = string.ascii_lowercase
alphabet = 'abcdefghijklmnopqrstuvwxyz'

a=a.lower()

print '.........................'
#print a

string= str( pangrm (a,alphabet) )

value = re.match (r'1',string,re.I)

print string

if value :
   print "pangrams"

else :
  print  " not "






