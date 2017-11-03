#!/usr/bin/python

def biggest_3(a) :
	a.sort()
	print a
	maxi=len(a)
	list1=[]
		#print a[i]
	try :
		zeroindex=  a.index(0) 
	except :
		print 'No Entry of 0 in list'
		zeroindex=  0
	
	if zeroindex :
			a.pop(zeroindex)
			maxi=len(a)
			print a

	if (a[0] * a[1]) > (a[maxi-1] * a[maxi-2] ) :	
		list1.append(a[0]) 
		list1.append(a[1]) 
		flag=0
	else :
		list1.append(a[maxi-1]) 
		list1.append(a[maxi-2])
		flag=1


	if flag==0  and a[maxi-1] > 0:
		list1.append(a[maxi-1] )

	elif flag==0  and a[maxi-1] < 0 :
		list1.pop()
		list1.pop()

		list1=[a[maxi-1],a[maxi-2],a[maxi-3]]



	else :
		list1.append(a[maxi-3])

	return list1




a=[1,-1,0,-10,-1,-2,-3,-4,-4,-5,-6,-3,-4,-5,-5]

l=biggest_3(a)
print l
print ' MUl of three numbers : ' + str ( reduce( lambda x,y:x*y,l))







