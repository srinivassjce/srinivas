#!/usr/bin/python

def extendList ( val ,list=[] ) :
 #   print 'list' + str (list ) + ' value' + str (val)

    list.append(val)
#    print 'list' + str (list ) + ' value' + str (val)
    return list


print extendList(10)
print extendList(123,[])
print extendList('a')

list1=extendList(10)
list2=extendList(123,[])
list3=extendList('a')

print "list1 = %s " % list1 
print "list2 = %s " % list2
print "list3 = %s " % list3

