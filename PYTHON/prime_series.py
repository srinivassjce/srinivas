input1=raw_input('Enter the total number of elements prime series ')
flag=1
try:
	input1=int(input1)

except (ValueError,KeyError,IndexError,RuntimeError,TypeError) :
	print 'error in input value'
	exit(1)




list1=[]
p=2
i=1
while i <= input1 :
	for j in range(2,int(p)/2,1) :
		if p % j == 0 :
			flag=0
			break
		



	if flag==1 :
		
		list1.append(p)
		p += 1
		i += 1
		
	else :
		flag=1
		p +=1


print len(list1)

print list1

