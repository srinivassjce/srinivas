import socket
import sys
from parser import *

host = 'localhost'
port = 8220
address = (host, port)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(address)
server_socket.listen(5)

print "Listening for client . . ."
conn, address = server_socket.accept()
print "Connected to client at ", address
#pick a large output buffer size because i dont necessarily know how big the incoming packet is                                                    
while True:
    output = conn.recv(2048);
    if output.strip() == "disconnect":
        conn.close()
        sys.exit("Received disconnect message.  Shutting down.")
        conn.send("dack")
    elif output:
        print "Message received from client:"
        print output
	p=Parser(output)
	
	result,message_dict=p.check_message()
	if result :
		conn.send("ack")
		#execute_command(message_dict)
		
