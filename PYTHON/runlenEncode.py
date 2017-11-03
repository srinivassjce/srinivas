#!/usr/bin/python
import re

def runlenEnocde(text) :

#	s=re.findall(r'(.)\1*',text)
	s = [match[1] + match[0] for match in re.findall(r"(.)(\1*)", text)]
	print text
	list1=[]
	t=''
	for i in s:
		if i.count(i[0])  >= 5 :
			count=i.count(i[0])
			t +="0x"+ str(count)  + str (i[0]) 
			list1.append(t) 
		else :
			list1.append(i)
			t+=str(i)
	
			
	return t
	









print runlenEnocde(raw_input('Enter a string : ') )


