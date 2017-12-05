#coding=utf-8

#netstat -tln
#tcpdump -i 端口号 如en0 作用是监听指定端口

import socket
import sys
from thread import *

server = ('192.168.0.105',20072) #ip+interface

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #ip地址簇（socket.AF_INET---ip v4 ,socket.SOCK_STREAM--TCP,  socket.SOCK_DGRAM--UDP)
print 'Socket Created'

try:
    sock.bind(server)
except socket.error, e:
    print 'Bind failed. Error Code : ' + str(e[0]) + ' Message ' + e[1]
    sys.exit()
print 'Socket bind complete'

sock.listen(5)
print 'now socket listening'

#Function for handling connections. This will be used to create threads
def clientthread(conn):
    #Sending message to connected client
    conn.send('Welcome to the server. Type something and hit enter\n') #send only takes string
     
    #infinite loop so that function do not terminate and thread do not end.
    while True:
        #Receiving from client
        data = conn.recv(1024)
        reply = 'OK...' + data
        if not data: 
            break
        conn.sendall(reply)
    
    #came out of loop
    conn.close()

#now keep talking with the client
while True:
    conn, address = sock.accept() #return two objects
    #display client information
    print 'Connected with ' + address[0] + ':' + str(address[1])
    
    #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    start_new_thread(clientthread, (conn,))

sock.close()