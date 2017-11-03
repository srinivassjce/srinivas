#!/usr/bin/python

def runlengthCode (text) :
	list1=list(text)
	print list1
	res=''
	count=1
	start=1
	d=1
	i=0
	finallist=[]
	while True :
	
		for j in range ( start, len(list1)) :
                        if  list1[j] == list1[i]  :
                                        count += 1
                                        print list1[i] , list1[j],count

                        else :

                                d=j
                        #       count=1
				print 'value of d',d
				print 'break'
                                break;
		print 'after break'
		if count > 4 :
			res +=  '\\'+ str(count) + str(list1[i])
			start=d +1 
			i=d
			print start
			count=1
		elif count <= 4 :
			res += str( list1[i] * count ) 
			print  'less than 4  ',list1[i] ,count
			start=d+1
			i=d
			
			
 		print 'start',start,i	
		max=len(list1) - 1
		i=i + 1 
				 		

			
		if i == max :
			return res
		



def runLengthEncode (plainText):
    res=''
    a=''
    count = 0
    for i in plainText:
        count+=1
	print a,len(plainText),res,i,count	
        if a.count(i)>0:
            a+=i
        else:
            if len(a)>4:
                if len(a)<10:
                    res+="/0"+str(len(a))+a[0][:1]
                else:
                    res+="/" + str(len(a)) + a[0][:1]
                a=i
            else:
                res+=a
                a=i
        if count == len(plainText):
            if len(a)>4:
                if len(a)<10:
                    res+="/0"+str(len(a))+a[0][:1]
                else:
                    res+="/" + str(len(a)) + a[0][:1]
            else:
                res+=a
    return(res)


print runlengthCode('sssssaaaatt')




