#!/usr/bin/python

#a=[6 7 3 2]


def insertionsort(a) :
    for i in range(len(a)) :
       
       if i < len(a) - 1 :
           j=i+1
          # print  str (j)
       else :
             j=i
       k=i
       for p in range(k+1) : 
           # print  str(p)
            if  a[j] < a[i]   :
           # swap(a[j],a[i])   
                c=a[j]
                a[j]=a[i] 
                a[i]=c
                if i >= 1 and i < len(a) -1 :
                   #i=i-1
                   #j=i+1
                   print  str (a)
                 #  print "sub i :" +str(i) +':' +str ( a[i] )
                  # print "sub j : " + str(j) +':' +str (a[j] )
                   i=i-1
                   j=i+1
                   #print "sub i :" +str(i) +':' +str ( a[i] )
                   #print "sub j : " + str(j) +':' +str (a[j] )
 
                else :
                    break
            print 'subiteration :' + str(p+1) + ':' + str (a)
            
               


       i=k+1
       print 'iteration :' + str(i) + ':' + str (a)
        
         
       if i == len(a) :
           return a
 


#a=[6,7,3,2,9,8,1,0]

a=[8,3,4,9,10,1,7]

print 'before sorting :' + str (a)
#for i in range(len(a)) :

 #   if i < len(a) - 1 : 
  #     j=i+1
   #    print  str (j)
   # else :
    #   j=i

           # swap(a[j],a[i])   
    #print  str (a[i])  + ":"+ str (a[j])
print 'After sorting :'
print  insertionsort(a)



