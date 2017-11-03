#!/usr/bin/python

def multiplier() :
    return [lambda num : num * i for i in range (4) ]  

print [ m(2) for m in multiplier() ]


