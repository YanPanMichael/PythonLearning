#coding=utf-8

#netstat -tln
#tcpdump -i 端口号 如en0 作用是监听指定端口

import socket

server = ('192.168.0.105',20072) #ip+interface

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #ip地址簇（socket.AF_INET---ip v4 ,socket.SOCK_STREAM--TCP,  socket.SOCK_DGRAM--UDP)
sock.bind(server)
sock.listen(5)
conn,address = sock.accept() #return two objects
print 'Connect by ',address
while True:
    data = conn.recv(1024) #bufsize max value
    if not data: break
    print data
    conn.send(data)
sock.close()