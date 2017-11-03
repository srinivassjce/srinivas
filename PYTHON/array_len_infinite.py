#!/usr/bin/python 

def find_element(array,k,k1,entry) :
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
			k += k1
			
	if flag==1 :
		if  k == k1  :
			k= k/10 
			k1 = k
		if  k > k1 :
			k = k - k1 
			k1=k1/10
		a=find_element(array,int(k),k1,entry)
		return a
			


array=[ i for i in range(1,2033111,1)]

print find_element(array,1000,1000,2978)







