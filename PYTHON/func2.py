#!/usr/bin/python

def func(c=1,d=2,b=1,*a,**z) :
	print 'a:',a
	print 'b:',b
	print 'c:',c
	for k,v in z.items() :
		print k ,v 




l=[1,2,3,4]
func(1,2,*l,sri=1,ranga=2)
