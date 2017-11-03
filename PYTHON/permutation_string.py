#!/usr/bin/python
import re
def permut(a) :
	list1=[]	
	list2=[]
	str2=''
	str1=''	
	for i in range(len(a)) :
		if int(i)  !=  0 :
			str1 += a[i-1] 
		
		a=a[i:]
		b=a
		for p in range(len(b)-i ) :
			for j in a:
				str2 +=  j
			s=str1 + str2
			a =  a [(i+1):] + a[i] 
			print a
			list1.append(s)
			str2=''
		
	return list1			


def swap(a) :
	pass
	

def permut(a) :
	list1=[]
	print [ p+q+r  for (p,q,r) in re.findall(r'(.)(.)(.)',a)  ]	
		
	
	return list1



a='xyz'
print permut(a)


