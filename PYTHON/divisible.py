#!/usr/bin/python
low=raw_input('Enter a low range')
high=raw_input('Enter a high range')
print 'Program to print numbers b/w '+ low  + ' and ' + high + 'divisible by 7 and not divible by 5'

for i in range (int(low),int(high)) :
	if i % 7 == 0  and i % 5 > 0 :
		print i

print  'second solution'
num1= int (low) %7 
low= int (low) -num1
num2=int (high) %7
high=int (high)  + num2

print low , high

for i in range (int(low),int(high),7) :
        if i % 5 > 0 :
                print i

print high
print 'third soln'
a=set()
b=set()
for i in range(int(low),int(high),7) :
	a.add(i)

for i in range(int(low),int(high),35) :
	b.add(i)

c=tuple( a - b )
list1=[]

f=[ list1.append(i)  for i in c ]
list1.sort()
print list1

print len(list1) 


