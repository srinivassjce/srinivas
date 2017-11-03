import time

def slow_generator():
     yield [ i for i in range(5) ]

print "starting"
for n in slow_generator():
    print n
print "done"


