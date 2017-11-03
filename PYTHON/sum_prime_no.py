#!/usr/bin/python
import re
import sys
def usage() :
	try :
		if len(sys.argv) != 2 :
			print 'usage of program: python '+str (sys.argv[0]) + ' <inputnumber>'
		elif int(sys.argv[1]) == 0 :
			print 'wrong input'
		else :
			pass
		
	except (ValueError,NameError):
		pass


usage()	

def generate_prime(min,max):


	list1=[]
	flag=1
	print max,min
	while int (min) < int (max)  :
		print min
        	for j in range(2,int(min)/2,1) :
                	if min % j == 0 :
                        	flag=0
                        	break
		if flag==1 :
			list1.append(min)

                min +=1
		flag=1

	return list1






min=2
max=sys.argv[1]

print max

list1= generate_prime(min,max)

list1.pop()

print list1

first=list1.pop()

for i in list1 :
	
	if ( int(first)  + int(i) ) == int(max) :
		second=i 
		break
	

print first		  


 

