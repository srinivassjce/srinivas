#!/usr/bin/python
import sys
cmd_args =sys.argv[1::]

def fact(n) :
	n=int(n)
	if n==1 :
		return 1
	else :
		return int(n) * fact(n-1)	



print fact(cmd_args[0])

