import socket
def checkbinary(inpt) :
        a=set(inpt)
	b=list(a)
	a=''
	for i in range(len(b)) :
		a += b[i]

        if a=='01' or a == '10' :
                return 1
        else :
                return 0

def paritycheck(iput) :
        a=list(iput)
	print a
	paritybit=a.pop()
        print  a.count('1')
	print paritybit 

        if paritybit =='0'  and int(a.count('1')) % 2 == 0  :
                return 1
	elif paritybit == '1'  and int (a.count('1')) % 2 == 1  :
		return 1
        else :
               return 0


s = socket.socket()
host = socket.gethostname()
print host
port = 1247
s.bind((host,port))
s.listen(5)
while True:
    c, addr = s.accept()
    print 'c'+ str(c)
    print 'addr' + str(addr) 
    print("Connection accepted from " + repr(addr[1]))

    c.send("Server approved connection\n")
    #print repr(addr[1]) + ": " + c.recv(1026)
    inpt=c.recv(1026)
    #inpt=s(inpt)
    print inpt 	
    result=1
    result=checkbinary(inpt)
    if result == 0 :
	print 'Entered value is not binary'
	exit(1)

    result=paritycheck(inpt)
    if result== 0 :
	print 'ERROR DATA'
    else	:
	print 'Pairty check is fine and data can be processed'			   	
    c.close()


