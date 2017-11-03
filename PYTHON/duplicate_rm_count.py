#!/usr/bin/python

l=[1,2,2,2,3,3,4,4,5,5,5,6,7,7,1,1,2,2,2,3,3,1,1,1,1]
l1=[l[0],]
l2=[]
dict1={}
for i in l[1::] :
#	print str(i)
     		
	for j in l1:
#	     print 'value of j '+ str(j) + 'comparing with i:' + str(i)
             if j == i :
                     flag=1
#		     print flag	
		     break
             else :
                     flag=0
	
	if flag==1 :
#		print flag,i
		l2.append(i)
	else :
		l1.append(i)

print l
print l1
print l2

dict1= {i: l.count(i) for i in l }
#listing the  number of duplciate elements
print dict1

