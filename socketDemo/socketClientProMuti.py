#coding=utf-8

#模拟并发请求

import socket
import time
import sys

server = ('192.168.0.105',20072)
msg = ['hello','welcome','michael']

socks=[]
for i in range(10):
    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    except socket.error, e:
        print 'Failed to create socket. Error code: ' + str(e[0]) + ' , Error message : ' + e[1]
        sys.exit();
    print 'Socket Created'
    socks.append(sock)

for s in socks:
    s.connect(server)

counter=0
for m in msg:
    for s in socks:
        s.send("The %d send %s"%(counter,m)) #客户端先写消息，发送给服务器
        counter+=1
    for s in socks:
        data = s.recv(1024) #之后接收消息，读消息
        print "%s echo %s"%(s.getpeername(),data) #客户端的名字
        if not data:
            s.close()
    time.sleep(2)