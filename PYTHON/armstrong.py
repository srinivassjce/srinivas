#!/usr/bin/python

i=0
input=9
number=100
list1=[]


while i <= input :
	total=0
	for j in str(number) :
		total += int(j) ** len(str(number))


	if number ==  total :
		list1.append(number) 
		number +=1
		i += 1
	
	else :
		number += 1

	

print list1
