#!/usr/bin/python 

def find_element(array,k,entry) :
	min=0
	entry=int(entry)
	
	while True :
		
		flag=0
		if entry <= array[k] :
			flag=1
			print k
			if array[k] == entry :
				#print k
				return k
			break
		else :
			k += 1
			
	if flag==1 :
		k= k/10
		a=find_element(array,int(k),entry)
		return a
			


array=[ i for i in range(100,2033111,1)]

print find_element(array,1000,121)







