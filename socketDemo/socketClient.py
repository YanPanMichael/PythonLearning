import socket
import sys

host = 'www.google.com'

server = ('192.168.0.105',20072)

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    remote_ip = socket.gethostbyname(host)
except socket.gaierror:
    #could not resolve
    print 'Hostname could not be resolved. Exiting'
    sys.exit()
print 'Ip address of ' + host + ' is ' + remote_ip

sock.connect(server)

try :
    #Set the whole string
    sock.send("hello")
except socket.error:
    #Send failed
    print 'Send failed'
    sys.exit()
print 'Message send successfully'

data = sock.recv(1024)
print 'echo',data

sock.close()