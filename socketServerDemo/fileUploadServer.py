#coding=utf-8

#服务器端

import socket

server = ('192.168.0.105',20072) #ip+interface

sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #ip地址簇（socket.AF_INET---ip v4 ,socket.SOCK_STREAM--TCP,  socket.SOCK_DGRAM--UDP)

sk.bind(server)
sk.listen(5)

while True:
    conn, address = sk.accept()
    conn.sendall(bytes("欢迎光临",encoding="utf-8"))

    size = conn.recv(1024)
    size_str = str(size,encoding="utf-8")
    file_size = int(size_str)

    conn.sendall(bytes("开始传送", encoding="utf-8"))

    has_size = 0
    f = open("db_new.jpg","wb")
    while True:
        if file_size == has_size:
            break
        data = conn.recv(1024)
        f.write(data)
        has_size += len(data)

    f.close()
    conn.close()

sk.close()