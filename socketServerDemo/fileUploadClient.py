#coding=utf-8

import socket
import os

server = ('192.168.0.105',20072) #ip+interface

obj = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #ip地址簇（socket.AF_INET---ip v4 ,socket.SOCK_STREAM--TCP,  socket.SOCK_DGRAM--UDP)

obj.connect(server)

ret_bytes = obj.recv(1024)
ret_str = str(ret_bytes, encoding="utf-8")
print "server received data are: %s" %ret_str

size = os.stat("yan.jpg").st_size
obj.sendall(bytes(str(size), encoding="utf-8"))

obj.recv(1024)

with open("yan.jpg", "rb") as f:
    for line in f:
        obj.sendall(line)