#from __future__ import print_function
s=13.4567
x=1
y=2.2
z=3.3
#print s.split('s')
print "Number is %1.4f"%(s)
print "Number is %10.4f"%(s)
print "Number is %5.1f"%(s)


print 'first %s second %1.2f thrid %s'%(x,y,z)

print 'first {x} second{y}  third {z} fourth{x}'.format(x=x,y=y,z=z) 
