import socket

def checkbinary(inpt) :
	a=set(inpt) 
	b=list(a)
	a=''
	for i in range(len(b)) :
		a += b[i]	
	
	print a		

	if a=='01' or a == '10' :
		return 1
	else :
		return 0

def addparity(iput) :
	a=list(iput)
	count_1 =a.count('1')
	print a
	print 'count of 1 are ' + str(count_1)
	if count_1 % 2 == 0 :
		a.append(0)
	else :
		a.append(1)
	b=a
	a=''
        for i in range(len(b)) :
                a += str (b[i])

        print a

	return a

def dividesegments(iput,seglen) :
	a=list(iput)
	for i in range(len(iput)) :
		for j in range(seglen) :
			


s = socket.socket()
host =socket.gethostname()
port = 1247
s.connect((host, port))
print s.recv(1024)
inpt = raw_input('enter binary input and click enter... ')
result=checkbinary(inpt) 
while 1 :
	if result == 0 :
		inpt = raw_input('Entered binary input is wrong  and kinldy reeneter binary input followed by enter... ')
		result=checkbinary(inpt)
	else :
		break

inpt=addparity(inpt) 
print 'Sending data after parity check is ' + str (inpt) 
s.send(inpt)
print "the message has been sent"
