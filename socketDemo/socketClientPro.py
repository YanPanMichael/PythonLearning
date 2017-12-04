#coding=utf-8

#模拟并发请求 不可同时启动多个客户端同时发送请求 服务器端因为有close所以也不能作为一个伺服器

import socket
import time

server = ('192.168.0.105',20072)
msg = ['hello','welcome','michael']

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(server)
for m in msg:
    sock.send(m)
    data = sock.recv(1024)
    print 'echo',data
    time.sleep(2)

sock.close()