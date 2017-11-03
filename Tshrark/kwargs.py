#!/usr/bin/python

def func1(n,*args) :
	print "number is %s"%n
	print "rest of argumnets are ",args


def func2(*args) :
	print "reading all argumnets ",args


def func3(a,**kwargs) :
	print "reading arguments  ",kwargs

def func4(n,*a,**k) :
	print "hi"
	print a
	print k


def func1(*a,**d) :
	print a
	print d

if __name__ == "__main__" :
	number=1
	boo=True
	string="srinivas"
        list1=[1,2,3,4,5]
        dict1={
                'srini' :1 ,
                'bambdev':2,
        }

        func4('up','hi','hello','welcome',a=1,b=2,c=3)





