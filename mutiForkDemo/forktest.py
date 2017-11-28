import os
import time

def myFork():
    r,w = os.pipe()
    a = 1
    pid = os.fork() #fork() method creats a child process for parent process as well as copy whole resources and open new space in memory
    if pid == 0: #child process id equals 0
        os.close(r)
        w=os.fdopen(w,'w')
        print "this is child process %d--%d**%d" % (pid,os.getpid(),os.getppid())
        for i in xrange(1,100,1):
            w.write(str(a))
            a+=1
            print 'child %s' % str(a)
        w.close()
    else:
        os.close(w)
        r=os.fdopen(r)
        print 'parent %s' % r.read()
        r.close()
        # time.sleep(1)
        print "this is parent process %d--%d**%d" % (pid,os.getpid(),os.getppid())
        # status=os.waitpid(pid,0) # 0 is status code which wait child process finish, 1 is not wait

if __name__ == '__main__':
    myFork()