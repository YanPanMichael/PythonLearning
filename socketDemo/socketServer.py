#coding=utf-8

#netstat -tln
#tcpdump -i 端口号 如en0 作用是监听指定端口

import socket
import sys

server = ('192.168.0.105',20072) #ip+interface

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #ip地址簇（socket.AF_INET---ip v4 ,socket.SOCK_STREAM--TCP,  socket.SOCK_DGRAM--UDP)

try:
    sock.bind(server)
except socket.error, e:
    print 'Bind failed. Error Code : ' + str(e[0]) + ' Message ' + e[1]
    sys.exit()
print 'Socket bind complete'

sock.listen(5)

#now keep talking with the client
while True:
    conn, address = sock.accept() #return two objects
    #display client information
    print 'Connected with ' + address[0] + ':' + str(address[1])

    if conn not sock: break
    
    while True:
        data = conn.recv(1024) #receive data, bufsize max value
        if not data: break
        print data
        conn.send(data)

    conn.close()

sock.close()