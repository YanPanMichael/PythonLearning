#coding=utf-8

#模拟并发请求

import socket
import time

server = ('192.168.0.105',20072)
msg = ['hello','welcome','michael']

socks=[]
for i in range(10):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socks.append(sock)

for s in socks:
    s.connect(server)

counter=0
for m in msg:
    for s in socks:
        s.send("The %d send %s"%(counter,m))
        counter+=1
    for s in socks:
        data = s.recv(1024)
        print "%s echo %s"%(s.getpeername(),data) #客户端的名字
        if not data:
            s.close()
    time.sleep(2)