input1=raw_input('Enter the number')
flag=1
try:
	input1=int(input1)

except (ValueError,KeyError,IndexError,RuntimeError,TypeError) :
	print 'error in input value'
	exit(1)




if input1 == 0 or input1  == 1 :
	print 'input number is not a prime number'
	exit(1)


for i in range( 2,int(input1)/2) :
	if input1 % i == 0 :
		flag=0
		break



if flag==0 :
	print 'non-prime'

else :
	print 'prime'


