#!/usr/bin/python


def runLengthEncode (plainText):
    res=''
    a=''
    tmp=''	
    for i in plainText:
	print  tmp ,i ,a , a.count(i),res 
        if a.count(i)>0  :
            a+=i
        else:
            if len(a)>4  :
                res+="/" + str(len(a)) + tmp
		a =''
		tmp =i
		#yield res
            else:
                res+=i
		a +=i
		tmp=i


    return(res)


print runLengthEncode('sssssaaaa')




