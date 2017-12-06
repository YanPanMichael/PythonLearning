#coding=utf-8

#netstat -tln
#tcpdump -i 端口号 如en0 作用是监听指定端口

import socket
import select
import Queue
import sys

server = ('192.168.0.105',20072) #ip+interface
try:
    #create an AF_INET, STREAM socket (TCP)
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #ip地址簇（socket.AF_INET---ip v4 ,socket.SOCK_STREAM--TCP,  socket.SOCK_DGRAM--UDP)
except socket.error, e:
    print 'Failed to create socket. Error code: ' + str(e[0]) + ' , Error message : ' + e[1]
    sys.exit();
print 'Socket Created'

sock.setblocking(False)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #复用端口号

sock.bind(server)
sock.listen(10)
# conn,address = sock.accept() #return two objects
rlists = [sock]
wlists = []

msg_que={}
timeout=20
# print 'Connect by ',address
while rlists:
    rs,ws,es = select.select(rlists,wlists,rlists,timeout)
    if not(rs or ws or es):
        print 'time ...'
        continue
    for s in rs:
        if s is sock: #数组只用对头的sock一个对象，则需要开放接受accept客户端发送的请求
            conn, addr=s.accept()
            print 'connect by ',addr
            conn.setblocking(False)
            rlists.append(conn) #将新的对象插在rlists队尾，这时rlists更新，并会对相应的rs进行通知响应
            msg_que[conn]=Queue.Queue() #字典结构，用键值对存储和查找，value值为新的队列
        else: #当前数组中有新的对象
            data = s.recv(1024) #服务器端先接收客户端的消息
            if data:
                print data
                msg_que[s].put(data)
                if s not in wlists:
                    wlists.append(s)
            else:
                if s in wlists:
                    wlists.remove(s)
                rlists.remove(s)
                s.close()
                del msg_que[s]
    for s in ws:
        try:
            msg = msg_que[s].get_nowait()
        except Queue.Empty:
            print 'msg empty'
            wlists.remove(s)
        else:
            s.send(msg)

    for s in es:
        print 'except',s.getpeername()
        if s in rlists:
            rlists.remove(s)
        if s in wlists:
            wlists.remove(s)
        s.close()
        del msg_que[s]